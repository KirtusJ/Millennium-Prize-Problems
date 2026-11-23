# Precision needed to test the midpoint from earlier transfer moments

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)  
Research program directed by Kirtus Justus

Let $J$ be the index of the mass-gap clock, $h=\lfloor(J-1)/2\rfloor$ its buffered midpoint, and $D\le J$ the last available moment index. Time separation at index $i$ is $2+2i$. Put $a=\beta^{-1/64}$. Once $D$ exceeds a sufficiently large constant times $J\sqrt a$, the worst-case number of bits of **absolute** precision required per ordinary moment, up to constant factors, is
$$
                         \frac{J^2a}{D}.
$$
The observation model supplies a common worst-case absolute error bound on moments $0$ through $D$. More time coverage reduces the required precision. At $D\asymp J\sqrt a$ the order is $J\sqrt a$ bits. At $D=J$ it is $Ja$ bits. No average-case error model or independence of measurement errors is assumed.

The upper bound applies to the positive buffered measures with the clover clock floor proved in the cited work. It yields vanishing relative error in the midpoint ratio. The lower bound uses two positive spectral controls on the same clock. Even deciding bounded versus divergent ratios can require the stated precision. The controls meet the moment and gap constraints but their realizability as Wilson states is open. [G4’s merged certificate](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/991672eab6a83cf3301b47a9f6f5aee27787aa9d/yang-mills/g4/site-clock/certificate.md) · [C4’s exact-prefix pair](../exact-clock-moments/README.md)

## A finite upper bound from a strided subsequence

Let $M_i=\int_{[0,1]}u^i\,d\nu$, with $M_0\le B$ and $M_J\ge F>0$. Both targets $j=h,J$ then have $M_j\ge F$. Take a relative tolerance $0<\epsilon\le1$, $\mathcal L=\log(16B/(\epsilon F))$, and an integer $4\sqrt{J\mathcal L}\le D\le J$. Use the **same** stride for both targets,
$$
 s=\left\lfloor\frac{D^2}{16J\mathcal L}\right\rfloor,\qquad
 q=\lfloor j/s\rfloor,\qquad r=j-sq,\qquad
 d=\min\big(q,\lfloor(D-r)/s\rfloor\big).
$$
With $v=u^s$, the moments at $r,r+s,\ldots,r+sd$ are ordinary moments in $v$ of the pushforward of $u^r d\nu$. Its mass is at most $B$ and the desired moment is its $q$th. Thus any remainder of $j$ modulo $s$ is accounted for exactly. Multiplying the polynomial by $u^r$ neither increases its uniform error nor amplifies its coefficients. At $r=0$ use $u^0=1$ even at zero.

