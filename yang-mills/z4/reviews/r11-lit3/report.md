# Report r11-lit3: literature reader, primary sources (six arXiv identifiers)

Worker of Director Z4, 23 November 2026. Control: `control.txt` = 0.272341. Page numbers are PDF page indices. In all five files read, they match the printed page numbers. Extracted text lives only in `ref/text/` and `child/ref/text/`. The reader is a language model of the director's family, so a READ row means "statement located", not refereed interpretation.

## 0. Fetched files (hypothesis first)

| id | bytes | pages | page 1: title / authors | matches expected? |
|---|---|---|---|---|
| 2204.12737 | 525 950 | 43 | A stochastic analysis approach to lattice Yang–Mills at strong coupling / H. Shen, R. Zhu, X. Zhu (v1, 27 Apr 2022) | yes |
| 2006.16229 | 335 742 | 35 | A probabilistic mechanism for quark confinement / S. Chatterjee (v5, 26 Mar 2021) | yes |
| 2111.12813 | 733 454 | 73 | A state space for 3D Euclidean Yang–Mills theories / S. Cao, S. Chatterjee (v4, 20 Nov 2023) | yes |
| 2201.03487 | 1 693 721 | 159 | Stochastic quantisation of Yang–Mills–Higgs in 3D / A. Chandra, I. Chevyrev, M. Hairer, H. Shen (v2, 15 Apr 2024) | yes |
| 2202.10375 | 523 219 | 35 | Correlation decay for finite lattice gauge theories at weak coupling / A. Adhikari, S. Cao (v3, 17 Mar 2024, Ann. Probab. submission) | yes |
| 1808.09896 | 308 537 | 5 | "Review Helpfulness Prediction with Embedding-Gated CNN" / C. Chen, M. Qiu, Y. Yang, J. Zhou, J. Huang, X. Li, F. S. Bao | **NO: MISMATCH**. This is an NLP paper, not Chatterjee's Ising Wilson-loop paper. The director's identifier is wrong. I did not fetch a substitute (not permitted). |

## 1. Verdict table

| item | verdict | evidence |
|---|---|---|
| SZZ 2204.12737, L1 | READ | Assumption 1.1/(1.3) p.4; Thm 1.2 p.5; Thm 1.4 p.6; Cor 1.5, Cor 1.6 ("Mass gap") p.7 |
| SZZ, L2 | READ | §1.3 p.8–9: LSI at vanishing spacing open; convergence to the CCHS dynamics in 2D/3D open |
| Chatterjee 2006.16229, L1 | READ | Thm 2.2 p.6, Def 2.3 and Thm 2.4 p.7 |
| Chatterjee 2006.16229, L2 | READ | p.2: gap at all couplings open (4D SU(3)), area law at weak coupling open above 2D; p.8 finite groups |
| Cao–Chatterjee 2111.12813, L1–L2 (delegated) | READ | Thm 1.6 p.7, Thm 1.12 p.11, Thm 1.16 p.13, Conj 1.8 / 1.13, Remark 1.15 p.11–12 (4D). I rechecked Thm 1.6 and Remark 1.15 myself |
| CCHS 2201.03487, L1–L2 (delegated) | READ | Thm 1.2 p.11, Thm 1.7 p.12–13, Thm 1.9 p.14, Remark 2.1 p.14–15 (d ≥ 4). I rechecked Thm 1.9 and Remark 2.1 myself |
| Adhikari–Cao 2202.10375, L1–L2 | READ | Thm 1.1 p.5; p.2 (4D SU(3) open; small β routine); p.4 (d = 4 only) |
| Chatterjee Ising paper (as 1808.09896) | MISMATCH | page 1 is an unrelated NLP paper |
| L3 lane comparison | READ (for 5 papers) | §3 below |
| L4 strong-coupling range vs B4 | READ, but convention-dependent | `results/compare.json`: covered if B4's weight is exp((β/2)Re Tr U_p), not covered if it is exp(β Re Tr U_p) |
| L5 finite groups vs Z4 | READ (AC only) | AC Thm 1.1 p.5; the Ising paper is missing |

Program predicates: `prog/extract.py`: 22 met, 2 failed, 12 measured only (bytes and pages per file). `prog/compare.py`: 6 met, 0 failed, 6 measured only. Total: **28 met, 2 failed, 18 measured only**.

## 2. L1/L2 per paper (own words) and hypotheses used

