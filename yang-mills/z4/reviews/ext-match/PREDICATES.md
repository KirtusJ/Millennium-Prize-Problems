# Extension of the matched measurement (Director Z4, 23 November 2026), fixed before the runs

Programs: `ym.py`, `analyse.py` of worker r11-match, unchanged (copied bytes). Reason for the extension: the worker's
fixed sample found R(l/6) different by a factor of two between the two spacings, with the coarse separation equal to one
lattice step, and left R(l/3) unresolved at the fine spacing.

Runs (every argument):
- mid:   python3 ym.py run --L 8 --beta 2.4 --ncfg 1500 --nsweep 2 --nor 3 --ntherm 200 --seed 824 --s 0.888889 --eps 0.0277778 --out meas_L8_b2.4_s824.txt
- fine2: python3 ym.py run --L 12 --beta 2.5 --ncfg 300 --nsweep 2 --nor 3 --ntherm 200 --seed 1206 --s 2.0 --eps 0.05 --out meas_L12_b2.5_s1206.txt
- fine3: python3 ym.py run --L 12 --beta 2.5 --ncfg 300 --nsweep 2 --nor 3 --ntherm 200 --seed 1207 --s 2.0 --eps 0.05 --out meas_L12_b2.5_s1207.txt

Scale (Fingberg, Heller, Karsch, hep-lat/9208012, Table 3): a sqrt(sigma) = 0.3690(30), 0.2660(20), 0.1905(8) at
beta = 2.3, 2.4, 2.5. Box sides l sqrt(sigma) = 2.214, 2.128, 2.286 for N = 6, 8, 12: the middle box is 3.9 per cent
smaller than the coarse one and 6.9 per cent smaller than the fine one. This mismatch is a systematic and is not corrected.
Flow time s = l^2/72 on each lattice (s/a^2 = 0.5, 0.889, 2.0).

Predicates, fixed now:
- E1 (must hold; a failure is a code or reasoning defect): R(tau) >= 0 within 2 sigma at every tau on every ensemble.
- E2 (measured only): Q0 = s^2 * 4 * Ebar at the three spacings against x = a^2/(8s) = 0.25, 0.14, 0.0625. Report the
  three values and the two-point slopes; "consistent with a straight line in x" means the middle point lies within
  2 sigma of the line through the outer two.
- E3 (measured only): R(0) at the three spacings, same reading.
- E4 (measured only): R at tau/l = 1/4 (N = 8: 2 steps; N = 12: 3 steps) and at tau/l = 1/2 (3, 4, 6 steps), ratios with errors.
  Whether R at fixed tau/l converges as the number of lattice steps in tau grows is the question; the answer is not presumed.
- E5: fine ensembles of the three seeds are combined only if their means of Ebar agree within 2.5 sigma pairwise; otherwise
  reported separately and the disagreement kept.
No tuning after the data are seen. Errors by jackknife with blocks of 10 integrated autocorrelation times, as in analyse.py.

## Interruption, recorded 23 November 2026 about 10:51 UTC
The session's process was restarted while the three runs were in progress; all three were killed and left no event in
the director's register. Lines on disk at that time: 466 configurations (N = 8), 44 and 44 (N = 12, seeds 1206, 1207).
They are continued with the same arguments plus `--resume` (the program's own checkpoint), as register checks
`ext-mid-L8-resume`, `ext-fine-1206-resume`, `ext-fine-1207-resume`. Predicates unchanged. The target numbers of
configurations are unchanged; if a run is cut again, what is on disk is analysed and the count stated.

## Second deviation, recorded 23 November 2026 about 11:25 UTC
`--resume` with `--ncfg n` adds n configurations to what is on disk; it does not stop at n in total. The director
assumed the latter. The resumed runs therefore went past the declared counts. `ext_results_1.txt` was computed while
they were still appending (1965, 329 and 329 configurations before the 10 skipped) and is kept as a snapshot, not as
the result. The runs were then stopped by the director (no register event for them, as for the first interruption).
The result is `predeclared/ext_results_2.txt`: the same program on the files cut to the declared counts, the first
1500 configurations of N = 8 and the first 300 of each new fine seed, together with the worker's 2990 coarse and its
fine file of 270 lines (the worker's own extension after seeing its data, flagged by the worker as optional stopping).
The full files are kept beside them.

Correction to the paragraph above (same day): the N = 8 run was not stopped by the director. It ended by itself after
adding 1500 configurations (1965 on disk) and has its register event (`ext-mid-L8-resume`, exit 0). Only the two fine
runs were stopped by hand, at 332 configurations each, and have no event.
