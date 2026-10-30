# Model and main result

We consider spatial conditional mutual information in states prepared by local quantum channels on a one-dimensional line. The input is a product of uniformly full-rank states. The channels may be coherent, nonunital, and strongly dissipative, subject to a uniform condition that they preserve full rank.

The proof uses established conditional data-processing and sequential-channel arguments. Its circuit construction and the quantitative spatial bounds are developed in [circuit-regrouping.md](circuit-regrouping.md), [contraction.md](contraction.md), and [spatial-decay.md](spatial-decay.md).

## 1. Sites, gates, and depth

The tensor product is the ordinary qudit tensor product. The locality assumptions refer to maps supported on those tensor factors. No separate claim about fermionic locality conventions or parity constraints is made.

For a finite open chain, let

$$
\Lambda=\{1,\ldots,n\},\qquad
\mathcal H_\Lambda=\bigotimes_{x=1}^n\mathcal H_x,
\qquad 1\le \dim\mathcal H_x\le d,
$$

where the integer bound $d\ge 2$ is independent of $n$. The case in which every site is one dimensional is trivial.

A gate $g$ is a completely positive trace-preserving map

$$
\Phi_g:\mathcal B(\mathcal H_{S_g})\longrightarrow
\mathcal B(\mathcal H_{S_g})
$$

on a nonempty set of sites $S_g$. For a positive integer $r$, its range is bounded by $r$ if

$$
\max S_g-\min S_g+1\le r.
$$

The set $S_g$ need not contain every site in its interval hull. In each circuit layer, the actual supports $S_g$ are pairwise disjoint. Their interval hulls are allowed to overlap. This includes the usual convention of disjoint interval gates.

For an integer depth bound $D\ge 1$, the circuit is

$$
\mathcal C=\mathcal C_D\circ\cdots\circ\mathcal C_1,
\qquad
\mathcal C_t=\bigotimes_{g\in G_t}\Phi_g,
$$

with identity maps on untouched sites. Gates are extended by identities whenever they act on the full chain. A circuit of smaller depth can be padded with identity layers. A circuit with no gates has product output and zero conditional mutual information.

All registers are fixed throughout the circuit. Each gate may use a local environment to realize its CPTP map, but environments of distinct gates are independent. An environment retained between operations must instead be included explicitly among the local registers and their circuit wires. A shared random choice of the entire circuit, a shared nonlocal environment, or nonlocal classical feedforward is not part of this model. Selected measurement outcomes are not conditioned upon: the maps in the circuit are trace preserving.

## 2. Input and faithfulness assumptions

The initial state is

$$
\rho^{\mathrm{in}}_\Lambda
=\bigotimes_{x=1}^n\omega_x,
\qquad
\omega_x\ge \delta I_x,
\qquad
0<\delta\le \frac1d.
$$

The upper restriction $\delta\le 1/d$ causes no loss: an available eigenvalue lower bound can always be decreased to $\min\{\delta,1/d\}$. This convention also permits the addition of independent maximally mixed padding sites in the proof.

Every gate satisfies

$$
\Phi_g(I_{S_g})\ge \alpha I_{S_g},
\qquad 0<\alpha\le 1.
$$

We call this **uniform faithfulness**. For a dimension-preserving CPTP map, $\Phi(I)>0$ is equivalent to mapping every positive definite input to a positive definite output. Indeed, $X\ge\lambda I$ implies

$$
\Phi(X)\ge \lambda\Phi(I).
$$

The condition concerns the image of the identity. It does not require the Choi matrix of each physical gate to be full rank; unitary channels are allowed. Explicit bounds for unitary gates, amplitude damping, arbitrary diamond-close gates, and finite-time local Lindblad gates are given in [examples-and-limits.md](examples-and-limits.md).

The constants $D,r,d,\delta,\alpha$ are uniform in the chain length and in the location of a gate. The gates and the individual input states can otherwise depend on both. Translation invariance is unnecessary.

Write the output as

$$
\rho_\Lambda=\mathcal C(\rho^{\mathrm{in}}_\Lambda).
$$

## 3. Conditional mutual information

All logarithms are natural, so entropies are measured in nats:

