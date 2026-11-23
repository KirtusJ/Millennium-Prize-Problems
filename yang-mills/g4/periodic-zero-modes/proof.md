# The compact periodic integral

## Tree coordinates and uniform bounds at fixed side length

Represent each $SU(2)$ matrix by a unit quaternion, write $d(g,h)=|g-h|$ and note $D(g)=d(g,1)^2/2$. Give the torus its periodic cubical cell structure with $4V$ positive links and $6V$ positive faces. At $L=2$ parallel links remain distinct, and at $L=1$ the four links are loops. In the cut-open cube take the tree in which the path from the origin to $x\in\{0,\ldots,L-1\}^4$ traverses coordinates in increasing order. In particular it contains the four unwrapped coordinate arms. Changing vertex frames along the tree pins its $V-1$ links to the identity with unit Haar factor. This follows by integrating the successive vertex changes against probability Haar and using gauge invariance of the action.

The closing link on the root axis in direction $i$ now equals the based cycle holonomy $g_i$. Define a background $B_e$ equal to $g_i$ on every wrap in direction $i$ and to one elsewhere. On the remaining $n=3(V-1)$ chords use $h_e=U'_eB_e^{-1}$. Haar invariance makes the four $g_i$ and $n$ residual coordinates product Haar integration variables. Set $h_e=1$ on the tree and the anchors. Residual conjugation at the root costs no volume factor.

With $S_1(g)=\sum_{i<j}D([g_i,g_j])$ there are positive constants depending only on the fixed box such that
$$
 c_L\left(S_1(g)+\sum_e D(h_e)\right)\le S(g,h)
 \le C'_L\left(S_1(g)+\sum_e D(h_e)\right).                    \tag{1}
$$
For the lower estimate, view each residual chord as its based tree loop followed by the inverse anchor cycle if the chord wraps. The lifted displacement is zero. The same holds for the commutators of the four based cycles. In $\mathbb Z^4$ sort each signed step word by coordinate and cancel opposite steps. Exchanging two neighboring perpendicular steps sweeps out one signed unit face. Projecting back, each word is a product of finitely many conjugated plaquettes and their inverses. The bi-invariant distance, triangle inequality and Cauchy–Schwarz bound its squared chord distance by a fixed multiple of $S$, allowing repeated faces. There are finitely many such words. For the upper estimate telescope each face against the four background links. Its background word is one except at a double wrap $x_i=x_j=L-1$, where it is $[g_i,g_j]$. The same metric inequalities give the other direction. This also proves that the $h$ coordinates have only the identity as an admissible zero when the $g_i$ commute.

## A transverse Gaussian near the commuting holonomies

The map $g\mapsto v=\operatorname{Im}g$ has probability density $\pi^{-2}(1-|v|^2)^{-1/2}$ on the unit three-ball. Both hemispheres are included. For four holonomies the sign of each real sheet can equivalently be absorbed into the corresponding wrap links by multiplying them by the central element $-1$. Every face is invariant under this operation. Thus we may write $g_i=\sqrt{1-|v_i|^2}+v_i$ with the two-sheet density, including in the full lattice integral. The identity $[g_i,g_j]-1=(g_ig_j-g_jg_i)g_i^{-1}g_j^{-1}$ gives exactly
$$
 S_1(g)=2\sum_{i<j}|v_i\times v_j|^2 .
$$

Let $r=\max_i|v_i|$. Ties have Haar measure zero. In a sector with pivot $k$, put $v_k=r\omega$, $\omega\in S^2$. Write $v_i=r(t_i\omega+z_i)$ for the other three, $z_i\perp\omega$ and $t_i^2+|z_i|^2\le1$. Put $t_k=1,\ z_k=0$. The Lebesgue factor is $r^{11}dr\,d\omega\,dt\,dz$. Set $q=\beta r^4$, $y_i=\sqrt q\,z_i$. Then
$$
 r^{11}q^{-3}dr=\beta^{-3}\frac{dr}{r}.
$$

Two ends of the radial integral contribute $O_L(\beta^{-p_L})$. For $r\le\beta^{-1/4}$ the four small balls have total volume $O(\beta^{-3})$. The residual factors in (1) give $O_L(\beta^{-3n/2})$, since $\int e^{-tD(h)}dh=O(t^{-3/2})$. For $r\ge r_0$ with $0<r_0<1/2$ fixed, the pivot bounds $S_1\ge2r^2\sum_{i\ne k}|v_i^\perp|^2$. Under Haar, the two components perpendicular to a fixed axis are uniform on the unit disk because integrating the three-ball density along the third component gives $1/\pi$. Dropping the nonpivot radius cut, each of the three remaining factors is $O_{r_0}(\beta^{-1})$. Together with the same $h$ estimate this proves the bound, including the integrable outer Haar singularity.

