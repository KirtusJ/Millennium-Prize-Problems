# Where an upper bound for the raw variance must enter

For one fixed orientation let $B(L_1,L_2,L_3)$ be the variance of the centered sum of the elementary $X_x$ over a rectangular block, divided by its number of sites. Use the same isotropic vacuum regulator in every block. For a cube write $B(L)$, and set $L_j=\min(2^j,N)$ through the first $L_J=N$. Then
$$
 \chi=B(1)+\sum_{j=0}^{J-1}\Delta_j,\qquad
 \Delta_j=B(L_{j+1})-B(L_j)\ge0 .
$$
The contact $B(1)\le K$ is already uniform. The open estimate is a uniform bound on the **sum** of the increments. A regulator-independent summable envelope for them suffices. This formulation does not require a sign for the connected covariance of two plaquettes at arbitrary displacement.

To increase one side $L$ at a time, keep the transverse block fixed and write $Y$ for its centered sum divided by the square root of its transverse area. By the [spatial transfer calculation, including crossing faces](../plaquette-covariance/README.md), $c_r=\mathbb E[\bar Y\,\tau_rY]$ is real and nonnegative at every longitudinal displacement. Counting ordered pairs gives
$$ B(L,\ldots)=c_0+2\sum_{r=1}^{L-1}(1-r/L)c_r.$$
All old weights increase and the new weight is nonnegative, including across the periodic seam. At a doubling $2L\le N$ the increment in this coordinate is exactly $\operatorname{Cov}(Q_0,Q_L)$ for adjacent length-$L$ blocks with their sums individually normalized by the square root of the block volume. Successively increase the three coordinates; the last truncated step uses the original pair formula. The sum of increments telescopes separately on each regulator.

By spatial translation the Fourier eigenvalues $\lambda(q)$ of the covariance are nonnegative. The cube formula is
$$ B(L)=V^{-1}\sum_q\lambda(q)\prod_{i=1}^3 L^{-1}\left|\sum_{a=0}^{L-1}e^{iaq_i}\right|^2 .$$
The zero term alone gives $(L/N)^3\chi\le B(L)\le\chi$, the latter by monotonicity. A uniform estimate at a single fixed positive fraction of the side would suffice. A uniform estimate at a fixed number of sites has no such consequence. Finite-volume plaquette generating-function bounds in the literature have a different choice of group, observable or source. No extensive equal-time estimate for this SU(2) scalar energy is imported from them. [Faria da Veiga and O'Carroll](https://arxiv.org/abs/2205.07376) · [Lüscher](https://doi.org/10.1007/BF01614090) · [Haar identities for Wilson link variables](https://arxiv.org/abs/2608.05415)

### Matched finite-slab observations

Each row uses the deposited single-orientation power spectrum, averaged under cubic rotations and over the two measurement slices. The zero-momentum power is centered with the common measured mean before applying the window. Errors on **increments** are paired delete-one-stream jackknife errors, four independent streams per preparation. All central increments are positive; the largest-scale increments have the largest relative uncertainties. These open-boundary measurements characterize the preparations at sides 6, 8 and 10. They have no supplied uniform bound on the vacuum bias or on later increments. [Source ensembles and matching](../plaquette-covariance/measurements.md) · [Fourier and overlap-count reproduction](blocks.py)

|Time extent|Side|Contact|1→2|2→4|4→min(8,N)|8→10|Full variance per spatial site|
|---:|---:|---:|---:|---:|---:|---:|---:|
|6N|6|.41531(93)|.02407(58)|.0133(28)|.0104(74)| |.4631(100)|
|6N|8|.41224(77)|.02448(59)|.0130(16)|.0122(73)| |.4619(90)|
|6N|10|.41005(68)|.02438(31)|.01437(16)|.0062(44)|.0055(50)|.4606(91)|
|10N|6|.41363(73)|.02365(55)|.0138(22)|.0108(92)| |.4619(112)|
|10N|10|.41115(38)|.02428(34)|.01309(55)|.0082(43)|.0093(41)|.4660(79)|

The plug-in squared mean has finite-sample bias. Replacing it by the average of products of means from distinct streams increases the full variances in table order by 0.000286, 0.000179, 0.000274, 0.000122 and 0.000076. For independent streams with the same population mean the cross-stream product is unbiased for its square. Their hot and cold starts also leave a possible preparation difference. A block of side $L$ receives precisely $(L/N)^3$ of the zero-mode correction.

### A failure test for every submacroscopic support size

Fix integers $1\le s_N=o(V)$, possibly growing arbitrarily close to volume order. There is an isotropic, reflection-positive nearest-neighbour Gaussian action on $N^3\times\mathbb Z$ and a bounded centered site observable with vanishing variance on **every** deterministic unit coefficient vector supported on at most $s_N$ sites, while the variance per spatial site of its full sum diverges. This tests the inference from local information to a uniform ceiling. The action and observable in this example are scalar.

Take $D_N=\sqrt{V/s_N}$, $A_N=N^{-4}$, $m_N=A_N/(2D_N)$ and action $\sum_{x} (m_N^2\phi_x^2+\sum_{\mu=1}^4(\phi_{x+\hat\mu}-\phi_x)^2)/(2A_N)$, interpreted by the infinite-time Gaussian limit. The usual time reflection through a bond has a cross weight $\exp(\phi_-\phi_+/A_N)$ with a positive power-series pairing. Every regulator has positive mass. Integrating the time momentum gives the equal-time covariance symbol
$$ \hat g(q)= A_N/\sqrt{u_q(u_q+4)},\qquad u_q=m_N^2+4\sum_i\sin^2(q_i/2). $$
The eigenvalue at zero momentum is asymptotic to $D_N$. For $q\ne0$, $\hat g(q)\le C N A_N$ by the lowest nonzero lattice momentum. Thus the covariance at contact is $g(0)\le D_N/V+C N A_N=o(1)$. In position space $0\le g(x)\le g(0)$ by the positive random-walk expansion of the massive inverse and Cauchy–Schwarz.

For $Y_x=\sin\phi_x$, Gaussian integration gives $C_Y(x)=e^{-g(0)}\sinh g(x)$. For large $N$ this lies between $e^{-g(0)}g(x)$ and $2g(x)$ entrywise. For a supported vector $c$ of unit Euclidean norm use $|c_x|$ before this entrywise comparison. Its squared overlap with the normalized constant vector is at most $s_N/V$. Splitting off zero momentum gives
$$ \operatorname{Var}\sum c_xY_x\ \le 2[D_Ns_N/V+C N A_N]=o(1),\qquad
 \chi_Y\ge e^{-g(0)}\hat g(0)\longrightarrow\infty .$$
Adding independent centered unit signs at each spacetime site preserves reflection positivity and boundedness and adds exactly one to every normalized variance. The example then looks like unit white noise to every one of these tests and still has diverging $\chi$. Additional Wilson-specific information is required to exclude this behavior. [Executable controls](controls.py)

For G4 and Z4 the unresolved quantity can now be measured at each doubling as an adjacent-block covariance. A pointwise Wilson bound summable over those doublings would settle the raw upper estimate. In the [quadratic Wilson comparison](quadratic-tail.md) the bound on the missing tail is $9\pi/(2L)$ at every side and block length.
