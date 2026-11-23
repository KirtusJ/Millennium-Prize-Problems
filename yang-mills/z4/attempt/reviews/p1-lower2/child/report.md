# T147 report
control.txt = 4.60541 (c*, independently recomputed by P1 with 800-pt GL and by grandchild T148).

## Verdicts
Counts: **met 76, failed 0, measured only 36**.
Met = P1 (1) + P2 (1) + grandchild moment check (1) + P5 ESS (36 cases) + P3 (36 cases) + P4 (1). Measured only = the 36 values of -log R and diff in the table. Failed predicates: none.

- P1 control reproduced: 4.60541319 -> file 4.60541 (checks.txt).
- P2 sampler mean cos(theta) beta=256, 2e5 draws: 0.994129 vs exact 0.994146, z=-1.61, tolerance 4 SE (~6e-5 normal tail) (checks.txt).
- Grandchild (T148, grandchild/result.md): E[cos]=I0/I1-2/beta=0.994146369513, I2/I1 agrees 3.7e-15; sample 0.99414085 SE 4.8e-6, 1.15 SE; MET. I reran its run.py in a copy: same numbers.
- P5 hypothesis (rule 4) 'weights usable, ESS>=1000': 36/36 cases qualify, min ESS 1890 (the a1=pi/2 points are the noisiest). Tolerance 1000: my own choice.
- P3 |diff| <= 5 SE + 2/sqrt(beta): met 36/36. 5 SE is statistical; the 2 is my own expectation for the O(beta^-1/2) coefficient, not derived.
- P4 sqrt(b)|diff| bounded: max over points 2.066 (256), 2.316 (1024), 2.606 (4096); met against 1.5x + 3SE-slack. Caveat: slack (~3.6) is large, so P4 is weak; the max at 4096 (a1=pi/2,c=0.1,y=1) is 1.7 SE from the sqrt(b)*diff=2.0 level. Looks bounded (~2 in magnitude), not shrinking; diff itself clearly shrinks: worst |diff| 0.129 / 0.072 / 0.041, i.e. ratio ~1.8 per factor-4 in beta (~sqrt 4 = 2).
- Systematic observation (measured): at a1=0.5, diff > 0 and sqrt(b)*diff ~ 1.2-2.3 well beyond SE (~0.005*sqrt(b)=0.1-0.3) - a genuine O(beta^-1/2) correction with positive coefficient; at a1=2.5 the sign is negative (~-1 to -1.7). Prediction pred holds only to leading order. At a1=pi/2 diff is within noise.

