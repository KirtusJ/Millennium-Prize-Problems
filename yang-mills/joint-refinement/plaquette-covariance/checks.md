# Mathematical controls and replay

### Compact and Gaussian comparisons

An interacting $\mathbb Z_2$ Wilson check on the $4\times2\times2$ periodic cubic complex enumerates $2^{18}$ closed surfaces. The independent generators are all but one elementary cube boundary and the three wrapping sheets. The character expansion weights each active face by $\tanh b_j$. Inserting a face toggles its membership, and inserting the same face twice gives one. The check builds the full equal-time/Euclidean covariance kernel for each orientation, tests every transverse Fourier sequence for positivity and monotonicity, and compares the largest eigenvalue with the zero mode. For couplings $(0.31,0.46,0.53)$ the three maxima are 0.12833564, 0.19298808 and 0.24579260. Two of the marked face orientations straddle the longest transfer direction. This finite-group, three-dimensional control checks the spectral reasoning independently of the four-dimensional SU(2) sampler. It also tests the contact value. [Enumerator and packet geometry](controls.py)

For the quadratic Wilson comparison keep the nonzero spatial modes and three independent colors in infinite Euclidean time. Write $s_i=4\sin^2(p_i/2)$ and $s=\sum_i s_i$. For a fixed spatial orientation $ij$ the Fourier coefficient of the equal-time curl covariance is $g=(s_i+s_j)/\sqrt{s(s+4)}$ for $s>0$, with $g(0)=0$. This follows by integrating $(s_i+s_j)/(s+4\sin^2(\omega/2))$ in temporal momentum. At lag $t$ multiply by $e^{-tE}$ where $E=2\operatorname{arsinh}(\sqrt s/2)$. For $O=\sum_{a=1}^3 F_a^2/2$, Wick’s formula gives
$$
 \widehat G(q)=\frac{3}{2N^3}\sum_p g(p)g(p-q),\qquad
 \widehat H(0;t)=\frac{3}{2N^3}\sum_p g(p)^2e^{-2tE(p)} .
$$
Cauchy–Schwarz puts the maximum at zero, both at equal time and at positive time. On every even grid of side at least two, each equal-time eigenvalue is between $1/64$ and $3/2$. The one-dimensional translation by half the period negates the cosine, so at least half the indices have nonpositive cosine. At side six these are indices 2, 3 and 4. A PCP challenger counted only two. Consequently on at least three quarters of the even-grid momenta one of the two relevant cosines is nonpositive, so $s_i+s_j\ge2$ and $g\ge1/\sqrt{48}$. This set and any one translate overlap on at least half the modes. For $t=N$ and shortest integer wave index $h$, $g\le\pi|h|/N$ and $NE\ge2|h|$. Thus the full raw transmitted covariance norm in this model is $O(N^{-5})$ by summation against $|h|^2e^{-4|h|}$. This is a fixed-color free-field comparison. Projecting onto the coarse algebra changes transmitted covariances, and removing the compact zero modes changes the interacting theory. [Z4’s Gaussian observable read-back](../../z4/attempt/reviews/l1-mcw/report.md) · [Earlier Gaussian coarse-space calculation](../fine-states/gaussian.md)

| $N$ | Gaussian equal-time $\chi$ | $N^5\widehat H(0;N)$ |
|---:|---:|---:|
| 2 | 0.43750000 | 0.00587732 |
| 8 | 0.42201697 | 0.00032077 |
| 32 | 0.42193487 | 0.00021594 |
| 64 | 0.42193480 | 0.00021145 |

The same script checks both sharp block inequalities on matrices of the form $D^{1/2}ww^*D^{1/2}$. A signed checkerboard sequence violates the variation ceiling when the midpoint covariance is negative. The Wilson derivation supplies the missing nonnegativity through the positive transfer and the reflected marked kernel. The two spectator countermodels, on the original filters and on the actual packet subspace, have a separate executable. [Spectator controls](audit_controls.py)

### Reproduction

Use Python with NumPy. The signed comparison also requires the dependencies of Z4’s sampler, including SciPy. These commands read the deposited data and evidence from this directory.

~~~text
python controls.py
python audit_controls.py
python spectra.py
python spectra.py --extent 10
python signed.py
python verify.py
~~~

To regenerate spatial fields, build the instrument and use a new output filename. For the original $6N$ open extent, the base seed is $194223+1435N$ and the four streams add $12007i$ for $i=0,1,2,3$. The $10N$ check uses $2432111+2143N+13883i$ at sides 6 and 10. The hot flag is $i\bmod2$. Couplings appear in the reduction script. Use 384 discarded cycles at $6N$, 512 at $10N$, and 320 saved configurations with a three-cycle stride. A binary64 record contains the three fine energies at each spatial site in $x$-fast order followed by the three coarse sums. The archive retains per-configuration sufficient statistics for every result reported here. For example:

~~~text
rustc --edition=2021 -O measure.rs -o measure
./measure 6 3.276133577 202833 0 384 320 6_202833.bin
./measure 6 3.276133577 2444969 0 512 320 6_2444969.bin 10
python spectra.py --pack /path/to/original/fields --archive original-replay.npz
python spectra.py --extent 10 --pack /path/to/longer/fields --archive longer-replay.npz
~~~

### PCP and Lean scope

Enterprise PCP builders and challengers investigated spatial transfer positivity, the coarse block inequality, pressure curvature and anisotropic tuning. Exact manuscript challenges cover the two supplied objections and the treatment of the physical clock. The archived records include the initial objections about midpoint positivity and the distinction between a per-regulator positive-measure tuning set and a common isotropic trajectory. The analytic proofs address these separately. These are same-provider reviews.

Three native PCP guests emitted the Lean source and the hosted compiler checked seven declarations with Lean 4.19 and mathlib. They verify the finite symmetric row estimate, the eight-corner isometry for complex coefficients, variance deficit algebra, mixed compression scalar bound, same-coefficient relative deficit, invariance of a sliding-mode quotient under common rescaling, and the scalar coupling ceiling. Two false mutations are rejected. The Wilson transfer construction, pressure estimate, conditional geometry and measure limits are manuscript arguments. Add the following arguments to replay each PCP register against the calibrated Enterprise method and its stored objects. [Lean](Covariance.lean) · [Evidence archive](evidence.zip) · [Verifier](verify.py)

~~~text
python verify.py --runtime /path/to/PCP_OS_Python --method /path/to/Method
~~~
