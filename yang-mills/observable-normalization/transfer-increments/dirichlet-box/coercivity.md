# A global lower bound for the compact action on Z4’s forest

Work on $[0,L]^4$ with $L=2N\ge2$. A link with both endpoints on the shell has prescribed value; the upward time links from interior vertices are fixed to identity. Let $\alpha_e\in[0,\pi]$ be the geodesic angle of a link, and let $\alpha_p$ be the angle of a plaquette. A bound valid on the whole compact group is
$$
 \sum_{e\ {\rm free}}\alpha_e^2
 \le 32 L^3
 \left(\sum_{p\in P_R}\alpha_p^2+\sum_{e\ {\rm shell}}\alpha_e^2\right).
 \tag{1}
$$
Here $P_R$ consists of the plaquettes touching a link with an interior endpoint. In particular Z4’s scaled chart variables obey
$$
 \beta S_R(\varphi/\sqrt\beta;\psi/\sqrt\beta)
 \ \ge\ \frac{2}{\pi^2}\left(\frac{\|\varphi\|^2}{32L^3}-\|\psi\|^2\right).
 \tag{2}
$$
This follows from $\alpha_p^2\le(\pi^2/2)(1-\cos\alpha_p)$. It permits arbitrary exterior shell data in the chart. The analogue of (1) for the additive group uses Euclidean vector norms and plaquette curls; its proof is identical.

For a spatial edge $b=(s,s')$ with at least one interior spatial endpoint let $H_t(b)$ denote its value at time $t$. Let $V_t(s)$ be the straight upward transport from $(t,s)$ to $(L,s)$. Comparing the two paths across the time strip gives
$$
 d\!\left(H_t(b),\, V_t(s)H_L(b)V_t(s')^{-1}\right)
      \le\sum_{r=t}^{L-1}\alpha_{0b}(r).
$$
Replace the horizontal segment successively by the three sides of the next square. Bi-invariance of the group distance makes the cost of each replacement its plaquette angle. These plaquettes all lie in $P_R$.

For $1\le t<L$, an interior spatial endpoint contributes no vertical edges because of the specified forest. A spatial boundary endpoint contributes only shell edges. Thus $\alpha(H_t(b))$ is bounded by a sum of at most $1+3L\le4L$ angles coming from the top edge, the stack of temporal plaquettes and the boundary vertical segments. When all $b,t$ are included, each input angle occurs at most $6L$ times: each stack has at most $L$ starting times, and a boundary vertex has at most six incident spatial edges. Cauchy–Schwarz bounds the total squared horizontal angles by $24L^2$ times the parenthesis in (1).

There remains one free bottom time link at each interior $s$. Write $W_s=V_0(s)$; in the interior this *is* the free bottom link. Across an active spatial edge, the full strip gives
$$
 d(W_s,W_{s'})\le\alpha(H_0(b))+\alpha(H_L(b))+
                  \sum_{r=0}^{L-1}\alpha_{0b}(r).
$$
From each interior $s$ follow a spatial line in direction $-e_1$ down to $s_1=0$. At the boundary endpoint $W$ is a product of $L$ shell time links. Consequently $\alpha(W_s)$ is bounded by at most $L^2+3L$ angles. Summing over $s$ uses each input at most $L$ times, since the two transverse coordinates are fixed along a line. The total squared bottom angles are at most $(L^2+3L)L$ times the parenthesis in (1). The horizontal and bottom estimates together give (1). The [exact Hessian calculation](spectrum.md) shows why a bound of order $L^{-2}$ in place of $L^{-3}$ on the right of (2), with fixed positive prefactor and identity shell, cannot hold uniformly: taking the second variation along a minimizing mode would contradict $\lambda_N\sim3\pi^2/L^3$.
