# Reproducible finite checks

The checks in this directory exercise the contraction lemma, exact circuit regrouping, and spatial conditioning geometry used in the theorem. They are finite numerical and combinatorial checks. They do not prove the theorem or establish a literature novelty claim.

## Run

The recorded run used Python 3.12.14 and NumPy 2.3.5. NumPy is the only nonstandard dependency and is pinned in [requirements.txt](requirements.txt). No network access or external data is used by the verifier.

From the repository root, in an environment with the pinned dependency installed:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python verification/verify.py --output verification/results.json
```

For a fresh virtual environment:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 .venv/bin/python verification/verify.py --output verification/results.json
```

The default seed is `20261030`; another seed can be supplied with `--seed`. The script exits with an assertion failure if a check fails and writes its JSON report only after all checks pass. Floating-point values can differ slightly across linear algebra backends. The absolute assertion tolerance is `5e-9`, and entropies are in nats. The wall-clock duration in the report is descriptive and is not a reproducibility condition.

## What is checked

### Conditioned resource contraction

Seventy-two cases test

$$
I(A:R\mid BYM)\le (1-p)I(A:X\mid B)
$$

for arbitrary mixed states on three qubits $ABX$, independent full-rank resources on $LMR$, and several boundary channels. The conditioned system $B$ is retained in the calculation. The examples include classical parity correlations, exact conditional independence with noncommuting conditional states, product resources, coherent channels, generic CPTP channels, replacement channels, and a parity measurement. Some channels preserve their input dimension, and others discard information or change the output dimension, as permitted by the local lemma.

The resource coefficient is computed from the generalized eigenvalue problem

$$
p=\lambda_{\min}\left[
(\sigma_{LM}\otimes\sigma_R)^{-1/2}
\sigma_{LMR}
(\sigma_{LM}\otimes\sigma_R)^{-1/2}
\right].
$$

The script independently reconstructs each resource from its canonical purification and internal Choi channel. It checks trace preservation and the internal Doeblin minorization. This is the internal channel reduction explained in [the contraction proof](../science/contraction.md); the contraction mechanism is inherited from existing conditional data-processing results.

A negative control shows why unrestricted CMI convexity would be invalid: two branches each have zero conditional mutual information, while their equal mixture has CMI $\log 2$. The branches have unequal emitted marginals. The actual lemma avoids this failure by ensuring those marginals coincide.

### Causal regrouping

The structural checks generate 320 circuit layouts with depths from 1 through 8 and support-hull ranges from 1 through 5. They include identity wires, noncontiguous gate supports whose hulls can overlap, and short terminal blocks. Initial-site dependency sets are propagated on the physical wire DAG without using special properties of the channels.

For the partition with $K=4Dr+1$, the checks verify that:

- each first-layer group is ancestor closed;
- each remaining gate belongs to one block boundary and lies in its $Dr$-wide strips;
- distinct boundary groups have disjoint actual supports;
- the regrouped ordering preserves every immediate causal predecessor;
- the cut-crossing support count used for the small-buffer bound is at most $2(r-1)$ sites per layer.

A fixed adversarial layout includes later gates located inside one block whose backward cones cross the block boundary. A grouping based only on the physical support of each gate reverses a causal dependency in this layout. This control tests the distinction on which the nonunitary regrouping proof depends.

### Equality for nonunitary channels

Two small circuits use coherent gates followed by nonunital amplitude damping. Every local channel is checked to be trace preserving and faithful. The original order is evaluated with a direct basis-index embedding of each Kraus operator. The regrouped order is evaluated with a separate tensor-permutation implementation.

For the four-qubit circuit, the input is a maximally entangled state of the system and a four-qubit reference. Comparing the resulting normalized Choi states checks the whole channel in that finite example. A six-qubit example compares the output on a mixed input. These small examples have one block boundary; the larger $K=4Dr+1$ layouts are covered by the structural checks.

The physical-support-only grouping is also evaluated on the four-qubit Choi input and gives a clearly different channel. This prevents a passing comparison from being explained by gates that happen to commute or by an insensitive input state.

### Spatial CMI and cut geometry

Nine examples use independent noisy Bell links

$$
\sigma_v=v|\Phi^+\rangle\langle\Phi^+|+(1-v)I/4
$$

and complete Bell measurements on disjoint neighboring link halves. The outcomes remain in orthogonal local output registers. These examples can be prepared from a maximally mixed product input: the first layer replaces each pair by $\sigma_v$, and the second layer is the trace-preserving Bell measurement channel. For $v<1$, both layers are faithful.

For a chain of $\ell$ links, the script compares the endpoint CMI conditioned on all intermediate outputs with the independent analytic expression

$$
I(A:C\mid B)=2\log 2-S(\sigma_{v^\ell}).
$$

The [worked example](../science/examples-and-limits.md#an-exactly-solvable-chain-with-conditional-correlations) derives this expression by Pauli-error convolution and specifies the full trace-preserving preparation.

It also checks the resource-chain estimate $2\log 2\,v^{\ell-1}$ and verifies that the unconditional endpoint mutual information vanishes. Thus the example exercises conditional correlations that are invisible to an ordinary distant two-point mutual-information check.

On one six-qubit example, the script checks 139 instances of the inequalities used for arbitrary interval endpoints, empty or short buffers, absorption of partial boundary cells, and the two-sided line geometry. These are finite examples of general entropy inequalities; their proofs are given in [spatial-decay.md](../science/spatial-decay.md) and the audit below.

## Recorded results

The complete machine-readable output is [results.json](results.json). The recorded run passed all checks.

| Check | Recorded result |
|---|---:|
| Conditioned contraction cases | 72 |
| Cases with nonzero output CMI | 21 |
| Maximum contraction-bound excess | $1.33\times10^{-15}$ |
| Maximum internal resource reconstruction error | $2.86\times10^{-15}$ |
| Structural circuit layouts | 320 |
| Gates in structural layouts | 92,106 |
| Gates with noncontiguous supports | 33,569 |
| Distinct short terminal-block sizes sampled | 85 |
| Maximum nonunitary regrouping Frobenius difference | $1.43\times10^{-16}$ |
| Wrong geometric regrouping Choi difference | $0.503$ |
| Noisy Bell-chain examples | 9 |
| Maximum analytic CMI discrepancy | $1.44\times10^{-15}$ |
| Spatial geometry inequality instances | 139 |
| Maximum geometry-bound excess | $1.78\times10^{-15}$ |

The positive excesses at the level of $10^{-15}$ are floating-point roundoff. The negative controls are expected violations of deliberately invalid shortcuts; they do not contradict the stated theorem.

## Limits of this evidence

These checks cover finitely many dimensions, channels, resources, and layouts. Random sampling, even with a fixed seed, cannot establish universal contraction or regrouping. The universal statements depend on the mathematical arguments in `science/`.

The script tests useful resource coefficients for small examples. It does not numerically validate the conservative circuit coefficient

$$
p_0=\delta^K\alpha^{KD}
$$

for arbitrarily large parameter values. That coefficient can be extremely small; ordinary floating-point subtraction can round $1-p_0$ to one. The theorem establishes a uniform finite Markov length under fixed positive floors, without asserting a sharp or practically useful value for the displayed bound.

The checks do not cover periodic rings, higher-dimensional lattices, global shared gate randomness, postselection, correlated inputs, or an exact extensive continuous-time limit. Those cases are outside the stated model.

See [audit.md](audit.md) for the mathematical boundary-case audit and its limitations.
