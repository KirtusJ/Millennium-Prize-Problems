# a1-rig report: what is rigorously established (for the Z4 SU(2) attempt)

Worker a1-rig. Control: `control.txt` = 0.272341 (= -ln tanh 1). Lean READY exists, but I did not use Lean (this is a literature brief). Fetched texts are in /tmp/a1-rig-dl only. Quotes are at most two sentences long.
Access limits: Project Euclid (Incapsula bot wall) and Springer/APS (login redirect) refused both curl and a web-fetch agent. Pre-2000 CMP/Ann. Phys. papers were therefore read **abstract only**, using the INSPIRE API. Every "ABSTRACT ONLY" below means I did not see the theorem statement itself.

## 0. Verdict table

Each verdict concerns the claim as I state it in the table for that question. DEFECT means a premise in the brief is wrong or misleading.

| item | verdict | one line of evidence |
|---|---|---|
| R1 requirements of the official problem | STANDS | Clay pdf, Sec. 4 p.6, fn.1 p.7, fn.2 p.12, read in full |
| R1 brief's paraphrase "spectrum in [Δ,∞) on the orthocomplement of the vacuum" | DEFECT (minor) | The text says "H has no spectrum in the interval (0, Δ)" and also requires the supremum m < ∞ (p.6). It never mentions an orthocomplement. |
| R1 "for SU(2)" as a solution | DEFECT | The problem says "for any compact simple gauge group G" (p.6). An SU(2)-only result is partial. |
| R2 Osterwalder-Seiler | STANDS (abstract level) | Abstract: physical positivity, a positive self-adjoint transfer matrix, existence and analyticity of the infinite-volume limit at strong coupling, Wilson confinement bound. Which reflections, the β range and the action class were NOT read. |
| R2 Lüscher 1977 | STANDS (abstract level) | Abstract: physical positivity holds in Wilson's lattice gauge theories, and H has only real eigenvalues. Hypotheses NOT read. |
| R2 Seiler LNP 159 | NOT CHECKED | INSPIRE record only |
| R3a Guth / Fröhlich-Spencer | STANDS (abstract level) | Guth: Coulomb-type lower bound on the Wilson loop for g² < 0.168, Villain action. FS: deconfining transition to a massless QED phase. |
| R3b Göpfert-Mack | STANDS (abstract level) | String tension α > 0 for all g² (3D, Villain action). Bound α ≥ const·m_D β⁻¹. Continuum limit is a free scalar of mass m_D. |
| R3c Adhikari-Cao | STANDS | Thm 1.1, read in full; the child's row is confirmed |
| R3d 2D | STANDS (partial) | Driver 1989 abstract: lattice expectations converge to the continuum. Chatterjee 2018 p.8: area law at all β for non-Abelian groups is known only in d=2. Mass gap in 2D NOT read. |
| R3e SU(2) in d=5, or a phase transition in d=4 | NOT CHECKED / nothing found | Tomboulis claims confinement at all couplings (arXiv:0707.2179). Ito-Seiler (0711.4930, 0803.3019) identify gaps, so this is not established. I found no d=5 result. |
| R4 Balaban | STANDS (abstract level) | LF II abstract: completes "the proof of the ultraviolet stability of four-dimensional pure gauge field theories, as formulated in Theorem 1". I did NOT read Theorem 1 itself. |
| R4 Magnen-Rivasseau-Sénéor | STANDS (abstract level) | SU(2), 4D, trivial topological sector, fixed infrared cutoff, no UV cutoff, regularized axial gauge. Slavnov identities checked. |
| R5a Shen-Zhu-Zhu | STANDS | Assumption 1.1, Thms 1.2 and 1.4, Cor 1.6, read in full |
| R5b Bakry-Émery constants | STANDS | SZZ eq. (4.8) Ric = α(N+2)/4 − 1 with α=2 for SU(N); eq. (4.2) Hessian bound 8(d−1)N\|β\|. Recomputed by check_rows.py (P6). |
| R5c two-scale criterion (GOVW Thm 3) | STANDS | GOVW p.306-307, read in full. It is stated on a **Euclidean space with linear P**, not on SU(N)^E. |
| R5c Otto-Reznikoff | STANDS (summary only) | Only Menz's restatement (arXiv:1309.0862, Thm 1.6) was read. It is for real-valued spins. |
| R5d Dobrushin-Shlosman | NOT CHECKED | Original not read. The two sources conflict on whether it has been carried out for LGT (see R5 table). |
| R5e Chatterjee 2021 | STANDS | Def 2.1, Thm 2.2, Def 2.3, Thm 2.4, read in full |
| R5f Chatterjee open problems | STANDS | Problems 4.1, 5.1, 5.2, read in full |
| R6 Gribov/Singer | STANDS (abstract level) | No continuous gauge slice on S⁴, for any compact non-Abelian group |
| R6 analyticity for all β, SU(N), d=4 | NOT CHECKED / nothing found | OS78 gives analyticity at strong coupling only. My one search found no theorem for all β. |

