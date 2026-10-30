# From block contraction to spatial CMI decay

This section proves the theorem in [model.md](model.md), including arbitrary cuts, small buffers, finite-chain edges, two-sided shields, and infinite-line limits.

Use the notation

```math
w=Dr,\qquad K=4Dr+1,\qquad
p_0=\delta^K\alpha^{KD},\qquad q=1-p_0,
```

```math
m(b)=\max\left\{0,\left\lfloor\frac bK\right\rfloor-2\right\}.
```

The sequential contraction and its iteration are instances of established conditional data-processing methods; see the attribution and internal-channel reduction in [contraction.md](contraction.md). The spatial construction to which those methods are applied is the exact regrouping in [circuit-regrouping.md](circuit-regrouping.md).

## 1. A cut mutual-information bound

We first record a bound that does not require full rank or faithfulness.

**Cut bound.** A depth-$`D`$ circuit of range at most $`r`$, with disjoint actual gate supports in each layer, acting on a product input satisfies

```math
I(P:Q)_\rho\le 4D(r-1)\log d\le 4w\log d
```

across every physical cut into a prefix $`P`$ and suffix $`Q`$.

### Proof

Consider one gate crossing the cut. Write its support as $`ab`$, where $`a`$ lies in the left half and $`b`$ lies in the right half, and write the untouched parts of the two halves as $`A`$ and $`B`$. Let $`\tau`$ and $`\tau'`$ be the states before and after the gate.

The marginal on $`AB`$ is unchanged because the gate is trace preserving. The chain rule gives

```math
\begin{aligned}
I(Aa:bB)_{\tau'}
&=
I(A:B)_{\tau'}
+I(A:b\mid B)_{\tau'}\\
&\quad +I(a:bB\mid A)_{\tau'}\\
&\le
I(A:B)_\tau
+2\log\dim\mathcal H_b
+2\log\dim\mathcal H_a\\
&\le
I(Aa:bB)_\tau+2|S_g|\log d.
\end{aligned}
```

Here $`I(U:V\mid W)\le2\log\dim\mathcal H_U`$ follows from the dimension bounds on conditional entropy. The last inequality uses data processing under discarding $`a`$ and $`b`$.

A gate entirely on one side cannot increase the cut mutual information. For a cut between sites $`j`$ and $`j+1`$, every crossing support of range at most $`r`$ lies in

```math
\{j-r+2,\ldots,j+r-1\},
```

a strip of $`2(r-1)`$ sites. The actual supports in one layer are disjoint, so

```math
\sum_{\substack{g\text{ crosses the cut}\\g\in G_t}}
|S_g|\le2(r-1).
```

Thus a layer increases the cut mutual information by at most $`4(r-1)\log d`$. The initial product state has zero cut mutual information. Summing over the $`D`$ layers proves the bound.

For the more restrictive convention of disjoint interval supports, at most one gate per layer crosses a cut, and the same argument gives the improved bound $`2Dr\log d`$. We retain $`4w\log d`$ to cover the general support convention of the model.

### Consequence for small buffers

For consecutive intervals $`A:B:C`$,

```math
I(A:C\mid B)\le I(A:BC).
```

Enlarge $`A`$ to the full prefix ending at its right boundary and enlarge $`BC`$ to the remaining suffix. Data processing then gives

```math
\boxed{
I(A:C\mid B)_\rho\le4w\log d.
}
```

This includes an empty buffer. If either endpoint region is empty, its CMI is zero without using the bound.

## 2. Buffers made of complete emitted cells

Use the padded, regrouped circuit from [circuit-regrouping.md](circuit-regrouping.md). Its regular emitted cells $`J_i`$ are contiguous intervals of $`K`$ sites, and the retained memory after step $`i`$ is $`R_i`$, with

```math
\dim\mathcal H_{R_i}\le d^w.
```

Let a buffer consist of $`k\ge1`$ complete consecutive cells,

```math
B=J_sJ_{s+1}\cdots J_{s+k-1}.
```

