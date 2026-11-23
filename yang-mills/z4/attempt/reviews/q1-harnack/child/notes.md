# notes
- control done: c*=4.6054 (numpy only; scipy absent -> dense np.linalg.eigh, Gauss-Legendre)
- grandchild T154 (admitted) returned: N=204, sqrt(b)L(0.1)=0.375048 at x=0.0924 (idx105), L(0)=0, lambda=0.8193455397; noted 2-fold degeneracy (wells 0 and pi).
- main.py run K2 FAILED predicate "g.min()>0": min=-6.1e-16 (floating roundoff in the far-tail between wells, where true g ~ 1e-100 scale). Failure = my own expectation (double precision cannot hold strict positivity in the tails), not a defect of the target. Revised predicate: g>0 at the used points (|x|<=0.5) and g.min()>-1e-12; failed run kept in the register.
- report.md written; verifies pass
