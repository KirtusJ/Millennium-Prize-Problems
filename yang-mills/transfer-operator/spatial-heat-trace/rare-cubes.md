# A lower bound, the spectral tail and fluctuations

Consider a fixed bounded physical Dirichlet domain containing a cube of positive physical side. Take $s>0$ fixed, $x=s/b^2\to\infty$ and $B=1+4\beta_s+2\beta_t=x^{o(1)}$, meaning $\log B/\log x\to0$. These assumptions include an isotropic logarithmic weak-bare trajectory. The enclosing Wilson lattices may grow. All statements concern the original finite-volume laws. They hold for each of the fixed particle representations without invariant vectors in the [group extension](representations.md).

## An almost-flat cube

Inside $\Lambda$ fix a cube of $m^3$ sites. Impose on its internal spatial links $\|I-\pi(U_e)\|_{\rm op}\le1/m$. This sufficient event can be specified in a single choice of gauge coordinates. The spectral conclusion is gauge invariant. No gauge fixing of the measure is involved.

On the SU(2) defining Wilson law the conditional density of any one link relative to Haar is everywhere at least $e^{-2(B-1)}$. This follows by bounding its exponent above and below by $B-1$. The Haar ball of angular radius $1/m$ has probability at least $8/(3\pi^3 m^3)$ for $m\ge1$, and lies in the specified operator-norm ball. There are fewer than $3m^3$ internal links. Successive conditioning gives probability at least $\exp[-C m^3(B+\log(2m))]$ for the entire event. For a fixed compact group, a ball of radius $c_\pi/m$ suffices by smoothness of $\pi$. Its mass is bounded below by $c_G m^{-\dim G}$ and the bounded Wilson character gives the same form of probability estimate. All constants can depend on the representations.

Use a product of three first Dirichlet sine modes on that cube times a constant unit spinor, extended by zero to $\Lambda$. The scalar Rayleigh quotient in lattice units is $6(1-\cos(\pi/(m+1)))\le3\pi^2/m^2$. On each internal bond the vector difference is bounded in norm by the scalar difference plus $m^{-1}$ times the scalar amplitude at the second endpoint. Squaring, summing and allowing at most three bonds with each second endpoint adds at most $6/m^2$ to twice the scalar energy. Edges to zero support contribute their usual scalar boundary energy. Thus on the event,
$$
 \lambda_{\min}(A_U)\le (6\pi^2+6)/(b^2m^2).
$$
Consequently
$$
 \mathbb E F_s \ge \exp[-C\{x/m^2+m^3(B+\log(2m))\}] .
$$
Choose $L_*=B+\log(2+x)$, $u=(x/L_*)^{1/5}$ and $m=\lfloor u\rfloor$. Eventually $u/2\le m\le u$. The physical side $bm$ tends to zero, so this cube fits. The cost is at most $C' x^{3/5}L_*^{2/5}$. In particular the lower estimate and the [upper estimate](README.md) imply
$$
 \boxed{\displaystyle \lim_{b\downarrow0}\frac{\log(-\log\mathbb E F_s)}{\log(s/b^2)}=\frac35 .}
$$
A fixed positive normalization, including division by physical volume when it tends to a finite nonzero constant, has the same exponent. Neither the leading constant nor a power of the logarithm in $-\log\mathbb E F_s$ has been identified. The nearly flat cube is a sufficient event for the lower bound. It is not assumed to be the only mechanism contributing to the mean. [Lean balance estimate and numerical trial](execution.md)

## How many low modes are present?

In lattice units put $A'=b^2 A_U$ and $N_\Lambda(\varepsilon)=|\Lambda|^{-1}\mathbb E\,\#\{\lambda(A')\le\varepsilon\}$, including multiplicities. This is the cumulative mean count per lattice site. In a large block of side $m$, choose $m$ to be the largest allowed multiple of the small-cell side below $c/\sqrt\varepsilon$. Choose $c>0$ small enough, and require $\varepsilon B^q$ sufficiently small, using $q=1$ for the SU(2) fundamental. Then the good-block potential for $A'$ exceeds $\varepsilon$. By the min–max principle applied to the diagonal potential lower bound, the number of low modes is at most the color dimension times the number of sites in bad blocks. The expected fraction of those sites is at most $\exp[-c' m^3]$. This gives $N_\Lambda(\varepsilon)\le d\exp[-c''\varepsilon^{-3/2}]$, with the same buffer or tiling conditions as the main estimate.

