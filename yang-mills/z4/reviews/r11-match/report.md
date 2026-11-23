# r11-match report: matched-pair measurement of R(tau) and Q0, SU(2) Wilson, (beta,N) = (2.3,6^4) vs (2.5,12^4)

Measurement only. No theorem, no continuum limit. Lean not used (/home/user/z4-lean/READY absent).
Primary result file: `results_1.txt` (fixed sample: coarse 2990 cfgs, fine 160 cfgs after 10 skipped).
Supplementary: `results_2.txt` (fine extended to 260 cfgs AFTER seeing results_1 — optional stopping, see below).
Control: `control.txt` = 0.272341.

## 1. Verdict table

| item | verdict | evidence |
|---|---|---|
| M0 a*sqrt(sigma): 0.3690(30) at 2.3, 0.1905(8) at 2.5 | STANDS | FHK hep-lat/9208012 Table 3, checked by me in the source text |
| M0 plaquette (FHK Table 8, 1-<U_p> at 2.2986/2.3726/2.4265/2.5115) | STANDS | checked in source; not tabulated at exactly 2.3/2.5, interpolated |
| M0 m(0++)/sqrt(sigma) = 3.74(12) continuum | STANDS | Teper hep-th/9812187 Table 1, SU(2) column, checked in source |
| Size matching l_f/l_c - 1 | +3.25(94)% | 12x0.1905 / 6x0.3690; LTW hep-lat/0307017 Table 1 (0.17680(76) at 2.5115) suggests the mismatch may be ~0 |
| C1 strong coupling beta=0.5 | STANDS | 0.875486(760) vs 1-I2/I1 = 0.876282, diff -1.0 sigma (seed 8) |
| C2 plaquette beta=2.3, 6^4 | STANDS | 0.602953(159) vs FHK-interp 0.602934(37) |
| C2 plaquette beta=2.5, 12^4 | STANDS | 0.652029(160) vs FHK-interp 0.651941(198) |
| C3 gauge invariance (plaq, Ebar unflowed and flowed) | STANDS | max deviation 4.4e-16 (tol 1e-10), both L, two seeds |
| C4 flowed spatial action monotone | STANDS | every RK3 step decreases, both L, two seeds |
| C5 step halving | STANDS | rel. change 1.1e-5 (6^4, eps .025) and 5.9e-7 (12^4, eps .05), tol 1e-4 |
| C6 free field s=0.5 | STANDS | +5.9%, +7.5% (6^4, two seeds), +5.6% (8^4); tol 20% |
| C6 free field s=1.0 | DEFECT (of the control on 6^4) | +29.6% FAILED (seed 7), +14.4% (seed 8), +10.0% (8^4): seeds disagree by ~5 sigma, so the quoted control errors are too small; see section 3 |
| P1 positivity, coarse | STANDS | R(0)=3.751(42)e-2, R(1)=1.012(32)e-2, R(2)=3.65(34)e-3 |
| P1 positivity, fine | STANDS | R(0)=3.42(12)e-2, R(2)=5.00(66)e-3, R(4)=0.48(1.20)e-3 |
| P2 monotone + log-convex, coarse | STANDS | differences +84, +20 sigma; R0R2-R1^2 = +3.3 sigma |
| P2 monotone + log-convex, fine | STANDS (weak) | differences +20, +3.2 sigma; R0R2-R1^2 = -0.2 sigma (R(l/3) unresolved) |
| Question: same within errors at matched l, s, tau? | DEFECT (not the same) | R(l/6) ratio fine/coarse 0.494(67), 7.6 sigma from 1; Q0 ratio 0.956(12), 3.6 sigma; R(0) 0.913(33), 2.7 sigma |
| R(l/3) at the fine spacing | NOT RESOLVED | 4.8e-4 +- 1.2e-3 (0.4 sigma); ratio 0.13(33) is meaningless |
| P4 m_eff/sqrt(sigma), coarse | measured only | 3.01(19) cosh form, 2.76(22) log form vs 3.74(12): 3.3 sigma low (cosh) |
| P4 m_eff/sqrt(sigma), fine | NOT RESOLVED | R(l/3) unresolved, jackknife error undefined |

Counts (all predicate evaluations in results_1 and the controls; results_2 supplementary adds 3 met): **25 met, 1 failed, 8 measured only**
(measured only: 6 P3 ratios, 2 P4 values).

### Measured numbers (results_1.txt)

| quantity | coarse 6^4 b=2.3 (s=0.5) | fine 12^4 b=2.5 (s=2.0) | fine/coarse |
|---|---|---|---|
| R(0) | 3.751(42)e-2 | 3.42(12)e-2 | 0.913(33) |
| R(l/6) | 1.012(32)e-2 [tau=1] | 5.00(66)e-3 [tau=2] | 0.494(67) |
| R(l/3) | 3.65(34)e-3 [tau=2] | 0.48(1.20)e-3 [tau=4] | 0.13(33), unresolved |
| Q0 = s^2 * 4 Ebar | 9.335(26)e-2 | 8.93(11)e-2 | 0.956(12) |
| Q0beta = s^2 * beta Ebar | 5.367(15)e-2 | 5.580(69)e-2 | 1.040(13) |
| m_eff l (log / cosh) | 6.12(48) / 6.66(42) | 14.0 / 14.1, error undefined | — |
| tau_int (cfgs), block, indep. blocks | 1.08, 11, 271 | 1.81, 19, 8 | |
| time per configuration | 0.24 s | 6.2 s | (1 core, machine load ~5) |

