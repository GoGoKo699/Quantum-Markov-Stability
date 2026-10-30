# Conditional contraction from an independent block resource

This section supplies the local inequality used after the circuit regrouping. The information-theoretic ingredients are inherited: conditional Doeblin contraction, conditional mutual-information data processing, and iteration along a sequential channel chain. The proof is included to make the conditioning systems and the relevant channel hypothesis explicit.

Chen, Kato, and Brandão prove conditional contraction for a channel with a completely forgetful component in [Proposition III.2, equations (38)–(42), of arXiv:2010.14682v3](https://arxiv.org/pdf/2010.14682v3); its proof is in Section V.B.3, on printed page 30 of that PDF. Hirche, George, Nuradha, and Wilde develop the corresponding conditional contraction framework in [Sections 2.4 and 3.1 of arXiv:2608.27171v1](https://arxiv.org/html/2608.27171v1): Proposition 2, equation (2.37), gives the Doeblin upper bound, and Corollary 1, equation (3.24), identifies the conditional relative-entropy coefficient with the CMI coefficient. Their [Section 7.2, Propositions 22–24](https://arxiv.org/html/2608.27171v1#S7.SS2), also treats iteration along nonstationary sequential broadcast chains.

The physical boundary channel in the regrouped circuit need not itself have a full forgetful component. The appropriate contraction acts on an internal resource channel, as shown below.

## 1. Registers and resource condition

Let $`\omega_{ABX}`$ be any state. The systems have the following roles:

- $`A`$ is an arbitrary reference region.
- $`B`$ is the already emitted part of the conditioning region.
- $`X`$ is the incoming memory.
- $`L,M,R`$ form a fresh resource, independent of $`ABX`$.

Let $`\sigma_{LMR}`$ be the resource state and let

```math
\mathcal E_{XL\to Y}
```

be any CPTP map. The output $`YM`$ is emitted, and $`R`$ becomes the next memory. Define

```math
\Omega_{ABYMR}
=
\left(\mathrm{id}_{ABMR}\otimes
\mathcal E_{XL\to Y}\right)
\left(\omega_{ABX}\otimes\sigma_{LMR}\right),
```

where the displayed tensor factors are identified by their register labels.

Assume that, for some $`0\lt p\le 1`$,

```math
\sigma_{LMR}
\ge p\,\sigma_{LM}\otimes\sigma_R.
```

No smallness, unitality, faithfulness, or mixing assumption is imposed on $`\mathcal E`$.

## 2. Resource contraction lemma

**Lemma.** Under the preceding assumptions,

```math
\boxed{
I(A:R\mid BYM)_\Omega
\le (1-p)\,I(A:X\mid B)_\omega.
}
```

The dimensions and the state of the reference systems $`A,B`$ are unrestricted.

### Proof by conditional entropy

First suppose $`0\lt p\lt 1`$, and set

```math
\tau_{LMR}
=
\frac{\sigma_{LMR}-p\,\sigma_{LM}\otimes\sigma_R}{1-p}.
```

This is a density operator. Its relevant marginals are exactly

```math
\tau_{LM}=\sigma_{LM},
\qquad
\tau_R=\sigma_R.
```

Let $`\Omega^{(0)}`$ be the output when the resource is
$`\sigma_{LM}\otimes\sigma_R`$, and let $`\Omega^{(1)}`$ be the output when it is $`\tau_{LMR}`$. Then

```math
\Omega=p\Omega^{(0)}+(1-p)\Omega^{(1)}.
```

Because $`\mathcal E`$ acts only on $`XL`$ and the two resources have the same $`LM`$ marginal,

```math
\Omega^{(0)}_{ABYM}
=\Omega^{(1)}_{ABYM}
=\Omega_{ABYM}.
```

Thus $`S(A\mid BYM)`$ has the same value in both branches and their mixture. Concavity of $`S(A\mid BYMR)`$ gives

```math
\begin{aligned}
I(A:R\mid BYM)_\Omega
&=S(A\mid BYM)_\Omega-S(A\mid BYMR)_\Omega\\
&\le
p\,I(A:R\mid BYM)_{\Omega^{(0)}}\\
&\quad +(1-p)\,I(A:R\mid BYM)_{\Omega^{(1)}}.
\end{aligned}
```

In the product branch, $`R`$ is independent of $`ABYM`$, so

```math
I(A:R\mid BYM)_{\Omega^{(0)}}=0.
```

For the residual branch, the chain rule and data processing on the unconditioned right-hand system give

```math
\begin{aligned}
I(A:R\mid BYM)_{\Omega^{(1)}}
&\le I(A:YMR\mid B)_{\Omega^{(1)}}\\
&\le I(A:XLMR\mid B)_{\omega\otimes\tau}\\
&=I(A:X\mid B)_\omega.
\end{aligned}
```

The last equality uses the independence of the fresh resource from $`ABX`$. These inequalities prove the claim.

If $`p=1`$, the resource inequality and equality of traces force
$`\sigma_{LMR}=\sigma_{LM}\otimes\sigma_R`$. The output CMI is then zero directly.

The restricted convexity used in this proof depends on equality of the emitted $`ABYM`$ marginals. CMI is not generally convex in the state, and averaging over unobserved “reset events” without this equality would not justify the bound.

## 3. Obtaining the resource condition

If $`\sigma_{LMR}`$ is full rank, then

```math
\sigma_{LMR}\ge
\lambda_{\min}(\sigma_{LMR})\,I_{LMR}.
```

A density operator has operator norm at most one, so

```math
\sigma_{LM}\otimes\sigma_R\le I_{LMR}.
```

Consequently, the lemma applies with the simple choice

```math
p=\lambda_{\min}(\sigma_{LMR}).
```

More generally, the largest admissible coefficient is

```math
p_\sigma
=
\left\|
\sigma_{LMR}^{-1/2}
\left(\sigma_{LM}\otimes\sigma_R\right)
\sigma_{LMR}^{-1/2}
\right\|_\infty^{-1}.
```

For a full-rank resource, $`0\lt p_\sigma\le 1`$. The upper bound follows by taking the trace of the resource inequality. The coefficient can be much larger than the smallest eigenvalue; for a product across $`LM:R`$, it equals one.

Full rank is a sufficient condition for the resource inequality, not a necessary one. The circuit theorem uses a uniform full-rank bound because it is easy to propagate through the first coarse layer.

## 4. Reduction to an internal Doeblin channel

Here is the explicit connection to the existing channel contraction results.

Write $`Q=LM`$, assume $`\sigma_Q`$ is full rank, and choose an eigenbasis

```math
\sigma_Q=\sum_j\lambda_j|j\rangle\langle j|.
```

Let $`V`$ be a copy of $`Q`$ and define the purification

```math
|\psi\rangle_{QV}
=\sum_j\sqrt{\lambda_j}\,|j\rangle_Q|j\rangle_V.
```

There is a CPTP map $`\mathcal T_{V\to R}`$ satisfying

```math
\sigma_{QR}
=
\left(\mathrm{id}_Q\otimes\mathcal T\right)
\left(|\psi\rangle\langle\psi|_{QV}\right).
```

For completeness, it is specified on matrix units by

```math
\mathcal T(|j\rangle\langle k|)
=
\frac{\langle j|\sigma_{QR}|k\rangle}
{\sqrt{\lambda_j\lambda_k}}.
```

Its unnormalized Choi operator is

```math
\Gamma^{\mathcal T}
=
(\sigma_Q^{-1/2}\otimes I_R)\,
\sigma_{QR}\,
(\sigma_Q^{-1/2}\otimes I_R),
```

with the first tensor factor identified with $`V`$ in the chosen basis. This operator is positive and has partial trace $`I_V`$, proving complete positivity and trace preservation.

The resource inequality becomes

```math
\Gamma^{\mathcal T}
\ge p\,I_V\otimes\sigma_R.
```

Equivalently, in completely positive order,

```math
\mathcal T
\ge_{\mathrm{CP}}p\,\mathcal R_{\sigma_R},
\qquad
\mathcal R_{\sigma_R}(X)=\mathrm{Tr}(X)\sigma_R.
```

For $`p\lt 1`$ this gives a CPTP decomposition

```math
\mathcal T
=p\,\mathcal R_{\sigma_R}+(1-p)\mathcal T_1.
```

The known conditional Doeblin inequality therefore yields

```math
I(A:R\mid BYM)
\le (1-p)I(A:V\mid BYM)
```

when $`\mathcal T`$ is applied to $`V`$. Before this application, $`\mathcal E`$ has acted on $`XL`$ in the independent input
$`\omega_{ABX}\otimes|\psi\rangle\langle\psi|_{LMV}`$. The chain rule and data processing give

```math
I(A:V\mid BYM)
\le I(A:YMV\mid B)
\le I(A:X\mid B)_\omega.
```

The two maps act on disjoint registers, so their order can be interchanged. Their combined output is precisely $`\Omega`$. This recovers the resource lemma as an application of the inherited internal-channel inequality.

## 5. Which channel must satisfy the contraction hypothesis?

The complete boundary map is

```math
\mathcal N_{X\to YMR}(X)
=
\left(\mathcal E_{XL\to Y}\otimes\mathrm{id}_{MR}\right)
(X\otimes\sigma_{LMR}).
```

It can transmit some or all of the input $`X`$ perfectly to the emitted register $`Y`$. Its full-output CMI contraction coefficient can therefore equal one, and its Choi operator need not be full rank. The full-Y-channel forgetful-component condition in Chen–Kato–Brandão, or the full broadcast-channel Choi condition in Hirche et al., should not be asserted for this physical map without checking it.

The needed coefficient belongs instead to $`\mathcal T_{V\to R}`$. Information retained in the emitted conditioning system $`YM`$ is allowed. This is why the resource proof remains applicable to boundary maps that preserve input information in their visible output.

Sequential multiplication of the resulting factors is the standard chain-rule/data-processing method. Its use for the spatially regrouped circuit is written out in [spatial-decay.md](spatial-decay.md).