Counts (verdict rows): STANDS 16, DEFECT 2, NOT CHECKED 4. Rows marked "abstract level" stand only as far as the abstract goes.
Predicate counts (my program): met 6, failed 0, measured only 2. Register checks: 5 run, 1 failed (see Sec. 3).

## 1. Tables per question (with hypotheses and what each result does NOT give)

### R1. Official problem: Jaffe and Witten, "Quantum Yang-Mills Theory", claymath.org pdf. FULL TEXT.
| requirement | text locator | content |
|---|---|---|
| gauge group | Sec. 4, p.6 | "for any compact simple gauge group G" |
| space-time | Sec. 4, p.6 | "a non-trivial quantum Yang–Mills theory exists on R⁴" |
| axioms | Sec. 4, p.6 | "axiomatic properties at least as strong as those cited in [45, 35]": Streater-Wightman (Wightman axioms) and Osterwalder-Schrader CMP 31, 42 |
| local operators | Sec. 4, p.6 | Local quantum field operators in correspondence with gauge-invariant local polynomials in F and its covariant derivatives, e.g. Tr F_ij F_kl(x). Fn. 1 (p.7) says the 1-1 correspondence holds only up to renormalization subtleties. |
| short distance | Sec. 4, p.6 | Correlation functions "should agree at short distances with the predictions of asymptotic freedom and perturbative renormalization theory". This includes a stress tensor and an OPE with the prescribed local singularities. |
| mass gap | Sec. 4, p.6 | HΩ=0 and spec H ⊂ [0,∞). A gap Δ means "H has no spectrum in the interval (0, Δ) for some Δ > 0". The supremum is the mass m, and "we require m < ∞". |
| consequence | Sec. 5, eq. (2), p.6 | Clustering \|⟨Ω,O(x)O(y)Ω⟩\| ≤ exp(−C\|x−y\|) for C<Δ, ⟨Ω,OΩ⟩=0, at large \|x−y\| |
| excluded | fn. 2, p.12 | Weak existence by compactness is excluded unless other techniques establish properties of the limit (mass gap, axioms) |
| not required | Sec. 5, p.7 | Isolated one-particle state (upper gap), confinement and others are "natural extensions", not part of the problem |
| context | Sec. 6.5, p.11-12 | Reflection positivity holds for the Wilson action [OS78]. Establishing the Hilbert space is "part of the solution". Balaban's estimates are uniform in the lattice spacing on a torus and "need to be extended to the study of expectations of gauge-invariant functions". A gap uniform in volume needs "new ideas" (p.12). |

### R2. Lattice foundations
| addr | authors, title, year | locator, how read | statement | hypotheses / NOT given |
|---|---|---|---|---|
| doi:10.1016/0003-4916(78)90039-8 | Osterwalder, Seiler, "Gauge field theories on a lattice", Ann. Phys. 110, 1978 | abstract via INSPIRE: ABSTRACT ONLY | Physical positivity for lattice YM and fermions, hence a positive self-adjoint transfer matrix. "existence and analyticity of the infinite volume limit of strongly coupled Yang-Mills theories" and Wilson's confinement bound. | Strong coupling only. The exact β range, the class of reflections (through planes of sites vs. links) and the action class were NOT read. Says nothing at weak coupling or in the continuum. |
| doi:10.1007/BF01614090 | Lüscher, CMP 54 (1977) 283 | abstract: ABSTRACT ONLY | "physical positivity holds in Wilson's lattice gauge theories", and the Hamiltonian has real eigenvalues only | Wilson action. I did not read whether strict positivity T>0 holds for all β, or for which groups. |
| Lect. Notes Phys. 159 | Seiler 1982 | none: FROM MEMORY / NOT CHECKED | — | — |

