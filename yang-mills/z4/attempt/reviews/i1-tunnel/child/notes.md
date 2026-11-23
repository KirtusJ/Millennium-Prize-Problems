# notes T102
- [step0] control.txt written first: 2*sqrt(pi)*Gamma(3/4)/Gamma(5/4) = 4.792561
- [step1] derivation (i): w=beta s^2, Gaussian ansatz psi=exp(-c x^2/2): c'=2w+beta p/(beta+p), p=2w+c.
  fixed point c=2 sqrt(w(w+beta)); Lambda=sqrt(beta)/(sqrt(w)+sqrt(w+beta)) = 1/(s+sqrt(1+s^2)).
  eps_1D = arcsinh(sin a), beta-independent; total 2 arcsinh(sin a) = arccosh(1+2 sin^2 a) (cosh 2u = 1+2 sinh^2 u). Exact.
- [step2] derivation (ii): see report.
- [step3] check.py run under pcp check (K1 exit 0): all predicates P1-P4 passed, 0 failed. P3 1000/1000 qualify.
  c = 2*int sqrt(asinh sin a) = 4.605413 (control, small-s approx eps=2 sin a, gives 4.792561).
- [step4] grandchild admitted as T104, launched; waiting.
- [step5] grandchild T104 returned, rerun identical, released; report.md written
