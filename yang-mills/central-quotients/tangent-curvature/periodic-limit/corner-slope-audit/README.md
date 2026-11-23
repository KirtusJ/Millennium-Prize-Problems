# How much spectral weight a square Wilson loop puts on large energy slopes

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

A4’s finite-box calculation gives a Gaussian limit for the first-order electric energy slopes seen by a large square. The exact finite list of moments also determines how much square weight reaches slopes that grow with the side. Write $\ell$ for the square side, $j=\ell-1$ for $\ell\ge2$, and $\nu$ for its slope measure. Uniformly in the allowed finite boxes and positive temporal couplings, if $x\to\infty$ and $\limsup 2x^2/j<1$, then
$$
\log\nu([x,x+4])=-2x^2+O(x),\qquad
\log\nu([x,\infty))=-2x^2+O(x).
$$
Both estimates hold on the reflected negative intervals as well. Here the probability of a slope is the fraction of the square Wilson trace’s squared norm on that slope. The magnetic derivative is taken at zero in each finite periodic box before the side grows. [A4’s theorem at the reviewed revision](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/d4f8b7f2e209db4532086579a4ff5c00df8183fb/yang-mills/observable-normalization/transfer-increments/electric-lag/corner-spectrum/README.md)

The estimates use only symmetry and moment matching through order $2j$. A4’s original range is $j=\lfloor(\ell-4)/2\rfloor$. The larger value above uses B4’s subsequent count of the cells removed across all four corners. [B4’s finite-side improvement](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/b0d0cad842ffc2758c482605eebc6da5af059dfb/yang-mills/observable-normalization/transfer-increments/electric-lag/corner-spectrum/b4-review/README.md)

## Independent readback of the Wilson input

Use A4’s fundamental SU(2) convention, with magnetic insertion $A=\tfrac12\sum_p\operatorname{Tr}U_p$ on an even spatial torus $L\ge4\ell$. Write $q=I_2(g)/I_1(g)$, $a=I_3(g)/I_1(g)$, $r=q^{4\ell}$ and let $P$ project onto the **entire** electric eigenspace of $r$. At fixed $g>0$, $0<q,a<1$. On $P$ the derivative of the symmetrically split transfer is $rPAP$. The top eigenvalue has zero derivative, so the normalized energy slopes are eigenvalues of $B=-PAP$. Write $f$ for the unit-norm square trace and $\nu$ for the spectral measure of $B$ in $f$.

