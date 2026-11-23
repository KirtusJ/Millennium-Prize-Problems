"""Apply gap (3) Delta h and gap (4) DG1/DG3 replacements to note/tun_lower_patched.tex. Each old string must occur once."""
import sys
p = "note/tun_lower_patched.tex"
s = open(p).read()
R = []

# ---- (3) Lemma tu:L-taylor: proof of the Delta S^2 and Delta h bounds, explicit corollary ----
R.append((r"""so $|W'-|w+\ell\xi|^2|\le2mr+r^2$ and $W'\le(m+r)^2$. Then
$|h(S')W'-h(S)|w+\ell\xi|^2|\le h|W'-|w+\ell\xi|^2|+|h(S')-h(S)|W'$. The change of $S^2$ comes from
$x_0'-x_0=-u\cdot\xi-(1-g_0)x_0$.""",
r"""so $|W'-|w+\ell\xi|^2|\le2mr+r^2$ and $W'\le(m+r)^2$. Then
$|h(S')W'-h(S)|w+\ell\xi|^2|\le h|W'-|w+\ell\xi|^2|+\Delta h\,W'$ with $\Delta h:=|h(S')-h(S)|$.

\emph{The change of $S^2$.} $S^2=\sum_i(1-x0_i^2)$, and the real part of $(x0_i,u_i)(g_{0i},\xi_i)$ is
$x0_i'=x0_ig_{0i}-u_i\cdot\xi_i$, so $x0_i'-x0_i=-u_i\cdot\xi_i-(1-g_{0i})x0_i$ and $|x0_i'-x0_i|\le\sin a_i\,r_b+r_b^2$
(Lemma~\ref{tu:L-exact}(c)). With $|x0_i'+x0_i|\le2$, $|S'^2-S^2|\le\sum_i|x0_i'-x0_i|\,|x0_i'+x0_i|\le\Delta S^2$.

\emph{The change of $h$.} $h$ is a function of $\sigma:=S^2$: $h=1+\sqrt{1+1/\sigma}$. (So $\sigma_-$ in the statement is a
lower bound for $S'^2$, a value of $S^2$, not of $S$; the bound is dimensionally consistent: $dh/d\sigma=-1/(2\sigma^2\sqrt{1+1/\sigma})$.)
For $0<\sigma_0\le\sigma_1$, with $A_j=\sqrt{1+1/\sigma_j}$,
\[
A_0-A_1=\frac{A_0^2-A_1^2}{A_0+A_1}=\frac{\sigma_1-\sigma_0}{\sigma_0\sigma_1(A_0+A_1)}\le\frac{\sigma_1-\sigma_0}{2\sigma_0^2A_0},
\]
because $2\sigma_0A_0\le\sigma_1A_0+\sigma_1A_1$ (both $\sigma_0A_0\le\sigma_1A_0$ and $\sigma_0A_0=\sqrt{\sigma_0^2+\sigma_0}\le\sqrt{\sigma_1^2+\sigma_1}=\sigma_1A_1$).
Take $\{\sigma_0,\sigma_1\}=\{S^2,S'^2\}$: $\sigma_1-\sigma_0\le\Delta S^2$ and $\sigma_0\ge S^2-\Delta S^2=\sigma_-$; since
$\sigma\mapsto\sigma^2\sqrt{1+1/\sigma}=\sigma^{3/2}\sqrt{1+\sigma}$ is increasing, $\Delta h\le\Delta S^2/(2\sigma_-^2\sqrt{1+1/\sigma_-})$.

\emph{Explicit form.} If $r_b\le S/8$, then, using $\sin a_1+\sin a_2\le\sqrt2S$,
$\Delta S^2\le2\sqrt2Sr_b+4r_b^2\le(\frac{\sqrt2}4+\frac1{16})S^2<\frac{S^2}2$, so $\sigma_-\ge S^2/2$ and
\begin{equation}\label{tu:L-dh-explicit}
\Delta h\le\frac{\Delta S^2}{2\sigma_-^{3/2}}\le\frac{\sqrt2\,\Delta S^2}{S^3}\le\frac{4r_b}{S^2}+\frac{4\sqrt2\,r_b^2}{S^3}\le\frac{5\,r_b}{S^2}.
\end{equation}"""))