### R3. Discriminator models (child's question; I reread the sources)
| addr | authors, title, year | locator, how read | statement | hypotheses / NOT given |
|---|---|---|---|---|
| doi:10.1103/PhysRevD.21.2291 | Guth 1980 | abstract (INSPIRE): ABSTRACT ONLY | A lower bound on ⟨W(C)⟩ "has the form of a Coulomb interaction and guarantees that electric charges are not confined", for g² < 0.168. The infinite-volume limit of ⟨W⟩ exists. Combined with OS78, there is at least one phase transition. | **Villain** action (not Wilson). A lower bound only: a perimeter-type law. The abstract does not say "massless photon". |
| doi:10.1007/BF01213610 | Fröhlich, Spencer, CMP 83 (1982) | abstract: ABSTRACT ONLY | "existence of a deconfining transition to a massless (QED) phase in the four-dimensional U(1) lattice gauge theory". Also Z_N for large N, XY in d≥3, abelian Higgs. | I did NOT read which correlation decays as a power, or with what exponent. |
| doi:10.1007/BF01961240 | Göpfert, Mack, CMP 82 (1981/82) 545 | abstract: ABSTRACT ONLY | 3D pure U(1), **Villain action**. String tension α > 0 for all g², with α ≥ const·m_D β⁻¹ for small a g², β=4π²/g², m_D² = (2β/a³) e^{−β v_Cb(0)/2}. Continuum limit at fixed m_D is a free scalar field of mass m_D, and α/m_D² → ∞. | Abelian, 3D, Villain. The gap is exponentially small in β. The continuum limit is a free field. |
| arXiv:2202.10375v3 | Adhikari, Cao, "Correlation decay for finite LGT at weak coupling" 2022/24 | Sec. 1.3, Thm 1.1, Rem 1.2, p.4-6: FULL TEXT | For β ≥ (114 + 4 log\|G\|)/Δ_G, Δ_G = min_{g≠1} Re(χ(1)−χ(g)): \|Cov\| ≤ 4(4·10²⁴\|G\|²)^{\|B1\|+\|B2\|} ‖f1‖∞‖f2‖∞ e^{−(β/2)Δ_G(L−1)}. Here f_i are conjugacy-invariant functions of loop holonomies in rectangles B_i at ℓ∞ distance ≥ L. | **Finite** G (non-Abelian allowed), **d=4 only**, finite box Λ ⊂ Z⁴ (any such box, constants uniform in Λ). Prefactor is exponential in \|B_i\|. No Lie groups. Fn. 1 p.2: Seiler's monograph's claimed extension to non-Abelian finite groups fails (Borgs). |
| doi:10.1007/BF01240222 | Borgs, CMP 96 (1984) | abstract: ABSTRACT ONLY | Finite **abelian** G at weak coupling: a unique translation-invariant state, and in 4D a non-translation-invariant state (flux tube) | Abelian finite groups only |
| doi:10.1007/BF01218586 | Driver, "YM2", CMP 123 (1989) | abstract: ABSTRACT ONLY | 2D continuum YM in complete axial gauge is defined via Lie-algebra white noise. Wilson-loop expectations are heat-kernel integrals in the areas. Lattice expectations converge to them. | Plane. Mass gap and OS axioms are not in the abstract. |
| arXiv:1803.01950v1 | Chatterjee 2018 | p.8: FULL TEXT | Area law at all β for non-Abelian groups "is currently known only in dimension two". Göpfert-Mack give the area law at arbitrary β in d=3 for U(1). | — |
| arXiv:0707.2179 vs 0711.4930, 0803.3019 | Tomboulis 2007; Ito, Seiler 2007/08 | abstracts: ABSTRACT ONLY | Tomboulis claims SU(2) confinement at all 0<g<∞, d≤4. Ito-Seiler point out "missing links" and "gaps". | **Not an established result.** The attempt must not cite it as a theorem. I found no rigorous SU(2) result in d=5, and none on the presence or absence of a d=4 phase transition. |

