"""Cold-start check P4 (L=4, beta=0.5, cold start, seed 77): |W11_cold - W11_hot(res/L4_b0.5.txt)| < 3*combined sigma."""
import sys, mc
d = mc.run(4, 0.5, 400, 3000, 77, hot=False)
with open("res/L4_b0.5_cold.txt", "x") as f:
    f.write("L=4 beta=0.5 COLD W11=%.6f +- %.6f W12=%.6f +- %.6f\n" % (d[:,0].mean(), mc.block_err(d[:,0]), d[:,1].mean(), mc.block_err(d[:,1])))
