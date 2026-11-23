# INDEX of repo/yang-mills (worker a1-idx, for Director Z4)

Read-only copy at `repo/yang-mills`. Method: each folder's README, then sub-READMEs (opening paragraphs and "open / not / remains" lines), Lean declaration names by grep. No program rerun, no Lean compiled. transfer-operator (B4) rows come from the child worker (`child/INDEX_B4.md`), reread and spot-checked by me (see report.md); my own corrections are marked [a1].

Status codes: **T** proved in text; **T+Lf** text proof, Lean (file) checks only finite/scalar/algebraic steps, as the README says; **L** the main statement itself is a Lean theorem (names given); **C** exact or certified computation; **M** Monte Carlo measurement; **Cj** conjectural/proposed. Every Lean file below compiles per its own execution record; I did not recompile any.
Regime codes: **FM** fixed spatial mesh (Hamiltonian or Wilson at a fixed spacing); **SC** strong coupling (small β or small κλ); **WK→free** β→∞ (with or without b→0) where the limit is Gaussian/free; **b→0 int** statement about the interacting Wilson law along b→0; **abs** abstract (any operator/measure). Volume: **unifL** uniform in box size; **fin** finite box.

## Top level
| path | statement (author's scope) | status | file says NOT established | layer |
|---|---|---|---|---|
| `README.md` | Clay problem statement (3 lines). | – | – | – |

## observable-normalization (A4)
| path | statement | status | NOT established | layer |
|---|---|---|---|---|
| `observable-normalization/README.md`, `SeparatedTime.lean` | abs: finite positive sums, C(t) ≥ C(0) − t·M₁; variance floor + first-moment ceiling along cutoffs ⇒ positive limit correlator at t* (`momentLowerBound`, `separatedTimeWitness`). Examples μₙ=δₙ, n⁻¹δ₁ lose correlation. | L (finite-sum); measure version T | "remains open" that any renormalized gauge-invariant smeared observable obeys these bounds along a 4D continuum, infinite-volume trajectory; gives no lower bound on the spectrum | L4 (criterion), NEG |
| `…/wilson-variance/` | 4D periodic SU(2) Wilson, every β ≥ 0, finite lattice: Var(Σc_p Tr U_p) ≥ (4e^{-15/4}/99) sin⁴(1/(4√(1+β))) Σc_p²; unifL; coefficient ~(1+β)⁻². | T+Lf (`WilsonVariance.lean`) | "No spectral gap, mixing estimate or infinite-volume limit enters" | L2 (FM/any β, floor → 0 as β→∞) |
| `…/thin-loops/` | 4D Wilson, any β: thin loop with L edges has |EF| ≤ 2ε, Cov(F,G) ≤ 2ε√VarG, ε=exp[−L/(19(4β+1))], unifL. | T+Lf (`ThinLoop.lean`) | – (it is a decorrelation statement) | L2, NEG (unrenormalized long loops decorrelate) |
| `…/hamiltonian-variance/` | SU(2) Kogut–Susskind Hamiltonian, FM, every κ>0, λ≥0: centered plaquette has positive autocorrelation at every fixed time, unifL. | T+Lf | dependence on couplings "matters when the spatial mesh changes" | L4 at FM |
| `…/hamiltonian-variance/excited-band/` (+`third-moment/`, `electric-endpoint/`) | Same Hamiltonian, FM, every coupling: plaquette spectral weight ≥ w in [L,U], unifL; M₂ ≤ 86 401κ²; L = max(A/16, κ/18). | T+Lf | upper bounds on bottom of spectrum only; no lower gap. Z4 audit: [L,U] ∝ 1/b on bare trajectory, w→0 as β→∞ | L2/L4 at FM |
| `…/wilson-loop/`, `…/smeared-plaquettes/` (+`moment-bounds/`, `action-curvature/`) | Hamiltonian at FM: first energy moment of smeared plaquettes by integration by parts; covariance lower bound for every smearing; coupling-averaged action has energies of order κ√G. | T+Lf | `moment-bounds`: single bare plaquette loses all weight at fixed physical energy under refinement; `action-curvature`: energies of order 1/b on bare trajectory | L2 (FM), NEG (refinement) |
| `…/energy-density/` (README, `spatial-limit.md`) | SU(2) Hamiltonian; bare tree-level trajectory κ=2/(βb), λ=β/b, β≥1, b→0: conserved-energy density has a volume- and cutoff-uniform first moment (b³D_H ≤ 25). | T+Lf (`EnergyDensity.lean`) | "Proving a nonzero limiting norm remains open" | L2 (upper bound, b→0 int, Hamiltonian) |
| `…/energy-density/lorentz-test/` | Conditional: the b²-normalized conserved-energy tests cannot give nonzero T⁰⁰ in a Poincaré-invariant vacuum theory. | T+Lf | conditional on identification; existence open | NEG (kills that normalization), L7 |
| `…/energy-density/wilson-contact/` | 4D periodic SU(2) Wilson, every β→∞ as b→0, unifL: smooth magnetic insertion has time-slice variance ≥ order b⁻⁵; removable part does not affect separated readings. | T+Lf | "size of the interacting separated reading and … mass gap remain open" | L2 (b→0 int; divergence of sharp-time variance) |
| `…/energy-density/contact-law/`, `star-orders/`, `star-reconstruction/`, `staple-response/` (+`staggered/`) | 4D SU(2) Wilson, β,L→∞, bL→∞: contact residual → Gaussian white noise; star observables have Gaussian Hermite-rank limits, correlations ∝ t^{−8q}; staple variance 3/2 − 1/(8β) − … . star-orders also: M at β=2.3, 8 on 4⁴. | T+Lf; star-orders also M | "no interacting Yang–Mills construction on a trajectory with nonzero renormalized interaction" (star-orders) | L3/L2 WK→free |
| `…/energy-density/maxwell-benchmark/`, `momentum-transport/`, `positive-time-sum-rule/`, `plaquette-response/` | Free Maxwell spectral densities; separation formulas assuming a covariant limit; abs sum rule; plaquette-response: finite box, small λ (electric vacuum = strong coupling in g). | T+Lf | "No signal floor, continuum construction or mass gap … follows"; plaquette-response "supply no uniform spectral weight … under spatial refinement" | L2 (free/abs/SC) |
| `…/replica-gap/` (+`exterior/`, `thermal-count/`, `spectral-weight/`) | Three periodic partition functions bracket the full finite-volume gauge-invariant transfer gap; explicit at SU(2) electric endpoint; certified λ₂/λ₁<0.990 on one open cube at β_s=1, β_t=0.01. | T+Lf; C (certificates) | "interacting continuum construction and a uniform gap along a physical trajectory remain open" | L5 at FM/fin (diagnostic) |
| `…/uniform-band/` | 4D isotropic SU(2) Wilson, even L≥8, small positive β: first transfer band isolated with constants independent of L; mass expansion. | T+Lf | strong coupling only | L5 SC |
| `…/transfer-increments/` | abs: V − C_k ≤ kD; sharp C(t) ≥ v·exp(−tM/v); counterexample showing transfer test strictly weaker than first-moment test. | L (finite) + T | identifying physical time requires k_n a_n → t and convergence | L4 criterion, NEG |
| `…/boundary-weight/` | Open cube, static covariance spectrum above 4+δ has positive fraction in boundary layer of fixed thickness. | T+Lf | – | L1/L2 FM (boundary artefact) |

## central-quotients (C4)
| path | statement | status | NOT established | layer |
|---|---|---|---|---|
| `central-quotients/README.md`, `CentralQuotient.lean`, `Model.lean`, `cube-strip.md` | Exact SO(3) pushforward density of fundamental SU(2) Wilson weight = Π cosh · Σ_closed surfaces Π tanh; single cube at identity, β=log 2: 8177/2048 vs independent-face 15625/4096; strip: ratio grows exponentially. Flat SO(3) rep of T⁴ with no flat SU(2) lift (Klein four); census 46/210. One-link E2 quotient gap −γ log λ > 4γ/(4+γ). | T; Lean kernel-checks the finite identities (9 decls, e.g. `cube_weight_at_identity`, `flatLift_iff`, `four_cycle_census`, `pfaffian_zero`) | "The continuum construction, physical mass scale, and gap remain open"; Lean "does not formalize measure theory or QFT reconstruction"; T⁴ example "supplies no topological obstruction" on ℝ⁴ | L6, NEG |
| `…/local-response/` (+`finite-graph.md`, `analytic-groups.md`, `rotor.md`) | Open cube strip, every finite β: influence ≤ tanh^{4d}β uniformly in length and SO(3) config (sharp). Finite graphs: quotient-link histories generate the center-fixed physical sector (full cover spectrum for SU(N) on simply connected box). Rotor: first spectral weight can vanish with coupling. | T+Lf (`LocalResponse.lean`) | gap and continuum open | L6 at FM |
| `…/momentum/` (+`infinite-volume.md`) | Compact connected simple G, FM, finite couplings: center-neutral plaquette has weight in a common bounded interval at most momenta, unifL; all momenta if a volume-uniform gap is supplied (B4). | T+Lf | band moves to UV energies on B4's trajectory (per Z4 disposition); conditional for every-momentum version | L2 FM |
| `…/locality/` (+`wilson-real-time.md`) | Compact G Wilson Hamiltonians, open/periodic box: Lieb–Robinson speed ∝ b√(κλ) in physical units, unifL, finite along bare SU(2) weak-coupling trajectory as b→0 (speed 6.914 in bare units). | T+Lf | "nontrivial four-dimensional limit, Lorentz covariance with the physical speed of light, and a positive physical mass gap remain open" | L7-adjacent (locality bound, b→0 int, Hamiltonian) |
| `…/clustering/` (+`strong-coupling.md`) | Finite regulator: gap ⇒ quantitative spacetime clustering; inverse test; applied in B4's small-magnetic-coupling interval. | T+Lf | physical mass and continuum "remain open" | L5 tool, SC |
| `…/electric-disorder/` (+`wilson-readings.md`, `multiplicity.md`) | SU(2): center-flipped vacuum has energy concentrated at 2λn, unifL; on Wilson transfer every β→∞, 0<a≤b: weight below (1−δ)2λn → 0. | T+Lf | on bare path these states "move to ultraviolet energies"; lowest excitation open; upper tail at a=b open | L6/L2, b→0 int (UV escape) |
| `…/tangent-curvature/` | Isotropic SU(2) Wilson, β,L→∞ any rates, fixed cells: √β·Im U_p → Gaussian (exact 2-cochain projection); action spectral mass ~ε⁸; finite-regulator gap → 0 in lattice units. | T+Lf | "different windows"; free limit | L3 WK→free, NEG |
| `…/magnetic-smearing/` (+`connector/`, `transfer-clock/`) | Explicit rapidly weakening SU(2) trajectories (b→0, β fast): fixed-physical-size smeared magnetic curvature has positive connected readings; field → free Maxwell. Connector: positive limit on fast trajectories, → 0 if β grows slower than connector length. | T+Lf | "The interacting physical spectrum remains open" | L4/L3 WK→free |
| `…/magnetic-smearing/flow-reflection/`, `flow-momentum/`, `spatial-flow/` | 4D gradient-flowed observables: reflected form across original plane strictly negative (every buffer, every grid, every momentum); disposes of Jofer v4 Thm 18.74 shifted-plane step. Spatial flow keeps transfer positivity. | T+Lf; C (certificates) | – | NEG (kills "flowed observables inherit RP"), L1 |
| `…/magnetic-smearing/flow-basis/` | Flow-time basis in fixed [a,b] can expose arbitrarily low energies; cost log χ ≥ C/ε². | T+Lf | – | NEG, L5 diagnostics |
| `…/lie-curvature/` | Compact simple G, character actions: Gaussian Maxwell color per Lie dimension; SU(3) charge-odd ratio 5/9 on explicit trajectories (β=r¹⁷). | T+Lf | free trajectories | L3 WK→free, L6 |

## spectral-support (D4)
| path | statement | status | NOT established | layer |
|---|---|---|---|---|
| `spectral-support/README.md`, `SpectralLimit.lean` | abs: common decay rate r on a dense family at late times (cutoff limit first) ⇒ μ_v((r,1])=0 ⇒ no spectrum below −log r/τ; endpoint atom; `decayAtRoundedTime`. Six E1 readings admit gapless measure (exact rationals, `check_family.py`). | L (`noTransferMassAbove`, `projectionVanishesOfDense`, `denseProjectionOfMomentBounds`, `endpointAtom`, `indistinguishableReadings`) + C | "Constructing the 4D YM theory and deriving that rate for it remain open"; "No rate for interacting four-dimensional Yang–Mills has been derived" | L5 criterion, NEG |
| `…/diagonal/`, `…/positive-time/` (+`vacuum/`) | abs: weak convergence of cutoff measures + one late time per cutoff ⇒ exclusion; positive-time comparison e^{mt}C(t) ≤ e^{mu}C(u); gap above whole vacuum kernel via fixed time difference. | L (`diagonalSpectralExclusion`, `nullTailOfWeakLimit`, `positiveGapAboveKernel`, …) | criteria only | L5 criterion |
| `…/adjoint-band/` | SU(2) Hamiltonian FM, every coupling, unifL: adjoint plaquette weight at energies ≥ κ/576; inherited by a selected joint Wilson-time/volume limit; SO(3)-measurable. | T+Lf | FM only | L2/L6 FM |
| `…/finite-readings/` | FM, 0 ≤ λ/κ ≤ √3/512: ≥3/4 raw mass in [5κ/2, 7κ/2]; first excitation ≤ 7κ/2; three readings exclude proposed gap 4κ. | T+Lf | SC/FM | L5 (upper bound on gap), SC |
| `…/electric-scale/` | Compact simple G, FM, unifL: vacuum needs ~g^{d/4} electric states per link; center flux law; class probes have signal only at times τb (→0 physically). | T+Lf | full local center-flux algebra loses connected weight at fixed physical times | L2, NEG |
| `…/graph-holonomies/` | 4D Wilson, any compact G, b(1+β)→0: holonomies on fixed physical graph → independent Haar (TV); OS form on positive-time cylinders has rank one; SU(2) compensated path → group Brownian motion. | T+Lf | "Construction of a nontrivial renormalized four-dimensional theory … remain open" | NEG (unsmeared probes), b→0 int |
| `…/ordinary-loop/`, `…/electric-slab/`, `…/staple-spectrum/` | SU(2) Wilson on explicit very weak trajectories (e.g. L=β=⌈exp(log²(2+r))⌉, β=r⁶⁵): β-rescaled fixed-size loops, link-star insertion have limits identifying the free 3-color Maxwell sector; staple: lattice-unit energy–momentum measure on every joint weak trajectory. | T+Lf | "Establishing an interacting continuum theory … remain[s open]" | L3/L4 WK→free |
| `…/scalar-response/`, `…/dual-scalar/` | Finite open 4D boxes, β→∞: signed Wilson triangle has nonzero first interacting coefficient (−0.0394…/β; 0.0411…/β), distinguishing SU(2) from Abelian. | T+Lf; C | finite box, O_box remainders | L4 at fixed box (perturbative order) |
| `…/magnetic-band-rank/` | abs: seven readings certify ≥3 distinct energies; applied to C4 fast trajectories: finite-box energies dense on compact intervals. | T+Lf | – | L5 diagnostics |
| `…/boundary-spectrum/` | Open cube: number of static coefficients > 4.01 grows like boundary area. | T+Lf; C | – | L1 FM (boundary artefact) |
| `spectral-support/evidence/`, `…/evidence` dirs | Execution/replay material. | – | – | none |

## g4 (G4)
| path | statement | status | NOT established | layer |
|---|---|---|---|---|
| `g4/README.md`, `ReflectionPositivity.lean` | abs: pointwise limit of kernels with nonnegative finite quadratic forms has nonnegative forms (also eventually). Controls: [[1,2],[2,1]]; 1/(1+s+t) RP+clustering without gap (text). | L (`kernel_limit_nonneg`, `limit_nonneg_eventually`, `adverseKernel_form`) | "Neither theorem assumes or establishes a common convergence rate or existence of a convergent regulator trajectory"; 5 listed obligations open | L1 (limit-stable), NEG |
| `g4/complex/`, `g4/integral/` | Complex/sesquilinear and Bochner-integral versions; exact pushforward; split compact-group holonomy action RP (`integral/wilson-kernel.md`). | L (`Q_nonnegative_of_entrywise_tendsto`, `reflectedIntegral_map_nonnegative`, …) | continuum test algebra open | L1 |
| `g4/wilson/`, `g4/periodic/`, `g4/site/` | Wilson law on finite open temporal slab is RP (`openSlab_wilson_reflection_positive`); periodic boundary-graph law RP; shared-boundary mixture transfer. Haar and representation are inputs. | L | Haar not constructed in module; "not a construction of continuum Yang–Mills" | L1 (each cutoff) |
| `g4/exterior/` | 4D SU(2) Wilson, assuming Gibbs specification + site RP: site-plane masks preserving half-cylinder quotient; two-time boundary measurement certifies compact positive band. | L (`ExteriorStates.lean`) + T | conditional on stated assumptions | L1/L2 FM |
| `g4/flow-audit/` | Confirms C4: at lattice flow time 20, slices 1–2, β = side ℓ, large even SU(2) cubes: reflected form negative. | T + L (`negative_form`) | concerns fully flowed observables only | NEG |
| `g4/contact-blocks/`, `g4/block-recovery/`, `g4/spatial-flow-variance/` | Conditional convergence of A4 contact residual to white noise in H^{-s}_loc; reflected-tail bound; flowed plaquette variance bounds. | L (parts) + T | written argument for full residual not in Lean | L2/L3 WK→free |
| `g4/evidence/`, `cross-lane-review.md` | Replays and cross-reads of C4/D4. | – | – | none |

## volume-uniformity (Z5)
| path | statement | status | NOT established | layer |
|---|---|---|---|---|
| `volume-uniformity/README.md`, `VolumeUniformity.lean` | Free massless lattice field: lowest mode ≤ 2π/L; gap ≤ C/L ⇒ no uniform gap; massive control uniform. | L (`massless_mode_energy_le`, `massless_physical_gap_le`, `no_uniform_gap`); C (`free_field_volume_control.py`, 3 met) | "No statement about a non-abelian theory"; no challenger | NEG (finite-box gap ⇒ nothing) |

## z4 (Z4)
| path | statement | status | NOT established | layer |
|---|---|---|---|---|
| `z4/README.md` §1, `lean/Z4YM/Scaling.lean`, `TwoSided.lean` | abs sequences: a_n→0⁺ and lattice gap ≥ c>0 ⇒ physical gap → ∞; finite physical gap ⇒ lattice gap → 0; two-sided bounds. | L (`not_uniform_lattice_gap_and_finite_physical_gap`, `physical_gap_tendsto_atTop`, `twoSided_of_tendsto`, `twoSided_cluster`) | "4D trajectory not known; no proof that the lattice-unit gap vanishes at that rate" | NEG (kills SC ⇒ continuum gap), L3 |
| `z4/README.md` §2–3, `FiniteGroupControl.lean`, `LevelsControl.lean` | 2D exact controls: U(1), SU(2) gaps → 1/2, 3/8 on β∝1/a²; Z_n gaps collapse on that trajectory. | L (finite group) + C (P1–P3 met) | two dimensions only | NEG/control |
| `z4/README.md` 2nd round, `TrajectoryAudit.lean` | A4 window [L,U] and B4 fixed-mesh gap ∝ 1/b; leave every fixed physical window when b→0 with β=o(b^{-1/2}); w→0 as β→∞. | L (`L_lower`, `w_upper`, `L_tendsto_top`, `w_tendsto_zero`, `L_bounded_forces`) | "says nothing about the true spectrum" | NEG (audit) |
| `z4/fixed-size/STATEMENT.md`, `HeatRegularized.lean`, rounds 5–11 | Free Maxwell benchmark: sharp-time smeared action density variance ~b⁻⁵, flowed version converges, no gap; norm/moments from two positive-time readings. One non-free MC measurement (loops at β=2.2–8). | L (abs) + C + M | "No estimate for the interacting theory" | L2 free, M |
| `z4/OVERALL_DISPOSITION.md`, `LITERATURE.md` | Z4's own lane-by-lane summary. | summary | see inflation/deflation note below | – |

## transfer-operator (B4) — from child, reread by a1
| path | statement | status | NOT established | layer |
|---|---|---|---|---|
| `transfer-operator/README.md`, `TwoSector.lean` | abs two-sector determinant test c² ≤ (u−m)(v−m) ⇒ defect ≥ am; adverse finite family T_a with lowest energy ≤ 2a; one-link SU(2) floor −g log r ≥ 3g/(2g+3). | L (`comparison_iff`, `block_defect`, `no_uniform_floor`, `one_link_floor`) + T | Wilson-lattice estimates for coupling "remain open" | L5 criterion, NEG |
| `…/hamiltonian-time/`, `…/blocked-time/` | SU(2), fixed spatial spacing, β_t=κ/a, β_s=aλ, z=κλ ≤ 1/384 (blocked) / small z (via Yarotsky): transfer gap ≥ 4 log 3/(13κ) uniform in L and a; local correlations converge for a↓0, L→∞. | T+Lf (`BlockedTime.lean`, `HamiltonianTime.lean`) | spatial refinement: `blocked-time/local-limit.md` obstruction; large-z gap undetermined; Z4: ∝ 1/(βb) | L5 FM+SC; L3 time direction only |
| `…/joint-cutoff/` | SU(2), side L, ac ≤ 1/36, c=6λL³+6/κ: |log-transfer gap − Hamiltonian gap| ≤ 180ac². | T+Lf (`JointCutoff.lean`) | bounded box; no lower bound on gap | L1/L3 (time only) |
| `…/strong-coupling/` | 4D Wilson, tanh β_s, tanh β_t ≤ 1/20: centered transfer norm ≤ 1/3 unifL; forces connected matrix elements → 0 as a→0 at fixed time. | T+Lf (`WilsonInfluence.lean`) | "A nontrivial Yang–Mills scaling limit … requires a different trajectory" | L5 SC, NEG |
| `…/connected-rectangles/`, `…/wilson-surfaces/` | Isotropic SU(2) Wilson, infinite volume, strong coupling: rectangle connected correlations C_k = B_k z^{D_k}(1+o(1)); torus mass min(4,L)|log β|+O(1); mean-normalized signed rectangle diverges at fixed physical time. | T+Lf | weak-coupling trajectory "remains open" | L5/L2 SC, NEG |
| `…/girth-shell/`, `…/periodic-time/` | Finite SU(2) lattice, temporal limit first: first cluster = shortest-cycle covariance, enclosures at β_s=1, β_t=0.01; periodic Wilson RP at two seams. | T+Lf; C | "existence and positive physical mass of four-dimensional continuum Yang–Mills remain open" (verified, `girth-shell/README.md:14`) | L1, L5 FM |
| `…/weak-cavity/` | Open cube of fixed N cells, g↓0 (couplings → ∞ at fixed lattice): six lowest levels → free formula; gap ~ 2√2π/√N → 0 on growing box; local spectral density to E=0. | T+Lf; C | free limit; interacting scale undetermined | L3 WK→free, NEG |
| `…/spatial-heat-trace/` | Original isotropic SU(2) Wilson, b²(1+β)→0: unrenormalized charged heat trace per volume → 0 (faster than any power if β polylog); centered vector has no weight on [0, x^η/a]. | T+Lf (`HeatTrace.lean`) | lowest excitation undetermined | NEG/L2, b→0 int (covers log trajectories) |
| `…/coarse-holonomies/`, `…/spatial-plaquette/` | Thin-path holonomies decorrelate when Σε_e² → 0; spatial slice extrema: ‖I − cB_κ‖ ≥ (1−b)/(1+b) kills a global-norm comparison route. | T+Lf | no continuum/gap claim | NEG |
| `…/pcp/` | Tooling (`replay.py`, `worker.c`). | – | – | none |

## (a) Interacting theory at fixed finite spacing (≤12)
1. G4 `wilson/`, `periodic/`: Wilson law RP on finite slab / periodic (Lean), every β, any compact G. (L1)
2. B4 `blocked-time/`, `hamiltonian-time/`: SU(2) transfer gap ≥ 4 log 3/(13κ), unifL, z ≤ 1/384, fixed spatial mesh. (L5 FM)
3. B4 `strong-coupling/`, `connected-rectangles/`, A4 `uniform-band/`: 4D isotropic Wilson at small β, lattice-unit gap unifL. (L5 SC)
4. A4 `hamiltonian-variance/excited-band/`, D4 `adjoint-band/`, C4 `momentum/`: plaquette/adjoint spectral weight in a bounded positive window, every coupling, unifL. (L2/L4 FM)
5. A4 `wilson-variance/`: 4D Wilson variance floor ~(1+β)⁻², every β, unifL. (L2)
6. A4 `replica-gap/`: partition-function brackets of full finite-volume gap; certified on one cube. (L5 fin)
7. C4 root + `local-response/`: exact SO(3) pushforward density; quotient-history sector; strip decay tanh^{4d}β. (L6)
8. C4 `electric-disorder/`: center-flip energies 2λn unifL. (L6/L2)
9. D4 `scalar-response/`, `dual-scalar/`: first interacting coefficient nonzero on fixed boxes. (L4 perturbative)
10. B4 `joint-cutoff/`: Hamiltonian vs Wilson-transfer gap within 180ac² on bounded box. (L1/L3 time)
11. D4 `finite-readings/`: at small λ/κ first excitation ≤ 7κ/2 (upper bound). (L5)

## (b) Limits toward a free (Gaussian) theory (≤12)
1. C4 `tangent-curvature/`: β,L→∞ at fixed cells → Gaussian curvature, spectral mass ε⁸.
2. C4 `magnetic-smearing/`, `lie-curvature/`: explicit fast trajectories → free Maxwell; positive fixed-size readings.
3. D4 `ordinary-loop/`, `electric-slab/`, `staple-spectrum/`: free 3-color Maxwell sector identified.
4. A4 `energy-density/contact-law/`, G4 `contact-blocks/`: contact residual → white noise.
5. A4 `energy-density/star-orders/`, `star-reconstruction/`, `staple-response/`: Gaussian Hermite-rank limits.
6. B4 `weak-cavity/`: g↓0 at fixed cube → free levels; gap closes as N grows.
7. Z4 `fixed-size/`, `maxwell-benchmark/` (A4): free Maxwell benchmark, no gap.
8. Z5 `volume-uniformity/`: free massless field (control).
9. Z4 §2: 2D U(1)/SU(2) exact (2D, not free but exactly solvable control).

## (c) Obstructions (NEG) and the inference each kills (≤12)
1. B4 root adverse family → "gap in each of two sectors ⇒ gap".
2. A4 root μₙ=δₙ; A4 `transfer-increments/` → "equal-time normalization (+ threshold) ⇒ surviving correlation".
3. D4 root six-reading gapless measure; eigenvector ⊕ L²(0,½) → "finitely many readings / one vector's decay ⇒ gap".
4. G4 root 1/(1+s+t), [[1,2],[2,1]] → "RP + clustering ⇒ gap"; "entrywise positivity ⇒ RP".
5. C4 `flow-reflection/`, `flow-momentum/`, `spatial-flow/`, G4 `flow-audit/` → "4D-flowed observables inherit RP across the original plane" (incl. Jofer v4 Thm 18.74 step).
6. D4 `graph-holonomies/`, B4 `spatial-heat-trace/`, `coarse-holonomies/`, A4 `thin-loops/` → "unrenormalized fixed-physical-size holonomies/loops give a nontrivial limit" (OS form rank one).
7. Z4 `Scaling.lean` + `TrajectoryAudit.lean`, B4 `strong-coupling/` → "uniform lattice-unit gap (strong coupling / fixed mesh) ⇒ finite physical gap in the continuum".
8. Z5 `volume-uniformity/` → "gap in every finite box ⇒ infinite-volume gap".
9. C4 root cube 8177/2048, strip → "SO(3) Wilson density factorizes over faces"; T⁴ Klein-four → "every flat SO(3) torus holonomy lifts".
10. A4 `energy-density/lorentz-test/` → "b²-normalized conserved energy gives nonzero T⁰⁰".
11. C4 `tangent-curvature/`, A4 `smeared-plaquettes/moment-bounds/`, `action-curvature/` → "single bare plaquette keeps weight at fixed physical energy under refinement".
12. Z4 §3 finite-group control; C4 `flow-basis/` → "positive transfer family with gaps ⇒ gap on the Lie-group trajectory"; "fixed flow-time window bounds low energies".

## Which links L1–L7 have no interacting-theory result uniform in the lattice spacing
**L3, L4, L5, L6, L7 have none.** No file gives an interacting continuum limit (every existence-of-limit statement is either toward a free/Gaussian theory or a trivialization to Haar/zero); no nonzero interacting limit (L4); no gap bound that survives b→0 (every gap bound is at fixed spatial mesh or strong coupling and is ∝ 1/b in physical units); the SO(3)/SU(2) comparison (L6) is exact per cutoff but no uniform bound on connected correlators exists (C4 says this is the needed next estimate); no Euclidean-invariance statement (L7) — C4 `locality/` gives only a finite Lieb–Robinson speed uniform in b, an inequality, not a symmetry axiom.
**L2** has interacting results uniform in b, but all are upper bounds or escapes: A4 energy-density first-moment ceiling, A4 wilson-contact variance ≥ b⁻⁵, C4 electric-disorder UV escape, B4 spatial-heat-trace / D4 graph-holonomies vanishing. None is a positive lower bound on a renormalized observable in the interacting theory.
**L1** holds at every cutoff exactly (Wilson RP, G4 Lean; transfer matrix), which is trivially uniform, but no limiting Hilbert space is constructed; G4's preservation lemma has no limit to apply to.

## Inflation found (partial: I did not compare every README sentence with its statement file)
1. `transfer-operator/blocked-time/README.md` title "A volume-independent physical gap for fine Wilson time steps": "physical" means Hamiltonian units at a fixed spatial mesh and z ≤ 1/384; on the bare trajectory it is ∝ 1/(βb) (Z4 audit) and `local-limit.md` states an obstruction under refinement. (child's finding, confirmed by a1 from title and `z4/README.md` table)
2. `observable-normalization/README.md` "Uniform isolation of the first Wilson transfer band gives the volume-independent spectral estimate" omits the restriction "small positive β" that `uniform-band/README.md:5` states (it adds "strong-coupling mass expansion" only for the expansion).
3. Deflation, relevant to the director: `z4/OVERALL_DISPOSITION.md` says "every result … is at a fixed spatial lattice spacing, or is a conditional criterion, or is a control model" and "every statement about refinement is an obstruction or an escape to infinite energy". The repository also has interacting Wilson-law results along b→0 that are positive but free-limit (C4 `magnetic-smearing`, D4 `ordinary-loop`, `electric-slab`) and a uniform locality bound (C4 `locality`). The conclusion (no interacting continuum result) is unchanged; the classification is incomplete.
No README claim was found that contradicts the statement file it summarizes.
