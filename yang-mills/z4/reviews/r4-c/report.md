# Report r4-c: disposition of two Yang–Mills lanes (central-quotients, spectral-support)

Worker r4-c for Director Z4. Principal: Kirtus Justus. Date: 2026-11-22.

This is an extraction. I checked no proofs. I share a model family with the director and with the lane authors, so my reading is not independent review.

## 1. Verdict table

| # | Item | Verdict | Evidence (one line) |
|---|---|---|---|
| 1 | Control: −ln(tanh 1) = 0.272341 | STANDS | control.txt. The child's control.txt gives the same value. |
| 2 | input/ holds 29 .md files: 17 central-quotients (CQ), 11 spectral-support (SS), 1 problem README | STANDS | count_md2.py, register check K2 exit 0. My first expectation (28) was wrong: K1 failed (see §3). |
| 3 | CQ: 14 rows state a result and all 17 files were read in full by me; nothing marked NOT READ | STANDS | notes.md steps 5–11 |
| 4 | CQ: every result is at fixed spatial mesh. Regimes are FIXED, ONE-LIMIT (volume), JOINT (time step and volume, wilson-time.md), CONDITIONAL (on B4's external gap) or CONTROL. None is CONTINUUM-4D. | STANDS | Rows 1–14 below. momentum/execution.md: "The positive-energy band is a research result at fixed spatial cutoff. The continuum construction is open." |
| 5 | CQ: no Jaffe–Witten requirement is CLAIMED for the 4D continuum theory | STANDS | CQ/README intro: "The continuum construction, physical mass scale, and gap remain open." |
| 6 | SS: 8 rows state a result. The child read 12/12 in full. I read 7 SS files in full and grepped 3 execution files. | STANDS (child claim plus my partial reread) | child/report.md; notes.md steps 14–17 |
| 7 | SS: the central results are CONDITIONAL criteria (rate ⇒ gap). The unconditional positives (adjoint band) are at fixed spatial mesh. Nothing is CLAIMED. | STANDS | SS/README: "Constructing the four-dimensional Yang–Mills theory and deriving that rate for it remain open." Also l.50: "No rate for interacting four-dimensional Yang–Mills has been derived in this work." |
| 8 | Child rows checked against files: 5 checked, 4 matched, 1 partial | DEFECT (child row 6, regime class) | adjoint-band/README's headline is a bound uniform in box size at fixed mesh, which is FIXED. Weak-volume limits are a sub-claim. The child gave ONE-LIMIT. |
| 9 | Child's own report.md | DEFECT (process, not target) | The harness refused the sub-agent's file write. I saved its returned text to child/report.md and marked it as written by the parent. |
| 10 | Cross-lane contradiction | STANDS: none found. There are 5 tensions or unconverted conventions, listed in §6. | §6 |
| 11 | Correctness of any proof, Lean file, or numerical script in the lanes | NOT CHECKED | The .lean, .py and evidence files are not in input/. |

Counts for predicates of programs and checks (met, failed, measured only): **met 6** (control; count_md2 P1, P2; child control; child count; child count rerun by me), **failed 2** (count_md P1, P2: my own expectation error), **measured only 5** (the five child-row comparisons: 4 matched, 1 partial).

Verdict counts in the table above: STANDS 8, DEFECT 2, NOT CHECKED 1.

Both PCP registers end with: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)` (pcp and child/pcp).

## 2. Hypotheses each statement uses, and where they are stated

Each row's "main statement" column (§4 and §5) states its hypotheses. In summary:

- **Fixed regulator.** All CQ rows and SS rows 4, 6, 8 assume a finite spatial lattice or graph: periodic or open, side ≥ 3 (L=2 excluded, momentum/local-estimates.md last §). They assume positive electric coefficients κ>0, λ≥0, Gauss law and product Haar measure.
- **Potential.** finite-graph.md assumes a smooth V and cycle rank ≥ 2. analytic-groups.md assumes a real-analytic V.
- **External inputs not proved in the lane.** CQ adjoint-weight.md §2, momentum/README §Bounds and wilson-time.md use B4's volume-independent gap in the small z=κ_Bλ regime (Yarotsky Thm 1) and B4's time-step comparison bounds. They also use A4's local energy estimate K_e ≤ B. SS adjoint-band uses A4's M_{2,F} ≤ 86401κ² and K_e bound. SS wilson-limit and positive-time §strong-coupling use B4's fixed-box convergence and B4's 0 ≤ S_k ≤ 1/3 for tanh β ≤ 1/20.
- **Abstract reconstruction.** SS README, diagonal, positive-time and vacuum assume a reconstructed nonnegative self-adjoint H, an identified vacuum, a common physical clock, convergence of cutoff correlations or measures, and a common rate on a **dense** family (SS/README §Which estimate; diagonal §Application; vacuum ¶3: "Vacuum uniqueness, a nonzero excitation, reconstruction … are separate inputs").
- **CQ transfer.md §1** assumes that both cover and quotient reconstruct a self-adjoint transfer semigroup and that a cover gap exists.

## 3. Failed predicates

1. count_md.py P1 (total = 28) and P2 (SS = 10) FAILED in register check K1. The count was 29 and 11. This was **my own expectation error**: I miscounted the initial listing. It is not a defect of the target. I corrected the predicates in a new program, count_md2.py, which passed (K2). The result file counts_0.txt is kept and was not overwritten.
2. Child row 6 (SS/adjoint-band/README.md), regime class, is a partial mismatch. It is a judgment difference, not a target defect (see §1 item 8).

Tolerances: all predicates are exact integer equalities, so none was needed. No randomness is used, so no seeds.

## 4–5. Per-note extraction and requirement tables
## Lane 1: central-quotients (Director C4). I extracted this lane myself. All 17 files read in full.

Files: 17 .md. 11 state a result (rows below). 3 are execution logs used only for the evidence column: execution.md, local-response/execution.md, momentum/execution.md. The 3 README files are also rows, because each states its own result.

Lean counts as the lane reports them. CQ/execution.md: 9 declarations, Lean core only; covers the finite identities, the Klein-four classification and the cube counts. Haar pushforward, surface expansion and the covering interpretation are "mathematical arguments above". local-response/execution.md: 17 declarations, Mathlib; "All three proof mutations failed and a guest rejected a three-face request"; the commutant, analytic continuation, OS, spectral and density arguments are "mathematical proofs in the notes". momentum/execution.md: 17 declarations; "The three altered Lean conclusions failed"; the heat-kernel comparison, cross-term cancellations, locality, Fourier and thermodynamic identifications are in "the mathematical notes"; "The positive-energy band is a research result at fixed spatial cutoff."

| # | File | Main statement and hypotheses | Regime | Group / dim | Units, and mesh → 0 | Evidence (as reported) | Open, per the note |
|---|---|---|---|---|---|---|---|
| 1 | CQ/README.md | (i) On a finite plaquette complex, the pushforward of the fundamental SU(2) Wilson weight to SO(3) has the exact density ∏cosh·Σ over closed 2-chains ∏tanh. On one cube at β=log 2 and the identity configuration this is 8177/2048, against 15625/4096 for independent face averaging. (ii) The E2 one-link quotient gap satisfies −γ log λ > 4γ/(4+γ) for every γ>0. (iii) There is a flat SO(3) representation of Z^4 with no flat SU(2) lift; table of counts 46/210/256. | FIXED. (ii) is a one-link model, CONTROL in character | SU(2)→SO(3); finite complex / one link / 4-torus holonomy | Lattice / dimensionless. Mesh → 0 not stated. It says "Physical time and a uniform four-dimensional gap remain open" (§positive gap). | Text proof. 9 Lean declarations for the finite identities only (§Formal coverage: "does not formalize measure theory"). One-link bound checked numerically at six couplings (execution.md). 1 mutation rejected (46→47). | "The continuum construction, physical mass scale, and gap remain open" (intro). Volume- and spacing-uniform control of connected correlators (§Which density). The holonomy result gives "no topological obstruction … on R^4". |
| 2 | CQ/cube-strip.md | On an open n×1×1 strip at fixed β>0, R_n ≥ (1+h^6)^n with h=tanh β. Hence no normalization c_n makes independent face-sign averaging uniformly accurate in relative pointwise density error. | FIXED (each n). The statement is uniform in n. | SU(2)→SO(3); 3D strip | Lattice. Mesh → 0 not stated. | Text proof (analytic). Exact rational enumeration for n=1,2,3 (check_strip.py). The note says the Lean declarations cover only the single cube. | "leaves open whether normalized expectations of specified local observables converge … on a four-dimensional trajectory" (§normalization). |
| 3 | CQ/local-response/README.md | Conditional on the quotient links, on the open d×1×1 strip at any β≥0: transverse sign covariance ≤ tanh^{4d}β, uniformly in length and SO(3) configuration. The rate is sharp for the connected covariance of nonzero fundamental traces. | FIXED (uniform in strip length) | SU(2)→SO(3); 3D strip | Lattice units. "Its rate in lattice units obeys −log q∼8e^{−2β} as β→∞" (§Checks and physical scope). | Text proof. Exact arithmetic at β=log 4, d=2,3 (check.py). Lean parts are in local-response/execution.md (17 declarations). | The unconditional part Cov(E[T_i\|Ū],E[T_j\|Ū]) "this bound leaves open". A 4D gap "requires physical time, a nontrivial continuum theory and uniform estimates" (§Checks). |
| 4 | CQ/local-response/finite-graph.md | Assumptions: finite SU(2) graph with cycle rank ≥2, κ_ℓ>0, Gauss law, real smooth gauge-invariant V. Claim: the closed span of positive-time SO(3)-link histories is exactly H^{D_V}. With Wilson V on an open cubic box this is the whole physical space. On a periodic 3-torus it is the winding-neutral sector, dim D_V=3. | FIXED (continuous time, finite spatial graph) | SU(2), spatial 3D graph (Hamiltonian) | Lattice. "does not furnish a lower bound on the energies or a cutoff-uniform family"; density "may become ill-conditioned as the regulator changes" (§Implication). | Text proof (commutant argument). Exact binary elimination (check_graph.py). Lean covers component identities and the 512-subset enumeration. The analytic steps are not in Lean (local-response/execution.md). | "A continuum construction still needs common physical time, surviving observable norms and uniform spectral estimates" (§Implication). |
| 5 | CQ/local-response/analytic-groups.md | Same conclusion as row 4 for every compact connected Lie G and finite central Z ⊂ Z(G), any cycle rank, real-analytic V. It also holds for observations on a fixed time mesh sℕ. For SU(N) Wilson faces, D_V=H^1(Y;Z). | FIXED | All compact connected G; spatial graph | Lattice. It "supplies no spatial continuum limit" (last §). | Text proof. Cites Palais and Morrey–Nirenberg. No Lean claimed for the analytic steps. | "The four-dimensional existence and positive mass-gap obligations remain open" (last §). |
| 6 | CQ/local-response/rotor.md | One continuous-time SU(2) plaquette with class-function sector and λ≠0: histories of \|½Tr U\| generate the whole class space. At λ=0 they generate only the even space, with history gap 8κ against cover gap 3κ. The weight of the first mode in U_2 is 4λ/(15κ)+O(λ²). | CONTROL (single plaquette) | SU(2), 0+1 dim | κ units. Mesh not applicable. | Text proof (Wronskian). Numerical character cutoffs 18 and 32. Lean has the differentiated Wronskian "under the specified derivative and ODE hypotheses". | The extension to a spatial lattice and uniform bounds are needed "for a continuum conclusion" (last §). |
| 7 | CQ/local-response/transfer.md | (i) If q intertwines reflection and translation, the OS pullback is an isometry. A cover gap bound on the vacuum complement passes to the quotient with the same time normalization. (ii) The single-slice projection defect satisfies lim s^{-2}D_s(f)=∫\|f\|²Σλ_p²t_p². This is Σλ_p²/4 for f=1, and Σλ_p²/18 for SU(3) with Z_3. | (i) CONDITIONAL: it assumes both systems reconstruct a selfadjoint transfer and that a cover gap exists. (ii) FIXED. | SU(2); also general compact group with finite central Z; finite Hamiltonian | Lattice. Mesh → 0 not stated. Identifying it with a 4D isotropic Wilson transfer "would require a separate argument". | Text proof. Finite character checks (check.py). Lean transfer identities (execution.md). | A nonzero test in the quotient vacuum complement "is a separate requirement" (§1). The Wilson-transfer identification (last §). |
| 8 | CQ/local-response/adjoint-weight.md | A4's SU(2) Hamiltonian on a periodic box of side ≥3: Var(A) ≥ v_* and C_A(t) ≥ v_* e^{−tM_A/v_*}, uniformly in box size. If B4's small-z volume-independent gap Δ holds, then μ_A([Δ,R]) ≥ v_*/2. | First part FIXED (spatial mesh fixed, uniform in volume). Band part CONDITIONAL on B4's perturbative gap (an external lane). | SU(2), spatial 3D lattice Hamiltonian | κ units. "Along a spatial continuum trajectory the constants can deteriorate, and a lower bound on an autocorrelation gives no lower mass-gap bound" (§1 end). | Text proof extending A4. The note points to the execution record for Lean. | "A bulk gap on a spatial refinement trajectory and the same positive band there remain open" (last §). |
| 9 | CQ/momentum/README.md | Compact connected simple G, periodic L≥3, fixed spatial mesh, continuous time. Centered center-neutral plaquette Fourier modes satisfy aI ⪯ ∫E dμ_k ⪯ bI and ∫E³dμ_k ⪯ cI, with constants independent of L. Then μ_k([ℓ,R]) ⪰ (a/2R)I on ≥(1−δ)N momenta. If a volume-independent gap Δ exists, [Δ,R] works at every momentum. | FIXED (uniform in L). The every-momentum band is CONDITIONAL on B4's gap ("B4's fixed-mesh small-interaction regime"). | Each compact connected simple G (no uniformity over groups claimed); spatial 3D Hamiltonian | Lattice units. "A bounded physical momentum region occupies a shrinking part of the dimensionless Brillouin zone … requires control … of a,c,ℓ,R in the physical units" (§Controls and continuum). | Text proof. 17 Lean declarations for the arithmetic and counting pieces. The heat-kernel and locality analysis is in the notes. 3 altered conclusions failed. Numerical controls (controls.py). | "Four-dimensional continuum existence and the Millennium mass gap remain open" (§Controls). "no claimed uniformity over all groups or over magnetic-to-electric coupling ratios" (§Bounds). |
| 10 | CQ/momentum/infinite-volume.md | Fixed mesh, L→∞. Subsequential joint momentum–energy limits exist. Their positive-energy momentum marginal is absolutely continuous. The density floor is 3a/(4R) on (0,R]. The [ℓ,R] window holds on ≥1−δ of the torus. | ONE-LIMIT (spatial volume, subsequential; mesh fixed, continuous time) | Same as row 9 | Lattice. A "lack of continuum rotational covariance" is compatible with these estimates (last §). | Text proof only. The thermodynamic identification is in the notes (momentum/execution.md). | Several subsequential limits are possible. "Reconstruction of a continuum gauge field still requires a common limit for its full positive-time test algebra" (last §). |
| 11 | CQ/momentum/local-estimates.md | Assumption L≥3. Conditional ground-state density ratio in [r^{−2}, r^2] with r=e^{τd}(h_+/h_−)^m. First-moment bounds a=4κr^{−2}J_f, b=16κ‖∇f‖². | FIXED (uniform in L) | Compact connected simple G | Lattice (κ). Mesh → 0 not stated. | Text proof. Side-two failure control (geometry.py). | L=2: "The independence step has no such justification in that geometry." |
| 12 | CQ/momentum/third-moment.md | The third-moment matrix has range ≤2 neighbour steps (≤63 entries per row). M_{3,pp} ≤ d_3, so M_3 ⪯ 63 d_3 I, independent of volume. | FIXED | Compact connected simple G | Lattice. Mesh → 0 not stated. | Text proof. Lean and worker counts 51/61/63. Numerical finite-difference control −64/9. | The note says that finding a particular vacuum matrix entry "would additionally require taking its expectation" (last §). |
| 13 | CQ/momentum/adjoint-refinement.md | SU(2) adjoint smearings: M_1(c) ≥ a_A n with a_A=9κ/[16(1+√B)²], and M_2 ≤ D_2κ²n. The band [δκ/12288, R] holds on ≥(1−δ)N momenta, uniformly in magnetic coupling. | FIXED (spatial mesh fixed, uniform in L and in g) | SU(2), spatial 3D Hamiltonian | κ (lattice) units. "Along B4's bare tree-level matching … If β→∞ and βb→0, this band moves to ultraviolet physical energies" (last §). | Text proof. The Lean "polynomial differential floor" and "quadratic window majorant" pieces are listed in momentum/execution.md. | Escape of the band to UV physical energies. "exempt a shrinking physical momentum patch" (last §). |
| 14 | CQ/momentum/wilson-time.md | SU(2), spatial mesh fixed, temporal spacing a_n→0 jointly with L_n→∞ on B4's explicit schedule a_n. The averaged trace-norm error between the Wilson and Hamiltonian momentum measures → 0, so the band transfers to (1−δ−o(1))N momenta. A stronger schedule a_n/(1+N)^3 preserves every good momentum. | JOINT (time step and spatial volume on schedule a_n; spatial mesh fixed). It rests on B4's comparison bounds (external), which this lane did not re-prove but replayed in Lean (momentum/execution.md). | SU(2), anisotropic 4D Wilson lattice (spatial mesh fixed) | Lattice. "Both paths leave the spatial lattice spacing fixed … Removing the spatial cutoff … remain separate obligations" (last §). | Text proof. Lean pieces are rank-one vacuum distance and Gram sum. The numerical control check_wilson.py gave mean 0.02698 < bound 0.36299. | Removing the spatial cutoff, a Euclidean-invariant field limit, and excluding small positive physical energies (last §). |

### Lane 1 against the problem requirements

| Req | Disposition | Basis |
|---|---|---|
| (a) continuum limit on R^4 | PARTIAL: only time step and spatial volume are removed (wilson-time.md, JOINT; infinite-volume.md, ONE-LIMIT). The spatial mesh is never removed. | wilson-time.md last §: "Both paths leave the spatial lattice spacing fixed". CQ/README intro: "The continuum construction, physical mass scale, and gap remain open." |
| (b) RP / OS axioms | PARTIAL | transfer.md §1: the OS pullback isometry from cover to quotient, assuming reconstruction on both sides. finite-graph.md: "M is the OS image of the exact history pushforward in this Hamiltonian model" at fixed regulator. No continuum OS axioms. |
| (c) Euclidean invariance | NOT ADDRESSED (negative remarks only) | momentum/README controls: the flat dispersion "illustrates how little a finite-cutoff positive band says about rotational invariance". infinite-volume.md: "lack of continuum rotational covariance … compatible". |
| (d) nontriviality | NOT ADDRESSED | Nothing asserted beyond interacting regulators at fixed cutoff. |
| (e) mass gap > 0, physical units | ADDRESSED AT FIXED REGULATOR, and partly CONDITIONAL | The lane proves positive-energy bands in lattice units at fixed spatial mesh. The every-momentum version uses B4's external perturbative gap. adjoint-refinement.md: the band "moves to ultraviolet physical energies". momentum/README: "the Millennium mass gap remain[s] open". |
| (f) all compact simple groups | PARTIAL | analytic-groups.md (all compact connected G) and momentum/README (each compact connected simple G) hold at fixed regulator, with "no claimed uniformity over all groups". Most quantitative results are SU(2) only. |

CLAIMED: none. No note asserts any requirement for the 4D continuum theory.

## Lane 2: spectral-support (Director D4). Delegated to the child; rows from child/report.md.

There are 11 .md files. 8 state a result and 3 are execution logs (execution.md, adjoint-band/execution.md, positive-time/execution.md). The child reports reading all 12 in full (the 11 plus the problem README). Below is the child's table, with my corrections marked **[r4-c]**.

| # | File | Main statement (hypotheses) | Regime | Group / dim | Units, and mesh → 0 | Evidence (as reported) | Open, per the note |
|---|---|---|---|---|---|---|---|
| 1 | SS/README.md | A common rate r on a dense family of centered vectors, at late physical times (cutoff limit first), implies μ_v((r,∞))=0. Hence no energy below −log(r)/τ in the vacuum complement. Also: E1's six readings admit a gapless measure. | CONDITIONAL (the common rate; "No rate … has been derived", §still needs) | abstract; SU(2) not specified | Physical clock τ assumed. Mesh not stated. | 6 Lean declarations (5 analytic + 1 finite certificate). The continuous map, scalar measures and spectral identity are Lean inputs. Exact rational checker. 3 mutations rejected (execution.md adverse table; **verified by r4-c**). | The rate for interacting 4D YM; convergence at rounded times "still needs proof along the chosen trajectory". |
| 2 | SS/diagonal/README.md | If the cutoff measures ν_k converge weakly to μ and ∫x^{t_k}dν_k ≤ M r^{t_k}, then μ((r,∞))=0. | CONDITIONAL (weak convergence, common clock, dense diagonal estimate, reconstruction) | abstract | Not stated | 5 Lean declarations (Lean 4.24.0). 3 mutations failed as expected. **Verified by r4-c.** | "still needs a nontrivial interacting reconstruction, a common physical clock, and a positive diagonal estimate … for each required compact simple gauge group". |
| 3 | SS/positive-time/README.md | A single late envelope C_k(T_k) ≤ Me^{−mT_k} plus convergence at u<t implies e^{mt}C(t) ≤ e^{mu}C(u). Sub-claim: on B4's strong-coupling 4D SU(2) Wilson trajectory (tanh β_s, tanh β_t ≤ 1/20), every connected autocorrelation limit vanishes. | CONDITIONAL; the sub-claim is ONE-LIMIT (time step) and rests on B4 | abstract; sub-claim SU(2), 4D lattice | Lattice steps vs physical time are stated. Mesh → 0 is the time step only. | 15 Lean declarations (shared with row 4). The Wilson-to-transfer step is analytic. 5 negative controls rejected (**count verified by r4-c** in positive-time/execution.md). | The weak-coupling late envelope; nontrivial 4D YM for all groups. |
| 4 | SS/positive-time/thin-loops.md | Conditioning on two nonadjacent slices bounds the covariance of two thin loops by perimeter suppressions. | FIXED | SU(2), 4D lattice | Lattice. Moving energy threshold (per child). | Text proof. Lean covers the last Hilbert step and the Markov bound. Enumeration on 3^4–5^4. 1 mutation rejected. | **NOT READ by r4-c**; child's row only. |
| 5 | SS/positive-time/vacuum/README.md | If D_sC(T_k) ≤ Me^{−mT_k}, then μ((0,m))=0. This is a gap above the whole kernel. | CONDITIONAL (envelope, reconstruction, vacuum uniqueness are "separate inputs") | abstract | Physical s fixed. Mesh not stated. | 5 Lean declarations (Lean 4.24.0). "Four false mutations exercised"; rejection not stated. **Verified by r4-c.** | No uniform lower bound on the weight fraction as E↓0. |
| 6 | SS/adjoint-band/README.md | SU(2) Hamiltonian H=−(κ/4)Δ+λΣ(1−x_q), periodic side ≥3, every finite λ. The band ν_{F_A}([L,U]) ≥ w with L ≥ κ/576, uniform in box. | **[r4-c] FIXED (uniform in volume)**, with a weak volume-limit sub-claim. The child had ONE-LIMIT (volume). | SU(2)/SO(3), 3D spatial Hamiltonian | κ (lattice) units. "On spatial refinement the guaranteed mass can decay and the upper endpoint can diverge." "As the electric coefficient diverges in physical units, the energy-weighted law loses all mass below every fixed physical energy." | 13 Lean declarations for scalar and measure steps. "Lean rejected all four" mutations (**verified**). | "Existence and a common lower mass gap for four-dimensional continuum Yang–Mills remain open." |
| 7 | SS/adjoint-band/wilson-limit.md | Spatial spacing fixed. Along a selected j(n) ≥ J(n) with dyadic a_j and growing boxes, the cutoff open window carries liminf mass ≥ w. Filtered readings converge uniformly. | JOINT (time step and volume, on a selected path with "no stated rate"; B4's explicit schedule is an alternative) | SU(2)/SO(3), anisotropic 4D Wilson | "Spatial spacing remains fixed throughout." | Text proof. Lean selection theorem and counterexample. | A common physical rate on a dense family. |
| 8 | SS/adjoint-band/review.md | D4 read back B4's time regulator and joint-regulator identities, A4's magnetic coefficient (6144 → 368), and C4's analytic-quotient commutant. | Headline ONE-LIMIT (time step, fixed volume); other items FIXED | SU(2); C4 item general compact connected | Lattice | Numerical: 40 matrix tests, residual 2.31e−13, reversed order 4.01e−5. Replays of 53 Lean declarations by others, covering "selected steps". | C4 item: "A uniform overlap, a bound on the length of histories, and density after taking the continuum limit are further questions." |

### Lane 2 against the problem requirements (child's verdicts, with r4-c adjustments marked)

| Req | Disposition | Basis |
|---|---|---|
| (a) continuum limit on R^4 | PARTIAL: time step and volume only | wilson-limit: "Spatial spacing remains fixed throughout." |
| (b) RP / OS | NOT ADDRESSED (child). **[r4-c]** It is at most a control-level test: positive-time/README §Controls uses a two-time RP test to detect a signed spectrum. Reconstruction is deferred to G4. | positive-time/README §Controls; §Why the comparison works ("G4's reflection-positivity interface") |
| (c) Euclidean invariance | NOT ADDRESSED | — |
| (d) nontriviality | NOT ADDRESSED | The band shows a nonzero excitation at fixed mesh only. |
| (e) mass gap > 0, physical units | Child: PARTIAL. **[r4-c] ADDRESSED AT FIXED REGULATOR** (adjoint band, lattice units). Otherwise only CONDITIONAL criteria. | adjoint-band/README; SS/README l.50 |
| (f) all compact simple groups | NOT ADDRESSED (SU(2) only; the group quantifier is deferred to C4) | SS/README §still needs |

CLAIMED: none.

## 6. Contradictions or incompatible conventions (both lanes)

No logical contradiction found. These are tensions or unconverted conventions:

1. **Two "Wilson trajectories".** SS/positive-time/README.md §"What happens on the strong-coupling Wilson trajectory" says all connected autocorrelation limits vanish (tanh β_s, tanh β_t ≤ 1/20). SS/adjoint-band/wilson-limit.md §Choosing the spacings and CQ/momentum/wilson-time.md §Spectral windows say a positive band survives. Those use β_t=κ_B/a→∞ and β_s=aλ at a fixed spatial mesh. The regimes are disjoint, since β_t→∞ leaves strong coupling, but no note states this reconciliation. (The child raised this.)
2. **Hamiltonian normalizations.** These are:
   - CQ/momentum/README: −κΣΔ_e with an arbitrary bi-invariant metric.
   - CQ adjoint-weight.md and adjoint-refinement.md: A4's −κΣX², generators iσ/2.
   - SS/adjoint-band/README: −(κ/4)Δ, unit round metric.
   - B4: −(2κ_B)^{-1}Δ.

   Stated conversions: κ=2/κ_B (CQ adjoint-weight §2, CQ wilson-time §1, SS review.md §1). SS adjoint-band/README does not state its relation to A4's κ. They coincide, because |iσ_j/2| = 1/2 in the round metric, and both give M_1 = 8κ at g=0 (my hand check, notes.md step 15). SS wilson-limit gives no conversion.
3. **JointCutoff declaration count.** SS/adjoint-band/review.md §B4 joint regulator says "All twelve declarations of JointCutoff" (revision 48fe5d2c). review.md l.35 again says 12. CQ/momentum/execution.md says "B4's fourteen JointCutoff declarations at 10820b46". The revisions differ and no note reconciles the counts.
4. **Lean toolchains.** SS diagonal/vacuum/README use Lean 4.24.0 with Mathlib f897ebcf. CQ execution files and SS review.md replays use Lean 4.19.0 with Mathlib c44e0c8e (CQ/execution.md: core Lean only). The SS Lean files cannot be replayed on this host's 4.19.0 as pinned.
5. **Band endpoints.** SS adjoint-band gives L ≥ κ/576 for a single plaquette in every box. CQ adjoint-refinement gives δκ/12288 for arbitrary smearings at a fraction 1−δ of momenta. These are different statements, not a contradiction. SS adjoint-band cites CQ's 1024E_*N_c/κ consistently with CQ's text.

## 7. Statements most in need of independent review, per lane

**CQ.** No note explicitly flags anything for review. My selection uses the lane's own statements of which steps are text-only (not in Lean):

1. The commutant and analytic-continuation proof that quotient histories span exactly H^{D_V} (finite-graph.md §commutant; analytic-groups.md §Proof). local-response/execution.md: "commutant and analytic continuation proofs … are mathematical proofs in the notes." SS review.md §C4 is a read-back by another director of the same program.
2. The conditional heat-kernel density comparison and the private-link cross-term cancellation giving a>0 (momentum/local-estimates.md). momentum/execution.md: "The mathematical notes establish the heat-kernel comparison, the actual cross-term cancellations…"
3. The Wilson-time transfer of the momentum band (momentum/wilson-time.md). momentum/execution.md: "Its operator and weak-limit arguments are in the Wilson note". It rests on B4's external bounds.

**SS** (child's list; quotes checked by grep):

1. execution.md l.22: "Independent scientific assessment requires a separate reviewer."
2. adjoint-band/execution.md l.15, l.17: the Haar, domain and transfer steps and the spectral theorem are analytic, not Lean.
3. thin-loops.md l.16: "Wilson factorization, the graph bound … are analytic."

## 8. What I did not check

- Correctness of any proof, Lean declaration or script. None of the .lean, .py or evidence files is in input/. Lean was not run.
- External sources the lanes cite: A4, B4, G4, E1, E2, Yarotsky and others.
- SS files I did not read in full myself: thin-loops.md, execution.md (read lines 5–36), adjoint-band/execution.md and positive-time/execution.md (grep only). Their rows rest on the child.
- SS child rows 3, 4 and 8 were not among my five checks. I did confirm row 3's counts.
- Whether the line numbers the child quotes (l.NN) are exact.

## 9. Delegated question and outcome

- **Delegated:** extract the smaller lane (spectral-support, 11 files) with the same template, in child/ with its own register. The control question was −ln(tanh 1).
- **Returned:** control 0.272341 (correct). There are 8 result rows. The requirements table has none CLAIMED. It lists 2 conventions or tensions and 3 review flags. The child's verify PASSed. I reran its count.py through child/pcp (K2 exit 0) and its verify (PASS).
- **Five rows checked against the files:** SS/README, diagonal, vacuum, wilson-limit and adjoint-band/README. Result: **4 matched, 1 partial.** The regime class of adjoint-band/README was corrected to FIXED. Requirement verdicts (b) and (e) were adjusted as marked.
- **Process defect:** the harness blocked the child's write of report.md. The parent saved the text and marked it.

## 10. Rerun commands

From C:/Users/donke/z4-workers/r4-c, in Git Bash:

```sh
export PYTHONUTF8=1
python -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"          # expect 0.272341
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py init pcp --principal principal --principal-name "Kirtus Justus"   # only in a fresh dir
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name count_md  --expect-exit 0 -- python count_md.py   # fails by design (own expectation 28)
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name count_md2 --expect-exit 0 -- python count_md2.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
cd child && python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name count --expect-exit 0 -- python count.py && python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```

Each run of count_md*.py writes a new counts*_N.txt and never overwrites an earlier one.
