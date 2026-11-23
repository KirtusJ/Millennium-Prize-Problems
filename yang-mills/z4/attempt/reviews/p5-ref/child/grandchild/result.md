# G(1) via Schwinger/Bessel reduction

Value: 0.0688747
Estimated quadrature error: 2.8e-17 (difference between successive refinements: 0.068874746, 0.068874746, 0.068874746)

Method: 1/khat^2 = int_0^inf exp(-s khat^2) ds; per-direction factor f_n(s)=e^{-2s}I_n(2s). Numerator khat_1^2 -> -f0'(s)=2(f0-f1) (using I0'=I1). cos(k0) -> f1. G(1)=2*int_0^inf 2(f0-f1) f0^2 f1 ds.
f_n computed as (1/N)sum exp(2s(cos t-1))cos(nt) (periodic midpoint rule, N=4096) for s<=200; for s>200 the Bessel large-argument asymptotic series (12 terms). Gauss-Legendre panels: linear on [0,1], log-spaced on [1,1e9]; tail beyond 1e9 ~ s^-3, negligible. Control: 1/(pi^2 2^4)=0.006333 (control.txt).
