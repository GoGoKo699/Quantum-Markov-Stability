# Literature comparison

Last checked: 30 October 2026. Exact primary versions and the extent of the reading are recorded in [sources.md](sources.md).

## Scope of the circuit result

The result in [model.md](../science/model.md) concerns a product input with a uniform spectral floor, followed by a fixed-depth, finite-range CPTP circuit on an open or infinite one-dimensional line. Physical gates obey a uniform lower bound on their image of the identity. Gates may be strong, nonunital, and noncommuting. Independent environments and a fixed bound on local dimension are part of the model.

Its quantitative input is

```math
\omega_x\ge\delta I_x,\qquad
\Phi_g(I)\ge\alpha I,\qquad
K=4Dr+1,\qquad p_0=\delta^K\alpha^{KD}\gt 0.
```

The proposed addition is an exact reduction from this physical preparation model to independent bounded-size faithful resources, followed by a uniform spatial CMI bound. Conditional contraction and its sequential iteration are established tools. The reduction, its environmental assumptions, and its uniform dimension and eigenvalue bounds are therefore the essential parts to check when assessing the result's relation to previous work.

## Closest contraction and matrix-product results

### Chen–Kato–Brandão: a replacement component in a sequential channel

[CKB23](sources.md#ckb23) Proposition III.2 assumes a Y-shaped channel with a completely positive convex decomposition

```math
N=(1-\eta)F+\eta N',\qquad F(X)=\mathrm{Tr}(X)\sigma,
\quad 0\le\eta\lt 1.
```

It proves conditional-memory contraction and exponential CMI decay upon iteration. This is a direct predecessor of the information-forgetting mechanism used here. The cited hypothesis is the channel decomposition in **PDF Eq. (38)** (HTML Eq. (53)), rather than an informal assertion that a channel has positive outputs. A physical gate satisfying only $`\Phi(I)\gt 0`$ need not possess such a replacement component: a unitary gate already distinguishes these conditions. A reduction establishing an appropriate internal channel remains necessary.

### Hirche–George–Nuradha–Wilde: conditional Doeblin bounds and chains

[HGNW26](sources.md#hgnw26) Proposition 2 and Corollary 1 imply

```math
\eta_{\mathrm{CMI}}(T)\le 1-\alpha_+(T),
```

where $`\alpha_+(T)`$ is the largest CP replacement weight. Section 7.2 already gives nonstationary sequential-chain CMI bounds; Propositions 23–24 turn a uniform Choi eigenvalue floor into exponential decay. Neither conditional contraction nor chain iteration is claimed here as a new general principle.

The channel to which this machinery applies in the circuit proof is the internal channel $`T_{V\to R}`$ obtained by normalizing the marginal of a faithful resource $`\sigma_{LMR}`$. It is not automatically the whole physical step that emits $`YM`$ while retaining $`R`$. That step can send its input perfectly into $`Y`$, giving whole-output contraction coefficient one. The resource argument and the chain rule connect internal contraction to the desired retained-memory estimate; applying Proposition 24 directly to every physical step would omit this distinction.

### Uniform matrix product states

[SMK24](sources.md#smk24) Theorem III.1 establishes exponential CMI decay, with a polynomial prefactor, for infinite uniform MPS. Their model is isometrically generated; the paper distinguishes this class of purely generated finitely correlated states from general MPDOs. An arbitrary circuit output with discarded local environments is not automatically in that class. Purifying it and then discarding ancillary systems in the conditioning region does not transfer a CMI upper bound by data processing: CMI need not decrease under operations on its conditioning system. The MPS theorem therefore does not by itself establish the present mixed-output circuit statement.

## Stability results with different preparation assumptions

| Source | Established setting | Relation to the circuit theorem |
|---|---|---|
| [YLLLZ26](sources.md#ylllz26) | Theorem 2 and Supplementary Theorem VII.1 preserve correlation decay under locally reversible channel circuits. Definition 1 requires forward and reverse circuits with recovery properties for subsets of gates. | The current assumptions impose a forward faithful preparation circuit, without assuming those reverse circuits. Local reversibility cannot simply be inferred from the desired CMI conclusion and then used to prove that same conclusion. |
| [ZG25](sources.md#zg25) | The quantum weak-decoherence theorem treats commuting-Pauli Gibbs inputs and weak stabilizer-mixing channels; see Theorem 5 and Appendix B, Theorem 38. | It allows correlated Gibbs inputs under specialized noise. The present input class is narrower, while its physical gates need not be weak or stabilizer mixing. |
| [ZG25HT](sources.md#zg25ht) | Theorem A.1 proves high-temperature exponential CMI for commuting Gibbs states under single-site unital, commutation-preserving channels. The classical theorem allows arbitrary local transition matrices. | The quantum theorem's channel restrictions do not include arbitrary faithful overlapping multiqudit gates. Conversely, the present product-input result does not cover general interacting Gibbs states. |

These statements address different sufficient conditions. None of the specifically checked hypotheses can be replaced merely by the observation that the circuit output has finite bond dimension or full-rank finite-region reductions.

## Full-rank entanglement-swapping result

[T26](sources.md#t26) reports that full-rank entangled two-qubit links have a finite entanglement-swapping distance, including adaptive postselected measurements. Its abstract also connects the mechanism to MPDOs and localizable entanglement. This is relevant prior work on full rank suppressing long-range conditional transmission.

Endpoint entanglement after measurements and CMI of the unmeasured state are different quantities. In particular, conditional correlations can be classical even when no endpoint entanglement is present. An entanglement-swapping cutoff alone therefore does not supply the stated spatial CMI bound.

**Review limit:** only the primary abstract was available for this comparison. No theorem number, proof-level distinction, or absence of a stronger internal result is asserted. Checking the complete paper remains necessary before making a definitive priority claim about overlap with its MPDO arguments.

## Relation to the full-rank stability question

[NL26](sources.md#nl26) constructs a weak-channel instability from a pure product input and asks in its closing discussion whether an analogous instability can occur for states with full-rank local density matrices, mentioning the maximally mixed state and finite-temperature Gibbs states.

The circuit theorem establishes stability for the **one-dimensional uniformly full-rank product-input subclass**, including the maximally mixed input, under the specified faithful finite-depth circuits. Its constants deteriorate when the input or gate spectral floors vanish, so it does not conflict with a rank-deficient construction. It does not settle the question for arbitrary correlated full-rank states, interacting Gibbs states, periodic chains, or exact extensive continuous-time dynamics.

## What is inherited and what must be established here

The proof should visibly separate three steps:

1. **Inherited information inequality:** a CP replacement component yields complete conditional-information contraction; chain rules turn repeated contraction into spatial decay in an appropriate sequential representation. The preceding CKB23 and HGNW26 results are credited for this mechanism.
2. **Circuit-specific reduction:** regroup the given fixed-depth DAG exactly into independent bounded-size resources and boundary maps, with spectral floor $`p_0`$. Neither full Choi rank of the physical gates nor a physical replacement component may be assumed.
3. **Spatial conclusion:** apply the internal resource channel estimate while retaining all emitted conditioning registers, and control arbitrary cuts, endpoint dimensions, and the line limits stated in the theorem.

This comparison is a bounded review of the explicit results listed above, not an exhaustive priority certification. The outstanding full-text comparison with T26 is recorded rather than treated as resolved.
