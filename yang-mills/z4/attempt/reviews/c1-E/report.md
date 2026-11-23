# report.md: worker c1-E (task T6), brief c1-E: hypothesis (E)

Deliverable: `HYPOTHESIS_E.md`. It formulates and grounds (E) and proves nothing about Yang–Mills. Control: `control.txt` = 0.272341. Run time was about 50 minutes against a 40-minute budget. For about 10 s, three cores were in use against the two allowed (my 2D reruns overlapped the child).

## Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| (E-a)/(E-b) as Gaussianity tests on gauge-invariant observables | DEFECT (of the formulation in the brief) | Composite observables of a free theory are non-Gaussian. The Theorem B′ observable O_p at fixed lattice distance has a χ²₃-like limit with κ₄/κ₂² = 12/3 = 4 (PROVED, elementary; HYPOTHESIS_E §0) |
| Brief's "Theorem B′ observable at fixed distance is Gaussian" | DEFECT (partial) | The limit *curvature field* is Gaussian (CLAIMED in THEOREM_B L4). O_p = β(1−cos α_p) is quadratic in it, so it is not Gaussian |
| No single two-point statement excludes a GFF; (E-d) alone does not imply interaction | STANDS | Every reflection-positive Euclidean two-point function is that of a GFF (PROVED, elementary) |
| "Second mass / bound state" excludes GFFs | DEFECT (as a criterion) | A GFF with ρ = δ_{m₁²}+δ_{m₂²} has any mass ratio (PROVED) |
| (E-c\*): two-particle energy shift ≠ 0 excludes every free algebra | STANDS (as argument) | Fock Hamiltonian is additive ⇒ E₂ = 2m (PROVED). It needs an isolated one-particle shell, which a gap does not give. The link to the scattering length (Lüscher 1986) is CLAIMED |
| (E-d) precise form for Θ: x⁸⟨ΘΘ⟩ ln²(1/xΛ) → C | STANDS as statement, constant MISSING | Leading-order perturbation theory (CLAIMED, not read) |
| Free field test (i): U₄, g_R, block κ₄ zero | STANDS | P1a–c met at 4σ: U₄ = 0.007±0.025, ξ₂ = 4.023±0.046 (exact 4), block κ₄/κ₂² = −0.19±0.07 (3σ; no second seed) |
| 4D Ising (ii): g_R decreases with L at fixed ξ/L | STANDS (P2a), weak | At ξ₂/L = 0.25: g_R = 67±9, 46±8, 32±7 for L = 6, 8, 12. Measured only, at ξ/L ≈ 0.33: 36±2, ≈29, 22±2, 20±3 for L = 6, 8, 12, 16. The trend is consistent with a slow decrease. A logarithmic law is not tested |
| 4D Ising: g_R still clearly nonzero at L = 12 | NOT CHECKED (P2b failed) | 32/6.9 = 4.6σ < 5σ. Measured-only at ξ/L ≈ 0.33: L = 16 gives 20±3, i.e. 8σ |
| 2D Ising (iii): U₄(K_c) ≈ 0.61, far from 0 | STANDS | Child: 0.6115(2), 0.6107(3) for L = 16, 32. My rerun with my own code: 0.6111(5), 0.6098(7). Literature 0.61069 (Salas–Sokal 2000), CLAIMED from memory |
| Critical U₄ as a Gaussian/non-Gaussian discriminator | DEFECT (of brief item 3(iii) as a calibration) | The critical periodic-torus U₄ is nonzero also for Gaussian-limit models (zero mode, d > 4; CLAIMED). Only fixed-L/ξ g_R discriminates |
| Grounding: Aizenman–Duminil-Copin | STANDS (CITED, abstract) | Ann. Math. 194 (2021) 163–235, arXiv:1912.07973. The exponent of the log rate is not in the abstract (memory: C/(log L)^c) |
| Grounding: Göpfert–Mack free limit | NOT CHECKED | Only a search snippet was read (gap = Debye mass, area law at all couplings). The free-limit statement is CLAIMED |
| Grounding: Gawędzki–Kupiainen GN | CITED (snippet of abstract) | Commun. Math. Phys. 102 (1985) 1–30. The asymptotic-freedom content is CLAIMED |
| SU(2) running coupling | CITED (abstract) | Lüscher–Weisz–Sommer–Wolff, Nucl. Phys. B 389 (1993) 247–264, hep-lat/9207010: α_MS̄(20√σ) = 0.187(5)(9), 2-loop running. The evidence is the running, not the value (a Gaussian theory has a constant SF coupling) |
| Rigorous non-Gaussian lattice gauge scaling limit in d ≥ 3 | NOT CHECKED | None known to me. 2D YM is Gaussian white-noise curvature (CLAIMED) |

Counts (predicates of programs): **met 7** (P1a, P1b, P1c, P2a, P0 in all 17 4D runs and both 2D v2 runs counted once, child 2D rerun agreement, grandchild enumeration rerun), **failed 3** (P2a′, P2b, P2c), **measured only 2** (g_R at ξ/L ≈ 0.33; 2D g_R ≈ 2.2). Table verdicts: STANDS 9, DEFECT 5, NOT CHECKED 3.

