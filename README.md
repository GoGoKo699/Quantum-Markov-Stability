# Quantum Markov Stability

**Uniformly full-rank product states retain finite Markov length under uniformly faithful local quantum circuits of bounded depth and range in one dimension.**

Conditional mutual information measures the dependence between two regions after the intervening region is available. A shallow local circuit need not make this conditional dependence short ranged: rank-deficient product inputs can exhibit algebraic decay after arbitrarily weak channels. This repository proves a complementary stability theorem for uniformly full-rank product inputs, allowing coherent, nonunital and noncommuting gates. The exact setting and comparison are in the [model](science/model.md) and [related work](references/comparison.md).

## Main result

Consider an open or infinite chain with site dimension at most $`d\geq2`$, product input $`\bigotimes_x\omega_x`$ satisfying $`\omega_x\geq\delta I_x`$, and a circuit with depth at most $`D`$ and gate range at most $`r`$, where $`D,r\geq1`$. Gates in each layer have disjoint supports. Assume every local CPTP gate satisfies $`\Phi_g(I)\geq\alpha I`$, with $`0\lt \delta\leq1/d`$ and $`0\lt \alpha\leq1`$ uniform in position and system size.

Set

```math
K=4Dr+1,\qquad p_0=\delta^K\alpha^{KD},
\qquad m(b)=\max\{0,\lfloor b/K\rfloor-2\}.
```

For every consecutive tripartition $`A:B:C`$,

```math
I(A:C\mid B)\leq4Dr\log d\,(1-p_0)^{m(|B|)}.
```

The bound is uniform in the endpoint sizes and chain length, and applies to arbitrary physical cuts. For a region shielded on both sides, the corresponding CMI is bounded by the sum of the two one-sided bounds. The [complete theorem and proof](science/spatial-decay.md) include empty buffers, finite boundaries and the infinite-line limit. Logarithms are natural.

The displayed constants are conservative. They establish a uniform finite length; they are not an estimate of the optimal length in a particular circuit.

## Why it works

The gate dependency graph can be regrouped exactly into independent block preparations followed by disjoint boundary operations. Full rank supplies a positive product component in each block resource. Established conditional Doeblin contraction then removes a fixed fraction of the remaining conditional information at each buffer block. A cut mutual-information bound handles short buffers, and chain rules connect the sequential construction to arbitrary spatial regions.

The [attribution account](references/comparison.md) separates the inherited information-contraction tools from this physical-circuit consequence. Physical-gate faithfulness means a positive image of the identity; it does **not** require a full-rank gate Choi matrix. In particular, arbitrary unitary gates are included.

## Scientific reading routes

| Question | Authoritative page |
|---|---|
| What is proved, and under which assumptions? | [Model and main result](science/model.md) |
| Why does a faithful resource contract conditional information? | [Resource contraction](science/contraction.md) |
| How can nonunitary gates be regrouped without assuming they commute? | [Exact causal regrouping](science/circuit-regrouping.md) |
| How does the construction cover arbitrary cuts and two-sided shields? | [Spatial decay](science/spatial-decay.md) |
| Which physical gates satisfy the assumptions? | [Examples and boundaries](science/examples-and-limits.md) |
| What is inherited from earlier work? | [Related-work comparison](references/comparison.md) and [sources](references/sources.md) |
| What can be reproduced computationally? | [Verification guide](verification/README.md) |

The [science overview](science/README.md) gives the connected proof route. [llms.txt](llms.txt) maps questions to the same authoritative pages.

## Scope that matters

The full-rank assumption is a property of the **preparation**, together with independence of the local input factors and gate environments. It is not a criterion on arbitrary output marginals. The theorem covers ordinary finite-dimensional tensor-product site algebras on a line. It does not establish stability for correlated interacting Gibbs inputs, postselected evolution, shared global randomness, unmodeled environment memory, periodic rings, higher dimensions or exact extensive continuous-time evolution.

The result permits strong faithful dissipation. Examples include arbitrary unital gates, partial amplitude damping with a uniform damping bound below complete reset, sufficiently small arbitrary CPTP perturbations of the identity, and finite-time bounded local Lindblad gates used in a fixed-depth circuit. Their spectral floors are derived in [examples and boundaries](science/examples-and-limits.md).

## Learning route

The educational anchor is Mark M. Wilde, _Quantum Information Theory_, second edition (2017). Start with the [learning overview](learning/README.md), use the [30-milestone map](learning/MILESTONES.md) to locate each concept in the argument, and follow the [Wilde-to-project bridge](learning/WILDE_BRIDGE.md) for notation, source sections, and worked examples. The map has 12 background milestones and 18 milestones for the proof, physical examples, and scope. The bridge makes the conversion from Wilde’s bits to the project’s nats explicit.

## Reproduce the finite checks

```bash
python -m pip install -r verification/requirements.txt
python verification/verify.py
```

The checks exercise conditioned resource contraction, structural circuit regrouping, exact finite channel/state comparisons, an analytical resource-chain example and spatial chain-rule inequalities. Deliberately invalid variants serve as negative controls. These computations probe the implementation and representative finite cases; the general result is the analytical proof under `science/`. See the [verification guide](verification/README.md) for outputs, tolerances and limits.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