### Supplementary (results_2.txt; fine extended to 260 cfgs after seeing results_1 — optional stopping, so weight it accordingly)
Fine: tau_int rose 1.81 -> 2.40 cfgs (block 25, 10 independent blocks); R(0)=3.30(9)e-2, R(l/6)=5.04(52)e-3,
R(l/3)=0.95(58)e-3 (1.6 sigma, still not resolved), Q0=9.07(10)e-2 (moved +1.3 sigma from the first 160 cfgs:
possible incomplete thermalisation after 100 sweeps, or underestimated errors), m_eff l (cosh) = 10.2(3.6),
m_eff/sqrt(sigma) = 4.5(1.6). Ratios fine/coarse: R(0) 0.880(25), R(l/6) 0.498(54), R(l/3) 0.26(16), Q0 0.972(11),
Q0beta 1.056(12), m_eff l 1.6(6). P1, P2 still MET; C2 plaquette 0.651949(113) MET. The conclusion is unchanged:
R(l/6) differs by a factor ~2 between spacings; Q0 differs by 3-4%; R(l/3) is not resolved at the fine spacing.

Size of an O(a^2) effect: the flow radius is sqrt(8s) = 2a (coarse) and 4a (fine), so (a/sqrt(8s))^2 = 0.25 vs
0.0625; a cutoff term c*(a^2/8s) with |c| ~ 0.2 accounts for the 4.4% Q0 difference. For R(l/6) the coarse
separation is ONE lattice spacing in time, and the observable is smoothed only in space, not in time: states at
the cutoff contribute e^{-E a} at one step. The factor 2 between spacings at tau = l/6 is far beyond an O(a^2)
effect of that size; it says R(l/6) at this coarse spacing is dominated by lattice-scale (unsmoothed temporal)
contributions. Size-mismatch systematic: if l_f/l_c = 1.0325, R ~ l^-3 alone would give R_f/R_c ~ 0.91 — this
covers R(0) (0.913(33)) but not R(l/6). For Q0 the mismatch moves s by +6.6%, and with d ln(s^2 E)/d ln s
= +0.42..+0.57 (measured) it would RAISE Q0_f by ~3%, the wrong direction to explain 0.956.

## 2. Hypotheses used and where stated
- Wilson action, SU(2), periodic 4D lattice: ym.py docstring.
- Scale from FHK Table 3 (a compilation from older lattices, sizes 10^4..32^4); its systematic is not ours to judge.
- Positive self-adjoint transfer matrix of the Wilson action (Luscher 1977) for P1: then C_conn(tau) =
  sum_{n,m} e^{-E_n(T-tau)-E_m tau} |<n|O-<O>|m>|^2 / Z >= 0 for ALL tau even at finite periodic T, because Ebar_0 depends
  only on unflowed spatial links of slice 0 (spatial flow acts per slice). derivations.md / this report.
- Tree-level normalisation E_mag a^4 = 4 Ebar: derivations.md.
- Free-field mode sum E_free(s): derivations.md (t=0 check 9/(4beta) reproduced to finite-volume accuracy).
- Glueball comparison assumes m_eff at tau in [l/6, l/3] is the ground state; with l sqrt(sigma) ~ 2.2 (~1 fm)
  this is a small-volume, short-time estimate, and the brief's caveat applies.
- Jackknife errors assume blocks of 10 tau_int are independent; fine ensemble has only 8 blocks, so its errors are
  themselves uncertain by ~25%.

## 3. Failed predicates
- C6 free field at s=1.0 on 6^4, seed 7: +29.6(2.2)% vs tol 20% — FAILED. Seed 8 gives +14.4(2.4)%, 8^4 gives +10.0(2.0)%.
  Judgement: the failure is in my control, not established as a code defect. Two seeds disagreeing by ~5 sigma means
  the 12-configuration error (no autocorrelation analysis, 60 thermalisation sweeps from cold at beta=40) is too small;
  spatially constant modes (k_s = 0) are not damped by spatial flow and their slow dynamics at weak coupling plausibly
  dominate the excess (my hypothesis, not tested beyond the L=8 run going in the right direction). The flow
  normalisation is tested at s=0.5, where a factor-2 error would be far outside 20%.
- Defect of my own code found by a control: jk_err in ym.py used sqrt((nb-1) var) instead of sqrt(var/(nb-1)),
  overstating the C1 error x19 in controls_7.txt. Fixed; controls rerun as controls_8.txt. analyse.py was not affected.
