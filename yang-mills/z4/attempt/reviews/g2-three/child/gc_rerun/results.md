# Results (N=2000000, seed 12345, Euler angles)

control I1(1)/I0(1) = 0.446390
max |det-1| (sample) = 6.66e-16

Haar check <|TrU|^2> = 1.00077 +- 0.00071 (expect 1)
Haar check <chi_1> = 0.00077 +- 0.00071 (expect 0)

beta=1: Z = 0.176840 +- 0.000126 ; X = 0.014773 +- 0.000329
beta=0.01: Z = 0.977807 +- 0.000008 ; X = -0.000542 +- 0.000699
beta=0.001: Z = 0.997753 +- 0.000001 ; X = 0.000183 +- 0.000707

FAILED P0: control 0.446390
FAILED P2: beta=0.01 Z=0.977807+-0.000008 (2946.5 se from 1)
FAILED P2: beta=0.001 Z=0.997753+-0.000001 (2920.1 se from 1)
