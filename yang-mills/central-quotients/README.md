# Central quotients in a Yang–Mills regulator

Director C4 · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Averaging the fundamental SU(2) Wilson weight over the lifts of its SO(3) edge variables couples the faces of even a single cube.** At the identity configuration and $\beta=\log 2$, the exact pushforward density is $8177/2048$. Averaging the six face signs independently gives $15625/4096$. The discrepancy is $729/4096$. This identifies a specific change of measure that a comparison of mass gaps across gauge groups must account for.

Clay asks for a nontrivial four-dimensional continuum theory and a positive gap for each compact simple gauge group. We examine the first central quotient, $SU(2)\to SO(3)$. The calculations concern finite regulators and flat torus holonomy. The continuum construction, physical mass scale, and gap remain open. [Jaffe–Witten, §4](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## Which density reaches the quotient?

Let $E$ be the edges of a finite plaquette complex, with one independent normalized Haar variable per unoriented edge. Use the inverse on traversing the edge backwards. For a quotient edge configuration, choose lifts $U_e\in SU(2)$ and write $t_p=\tfrac12\operatorname{Tr}(U_{\partial p})$. Another lift multiplies each edge by a sign $z_e$. Its plaquette trace is $z_{\partial p}t_p$, where $z_{\partial p}$ is the product of the signs along the boundary, with repetitions.

Normalized Haar measure pushes forward to normalized Haar measure because its pushforward is a left-invariant probability. Averaging over the finite kernel on every edge leaves all integrals of functions pulled back from the quotient unchanged. Consequently the following is the density, relative to product quotient Haar and before the common partition-function normalization, of the pushforward of the fundamental Wilson regulator.

$$
W(\bar U)=2^{-|E|}\sum_{z\in\{\pm1\}^{E}}
                 \exp\!\left(\beta\sum_p z_{\partial p}t_p\right)
=\prod_p\cosh(\beta t_p)
  \sum_{S:\,\partial S=0\; (\mathrm{mod}\,2)}
                 \prod_{p\in S}\tanh(\beta t_p).
$$

To obtain the second expression, expand each exponential as its cosh term plus its signed sinh term. An edge sign with odd total exponent averages to zero. All remaining sign products equal one. This argument includes any closed two-chain allowed by the chosen boundary conditions. Changing the reference lifts merely permutes the first sum. It also leaves every surviving term of the second sum invariant. Related work on Wilson weights and center variables includes the $SO(3)\times\mathbb Z_2$ formulation studied by Alexandru and Haymaker. [Alexandru–Haymaker](https://arxiv.org/abs/hep-lat/0009013)

On the boundary of a cube, a closed set of selected faces contains either none or all six. Each edge forces its two incident faces to have equal membership, and face adjacency is connected. Thus the exact answer is the product of the six coshes **plus the product of the six sinhes**. At the identity the two products at $\beta=\log 2$ are $(5/4)^6$ and $(3/4)^6$. An edge with trace zero and all other edges equal to the identity instead gives two zero plaquette traces. The ratio of the exact density to the product of coshes is then one, whereas at the identity it is $1+(3/5)^6$. Both weights are continuous and product Haar has full support. No choice of constant normalization makes these two densities agree almost everywhere.

For a genuinely center-invariant weight $w$ on quotient edge space, the measure with density $w\circ q^E$ on the cover pushes forward exactly to the measure with density $w$ downstairs. For the fundamental Wilson action, $W$ above gives the corresponding exact comparison for all bounded quotient observables, including products at separated times. A gap argument using an independently specified SO(3) regulator must relate its dynamics to this density along the same continuum trajectory, or establish convergence for its own regulator. A useful next estimate would control changes of **connected** local correlators from the closed-surface terms uniformly in volume and lattice spacing at fixed physical separation. The one-cube discrepancy rules out exact independent-face factorization and gives no such bound.

The calculation extends to a strip of arbitrary length. A second explicit configuration fixes the density ratio at one, while at the identity the ratio grows at least exponentially in the number of cubes. [Strip estimate and three exact checks](cube-strip.md)

## A positive gap in the parent program’s one-link quotient

For K. Justus’s E2 convolution with coupling $\gamma>0$, the quotient comparison can be completed. Pullback identifies $L^2(SO(3))$ with the functions on $SU(2)$ satisfying $f(-U)=f(U)$. The quotient kernel is the center average $\cosh(\gamma\operatorname{Tr}(UV^{-1})/2)/Z_\gamma$. In the dimension-$n$ representation $\mathrm{Sym}^{n-1}(\mathbb C^2)$, the central element $-I$ multiplies by $(-1)^{n-1}$. Only odd $n$ survive. E2 diagonalizes the convolution with eigenvalue $I_n(\gamma)/I_1(\gamma)$ and shows strict decrease in $n$. The first excited quotient mode is therefore $n=3$, with multiplicity nine in the full regular space and one in the character space. [FPHPM, E2 §1](https://github.com/KirtusJ/From-Prephysical-Hypotheses-to-Physical-Models/blob/aca29276aa180af3c81ccc9f3aa06b4e2ae4d404/edition/PAPERS/E2_Compact_Group_Transfer_Spectra_and_Ultraviolet_Operator_Limits/source/01_editable_Compact_Group_Transfer_Operators.md)

Write $r=I_2/I_1$, $s=I_3/I_2$, and $\lambda=I_3/I_1$, all at $\gamma$. E2 gives $0<r,s<1$. The recurrence $I_1-I_3=4I_2/\gamma$ gives both $\gamma(1-\lambda)=4r$ and $r=\gamma/(4+\gamma s)$. Consequently the abstract one-link gap satisfies

$$
-\gamma\log\lambda \;\ge\; \gamma(1-\lambda)
=4r\;>\;\frac{4\gamma}{4+\gamma}.
$$

This lower bound works at every positive coupling and tends to the exact limiting energy $4$ from E2’s fixed-order asymptotics. It also gives a concrete check on any use of the $n=2$ excitation after projecting to $SO(3)$. The proof here is analytic; the nine Lean declarations below concern the finite regulator. Spatial plaquettes introduce shared signs, as the cube calculation demonstrates. Physical time and a uniform four-dimensional gap remain open. [DLMF 10.29.1](https://dlmf.nist.gov/10.29.E1) · [B4’s cover calculation](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/b31a34c79c81ba627a128ba17fb1a36fba83c39e/yang-mills/transfer-operator/README.md)

## When flat holonomies lift

View $SU(2)$ as the unit quaternions acting by conjugation on the imaginary quaternions; the kernel is $\{1,-1\}$. The images of $1,i,j,k$ form a Klein four subgroup of $SO(3)$. In particular, the half-turns about the first two coordinate axes commute. Their four possible pairs of lifts all anticommute since $ij=k=-ji$. Sending the first two generators of $\mathbb Z^4$ to those rotations and the remaining two to the identity gives a flat $SO(3)$ representation of the four-torus with no flat $SU(2)$ lift. Each individual edge or generator still lifts. This is a boundary-condition check on a periodic approximation. It supplies no topological obstruction to a construction directly on $\mathbb R^4$. [Schweigert, §§1–2](https://arxiv.org/abs/hep-th/9611092)

For any family taking values in this Klein four subgroup, signs can produce pairwise commuting lifts exactly when every pair has zero commutator sign. Label the four elements by vectors in $\mathbb F_2^2$. The commutator sign exponent of a pair is its determinant over $\mathbb F_2$. For an ordered four-tuple this produces six bits. Their alternating matrix has rank at most two, and its Pfaffian vanishes. The finite enumeration distinguishes counts of tuples from counts of bit patterns.

| Four cycles in this fixed Klein four subgroup | Ordered tuples | Distinct six-bit patterns |
|---|---:|---:|
| A simultaneous flat lift exists | 46 | 1 |
| No simultaneous flat lift exists | 210 | 35 |
| Total | 256 | 36 |

The rank-zero case has one all-identity tuple and $3(2^4-1)$ tuples taking values in a single order-two subgroup. For rank two, write the four columns as a $2\times4$ matrix. Its two row vectors span a plane in $\mathbb F_2^4$. There are $15\cdot14/(3\cdot2)=35$ planes; each has six ordered bases and determines its unique nonzero exterior square over $\mathbb F_2$. This recovers the computed multiplicities. The table counts neither bundles with a quantum weight nor all flat connections up to conjugacy.

The parent program already distinguished local from global holonomy in its $\mathbb{RP}^2$ reflection example. Here the global test uses an explicit central commutator, followed by a separate calculation of the measure. The earlier geometric result is internal provenance for the question. [FPHPM, Director B, Proposition “Full holonomy of $\mathbb{RP}^2$”](https://github.com/KirtusJ/From-Prephysical-Hypotheses-to-Physical-Models/blob/aca29276aa180af3c81ccc9f3aa06b4e2ae4d404/edition/REVIEW_RECORDS/Directors_A_B_G_2026-11-12/Director_B_Initial_External_Grounding_2026-11-12_B1/research/Finite_Homogeneity_Holonomy_and_Composition_Obstructions.tex)

## Formal coverage

The Lean definitions use integer Hamilton multiplication, explicit signed lifts, and a cube with twelve edges. Nine generated theorems check the finite identities. The classification of Klein-four tuples, the commuting-lift criterion, the four-cycle Pfaffian, and the cube counts are kernel-checked. For the cube, 32 even face-sign patterns each have 128 edge assignments. The direct integer sum of 64 times the Boltzmann weight over 4096 edge assignments is 1,046,656. Dividing by $64\cdot4096$ gives $8177/2048$. The covering-group interpretation, Haar pushforward and general surface expansion have the mathematical arguments above. The Lean file does not formalize measure theory or quantum-field reconstruction. [Definitions](Model.lean) · [Generated proofs](CentralQuotient.lean) · [Execution and replay](execution.md)

## Local response and observable histories

The open cube strip has an exact binary sign chain and a sharp conditional decay rate at every finite coupling. In a continuous-time single-plaquette model the complete history of center-even observations detects the entire interacting class-function sector. Its first spectral weight can nevertheless vanish with the coupling. [Strip theorem](local-response/) · [Transfer test](local-response/transfer.md) · [Observable sector and its gap](local-response/rotor.md)

For finite spatial graphs with analytic potentials and positive elliptic electric terms, complete histories of quotient links generate the physical sector fixed by the center symmetries of the potential. This gives the full cover spectrum on a simply connected box for the fundamental \(SU(N)\) Wilson Hamiltonian. [Finite-graph proof and torus checks](local-response/finite-graph.md) · [Compact connected groups and fixed time mesh](local-response/analytic-groups.md)
