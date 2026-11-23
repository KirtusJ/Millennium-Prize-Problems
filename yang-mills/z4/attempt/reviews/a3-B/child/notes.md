# notes
control: (2/pi)int exp(2cos a)sin^2 = 2 I1(2)/2 = I1(2)=1.590637 (analytic); numeric midpoint gives 1.590637
S1 whole group max|P-1| = 2.22e-16 -> MET
S2 quad max rel diff 1.43e-14 -> MET
S3 trunc J400 vs J200 max rel diff 0.00e+00; max last-kept denominator term r_J^N 7.57e-71 -> MET
S4 monotone-approach (L=8 closer than L=2): 40/40; failing (beta,delta): []
T1: cases=200, qualify(L even or inf)=200, nontrivial bound (<1)=30, satisfy=200, violate on grid=0, violate on 2e6-grid=0
violations (beta,delta,L): logratio : []
P_inf(beta=16,delta=0.2) = 8.9270835615e-02

