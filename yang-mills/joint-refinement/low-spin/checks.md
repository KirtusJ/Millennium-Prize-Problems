# Matched open slabs and checks

### How much winding variance can pass through the exterior?

Use the three-component cyclic difference $F_i$ of spatially averaged adjoint windings, in G4’s normalization. Let $C_{0,i}$ be its predictor built by averaging only the lines of origin parity zero, with the correct normalized line count. Average the inner products over components. For population quantities in the symmetric open preparation, put $v=\mathbb E F^2$, $d=\mathbb E(C_0-F)^2$, $r_f=\mathbb E|F-\mathbb E[F\mid C]|^2$. Cubic symmetry centers $F$. The mean of the eight parity predictors is $F$ on every configuration. Translation invariance therefore gives $\mathbb E[C_0F]=v$ and the optimal scalar multiple of $C_0$ has squared loss $U=vd/(v+d)$.

For the spatial selection in the [proof](README.md), set $m_F=\mathbb E[F\mid\mathcal E]$ and $J=\mathbb E\operatorname{Var}(F\mid\mathcal E)$. The spectrum of the symmetric two-endpoint pairing is nonnegative by transfer positivity. Conditional independence of the two endpoint sets gives the following **population inequalities**, with $QF$ denoting the residual relative to the open endpoint marginal:
$$
 J\le r_f\le U,\qquad
 0\le \frac{\mathbb E[(QF)_0(QF)_N]}{r_f}
 \le 1-J/r_f\le1-J/U .
$$
The absolute pairing of the normalized residual with any normalized coarse reading is at most $\sqrt{1-J/U}$, by positivity and contractivity of the two-endpoint form. These are statements about this observable and preparations symmetric between the two insertions. They also apply componentwise with that component’s inputs. The table uses direct-sum component averages.

Here $C$ is exterior-measurable because all selected links lie off the even coarse skeleton. With half magnetic weights at the free temporal ends, the bilinear form at the symmetric insertions is proportional to $\langle h g,T^N h f\rangle$, where $h=T^{5N/2}1$. Its positivity follows from $T\ge0$ and its contraction from the equal endpoint marginals and Cauchy–Schwarz.

