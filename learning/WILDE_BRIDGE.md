# From Wilde's quantum information theory to spatial Markov stability

Imagine preparing neighboring pairs of spins and then measuring the spins between two distant endpoints. The endpoint state averaged over the outcomes can be completely uncorrelated, while the retained measurement record reveals a correlation. The project asks whether this dependence can persist through an arbitrarily wide intervening region when a circuit on a one-dimensional line has bounded depth and range, begins with uniformly full-rank product states, and preserves full rank uniformly.

The [theorem](../science/model.md#4-quantitative-theorem) gives exponential decay of conditional mutual information under those preparation assumptions. This bridge connects the selected textbook to the argument through small complete examples. The [30-milestone map](MILESTONES.md) supplies the understanding targets; the linked `science/` pages remain the authoritative statements and proofs.

## The selected source and a focused reading route

The educational anchor is **Mark M. Wilde, _Quantum Information Theory_, second edition, Cambridge University Press, 2017**, ISBN 9781107176164, [DOI](https://doi.org/10.1017/9781316809976). The publisher's [front matter](https://assets.cambridge.org/97811071/76164/frontmatter/9781107176164_frontmatter.pdf) verifies the edition; its [contents](https://assets.cambridge.org/97811071/76164/toc/9781107176164_toc.pdf) verifies the following section starts.

| Foundation | Selected 2017 edition | Use in this project |
|---|---|---|
| States and composite systems | §§4.1, 4.3; pp. 102, 117 | Spectral floors, partial traces, independent resources |
| Channels | §§4.4–4.7; pp. 129, 141, 143, 154 | CPTP maps, Choi operators, environments, measurement channels |
| Purification and isometries | §§5.1–5.2; pp. 165, 168 | Representing a resource through an internal channel |
| Entropy and conditional entropy | §§11.1, 11.4; pp. 301, 311 | Information quantities and conditional-entropy arguments |
| Mutual and conditional mutual information | §§11.6–11.7; pp. 315, 318 | Chain rules, strong subadditivity, dimension bounds |
| Relative entropy and inequalities | §§11.8–11.9; pp. 321, 327 | Data processing and conditional-information bookkeeping |
| Entanglement and unit protocols | §§3.6, 6.2; pp. 81, 188 | Bell states and the worked swapping example |

Use these sections alongside the argument; reading the whole book is unnecessary. In particular, §4.4 supplies the Choi–Kraus framework, and §11.7 supplies the conditional-information relationships used repeatedly below.

An accessible [author manuscript](https://www.markwilde.com/qit-notes.pdf), titled _From Classical to Quantum Shannon Theory_, is dated **5 December 2021**. It provides an access route to this source, but its pagination differs: for example, §11.7 begins on its printed p. 335, whereas it begins on p. 318 in the selected 2017 edition. All page pointers in the table refer to the **2017 published edition**. Section-level references avoid silently transferring equation or exercise numbering between versions. The book is linked, not redistributed here.

## Translate notation and units first

This supports [M01–M09](MILESTONES.md#m01).

Wilde writes entropy in bits, using base-two logarithms. The project writes entropy as $`S`$ and uses natural logarithms:

```math
S(\rho)=-\mathrm{Tr}(\rho\ln\rho)
=(\ln2)H_{\mathrm{bits}}(\rho).
```

The same conversion applies to mutual information, conditional mutual information, and relative entropy:

```math
I_{\mathrm{nats}}=(\ln2)I_{\mathrm{bits}},
\qquad
D_{\mathrm{rel,nats}}=(\ln2)D_{\mathrm{rel,bits}}.
```

Consequently a dimension bound written as $`2\log_2 d`$ bits becomes $`2\ln d`$ nats. Multiplicative contraction factors such as $`1-p`$ are unchanged. Changing information units also leaves unchanged the spatial length extracted from exponential decay.

| Book object or convention | Project notation and role |
|---|---|
| $`H(A\mid B)=H(AB)-H(B)`$ | $`S(A\mid B)=S(AB)-S(B)`$, measured in nats |
| $`I(A;C\mid B)`$ | $`I(A:C\mid B)`$; the semicolon/colon change has no mathematical effect |
| A channel $`\mathcal N`$ | $`\Phi_g`$ for a physical gate; $`\mathcal E`$ for a boundary map; $`\mathcal T`$ for the internal resource channel |
| A finite-dimensional register | A physical site has dimension at most $`d`$; a memory or virtual register can contain several sites |
| Relative entropy $`D(\rho\Vert\sigma)`$ | Written $`D_{\mathrm{rel}}`$ here when needed, to distinguish it from circuit depth $`D`$ |
| Choi operator from an unnormalized entangled vector | $`\Gamma^{\mathcal T}`$, with partial trace equal to the input identity |

For the last row, if $`V`$ has dimension $`d_V`$, the unnormalized vector is $`|\Gamma\rangle=\sum_j|j\rangle|j\rangle`$. A trace-preserving channel has $`\mathrm{Tr}\Gamma^{\mathcal T}=d_V`$. The normalized Choi **state** would be $`\Gamma^{\mathcal T}/d_V`$. These two objects have different eigenvalues; the distinction matters when converting an eigenvalue floor into a replacement weight.

## A complete example of conditional information

This illustrates [M08](MILESTONES.md#m08) and [M09](MILESTONES.md#m09).

Let $`A`$ and $`C`$ be independent fair classical bits, and store their parity in a third register, $`B=A\mathbin{\oplus}C`$. The four pairs $`(A,C)`$ occur with probability $`1/4`$. Thus

```math
S(A)=S(C)=S(B)=\ln2,
\qquad S(AC)=2\ln2,
```

```math
S(AB)=S(BC)=S(ABC)=2\ln2.
```

The endpoints are independent, but knowing the parity tells whether they agree:

```math
I(A:C)=0,
\qquad
I(A:C\mid B)=2\ln2+2\ln2-\ln2-2\ln2=\ln2.
```

This classical calculation is also a quantum-state calculation for a density matrix diagonal in the corresponding basis. In the general theorem the conditioning register can be quantum; it is not implicitly measured.

Operations on the conditioning register need separate care. For another simple state, let $`A`$, $`B`$, and $`C`$ hold the **same** fair classical bit. Then $`I(A:C\mid B)=0`$, but discarding $`B`$ leaves $`I(A:C)=\ln2`$. Endpoint data processing therefore cannot be applied to an operation on $`B`$. The [arbitrary-cut proof](../science/spatial-decay.md#3-arbitrary-positions-of-the-cuts) handles changes to a buffer by an explicit chain rule instead.

## From a faithful resource to contraction

The bridge from textbook tools to the local mechanism is [M13–M16](MILESTONES.md#m13).

Take a fresh state $`\sigma_{LMR}`$, independent of an incoming state $`\omega_{ABX}`$. Here $`A`$ is a reference, $`B`$ is an already emitted record, and $`X`$ is the incoming memory. A boundary channel acts on $`XL`$, emits $`Y`$, and leaves $`R`$ as the new memory. The untouched middle register $`M`$ is emitted as well.

The useful resource condition is

```math
\sigma_{LMR}\ge p\,\sigma_{LM}\otimes\sigma_R,
\qquad 0\lt p\le1.
```

The symbol $`\ge`$ is positive-operator order: subtracting the right side leaves a positive operator. A full-rank resource supplies at least $`p=\lambda_{\min}(\sigma)`$, because $`\sigma\ge\lambda_{\min}(\sigma)I`$ and $`\sigma_{LM}\otimes\sigma_R\le I`$. This is a sufficient coefficient and can be conservative.

The [resource lemma](../science/contraction.md#2-resource-contraction-lemma) then states

```math
I(A:R\mid BYM)\le(1-p)I(A:X\mid B).
```

The strict factor comes from the fresh resource. The boundary map itself can be an arbitrary CPTP map.

### Why averaging works in this particular argument

For $`p\lt 1`$, write the resource as a mixture of its product component and

```math
\tau=\frac{\sigma-p\,\sigma_{LM}\otimes\sigma_R}{1-p}.
```

The two components have the same $`LM`$ marginal. Therefore their emitted $`ABYM`$ marginals after the boundary operation are identical. In

```math
I(A:R\mid BYM)=S(A\mid BYM)-S(A\mid BYMR),
```

the first term is fixed across the components and their mixture. Concavity of the second conditional entropy supplies the required inequality. The product component contributes zero retained conditional information. This is the precise connection to Wilde's conditional-entropy tools; it does not assert general convexity of CMI. The complete proof and the residual-component data-processing step are in the [canonical lemma](../science/contraction.md#2-resource-contraction-lemma).

### Identify the internal channel

For the full-rank resources used here, put $`Q=LM`$. Its marginal $`\sigma_Q`$ is full rank as well. Diagonalize $`\sigma_Q`$ and purify it using a copy $`V`$ in that eigenbasis. The channel representing $`\sigma_{QR}`$ has unnormalized Choi operator

```math
\Gamma^{\mathcal T}
=(\sigma_Q^{-1/2}\otimes I_R)
\sigma_{QR}
(\sigma_Q^{-1/2}\otimes I_R).
```

Its partial trace over $`R`$ is $`I_V`$. The resource inequality becomes

```math
\Gamma^{\mathcal T}\ge p\,I_V\otimes\sigma_R,
\qquad
\mathcal T=p\mathcal R_{\sigma_R}+(1-p)\mathcal T_1,
```

where $`\mathcal R_{\sigma_R}(Z)=\mathrm{Tr}(Z)\sigma_R`$ is a replacement channel and $`\mathcal T_1`$ is CPTP when $`p\lt 1`$. This is completely positive order, so the statement remains valid with arbitrary reference systems.

The conditional Doeblin implication and sequential iteration are inherited research ingredients, credited to [CKB23 and HGNW26](../science/contraction.md). Wilde supplies their channel and entropy foundations; the [internal-channel derivation](../science/contraction.md#4-reduction-to-an-internal-doeblin-channel) supplies the resource connection used here. A physical boundary map might send $`X`$ perfectly into $`Y`$, so its **whole-output** contraction coefficient can be one. The coefficient required here belongs to $`\mathcal T_{V\to R}`$.

## Two noisy Bell links worked through

This connects the local mechanism to [M28](MILESTONES.md#m28). The [general chain example](../science/examples-and-limits.md#an-exactly-solvable-chain-with-conditional-correlations) is the authoritative extension.

Use four qubits in spatial order $`A,X,L,R`$, initially $`I_{16}/16`$. In the first layer, replace each pair $`AX`$ and $`LR`$ by

```math
\sigma_v=v|\Phi^+\rangle\langle\Phi^+|+(1-v)I_4/4,
\qquad
|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2.
```

Set $`v=1/2`$. A pair-replacement channel sends $`I_4`$ to $`4\sigma_{1/2}\ge I_4/2`$, so it is faithful with $`\alpha=1/2`$. The initial one-qubit floor is $`\delta=1/2`$.

In the second layer, measure the middle pair $`XL`$ in the Bell basis, consisting of $`(|00\rangle\pm|11\rangle)/\sqrt2`$ and $`(|01\rangle\pm|10\rangle)/\sqrt2`$. Store the outcome $`j`$ in the two-qubit register $`Y`$:

```math
\mathcal E(Z)=\sum_{j=0}^3
\langle\beta_j|Z|\beta_j\rangle\,|j\rangle\langle j|_Y.
```

Its Kraus operators $`|j\rangle\langle\beta_j|`$ show that it is trace preserving and unital. All four outcomes are kept as a classical record. The physical buffer is this middle pair; no outcome is selected. The preparation is a depth-two, range-two circuit in the stated model.

For one link, both one-qubit marginals are $`I_2/2`$. Hence the internal Choi operator and channel are

```math
\Gamma^{\mathcal T_v}=2\sigma_v,
\qquad
\mathcal T_v(Z)=vZ+(1-v)\mathrm{Tr}(Z)I_2/2.
```

The replacement weight is $`p=1-v=1/2`$. By comparison, the simple smallest-eigenvalue choice gives only $`\lambda_{\min}(\sigma_{1/2})=1/8`$.

To compute the output exactly, label the four Bell states by Pauli errors modulo phase. A link has error distribution

```math
p_v=v\delta_0+(1-v)u,
```

where $`u`$ is uniform on the four labels. Bell swapping adds the two independent error labels, together with a correction determined by the recorded outcome. Since $`u*u=u`$ and $`u*\delta_0=u`$,

```math
p_v*p_v=v^2\delta_0+(1-v^2)u=p_{v^2}.
```

Each Bell outcome is uniform, and, conditioned on that outcome, the endpoints have state $`\sigma_{1/4}`$ up to a local Pauli. The eigenvalues are $`7/16,3/16,3/16,3/16`$. A classical conditioning record makes CMI the average branch mutual information, and local Paulis leave entropy unchanged. Therefore

```math
\begin{aligned}
I(A:R\mid Y)
&=2\ln2-S(\sigma_{1/4})\\
&=\frac7{16}\ln\frac74+\frac9{16}\ln\frac34\\
&\approx0.08301074\text{ nats}.
\end{aligned}
```

The input link has

```math
I(A:X)=\frac58\ln\frac52+\frac38\ln\frac12
\approx0.31275151\text{ nats}.
```

The resource lemma predicts $`I(A:R\mid Y)\le\tfrac12 I(A:X)\approx0.15637576`$ nats, consistent with the exact value. If the record is ignored, the endpoint marginal is $`I_4/4`$ and its mutual information is zero. The example therefore displays both the relevant conditional dependence and its contraction. The [finite verifier](../verification/README.md) checks the general example against density-matrix calculations.

## Regroup five nonunitary gates

The spatial step, [M17–M21](MILESTONES.md#m17), builds on the circuit and memory setting of [M10–M12](MILESTONES.md#m10) and requires an additional argument beyond the textbook's channel composition rules. Consider depth $`D=2`$, range $`r=2`$, so $`w=4`$ and $`K=17`$. Divide a 34-site chain between sites 17 and 18. Use the following five gates, with identities elsewhere:

| Gate | Layer | Actual support | Initial wires in its backward cone | Coarse group |
|---|---:|---|---|---|
| $`g`$ | 1 | $`\{17,18\}`$ | $`\{17,18\}`$ | Boundary |
| $`h`$ | 1 | $`\{22,23\}`$ | $`\{22,23\}`$ | Right block |
| $`a`$ | 2 | $`\{18,19\}`$ | $`\{17,18,19\}`$ | Boundary |
| $`b`$ | 2 | $`\{15,16\}`$ | $`\{15,16\}`$ | Left block |
| $`c`$ | 2 | $`\{22,23\}`$ | $`\{22,23\}`$ | Right block |

Every gate may be a nonunitary CPTP map satisfying the model's faithfulness bound. Gate $`a`$ acts entirely inside the right block, but it follows $`g`$ along wire 18. Its cone crosses the boundary, so it must remain in the boundary group. Grouping only by a gate's immediate support would miss that dependency.

The first coarse layer is

```math
\mathcal F_L=\Phi_b,
\qquad
\mathcal F_R=\Phi_c\circ\Phi_h,
```

and the second coarse layer is $`\mathcal E=\Phi_a\circ\Phi_g`$. All maps are extended by identities on their unused sites. Moving $`b`$ earlier passes only gates with disjoint supports; the order $`h`$ before $`c`$ and $`g`$ before $`a`$ is preserved. Thus the original channel is exactly

```math
\mathcal C=\mathcal E\circ(\mathcal F_L\otimes\mathcal F_R).
```

This equality uses neither inverse channels nor commutation of overlapping gates. The boundary supports lie in the permitted strip $`\{14,\ldots,21\}`$. The [general DAG proof](../science/circuit-regrouping.md) uses ancestor-closed sets to perform this construction uniformly along a chain.

## Assemble the spatial bound

The final connection is [M20–M26](MILESTONES.md#m20). Return to the general parameters $`w=Dr`$ and $`K=4Dr+1`$. A $`K`$-site input block has floor $`\delta^K`$. Applying a gate to a state bounded below by $`\lambda I`$ leaves a lower bound $`\lambda\alpha I`$. At most $`KD`$ original gates enter one block preparation, giving

```math
\sigma_i\ge p_0 I,
\qquad p_0=\delta^K\alpha^{KD}\gt 0.
```

The product input and disjoint first coarse layer make these block resources independent. Each subsequent spatial step emits a complete $`K`$-site cell and retains at most $`w=Dr`$ sites of memory. The resource lemma contracts the remaining conditional information by $`q=1-p_0`$ per complete cell. The memory dimension supplies a $`2w\ln d`$ prefactor for aligned cells.

For an arbitrary physical buffer, the proof moves its two partial end cells into enlarged endpoints by a chain-rule inequality. A separate cut bound covers buffers containing no complete cell. The [result](../science/spatial-decay.md) is

```math
I(A:C\mid B)\le4Dr\ln d\,
(1-p_0)^{\max\{0,\lfloor |B|/K\rfloor-2\}}.
```

The key uniformity is that the prefactor and decay factor do not depend on the endpoint sizes or total chain length. The canonical proof also treats two-sided shields and infinite-line limits. Its constants are sufficient bounds, not optimized physical correlation lengths.

## Keep the assumptions attached to their roles

This completes the connections to [M29](MILESTONES.md#m29) and [M30](MILESTONES.md#m30).

| Assumption or distinction | Role in the argument |
|---|---|
| Product input and independent gate environments | Give independent first-layer block resources |
| Fixed depth, finite range, bounded site dimension | Give bounded blocks, disjoint boundary strips, and bounded memory |
| Uniform input and gate spectral floors | Give one positive $`p_0`$ for the entire family |
| Trace-preserving evolution | Supports unchanged-marginal and data-processing steps |
| Internal channel versus whole emitted output | Locates the strict contraction where the proof actually needs it |
| Open or infinite one-dimensional line | Supplies the spatial ordering and geometry used in the construction |

Individual full rank without a common lower bound does not provide a uniform length. Rank loss invalidates this guarantee but need not cause a divergence: complete reset can produce a product state. Interacting initial Gibbs states, shared unmodeled environments, postselection, rings, and exact extensive continuous-time dynamics change hypotheses used in the proof. Their status is explained in [examples and boundaries](../science/examples-and-limits.md), rather than inferred from the present result.

The complete scientific route is [model](../science/model.md) → [resource contraction](../science/contraction.md) and [causal regrouping](../science/circuit-regrouping.md) → [spatial decay](../science/spatial-decay.md). The [related-work account](../references/comparison.md) identifies inherited ingredients and the precise preparation-level consequence.