**Shen–Zhu–Zhu (2204.12737).**
- *Hypotheses:*
  - G = SU(N) or SO(N), on the lattice ℤ^d for any d ≥ 2, at unit spacing.
  - Weight exp(Nβ Σ_p Re Tr Q_p) ('t Hooft scaling), eq. (1.2), p.4.
  - Strong coupling, Assumption 1.1/(1.3), p.4: |β| < 1/(16(d−1)) for SU(N), and |β| < 1/(32(d−1)) − 1/(16N(d−1)) for SO(N). The bounds are uniform in N.
- *Proved:*
  - Thm 1.2 (p.5): the Langevin dynamics has a unique invariant measure. The periodic finite-volume measures converge to it as L → ∞, and it is exponentially ergodic in a Wasserstein distance.
  - Thm 1.4 (p.6): log-Sobolev and Poincaré inequalities with constant K_S.
  - Cor 1.5 (p.7): large-N factorization of Wilson loops.
  - Cor 1.6 (p.7, titled "Mass gap"): exponential decay of covariances of smooth cylinder functions with disjoint supports in infinite volume. The rate c_N depends on K_S, N and d; no number is given in the statement.
- *Open (pp.8–9):* whether log-Sobolev inequalities survive vanishing spacing, and whether the lattice dynamics converge to the 2D/3D continuum dynamics. They make no 4D continuum claim.
- On p.2 they credit Osterwalder–Seiler with a convergent strong-coupling cluster expansion that is uniform in volume, implying a mass gap (exponential clustering). That is a secondary attribution; OS78 was not opened.
- Quotation: "the inﬁnite volume measure has a strictly positive mass gap" (p.1).

**Chatterjee (2006.16229).**
- *Hypotheses:* G a closed connected subgroup of U(n); ℤ^d, d ≥ 2; any Gibbs measure for weight exp(β Σ Re Tr ω_p) (eq. 2.1, p.4); β fixed.
- *Proved:*
  - Thm 2.2 (p.6): unbroken center symmetry (Def 2.1: on a slab, under every boundary condition) implies |⟨W_ℓ⟩| ≤ e^{−V(R)T} with V(R) → ∞. This holds for representations acting nontrivially on the center.
  - Thm 2.4 (p.7): exponential decay of correlations under arbitrary boundary conditions (Def 2.3: on cubes, with constants depending only on G, β, d) implies unbroken center symmetry, and hence the area law.
  - The paper gives no explicit β range. On p.7 it says Def 2.3 holds for β small enough "using the methods of Dobrushin and Shlosman".
- *Open (p.2):*
  - Mass gap at all couplings ("All such questions remain open", p.2), with 4D SU(3) named as the key case.
  - Area law at weak coupling above dimension two.
  - On p.7 it is unclear whether the conjectured 4D gap includes the strong, every-boundary-condition form.
  - On p.8: finite-group theories are believed gapped but non-confining at large β. Their decay is of a different, boundary-condition-specific kind, and some have several Gibbs measures.

**Cao–Chatterjee (2111.12813)**, from the sub-agent, with two statements rechecked by me.
- *Hypotheses:* continuum 3D unit torus; G a product of tori, U(n), SU(n), O(n), SO(2n+1); no coupling regime.
- *Proved:*
  - Thm 1.6 (p.7): tightness criterion. If the Yang–Mills action of the heat-flowed field is tight at every flow time t > 0, there is a subsequential weak limit on the space X of distributional gauge orbits.
  - Thm 1.12 (p.11): conditional on GFF-like hypotheses, that criterion holds.
  - Thm 1.16 (p.13): the "gauge invariant free field" exists as a limit.
- *Open:* Conj 1.8 and 1.13, i.e. that actual Yang–Mills approximations satisfy the hypotheses. 4D: Remark 1.15 (p.11–12) says the method fails because 4D is critical.
- No gap, decay or area law.
- Quotation: "the laws of XN converge weakly to the law of X" (p.13).

**CCHS (2201.03487)**, from the sub-agent, with two statements rechecked by me.
- *Hypotheses:* continuum T³; any compact G, with a Higgs field or pure Yang–Mills.
- *Proved:*
  - Thm 1.2 (p.11): a state space S and an orbit space O.
  - Thm 1.7 (p.12–13): local-in-time solutions of the renormalised SPDE, independent of the mollifier.
  - Thm 1.9 (p.14): a unique counterterm gives gauge covariance, and there is a unique Markov process on O.
- *Open (p.3, p.7–8):*
  - The 3D Yang–Mills measure, even in finite volume.
  - An invariant measure for the process, and global existence.
  - Extension to ℝ³.
- 4D: Remark 2.1 (p.14–15) says the state space does not support the GFF in d ≥ 4, and the later results "break down badly".
- No gap or decay.
- Quotation: "There exists a unique Markov process X on O such that" (p.14).

**Adhikari–Cao (2202.10375).**
- *Hypotheses:*
  - G finite, possibly non-abelian.
  - d = 4 only, on a finite cubic box Λ. The constants do not depend on Λ.
  - Weight exp(−β Σ_p Re(χ(1) − χ(σ_p))), eqs. (1.2)–(1.3), p.5.
- *Proved, Thm 1.1 (p.5):*
  - Hypothesis: β ≥ (114 + 4 log|G|)/Δ_G, where Δ_G = min over g ≠ 1 of Re(χ(1) − χ(g)).
  - Conclusion: |Cov| ≤ 4(4·1024|G|²)^{|B₁|+|B₂|} ‖f₁‖‖f₂‖ e^{−(β/2)Δ_G(L−1)}. This holds for conjugacy-invariant functions of Wilson loops in rectangles at ℓ∞ distance L.
- *Stated (p.2):*
  - The authors read Thm 1.1 as a mass gap for finite groups at large β.
  - 4D SU(3) decay is a central open question.
  - Small β is called "routine" by high-temperature expansion.
- On p.4 they expect general d to work but do not prove it.
- Quotation: "exponential decay of correlations for a wide class of gauge invariant functions" (p.1).

## 3. L3: bearing on the program's lanes

| lane | SZZ | Chatterjee conf. | Cao–Chatterjee | CCHS | Adhikari–Cao |
|---|---|---|---|---|---|
| **B4** volume-uniform strong-coupling gap | **Overlapping, partly stronger.** Infinite-volume uniqueness and exponential decay for SU(N), any d, \|β\| < 1/(16(d−1)) (Cor 1.6 p.7). It covers all N uniformly; B4 explicitly covers SU(2) only. **Weaker in one respect:** SZZ's rate c_N is not given as a number, while B4 has the explicit 4 log 3/(13κ). **Different object:** Euclidean clustering on the isotropic lattice, whereas B4 has a transfer-operator gap with anisotropic β_t = κ/a, β_s = aλ and a joint time-step limit. SZZ has no anisotropic or Hamiltonian statement. | Weaker: says a gap at small β is "not hard" (p.2, by Dobrushin–Shlosman), with no number | nothing | nothing | different (finite groups, large β) |
| **A4** observable normalization, variance floors | Different: upper bounds Var(W/N) ≤ 4n(n−3)/(K_S N) (Cor 1.5) and susceptibility bounds (Cors 4.7, 4.8, not opened). These are upper bounds; A4 proves floors. | nothing | nothing | nothing | nothing |
| **C4** central quotients, Gaussian limits | nothing | **Related, different:** center symmetry and the center action on representations drive Thms 2.2 and 2.4. C4's pushforward to SO(3) is not treated. On p.7 the paper says trivial-center groups (SO(3)) are believed non-confining. | **Related:** the gauge-invariant free field (Thm 1.16) is a Gaussian-type limit object in 3D on the orbit space. Different dimension, and not the tangent law of local curvature. | Related: a 3D state space for distributional connections; no Gaussian limit of observables | nothing |
| **D4** spectral criteria | Different: Poincaré constant K_S gives an L² spectral gap of the Langevin generator (Thm 1.4 remark p.5). That is a dynamics gap, not a transfer-matrix or Hamiltonian gap. | Different: decay ⇒ center symmetry ⇒ area law. A criterion of another kind. | nothing | nothing | nothing |
| **G4** reflection positivity | nothing (RP not used) | nothing | nothing | nothing | nothing |
| **Z4** trajectory, fixed-size observables | nothing on refinement | nothing | **Stronger relative of Z4's flowed-observable plan:** regularized Wilson loops = Wilson loops of the heat-flowed field at t > 0 (pp.6–7), as the natural fixed-size observables. Only 3D, conditional; 4D excluded (Rem 1.15). | Same direction (gauge-invariant observables via flow), 3D only, 4D excluded (Rem 2.1) | Finite-group 4D gap at large β; see L5 |

## 4. L4: the largest strong-coupling range read, and B4's regime

- Among the papers read, the only explicit range for SU(N) lattice Yang–Mills is SZZ's |β| < 1/(16(d−1)) in their normalization Nβ Re Tr. In d = 4 that is β_SZZ < 1/48 = 0.020833. For SU(2) the coefficient of Re Tr U_p must then be below 2/48 = 1/24 = 0.041667.
- Chatterjee and Adhikari–Cao give no number for small β; they cite Dobrushin–Shlosman, Seiler, and Osterwalder–Seiler, which I did not open.
- B4's Wilson regime, tanh β ≤ 1/20, means β ≤ atanh(1/20) = 0.050042 (`results/compare.json`). My inputs do not state B4's normalization, so two cases:
  - weight exp(β Re Tr U_p) (Chatterjee's convention): B4's range is **1.201 ×** SZZ's, so it reaches about 20% beyond the explicit SZZ range;
  - weight exp((β/2) Re Tr U_p) (physics β = 4/g²): B4's range is **0.600 ×** SZZ's and lies inside it.
- **B4 must state its normalization.** Under the second convention, B4's Euclidean decay statement at tanh β ≤ 1/20 is contained in SZZ's infinite-volume decay, though not with an explicit rate.
- B4's Hamiltonian regime κλ ≤ 1/384 has no counterpart in any paper read. None treats anisotropic or Hamiltonian couplings, so I give no comparison.
- Every result read on the gap is at fixed lattice spacing and small β. None moves requirement (a) or (e) of the disposition.

## 5. L5: finite groups at weak coupling

- **Adhikari–Cao.** For any finite G in 4D and β ≥ (114 + 4 log|G|)/Δ_G (Z₂ with the sign character: β ≥ 58.39; Z₃: β ≥ 78.93), correlations of gauge-invariant Wilson-loop functionals decay at rate (β/2)Δ_G per lattice unit. That is at least 57 per lattice unit at threshold, and it **grows** with β.
- **Relation to Z4's controls.** Z4's 2D statement, "a finite group has a gap on its own trajectory", now has a published 4D lattice analogue at large β with an explicit rate. Since the rate grows linearly in β, on any trajectory with β → ∞ and spacing a → 0 the physical rate is at least (β/2)Δ_G/a → ∞. The correlation length in lattice units goes to 0, not ∞. This is the "collapse" Z4 reports for finite groups (with no continuum limit), not a continuum gap.
- **Consequence for Z4's withdrawn "proves too much" argument.** Any argument that would yield a continuum mass gap from a lattice-unit exponential-decay bound at large β alone would also apply to finite groups, for which AC prove exactly such a bound. This supports withdrawing it. I did not see the text of that argument, so this is a reading of its label only.
- Chatterjee 2006.16229 (p.8) adds that finite-group theories are believed gapped yet non-confining at large β, with multiple Gibbs measures in some cases. So "exponential decay" in AC's sense, for these observables and these boundary conditions, is weaker than Def 2.3's every-boundary-condition decay.
- The Ising paper was **not available** (MISMATCH), so nothing from it is used.

## 6. Failed predicates

- extract.py P3, P4 on 1808.09896: the expected author (Chatterjee) and keywords ("Wilson loops", "Ising") are absent from page 1. The defect is in the **target** (wrong identifier in the director's brief), not in my expectation.
- Register check K1 (extract): exit 1 against the expected 0. The cause was a syntax error I introduced by a shell edit before any output; it wrote no result file. This was my defect, fixed and rerun as K2.
- No predicate of compare.py failed.

## 7. Not checked

- Chatterjee's Ising Wilson-loop paper: its real identifier is unknown and it was not fetched.
- Osterwalder–Seiler, Seiler's monograph, Dobrushin–Shlosman, Bałaban: cited only.
- SZZ §4.3 and §5 proofs, and whether its rate c_N can be made numeric (pp.25–30 not read in full).
- AC proofs; whether "log" in Thm 1.1 is natural. I assumed natural (INFERRED); Z₂ with log₂ would give 59.0.
- B4's Wilson normalization, which decides §4.
- The child's statements other than the two I rechecked. Its other theorem numbers and pages (Thm 1.2, 1.7, 1.12, 1.16 of the respective papers; Conj 1.8, 1.13) are its claims, though the Thm 1.16 quotation was located by me on p.13.
- Novelty of any lane result against literature not in this list.

## 8. Delegated question and outcome

- **Question.** L1 (main theorems with hypotheses, theorem and page numbers) and L2 (what is open, what is said about 4D) for 2111.12813 and 2201.03487. The control was −ln tanh 1 with known answer 0.272341. The sub-agent worked in `child/` with its own register `child/pcp`.
- **Returned.** `child/answer.md` (summarized in §2) and control 0.272341 (correct).
- **Checked by me against my own extraction:** (a) Cao–Chatterjee Thm 1.6 p.7 and Remark 1.15 p.11–12; (b) CCHS Thm 1.9 p.14 and Remark 2.1 p.14–15. Both were found as stated, and both of its quotations were located verbatim.
- I reran `verify` on `child/pcp`: PASS.

## 9. Rerun

```
cd C:/Users/donke/z4-workers/r11-lit3
export PYTHONUTF8=1
for id in 2204.12737 2006.16229 2111.12813 2201.03487 2202.10375 1808.09896; do curl -sL -o ref/$id.pdf https://arxiv.org/pdf/$id; done
# result files are never overwritten: move results/manifest.json, results/compare.json, ref/text/heads.txt aside first
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name extract2 --expect-exit 0 -- python -I prog/extract.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name compare --expect-exit 0 -- python -I prog/compare.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
(cd child && python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp)
```

Last line of `verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
