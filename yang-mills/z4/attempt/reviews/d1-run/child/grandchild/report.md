# k_check report (R=4, eta=pi/4)
Control (768*(1-cos(pi/32))): 3.698130 (control.txt)

- S(V) from plaquette sum = 3.6981299157527445; closed form = 3.6981299157527587; diff 1.4e-14 -> PASS (<1e-9)
- k = 4 dS/deta, central diff: h=1e-3: -37.6385817883; h=5e-4: -37.6385818613; Richardson: -37.6385818856
- Closed form quoted as 24 R^2 sin((pi-2eta)/R^2) = +37.6385818866
- Predicate as literally stated (signed relative error <1e-6): FAIL, because of sign. rel err = 2.0.
  Cause: S0 depends on (pi-2eta), so the true derivative is dS/deta = -6R^2 sin(u); the quoted closed form is the magnitude.
- Magnitude |k_FD| vs closed form: relative error 2.5e-11 (Richardson) -> would PASS at 1e-6 if sign convention is ignored.
So k_FD = -37.638582 = -(parent's 37.638582). The parent value matches in magnitude only; sign differs.