Let $`A'`$ be the entire emitted prefix before $`J_s`$, and let $`C'`$ be the full physical suffix after the buffer. Immediately before step $`s`$, the joint state of the prefix and incoming memory is some state on $`A'R_{s-1}`$. All later resources are independent of that state and of one another.

Initialize the accumulated conditioning register as empty. At each buffer step, the contraction lemma gives

```math
I(A':R_i\mid J_s\cdots J_i)
\le
q\,
I(A':R_{i-1}\mid J_s\cdots J_{i-1}).
```

Applying this $`k`$ times,

```math
I(A':R_{s+k-1}\mid B)
\le q^k I(A':R_{s-1}).
```

The incoming memory has at most $`w`$ sites, so

```math
I(A':R_{s-1})\le2\log\dim\mathcal H_{R_{s-1}}
\le2w\log d.
```

The remaining suffix is produced from $`R_{s+k-1}`$ and fresh independent resources by a channel acting entirely on the unconditioned right-hand side. Conditional mutual-information data processing therefore yields

```math
\boxed{
I(A':C'\mid B)_\rho
\le2w\log d\;q^k.
}
```

This argument allows a nonstationary sequence of block states and boundary channels. It does not assume a primitive transfer map, translation invariance, or a full-rank Choi operator for the entire boundary step.

## 3. Arbitrary positions of the cuts

Let $`A:B:C`$ be any consecutive tripartition on the original chain, and put $`b=|B|`$. The independent padding leaves its reduced state unchanged and places every original site within the regular $`K`$-site cell partition.

Let $`k_B`$ be the number of regular cells wholly contained in $`B`$. At most two partially intersected cells are discarded when passing from $`B`$ to its complete-cell interior. In particular,

```math
k_B\ge
\max\left\{0,\left\lfloor\frac bK\right\rfloor-2\right\}
=m(b).
```

One can obtain a slightly better count for an exact equal-cell partition; the displayed conservative count is sufficient here.

### Case 1: at least one complete cell

Suppose $`k_B\ge1`$. Write

```math
B=B_{\mathrm{left}}\,B_{\mathrm{mid}}\,B_{\mathrm{right}},
```

where $`B_{\mathrm{mid}}`$ is the union of all $`k_B`$ complete cells in $`B`$ and the two end pieces have fewer than $`K`$ sites each.

The following step uses the chain rule, not monotonicity under changing a conditioning system:

```math
I(A:C\mid B_{\mathrm{left}}B_{\mathrm{mid}}B_{\mathrm{right}})
\le
I(AB_{\mathrm{left}}:B_{\mathrm{right}}C\mid B_{\mathrm{mid}}).
```

For clarity, the right-hand side is exactly the left-hand side plus

```math
\begin{aligned}
&I(B_{\mathrm{left}}:B_{\mathrm{right}}\mid B_{\mathrm{mid}})\\
&\quad+
I(B_{\mathrm{left}}:C\mid B_{\mathrm{mid}}B_{\mathrm{right}})\\
&\quad+
I(A:B_{\mathrm{right}}\mid B_{\mathrm{mid}}B_{\mathrm{left}}),
\end{aligned}
```

which are all nonnegative.

Now enlarge $`AB_{\mathrm{left}}`$ to the entire prefix $`A'`$ before $`B_{\mathrm{mid}}`$, and enlarge $`B_{\mathrm{right}}C`$ to the entire suffix $`C'`$ after it. Monotonicity under discarding from the unconditioned systems gives

```math
I(A:C\mid B)
\le I(A':C'\mid B_{\mathrm{mid}}).
```

The complete-cell result applies:

```math
I(A:C\mid B)
\le2w\log d\;q^{k_B}
\le4w\log d\;q^{m(b)}.
```

### Case 2: no complete cell

If $`k_B=0`$, then $`m(b)=0`$. Use the cut bound from Section 1:

```math
I(A:C\mid B)\le4w\log d
=4w\log d\;q^{m(b)}.
```

There is no need to absorb two overlapping fragments of a single cell or to introduce a reversed sequential construction.

Together, the two cases prove

```math
\boxed{
I(A:C\mid B)_\rho
\le4w\log d\;
q^{\max\{0,\lfloor |B|/K\rfloor-2\}}.
}
```

