# r11-flowbounds — report (builder, positive arc)

Setting: STATEMENT.md, with the spatial flow from the brief. l = 1 in all numerics. Test function (non-symmetric, f > 0, ∫f = 1.42213):
f(y) = exp(0.8 cos2πy₁ + 0.3 sin4πy₁ + 0.6 cos(2πy₂ − 0.4) + 0.5 sin2πy₃ + 0.3 cos2π(y₁ − y₃)).
Control: control.txt = 0.272341. Programs: `flowbounds.py` (results_smoke.json, results_run1.json) and `R11Flow.lean`. Step log: notes.md.
