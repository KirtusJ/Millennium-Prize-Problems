# Top eigenvalue of Tf(u)=Int k(u,v)f(v)dv, k=(8pi)^-1/2 exp(-(u-v)^2/8-(u^2+v^2)/4)

## Algebra (f=exp(-alpha v^2/2))
Tf(u) = (8pi)^-1/2 e^{-u^2/4} Int exp(-(u-v)^2/8 - v^2/4 - alpha v^2/2) dv
Exponent in v: -A v^2 + (u/4) v - u^2/8, with A = 3/8 + alpha/2.
Gaussian integral: sqrt(pi/A) exp(u^2/(64A)).
So Tf(u) = (8pi)^-1/2 sqrt(pi/A) * exp[(-3/8 + 1/(64A)) u^2]  (prefactor = 1/sqrt(8A)).
Eigen-condition: -alpha/2 = -3/8 + 1/(64A). With x=alpha/2: x(3/8+x) = (3/8)(3/8+x) - 1/64 -> x^2 = 1/8.
x = 1/(2 sqrt2) => alpha = 1/sqrt2 = 0.7071067812 (positive root, normalizable).
A = 3/8 + 1/(2 sqrt2) = (3+2 sqrt2)/8 => 8A = (1+sqrt2)^2.
lambda = 1/sqrt(8A) = 1/(1+sqrt2) = sqrt2 - 1 = 0.414213562 = exp(-arsinh 1). Claim confirmed.

## Numbers (check.py, output in check_output.txt)
- alpha = 0.7071067812, lambda_analytic = 0.414213562373, claimed = 0.414213562373 (diff -5.6e-17)
- Nystrom grid, symmetric K*h, eigvalsh top:
  L=10,h=0.2: 0.414213562373 (diff 1.5e-15); L=12,h=0.1: diff 1.5e-15; L=12,h=0.05: -5.8e-15; L=14,h=0.05: -5.8e-15
- Grid difference ~1e-14 or less.

## Tolerance source
Not fixed a priori: errors are floating-point roundoff (~1e-15 to 1e-14, eigvalsh on a few-hundred-dim matrix)
plus quadrature error and box truncation. The trapezoid/Riemann rule on a smooth Gaussian integrand is
spectrally accurate (error ~ exp(-pi^2 * w / h^2)-type), and truncation error ~ exp(-L^2/ something) with kernel decay
e^{-u^2/4}; both are far below roundoff for L>=10, h<=0.2. A sensible tolerance is therefore ~1e-12.
Also note: all tested (L,h) agree, so the result is converged.
