# Results (seed 7, beta=1, 2e6 samples = 20 batches x 1e5, self-normalised importance weights)
- pointwise max |sum A^2 - (2+Y^2)| = 3.109e-15
- (a) E[sum A^2] = 2.279665 +- 0.000226; E[2+Y^2] = 2.279665 +- 0.000226
- (b) E[Z] = 0.006215 +- 0.004504 (expect 0)
- E[(Y-EY)Z] = 2.279421 +- 0.001750; E[2+Y^2] = 2.279665 +- 0.000226
- difference = -0.000244, SE(diff, paired batches) = 0.001571, z = -0.16
- ||Z||_L2/beta = 5.133686 +- 0.002191
- E[Y] = 0.240728
- finite-difference check of A_ab (h=1e-4): max err = 5.832e-09
- Verdict: E[(Y-EY)Z] equals E[2+Y^2] within 3 SE? YES
