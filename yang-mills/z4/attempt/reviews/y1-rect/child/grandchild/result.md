# T198 result
u(0.5)=I2/I1=0.12371793  u^2=0.01530613
## beta=0.5, 2^4 periodic, heatbath, 4000 sweeps hot + 4000 cold (300 thermalization each), 20 bins
hot  W11=0.12488 +- 0.00087
cold W11=0.12528 +- 0.00066
combined W11=0.12508 +- 0.00054
W11-u = +0.00136 = +2.50 sigma
## beta=0 Haar, 20000 samples
W11=-0.00008 +- 0.00036
W12=+0.00039 +- 0.00034  (on L=2 the 2-step wraps: U_nu(x+2mu)=U_nu(x), so the nu legs cancel and W12 is a trace of 4 distinct links; expectation still 0)
## predicates
P2 beta=0 W11~0 (4 sigma): PASS
P3 beta=0 W12~0 (4 sigma): PASS
P4 beta=0.5 W11==u (4 sigma): PASS
P5 sanity hot/cold agree, 0<W11<0.5: PASS