R.append((r"""\noindent\emph{Status.} Proved in the working file as stated, with a pointwise numerical check
($0$ violations in $1.6\cdot10^6$ samples; a challenger found $0$ in $2\cdot10^4$). The bound on
$\Delta h$ is stated there without its derivation; it is reproduced here as written (see the list of
open steps in the writer's report). The bound is vacuous unless $r_b$ is small against $\sin^2\eta'$;
with $r_b=L/\sqrt\beta\to0$ this holds for $\beta$ large.""",
r"""\noindent\emph{Status.} Proved in the working file as stated, with a pointwise numerical check
($0$ violations in $1.6\cdot10^6$ samples; a challenger found $0$ in $2\cdot10^4$). The bounds on
$\Delta S^2$ and $\Delta h$, stated there without derivation, are now derived (the $\Delta h$ step is Lean-checked as
\texttt{delta\_h}, and \repo{prog/gap\_dh.py} H1--H3 found $0$ violations in $2\cdot10^5$ random samples; worst ratio
$\Delta h/\text{bound}=0.96$ for the stated bound and $0.33$ for $4r_b/S^2+4\sqrt2r_b^2/S^3$). The stated bound is correct;
it is not dimensionally wrong, since $\sigma_-$ bounds $S'^2$. On $\mathcal T$ ($S\ge s_-$), $r_b\le s_-/8$ gives
$\Delta h\le5r_b/s_-^2=O(r_b)$ uniformly."""))

# ---- (4) Lemma tu:L-gauss: exact gap and derived bounds ----
R.append((r"""\emph{Gap bounds.} Put ${\rm gap}:=[-e(S)+|p|^2/2]-[(h-2)|b|^2+\log J]$. Then
\begin{align*}
{\rm gap}&\le DG_1:=\frac{2h|b|^2}{\beta S^2}+\frac{\kappa^2|b|^2}{2\beta\sigma_w^2}+\frac{|\kappa||b|^2}{\sqrt\beta\sigma_w^2}+\frac{4h^2|b|^4}\beta,\\
-{\rm gap}&\le DG_3:=\frac{h(2+2/S^2)|b|^2}\beta+\frac{|\kappa_3||b|^2}{\sqrt\beta\sigma_w^2},
\end{align*}
($\kappa_3=\Psi'\cot a_1$, the value of $\kappa$ without the $\Theta$-tilt), and all terms are
$O(M^2(1+\bar\kappa)^2/(\sqrt\beta\sin^2\eta'))$ uniformly on $\mathcal T$.""",
r"""\emph{Exact gap.} Put ${\rm gap}:=[-e(S)+|p|^2/2]-[(h-2)|b|^2+\log J]$, $A:=1+2hS^2$, $W=|w|^2=|b|^2/\beta$,
$D_w:=1+2h\sigma_w^2$ and $x:=4hW/A$. Then $\sigma_w^2\ge0$, $D_w=A(1-x)\ge1$, $0\le x<1$, and
\begin{equation}\label{tu:L-gap-exact}
{\rm gap}=\tfrac12\log(1-x)+\tfrac12\log(1+hx)+\frac{hx|b|^2}{D_w}+\frac{h|b|^2}{D_w}\Big(\frac{\kappa^2}\beta-\frac{2\kappa}{\sqrt\beta}\Big).
\end{equation}
\emph{Gap bounds.} Consequently
\begin{align*}
{\rm gap}&\le DG_1':=\frac{2h^2|b|^2}{\beta A}+\frac{4h^2|b|^4}{\beta AD_w}+\frac{h\kappa^2|b|^2}{\beta D_w}+\frac{2h|\kappa||b|^2}{\sqrt\beta D_w}\ \le\ DG_1,\\
-{\rm gap}&\le DG_3'(\kappa):=\frac{2h|b|^2}{\beta D_w}+\frac{2h|\kappa||b|^2}{\sqrt\beta D_w}\ \le\ DG_3(\kappa),
\end{align*}
where $DG_1:=\frac{2h|b|^2}{\beta S^2}+\frac{\kappa^2|b|^2}{2\beta\sigma_w^2}+\frac{|\kappa||b|^2}{\sqrt\beta\sigma_w^2}+\frac{4h^2|b|^4}\beta$ and
$DG_3(\kappa):=\frac{h(2+2/S^2)|b|^2}\beta+\frac{|\kappa||b|^2}{\sqrt\beta\sigma_w^2}$ are the bounds of the working file (the last two
inequalities need $\sigma_w>0$). The same holds for ${\rm gap}_3$ (the gap with $\Theta'=0$) with $\kappa$ replaced by
$\kappa_3=\Psi'\cot a_1$; in particular $-{\rm gap}_3\le DG_3(\kappa_3)$. On $\mathcal T$, with $h_-:=h(s_-)\ge h$, $|b|^2\le M^2$ and
$|\kappa|,|\kappa_3|\le\bar\kappa$:
\begin{equation}\label{tu:L-gap-unif}
|{\rm gap}|,\ |{\rm gap}_3|\ \le\ \frac{2h_-\bar\kappa M^2}{\sqrt\beta}+\frac{h_-M^2(2h_-+4h_-M^2+\bar\kappa^2+2)}{\beta}.
\end{equation}
No lower bound on $\sigma_w$ is needed."""))

