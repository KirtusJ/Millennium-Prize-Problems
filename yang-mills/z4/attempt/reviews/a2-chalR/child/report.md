# Report: hypothesis (C), C(xi/2) <= D*C(xi)

**Verdict: STANDS** (numerically, m = 0.4 ... 0.0125; not a proof for m -> 0).

Control: control.txt = 0.367879 (e^-1).

## R(m) = C(xi/2)/C(xi)  (ratio.py; out1.txt, out2.txt)
Continuum prediction Rc = J(1/2)/J(1) = 2 K1(1/2)/K1(1) = **5.503975** (own Simpson quadrature of the integral; second route via the K1 integral agrees to 1e-15).

| m | xi | R(m) | R - Rc | R2 = R^2 |
|---|---|---|---|---|
| 0.4 | 2.516 | 5.469064 | -0.0349 | 29.9107 |
| 0.2 | 5.008 | 6.513378 | +1.0094 | 42.4241 |
| 0.1 | 10.004 | 5.738552 | +0.2346 | 32.9310 |
| 0.05 | 20.002 | 5.550620 | +0.0466 | 30.8094 |
| 0.025 | 40.001 | 5.515154 | +0.0112 | 30.4169 |
| 0.0125 | 80.0005 | 5.506743 | +0.0028 | 30.3242 |

R stays bounded (max 6.51 over all 6 cases, 6/6 below D=10) and converges to Rc = 5.504; the excess shrinks roughly by a factor 4 per halving of m (looks like O(m^2)). Limit estimate: R -> 5.504 (R2 -> 30.29). The finite D exists: D ~ 6.6 covers all tested m.
Caveat: "for all small m" is only tested at 6 values, with a smooth approach to the continuum limit. This is evidence, not proof.

## Predicates (fixed in ratio.py docstring before first run)
- P0 (Rc by two quadratures agree 1e-6): PASS.
- P1 (grid convergence, N=14xi vs 17.5xi, rel < 1e-6; tolerance from aliasing e^{-N/xi}~1e-6..1e-7): PASS all 6 (~1e-7).
- P2 (R <= D = 10, D my choice, ~2 Rc): PASS 6/6 cases.
- **P3 FAILED** (my expectation: |R-Rc| decreases monotonically as m decreases): m=0.4 gives |R-Rc|=0.035 < m=0.2 value 1.01. Failure of my own expectation (R overshoots at xi~5, non-monotone at coarse xi), not a defect of the target. Monotone for m <= 0.2.
- P4 (R2 = R^2): holds by construction, trivial.
Grid caveat: P1 compares only two grids of the same method (not an independent check); the grandchild supplies the independent one.

## Grandchild (grandchild/)
Asked: recompute R at m=0.1 only via the Schwinger/Bessel representation C(t)=int dtau e^{-tau(m^2+8)} I_0(2tau)^3 I_t(2tau) (non-integer order, own numpy implementation), control integral_0^1 x^2 dx = 0.333333 (control.txt: correct, 0.333333).
Came back (grandchild/run3.txt): C(xi/2)=8.87315000596502e-4, C(xi)=1.54623499139266e-4, R=5.73855206702649. Mine: C(xi/2)=8.873150e-4, C(xi)=1.546235e-4, R=5.738552049; relative difference 3e-9. **Agreement.**
Grandchild failed predicates (kept in grandchild/notes.md, run1_failed.txt, run2_P2fail_umin-12.txt): run1 P1/P2 failed (cancellation in the 2-term Bessel formula), run2 P2 failed at 2.8e-8 (tau lower cutoff), both fixed and rerun with the predicates unchanged. Its P5 ("0<R<1") is a wrong expectation (R>1 since C decreases in t); I did not see a P3-P5 output line in run3.txt (only R printed), so P3/P4 of the grandchild are not confirmed by me.
My rerun: bessel_R.py rerun twice by me. Both runs were cut by timeouts (120 s tool, 175 s own) before the main R line; they reproduced only P1 (3.8e-14) and P2 (1.3e-15; Bessel vs direct 3D at m=1 identical to 15 digits). So the grandchild's R=5.738552067 is **read from its own output, not independently rerun by me**; the P2 rerun does confirm its method.

## Rerun commands
    cd child
    python3 ratio.py 0.4 0.2 0.1 0.05 0.025      # ~2 s
    python3 ratio.py 0.0125                      # ~9 s
    cd grandchild && python3 -u bessel_R.py      # slow (>3 min with other load; main line after P2)

## PCP OS verify (last lines)
- python verify: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- rust verify: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- `init` reported method not found (expected).

## Addendum (grandchild final message, chk3.log)
- Grandchild's own P3 (2.7e-14) and P4 (1.7e-15) passed per its report; P5 (0<R<1) failed by its own wrong expectation. Its full run took 10m50s wall (user 15m44s > real, so it likely used more than one core: a breach of the 1-core limit and the 90 s per-program limit, by the grandchild). Those P3/P4 numbers are its claims; I did not see them in run3.txt.
- My PCP check `grandchild_rerun2` recorded exit 124 (expected 0): my 175 s timeout killed it before the main R line. This is a recorded failed check, as stated above.
