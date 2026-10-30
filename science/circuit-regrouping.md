# Exact regrouping into independent block resources

The circuit in [model.md](model.md) can be rearranged into two coarse layers without inverting any gate. The first layer acts independently on blocks of $K=4Dr+1$ sites. The second consists of independent channels near the boundaries between those blocks.

The argument uses the causal directed acyclic graph of the circuit. It applies to CPTP maps, including nonunitary maps, because it only changes the order of operations that have disjoint actual supports.

Throughout, let

$$
w=Dr,\qquad K=4Dr+1.
$$

## 1. Padding finite chains

It is convenient to begin with a chain whose length is a multiple of $K$. This introduces no restriction on the original finite-chain theorem.

For an original chain of $n\ge 1$ sites, add $K$ padding sites on the left and between $K$ and $2K-1$ padding sites on the right, so that the total length is

$$
N=K\left(\left\lceil\frac nK\right\rceil+2\right).
$$

Each padding site has dimension $d$ and input $I/d$. No physical gate acts on a padding site. Since $\delta\le 1/d$, the same input eigenvalue floor holds. Identity maps satisfy the same gate faithfulness bound because $\alpha\le 1$.

The padded output is exactly

$$
\widetilde\rho
=\tau_{\mathrm{left}}\otimes\rho\otimes\tau_{\mathrm{right}}.
$$

Thus every reduced state on original sites is unchanged. The padding also places those sites away from the exceptional first emitted cell and the final retained memory in the sequential description below.

The construction is purely an aid to the proof. No operation on the original system is changed.

## 2. The geometric backward cone of a gate

For a gate $g$ in layer $t$, start with its support $S_g$ at the input of that layer. Traverse layers $t-1,t-2,\ldots,1$ backwards. Whenever a gate in an earlier layer has support intersecting the current set of wires, add its entire support to that set. Denote the resulting set of initial-site labels by $C(g)$.

This is a geometric wire-dependency cone. It includes every input wire of every ancestor gate. It is not minimized using special algebraic features of a channel, such as its ignoring or erasing an input.

Two elementary properties will be used.

**Spatial bound.** For every $x\in S_g$ and every $y\in C(g)$,

$$
|x-y|\le t(r-1)\le w.
$$

Indeed, at each backward layer a path can move by at most $r-1$ sites. The initial step within the support of $g$ obeys the same bound. Consequently the interval hull of $C(g)$ has length at most $2w+1$.

**Ancestor inclusion.** If $h$ is an ancestor of $g$ in the circuit DAG, then

$$
C(h)\subseteq C(g).
$$

Every initial wire that can reach $h$ can continue along the causal path from $h$ to $g$. Equivalently, the backward construction for $g$ contains the construction for each of its ancestor gates.

One can use DAG edges between consecutive gates on each physical site wire. Gates in a single layer have disjoint actual supports, so there is no within-layer ordering ambiguity. A topological ordering of this DAG preserves the original channel.

## 3. Assigning gates to the first coarse layer

Partition the padded chain into blocks

$$
I_i=\{(i-1)K+1,\ldots,iK\},
\qquad i=1,\ldots,M,
\qquad M=N/K.
$$

Assign a gate $g$ to block $i$ if

$$
C(g)\subseteq I_i.
$$

The assignment is unique when it exists. Let $F_i$ be the set of gates assigned to $i$.

By ancestor inclusion, $F_i$ is ancestor closed: every ancestor of a gate in $F_i$ is also in $F_i$. In particular, no gate left outside all the $F_i$ can be a predecessor of a gate in an $F_i$.

Every gate in $F_i$ acts on $I_i$, since $S_g\subseteq C(g)$. Compose the gates in $F_i$ in their original chronological order and denote the resulting channel on the entire block by $\mathcal F_i$, with identities on untouched sites.

All the $\mathcal F_i$ can be executed first. To see this directly, move the selected gates earlier in a topological ordering. A selected gate never has to pass an unselected predecessor. If two gates are reordered relative to their original chronology and share an actual site, the earlier one is a causal predecessor of the later one, so that reordering is prohibited by the DAG. Every permitted interchange therefore involves disjoint supports, for which the extended CPTP maps commute.

The channels $\mathcal F_i$ have disjoint block supports and form the first coarse layer.

## 4. Assigning all remaining gates to boundary strips

Let $g$ be a gate not assigned to any $F_i$. Its cone meets more than one block.

The interval hull of $C(g)$ has diameter at most $2w$, whereas successive block boundaries are $K>2w$ sites apart. Therefore the cone crosses exactly one boundary. Write that boundary as the cut between sites

$$
b_i=(i-1)K
\quad\text{and}\quad b_i+1,
\qquad i=2,\ldots,M.
$$