R.append((r"""The gap bounds are obtained by comparing $\sigma_w^2=S^2-2|w|^2$, $\sigma_b^2\le2|w|^2/S^2$ with the
valley values and using $2h\sigma/(1+2h\sigma^2)\le1/\sigma$ for the cross term.
\end{proof}""",
r"""\emph{Exact gap.} $\sigma_w^2=S^2-2W\ge0$ because $|w|\le\sin a_1\sin a_2\le S^2/2$ and $S^2\le2$, so $W\le S^4/4\le S^2/2$.
By (G1), $\sigma_w^2+\sigma_a^2+\sigma_b^2=S^2-2W+S^2$ with $\nu_++\nu_-=S^2$, $\nu_+\nu_-=W$, hence
\[
\tfrac12\sum_j\log(1+2h\sigma_j^2)=\tfrac12\log(A-4hW)+\tfrac12\log\big((1+2h\nu_+)(1+2h\nu_-)\big)
=\tfrac12\log(A-4hW)+\tfrac12\log(A+4h^2W),
\]
which is $\log A+\frac12\log(1-x)+\frac12\log(1+hx)=e(S)+\frac12\log(1-x)+\frac12\log(1+hx)$, and $D_w=A-4hW=A(1-x)$.
In the last term of $\log J$, $\sigma_wp_w=-\kappa|w|$ and $b_w=|b|=\sqrt\beta|w|$, so
$h p_w^2\sigma_w^2+2h\sigma_wp_wb_w=h|b|^2(\kappa^2/\beta-2\kappa/\sqrt\beta)$. Finally, by the flat identity
$(h-2)|b|^2=h|b|^2/A$, and $\frac{h|b|^2}{D_w}-\frac{h|b|^2}A=\frac{h|b|^2(A-D_w)}{AD_w}=\frac{hx|b|^2}{D_w}$. Substituting into
${\rm gap}=-e(S)+\frac{|p|^2}2-(h-2)|b|^2-\log J$ gives \eqref{tu:L-gap-exact}.

\emph{Bounds.} Upper: $\frac12\log(1-x)\le0$, $\frac12\log(1+hx)\le\frac{hx}2=\frac{2h^2|b|^2}{\beta A}$,
$\frac{hx|b|^2}{D_w}=\frac{4h^2|b|^4}{\beta AD_w}$, and the last term is $\le\frac{h\kappa^2|b|^2}{\beta D_w}+\frac{2h|\kappa||b|^2}{\sqrt\beta D_w}$.
Lower: $-\frac12\log(1-x)\le\frac{x}{2(1-x)}=\frac{2hW}{D_w}=\frac{2h|b|^2}{\beta D_w}$, $\frac12\log(1+hx)\ge0$, $\frac{hx|b|^2}{D_w}\ge0$,
and the last term is $\ge-\frac{2h|\kappa||b|^2}{\sqrt\beta D_w}$. Comparison with $DG_1,DG_3$: $A\ge2hS^2$ gives
$\frac{2h^2}{A}\le\frac{h}{S^2}\le\frac{2h}{S^2}$; $A,D_w\ge1$; and $\frac h{D_w}=\frac{h}{1+2h\sigma_w^2}\le\frac1{2\sigma_w^2}$ (this is the cross-term
inequality of the working file in the form $2h\sigma/(1+2h\sigma^2)\le1/\sigma$, divided by $\sigma$), so
$\frac{2h|\kappa|}{D_w}\le\frac{|\kappa|}{\sigma_w^2}$, $\frac{h\kappa^2}{D_w}\le\frac{\kappa^2}{2\sigma_w^2}$, and $\frac{2h}{D_w}\le2h\le h(2+\frac2{S^2})$.
\eqref{tu:L-gap-unif} follows from $A,D_w\ge1$, $h\le h_-$ ($h$ decreases in $S$ and $S\ge s_-$ on $\mathcal T$).
\end{proof}"""))

