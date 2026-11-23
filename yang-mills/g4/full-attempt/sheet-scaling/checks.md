# Wilson-sheet checks

### Vacuum normalization from two electric eigenstates

In the finite-box Hamiltonian let $e_4=6/\kappa$ and $e_6=9/\kappa$ be the electric energies of a fundamental square and a two-tile rectangular loop. A unit-norm unnormalized square trace $\chi_p$ occurs in the first vacuum correction with coefficient $1/(2e_4)$. Its normalized vacuum expectation has linear coefficient $1/(2e_4)=\kappa/12$. This follows directly from the normalized magnetic insertion $\chi_p/2$. [Hamiltonian formulation](https://doi.org/10.1103/PhysRevD.11.395)

For adjacent faces $p,s$, the normalized rectangular reading $W=\chi_R/2$ satisfies $\langle W,\chi_p\chi_s\rangle_0=1/4$ by shared-link Haar integration. At order two the center rule permits just the two faces, and the first vacuum correction on them is $v_1=(\chi_p+\chi_s)/(2e_4)$. With the constant Fourier component of the vacuum fixed to one, the second correction on the rectangular eigenstate is obtained by dividing the corresponding matrix element of $A v_1$ by $e_6$. Consequently
$$
 [j^2]\pi_j^H W
 =2\langle W,v_2\rangle+\langle v_1,Wv_1\rangle
 =\frac1{4e_4e_6}+\frac1{8e_4^2}=\frac{7\kappa^2}{864}.
$$
The vacuum norm denominator multiplies a zero constant and linear numerator here. The two contributions check the first rectangular coefficient independently of the strip generating function. [Electric spectrum and normalization](../electric.md) · [Finite nonabelian vacuum controls](../all-readings/checks.md)

### Height comparison and the strip spectrum

For a checkerboard assignment $x_i=\pm(1/2-\delta)\epsilon$ inside the cell centered at zero, every incidence contributes its full rounding error. The per-tile difference of energies is $(2-4\delta)\epsilon$. Thus the uniform constant two in the **pointwise cell estimate** cannot be reduced. Averaging over a cell can give smaller errors. The exact subset recurrence tests twelve rectangle/coupling pairs, including $3\times3$ at $q=0.99$. There the log difference per tile is $0.000050018$ and the proven upper bound $2\epsilon$ is $0.0201007$. [Numerical and exact tests](check.py)

The run recurrence and independent division of the power series of $J_1(x)/x$ and $J_1'(x)$ agree over the rationals through degree 40. Computing all positive and negative height-support subsets also agrees for lengths one through nine. The strip gives $C_4=73/720$, while four tiles in a square give $35/288$. This is one way to distinguish a coefficient depending on shape from a coefficient depending only on area.

The first positive zero of $J_1'$ lies between $1.84118378134065$ and $1.84118378134067$. Alternating rational Taylor sums rigorously give opposite derivative signs at the endpoints. On $0<x\le2$, the differentiated alternating series gives $J_1''(x)\le-3x/8+5x^3/96<0$, since its remaining terms start negative and decrease in magnitude. This identifies the first root. It gives $\lambda_*=0.589977860244\ldots$ and pole amplitude $0.836834888772\ldots$. A worker’s first decimal approximation to the amplitude was inconsistent with its own formula. The exact series and the derivative-root bracket resolve it. [Bessel series](https://dlmf.nist.gov/10.2) · [Zeros](https://dlmf.nist.gov/10.21.i)

| Height spacing $\epsilon$ | Top eigenvalue of scaled integer-height transfer truncated to $|x|\le8$ |
| ---: | ---: |
| 0.4 | 0.65600714 |
| 0.2 | 0.60556178 |
| 0.1 | 0.59380959 |
| 0.05 | 0.59093171 |
| 0.025 | 0.59021607 |

For the independent spatial transfer computation, the program multiplies the finite matrix by positive vectors and checks that all componentwise eigenvalue ratios agree. The analytic truncation error in operator norm is at most $\epsilon\sqrt{2ST}$, where $S=(1+q^2)/(1-q^2)$ and $T=2q^{2(M+1)}/(1-q^2)$ for integer height cutoff $M$. This bounds the Hilbert–Schmidt norm of the omitted entries by summing rows or columns outside the interval. The largest such bound in the table is less than $0.00047$. The tabulated eigenvalues are numerical. The Bessel quotient and the limit theorem have independent proofs. [Transfer code](check.py) · [Strip proof](strip.md)

### Formal scope and provenance

The five [Lean declarations](SheetScaling.lean) prove the single-edge rounding bound, its finite-graph sum, the square-lattice incidence budget, and the scalar algebra of the signed runs and pole amplitude. The real integral, Hamiltonian expansion, spectral operator and Bessel-function solution are derived in the two manuscripts. Lean 4.19.0 with Mathlib at `c44e0c8ee63ca166450922a373c7409c5d26b00b` compiled the final source with standard logical axioms only. Four false alternatives are rejected. G4 corrected nested absolute-value syntax and the library lemma spelling in the worker’s first draft. The compiler initially found a mutation selector that matched two lines; the deposited selector identifies the theorem statement uniquely. [Adverse variants](mutations.json)

Three PCP builder–challenger commissions and a further challenge of the final manuscripts and their Wilson input are archived. They share a model provider. The verifier checks 13 hosted registers, the separate compiler results, the six native packet and capability cases, the source emitted in three native guests and the exact and numerical controls. The source is pinned to its SHA-256 digest in the archive. [Evidence archive](evidence.zip) · [Verifier](verify.py)

Use `python -B verify.py` with NumPy from this directory. Add `--runtime /path/to/PCP_OS_Python --method /path/to/PCP/Method` to replay the register histories. From the pinned Mathlib checkout, `lake env lean /absolute/path/to/SheetScaling.lean` rechecks the source. The area limit here is taken in units of the fixed spatial lattice, at the first nonzero magnetic order for each loop. Spatial refinement of a nontrivial Yang–Mills field with a finite physical mass gap remains open. [Independent fixed-scale attempt](../README.md)
