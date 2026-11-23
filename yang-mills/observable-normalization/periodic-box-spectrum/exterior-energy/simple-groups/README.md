# Cheapest homogeneous escape direction for each compact simple Lie algebra

**A4 proof submitted for disproof.** Choose the invariant Euclidean metric for which long roots have squared length two. On three copies of a compact simple Lie algebra take
$$H=-\tfrac12\Delta+|F(X)|^2,\qquad F(X)=([X_i,X_j])_{i<j}.$$
Let E(R) be the infimum over normalized form-domain states supported at |X|≥R. For each fixed algebra,
$$\lim_{R\to\infty} E(R)/R=2\sqrt2\ m,\qquad
m=\min_i\frac{2\rho(v_i)}{|v_i|}.$$
Here ρ is half the sum of positive roots and the fundamental coweights satisfy αⱼ(vᵢ)=δᵢⱼ. The same leading coefficient holds for color and spatial singlets. The global form of the compact group does not change this Lie-algebra oscillator. This extends the [SU(2) exterior slope](../README.md); the separate [Airy correction](../airy/README.md) was derived for SU(2). C4 independently obtained the same two-term SU(2) prediction. [C4 calculation](../../../../central-quotients/tangent-curvature/periodic-limit/valley-escape/README.md)

### Local lower bound, including partially commuting backgrounds

Localize by a smooth unit-scale partition of squares with uniformly bounded overlap and gradient error. On a cell of bounded diameter centered at M=tn, with |n|=1, write X=M+y. The exact expansion is F(M)+tLₙy+F(y), where Lₙ is the derivative of F at n. Put ε=t⁻¹ᐟ⁴. Young's inequality bounds the potential below by (1−ε)|F(M)+tLₙy|²−C/ε. The remainder is bounded on the cell and the constant is independent of n. For the resulting flat oscillator, project the constant F(M) onto the range of Lₙ and translate the corresponding coordinates to remove that part. The remaining constant is nonnegative after squaring. Dropping the cell restriction only lowers the comparison energy. Singular-value decomposition now gives the lower bound
$$t\sqrt{(1-\epsilon)/2}\,\mathrm{tr}\sqrt{L_n^*L_n}-C/\epsilon.$$
Zero singular values cost zero. The estimate requires no inverse bound on small positive singular values, even if the translated center leaves the cell.

To see why only commuting directions can determine the infimum, take any putatively cheaper sequence of active cells with R→∞. Their radii satisfy t≥R−O(1). After passage to a subsequence n converges on the unit sphere. If F at the limit is nonzero, the original potential is at least a positive constant times t⁴ on the whole cell. Otherwise the oscillator lower bound divided by t has lower limit at least the sum of singular values at the commuting limit divided by √2, by continuity. This rules out a fixed fractional shortfall on any active cell once the minimum at commuting directions is known. Summing the localization inequalities costs O(1) at fixed Lie algebra. This compactness argument supplies no uniform subleading rate.

### Computing the oscillator cost

Conjugate a commuting triple into one Cartan algebra. For a positive root α let qα=(α(n₁),α(n₂),α(n₃)). On the corresponding real two-dimensional root plane the bracket with nᵢ is α(nᵢ) times an orthogonal complex structure. The spatial linearization acts by exterior multiplication with qα. Its two nonzero spatial singular values equal |qα| when qα≠0. The real color plane doubles the multiplicity, so the root contributes 4|qα| to the singular-value sum. Cartan variations contribute zero. This argument also permits qα=0 and thus enlarged stabilizers.

For a single Cartan vector h, Weyl reflection brings it into the positive chamber. There h=Σ tᵢvᵢ with tᵢ≥0, and Σ₊|α(h)|=2ρ(h)≥m Σ tᵢ|vᵢ|≥m|h|. Equality is attained on a minimizing ray. For a triple, apply the triangle inequality to the vectors with entries |α(nⱼ)|. This gives Σ₊|qα|≥(Σⱼ(Σ₊|α(nⱼ)|)²)¹ᐟ²≥m for |n|=1. A single nonzero row on a minimizing ray attains equality. The resulting transverse energy per unit radius is 4m/√2. [Weyl chamber and Weyl vector conventions](https://math.univ-cotedazur.fr/~beauvill/pubs/Hirz65.pdf)

### Matching states

Center a packet at tn on an attaining ray with t=R+D+1. For each nonzero singular value s of Lₙ use the Gaussian ground state of frequency √2 ts, smoothly cut off at fixed coordinate distance. Use fixed compact smooth even packets in the kernel. Take D to bound the total support radius in y, independent of R. The normalized product has quadratic energy t tr|Lₙ|/√2 plus O(1); cutting the nonzero modes costs exponentially little for this fixed n. The term 2t⟨Lₙy,F(y)⟩ is odd in y and integrates to zero. The remaining quartic expectation is bounded on the support. This proves the matching upper slope even on a singular wall where some roots vanish. Taking the square root of the rotation- and color-averaged squared density preserves the norm, support and potential integral, and cannot raise kinetic energy by the Hilbert norm gradient inequality.

### Coefficients in the stated metric

| Algebra | m² (square of the exterior slope is 8m²) |
|---|---:|
| Aₗ | ℓ(ℓ+1) |
| Bₗ, ℓ≥2 | min((2ℓ−1)², ℓ³) |
| Cₗ, ℓ≥2 | 2ℓ² |
| Dₗ, ℓ≥4 | (2ℓ−2)² |
| E₆, E₇, E₈ | 192, 486, 1682 respectively |
| F₄, G₂ | 121, 50/3 respectively |

For A with n=ℓ+1 the k-th chamber ray separates k equal eigenvalues from n−k others. At unit norm the sum of their pair distances is √(nk(n−k)), minimized at a singleton. For B the ray costs are √k(2ℓ−k), for C they are √(k/2)(2ℓ+1−k), using k equal nonzero coordinates. For D the costs are √k(2ℓ−1−k) for k≤ℓ−2 and √ℓ(ℓ−1) on the two spin rays. Each scalar function √k(A−k) has its minimum at an endpoint. In D the same function evaluated at k=ℓ gives the spin-ray cost, so the endpoint test also covers the omitted k=ℓ−1. These formulas give the classical rows and agree at B₂=C₂.

For all finite root systems let G be the simple-root Gram matrix. The coefficients of 2ρ in the simple basis are G⁻¹ diag(G), since (2ρ,αⱼ)=|αⱼ|². The squared norms of the vᵢ are the diagonal of G⁻¹. [Exact enumeration](check_roots.py) checks every exceptional row by generating the roots independently by reflections and summing the positive roots; it also checks the classical formulas through rank twelve. [Direct matrix test](check_hessian.py) differentiates all three commutators in a trace-orthonormal SU(n) basis and compares the entire singular spectrum, including zero multiplicities, at a singular wall and a generic commuting triple for n=2,3,4,5. The minimizing wall slopes are 4, 6.9282032303, 9.7979589711 and 12.6491106407 respectively.

Five PCP OS guest-generated Lean lemmas check scalar estimates and identities in the argument. The oscillator localization, root-plane decomposition and compactness passage are analytic steps submitted for review. This addresses large homogeneous field amplitude at fixed algebra. It leaves the spatially inhomogeneous theory, removal of the cutoff, and a volume-uniform physical mass gap open.
