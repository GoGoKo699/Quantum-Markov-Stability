# Examples, consequences and boundaries

The [spatial decay theorem](spatial-decay.md) uses two local spectral floors: the input states obey $\rho_x\geq\delta I_x$, and every gate obeys $\Phi_g(I)\geq\alpha I$. Both floors must be uniform in the chain length and in any parameter family for which a uniform conclusion is claimed. This page identifies common operations satisfying those assumptions and explains the resulting stability statement. All logarithms are natural.

## Maximally mixed and noninteracting thermal inputs

For equal local dimension $d$, the maximally mixed product input has $\delta=1/d$. Thus every circuit in the model has finite Markov length on that input, even if its faithful gates are strong, nonunital or noncommuting. The positive lower bound concerns the gates' action on the identity; no inverse channel is assumed.

A noninteracting thermal state is also a product input. If

$$
\rho_x=\frac{e^{-\beta h_x}}{\operatorname{Tr}e^{-\beta h_x}},
\qquad \beta\geq0,
$$

and each on-site energy width is at most $W$, then

$$
\lambda_{\min}(\rho_x)\geq\frac{e^{-\beta W}}{d}.
$$

Indeed, the largest and smallest Boltzmann weights differ by at most $e^{\beta W}$, and the partition function has at most $d$ terms. A uniform finite temperature and bounded energy width therefore supply a valid $\delta$. This observation does not cover interacting Gibbs states: their initial correlations invalidate the independent-block preparation step.

## Arbitrary unitary gates

For $\Phi(X)=UXU^\dagger$, one has $\Phi(I)=I$ and can take $\alpha=1$. The circuit theorem therefore includes arbitrary bounded-depth local unitary circuits on uniformly full-rank product inputs. A gate's distance from the identity does not enter this example.

The theorem's constants can be very loose even here. Their role is to establish uniform exponential decay for the entire channel class, not to optimize a particular reversible circuit's correlation range.

## A strong nonunital example

The qubit amplitude-damping channel with $0\leq\gamma<1$ has Kraus operators

$$
K_0=\begin{pmatrix}1&0\\0&\sqrt{1-\gamma}\end{pmatrix},
\qquad
K_1=\begin{pmatrix}0&\sqrt{\gamma}\\0&0\end{pmatrix}.
$$

Consequently,

$$
\mathcal A_\gamma(I)
=\begin{pmatrix}1+\gamma&0\\0&1-\gamma\end{pmatrix}
\geq(1-\gamma)I.
$$

For any two-qubit unitary $U$, the gate

$$
\Phi=(\mathcal A_\gamma\otimes\operatorname{id})\circ\operatorname{Ad}_U
$$

has the same faithfulness floor $\alpha=1-\gamma$. Such gates can be placed in staggered layers with unrelated unitaries and need not commute. If their damping parameters satisfy $\gamma\leq\gamma_*<1$, the theorem gives a system-size-independent Markov bound. At $\gamma=1$ the gate loses faithfulness. The bound then ceases to apply; this does not assert that the resulting state is critical. A complete reset can instead produce an uncorrelated state.

## Weak arbitrary CPTP perturbations

Suppose a gate acts on a $q$-dimensional support and satisfies

$$
\|\Phi-\operatorname{id}\|_\diamond\leq\varepsilon.
$$

Here the diamond norm is the full norm, with no factor of one half. By its induced trace-norm bound,

$$
\|\Phi(I)-I\|_\infty
\leq\|\Phi(I)-I\|_1
\leq q\varepsilon.
$$

Since $q\leq d^r$, every gate with a uniform $\varepsilon<d^{-r}$ obeys

$$
\Phi(I)\geq(1-d^r\varepsilon)I.
$$

This gives a direct weak-channel stability corollary for any uniformly full-rank product input. The sufficient threshold is conservative. It neither identifies an optimal perturbation radius nor predicts the actual length near a rank-deficient preparation.

## Finite-time local Lindblad gates

A fixed finite-dimensional local gate generated for finite time by a bounded Lindblad generator is faithful. Write

$$
\mathcal L(X)=AX+XA^\dagger+\sum_\mu L_\mu X L_\mu^\dagger,
\qquad
A=-iH-\frac12\sum_\mu L_\mu^\dagger L_\mu.
$$