### R4. Ultraviolet side
| addr | authors, title, year | locator, how read | statement | NOT given |
|---|---|---|---|---|
| doi:10.1007/BF01215223 | Balaban, RG approach I, CMP 109 (1987) | abstract: ABSTRACT ONLY | 4D pure gauge, **small-field approximation**: localized effective actions via cluster expansions, β-functions, coupling-constant renormalization by a recursive RG system | — |
| doi:10.1007/BF01257412 / BF01238433 | Balaban, Large field renormalization I, II, CMP 122 (1989) | abstracts: ABSTRACT ONLY | The ℝ operation for large-field regions. II "complete[s] the proof of the ultraviolet stability of four-dimensional pure gauge field theories, as formulated in Theorem 1". | I did not read Theorem 1 itself. FROM MEMORY (not attributed): it is a bound on the partition function / effective action on a finite periodic torus, uniform in the lattice spacing. Clay p.11-12 (read) confirms "uniform in the lattice spacing" and that the work must "be extended to the study of expectations of gauge-invariant functions". Chatterjee p.12 (read): UV stability means subsequential convergence by compactness, and nothing in the infrared. |
| doi:10.1007/BF01229380 | Balaban, UV stability 3D, CMP 102 (1985) | abstract: ABSTRACT ONLY | UV stability for 3D Wilson lattice pure YM | 3D |
| doi:10.1007/BF02097397 | Magnen, Rivasseau, Sénéor, CMP 155 (1993) | abstract: ABSTRACT ONLY | "the basis for a rigorous construction of the Schwinger functions of the pure SU(2) Yang-Mills" in 4D, trivial topological sector, fixed IR cutoff, no UV cutoff, regularized axial gauge. Slavnov identities hold non-perturbatively. | Fixed IR cutoff, so no infinite volume and no mass gap. Gauge invariance is restored only through counterterms. |
| Dimock | — | not searched successfully: NOT CHECKED | — | — |

