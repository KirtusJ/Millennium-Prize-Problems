# Notes
Scripts: control.py, haar_p12.py, link.py (results in *_result.txt, written mode 'x'). No scipy; Bessel I1,I2 by integral rep + Simpson.
Control: P(theta<pi/2)=0.500000000 (Simpson, 4M pts, density (2/pi)sin^2 chi; norm=1.000000000).
(1) P(theta<1.2): quadrature 0.27446856 (= closed form (t-sin t cos t)/pi); MC 0.274334 +- 0.000315 (N=2e6, seed 12345), pull -0.43.
(2) beta=3.276133577: <a0>=0.59653220 (= I2/I1), <a0^2>=0.45374737. Kennedy-Pendleton (k=beta, accept r4^2<=1-lam^2, a0=1-2lam^2), N=1e6 seed 777:
<a0>=0.596413+-0.000313 (pull -0.38), <a0^2>=0.453709+-0.000285 (pull -0.13); quaternion norm err 9e-16. No failures.