* **Other eigenvectors with the same energy.** A face with zero shared edges multiplies the electric eigenvalue by $q^4$. With one shared edge the tensor product there contains spin zero and spin one, giving multipliers $q^2$ and $q^2 a$. With two consecutive shared edges, orient the common path oppositely and denote its product by $X$. The shared factors occur as $\operatorname{Tr}(XU)\operatorname{Tr}(X^{-1}V)$. Schur orthogonality in the fundamental representation gives $\operatorname{Tr}(UV)/2$ upon averaging either shared link. For fixed other shared link the product $X$ is Haar, so both one-link singlet projections give exactly the same detour. Subtracting it leaves spin one on **both** shared edges, with eigenvalue $ra^2$. Only the detour remains at $r$ and its magnetic coefficient is $1/4$. This exhausts the image of each tested face before projection, even if further unrelated spin networks have eigenvalue $r$. [SU(2) Clebsch–Gordan decomposition](https://www.math.ucdavis.edu/~bxn/introduction_to_qss-lecture4-su2.pdf) · [A4’s shared-path calculation](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/d4f8b7f2e209db4532086579a4ff5c00df8183fb/yang-mills/observable-normalization/transfer-increments/electric-lag/bends/README.md)
* **Bounded-depth geometry.** At depth $d<j$, each removed corner diagram fits within $d$ cells of its original vertex in each coordinate. A face touching a modified edge lies in the corresponding corner box enlarged by one cell. Such boxes are separated along every original side under $\ell\ge2j+4$. Within each box the two incident side segments and their replacement form one monotone staircase. Two opposite horizontal edges of a unit face would traverse the same horizontal unit interval twice, and the analogous vertical configuration is also excluded. An off-plane unit face has at most one coplanar edge. Hence a surviving face turns a single staircase by an addable or removable cell. Conversely either change produces a simple perimeter-preserving detour. This induction needs only the first $j$ outward moves, since the $2j$th moment is a squared norm. The torus has enough space for the lifted square and its one-cell neighborhood.
* **B4’s refinement.** At depth $d\le j-1$, write $m_c$ for the size of each corner diagram. Their total is at most $d$. In a coordinate separating any two corners, the two one-cell-enlarged boxes use at most $m_c+m_{c'}+2\le d+2\le\ell$ cell columns. Thus no test cell belongs to both boxes. Each box also stops short of the opposite side. At depth $j\le\ell-1$ the original unpadded boxes of each pair have a full intervening cell column in a separating direction, so each removed component recovers its own corner label. This verifies the stronger induction range used here.
* **Moments.** Four independent Young diagrams give the commutator $DU-UD=4I$. A4’s factor $1/4$ on each move then gives $M_{2k}=\int s^{2k}\,d\nu=(2k-1)!!/4^k$ for $0\le k\le j$, with $M_0=1$. The periodic link-center transformation makes $\nu$ exactly symmetric. For instance put the sign $(-1)^{\sum_{i<d}x_i}$ on a positive link in direction $d$ at $x$. Its product around each elementary face is $-1$, and its product around the square is $(-1)^{\ell^2}$. It commutes with the electric transfer and negates $B$. [Stanley, *Differential Posets*](https://math.mit.edu/~rstan/pubs/pubfiles/77.pdf)

## Weight on increasing slopes

For $x\ge1$ choose $h=\lfloor 2x^2\rfloor$ and $k=\lceil 2(x+2)^2\rceil$. Whenever $k+2\le j$ there are explicit two-sided bounds:
$$
\frac{3M_{2k}}{8(x+4)^{2k}}
\ \le\ \nu([x,x+4])\ \le\ \nu([x,\infty))
\ \le\ \frac{M_{2h}}{2x^{2h}} .
$$
The upper bound uses symmetry and Markov’s inequality. For the lower bound reweight $\nu$ by $s^{2k}/M_{2k}$. Under this probability law $s^2$ has mean $\mu=(2k+1)/4$ and variance $(2k+1)/8=\mu/2$, using only the next two even moments. Chebyshev puts at least $3/4$ of the reweighted mass in $|s^2-\mu|\le\sqrt{2\mu}$. The choice of $k$ gives $x+2\le\sqrt\mu<x+3$ and places this event inside $x\le |s|\le x+4$. Removing the weight costs at most $(x+4)^{2k}/M_{2k}$ there, and symmetry gives half the resulting bound to each sign.

Stirling’s formula gives $\log M_{2k}=k\log(k/2)-k+O(1)$. Inserting $h=2x^2+O(1)$ and $k=2x^2+O(x)$ proves the headline estimates whenever $k+2\le j$ eventually, in particular under the stated limsup condition. The more restrictive requirement $x=o(\sqrt j)$ is unnecessary for these window estimates. [NIST DLMF, Stirling expansion](https://dlmf.nist.gov/5.11)

For any $b_\ell\to\infty$ with $b_\ell=o(\sqrt j)$, the scaled slopes $s/b_\ell$ obey a full large-deviation principle with speed $b_\ell^2$ and good rate $2z^2$. A fixed open interval about $z>0$ eventually contains $[b_\ell z,b_\ell z+4]/b_\ell$, and symmetry handles $z<0$. Neighborhoods of zero have probability tending to one by the fixed variance. For a closed set at distance $d>0$ from zero the two tails at $b_\ell d$ give the upper bound. For a closed set meeting zero the trivial probability bound suffices. This proof needs no bound on a finite-box exponential moment.

## Central accuracy and extreme support

**Distribution function.** Let $\gamma=N(0,1/4)$. Comparing the Taylor expansions of the two characteristic functions through degree $2j-1$, the integral remainder gives
$$
|\widehat\nu(t)-\widehat\gamma(t)|
\le 2\frac{|t|^{2j}M_{2j}}{(2j)!}
=\frac{2}{j!}(t^2/8)^j .
$$
For $T=2\sqrt{j/e}$, the integral of this upper bound divided by $|t|$ over $[-T,T]$ is at most $2^{1-j}/j$, using $j!\ge(j/e)^j$. The Gaussian density is bounded. The real-line smoothing inequality therefore gives $\sup_z|\nu((-\infty,z])-\gamma((-\infty,z])|=O(j^{-1/2})$ for $j\ge1$. This additive error is uniform in $L,g$; the weight estimate above also handles tails exponentially smaller than that error. [Borda, Theorem A](https://real.mtak.hu/139037/2/2005.pdf)

**Visible slopes.** The polynomials of degree at most $j$ have the same inner products for $\nu$ and $\gamma$. They form a space of dimension $j+1$, so at least $j+1$ distinct slopes have positive square weight. In the normalized Hermite basis the compression of multiplication by $s$ to this space has zero diagonal and off-diagonal entries $\sqrt h/2$, $1\le h\le j$. Its entries require moments through order $2j+1$, whose last (odd) entry vanishes by symmetry. The variational principle puts a visible slope at least at the largest eigenvalue of this matrix, and symmetry gives the negative counterpart. This eigenvalue is half the largest zero of the probabilists’ Hermite polynomial $\mathrm{He}_{j+1}$. For any $2\le m\le j+1$, the positive first sine vector on the last $m$ basis elements gives the explicit lower bound $\sqrt{j-m+2}\cos(\pi/(m+1))$. Taking $m=\lfloor\sqrt j\rfloor$ for large $j$ proves a visible slope of magnitude at least $(1-o(1))\sqrt j$ on **each** side. Its individual weight can be small. [NIST DLMF, Jacobi matrices and quadrature nodes](https://dlmf.nist.gov/3.5#vi) · [Hermite recurrences](https://dlmf.nist.gov/18.9)

All conclusions concern first derivatives in the square’s excited electric cluster. Controlling finite magnetic coupling uniformly in the box or obtaining a continuum mass gap requires additional estimates.

## Executed checks and limits

Three linked PCP OS guests carried out independent finite tests. The first scanned all planar test cells in and around a side-12 square through four outward steps, aggregating repeated paths by sorted physical cell coordinates. It checked the squared multiplicity sums $4,48,960,26880$ without generating moves from partitions. The second checked 1,024 singlet contractions on noncommuting quaternion units by averaging the two shared links separately. The third evaluated finite Hermite Jacobi recurrences in dimensions 2 through 8. In dimension $n$ they reproduce the standardized normal moments through order $2n-1$ and miss $n!$ at order $2n$, providing an explicit check on the truncation index. Lean 4.19.0 accepted four declarations, and the replay rejected a malformed task and three altered declarations. The Haar projection, geometry at general side, tail bounds and limiting statements are analytic arguments above. [Worker](worker.c) · [Replay](verify.py) · [Lean declarations](CornerSlopeAudit.lean)
