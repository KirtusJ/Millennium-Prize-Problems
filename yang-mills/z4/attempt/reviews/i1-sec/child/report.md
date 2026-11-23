# Fidelity check of target/sec_smallbox.tex (task T105)

**Control:** -ln(tanh(1/2)) = 0.771937 (control.txt). Grandchild control -ln tanh 3 = 0.004958 (reread, correct).

Summary: every number in the section and table is FAITHFUL to the inputs. No number is WRONG. The problems are
(a) one OVERSTATED attribution, (b) provenance wording, (c) UNSUPPORTED path/cite items, (d) wrong trace comments for numerics3.md.

## Verdict table
| # | item | verdict | input file:line | evidence |
|---|---|---|---|---|
| 1 | "Every result proved in this paper bounds the gap from above" | FAITHFUL | A3_NOTES:65 | "Everything proved so far bounds the gap from above" |
| 2 | Intro "It was proved by a session of ... OpenAI Codex" | OVERSTATED | A3_NOTES:105,114; A4_M1:5 | inputs say "written proof", "submitted for independent review", "not read by anyone but its author"; section's own Status line is correct, the intro word "proved" is stronger. "Codex" rests on the sessions' "own statement" (A3_NOTES:45), not stated as such |
| 3 | Setting: Wilson increment, K1=1, V=2βΣ\|u_i×u_j\|², T=e^{-V/2}Ke^{-V/2}, k=2,3 | FAITHFUL | A4_M0:11; A4_M1:5,18 | same formulas |
| 4 | Unnormalised kernel shifts -log T by a β-dependent constant, gaps unaffected | FAITHFUL | A3_NOTES:102 | "3 ln β + O(1)... gaps are unaffected" |
| 5 | Center-even sector, projector = identity, h=β^{-1/3}, h_k = -½ΣΔ+2Σ\|x_i×x_j\|² | FAITHFUL | A4_M1:5,10-12,18 | same |
| 6 | Reported statement (1-λ_j)/h→e_j, log(λ0/λ1)/h→e1-e0>0 | FAITHFUL | A4_M1:7-9 | same |
| 7 | Status: 27 of 30 stand, 0 defective, 3 not checked | FAITHFUL | crossreview:41; A3_NOTES:112 | "STANDS 27, DEFECT 0, NOT CHECKED 3" |
| 8 | Checked "step by step" by the first lineage | FAITHFUL (see 9) | crossreview:1,4 | reviewer says it shares Z4's family; agreement "not independent review" (section says lineage, ok) |
| 9 | "one wording slip in the companion proof of the vacuum energy" | FAITHFUL | crossreview:1,15 | "concavity" for convexity chord bound, in M0 |
| 10 | "not read by a person" | FAITHFUL | A3_NOTES:105,114 | "None of this has been read by anyone but its author" |
| 11 | "Lean files cover scalar lemmas only" | FAITHFUL | crossreview:1,33-34,51 | real-number lemmas only |
| 12 | Full text at repository folder `yang-mills/observable-normalization/one-site-vacuum/` and \cite{Repo} | UNSUPPORTED | none | no input contains "observable-normalization"; the .tex header says one-site-vacuum/excitation/README.md. \cite{Repo} has no bibitem in refs_add.tex (may be in main.tex: NOT CHECKED) |
| 13 | No numerical value for e1-e0 from the proof; companion c β^{-1/3} ≤ -logλ0 ≤ Cβ^{-1/3} | FAITHFUL | A4_M1:14; A4_M0:7 | |
| 14 | Proof step 1 (fibre inequality, m=⌈8/r⌉, smoothing, tube, K≤K_j, V≥V_ij, (2)) | FAITHFUL | A4_M1:20-25 | "I−K ≥ I−K_j and V ≥ V_ij"; walk killed at rate V_ij is via B=(1+V)^{-1}K (M1:22 end) |
| 15 | Step 2 (g=e^{-V/2}F, C'/R, valley arms, kinetic bound (3), J_h, Rellich) | FAITHFUL | A4_M1:30-36; crossreview:21,26 | "controls escape along the commuting valley" is M1 l.30 (trace comment says l.28) |
| 16 | Step 3 (consistency; βEξξ→δ; remainder O(β^{-3/2}h^{-3})=O(h^{3/2})) | FAITHFUL | A4_M1:46-48; crossreview:27 | trace comment says l.46, text is l.48 |
| 17 | Step 4 (min-max both ways, compact resolvent, simple positive ground state, e1>e0, -logλ=(1-λ)+O(h²)) | FAITHFUL | A4_M1:52-54 | |
| 18 | Second proof of k=2: 4 center boxes + capped arms; 11 stand, 1 sign defect (bound survives), 1 constant rederived, 1 partition function replaced; not read by a person | FAITHFUL | A3_NOTES:113-114 | "challenged once": same-lineage challenger (l.114) |
| 19 | Remark: all-center-sector bounds e^{-C√β} ≤ log(λ0/λχ) ≤ e^{-c√β}; first gap between them; β^{-1/3} only center-even | FAITHFUL | A4_center:5-9; A3_NOTES:109 | |
| 20 | Remark status: not in the step-by-step check | FAITHFUL | crossreview:1 | covers M0, M1 only |
| 21 | "center-odd splittings fall below double precision from β=128"; form not fixed | FAITHFUL | numerics2:23-24; A3_NOTES:93 | "functional form: DEFECT (overclaim)"; "β≥128 below double precision" |
| 22 | Table e0=3.3505330, e1=5.3254970, e1-e0=1.974964 | FAITHFUL | numerics2:14-15; A3_NOTES:91 | my P2: 1.9749640 |
| 23 | log(λ0/λ1)β^{1/3}: 1.636,1.760,1.837,1.887,1.919,1.939 (β=32..1024) | FAITHFUL | A3_NOTES:85; crossreview:164-169 | my P1: 1.6355,1.7598,1.837,1.8866,1.9186,1.9391 (6/6 within 5e-4) |
| 24 | two-term fit 1.97496; endpoint deletion 1.97503, 1.97489 | FAITHFUL | A3_NOTES:92; numerics2:20 | |
| 25 | e0(h3)=6.534885; first gap 3.012539 (5-fold, J=2); scalar gap 3.602838 | FAITHFUL | numerics3:20,95; A3_NOTES:96 | trace comment cites numerics3 l.164/242: wrong (see 40) |
| 26 | e0 in vB normalisation 4.1167196, published 4.116719735 | FAITHFUL | A3_NOTES:116; grounding:10,28 | my P8: 4.1167195851, diff -1.499e-7, tol 3.15e-7 |
| 27 | lattice log(λ0/λ1) β=1,2,4: 2.876117, 1.621505, 0.968930 | FAITHFUL | numerics3:18,81-83 | trace comment l.225-227 does not exist (see 40) |
| 28 | times β^{1/3}: 2.88, 2.04, 1.54 (not asymptotic) | FAITHFUL | numerics3:21,81-83; A3_NOTES:96 | my P3: 2.8761, 2.043, 1.5381 |
| 29 | O(2) symmetry, e1=e2 exact doublet of charge two; lowest non-scalar branch proved, position below scalar level rests on numerics | FAITHFUL | A3_NOTES:94; numerics2:16 | |
| 30 | Lattice splitting 0.19238 vs 0.19331 at β=1024; square group permits not forces | FAITHFUL | A3_NOTES:94 | |
| 31 | Lattice values approach from below; at β=1024 (1-λ)/h 16-23% below e_j, -logλ/h within 1.3% | FAITHFUL | crossreview:1,171 | my P4: 15.61%, 23.07%; 0.95%, 1.27% |
| 32 | 4-point fit, one residual dof; three-point geometric extrapolation 1.97583 | FAITHFUL | A3_NOTES:92; numerics2:21 | |
| 33 | Two methods (Peter-Weyl; Nyström+Lanczos), agree to 4.6e-9 | FAITHFUL | A3_NOTES:91; numerics2:12 | |
| 34 | 3-direction lattice converged only to β=4; β=8 not converged; nothing measured about the limit | FAITHFUL | A3_NOTES:96; numerics3:19,21 | |
| 35 | vB normalisation -½Δ+½Σ, energies ÷4^{1/3} | FAITHFUL | grounding:9,35; A3_NOTES:116 | grandchild + my P derivation: a=4^{-1/6} |
| 36 | vB00 calls 4.1167 "mass of the scalar glueball"; ground energy in eq. (12) | FAITHFUL | grounding:14; A3_NOTES:120 | |
| 37 | Gaps 1.89778, 2.26965; not compared with literature; LM84 abstract only | FAITHFUL | A3_NOTES:116; grounding:11-12,30 | conversion reproduced (grandchild: 1.89778065, 2.26964572) |
| 38 | Derivation: 1-½TrU_P=⅛\|A×A\|², H, rescaling to (βL³)^{-1/3}h3, m≈eβ^{-1/3}/L, e=3.012539 | FAITHFUL | grounding:43-50 | my P6 re-derives coefficients ½ and 2 |
| 39 | "mL=e'g^{2/3}... small-volume expansion of Lüscher [Lu83] with the same leading coefficients" | OVERSTATED | grounding:29,35,50; A3_NOTES:116 | Lu83 read as abstract only, which gives no numbers; coefficient match was made against van Baal/LM (g^{2/3} form, and only e0 compared; gaps not compared). Only the g^{2/3} form is supported for Lu83 |
| 40 | Trace comments for numerics3.md (l.164, 165, 242, 225-227, 272, 162-165) | WRONG (trace) | numerics3:18-21,81-83,95,128 | file has 188 lines; l.225-227, 242, 272 don't exist; l.162-165 are the grandchild's Monte-Carlo text. The values are right, the line cites are not (my P10) |
| 41 | Derivation assumes T→e^{-H}, neglects non-constant modes, not proved for L>1 | FAITHFUL | grounding:53,70,80 | "box analogue of the reported statement" is writer's wording; inputs say only "assumed, not proved" |
| 42 | Literature regime: z>0.9 (vB pp.11-12), crossover z≈2 (LM abstract) | FAITHFUL | grounding:17,57-58 | |
| 43 | Conclusion "gives no lower bound uniform in the volume" | FAITHFUL (writer's inference) | A3_NOTES:116 | |
| 44 | Search statement: no proof of discrete-time limit, no uniform lower-bound theorem, no published h2 spectrum; weak evidence | FAITHFUL | grounding:16,18-19,101; A3_NOTES:118 | |
| 45 | Reading marks: vB00 full; Lu83, LM84 abstract only; refs_add notes | FAITHFUL | grounding:28-30 | |
| 46 | refs_add: LM84 NPB232 (1984) 445; Lu83 NPB219 (1983) 233; vB00 hep-ph/0008206 (2000) preprint | FAITHFUL | grounding:28-30 | DOIs match; "Münster", titles as in grounding:29-30; end pages not given (as stated) |
| 47 | False start: uncapped weight false because 1-K≤1 and V=0 on high-spin states at a1=a2=π/2, common axis; capped lemma replaces it | FAITHFUL to source, argument incomplete | A3_NOTES:103 | wording copies A3; the writer's own note says the formula as printed does not imply falsity. Not a section-vs-input difference; the logic is unproved in the input |
| 48 | "Table: all entries measured, none proved" | FAITHFUL | A3_NOTES:85,96 | numerics2:14-15 independently reproduced |
| 49 | cite page "pp. 11-12" for z>0.9 | FAITHFUL | grounding:58 | A3_NOTES:118 says 11-15 for the regime generally |
| 50 | Proof sketch step numbering "ours"; sketch is "as written by its author" | FAITHFUL (partly paraphrase) | A4_M1 | Step 1 phrase "survival of the walk killed at rate V_ij" paraphrases M1:22 (B=(1+V_ij)^{-1}K_j) |

## Programs
check_sec.py (v1): met 10, failed 0, measured only 1, **but P10 (trace line numbers exist) passed wrongly: my parser read only comments that start a line, so table-row comments were skipped. A defect of my program, not of the target.** Kept as results_check_sec.txt.
check_sec_v2.py (parser fixed): **met 9, failed 1, measured only 1.** Failed predicate P10: numerics3.md l.227, 242, 272 do not exist (file has 188 lines) — a defect of the target (items 40). Predicates P1-P9 met (items 22-28, 31, 35, 38).
P10 "for all" hypothesis: 54 cited line references qualify to test; 51 within file length, 3 not.
Grandchild (grandchild/check.py, own report): met 7, failed 0, measured only 1; its rerun by me reproduced all values (the rerun's last line failed only because of mode "x" on an existing results.txt; no values differed). Tolerances: half unit of the last printed digit of each quoted number, plus 5e-7·4^{-1/3} for the 6-decimal inputs.
Tolerance for P1: 5e-4 (3 printed decimals); P3: 5e-3; P4: 0.5 point (the text gives integers 16, 23) and 1.3+0.05.

## Not checked
- the main.tex (hyp:A, \cite{Repo}, cite keys beyond refs_add.tex);
- primary literature (vB00, Lu83, LM84): only the grounding record was used;
- the soundness of the proofs themselves, only whether the section describes them as the inputs do;
- raw numerics (λ's) behind A3_NOTES numbers; I recompute only products/ratios from tabulated values;
- the three-point extrapolation 1.97583 and fit values (no raw data);
- references' page ranges/DOIs beyond the grounding record.

## Rerun
```
cd /home/user/z4-workers/i1-sec/child
python3 -c "import math;print('%.6f'%-math.log(math.tanh(.5)))"
mv results_check_sec_v2.txt /tmp/old 2>/dev/null; python3 -I check_sec_v2.py   # exit 1 by design (P10)
cd grandchild && rm -f results.txt && python3 check.py
```
PCP register in pcp/: checks K1 check-sec (exit 0, expected 1: the v1 parser defect) and K2 check-sec-v2 (exit 1).

## Register verification (last lines)
- `$P verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
- Task graph: grandchild admitted as T106, released after its result was reread and rerun. The register's K1 mismatch (exit 0, expected 1) is the v1 parser defect named above.
