# Findings
Control: p=(1,2,2), q=0 -> L=2.777778 (control.txt, written first by ctl.py).
Script check.py (seed 12345, 200000 samples per family, results.txt opened with mode "x"). Tolerance 1e-12*(1+|RHS|): about 4500 double ulps, to absorb rounding in norms/products, not a mathematical slack.

## Analytic
A: p=(0,0,t), q=(a,b,c). u=(a/2,b/2,c/2+t), w=(a/2,b/2,c/2-t). With rho^2=(a^2+b^2)/4, L = rho^4/(|u||w|) >= 0 (0 if u or w is 0). RHS=-t^2-(3/4)|q|^2 <= 0. So L>=RHS always; equality only at t=0,q=0 (L=0=RHS). Also L-RHS=0 whenever p=0,q=0 only; otherwise strictly positive.
B: q=lam p: u=(1+lam/2)p, w=(lam/2-1)p, g(sp)=|s|h with h=(p1^2+p2^2)/(2|p|), so L=|lam^2-4| h^2 (0 at lam=+-2). Not proved by hand for all lam; numerics only. Hand-checked cases: lam=0 gives L=s^2/(s+z) vs RHS s-z (s=p1^2+p2^2, z=p3^2): L-RHS=z^2/(s+z)>=0, exactly tight when p3=0 (L=RHS=p1^2+p2^2). At lam=+-2, RHS=-2s-4z <=0 = L.
Numeric L matched analytic formulas: max |L-an|/(1+L) = 4.3e-16 (A), 1.0e-12 (B).

## Numerics
A: violations = 0. min(L-RHS)=0 at p=q=0 (forced sample). 62438 samples have L-RHS<1e-9, mostly because tiny t (1e-8 scale) makes absolute slack tiny; this is scale effect, only exact zero is p=q=0.
B: violations = 0. min(L-RHS)=0 at p=0 (5% of samples forced p=0), q=0. 10416 samples with slack<1e-9 (p=0 or tiny p). Genuine tightness exists analytically at lam=0, p3=0 (random sampling hit p3=0 only never; not sampled).
Failed predicates: none. Caveat: the sampler did not specifically sample lam=0 with p3=0, so that tight family is from the hand derivation, not the run; "tight" counts are absolute-slack and inflated by small scales.
