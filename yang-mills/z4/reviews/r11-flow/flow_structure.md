# Spatial Wilson flow on one time slice: structural facts (r11-flow, Part B)

Status: proofs in text only. Nothing here is formalized. Each step is followed by its reason in brackets. "ASSUMED" marks a standard fact I did not prove. "NOT PROVED" and "OPEN" are used as defined in the brief. The numerical check of B1 (iii) and (iv) and of the gauge covariance is in `child/` (the sub-agent's program, rerun by me in `rerun_child/` with a byte-identical result).

## B1. Definition and the four properties

**Setting.**
- Λ is a finite periodic spatial lattice (N³ sites). G is a compact connected Lie group, for example SU(N).
- 𝔤 is its Lie algebra, with the Ad-invariant inner product ⟨X, Y⟩ = −2 tr(XY) for a matrix group.
- A slice configuration is V = (V(x,i)), with x ∈ Λ and i = 1, 2, 3. So V ∈ 𝒞 := G^{3N³}.

**Action and flow.**
- S_sp(V) = Σ_{x, i<j} (1 − (1/n) Re tr U_ij(x)), with U_ij(x) = V(x,i)V(x+i,j)V(x+j,i)⁻¹V(x,j)⁻¹ and n the dimension of the representation.
- The Lie derivative ∂_{x,i}S ∈ 𝔤 is defined by ⟨X, ∂_{x,i}S(V)⟩ = d/dt S(V with V(x,i) ↦ e^{tX}V(x,i))|_{t=0}, for all X ∈ 𝔤.
- The flow is dV_s(x,i)/ds = −g₀² (∂_{x,i}S_sp(V_s)) V_s(x,i), with V₀ = V.

**(i) Existence and uniqueness for all s ≥ 0.**
1. 𝒞 is a compact smooth manifold without boundary. [It is a finite product of compact Lie groups.]
2. S_sp is smooth on 𝒞. [It is a polynomial in matrix entries.] So ∂_{x,i}S_sp is a smooth 𝔤-valued function. [It is a derivative of a smooth function along smooth left-translation curves.]
3. X(V)(x,i) := −g₀²(∂_{x,i}S_sp)V(x,i) is a smooth vector field on 𝒞. [Z·V with Z ∈ 𝔤 is a tangent vector at V, by right translation of 𝔤 = T_eG.]
4. A smooth vector field on a compact manifold is complete. Its flow Φ_s exists for all s ∈ ℝ, is unique, and is smooth in (s, V). [This is a standard ODE theorem: Picard–Lindelöf gives local existence and uniqueness, since smooth implies locally Lipschitz. Compactness prevents escape in finite time, by the escape lemma.] ∎

**(ii) Gauge covariance.**
- A gauge transformation of the slice is Λ: Λ → G, acting by V^Λ(x,i) = Λ(x)V(x,i)Λ(x+i)⁻¹.
- S_sp(V^Λ) = S_sp(V). [U_ij(x) ↦ Λ(x)U_ij(x)Λ(x)⁻¹, and the trace is conjugation-invariant.]
- ∂_{x,i}S_sp(V^Λ) = Ad_{Λ(x)} ∂_{x,i}S_sp(V). [e^{tX}V^Λ(x,i) = Λ(x)·e^{t Ad_{Λ(x)⁻¹}X}V(x,i)·Λ(x+i)⁻¹ = (V with V(x,i) ↦ e^{tAd⁻¹X}V(x,i))^Λ. So, by invariance of S_sp, ⟨X, ∂S(V^Λ)⟩ = ⟨Ad⁻¹X, ∂S(V)⟩ = ⟨X, Ad ∂S(V)⟩, using Ad-invariance of ⟨·,·⟩.]
- Put W_s := (Φ_s V)^Λ, with Λ independent of s. Then:
  dW_s(x,i)/ds = Λ(x)(−g₀²∂S(V_s)V_s(x,i))Λ(x+i)⁻¹ = −g₀² Ad_{Λ(x)}∂S(V_s) · W_s(x,i) = −g₀² ∂S(W_s) W_s(x,i),
  and W₀ = V^Λ.
- By uniqueness in (i), Φ_s(V^Λ) = (Φ_s V)^Λ. ∎

  The proof needs an Ad-invariant inner product. Without one the gradient is not Ad-covariant.

**(iii) Monotonicity.**
- dS_sp(V_s)/ds = Σ_{x,i} ⟨∂_{x,i}S, −g₀²∂_{x,i}S⟩ = −g₀² Σ‖∂_{x,i}S‖² ≤ 0. [Chain rule along the curve V(x,i) ↦ e^{−g₀² ds ∂S}V(x,i).]
- Equality holds exactly at critical points of S_sp. ∎

**(iv) Locality to the slice.**
- The vector field X depends only on S_sp. S_sp depends only on the spatial links of that slice. So the ODE lives on 𝒞, the spatial links of one slice.
- Φ_s V is therefore a (smooth) function of the initial spatial links of that slice alone. Temporal links and other slices do not enter. [Definition, plus (i).] ∎

**Numerical check (B4, delegated; rerun).** SU(2), 4³, Haar-random links, seed 20261123. Convention: Z = P_ah(V·staple), dV/ds = −ZV, which gives dS/ds = −½Σ‖Z‖²_F.
- The sign and normalization were checked by finite difference: relative error 5.4·10⁻⁸.
- S decreases at every step: from 189.80 at s = 0 to 10.638 at s = 1, for Euler and RK3 with ε = 0.01 and 0.005.
- Gauge covariance holds to 2.9·10⁻¹⁵ (Euler) and 4.0·10⁻¹⁵ (RK3). This is roundoff, not O(ε), because every integrator step is itself covariant.
- Links stay in SU(2) to 1.1·10⁻¹⁴.
- The measured integrator orders are 1.008 (Euler) and 2.979 (RK3).
- Locality: the field array holds only the slice's three spatial directions.

## B2. Consequence for the transfer formalism

**ASSUMED standard facts.** For these I rely on attribution only: Osterwalder–Seiler, as credited by Jaffe–Witten and by Chatterjee's survey in LITERATURE.md. The paper itself was not opened.
- (T1) The Wilson action on a lattice that is periodic in time (or infinite in time) is reflection positive for reflections through a time slice. There is a bounded, positive, self-adjoint transfer matrix T on ℋ = L²(𝒞, Haar). T commutes with the gauge transformations of the slice.
- (T2) On the gauge-invariant subspace ℋ_phys, T has a nondegenerate top eigenvalue with eigenvector Ω. We write T = e^{−bH} on the closure of its range, with H ≥ E₀ = 0. (For a finite lattice, nondegeneracy is a Perron–Frobenius-type statement for a positivity-improving kernel. ASSUMED, not checked here.)
- (T3) For bounded functions F, F' of one slice's spatial links, the Euclidean correlator at time separation τ = nb in the limit of infinite time extent is ⟨Ω, F' Tⁿ F Ω⟩. This is the transfer-matrix representation, which uses the temporal gauge, or equivalently the gauge-projected T.

**Claim.** Let φ: 𝒞 → ℝ be bounded, measurable and gauge-invariant. For example, φ can be the clover or plaquette action density at x, smeared over x with f. Put F := φ∘Φ_s. Then:
1. F is bounded, with sup|F| ≤ sup|φ|. It is measurable [Φ_s is smooth, by (i)] and gauge-invariant: F(V^Λ) = φ((Φ_sV)^Λ) = φ(Φ_sV), by (ii).
2. By (iv), F is a function of the spatial links of one slice. So it acts on ℋ as a bounded multiplication operator. It commutes with the gauge action, so it maps ℋ_phys to itself. It is a time-zero observable in exactly the sense an unflowed slice observable is. [Nothing else is required of a time-zero observable in (T1) to (T3).]
3. Reflection positivity: ⟨Θ(F)F⟩ ≥ 0. [F is supported on the slice, which lies in the positive half-lattice for the site reflection. (T1).]
4. Spectral representation. Write F_c = F − ⟨Ω,FΩ⟩. Then
   C(τ) = ⟨F_cΩ, e^{−τH}F_cΩ⟩ = ∫ e^{−τE} dν(E), for τ ∈ bℕ.
   Here ν is the spectral measure of H in the vector F_cΩ, with ν(ℝ) = ‖F_cΩ‖² ≤ 4 sup|φ|². [(T2), (T3) and the spectral theorem.]

The statements S5 (a) to (g), and so the window, gap and no-gap lemmas of HeatRegularized.lean, therefore apply to C(τ). This uses the finite-sum versions when ℋ_phys is finite-dimensional, which it is not for compact G (L² of a compact group is infinite-dimensional), so the measure version is needed. That version is NOT formalized (STATEMENT review: "the measure version is not formalized").

**Which step fails for the four-dimensional flow.**
- (iv) fails. The four-dimensional flow equation contains plaquettes with temporal links, and it couples neighbouring slices. So the flowed links at time 0 are functions of links at **all** times, at positive flow time on a finite lattice. In general the dependence is nonzero, though suppressed at distance, and I have not quantified that suppression.
- Hence F is not a function of one slice. It is not a multiplication operator in the transfer-matrix Hilbert space at time 0. It is not supported in a half-lattice, so step 3 (reflection positivity) does not follow, and (T3) does not give step 4.
- At best one has approximate versions with heat-kernel tails, which LITERATURE.md calls "control of the tails". NOT PROVED here.
- Steps (i) to (iii) hold for the four-dimensional flow as well; only (iv) breaks.

**Scope.** Only magnetic (spatial-plaquette) quantities are flowed. An electric density involves temporal links or, in the Hamiltonian picture, the conjugate momenta. It is not a function of the slice's spatial links, and a "flowed electric density" is not defined by this construction. This matters for STATEMENT defect 4 (the B² vs E² mixing) and for B3.

## B3. What the spatial flow does not give (OPEN)

- The all-order finiteness theorem (Lüscher, arXiv:1006.4518; Lüscher–Weisz, arXiv:1101.0963, as read in LITERATURE.md) is proved for the **four-dimensional** flow, in dimensional regularization, through a local (4+1)-dimensional field theory and its BRST symmetry. The flow damps all four momentum components there.
- The spatial flow is not that flow. **The theorem is not known to apply to it as stated.** I know of no result proving or disproving finiteness for spatially flowed correlators, so: not known to me.

**What would have to be shown.** For correlators of spatially flowed fields at positive flow time, including equal-time products on one slice: finiteness to all orders, with no renormalization beyond the coupling (and, on an anisotropic setup, possibly the anisotropy parameter). That is, a (3+1)+1-dimensional analogue of the Lüscher–Weisz argument.

**Candidate obstructions (my own inference, not literature).**
1. **Anisotropic power counting.** The flow damps spatial loop momenta only. Subdiagrams with large temporal momentum p₀ and bounded spatial momentum are undamped. Finiteness then requires the p₀-integrals alone to converge at each flowed vertex. In the free theory they do: Part A proves the equal-time variance finite. At higher loops I have not checked this.
2. **Loss of four-dimensional rotation invariance.** The flow-time boundary and the flowed operators are only cubic-symmetric in space, with a distinguished time axis. The symmetry argument that limits counterterms in Lüscher–Weisz therefore admits more terms, for example separate renormalizations of electric and magnetic parts at the boundary. The flowed magnetic density could mix with unflowed electric densities through such terms. This is the same B²–E² mixing that the review of S6 (defect 4) found for the unflowed density.
3. **Gauge.** Lüscher's perturbative proof uses a gauge-damping term (α₀) in the flow. For the spatial flow the analogous construction (spatial gauge-damping, with A₀ unflowed) would have to be redone.

**Status: OPEN.** Note that the S6″ obligations for the spatially flowed density are not equivalent to the ones for the literature's flowed E(t).