$$
S(\tau)=-\operatorname{Tr}(\tau\log\tau),
$$

$$
I(A:C\mid B)_\rho
=S(\rho_{AB})+S(\rho_{BC})
 -S(\rho_B)-S(\rho_{ABC}).
$$

A consecutive tripartition means three disjoint intervals $A,B,C$, in that order, whose union is an interval. The union need not be the whole chain. The buffer $B$ may be empty. If $A$ or $C$ is empty, the CMI is zero.

## 4. Quantitative theorem

Set

$$
w=Dr,\qquad K=4Dr+1,
$$

$$
p_0=\delta^K\alpha^{KD},
\qquad q=1-p_0,
\qquad
m(b)=\max\left\{0,\left\lfloor\frac bK\right\rfloor-2\right\}.
$$

The assumptions imply $0<p_0<1$, hence $0<q<1$.

**Theorem.** For every finite open chain in this model and every consecutive tripartition $A:B:C$,

$$
\boxed{
I(A:C\mid B)_\rho
\le 4w\log d\;q^{\,m(|B|)}.
}
$$

The same constants work for all chain lengths and for cuts that do not align with circuit gates or the coarse blocks used in the proof. The bound also applies to arbitrarily small chains and empty buffers.

For the usual two-sided shielding geometry on a line,

$$
C_L\;B_L\;A\;B_R\;C_R,
$$

one has

$$
\boxed{
I(A:C_LC_R\mid B_LB_R)_\rho
\le
4w\log d
\left[
q^{\,m(|B_L|)}+q^{\,m(|B_R|)}
\right].
}
$$

An absent outer region contributes zero and its term can be omitted.

These statements extend to the infinite line and the half-infinite line, first for finite regions and then for semi-infinite endpoint regions by a monotone limit. The construction of this limit appears in [spatial-decay.md](spatial-decay.md).

### Exponential form

Since $m(b)\ge b/K-3$, define

$$
\xi_*=\frac{K}{-\log q}.
$$

Then

$$
I(A:C\mid B)_\rho
\le 4w\log d\;q^{-3}e^{-|B|/\xi_*}.
$$

For two buffers, the analogous bound is a sum of two exponentials. In particular, it is at most

$$
8w\log d\;q^{-3}
e^{-\min\{|B_L|,|B_R|\}/\xi_*}.
$$

Thus the preparation assumptions imply a finite spatial Markov length. The displayed $\xi_*$ is an upper bound, not an exact correlation length. Its dependence on depth and the spectral floors is deliberately conservative.

## 5. Why these hypotheses arise

The causal regrouping writes the circuit as two coarse layers. The first layer prepares independent states $\sigma_i$ on $K$-site blocks, each satisfying

$$
\sigma_i\ge p_0 I.
$$

Writing a block as $L_iM_iR_i$, this gives

$$
\sigma_i\ge p_0\,(\sigma_i)_{L_iM_i}
\otimes(\sigma_i)_{R_i}.
$$

The second layer joins $R_{i-1}$ to $L_i$. The displayed positive product component supplies a conditional-information contraction at each block. The contraction and its iteration use standard conditional data-processing tools; the regrouping shows how those tools apply to the physical circuit.

Full rank is used as a preparation condition. The theorem is not a statement that an arbitrary many-body state has finite Markov length whenever all of its finite-region density matrices are full rank. The independent coarse resources are essential to the argument.

## 6. Limits of the conclusion

The theorem is for open or infinite one-dimensional lines. Periodic closure, higher-dimensional geometries, correlated initial Gibbs states, postselected trajectories, and exact extensive continuous-time dynamics require separate arguments.

Uniformity matters. A sequence of individually faithful gates can have $\inf_g\lambda_{\min}(\Phi_g(I))=0$; the theorem then supplies no uniform Markov-length bound.

Within a family for which $D,r,d,\delta,\alpha$ stay uniformly bounded as specified, the spatial Markov length cannot diverge. For a fixed finite pattern of gates repeated along the line and a fixed full-rank product input, a divergence therefore requires leaving the faithful-gate region or changing one of the other uniform structural assumptions. This is a necessary-condition statement, not a claim that rank loss always produces a divergence.
