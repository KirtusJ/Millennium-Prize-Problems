# Deterministic mean normalization on a path of fixed physical length

Take a **spatial** straight path in the original isotropic defining $SU(2)$ Wilson law. Every periodic side has dyadic length at least four. The path uses $L$ distinct bonds, with $Lb\to\ell>0$, $\beta\to\infty$, and $L/\beta\to\infty$. Mark $m=\min(L,\lceil\beta^{3/2}\rceil)$ approximately evenly spaced bonds, fixed before observing the field. In an ordered comparison path keep every unmarked bond and replace only the marked ones by their six-staple polar directions. Let $W$ be the original product, $P$ the comparison product and
$$F=\tfrac12\operatorname{Tr}(WP^{-1}),\quad q(r)=I_2(r)/I_1(r),\quad s_0=q(6\beta)^m.$$
This is a bounded gauge-invariant observable. It uses transport down the original path and back through its measured comparison, including temporal staples one lattice step on either side of the slice. It differs from the ordinary, uncompensated Wilson loop. The path covers fixed physical length even on the logarithmic bare trajectory.

Its **ordinary ensemble mean** $M=\mathbb EF$ satisfies $M/s_0\to1$, while $s_0\to0$ and $\operatorname{Var}F\to1/4$. For two time translates on nonadjacent slices, including fixed positive physical separations on a sufficiently long time circle,
$$\frac{\mathbb E[F_1F_2]}{M^2}-1\longrightarrow0.$$
Thus the mean-normalized connected signal vanishes although the mean-normalized equal-time variance diverges. This conclusion uses the four-dimensional interacting measure and two-sided conditional integration. A bound for unit-variance probes alone would not imply it.

## Proof

Expose all links except the marked ones on both paths. The retained bonds are jointly noncofacial; neither set occurs in the other path's staples. The two readings are conditionally independent. For either reading the normalized conditional expectation is
$$s/s_0=\prod_{j\,\mathrm{marked}} [q(6\beta x_j)/q(6\beta)],\qquad x_j=|S_j|/6,$$
where the displayed product means the product of the $m$ ratios. The identity follows by conjugating the independent central fluctuations through the comparison product. It is valid for a single reading with its own marked exterior as well. Monotonicity of $q$ gives $0\le s/s_0\le1$ for **every** exterior.

Choose the good event $1-x_j\le\eta=80\log\beta/\beta$ at every mark on the two paths. By the [site-reflection estimate](crossover.md), the probability of its complement is at most $12m c_0^{-4}e^{48}\beta^{6-80/4}=O(m\beta^{-14})$. Each violated staple needs at least one violated incident plaquette. For large $\beta$ the good radii exceed $3\beta$. The large-$r$ expansion is
$$\log q(r)=-3/(2r)-3/(4r^2)+O(r^{-3}).$$
It follows uniformly there that $0\le\log(s_0/s)\le C m(\eta/\beta+\beta^{-3})=o(1)$. Since $s/s_0$ is always at most one it converges to one in every finite $L^p$. Apply the conditional independence identity to $(s_1/s_0)(s_2/s_0)$ to obtain the claimed deterministic mean normalization. Meanwhile $m/\beta\to\infty$ and $\log s_0\sim-m/(4\beta)$. The character identity $4F^2=1+\chi_2(WP^{-1})$ and $q_2(r)\le q(6\beta)^2$ bound the second term's mean magnitude by $3s_0^2$. This proves the variance assertion. The estimates are uniform in the temporal period, so the same statements pass to the zero-temperature Wilson expectation on a fixed dyadic spatial box at each cutoff. They give neither the sign nor the scale of the first *nonzero* subleading connected term.

## The next centered reading is a local Wilson observable

A second deterministic scaling identifies what would have to survive. For the six unit quaternion staples $S_{ja}$ at mark $j$, define
$$A=\frac{4\beta^2}{m}\left(1-\frac{F}{s_0}\right),\qquad
B=\frac{\beta}{36m}\sum_{j,a<c}\left(1-\tfrac12\operatorname{Tr}(S_{ja}S_{jc}^{-1})\right).$$
Each product of staples is a closed walk of length six. The local $B$ insertion is independent of every marked bond on that straight line. For any two nonadjacent copies,
$$\|\mathbb E[A\mid Y]-B\|_2\to0,\qquad
\operatorname{Cov}(A_1,A_2)-\operatorname{Cov}(B_1,B_2)\to0.$$
Here $Y$ is the common marked exterior. The first formula concerns the conditional reading. The unconditioned $A$ has a large link-noise term.

Indeed for six unit vectors, $36-|\sum_a S_{ja}|^2=\sum_{a<c}|S_{ja}-S_{jc}|^2$. Hence the inner sum divided by 36 equals $(1-x_j^2)/2$ exactly. On the good event, write $D=\log(s_0/s)$. The two Bessel terms give
$$D=\frac1{4\beta}\sum_j(1/x_j-1)+O\big(m(\eta/\beta^2+\beta^{-3})\big).$$
Use $0\le D-(1-e^{-D})\le D^2/2$ and $|(1/x-1)-(1-x^2)/2|\le 3(1-x)^2$ for $1/2\le x\le1$. The absolute error between $\mathbb E[A\mid Y]$ and $B$ there is at most $C((\log\beta)^2/\beta+m(\log\beta)^2/\beta^2)$. On the complement it is at most $4\beta^2/m+\beta$ by the global product bound. With $m\le\lceil\beta^{3/2}\rceil$ and $m/\beta\to\infty$ the resulting $L^2$ error is $O(\beta^{-1/2}(\log\beta)^2)$. The same good event gives $\|B\|_2=O(\log\beta)$. Cauchy–Schwarz and conditional independence prove the absolute covariance comparison. In particular the centered reading scaled using $M$ instead of $s_0$ differs by a factor $s_0/M=1+O(\beta^{-1/2}\log\beta)$, also small against the $O((\log\beta)^2)$ covariance bound.

This reduction leaves a concrete physical question about a spatial average of elementary staple-pair differences. It does not assume the needed separated-time data for that insertion. It gives no answer for a mean-normalized uncompensated Wilson loop or for the charged spatial heat trace. [Z4’s free benchmark](../../z4/fixed-size/WILSON_LOOP.md) · [Direct conditional and Bessel checks](check_wilson.py)

In the infinite-time Wilson vacuum C4’s independent exponential plaquette-moment bound and finite-cell limit determine the subleading coefficient and permit arbitrary spatial sides. [Vacuum bias, physical-time exclusion and the second scale](second-scale.md)