Choose $y_-\in C(g)$ with $y_-\le b_i$ and $y_+\in C(g)$ with $y_+\ge b_i+1$. For any $x\in S_g$, the spatial bound gives

$$
x\le y_-+w\le b_i+w,
$$

$$
x\ge y_+-w\ge b_i-w+1.
$$

Hence

$$
S_g\subseteq
T_i:=\{b_i-w+1,\ldots,b_i+w\}.
$$

The strip $T_i$ consists of the last $w$ sites of block $i-1$ and the first $w$ sites of block $i$. Distinct strips are disjoint because $K>2w$.

Let $\mathcal E_i$ be the chronological composition of all remaining gates assigned to boundary $i$, extended by the identity to $T_i$. There are no shared physical sites between different $\mathcal E_i$. After the first coarse layer has been executed, the remaining gates can therefore be arranged into the second coarse layer

$$
\bigotimes_{i=2}^M\mathcal E_i,
$$

with identities elsewhere.

We obtain the exact channel identity

$$
\boxed{
\widetilde{\mathcal C}
=
\left(\bigotimes_{i=2}^M\mathcal E_i\right)
\circ
\left(\bigotimes_{i=1}^M\mathcal F_i\right).
}
$$

The tensor products here are over disjoint supports within the respective coarse layer. The identity is valid on every input state. Product structure is used only in the next step, when the first-layer output is analyzed.

## 5. Independent resources and a uniform spectral floor

On block $i$, let

$$
\sigma_i
=\mathcal F_i
\left(\bigotimes_{x\in I_i}\omega_x\right).
$$

Because the initial state and the first coarse layer both factor over the blocks, the first-layer output is

$$
\bigotimes_{i=1}^M\sigma_i.
$$

The input on a block obeys

$$
\bigotimes_{x\in I_i}\omega_x\ge\delta^K I_{I_i}.
$$

If a state on that block is bounded below by $\lambda I_{I_i}$, applying one original gate gives

$$
(\Phi_g\otimes\operatorname{id})(\lambda I_{I_i})
\ge\lambda\alpha I_{I_i}.
$$

Let $N_i$ be the number of gates in $F_i$. In any original layer, at most $K$ nonempty pairwise disjoint gate supports can lie in a $K$-site block. Therefore

$$
N_i\le KD.
$$

Since $\alpha\le1$,

$$
\boxed{
\sigma_i
\ge\delta^K\alpha^{N_i}I_{I_i}
\ge\delta^K\alpha^{KD}I_{I_i}
=p_0I_{I_i}.
}
$$

This is a local spectral bound on a block of fixed size. No lower bound on the smallest eigenvalue of the entire many-body density operator is used.

## 6. Block parts, emitted cells, and retained memory

Split each block in spatial order as

$$
I_i=L_iM_iR_i,
$$

with

$$
|L_i|=|R_i|=w,\qquad |M_i|=K-2w.
$$

The boundary channel $\mathcal E_i$ acts on

$$
R_{i-1}L_i,
\qquad i=2,\ldots,M.
$$

Process the coarse representation from left to right. The state $\sigma_1$ initializes the emitted register $L_1M_1$ and the memory $R_1$. At step $i\ge2$:

1. introduce the independent resource $\sigma_i$ on $L_iM_iR_i$;
2. apply $\mathcal E_i$ to the incoming memory $R_{i-1}$ and $L_i$;
3. emit the output on $R_{i-1}L_i$, together with $M_i$;
4. retain $R_i$ as the next memory.

The emitted cell is the contiguous physical interval

$$
J_i=R_{i-1}L_iM_i,
\qquad i=2,\ldots,M,
$$

and it has exactly $K$ sites. The cells occur consecutively on the line. The first emitted interval $L_1M_1$ has $K-w$ sites, and the final memory $R_M$ has $w$ sites.

The earlier padding guarantees that all original sites lie between these exceptional end pieces. Buffers on the original chain therefore encounter only the regular $K$-site cell partition.

The sequential construction has exactly the same output state as the two coarse layers. The boundary channels have disjoint physical supports; they are being described sequentially only to track the conditional information.

Finally, because a product of density operators is bounded above by the identity,

$$
\sigma_i
\ge
p_0\,(\sigma_i)_{L_iM_i}\otimes(\sigma_i)_{R_i}.
$$

Every regular step thus satisfies the resource condition in [contraction.md](contraction.md), with the same $p_0$ and memory dimension at most $d^w$.

The original gate faithfulness assumption was used to guarantee full-rank first-layer resources. The boundary contraction itself permits arbitrary CPTP maps $\mathcal E_i$. This distinction does not enlarge the stated circuit theorem, but it identifies the exact place where the preparation hypothesis enters its proof.