In the middle interval put $\alpha=-4\log r/\log\beta$. For fixed $0<\alpha<1$, $r\to0,\ q\to\infty$. Use the principal logarithm $h_e=\exp(X_e/\sqrt\beta)$, $|X_e|<\pi\sqrt\beta$, omitting a null set. Its measure is $\beta^{-3/2}(2\pi^2)^{-1}\operatorname{sinc}^2(|X_e|/\sqrt\beta)\,d^3X_e$. Since $1-\cos u\ge2u^2/\pi^2$ on $[0,\pi]$, (1) bounds the scaled density after the Jacobians by a fixed-box constant times $\exp[-c(\sum_e|X_e|^2+\sum_{i\ne k}|y_i|^2)]$. All holonomy Haar density factors are bounded at $r\le r_0$. This gives an integrable majorant in $(\alpha,\omega,t,y,X)$, with $|t_i|\le1$. The radial factor is now $\beta^{-3}\log(\beta)\,d\alpha/4$.

Let $D_1$ be the real cellular curl with columns restricted to the $n$ residual links. At fixed scaled coordinates,
$$
 \beta S \ \longrightarrow\ \tfrac12\|D_1X+F\|^2,\qquad
 F_{ij}(x)=\mathbf1_{\{x_i=x_j=L-1\}} f_{ij},\quad
 f_{ij}=2\omega\times(t_i y_j-t_j y_i).                         \tag{2}
$$
Indeed the residual insertions give their signed linear face sum because their conjugating backgrounds tend to one. On a double wrap the exact quaternion commutator identity above gives $\sqrt\beta(v_i\times v_j)=\omega\times(t_i y_j-t_j y_i)+q^{-1/2}y_i\times y_j$. The two inverse factors tend to one. Thus $\sqrt\beta(U_p-1)$ has the stated imaginary limit and its squared norm divided by two gives (2). All products involve finitely many links. Away from $|t_i|=1$ the transverse domains exhaust the full planes.

The columns of $D_1$ span the exact two-cochains and are independent, as shown in the [determinant calculation](determinant.md). On each color integrate $X$ by completing the square. The residual is the orthogonal projection of $F$ off exact forms. Its $ij$ component is the constant $f_{ij}/L^2$. Explicitly, put $w_i(x)=\mathbf1_{\{x_i=L-1\}}$, $H_i(x)=-x_i/L$ and let $\Delta_i$ denote forward difference. Then $\Delta_i H_i=w_i-1/L$, and
$$
 w_iw_j-L^{-2}=\Delta_i(H_iw_j)-\Delta_j(-H_j/L).
$$
The potential with the indicated $i,j$ components has no other curl components. Constants are orthogonal to differences by periodicity. Since $V/L^4=1$, the residual squared norm is exactly $\sum_{i<j}|f_{ij}|^2$. The residual-link Gaussian integral including its Haar factor contributes $(2/\pi)^{n/2}\det(D_1^TD_1)^{-3/2}$ to the coefficient.

For either of the two transverse coordinates $y\in\mathbb R^3$, the remaining exponent is $-2y^TA(t)y$, with $t$ restricted to the three nonpivot entries and $A(t)=(1+|t|^2)I-tt^T$. The pivot supplies the identity term. The two Gaussian integrals together give $(\pi/2)^3/(1+|t|^2)^2$. The integral of $(1+|t|^2)^{-2}$ on $[-1,1]^3$ is $|S^3|/8=\pi^2/4$. Indeed, the map $t\mapsto(1,t)/\sqrt{1+|t|^2}$ parametrizes the patch where the distinguished coordinate is positive and largest in absolute value, with precisely this area element. Each of the eight signed pivot patches has the same area. Multiplying the four pivots, angular area $4\pi$, Haar factor $\pi^{-8}$, radial factor $1/4$, and the two preceding integrals gives $1/(8\pi^2)$. With $L=1$ this is the entire coefficient. The determinant factor supplies the result for larger $L$.

Dominated convergence on the middle interval proves the asymptotic. Restricting $\alpha$ to a fixed subinterval of $(0,1)$ multiplies the limit by its length. Tilting by $e^{-s\beta S}$, $s\ge0$, multiplies the limiting Gaussian integral by $(1+s)^{-(3n+6)/2}$ since the quadratic form in the $3n+6$ normal variables is positive definite for every $t$. The two ends have vanishing relative mass. These restricted Laplace transforms prove convergence to the product of the uniform distribution on $[0,1]$ and the Gamma distribution stated in the [theorem](README.md).
