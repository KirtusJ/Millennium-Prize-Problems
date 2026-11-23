# Claim (A) for SU(2), d = 4, by a finite-size criterion: the chain, a3-Afs

**This is NOT a proof.** The chain has one CLAIMED step in Half 1 (S1) and two MISSING steps in Half 2 (S5, S6). One more step (S4) is CLAIMED and rests on perturbation theory and on a small-lattice Monte Carlo. Steps S2, S3 and S7 are PROVED, conditional on the inputs they name.

Setting: SU(2) Wilson action on Z⁴, S = β Σ_p (1 − ½ Re Tr U_p), β > 0 fixed. U(1) is used for comparison with weight exp(β cos θ_p).
Notation: E is the set of links, V_L ⊂ E is the set of links inside a box Λ_L of side L, ∂V_L is the set of links outside V_L that share a plaquette with V_L, μ_V^ω is the conditional (DLR) measure on SU(2)^V given ω ∈ SU(2)^{E∖V}, and ρ is the bi-invariant geodesic distance on SU(2) scaled to diameter 1.

## Half 1: the criterion

**S0. Setting and the infinite-volume state.** Tag: CITED, abstract level only.
- Infinite-volume Gibbs measures exist for every β because the spin space is compact.
- Limits of periodic-box measures are reflection positive (RP), and RP gives a positive self-adjoint transfer matrix. Sources: LIT_RIGOROUS R2 (Osterwalder–Seiler 1978, Lüscher 1977, both read at abstract level only) and INDEX_EXTRACT (a)1 (Wilson RP on a finite periodic box, Lean, every β).
- RP passes to weak limits, because it is a family of inequalities between expectations of local observables.
- Hypotheses checked: compact group yes, Wilson action yes. The reflection plane type was not read. I use whichever plane gives T ≥ 0 for one or two time steps, and S3 works with either.
- Order of limits: box → ∞ at fixed β.

**S1. Criterion: a Dobrushin–Shlosman condition for the link spin system.** Tag: CLAIMED.
- *Condition K(L, β, γ).* Define
  κ_{L,y} := sup over pairs (ω, ω′) that differ only at y of W₁(μ_{V_L}^ω, μ_{V_L}^{ω′}).
  Here W₁ is the Wasserstein distance on SU(2)^{V_L} for the cost d(U, U′) = Σ_{x ∈ V_L} ρ(U_x, U′_x). The condition is
  Σ_{y ∈ ∂V_L} κ_{L,y} ≤ γ · |V_L|  for some γ < 1.
- *Claimed theorem.* If K(L, β, γ) holds, then:
  1. the Gibbs measure is unique;
  2. for all bounded f, g that are Lipschitz in ρ, with supports A and B,
     |Cov(f, g)| ≤ C (|A| + |B|) ‖f‖_Lip ‖g‖_Lip · exp(−c(γ) dist(A, B)/L), with c(γ) = −ln γ / 2.
- *Argument as I would defend it.*
  1. This is the DS (1985) "constructive uniqueness criterion" applied to the spin system whose spins are the link variables (compact metric space SU(2)) and whose interaction is the plaquette term (finite range: two links interact only through a common plaquette).
  2. Gauge invariance plays no role in the theorem. It is a statement about the specification {μ_V^ω}, and that specification is well defined without gauge fixing.
  3. The proof is a block path coupling. Couple two copies that disagree on a set D, refresh a random translate of V_L under the optimal W₁ coupling, and sum over the boundary links in D. The expected disagreement weight then contracts by the factor γ per sweep of translates.
  4. Disagreement spreads by at most one box diameter per sweep. Hence the influence at distance r is bounded by γ^{r/(2L)}.
  5. "Boundary conditions" for a gauge theory are therefore simply the link variables outside V_L. No gauge-invariant boundary datum is needed, because the sup over ω in κ already runs over every configuration, gauge-equivalent or not.