For the reverse bound take a Dirichlet cube whose side in sites exceeds $2(m'+1)$ with $m'=\lceil\sqrt{(6\pi^2+6)/\varepsilon}\rceil$. Pack cubes of side $m'$ separated by at least one layer of unused sites. There are at least $c|\Lambda|/(m')^3$ such cubes. For each favorable cube the sine trial above has energy at most $\varepsilon$. Trials on different cubes have disjoint supports and no edge between supports, so their **entire linear span** obeys the same bound. For every configuration the low-mode count is at least the number of favorable cubes. Linearity of expectation suffices even though favorable cubes need not be independent. Hence
$$
 c(m')^{-3}e^{-C(m')^3[B+\log(2m')]}
 \le N_\Lambda(\varepsilon)\le d e^{-c'\varepsilon^{-3/2}} .
$$
For a sequence with $B=(1/\varepsilon)^{o(1)}$, $\varepsilon\downarrow0$, sufficient cube sizes and outer padding, this gives $\log(-\log N_\Lambda(\varepsilon))/\log(1/\varepsilon)\to3/2$. Any compatible infinite-volume integrated density of states inherits the corresponding finite-box bounds upon taking its defining limits. The estimates require no thermodynamic-limit existence claim. The energy here is the one-particle charged spatial kinetic energy in a random Wilson gauge background.

## Mean normalization and a typical gauge field

Let $Y_b=F_s/\mathbb E F_s$. At fixed physical volume, $F_s$ is bounded deterministically. The mean-normalized trace has the following contrasting statistics in the original Wilson ensemble:
$$
 Y_b\longrightarrow 0\ \text{in probability},\qquad
 \mathbb E Y_b=1,\qquad
 \lim_{b\downarrow0}\frac{\log\log\mathbb E Y_b^p}{\log(s/b^2)}=\frac35
 \quad(p>1).
$$
The last formula describes a divergent moment. To prove it, fix $0<\sigma<1/5$ and take large blocks of side comparable to $x^\sigma$, rounded to a multiple of the cell side. The chance that any block touching the test domain is bad is at most $C|\Lambda|e^{-c x^{3\sigma}}$. On the complementary good event,
$$
 s\lambda_{\min}(A_U)\ge c x/(m^2+B^q)\ge c' x^{1-2\sigma}
$$
eventually. The lower estimate on the mean costs at most $x^{3/5+o(1)}$ in its negative logarithm. Since $1-2\sigma>3/5$ and $|\Lambda|=O(x^{3/2})$, $F_s\le d|\Lambda|e^{-s\lambda_{\min}}$ gives $Y_b=o(1)$ uniformly on the good event. This proves convergence in probability and $\mathbb E[Y_b\,1_{\rm bad}]=1-o(1)$. Hölder's inequality then gives $\mathbb E Y_b^p\ge (1-o(1))^p\Pr({\rm bad})^{1-p}$. It follows that the lower limit of the log-log ratio is at least $3\sigma$ for every $\sigma<1/5$. Finally $Y_b\le C/\mathbb E F_s$ and $\mathbb E Y_b=1$ imply $\mathbb E Y_b^p\le(C/\mathbb E F_s)^{p-1}$, which proves the matching upper limit.

Hence any deterministic multiplicative renormalization keeping the mean bounded still gives zero in probability; if the mean tends to a positive finite value, the second moment diverges. The same statement at a fixed $s$ covers an additive deterministic shift $A_U-\mu_b I$, since its heat trace equals $e^{s\mu_b}F_s$. For example, along $\beta\asymp\log(1/b)$ a counterterm allowing a bounded *typical* lowest auxiliary eigenvalue would have to compete with a lower scale of order $1/[b^2\log(1/b)]$. Boundedness of the mean shifted heat trace allows a shift of at most $O_s(x^{3/5}(B+\log x)^{2/5})$ by the rare-cube lower bound. These scales are incompatible. Field-dependent subtractions, changes to the charged operator and other gauge-invariant observables are separate mathematical questions.

### Averaging over a fixed physical interval

The same probability and moment conclusions hold for a nonnegative normalized average of the mean-normalized traces on polynomially many time slices of a stationary Wilson ensemble. This includes ordinary Euclidean-time smearing over a fixed physical interval on isotropic lattices. Use the same spatial domain and diffusion time on each slice and nonnegative deterministic weights summing to one. A union bound over all those slices changes the exceptional-set probability by only a polynomial factor. On their common good event every summand is uniformly small. The average still has mean one. Hölder on the exceptional set gives the same lower moment exponent, while Jensen bounds its $p$th moment by the common single-slice moment. No temporal independence or decay assumption enters.

This concerns moments under the positive Wilson path measure. The Osterwalder–Schrader norm of a positive-half observable pairs it with its time reflection, and a strictly positive separation is a different quantity from a same-history square. The divergence of the mean-normalized path second moment alone leaves those reflected correlations open. For the unrenormalized trace the deterministic bound and its vanishing first moment already force the separated correlations with bounded probes to vanish. [Positive-time benchmarks](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/48c8779453135ed74159be4e0f4061c5ac703eb6/yang-mills/z4/fixed-size/STATEMENT.md)