R.append((r"""determinant formula to $4\cdot10^{-15}$; the flat identity is Lean-checked in the working file). The gap bounds
$DG_1,DG_3$ are stated in the working file without a written derivation; only the cross-term inequality
$2h\sigma/(1+2h\sigma^2)\le1/\sigma$ is given (it replaces an earlier false bound with $1/\sigma$ replaced by $1$;
the supremum over $\sigma$ of $2h\sigma/(1+2h\sigma^2)$ is $\sqrt{h/2}$). No challenger checked $DG_1,DG_3$. The
estimates $\Delta_1,\Delta_3$ below use the exact gap, not $DG$; what is needed is only ${\rm gap}=O(\beta^{-1/2})$
uniformly on $\mathcal T$, which is what $DG_1,DG_3$ assert.""",
r"""determinant formula to $4\cdot10^{-15}$; the flat identity is Lean-checked in the working file). The exact gap
\eqref{tu:L-gap-exact} and the bounds $DG_1',DG_3'$ and their comparison with $DG_1,DG_3$ are written for this note
(gap DG1/DG3 of the writer's report). Checked: \repo{prog/gap\_dh.py} Q1--Q8, $2\cdot10^5$ random configurations
($\beta\in[10,10^8]$, arbitrary $a_1,a_2$, directions and tilts), \eqref{tu:L-gap-exact} agrees with the direct
$6$-dimensional determinant formula to relative $2.5\cdot10^{-15}$, $0$ violations of the four bounds; the scalar steps
($\log$ bounds, cross term, determinant factorisation, coefficient difference) are Lean-checked. The
estimates $\Delta_1,\Delta_3$ below use the exact gap; what is needed is ${\rm gap},-{\rm gap}_3=O(\beta^{-1/2})$
uniformly on $\mathcal T$, which \eqref{tu:L-gap-unif} gives with explicit constants."""))

