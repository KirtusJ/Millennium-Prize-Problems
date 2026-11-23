# The constant after the linear exterior energy

**A4 proof submitted for disproof.** For the homogeneous SU(2) Hamiltonian and the hard exterior support condition in the [preceding estimate](../README.md), let E(R) be the infimum of the energy over normalized form-domain states supported at Frobenius radius at least R. If a₁ is the largest negative zero of the Airy function Ai, then

$$4R+2|a_1|-O(R^{-1/2})\ \le E(R)\le\ 4R+2|a_1|+O(R^{-2}).$$

Thus the additive term in the earlier 4R+O(1) estimate tends to **4.676214820919534…**. It is the kinetic cost of the Dirichlet wall in the direction of the largest singular value. A smooth penalty or a different radius would require a fresh calculation.

### The four normal coordinates and their measure

Averaging the squared modulus over independent left and right O(3) rotations and taking the square root preserves support, norm and potential expectation, and can only lower kinetic energy. This follows from the Hilbert norm gradient bound in the preceding estimate. Hence the full infimum equals the one over functions of singular values. It also equals the scalar singlet infimum. Write x≥u≥v≥0 for the singular values and d²=u²+v². The radial kinetic form has integrand one half the sum of squared derivatives in x,u,v, since the three singular-value gradients are orthonormal at simple positive spectrum. The measure is proportional to (x²−u²)(x²−v²)|u²−v²| dx du dv. [Real SVD Jacobian, Edelman and Rao](https://math.mit.edu/~edelman/publications/random_matrix_theory.pdf)

Lift u,v to the singular values of a real 2×2 matrix B. Its Lebesgue measure supplies exactly the factor |u²−v²|. The quotient is therefore a weighted flat form on (x,B), restricted to invariant functions, with d=|B| and
$$W=x^4-x^2 d^2+(\det B)^2,\qquad V=2x^2d^2+2(\det B)^2.$$
The same radial gradient identity holds for B. This description uses the actual reflection-invariant form domain: no extra Dirichlet boundary is imposed at v=0 or u=v. Equivalently obtain the identities first on smooth invariant functions by integration in matrix coordinates, then use form closure. The top singular value remains isolated in the tube used below. A smooth invariant trial function of B and x there lifts locally to a matrix function using smooth orthonormal frames for the leading singular directions and their complements. Invariance makes its value independent of frame choices.

Inside d≤x/2 conjugate to flat measure by multiplying the function by √W. Integration by parts adds
$$U=\frac{\Delta\sqrt W}{2\sqrt W}=\frac{x^2}{W}-\frac{|\nabla W|^2}{8W^2}.$$
Indeed ΔW=4x² in the five flat variables. Here W≥9x⁴/16. The x derivative is at most 4x³ in magnitude and the B-gradient has norm at most 2x²d+d³, so |U|≤13/x². This estimate stays regular across both degeneracies of the smaller singular values.

### Lower estimate

Use two smooth cutoffs whose squares sum to one, the first supported in d≤2w and the second in d≥w, where w=R^(1/4). They can be taken as the cosine and sine of a smooth angle increasing from zero to π/2 on [w,2w]. The function d is distance to the rank-at-most-one matrices and is 1-Lipschitz. The quadratic-form localization error is O(w⁻²). Everywhere in the exterior x≥R/√3. On the outer piece V≥2R²w²/3. This dominates the claimed lower energy.

On the inner piece x≥x₀=R−4w²/R, by x²+d²≥R². For large R the piece lies inside d≤x/2. After conjugation extend by zero outside its support. It is an H¹ function supported on x≥x₀ and therefore has Dirichlet trace at x₀. There is no extension across a live boundary at u=x since the cutoff vanishes in a neighborhood of it. At every fixed x the four-dimensional oscillator in B with potential 2x²d² has ground energy 4x. Dropping the nonnegative determinant term retains the full x kinetic energy. The remaining lower operator is −∂ₓ²/2+4x on the Dirichlet half-line, up to O(R⁻²) from U. Its lowest energy is 4x₀+2|a₁|, with eigenfunction proportional to Ai(2(x−x₀)+a₁). Summing the localized estimates loses O(w⁻²+w²/R)=O(R⁻¹ᐟ²).

### Upper estimate

In flat measure take the normalized Dirichlet Airy ground state starting at x=R times the normalized four-dimensional Gaussian oscillator ground state proportional to x exp(−x d²). Extend by zero to x<R. The packet satisfies the original exterior constraint because its Frobenius radius is at least x. Cut off smoothly at d/x between 1/4 and 1/2 before conjugating back. Gaussian tails there and all fixed polynomial derivative factors contribute O(exp(−cR³)) to norm and energy, with c>0 possibly decreased to absorb polynomials.

In the uncut Gaussian each matrix entry has variance 1/(4x). Its x derivative is orthogonal to it and has squared norm 1/(2x²), from the variance of d². The determinant potential has mean 2 E[(det B)²]=1/(4x²). Thus the extra longitudinal kinetic term and determinant term together cost 1/(2x²); the cutoff Jacobian term is bounded in absolute value by 13/x². Normalizing the cut packet gives the stated upper estimate. It is invariant under left and right rotations, so it supplies the same upper estimate in the singlet sector.

### Checks and scope

The six guest-generated Lean lemmas verify polynomial identities, the wall shift, the Airy scaling and the Gaussian variance algebra. The analytic form-domain and localization arguments above are submitted for independent review. The [numerical control](check_constants.py) differentiates the Jacobian independently at 81 matrices and solves the one-dimensional Dirichlet problem on [0,12] by finite differences. At 512, 1024, 2048 and 4096 intervals the respective absolute errors against 2|a₁| are 0.0004004, 0.0001001, 0.00002502 and 0.000006256. These checks concern the reduced operator. The theorem concerns large field amplitude at fixed homogeneous dynamics. It supplies neither a full Wilson ensemble measurement nor a bound uniform in spatial volume.