### R5. Tools
| addr | authors, title, year | locator, how read | exact statement | hypotheses / NOT given |
|---|---|---|---|---|
| arXiv:2204.12737v1 | Shen, Zhu, Zhu 2022 (CMP 2023) | (1.1)-(1.3), Thm 1.2, Rem 1.3, Thm 1.4, Cor 1.6, (4.2), (4.7), (4.8): FULL TEXT | Measure ∝ exp(Nβ Re Σ_p Tr Q_p) dHaar on Z^d, any d>1. Assumption (1.3): SU(N) \|β\| < 1/(16(d−1)); SO(N) \|β\| < 1/(32(d−1)) − 1/(16N(d−1)). K_S = (N+2)/2 − 1 − 8N\|β\|(d−1) for SU(N). Thm 1.2: the infinite-volume invariant measure is unique, and finite-volume periodic measures converge to it (b.c. inessential, Rem 1.3). Thm 1.4: LSI with constant 2/K_S and Poincaré with 1/K_S for cylinder functions. Cor 1.6: Cov(f,g) ≤ c1 e^{−c_N d(Λf,Λg)}(\|\|\|f\|\|\|∞\|\|\|g\|\|\|∞ + ‖f‖₂‖g‖₂) for disjoint supports, c1 depending on \|Λf\|, \|Λg\|. Proof route: Bakry-Émery (4.7) Ric − Hess S ≥ K_S, and Sec. 4.3 uses Poincaré plus Lie-bracket Lemma 4.9. | **Strong coupling only.** My arithmetic (P6): SU(2), d=4 gives β < 1/48, equivalently conventional β_W = 4β < 1/12. Euclidean lattice only: nothing about the continuum, weak coupling, or the OS Hilbert-space gap. c_N is not explicit in the corollary. |
| (same) | — | (4.2), (4.8) | Ric(u,u) = (α(N+2)/4 − 1)\|u\|², α=2 for SU(N) (= N/2), cited from AGZ10 (F.6). \|Hess S(v,v)\| ≤ 8(d−1)N\|β\|\|v\|². | Both constants depend on the normalization S = Nβ Re Tr. |
| doi:10.1214/07-AIHP200 | Grunewald, Otto, Villani, Westdickenberg, AIHP 45 (2009) | Sec. 2.1 (2)-(5), Thm 3 (7), p.306-307: FULL TEXT | X Euclidean, P: X→Y linear with N P Pᵗ = id_Y. μ = e^{−H}dx. Hypotheses: (i) κ = max⟨Hess H u, v⟩ over unit u ∈ Ran NPᵗP and v ∈ Ran(id−NPᵗP) is finite; (ii) the conditional measures μ(dx\|y) satisfy LSI(ρ) for all y; (iii) the marginal μ̄ satisfies LSI(λN). Conclusion: μ satisfies LSI(ρ̂), with ρ̂ = ½[ρ+λ+κ²/ρ − √((ρ+λ+κ²/ρ)² − 4ρλ)] > 0. | **Linear space, Lebesgue reference measure.** It does not apply verbatim to SU(N)^E or to gauge-invariant coarse-graining. |
| doi:10.1016/j.jfa.2006.10.002 | Otto, Reznikoff, JFA 243 (2007) | via Menz arXiv:1309.0862 Thm 1.6: SUMMARY ONLY | Real spins with single-site ψ = z⁴/12 + ψ_b (\|ψ_b''\| ≤ C), symmetric M with M_ii = 0. Exponential decay of M_ij and of cov_{μΛ}(x_i,x_j), uniformly in subvolumes Λ, implies an LSI uniform in system size. | Real-valued unbounded spins only. Requires decay of correlations **uniformly in all sub-volumes** (all b.c.), which is the hard input. |
| Dobrushin-Shlosman | — | not read: FROM MEMORY / NOT CHECKED | — | **Conflict between two sources I did read:** Chatterjee 2006.16229 p.7 says Def 2.3 "can be shown to hold for essentially any lattice gauge theory when β is small enough, using the methods of Dobrushin and Shlosman". SZZ p.6 says a Dobrushin uniqueness argument "has not been carried out in detail for lattice Yang Mills in the literature". |
| arXiv:2006.16229v5 | Chatterjee, "A probabilistic mechanism for quark confinement" (CMP 2021) | (2.1)-(2.3), Def 2.1, Thm 2.2, Def 2.3, Thm 2.4, p.4-8: FULL TEXT | Any compact G, Z^d, β fixed. Thm 2.2: unbroken center symmetry (Def 2.1: in some slab {0..N}×Z^{d−1}, under every b.c., every Gibbs measure is invariant under center transforms), with π irreducible and acting nontrivially on the center, gives \|⟨W_ℓ⟩\| ≤ e^{−V(R)T} with V(R)→∞. Def 2.3 ("strong mass gap"): \|⟨fg⟩−⟨f⟩⟨g⟩\|_{B,δ} ≤ K1 e^{−K2 dist} for every cube B, every b.c. δ, local f,g ∈ [−1,1], with K1, K2 depending only on G, β, d. Thm 2.4: Def 2.3 implies unbroken center symmetry and the area law (2.3) for every Gibbs measure. | Thm 2.2 alone is **not** the area law. Needs a nontrivial center (fails for SO(3)). Def 2.3 is much stronger than decay in one infinite-volume state. p.7: "not clear whether this belief [mass gap conjecture] includes the strong version". |
| arXiv:1803.01950v1 | Chatterjee, "Yang-Mills for probabilists" 2018 | Problems 4.1, 5.1, 5.2, p.8-10: FULL TEXT | 4.1: area law \|⟨W_{R,T}⟩\| ≤ C(β)e^{−c(β)RT} for every compact non-Abelian G ⊆ U(N), d=4, any infinite-volume limit, every β. 5.1: plaquette-plaquette correlation length ξ(β) ∈ (0,∞) for every β>0, and ξ(β)→∞ as β→∞. 5.2: ε(β)→0, c(β)→∞, d≠0 with log⟨W_{R/ε,T/ε}⟩ = −c(R+T) − dRT + o(1). | p.12: no continuum limit in d>2 with nontrivial Wilson loops is known. I did not search for a later survey. |

