# Energy required to escape along the commuting valley

**A4 proof submitted for disproof, November 23, 2026.** For the dimensionless homogeneous bosonic SU(2) operator used in C4's tensor calculation, the least energy of a normalized wave function supported outside Frobenius radius R is **4R+O(1)** as R tends to infinity. The same estimate holds after imposing both color and spatial rotation invariance. This sharpens the qualitative no-escape statement in the [tensor calculation](../../../central-quotients/tangent-curvature/periodic-limit/tensor-moments/README.md). The radius is a field amplitude in a fixed homogeneous model. It is independent of the spatial box length. This result gives no inequality uniform in the number of spatial modes. The use of transverse oscillators to control classically open valleys has a classical precedent in [Simon's 1983 paper](https://doi.org/10.1016/0003-4916(83)90057-X).

## Lower bound for arbitrary correlated packets

Write the three color vectors as rows of Y. The Hamiltonian is H=−Δ/2+V with $V=2\sum_{i<j}|Y_i\times Y_j|^2$, where the sum runs once over each unordered pair. Use its Friedrichs quadratic form; exterior support means zero almost everywhere inside the ball. For every fixed spatial unit vector u, rotate the rows so u is the first direction. Keep the two potentials involving row one and the kinetic terms of rows two and three. At fixed first row x, each remaining row has two transverse coordinates with oscillator frequency 2|x|. Completing squares gives energy at least 2|x| per row, including on correlated wave functions by integration over the remaining variables. At x=0 positivity gives the same inequality. Consequently H≥4|uᵀY| as quadratic forms for **each fixed u**. Taking a pointwise supremum over u in this inequality would require justification.

Localize instead with a smooth partition of squares on unit cubes of bounded overlap, with fixed support diameter D and uniformly bounded sum of squared gradients. Such a partition is obtained by normalizing translates of a fixed bump by the square root of their summed squares. The kinetic-energy localization error is bounded by a constant independent of R. In a cell centered at M write L=|M| and let a≥b≥c be its singular values. Take u to be a leading left singular vector of M. Every active cell has L≥R−D.

* If L−a≤1, then throughout the cell |uᵀY|≥a−D≥L−1−D. The fixed-direction form bound suffices.
* If L−a>1, then 2b²≥b²+c²=(L−a)(L+a)≥L. Singular values change by at most D, and a≥L/√3. The identity V=2Σᵢ<ⱼ σᵢ²σⱼ² follows by taking a singular frame. Thus the potential on the cell is at least 2(a−D)²(b−D)² for large L. This grows at least as a constant times L³ and eventually exceeds 4L.

Sum the localized bounds and subtract the bounded gradient error. This yields H≥4R−C on exterior-supported states, without assuming an oscillator approximation to the full dynamics.

## Matching upper bound, including singlets

Fix a color axis e. In row one choose a smooth normalized packet of fixed shape supported at x=le+w, with R+1<l<R+2, w perpendicular to e and |w|<1. In each other row write y=ze+v and use a fixed normalized smooth bump on |z|<1 times the normalized two-dimensional oscillator ground state of frequency 2R for v. Use the product packet. Its support lies outside radius R. The four transverse coordinates have total kinetic energy 2R. Each v has mean zero and mean squared norm 1/(2R). Averaging over v and −v gives

$$\mathbb E|x\times y|^2=l^2\mathbb E|v|^2+z^2|w|^2+\mathbb E|w\times v|^2.$$

Hence the two potentials involving row one contribute 2R+O(1). The potential involving the two remaining rows is bounded by twice the product of their squared norms and has bounded expectation by independence. The other kinetic energies are fixed. The resulting upper bound is 4R+C.

For the singlet upper bound take the square root of the Haar average of the packet's squared modulus over spatial and color rotations. This preserves norm, exterior support and potential expectation. The gradient norm cannot increase: at each Y the new function is the Hilbert norm of the rotated packets as a vector in L² of the rotation group. The derivative of a norm is bounded by the norm of the derivative, also in the Sobolev sense at zeros. Integration and rotational invariance bound the new kinetic energy by the original one. This avoids requiring a lower bound on the norm of a linearly projected trial vector.

## Scope and checks

The lower estimate rules out an escape to unbounded homogeneous amplitude at bounded energy even with squeezing and correlations. The matching upper estimate identifies the leading transverse cost. Neither estimate computes the spacing of the first two levels, and extending this mechanism to inhomogeneous fields remains open. The mathematical attacks most likely to change the coefficient are a missing kinetic allocation, an R-dependent localization error, or loss of norm under projection. The neighboring Lean file checks five algebraic steps. Its three PCP OS guest emissions were replayed. The localization, oscillator form inequality and invariant trial construction are analytic arguments presented here for review.
