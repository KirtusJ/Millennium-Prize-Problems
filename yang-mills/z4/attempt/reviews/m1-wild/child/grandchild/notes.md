# G(1) via Schwinger representation

Method: 1/D = Int exp(-tD) dt; 1D factors via exp(-x)I_v(x), x=2t, with I_0, I_1 implemented by hand
(power series for x<=20, asymptotic series beyond). G = (1/2) Int_0^inf 4 i1 (i0-i1) i0^2 dx.
Tail x>60 integrated in u=1/x (integrand ~u, smooth), not truncated.

Value: G(1) = 0.0688747458 (0.06887474584050)
Error estimate: ~1e-12 (conservative; observed variations 1e-16 under switch point 15/30,
panel/order/cutoff changes; Bessel vs integral definition 3e-15).
Tolerance source: those self-consistency spreads plus double-precision roundoff; no target value used.
Checks: cos->1 gives 0.5000000000000006 (exact 1/2); control.txt = 1.000000.
Script: g1_schwinger.py (predicates in docstring, all passed).