- *Weakest point.* I did not read the DS theorem (LIT_RIGOROUS R5d is NOT CHECKED, and the two sources there conflict on whether it has been carried out for lattice gauge theory). The exact form of their condition (W₁ or total variation, weights α_y) and their hypotheses on the spin space are taken from memory.

**S2. Uniqueness gives an RP, translation-invariant state.** Tag: PROVED, given S0 and S1.
- By S1 the Gibbs measure is unique.
- Every subsequential limit of periodic-box measures is a Gibbs measure, so it is that unique measure.
- By S0 it is RP. It is translation invariant because it is unique.
- The OS reconstruction then gives 𝓗, Ω and T = e^{−H} with 0 ≤ T ≤ 1. If RP holds only for site planes, use T² instead.

**S3. Uniform-rate Euclidean decay gives a transfer-matrix gap.** Tag: PROVED.
- *Statement.* Suppose that for a set 𝒟 of local bounded observables F, supported at times ≥ 0, whose vectors (F − ⟨F⟩)Ω are dense in Ω^⊥, we have
  0 ≤ C_F(n) := ⟨(F − ⟨F⟩)Ω, Tⁿ (F − ⟨F⟩)Ω⟩ ≤ K_F e^{−mn}  for all n ≥ 0,
  with m independent of F. Then spec(H restricted to Ω^⊥) ⊂ [m, ∞).
- *Proof.*
  1. Let ν_F be the spectral measure of ψ_F = (F − ⟨F⟩)Ω for H. Then C_F(n) = ∫ e^{−nε} dν_F(ε).
  2. For m′ < m: e^{−nm′} ν_F([0, m′)) ≤ C_F(n) ≤ K_F e^{−mn}.
  3. So ν_F([0, m′)) ≤ K_F e^{−n(m−m′)} → 0, hence ‖P_{[0,m′)} ψ_F‖² = 0.
  4. P_{[0,m′)} is bounded and vanishes on a dense subset of Ω^⊥, so it vanishes on Ω^⊥. Since m′ < m was arbitrary, the claim follows.
  5. C_F(n) is the connected correlation ⟨θF · τ_n F⟩ − |⟨F⟩|², which S1 bounds with dist = n − (time extent of F). The thickness goes into K_F.
  6. The set 𝒟 can be taken to be Lipschitz functions, which are uniformly dense in the continuous functions. The vectors from continuous local F are dense by the OS construction.
- *Output.* m(β) ≥ c(γ)/L > 0.
- No Lean was used. The step is measure theory, not algebra.

## Half 2: the criterion holds at some scale for every β

**S4. A finite-volume running coupling.** Tag: definition, plus a CLAIMED monotonicity.
- *Definition.* z(L, β) := L · E_f(L, β), where E_f is the lowest energy of the transfer matrix of the periodic L³ box (T → ∞ first) in the sector of one unit of 't Hooft electric flux in direction x.
- *Measurement.* E_f is measured from the correlator of the zero-momentum spatial Polyakov loop p(t) = L⁻² Σ_{y,z} ½ Tr Π_x U_x(x, y, z, t). The Polyakov loop is odd under the center transformation, so this correlator lives in the flux sector. In every finite box, E_f is finite and positive.
- *Free-photon value.* For the U(1) free photon, z = g²/2 = 1/(2β) at every L. The energy is that of the zero mode: H = g² p_Φ²/(2L), and e^{iΦ} raises p_Φ by one unit. See the MC check P_D in report.md.
- *CLAIMED for SU(2):* z(·, β) is increasing in L.
- *Argument.*
  1. At small L the box is weakly coupled.
  2. z(L) is a renormalized coupling at scale L, and its scale derivative is −b₀ z² + O(z³) in some scheme, with b₀ = 11·2/(48π²) > 0 for SU(2). The sign of b₀ comes from the non-abelian self-coupling.
  3. For U(1) without matter the β-function vanishes at this order and nonperturbatively (free photon), so z is constant.