### R6. Obstructions
| addr | authors, title, year | locator, how read | statement | NOT given |
|---|---|---|---|---|
| doi:10.1007/BF01609471 | Singer, "Some remarks on the Gribov ambiguity", CMP 60 (1978) 7 | abstract: ABSTRACT ONLY | For bundles over S⁴ with compact non-Abelian group, "no continuous choice of exactly one connection on each orbit can be made". "No gauge fixing is possible." | A statement about smooth connections on S⁴, not about lattice gauge fixing |
| large-field problem | Balaban LF I abstract | ABSTRACT ONLY | Large-field regions are "the main obstacle to prove the ultraviolet stability" | — |
| analyticity for all β | OS78 abstract; one web search | ABSTRACT ONLY / search | Analyticity is proved at strong coupling only. Nothing found for all β in SU(N), d=4. | Absence of evidence from one search is not a theorem |

## 2. Hypotheses each statement uses (where stated)
- Clay (Sec. 4, p.6): G compact simple; R⁴; Wightman/OS axioms; non-trivial; asymptotic-freedom short-distance behavior; m < ∞.
- OS78 (abstract): strong coupling, Wilson-type lattice action. The rest was not read.
- SZZ (Assumption 1.1, eq. (1.2)): S = Nβ Re Tr Q_p; \|β\| < 1/(16(d−1)) for SU(N); d>1; cylinder test functions; periodic b.c. inessential (Rem 1.3).
- Adhikari-Cao (Sec. 1.3): finite G, unitary representation ρ with character χ, d=4, finite box with equal sides, β ≥ (114+4log\|G\|)/Δ_G.
- Chatterjee 2021 (Sec. 2.1, Def 2.1, 2.3): compact G, Z^d, Gibbs measures of the specification, π acting nontrivially on the center.
- GOVW Thm 3 (Sec. 2.1): Euclidean X, linear P with NPPᵗ=id, κ<∞, conditional LSI(ρ), marginal LSI(λN).
- Göpfert-Mack, Guth (abstracts): Villain action.
- MRS (abstract): SU(2), trivial topological sector, fixed IR cutoff, axial gauge.

## 3. Failed predicates
- check_rows.py: P1-P6 all MET (6 met, 0 failed, 2 measured only).
- Register check `child-tool-rerun` (K3): exit 1, expected 0. **My own error.** I passed `results2.json` as argv[1], which the child's script opens with mode "x" as its output, so it raised FileExistsError. This is not a defect of the child. The correct rerun `child-tool-rerun2` (K4) exited 0: "rows=7 complete=7 fails=0".
- Brief-premise defects: see R1 rows in the verdict table.

## 4. What I did not check
Full texts of OS78, Lüscher, Balaban (including the statement of Theorem 1, its volume and its coupling trajectory), MRS, Guth, Fröhlich-Spencer, Göpfert-Mack, Borgs, Singer, Seiler LNP 159, Otto-Reznikoff original, Dobrushin-Shlosman, Dimock, Lévy, Sengupta. Also: any rigorous 2D mass gap, SU(2) in d=5, and a later Chatterjee survey. The SZZ arithmetic is a recomputation of two constants; I did not re-derive the proofs.

## 5. Delegated questions and outcomes
- Child (child/, sonnet, headless, register check K1 exit 0 in 92 s). Question: R3 alone. Control "in which dimension did Gopfert-Mack prove confinement": answer `three`, **correct** (graded first). It returned an honest table: everything ABSTRACT/SUMMARY/FROM MEMORY. Guth via INSPIRE; Adhikari-Cao Thm 1.1 via an agent's HTML read; 2D/5D from memory. I reread: Adhikari-Cao Thm 1.1 confirmed against the full text (threshold, bound and constants match). Göpfert-Mack, Guth and FS confirmed against the INSPIRE abstracts, which I extended with the Villain action, g² < 0.168 and the m_D formula. I reran its checker (K4) and its register verify (K5), both exit 0. The child's "pass" checks only table completeness, not truth (it says so itself).
- Grandchild (child/grandchild/). Question: the Adhikari-Cao abstract (β range, observables). Control "year prefix of 2202.10375": `2022`, correct. It reported "no explicit numeric beta range on the abs page". That is consistent with the abstract I read. The threshold appears only in Thm 1.1, so this is a limit of reading the abstract, not an error.
- web-fetch agent (mine): abstracts from Springer/Euclid. All 12 NOT READ (login wall). It filled nothing from memory.

