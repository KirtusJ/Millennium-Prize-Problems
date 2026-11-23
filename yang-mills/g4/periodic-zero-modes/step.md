# From the partition function to the plaquette step

## Analytic improvement of the remainder

The [compact integral](proof.md) fixes both the leading power and logarithm. To extract the mean action at order $1/\log\beta$ one also needs control of the remainder. At each fixed $L$, $S$ is a nonconstant real-analytic function on the compact product of copies of $SU(2)$, and probability Haar has a smooth positive density in each analytic chart. Its zero set has Haar measure zero. A finite smooth partition of unity covers the zero set, and the contribution supported away from it is exponentially small.

Apply Greenblatt’s local sublevel-volume expansion, Theorem 1.1, to the chart integrals of $\mathbf1_{\{0<S<t\}}$. If a chart domain with the zero on its boundary is desired, divide the centered chart into its finitely many open coordinate orthants. Their boundaries have measure zero. The density times the cutoff is a smooth test. Each local expansion has exponents in a discrete progression of positive rationals and finite log degree at each exponent, with a positive gap to subsequent powers. For $F(t)=\mathrm{Haar}\{S\le t\}$ use $Z_L(\beta)=\beta\int_0^\infty e^{-\beta t}F(t)\,dt$. Substituting $u=\beta t$ integrates each sublevel term into a power of $\beta^{-1}$ times a polynomial in $\log\beta$. The remainder to any prescribed finite order has a positive additional power after shrinking the exponent to absorb logs. Compactness leaves a finite union of progressions. [Greenblatt, Theorem 1.1 and remainder (1.7)](https://arxiv.org/pdf/0709.2496)

The leading comparison with $C_L\beta^{-p_L}\log\beta$ excludes earlier nonzero terms and higher log degrees at $p_L$. Thus for some real $d_L$ and $\eta_L>0$,
$$
 Z_L(\beta)=C_L\beta^{-p_L}
       [\log\beta+d_L+O_L(\beta^{-\eta_L})].                    \tag{3}
$$
All statements here fix the box before taking $\beta$ large.

The derivative of $\log Z_L$ is $-\mathbb E S$ and its second derivative is $\mathrm{Var}(S)\ge0$. Bracket the first derivative by forward and backward secant slopes with endpoints $\beta(1\pm h)$, $h=(\log\beta)^{-3}$. For the explicit main term of $\log Z_L$, multiplying a secant slope by $\beta$ gives $-p_L+(\log\beta+d_L)^{-1}+O_L(h)$ by Taylor’s theorem. From (3) the error due to the unknown remainder is $O_L(\beta^{-\eta_L}/h)$. Hence
$$
 \beta\mathbb E S = p_L-1/\log\beta+O_L((\log\beta)^{-2}).
$$
This secant argument uses only the controlled values of the remainder. All $6V$ terms of $S$ have the same expectation by translations and coordinate permutations. Dividing gives the elementary-plaquette coefficient in the [theorem](README.md).

## Step at fixed box sizes

With $u_L=\mathbb E S/p_L$, (3) gives $u_L=\beta^{-1}[1-1/(p_L\log\beta)+O_L((\log\beta)^{-2})]$. One can use $u_L$ as the independent variable near zero because its derivative is $-\mathrm{Var}(S)/p_L<0$ at finite coupling since $S$ is nonconstant and the density is strictly positive. At the same $\beta$, form the difference for $L$ and $sL$. Then $\log(1/u_L)=\log\beta+O_L(1/\log\beta)$ and the normalized difference satisfies
$$
 \lim_{\beta\to\infty}
 \frac{u_{sL}-u_L}{u_L/\log(1/u_L)}
 = \frac{1}{p_L}-\frac{1}{p_{sL}}>0 .
$$
In particular $(u_{sL}-u_L)/u_L^2\to+\infty$. With the coupling normalized instead to the conventional $g_0^2=4/\beta$, the two couplings and their difference are multiplied by four. The leading $u/\log(1/u)$ coefficient is unchanged under this fixed rescaling. Neither the remainders nor the range of $\beta$ here are uniform in $L$. A continuum step-scaling scheme must specify its observable, boundary conditions, physical scale and order of limits. [Finite-volume gradient flow](https://arxiv.org/abs/1208.1051) · [Periodic Wilson-loop calibration](https://arxiv.org/abs/2303.01008)

## A boundary control

Take a nontrivial finite contractible cubical box with its internal links and plaquettes and free boundary. Tree gauge leaves $n_o=|E|-|V|+1$ independent links. A flat connection at the gauge-fixed tree is the identity on every link since each loop is filled by plaquettes. The quadratic action on the remaining link coordinates is $\|d_1X\|^2/2$. A closed real one-cochain on this complex is a vertex gradient, and zero tree data force that gradient to vanish. Hence the minimum is nondegenerate, with $p_o=3n_o/2$. Ordinary Laplace asymptotics give $Z_o=C_o\beta^{-p_o}[1+c_o/\beta+O_o(\beta^{-2})]$ and $\mathbb E S/p_o=\beta^{-1}+(c_o/p_o)\beta^{-2}+O_o(\beta^{-3})$. The differentiated expansion follows, for example, by applying the same Gaussian expansion directly with the action insertion. In exponential link coordinates the coefficient is
$$
 c_o=\mathbb E_G\!\left[\tfrac12 S_3(X)^2-S_4(X)-\tfrac13\sum_e |X_e|^2\right],
$$
where $S_j$ is the degree-$j$ Taylor term of the gauge-fixed action and $G$ has density proportional to $e^{-S_2(X)}$. The final contribution comes from the product of $\operatorname{sinc}^2$ Haar factors. For a single square the remaining holonomy is Haar, $S_2=|X|^2/2$, $S_3=0$, $S_4=-|X|^4/24$, and $c_o=15/24-3/3=-3/8$. This checks the sign and illustrates why a fixed open-box probe can have an ordinary quadratic term. It supplies no identification of that term with a universal continuum coefficient.