Because padding was independent and untouched, this proof applies to the original finite chain even when it has fewer than $`K`$ sites or the specified intervals meet its endpoints.

## 4. Two-sided shielding on a line

Consider consecutive regions in the order

```math
C_L\;B_L\;A\;B_R\;C_R.
```

The outside region $`C_LC_R`$ is disconnected. Apply the chain rule:

```math
\begin{aligned}
I(A:C_LC_R\mid B_LB_R)
&=I(A:C_L\mid B_LB_R)\\
&\quad+I(A:C_R\mid B_LB_RC_L).
\end{aligned}
```

The first term is bounded by

```math
I(C_L:AB_RC_R\mid B_L),
```

because the latter equals the first term plus
$`I(C_L:B_R\mid B_L)`$ and
$`I(C_L:C_R\mid B_LB_RA)`$.

The second term is bounded by

```math
I(C_LB_LA:C_R\mid B_R),
```

because the latter equals the second term plus
$`I(C_LB_L:C_R\mid B_R)`$.

Consequently,

```math
\boxed{
\begin{aligned}
I(A:C_LC_R\mid B_LB_R)
&\le I(C_L:AB_RC_R\mid B_L)\\
&\quad+I(C_LB_LA:C_R\mid B_R).
\end{aligned}
}
```

Each term on the right is a one-sided consecutive-tripartition CMI. Applying the established bound separately gives

```math
\boxed{
I(A:C_LC_R\mid B_LB_R)
\le4w\log d
\left[
q^{m(|B_L|)}+q^{m(|B_R|)}
\right].
}
```

Empty buffers are covered by $`m(0)=0`$. If an outer region is absent, its corresponding term vanishes.

This proves the standard two-buffer shielding statement on a line. It does not invoke a periodic identification of the ends.

## 5. Infinite and half-infinite lines

Let the site set be $`\mathbb Z`$ or a half-infinite interval, with the same uniform bounds on dimensions, input states, depth, range, and gate faithfulness.

The output state is well defined on local observables. Pulling a finite-support observable backwards through a depth-$`D`$ circuit produces an observable supported in a finite geometric backward cone. Its expectation is then evaluated in the infinite product input. These local expectations are consistent and define the output state.

For any fixed finite consecutive regions $`A:B:C`$, retain the gates in their complete backward wire cone. All such gates lie in the finite interval obtained by extending $`ABC`$ by at most $`w`$ sites on each available side. The retained gates form a finite-depth finite-range circuit with the same uniform parameters. They reproduce the exact reduced state on $`ABC`$: gates outside this causal past cannot influence those outputs.

The finite-chain theorem therefore applies with constants independent of the containing interval. This establishes the same bound on the infinite and half-infinite lines for all finite regions.

For a semi-infinite endpoint region, define the corresponding CMI with a finite buffer as the increasing limit over finite endpoint intervals. For example,

```math
I(A_\infty:C_\infty\mid B)
:=
\sup_{A_0,C_0}
I(A_0:C_0\mid B),
```

where $`A_0,C_0`$ exhaust the specified left and right endpoint regions by finite intervals. Monotonicity under enlarging the unconditioned endpoint systems ensures the existence of this limit. The uniform finite-region bound gives

```math
I(A_\infty:C_\infty\mid B)
\le4w\log d\;q^{m(|B|)}.
```

The same limiting procedure applies to two-sided outside regions. No subtraction of infinite von Neumann entropies is required.

## 6. What the argument does and does not use

The proof uses the exact causal structure of a finite-depth circuit, a local eigenvalue floor on its independent first-layer resources, and conditional contraction on their internal memory channels.

It does not derive CMI decay merely from ordinary correlation decay or from a transfer-matrix spectral gap. It does not use a many-body logarithmic expansion, a global smallest-eigenvalue perturbation argument, or the assumption that CMI is convex under arbitrary mixing.

The constants do not remain controlled when the circuit depth is taken to infinity without additional estimates. Thus the proof does not supply an exact extensive continuous-time Lindblad theorem by Trotterization.