# ---- propagate into Prop tu:L-E13 ----
R.append((r"""Rate: with $L=\sqrt{C\log\beta}$,
${\rm Err}=O\big(h(M+2L)L^2/\sqrt\beta+L(M+2L)^2/(\sqrt\beta s_-^4)+(H_\Psi+H_\Theta)L^2/\sqrt\beta\big)$,
${\rm gap}=O(\beta^{-1/2})$ (Lemma~\ref{tu:L-gauss}), ${\rm Tail}/J$ and $Q$ are $O(\beta^{-c})$, $L^4/\beta\to0$, and
$\log\varrho=O(\beta^{-2/3})$, $-\log\varrho\le-\log D_\beta=O(1/\beta)$. On $\mathcal T$: $S\ge s_-$, so
$h\le1+\sqrt{1+s_-^2}/s_-$ and $\sigma_w^2=S^2-2|w|^2\ge s_-^2-2M^2/\beta$ stay bounded away from $0$.""",
r"""Rate: let $L/\sqrt\beta\le s_-/8$ (so $r_b\le\frac18$). On $\mathcal T$, $|b|\le M$, $S\in[s_-,\sqrt2]$, $h\le h_-:=h(s_-)$, so
$\sqrt\beta m\le M+2L$, $\sqrt\beta r\le r_b(2r_bM+\frac{81}{64}L)\le r_b(M+2L)$, hence $E_W\le\frac{17}8r_b(M+2L)^2$,
$B_W\le\frac{81}{64}(M+2L)^2$, and by \eqref{tu:L-dh-explicit} $\Delta h\le5r_b/s_-^2$. With $r_b'\le1.003\,r_b$ and
$r_b'-r_b\le0.17\,r_b^3$ for $r_b\le\frac18$:
\begin{equation}\label{tu:L-err-explicit}
{\rm Err}\le\frac1{\sqrt\beta}\Big[L(M+2L)^2\Big(2.2\,h_-+\frac{6.4}{s_-^2}\Big)+L^2\big(0.51(H_\Psi+H_\Theta)+0.03(\Lambda+\theta_0)\big)\Big].
\end{equation}
With $L=\sqrt{C\log\beta}$ this is $O((\log\beta)^{3/2}\beta^{-1/2})$; $|{\rm gap}|,|{\rm gap}_3|$ are bounded by
\eqref{tu:L-gap-unif}, $O(\beta^{-1/2})$; ${\rm Tail}/J$ and $Q$ are $O(\beta^{-c})$, $L^4/\beta\to0$, and
$\log\varrho=O(\beta^{-2/3})$, $-\log\varrho\le-\log D_\beta=O(1/\beta)$. On $\mathcal T$: $S\ge s_-$, so
$h\le h_-=1+\sqrt{1+s_-^2}/s_-$; no lower bound on $\sigma_w$ is used (the bounds of Lemma~\ref{tu:L-gauss} have $D_w\ge1$
in the denominators)."""))

R.append((r"""The proof takes any
$\eta'>0$, and its constants depend on $\eta'$ only through $s_-=\sin\eta'$ (via $s_-^{-4}$, $h(s_-)$ and the
$\Delta h$ bound) and on $H_\Psi,\Lambda$;""",
r"""The proof takes any
$\eta'>0$, and its constants depend on $\eta'$ only through $s_-=\sin\eta'$ (via $s_-^{-2}$ and $h(s_-)$ in
\eqref{tu:L-err-explicit} and \eqref{tu:L-gap-unif}, and the condition $L/\sqrt\beta\le s_-/8$) and on $H_\Psi,\Lambda,\bar\kappa$;"""))

R.append((r"""(A wording fix: the assembly
file says ``only through $\sin^2\eta'$''; $s_-^{-4}$ and $h(s_-)$ also enter.)""",
r"""(A wording fix: the assembly
file says ``only through $\sin^2\eta'$''; $h(s_-)$ also enters. The earlier $s_-^{-4}$ is replaced by $s_-^{-2}$ through
\eqref{tu:L-dh-explicit}.)"""))

for old, new in R:
    c = s.count(old)
    if c != 1:
        print("NOT UNIQUE/NOT FOUND", c, old[:90]); sys.exit(1)
    s = s.replace(old, new)
open(p, "w").write(s)
print("lower patched", len(R))