## 6. Ten facts the attempt must not get wrong
1. Clay asks for **every** compact simple G on R⁴. SU(2) alone is a partial result (p.6).
2. The gap is "no spectrum of H in (0,Δ)", and m < ∞ is also required, i.e. the theory must not be empty or trivial (p.6).
3. Existence includes Wightman/OS axioms, local operators for Tr F F, and short-distance agreement with asymptotic freedom (stress tensor, OPE) (p.6).
4. Compactness or weak existence alone is explicitly excluded (fn. 2, p.12).
5. Balaban proved UV stability (uniform bounds on a torus), not convergence of correlation functions and nothing in the infrared (Clay p.11-12; Chatterjee 2018 p.12).
6. SZZ's mass gap is Euclidean lattice decay of covariances for \|β\| < 1/(16(d−1)) (SU(2), d=4: β_W < 1/12). It is strong coupling only and says nothing about the continuum.
7. Bakry-Émery for SU(N): Ric = N/2 (α=2), \|Hess S\| ≤ 8(d−1)N\|β\| with S = Nβ Re Tr. Normalizations matter.
8. GOVW's two-scale criterion is proved on linear spaces with linear coarse-graining. It is not a theorem on SU(N)^E.
9. Chatterjee: area law needs the **all-b.c., all-cubes** decay of Def 2.3 (Thm 2.4). Thm 2.2 gives only e^{−V(R)T}. A nontrivial center is required.
10. U(1) in d=4 does NOT confine at weak coupling (Guth, FS; Villain action). Gap and confinement are dimension- and group-specific. No rigorous SU(2) all-β result exists (Tomboulis's claim is disputed by Ito-Seiler).

## 7. Commands to rerun (from /home/user/z4-workers/a1-rig)
```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"            # control
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task,WebFetch,WebSearch' < PROMPT.txt"
$P check --ws pcp --name check-rows-1 --expect-exit 0 -- python3 check_rows.py rows.json result_check_rows_1.txt   # new output name on rerun (mode x)
$P check --ws pcp --name child-tool-rerun2 --cwd child --expect-exit 0 -- python3 tools/check_table.py /home/user/z4-workers/a1-rig/result_child_rerun2.txt
$P check --ws pcp --name child-verify-rerun --cwd child --expect-exit 0 -- python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
# fetches (to /tmp/a1-rig-dl): curl -sL -o clay.pdf https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf ;
#  arxiv.org/pdf/{2204.12737,2006.16229,1803.01950,2202.10375,1309.0862v1}; numdam.org/item/10.1214/07-AIHP200.pdf ;
#  python3 -I /tmp/a1-rig-dl/insp.py '<INSPIRE query>'  (inspirehep.net/api/literature, queries listed in the fetch log)
```
PCP verify last lines:
- `$P verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

## 8. Fetch log
| source | result |
|---|---|
| claymath.org yangmills.pdf | 200, full text |
| arxiv.org/pdf/2204.12737, 2006.16229, 1803.01950, 2202.10375, 1309.0862v1 | 200, full text |
| numdam.org GOVW pdf | 200, full text |
| projecteuclid.org (CMP pdfs and article pages) | blocked (Incapsula stub, ~1 kB) |
| link.springer.com / doi.org for BF01215223, BF01257412 | blocked (login redirect), curl and web-fetch agent |
| export.arxiv.org API (Otto-Reznikoff, GOVW) | 0 hits |
| inspirehep.net API | abstracts: CMP 109:249, 122:175, 122:355, 102:255, 54:283, 155:325, 83:411, 82:545, 96:251, 60:7, 123:575; Ann. Phys. 110:440; PRD 21:2291; arXiv:0707.2179, 0711.4930, 0803.3019; LNP 159 (no abstract); math/0101239 (no abstract) |
| WebSearch (4 queries) | bibliographic pointers only. Nothing was attributed from search snippets except the existence of Tomboulis 2007 and the critique, which I then read via INSPIRE |
