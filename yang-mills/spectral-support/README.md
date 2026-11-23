# From Euclidean decay to a continuum spectral gap

Director D4 · 22 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

A bound on a dense family of connected correlations excludes a low-energy band if it holds at arbitrarily late physical times with a shared decay rate. Each observable can have its own prefactor and sequence of times. The Lean result proves this implication for positive spectral measures. Constructing the four-dimensional Yang–Mills theory and deriving that rate for it remain open. [Lean source](SpectralLimit.lean) · [Jaffe and Witten, §4](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## Which estimate would suffice?

Fix a physical time step $\tau>0$, a reconstructed nonnegative self-adjoint Hamiltonian $H$, and an identified vacuum vector. Work in its orthogonal complement. For $T=\exp(-\tau H)$ let $\mu_v$ denote the spectral measure of a centered test vector $v$ for $T$. The spectral variable $x=e^{-\tau E}$ takes values in $[0,1]$. Fix $0<r<1$.

For each vector in a dense set, choose integer times $t_v(n)\to\infty$ and a finite constant $M_v$. At each fixed $n$, require the cutoff correlations $c_{v,k,n}$ to converge as $k\to\infty$ to $\int x^{t_v(n)}\,d\mu_v(x)$. Also require

$$c_{v,k,n}\le M_v r^{t_v(n)}\qquad\text{for all sufficiently large }k.$$

The cutoff at which the estimate starts may depend on $v$ and $n$. The rate $r$ is common to the family, and $M_v$ is fixed across all its times. The proof first takes the cutoff limit at each fixed time. For every $s>r$, positivity then gives

$$\mu_v([s,\infty))\le M_v(r/s)^{t_v(n)}.$$

Sending $n$ to infinity kills this tail. A countable union gives $\mu_v((r,\infty))=0$. At the endpoint, the point mass at $r$ attains the moment bound at every time and has mass one on $[r,\infty)$. Both the open-tail statement and the endpoint example are checked in Lean.

For $P=\mathbf 1_{(r,\infty)}(T)$, the spectral identity gives $\lVert Pv\rVert^2=\mu_v((r,\infty))$. The kernel of $P$ is closed, so density implies $P=0$ on the full vacuum complement. With the stated spectral calculus and physical clock this excludes energies below $-\log(r)/\tau$ in that complement. Lean takes the continuous map, scalar measures and spectral identity as inputs. The Hamiltonian interpretation uses the spectral theorem. An energy-1 eigenvector in direct sum with multiplication by $E$ on $L^2(0,1/2)$ illustrates the density requirement. The eigenvector's correlations decay exactly as $e^{-t}$ while the orthogonal summand contains arbitrarily low positive energies. A separate vacuum can be adjoined.

## What the parent program’s six readings permit

Kirtus Justus’s E1 benchmark samples $1,E,E^2,E^3,2^{-E},4^{-E}$. Its equal-weight probability measure on energies $1,\ldots,6$ has threshold 1. E1 optimizes the largest compatible threshold. Here is the opposite endpoint. The very same six exact values admit a **gapless probability measure with no atom at zero**. [E1, §1 and §3](https://github.com/KirtusJ/From-Prephysical-Hypotheses-to-Physical-Models/blob/aca29276aa180af3c81ccc9f3aa06b4e2ae4d404/edition/PAPERS/E1_Positive_Spectral_Measures_Under_Finite_Moment_and_Laplace_Constraints/source/01_editable_Positive_Spectral_Feasibility.md)

Let $f(E)=(1,E,E^2,E^3,2^{-E},4^{-E})^T$ and let the six columns of $A$ be $f(1),\ldots,f(6)$. Choose the uniform probability measure $\nu$ on $(0,1)$, put $b=\int f\,d\nu$, and set $z=A^{-1}b$. Exact rational elimination gives

$$\det A=-243/32768,\qquad \lVert A^{-1}\rVert_\infty=58492/27.$$

Every coordinate of $b$ lies in $[0,1]$. With $\varepsilon=1/32768$, every corrected anchor weight $1/6-\varepsilon z_j$ is at least $22241/221184>1/12$. Define

$$\mu=\varepsilon\nu+\sum_{j=1}^6(1/6-\varepsilon z_j)\delta_j.$$

Its six readings equal the original six because $\varepsilon b-\varepsilon A z=0$. The first coordinate gives total mass one. It has zero mass at the singleton $\{0\}$ and positive mass $\varepsilon d$ on $(0,d)$ for every $0<d<1$. In particular, its continuum contribution to the Euclidean correlator is $\varepsilon(1-e^{-t})/t$ for $t>0$. These exact observations are compatible with a power-law tail. The argument also works for any probability measure on $(0,1)$ when only the six-reading identity is needed. The interval measure argument is analytic. Its matrix, inverse identity, anchor bound and original readings are checked with rational arithmetic. [Exact checker](check_family.py)

A separate finite Lean control uses weights in units of $1/600$ at energies $0,\ldots,6$. A PCP OS guest obtains the perturbation by multiplying the six factors in $(X-1)^4(2X-1)(4X-1)$. The fourfold root at 1 cancels the four polynomial readings, and the other two roots cancel the Laplace readings.

| Weights | $E=0$ | $E=1$ | $E=2$ | $E=3$ | $E=4$ | $E=5$ | $E=6$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Reference | 0 | 100 | 100 | 100 | 100 | 100 | 100 |
| Alternative | 1 | 90 | 138 | 28 | 173 | 62 | 108 |

Lean computes the four polynomial numerators after scaling by 600, and the two Laplace numerators after scaling by $600\cdot 2^6$ and $600\cdot 4^6$, respectively. The six integers are $(600,2100,9100,44100,6300,136500)$ for both measures. The alternative in this table has a zero-energy atom. The continuous construction above addresses the objection that centering could remove such an atom.

## What the construction still needs

The Lean bridge `decayAtRoundedTime` matches B4’s one-step estimate to physical time. If an excited transfer value satisfies $0\le q\le 1-am$ and $N$ lattice steps cover $t$ so that $Na\ge t$, then $q^N\le e^{-mt}$. For $a>0$ choose $N=\lceil t/a\rceil$. With a positive transfer operator, the spectral theorem and a bound on the regulated norm of each test vector give the scalar envelope. Convergence at those rounded times still needs proof along the chosen trajectory. [B4’s regulator result](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/b31a34c79c81ba627a128ba17fb1a36fba83c39e/yang-mills/transfer-operator)

A4’s nonzero-observable result concerns survival of selected vectors. G4’s reflection-positivity work concerns reconstruction, and C4’s work addresses the quantifier over gauge groups. The next test for this route is a single physical rate on a dense family of centered gauge-invariant states along the same continuum and infinite-volume limit. A rate that deteriorates to zero as the test family grows leaves a gapless sector possible. No rate for interacting four-dimensional Yang–Mills has been derived in this work. [Director rendezvous](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1) · [Execution evidence](execution.md)

A second checked result gives a different route when the actual cutoff spectral measures converge weakly. One cofinal sequence of measured times then suffices for each vector, with just one time per cutoff. Finite-cutoff near-zero modes whose weights vanish are compatible with a gap in the limit. [Proof, hypotheses and controls](diagonal/README.md)

Positive-time correlation limits can also replace weak convergence of finite spectral measures. The physical-time comparison applies with divergent equal-time mass and strengthens the strong-coupling Wilson obstruction to any normalization with finite earlier positive-time correlations. [Positive-time theorem and signed-spectrum test](positive-time/README.md)

For several zero-energy states, the transfer projection above acts on the orthogonal complement of the full kernel of the reconstructed Hamiltonian. Centering against a single vacuum suffices when that vacuum spans the kernel in the chosen sector. A fixed physical time difference gives a test that allows arbitrary zero-energy multiplicity. [Gap above the vacuum sector](positive-time/vacuum/README.md)

The directly measured $SU(2)$ adjoint plaquette retains a positive-energy component at all finite couplings, uniformly in box size at fixed spatial mesh. Its lower window endpoint is at least $\kappa/576$. A selected simultaneous Wilson-time and spatial-volume limit inherits the witness. [Adjoint spectral band and scope](adjoint-band/)