Conditionally on fixed staples, each erased winding has mean character $\mathbb E\chi_n=(\prod k_n(x_e))\chi_n(w_\mathrm{center})$, where fixed link factors keep their path ordering. Measure its variance using $\chi_2^2=1+\chi_2+\chi_4$ and independence between lines. The variance in each cyclic difference divides the sum of the line variances of its two axes by $9N^4$. The positive Bessel series is evaluated in binary64. This integrates selected links analytically on each saved configuration. [Rust sampler](private.rs) · [NIST series](https://dlmf.nist.gov/10.25.E2)

| Side | Estimated lower endpoint $J/v$ | Estimated upper endpoint $U/v$ | Estimated transmission ceiling $1-J/U$ |
|---:|---:|---:|---:|
| 6 | 0.1708 ± 0.0017 | 0.6270 ± 0.0040 | 0.7276 ± 0.0015 |
| 8 | 0.2652 ± 0.0024 | 0.6949 ± 0.0037 | 0.6184 ± 0.0026 |
| 10 | 0.3475 ± 0.0064 | 0.7229 ± 0.0042 | 0.5192 ± 0.0064 |

These are plug-in estimates with paired, leave-one-stream-out standard errors from four streams per side. They are neither certified bounds on the population values nor vacuum or full-sector estimates. Each stream used the old matched coupling, 384 discarded cycles, alternating hot and cold starts across streams, and 320 saved configurations three cycles apart. The temporal extent was $6N$ steps and insertions were at $5N/2,7N/2$. The full winding agrees with all 23,040 original single-component readings at archived binary32 precision. The independently recomputed origin-zero predictor agrees with the earlier binary64 anchor. [Paired measurements](samples.zip) · [Original matched trajectories](../../g4/full-attempt/physical-refinement/samples.zip) · [Original anchor records](../fine-states/anchors.zip)

### Discrepancies and independent replication

Two statistics vanish in the equilibrium population. The first is $\mathbb E[m_F^2+\operatorname{Var}(F\mid\mathcal E)-F^2]/v$. The second is $\mathbb E[m_{F,0}m_{F,N}-F_0F_N]/v$. The second exceeded three four-stream standard errors at sides 6 and 10, in opposite directions. We therefore reran those exact couplings with six new seeds per side, 512 discarded cycles, 320 saved configurations, and the same stride. The lag discrepancies changed sign at both sizes. The added streams reproduce the conditional-variance fractions. The original deviations remain in the table. The number of independent streams limits precision; a small error on an innovation fraction cannot certify a small error on a lag.

| Ensemble | Side | $J/v$ | Equal-time discrepancy | Two-end discrepancy |
|---|---:|---:|---:|---:|
| Original | 6 | 0.1708 ± 0.0017 | +0.0077 ± 0.0114 | +0.0120 ± 0.0029 |
| Original | 8 | 0.2652 ± 0.0024 | +0.0025 ± 0.0089 | +0.0106 ± 0.0068 |
| Original | 10 | 0.3475 ± 0.0064 | −0.0179 ± 0.0095 | −0.0214 ± 0.0064 |
| New seeds | 6 | 0.1698 ± 0.0027 | +0.0085 ± 0.0065 | −0.0093 ± 0.0078 |
| New seeds | 10 | 0.3449 ± 0.0075 | −0.0141 ± 0.0150 | +0.0089 ± 0.0138 |

A separate fixed-exterior heat-bath control draws the selected links independently on two noncommuting fields. It compares six conditional means, six conditional variances and three two-end residual products at each size against the analytic instrument. Across 8,192 draws per field, the largest standardized discrepancies were 2.14 at $N=6$ and 1.84 at $N=10$, rounded upward. This tests the two-end integration without relying on temporal equilibration of the whole lattice. [Independent streams](replication.zip) · [Read-back](readback.py)

### Grounding and replay

The full-winding analytic estimate already gives $\theta<0.004889$ at $N=2040,\beta=7/2$ by rational arithmetic. This is a fixed-coupling illustration. For the elementary plaquette the all-even worst-case deficit $\delta/K$ is about $9.46\,10^{-17}$, independent of $\beta\ge1$. Positivity of that exact ratio, rather than its difference from one rounded in machine arithmetic, enters the proof. Enumeration checks plaquette incidence, collinear witnesses for each elementary face, winding counts and periodic seams. An independent quaternion calculation rebuilds all twelve face terms after fixing the product of a link pair, and rectangular enumeration checks fourfold face multiplicity. [Geometry and rational arithmetic](geometry.py) · [Plaquette controls](plaquette_check.py)

Run these from this directory with Python and NumPy:

~~~text
python geometry.py
python plaquette_check.py
python readback.py
python verify.py
rustc --edition=2021 --test -O private.rs -o private-tests
./private-tests --nocapture
rustc --edition=2021 -O private.rs -o private
./private 6 3.276133577 202833 0 384 320 replay.bin
~~~

The output is little-endian binary64 in configuration, endpoint, quantity and cyclic-component order. The four quantities are $F,C_0,m_F,\operatorname{Var}(F\mid\mathcal E)$. The first archive uses the production seeds in the anchors archive. For the second use seed $1357001+1123N+15101i$ and hot flag $i\bmod 2$ for $0\le i<6$. The matched couplings are 3.276133577, 3.399810242 and 3.493705679 for $N=6,8,10$.

PCP Enterprise builders and challengers examined temporal-column contraction, coarse prediction, averaging over origins, and the path argument. A temporal-column contraction leaves a conditional mean through the exterior. A single-link heat bath at fixed ordered product can freeze the factors. Averaging projections over origins can still miss a common direction. The paired-link variation and the spatial selection address specific surviving states. The exact analytical and matched-data manuscripts were separately submitted to PCP challengers. These are same-provider reviews. The newer one-site tensor enclosure and its normalization-invariant signed share concern a different regulator. [A4’s one-site disposition](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/19#issuecomment-7112191783) · [G4’s signed normalization follow-up to Z4](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/21#issuecomment-7112060416)

Native PCP guests emitted the source in three parts. Hosted Lean 4.19 checked the rearranged Bessel bound, character identity, complex Hilbert-space pairing after endpoint factorization, and variance-ratio inequality, with two false mutations rejected. The Wilson conditional law, rectangular pressure proof, and its application to all single plaquettes are written proofs. To deep-replay the PCP archives add the two arguments shown below. [Lean source](LowSpin.lean) · [Evidence](evidence.zip) · [Verifier](verify.py)

~~~text
python verify.py --runtime /path/to/PCP_OS_Python --method /path/to/Method
~~~
