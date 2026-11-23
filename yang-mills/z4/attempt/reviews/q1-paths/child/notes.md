# notes T153
- control: I=1.648721 (=exp(1/2)); no mpmath/scipy available -> will use python Decimal (50 digits) for eigenvectors (tail accuracy of h near pi/2). Grandchild T155 admitted, running.
- run1 (tag dbg) crashed: Decimal+float TypeError (own bug; pcp K2 exit 1). run dbg2: g eigvector sign not fixed (g_min<0, rho garbage) -> own bug, fixed (flip g if sum<0). Delta(16)=6.00392838e-7 matches grandchild T155 (identity 6.003928380884987e-07). Finding: h is EVEN under x->-x (h(0)=+1,h(pi)=-1), not odd as the statement says; it is sigma-odd.