## Table (N=4e5 samples per point, SE of -log R by delta method)
| beta | a1 | c | y | -log R | pred | diff | sqrt(b)*diff | SE | ESS |
|---|---|---|---|---|---|---|---|---|---|
| 256 | 0.500000 | 0 | 0 | 0.124817 | 0.000000 | 0.124817 | 1.9971 | 0.003902 | 56408 |
| 256 | 0.500000 | 0 | 1 | 0.092557 | 0.007301 | 0.085256 | 1.3641 | 0.004438 | 45054 |
| 256 | 0.500000 | 0.1 | 0 | 0.147642 | 0.018510 | 0.129133 | 2.0661 | 0.003962 | 54965 |
| 256 | 0.500000 | 0.1 | 1 | 0.107559 | 0.025582 | 0.081976 | 1.3116 | 0.004443 | 44961 |
| 256 | 1.570796 | 0 | 0 | 0.000708 | 0.000000 | 0.000708 | 0.0113 | 0.016136 | 3804 |
| 256 | 1.570796 | 0 | 1 | -0.013688 | 0.002755 | -0.016442 | -0.2631 | 0.015962 | 3887 |
| 256 | 1.570796 | 0.1 | 0 | 0.018070 | 0.007021 | 0.011049 | 0.1768 | 0.013379 | 5510 |
| 256 | 1.570796 | 0.1 | 1 | -0.021343 | 0.009737 | -0.031081 | -0.4973 | 0.022945 | 1890 |
| 256 | 2.500000 | 0 | 0 | -0.081632 | 0.000000 | -0.081632 | -1.3061 | 0.006822 | 20394 |
| 256 | 2.500000 | 0 | 1 | -0.088995 | 0.005574 | -0.094569 | -1.5131 | 0.008891 | 12261 |
| 256 | 2.500000 | 0.1 | 0 | -0.093013 | 0.014166 | -0.107179 | -1.7149 | 0.007550 | 16807 |
| 256 | 2.500000 | 0.1 | 1 | -0.065329 | 0.019608 | -0.084938 | -1.3590 | 0.010313 | 9186 |
| 1024 | 0.500000 | 0 | 0 | 0.072375 | 0.000000 | 0.072375 | 2.3160 | 0.004224 | 49160 |
| 1024 | 0.500000 | 0 | 1 | 0.046078 | 0.001834 | 0.044244 | 1.4158 | 0.004908 | 37615 |
| 1024 | 0.500000 | 0.1 | 0 | 0.079467 | 0.018510 | 0.060958 | 1.9506 | 0.004257 | 48501 |
| 1024 | 0.500000 | 0.1 | 1 | 0.070690 | 0.020286 | 0.050404 | 1.6129 | 0.004667 | 41182 |
| 1024 | 1.570796 | 0 | 0 | 0.011696 | 0.000000 | 0.011696 | 0.3743 | 0.013414 | 5482 |
| 1024 | 1.570796 | 0 | 1 | -0.014829 | 0.000690 | -0.015519 | -0.4966 | 0.018121 | 3022 |
| 1024 | 1.570796 | 0.1 | 0 | 0.007407 | 0.007021 | 0.000386 | 0.0124 | 0.014261 | 4857 |
| 1024 | 1.570796 | 0.1 | 1 | 0.038213 | 0.007702 | 0.030512 | 0.9764 | 0.014951 | 4424 |
| 1024 | 2.500000 | 0 | 0 | -0.055513 | 0.000000 | -0.055513 | -1.7764 | 0.006973 | 19561 |
| 1024 | 2.500000 | 0 | 1 | -0.036412 | 0.001399 | -0.037811 | -1.2099 | 0.007918 | 15339 |
| 1024 | 2.500000 | 0.1 | 0 | -0.027391 | 0.014166 | -0.041557 | -1.3298 | 0.006981 | 19518 |
| 1024 | 2.500000 | 0.1 | 1 | -0.013373 | 0.015531 | -0.028905 | -0.9249 | 0.007672 | 16297 |
| 4096 | 0.500000 | 0 | 0 | 0.031622 | 0.000000 | 0.031622 | 2.0238 | 0.004589 | 42439 |
| 4096 | 0.500000 | 0 | 1 | 0.019677 | 0.000459 | 0.019218 | 1.2300 | 0.004952 | 37011 |
| 4096 | 0.500000 | 0.1 | 0 | 0.040132 | 0.018510 | 0.021623 | 1.3839 | 0.004498 | 43995 |
| 4096 | 0.500000 | 0.1 | 1 | 0.038162 | 0.018954 | 0.019208 | 1.2293 | 0.005083 | 35290 |
| 4096 | 1.570796 | 0 | 0 | 0.005625 | 0.000000 | 0.005625 | 0.3600 | 0.014304 | 4828 |
| 4096 | 1.570796 | 0 | 1 | -0.022357 | 0.000173 | -0.022529 | -1.4419 | 0.018878 | 2787 |
| 4096 | 1.570796 | 0.1 | 0 | -0.017319 | 0.007021 | -0.024341 | -1.5578 | 0.018867 | 2790 |
| 4096 | 1.570796 | 0.1 | 1 | 0.047910 | 0.007192 | 0.040719 | 2.6060 | 0.015059 | 4361 |
| 4096 | 2.500000 | 0 | 0 | -0.022365 | 0.000000 | -0.022365 | -1.4313 | 0.006499 | 22354 |
| 4096 | 2.500000 | 0 | 1 | -0.014616 | 0.000350 | -0.014966 | -0.9578 | 0.007750 | 15984 |
| 4096 | 2.500000 | 0.1 | 0 | 0.006035 | 0.014166 | -0.008131 | -0.5204 | 0.006641 | 21461 |
| 4096 | 2.500000 | 0.1 | 1 | 0.008057 | 0.014508 | -0.006451 | -0.4129 | 0.007231 | 18251 |

Worst |diff|: beta=256 0.1291, beta=1024 0.0724, beta=4096 0.0407.

## Method notes
Sampler exactly as specified (Gamma(3/2) + accept sqrt(1-t/2)); R = exp(-V/2) E[exp(-V'/2) phi'/phi] computed in log domain; Psi differences by 32-pt Gauss-Legendre on [a1,a1']. U2 vector part = (d,0,c) direction. Seeds 20260000+k (k=1..36), P2 seed 777.

## Rerun (fresh empty dir; result files open mode x)
cp mc.py p2.py judge.py control.txt <newdir>; cd <newdir>; python3 mc.py; python3 p2.py; python3 judge.py
PCP: P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P check --ws pcp --name mc --expect-exit 0 -- python3 mc.py (also p2, judge)

## PCP verify (last lines)
python verify: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
rust verify: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
