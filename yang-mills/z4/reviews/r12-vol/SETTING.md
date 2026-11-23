## Setting: free lattice Maxwell theory in Hamiltonian form

Periodic cubic lattice of side N, spacing b, physical side ℓ = Nb. Real link variables A_i(x), conjugate E_i(x), [A_i(x), E_j(y)] = i δ_ij δ_xy. Plaquette angle θ_ij(x) = A_i(x) + A_j(x+e_i) − A_i(x+e_j) − A_j(x).

H = (g²/2b) Σ E_i(x)² + (1/(2g²b)) Σ_{x, i<j} θ_ij(x)², on the Gauss-law subspace, zero modes removed.

Lattice momenta k ∈ (2π/ℓ)ℤ³ in the Brillouin zone, k̂_i = (2/b) sin(k_i b/2), k̂ = |(k̂_1, k̂_2, k̂_3)|. Each k ≠ 0 carries two transverse oscillators of frequency ω(k) = k̂. The physical magnetic field is B_3(x) = θ_12(x)/(g b²). Its vacuum two-point function at Euclidean time separation t ≥ 0 is

D_t(x − y) = ⟨B_3(x) e^{−tH} B_3(y)⟩ = ℓ⁻³ Σ_{k ≠ 0} e^{ik·(x−y)} · ((k̂_1² + k̂_2²)/k̂²) · (k̂/2) · e^{−t k̂}

(the factor (k̂_1² + k̂_2²)/k̂² is the transverse projector for the 3-component; the normalization k̂/2 is to be rederived by the worker, not assumed).

Observable: for a smooth f of fixed physical width, O_b(f) = b³ Σ_x f(bx) (B_3(x)² − ⟨B_3²⟩). It is the free-theory image of a smeared plaquette action: for a compact group the plaquette character is 1 − const·g²b⁴·B² + higher order.

Correlator: C_b(t) = ⟨O_b(f) e^{−tH} O_b(f)⟩. The vacuum is Gaussian, so by Wick's theorem C_b(t) = 2 b⁶ Σ_{x,y} f(bx) f(by) D_t(x−y)².

## Statements