For $q\ge1$, the degree-$d$ shifted Chebyshev truncation of $v^q$ has error at most $2e^{-d^2/q}$ and coefficient absolute sum at most $\alpha^d$, $\alpha=3+\sqrt8$. To see this, expand $\cos^{2q}(t/2)$ with $v=(1+\cos t)/2$. The omitted Chebyshev weights sum to a two-sided binomial tail. Each shifted basis polynomial of degree $k$ has alternating monomial coefficients with absolute sum $T_k(3)\le\alpha^k$. At $d=q$ the polynomial is exact; at $q=0$ the target is a directly supplied moment. [Sachdeva and Vishnoi, §3](https://sachdevasushant.github.io/pubs/fast-algos-via-approx-theory.pdf) · [G4’s exact shifted coefficients](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/991672eab6a83cf3301b47a9f6f5aee27787aa9d/yang-mills/g4/site-clock/certificate.md)

Here $1\le s\le D/16$ and $s\ge D^2/(32J\mathcal L)$. Therefore $d\le32J\mathcal L/D$. If $d<q$, then $d\ge D/s-2\ge D/(2s)$ and $q\le J/s$, giving $d^2/q\ge D^2/(4sJ)\ge4\mathcal L$. With input intervals of radius at most $\delta$, termwise interval evaluation and the polynomial remainder give an interval of width at most
$$
             2\delta\alpha^d+4B e^{-4\mathcal L}
$$
for either target. The remainder term can be omitted for an exact polynomial. It suffices that $\delta\le(\epsilon F/16)\alpha^{-32J\mathcal L/D}$. Then the width is less than $\epsilon F/2$; since the true value is at least $F$, the upper-to-lower quotient is at most $1+\epsilon$. Dividing the two enclosures gives a ratio interval of upper-to-lower quotient at most $(1+\epsilon)^2$.

For the clover floor take $B=O(1)$ uniformly bounded above, $F=c_0\beta^{-1/8}\exp(-C_0 Ja)$, and $\epsilon=\beta^{-p}$ for fixed $p>0$. The bound $J\gtrsim\beta^{1/7}$ implies $\log\beta=o(Ja)$. Thus $\mathcal L=O_p(Ja)$, and a sufficiently large constant multiplying $J\sqrt a$ ensures the hypothesis on $D$. A radius $\exp[-C J^2a/D]$ suffices for a large enough fixed $C$, since $Ja\le J^2a/D$. The finite result uses certified input bounds or explicit floor constants to select its stride. The rate alone does not provide numerical Wilson covariances.

## A lower bound at the same time cutoff

Use the previously constructed pair with $m=\beta^{-1/7}$ and identical $M_0,\ldots,M_k$, where $k=\lfloor\kappa J\sqrt a\rfloor$ for any fixed $0<\kappa<1/4$. They have a common mass bounded by a fixed $B$, can be normalized to the reference mass, satisfy the same clock floor with suitable constants, and approach midpoint ratios $\sqrt e$ and infinity. Both approximate every free clover moment to $O(\beta^{-1/8})$. Write $\Delta\nu$ for their difference. For $i>k$ it annihilates the degree-$k$ truncation of $u^i$, so
$$
 |\Delta M_i|\le \|\Delta\nu\|_{\rm TV}\,2e^{-k^2/i}
                  \le 4B\,e^{-k^2/D}\qquad(k<i\le D).
$$
The earlier differences are exactly zero. Hence for all indices at once there are common intervals of radius $2B e^{-k^2/D}$ containing both sets of moments. This step also covers queries chosen after previous answers. Each query receives the very same admissible interval under both measures. For large $J$ the displayed radius is bounded by $\exp[-cJ^2a/D]$ for some $c>0$, uniformly over $k<D\le J$. Thus an error allowance of that latter size can still conceal opposite midpoint limits. The difficulty persists when the common gap is provided exactly. [Positive pair and free-reference assumptions](../exact-clock-moments/README.md)

Together these statements determine the order of $\log(1/\delta)$ up to multiplicative constants for the specified worst-case guarantee. For $D\le k$ no increase in precision separates that pair. The transition constants, optimal sampling indices, effects of stochastic errors and any improvement using additional Wilson identities remain open. The general ill-posedness of reconstructing a density from Hausdorff moments concerns a different target. [Gerth, Hofmann, Hofmann and Kindermann](https://arxiv.org/abs/2104.06029)

## Calculator and checks

Run the calculator as follows from this directory in a checkout containing G4’s merged calculator.

~~~sh
python stride.py input.json
python check.py
~~~

The JSON input has a positive integer field named "target_index", a positive integer "stride", and "moments", an ordered list of inclusive endpoint pairs beginning with $M_0$. Use integers or quoted rational or decimal strings. The stride may run up to the length of the usable prefix. The implementation reuses G4’s exact-rational interval procedure on each residue subsequence. It returns a null ratio when the clock lower bound is zero.

The checker tests 989 exact rational enclosures using a measure with an atom at zero and verifies that stride one reproduces G4’s routine. A separate degree-three extrapolation pair tests the lower-bound inequality at every index through 79. For $J=4099$, $D=1100$ and stride eight, intervals of radius $10^{-120}$ around the uniform measure’s moments give a ratio interval of relative width $1.10\times10^{-14}$ or less. This is a calculator test with known moments.

Two three-generation PCP OS deployments checked a binomial tail count, 47,840 integer stride and residue cases, and a lifted polynomial identity. Four supporting Lean statements passed, three altered statements and an invalid guest request failed in each run. The general estimates above are written proofs. [Calculator](stride.py) · [Numerical and rational checks](check.py) · [Native worker](worker.c) · [Lean read-back](ClockPrecision.lean) · [Replay](verify.py) · [Receipts](receipts.zip)