- Not a failed predicate but noted: fine R(6) = -2.0(1.1)e-3 (-1.8 sigma), R(5)=R(7) = -0.5(1.0)e-3. Positivity holds for
  all tau by the argument above, so these are fluctuations within 2 sigma; P1 as fixed covers only l/6 and l/3.
- The question itself ("same within errors"): answered NO at tau = 0 (2.7 sigma), l/6 (7.6 sigma) and for Q0 (3.6 sigma).

## 4. Not checked
- Any continuum limit (two spacings only); a third spacing (e.g. 2.4 with N=9 would need a 9^4, not done).
- Clover form of the density (only plaquette form used).
- Finite-T/aspect-ratio effects: T = l (symmetric box), so the "time" direction is periodic with the same short extent;
  wrap-around is handled only in the cosh form of m_eff.
- Plaquette at exactly beta=2.3, 2.5 from a publication (interpolated FHK Table 8; tolerance includes interpolation).
- The scale at exactly beta=2.5 from a second source (LTW values only near 2.5115).
- The analytic claim that the C6 s=1.0 excess is a zero-mode effect.
- Autocorrelation of the Monte Carlo at beta=40 (C6).

## 5. Delegated questions and outcomes
- Child (sonnet, child/, K1 in my register, 77 s): literature lookup M0 + size matching.
  Control I2(1)/I1(1): answered 0.240194 — CORRECT (graded first). Returned FHK Table 3 / Table 8, Teper Table 1,
  LTW Table 1 numbers; I verified each number used in the source text (section 1). I reran child/match.py in
  rerun_child/: output identical. The child reported web search refused and used arXiv PDFs only. The child
  violated "do not copy paper text": it saved PDFs/text in child/src; I deleted child/src after checking.
- Grandchild (child's Agent, child/grandchild/): re-locate a*sqrt(sigma) at beta=2.5. Control 1 - I2(.5)/I1(.5):
  grandchild/control.txt = 0.876282 — CORRECT (I computed 0.876282). The grandchild left no result file; its answer
  0.1905(8), FHK Table 3, exists only as the child's claim. I confirmed 0.1905(8) in the source myself.

## 6. Commands to rerun (from /home/user/z4-workers/r11-match, OMP_NUM_THREADS=1)
```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name controls --expect-exit 0 -- python3 ym.py controls --seed 7
$P check --ws pcp --name controls-seed8 --expect-exit 0 -- python3 ym.py controls --seed 8
$P check --ws pcp --name freefield-L8 --expect-exit 0 -- python3 ym.py freefield --L 8 --seed 11 --n 12
$P check --ws pcp --name run-f-12-b2.5 --expect-exit 0 --timeout 1500 -- python3 ym.py run --L 12 --beta 2.5 --ncfg 170 --nsweep 2 --nor 3 --ntherm 100 --seed 1205 --s 2.0 --eps 0.05 --out meas_L12_b2.5_s1205.txt
$P check --ws pcp --name run-c-6-b2.3 --expect-exit 0 --timeout 1500 -- python3 ym.py run --L 6 --beta 2.3 --ncfg 3000 --nsweep 2 --nor 3 --ntherm 200 --seed 623 --s 0.5 --eps 0.025 --out meas_L6_b2.3_s623.txt
$P check --ws pcp --name analyse-1 --expect-exit 0 -- python3 analyse.py meas_L6_b2.3_s623.txt meas_L12_b2.5_s1205_first170.txt results_1_rerun.txt   (original ran on the 170-cfg file before extension)
$P check --ws pcp --name run-f-12-b2.5-ext1 --expect-exit 0 --timeout 1200 -- python3 ym.py run --L 12 --beta 2.5 --ncfg 100 --nsweep 2 --nor 3 --seed 1205 --s 2.0 --eps 0.05 --out meas_L12_b2.5_s1205.txt --resume
$P check --ws pcp --name analyse-2 --expect-exit 0 -- python3 analyse.py meas_L6_b2.3_s623.txt meas_L12_b2.5_s1205.txt results_2.txt
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
```
To extend any run: same `run` line with `--resume` and a new `--ncfg` (state in `<out>.ckpt.npz`, appends lines).
Rerunning into existing output names fails by design (mode "x"); choose new names.
The first 170 fine lines are kept read-only in meas_L12_b2.5_s1205_first170.txt (input of results_1).

## 7. PCP OS record
Register pcp/ (checks K1 child-run1, K2 controls, K3 run-c-6-b2.3, K4 controls-seed8, K5 freefield-L8, K6 run-f-12-b2.5,
K7 analyse-1, K8 run-f-12-b2.5-ext1, K9 analyse-2, K10 analyse-1-rerun).
- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp` last line:
  `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl` last line:
  `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
Note: the ad-hoc FFT recomputation of R(tau) and the timing probe were run outside the register (recorded in notes.md).
Reviewer caveat: the director and I share a model family; this is not independent review.