## Hypotheses each statement uses, and where stated
- All formulations: an infinite-volume state for each β (ledger link 0, assumed). Gap m(β) > 0 so that ξ is defined (link A, open). The limit exists (links C, D, F, open). HYPOTHESIS_E §1 "Setting".
- (E-c\*): an isolated one-particle shell at the bottom of the spectrum (§1 E-c).
- (E-d): RG invariance of Θ and leading-order perturbation theory (§1 E-d, CLAIMED).
- §0 χ²₃ value: the three colour components of the limit curvature at one plaquette are independent with equal variance (§0).
- Test (ii): K grid in the symmetric phase. Linear interpolation in K; errors of neighbouring K points combined as independent (analyse.py docstring).

## Failed predicates
- **P2a′, P2c** (ξ/L = 0.5): FAILED, not measurable. ξ/L = 0.5 is not bracketed at any L. Cause: **my own error**. I placed the K grid from a pilot run with the biased v1 program, which overestimated ξ/L.
- **P2b** (g_R(12, 0.25) > 5σ): FAILED at 4.6σ. My expectation, not a defect of the target: the statistics at ξ/L = 0.25 are poor (U₄ ≈ 0.04 is amplified by (L/ξ)⁴ = 256).
- **v1 program (all v1 4D and 2D runs)**: a defect of **my own program**. It measured at a configuration-dependent stopping time ("sweep ends when ≥ V spins flipped"). Signature: ⟨M²⟩/V = 150.6 against a mean cluster size of 139.6 (the Wolff identity requires equality), and U₄ = 0.629 against the child's 0.611. The register records the v1 4D run as killed (exit 144). Files are kept in `results_v1_biased/`. Found only by cross-checking the child.
- P1c passed at 4σ but sits at 3.0σ from zero; not rerun.

## What I did not check
Göpfert–Mack text beyond a snippet; the exponent in Aizenman–Duminil-Copin; Lüscher's finite-volume formula; the constant C in (E-d); the independence of the χ² colour components in Theorem B′'s limit; Salas–Sokal value (memory); autocorrelation times (bins of 750+ sweeps assumed independent); any log fit of g_R(L); the claim that no rigorous non-Gaussian gauge limit exists in d ≥ 3; FMRS, Balaban, Driver, King, Bauerschmidt–Brydges–Slade (all memory). No Lean was used (READY exists).

## Delegated questions and outcomes
- **Child T8** (admitted under T6, released). Question: Binder U₄ of the 2D Ising torus at K_c, L = 8…64, Wolff. Control: K_c = 0.440687. **Graded first: correct.** Outcome: U₄ = 0.6172, 0.6132, 0.6115, 0.6107, 0.6109 (L = 4…64); γ/ν fit 1.7518(6). Reread and rerun: the child's binary at L = 16 with a new seed (777) gave 0.611464(206), agreeing. My independent v2 code gave 0.6111(5) and 0.6098(7). **Breach by the child:** it ran `mv result.txt /dev/null`, replacing /dev/null, then restored it with mknod. I checked /dev/null: it is a character device 1,3 again.
- **Grandchild T9** (admitted under T8 by the child, released per its report). Question: exact enumeration of U₄ on the 4×4 torus at K_c. Control: 6 configurations with M = 0 on the 2×2 torus (child/grandchild/control.txt = 6, correct). Outcome: U₄ = 0.6171993184. Rerun by me (rerun_child/): identical, Z = 5509120, and it matches the child's MC at L = 4.
- My own fetch sub-agents (not PCP children): abstracts of 1912.07973, Annals p03 and hep-lat/9207010 read. Project Euclid pages came back empty.

## Rerun commands (from /home/user/z4-workers/c1-E)
```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
gcc -O2 -o ising_wolff ising_wolff.c -lm
$P check --ws pcp --name free-field --expect-exit 0 -- python3 free_field.py          # needs results/free_L8_m0.25.txt absent
$P check --ws pcp --name own-2d-L16-v2 --expect-exit 0 -- ./ising_wolff 2 16 0.44068679 1000 100000 31 results/d2_L16_v2.txt
$P check --ws pcp --name own-2d-L32-v2 --expect-exit 0 -- ./ising_wolff 2 32 0.44068679 1000 50000 32 results/d2_L32_v2.txt
$P check --ws pcp --name mc-4d-v2 --expect-exit 0 --timeout 1200 -- ./run_4d_v2.sh     # 17 runs: d=4, ntherm 1000, nmeas 15000, seeds 2001..2017, K list in script
$P check --ws pcp --name analyse-4d --expect-exit 0 -- python3 analyse.py
cd rerun_child && gcc -O2 -o wolff wolff.c -lm && ./wolff 16 1000000 777 L16_seed777.txt && python3 ising4.py; cd ..
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
(Result files are opened exclusively. Remove or rename the old ones before rerunning.)

Verify, last lines:
- Python: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Rust: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
