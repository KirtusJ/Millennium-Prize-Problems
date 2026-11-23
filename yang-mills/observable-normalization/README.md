# A nonzero observable at positive physical separation

Director A4 · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

A normalized lattice observable can have positive variance at every cutoff while losing all its correlations at positive physical time. For a centered observable with positive finite spectral measure, write

$$C_n(t)=\int_{[0,\infty)}e^{-tE}\,d\mu_n(E).$$

Fix the observable smearing, the renormalization prescription and the physical clock across cutoffs. The vacuum component must have been removed. The following tests apply to this scalar spectral representation, conditional on having constructed it for the theory of interest. [Official Yang–Mills problem](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## Two failure cases

* If $\mu_n=n^{-1}\delta_1$ for $n\ge1$, every finite spectrum starts at one while $C_n(t)=e^{-t}/n$ vanishes in the limit. Dividing by $C_n(0)$ would discard evidence that the prescribed observable vanishes.
* If $\mu_n=\delta_n$, then $C_n(0)=1$ at every cutoff, yet $C_n(t)=e^{-nt}$ tends to zero for every fixed $t>0$. Equal-time normalization alone allows all the weight to move to arbitrarily high energy. A uniform positive lower spectral threshold also holds in this example.

In contrast, the fixed family $\delta_1$ retains the correlator $e^{-t}$. These examples can all be realized as spectral measures of a vector for a diagonal nonnegative Hamiltonian alongside a separate vacuum vector. None constructs a Yang–Mills field.

## A sufficient estimate with measurable inputs

For finite positive sums the checked lemma `momentLowerBound` gives

$$ C_n(t)\ge C_n(0)-t\sum_i w_{n,i} E_{n,i}.$$

The proof applies $e^x\ge1+x$ to each atom and sums with positive weights. For positive Borel measures the same calculation integrates the pointwise inequality when the first moment and total mass are finite. The Lean file checks the finite-sum version. If $v\le C_n(0)\le V$ with $v>0$, the first moment is at most $M>0$, and $E_{n,i}\ge0$, choose the same physical time $t_*=v/(2M)$ for every cutoff. Then $v/2\le C_n(t_*)\le V$. If $M=0$, positivity of energy and weights puts the measure at zero. That case would require scrutiny of vacuum centering and ground-state degeneracy. A first-moment bound is sufficient and can be stronger than necessary.

If the correlators converge at $t_*$, `separatedTimeWitness` passes the two eventual bounds to the limit and proves strict positivity. Under Osterwalder–Schrader reconstruction with the stated correlator identification, this would witness a nonzero centered vector. Establishing that a particular renormalized, gauge-invariant smeared observable obeys these bounds along a four-dimensional continuum and infinite-volume trajectory remains open. A positive correlator alone also allows $\mu$ with support arbitrarily near zero.

## Relation to the parent program

Kirtus Justus’s E1 treats feasibility of positive spectral measures under finitely many moment and Laplace observations. Its optimized lower support endpoint is an upper bound on the endpoints compatible with those data. Here the first moment instead prevents total loss of weight at a fixed positive time. Neither estimate supplies a lower bound on the full excited spectrum. [E1 source at the inspected revision](https://github.com/KirtusJ/From-Prephysical-Hypotheses-to-Physical-Models/blob/aca29276aa180af3c81ccc9f3aa06b4e2ae4d404/edition/PAPERS/E1_Positive_Spectral_Measures_Under_Finite_Moment_and_Laplace_Constraints/source/01_editable_Positive_Spectral_Feasibility.md)

## Next calculation

For a candidate transfer Hamiltonian and centered vector, the two inputs are the squared norm and the energy quadratic form in physical units. Determine whether fixed physical smearing yields a positive lower norm and a cutoff-independent upper energy form along the same trajectory used by B4, D4 and G4. A divergent first moment defeats this sufficient test and leaves other tightness estimates open. A lower bound obtained only by changing smearing or units with each cutoff needs a separate identification theorem.

[Spatial smearing of the conserved Hamiltonian energy](energy-density/) gives an exact first moment in terms of local weight differences and a cutoff-uniform compactness test for a time-differenced energy density.

[Three periodic Wilson partition functions](replica-gap/) bound the full finite-box transfer gap. At the SU(2) electric endpoint the first multiplet gives an explicit magnetic susceptibility, dispersion, and two-copy measurement variance.

[Uniform isolation of the first Wilson transfer band](uniform-band/) gives the volume-independent spectral estimate and its strong-coupling mass expansion.

[Boundary weight above the bulk static spectrum](boundary-weight/) bounds the fraction carried by a fixed open-cube boundary layer.

[Periodic thermal transition frequencies](thermal-transitions/) tests the number of nonzero energy differences visible in the matched slice-flow measurements.

[Minimal two-charge winding supports](winding-count/) counts bends and gives the leading fixed-box Bernoulli witness probability.

[Directional winding-energy bounds](winding-rate/) applies displacement-weighted walks to the charged Wilson sectors.

[Unit-coupling plaquette spectral window](plaquette-window/) bounds both lattice-energy endpoints using two exterior slices and the fundamental-link tensor rule.

[A finite difference of cube-centered plaquettes](filtered-contrast/) isolates the quartic overlap and its eleventh-power spectral weight.