- *Weakest point.* This is perturbation theory (hole (v)). For SU(2) on a torus the small-volume flux energy is also known to be dominated by tunnelling and not by the perturbative zero mode (van Baal, from memory). So "z ∝ g²(L)" is itself not the right small-L form.
- *Evidence (measured only, report.md).* On 4D lattices L = 2, 4, 6 at β = 2.3, z_SU2 rises with L, while z_U1 stays near 1/(2β). Six lattice sizes at one β say nothing about β → ∞.

**S5. Unboundedness: for every β there is L(β) with z(L(β), β) ≥ z*.** Tag: MISSING.
- *Testable form.* For every β > 0, sup_L z(L, β) = +∞.
- *Why it is open.*
  - The statement would follow from a positive string tension σ(β) > 0, since then E_f ~ σL and z ~ σL².
  - σ(β) > 0 at every β is Chatterjee's open Problem 4.1 (LIT_RIGOROUS R5f).
  - Tomboulis's all-β claim is disputed (LIT_ATTEMPTS T1).
  - I have no argument that avoids confinement.
- *Order of limits.* T → ∞ at fixed L, then L → ∞ at fixed β. Nothing here needs uniformity in β.

**S6. The bridge: z large at scale L implies K at scale kL.** Tag: MISSING.
- *Testable form.* There exist z* < ∞, k ∈ ℕ and γ < 1 such that, for every β and L, z(L, β) ≥ z* implies K(kL, β, γ).
- *What it would have to overcome.*
  1. z is a periodic-box, one-sector quantity. K is uniform over all exterior configurations ω, including ones that are not typical, for example ones carrying flux into the box. This step is where uniformity in the volume (all boundary conditions, all embeddings) is used.
  2. The zero-flux sector, which contains the glueballs, is not controlled by E_f at all. A large flux energy says nothing directly about the influence of a boundary link on the interior.
  3. Finite gauge groups at weak coupling satisfy (A), and plausibly K at L = 1, while their flux energy tends to 0 (deconfined phase). So z ≥ z* is not necessary for K. I have no proof that it is sufficient.
  4. The brief's simpler criterion "L·m_L bounded below in the periodic box implies inf_L m_L > 0" is not available. INDEX (c)8, Z5 `volume-uniformity`, kills "gap in every box implies an infinite-volume gap", and I have no threshold version.

**S7. Conclusion (A).** Tag: PROVED from S1–S6. It is no stronger than its weakest input (S5, S6, MISSING).
- S5 gives L(β) with z ≥ z*.
- S6 then gives K(kL(β), β, γ).
- S1 and S2 then give a unique RP state with decay rate c(γ)/(kL(β)).
- S3 then gives m(β) ≥ c(γ)/(k L(β)) > 0.
- The order of limits throughout: β fixed, the box goes to ∞ (S0–S3), and L(β) is finite for each β. Nothing is claimed uniform in β, and (A) does not need it.

## Discriminator table

| Model | Truth of (A) | S1–S3 (criterion) | S4 (z increasing) | S5 (z unbounded) | S6 (bridge) | First step that fails |
|---|---|---|---|---|---|---|
| U(1), d = 4, weak coupling (β > β_c ≈ 1) | false | general theorems: they hold, but K is never satisfied | fails: z constant ≈ 1/(2β) (free zero mode; MC P_B) | fails | vacuous | **S4/S5.** The abelian group has no self-interaction: the flux zero mode is free and z does not run. So K(L) never holds, which is consistent with S1 ⇒ gap. The difference from SU(2) is only the claimed sign of b₀ (perturbative, hole (v)) and unproved σ > 0. |
| Finite group, d = 4, weak coupling | true | K plausibly holds already at L ≈ 1 (Adhikari–Cao decay, LIT R3c, is close but is not the all-b.c. W₁ condition) | false: in the deconfined phase z → 0 | fails | not needed | S4/S5. The mechanism does not reach (A) here, although (A) is true. The route is incomplete, not wrong. |
| U(1), d = 3 | true (Göpfert–Mack, Villain) | general | holds: z ≈ g²L/2 grows by dimension, then σL² | true if σ > 0 (Göpfert–Mack: α > 0 for all g²) | MISSING | S6 (bridge). The argument does not reach (A) without it, but nothing false is derived. |
| SU(2) or U(1), d = 2 | true | K expected: the interior depends on the boundary only through the holonomy, heat kernel at area L² | holds exactly: z = −L² ln a(β) (child, verified) | holds exactly | MISSING, though d = 2 should be checkable | S6. Not a counterexample. |
| SU(2), d = 4 | target | general | CLAIMED (pert. + MC, 3 sizes) | MISSING (≡ confinement-type statement) | MISSING | S5 |