This is the standard finite-dimensional generator form of [Gorini, Kossakowski and Sudarshan](https://doi.org/10.1063/1.522979). The completely positive Dyson expansion of $e^{t\mathcal L}$ contains the term $X\mapsto e^{tA}Xe^{tA^\dagger}$, with every remaining term completely positive. Therefore

$$
e^{t\mathcal L}(I)
\geq e^{tA}e^{tA^\dagger}
\geq e^{-2t\|A\|_\infty}I.
$$

The last inequality follows from $\|e^{-tA}\|_\infty\leq e^{t\|A\|_\infty}$. Uniform bounds on the local duration and $\|A\|_\infty$ supply a uniform $\alpha>0$ for a fixed-depth circuit of these gates.

This statement concerns a finite sequence of local gates. It does not extend the theorem to exact continuous-time evolution under an extensive, overlapping many-body generator. Approximating that evolution by ever finer Trotter circuits increases the depth; the present block size and spectral bound deteriorate with it. A continuity argument would also need errors controlled uniformly for the spatial CMI and regions in question. No such limit is taken here.

## An exactly solvable chain with conditional correlations

An elementary noisy entanglement-swapping chain illustrates why the theorem concerns conditional information. This example uses standard Bell-state and Pauli-channel identities; it is an illustration of the bound, not an additional novelty claim.

Take $2\ell$ qubits, with $\ell\geq2$, initially maximally mixed. In the first layer, replace each disjoint pair $(1,2),(3,4),\ldots$ by

$$
\sigma_v=v|\Phi^+\rangle\langle\Phi^+|+(1-v)I_4/4,
\qquad 0\leq v<1.
$$

The pair replacement map has $\Phi(I_4)=4\sigma_v\geq(1-v)I_4$. In the second layer, measure the disjoint pairs $(2,3),(4,5),\ldots,(2\ell-2,2\ell-1)$ in the Bell basis and store each outcome in the corresponding pair's four orthogonal computational-basis states. Its Kraus operators are $|j\rangle\langle\beta_j|$ for the four Bell states $|\beta_j\rangle$, so the channel is trace preserving and unital. Every outcome is retained; no branch is selected or discarded.

This is a depth-two range-two circuit with product-input floor $\delta=1/2$ and gate floor $\alpha=1-v$. Let $A$ and $C$ be the endpoint qubits, and let $B$ contain all intermediate outcome registers.

The link state is Bell diagonal. Its Pauli-error probabilities are

$$
p_v(0)=\frac{1+3v}{4},
\qquad p_v(a)=\frac{1-v}{4}\quad(a=1,2,3).
$$

On the four Pauli labels modulo phase, this distribution is $v$ times the point mass at the identity plus $(1-v)$ times the uniform distribution. Convolution therefore obeys $p_v*p_u=p_{vu}$. Bell swapping adds these error labels, together with a Pauli correction determined by the observed outcomes. Conditional on all outcomes, the endpoints consequently have state $\sigma_{v^\ell}$ up to a known local Pauli.

At each step the measured pair has reduced state $I_4/4$, including after conditioning on earlier outcomes, so every Bell outcome is uniform. The record is classical, and the CMI is the average endpoint mutual information in those branches. Local Pauli corrections preserve entropy. Hence

$$
I(A:C\mid B)=2\log2-S(\sigma_{v^\ell}).
$$

The eigenvalues needed to evaluate this expression are $(1+3v^\ell)/4$ and three copies of $(1-v^\ell)/4$. Averaging over the recorded Pauli outcomes gives the unconditional endpoint state $I_4/4$, so $I(A:C)=0$. Ordinary distant endpoint mutual information therefore misses the conditional dependence in this example.

For each fresh link, $\sigma_{LM}\otimes\sigma_R=I_4/4$ with a trivial $M$, and the optimal product-component weight is $p=1-v$. The resource lemma gives

$$
I(A:C\mid B)
\leq v^{\ell-1}\bigl[2\log2-S(\sigma_v)\bigr]
\leq2\log2\,v^{\ell-1}.
$$

The closed expression and this bound both decay for fixed $v<1$. At the excluded value $v=1$, the first layer loses faithfulness and the endpoint CMI equals $2\log2$ for every length of this finite open-chain family. This identifies a concrete failure when the gate spectral floor vanishes; it makes no claim about a translation-invariant infinite-bulk critical state. The [finite verifier](../verification/README.md) compares the formula with full density-matrix calculations.

## What a divergent Markov length would require

Keep the local dimension, range and depth bounded throughout a family. If the input and gate floors remain bounded away from zero, the [same theorem constants](spatial-decay.md) work for every member. Divergent Markov length is therefore impossible within that uniformly faithful preparation class.

For a family otherwise obeying the model, a putative divergence must evade a uniform spectral floor. This is a preparation-level obstruction. It does not say that rank loss is sufficient for a divergence, nor that a bound on a few reduced output eigenvalues controls the Markov length. The theorem also does not claim an optimal dependence on either spectral floor.

The distinction matters in comparison with [Newsom and Levin](../references/comparison.md): their instability already occurs for pure product inputs under arbitrarily weak local channels. The present result supplies the complementary uniformly full-rank product-input stability statement on a one-dimensional line. Their broader question about correlated full-rank inputs remains outside this proof.

## Why the model's independence matters

The [causal regrouping](circuit-regrouping.md) produces independent block resources because both the input and disjoint gate implementations factorize. A shared global random variable can correlate nominally separate local operations, so an averaged evolution need not equal a tensor product of the advertised local maps. An environment reused across gates can similarly carry information beyond the stated circuit wires. Such processes need an enlarged, explicitly modeled circuit before the theorem can be applied.

Postselection replaces a trace-preserving evolution by an outcome-conditioned map and renormalizes its output. The data-processing and unchanged-marginal steps used in the proof then require a different analysis. The theorem concerns the unconditional CPTP output and retains all physical site registers; classical records, if present, must be included in the stated local dimensions and locality rules.

The proof is for ordinary finite-dimensional tensor-product site algebras on an open or infinite line. It includes inhomogeneous spin and qudit chains. It makes no separate assertion about infinite-dimensional bosonic systems, unmodeled fermionic locality conventions, periodic rings or higher-dimensional geometries.

## Reading onward

The [related-work comparison](../references/comparison.md) identifies the inherited contraction results and the distinct circuit consequence. The [verification guide](../verification/README.md) explains the finite computational checks and their limits. The complete analytical result resides in [spatial decay](spatial-decay.md), with its exact assumptions in the [model](model.md).
