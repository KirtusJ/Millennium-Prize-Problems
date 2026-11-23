# T124 results (exact Gaussian, 2x2x2xT; no Monte Carlo)

Method: per colour phi=sqrt(beta)*theta ~ N(0,P), P projector on range(B); X=(1/2)sum_a phi^T M phi => <X>=1.5 tr(MP), Cov=1.5 sum P_pq^2. P from exact time-Fourier blocks (48x32). T->infinity = T=512 (time-direction transfer-matrix gap makes finite-T error ~e^{-3.5T}; T=32..512 agree to 1e-17 for ratios, so extrapolation is trivial). Colour sum included (3 colours).

## Q1  C_X(0) and C_X(t)/C_X(0)

C_X(0) (T=32,48,64,512): S: 3.5/3.5/3.5/3.5; A1: 12.75/12.75/12.75/12.75; E: 3.125/3.125/3.125/3.125  (exact rationals 7/2, 51/4, 25/8; differences <=1e-14, roundoff)

### T=32

| t | S | A1 | E |
|---|---|---|---|
| 0 | 1.000000000000e+00 | 1.000000000000e+00 | 1.000000000000e+00 |
| 1 | 1.772599481725e-02 | 1.610170542690e-02 | 1.883051160269e-02 |
| 2 | 4.198088516466e-04 | 3.595403283524e-04 | 4.607914474866e-04 |
| 3 | 1.140744607211e-05 | 9.527461481374e-06 | 1.268583559382e-05 |
| 4 | 3.265686469808e-07 | 2.702564390482e-07 | 3.648609483750e-07 |
| 5 | 9.521436373542e-09 | 7.854418961947e-09 | 1.065500821343e-08 |
| 6 | 2.793599748534e-10 | 2.301951504834e-10 | 3.127920554240e-10 |

### T=48

| t | S | A1 | E |
|---|---|---|---|
| 0 | 1.000000000000e+00 | 1.000000000000e+00 | 1.000000000000e+00 |
| 1 | 1.772599481725e-02 | 1.610170542690e-02 | 1.883051160269e-02 |
| 2 | 4.198088516466e-04 | 3.595403283524e-04 | 4.607914474866e-04 |
| 3 | 1.140744607212e-05 | 9.527461481374e-06 | 1.268583559382e-05 |
| 4 | 3.265686469810e-07 | 2.702564390483e-07 | 3.648609483752e-07 |
| 5 | 9.521436373554e-09 | 7.854418961957e-09 | 1.065500821344e-08 |
| 6 | 2.793599748559e-10 | 2.301951504860e-10 | 3.127920554278e-10 |

### T=64

| t | S | A1 | E |
|---|---|---|---|
| 0 | 1.000000000000e+00 | 1.000000000000e+00 | 1.000000000000e+00 |
| 1 | 1.772599481725e-02 | 1.610170542690e-02 | 1.883051160269e-02 |
| 2 | 4.198088516466e-04 | 3.595403283524e-04 | 4.607914474866e-04 |
| 3 | 1.140744607211e-05 | 9.527461481374e-06 | 1.268583559382e-05 |
| 4 | 3.265686469809e-07 | 2.702564390483e-07 | 3.648609483751e-07 |
| 5 | 9.521436373548e-09 | 7.854418961953e-09 | 1.065500821343e-08 |
| 6 | 2.793599748522e-10 | 2.301951504827e-10 | 3.127920554234e-10 |

### T=512 (= T->inf)

| t | S | A1 | E |
|---|---|---|---|
| 0 | 1.000000000000e+00 | 1.000000000000e+00 | 1.000000000000e+00 |
| 1 | 1.772599481725e-02 | 1.610170542690e-02 | 1.883051160269e-02 |
| 2 | 4.198088516466e-04 | 3.595403283524e-04 | 4.607914474866e-04 |
| 3 | 1.140744607212e-05 | 9.527461481374e-06 | 1.268583559382e-05 |
| 4 | 3.265686469810e-07 | 2.702564390483e-07 | 3.648609483752e-07 |
| 5 | 9.521436373542e-09 | 7.854418961948e-09 | 1.065500821343e-08 |
| 6 | 2.793599748614e-10 | 2.301951504906e-10 | 3.127920554340e-10 |

Note: at T=32/48/64 the three tables are identical to ~1e-17 relative; difference from T->inf is not resolvable in double precision for t<=6.

## Q2  single plaquette (T->inf)

Spatial plaquette (any of 12,13,23; spread over sites/orientations 6.7e-16): P_pp = 0.4530696241773; mean = 1.5 P_pp = 0.679604436266; variance = 1.5 P_pp^2 = 0.307908126528. These are T-independent (T=16..512 identical to 1e-12).
Temporal-type plaquette (for reference): P_pp(T) = 0.5469303758227 - 1/(8T) (checked T=16..256), limit mean 0.8203955637, variance 0.4486992540. Sanity: spatial+temporal P_pp average = 1 (tr P/(plaquettes) = 1/2 asymptotically).
Mean of O_12 = 8*mean = 5.4368354901.

## Q3  spectrum, T->inf

Spectrum (checked by exact-fit, residual 6e-16): E_m = 4 asinh(sqrt m) (two photons of equal spatial momentum, phat^2=4m), E_1=3.5254943481, E_2=4.5848633391, E_3=5.2678315877. Three terms reproduce C(t) t=0..8 to 6e-16 relative.

| X | w_1 (abs) | w_1/C(0) | w_2 | w_2/C(0) | w_3 | w_3/C(0) |
|---|---|---|---|---|---|---|
| S | 1.5 | 0.4285714286 (1.5/3.5) | 1.5 | 0.4285714286 | 0.5 | 0.1428571429 |
| A1 | 4.5 | 0.3529411765 (4.5/12.75) | 6 | 0.4705882353 | 2.25 | 0.1764705882 |
| E | 1.5 | 0.4800000000 (1.5/3.125) | 1.25 | 0.4000000000 | 0.375 | 0.1200000000 |

E1 is the same for S, A1, E: 3.5254943 (auditor's 3.52549435 agrees to 2e-9, rounding). Weights: w1/C(0) = 3/7=0.428571 (S), 6/17=0.352941 (A1), 12/25=0.48 (E). Auditor's 0.046875 = 3/64 matches NONE of these normalised weights. It equals w_1(S)/32 = 1.5/32, i.e. the single-orientation absolute weight 1.5 divided by 32; no definition in the task gives that normalisation (my reading: unverified guess).