**Where non-abelian structure enters (one line):** only in S4, through the sign of b₀ (the gluon self-coupling makes the flux coupling z grow with L), and that step is perturbative (CLAIMED). S1–S3 and S6 make no distinction between U(1) and SU(2).

## Weakest link

S6, the bridge from a periodic-box, flux-sector, single-number coupling to a Dobrushin–Shlosman condition that holds uniformly over all exterior link configurations. It is MISSING, and I do not know a single inequality connecting the two quantities, even at strong coupling. S5 is the confinement problem in another form.

## What a challenger should attack first

1. **S6.** Find a model with z(L) → ∞ in which K(L′) fails for every L′. Candidates: a Higgs-like or mixed theory with a large flux energy but massless modes in the zero-flux sector. Or show that K fails for SU(2) at small L for an atypical ω, for any choice of k.
2. **S1.** Check the DS 1985 theorem's exact hypotheses, and whether W₁ with sum-cost and the c(γ)/L rate are what it gives. Check also whether the sup over all ω (including enormous-action boundaries) makes K impossible at weak coupling for every L. A single boundary link change gives O(1) displacement on the adjacent interior links, and the Gaussian estimate makes Σ_y κ_y of order |V_L|, that is marginal.
3. **S4.** The MC monotonicity is three sizes at one β. Small-volume SU(2) flux energies are tunnelling-dominated, so what is visible may be the onset of confinement at β = 2.3, not asymptotic freedom.

## TEST (iii) of the first CLAIMED step of Half 2 (S4, monotonicity of z), measured only

zflux.py, result_zflux_1.txt. 4D lattices L³×12, β = 2.3, z = L·m_eff(t=1):

| L | z SU(2) | z U(1) | U(1) rotor model at T=12 (expected, post hoc) |
|---|---|---|---|
| 2 | 0.562 ± 0.016 | 0.335 ± 0.024 | 0.324 |
| 4 | 2.12 ± 0.06 | 0.553 ± 0.078 | 0.422 |
| 6 | 8.02 ± 0.40 | 0.684 ± 0.068 | 0.500 |

- **SU(2).** z rises steeply with L, roughly like L². At β = 2.3 that looks like the onset of the area law: the string tension in lattice units is O(0.1).
- **U(1).**
  - The true zero-T value is z = 1/(2β) = 0.217 at every L. The measured z drifts upward only because at T = 12 several flux levels of the free zero mode are thermally populated. The post-hoc rotor model reproduces this drift (last column).
  - So P_D failed. That failure is my own expectation, which ignored the finite T. It is not a defect of the target.
- **Verdict on S4.** The test does **not refute** S4. It is also very weak evidence for it.
  - It is one β, three sizes, and an effective mass at t = 1 contaminated by excited states (m_eff(2) < m_eff(1) for SU(2)).
  - It shows confinement-scale physics at β = 2.3. It does not show running from weak coupling, which would need L ~ exp(β·const).
- **2D check (the child's, rerun by me).** z = −L² ln a(β) holds exactly for both groups. The 2D U(1) Monte Carlo agrees within 3σ at L = 2 and 3. So 2D does not discriminate between the groups. That is correct, because (A) holds for both in 2D.
