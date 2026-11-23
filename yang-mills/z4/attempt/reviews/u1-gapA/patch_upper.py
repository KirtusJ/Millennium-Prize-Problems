"""Apply the W1/W3 replacement text to note/tun_upper_patched.tex (copy of tun_upper.tex). Each old string must occur once."""
import sys
p = "note/tun_upper_patched.tex"
s = open(p).read()

R = []
R.append((r"""\item[(W1)] A function $\rho_\eta:[0,\infty)\to[0,\infty)$ with $\sqrt{\rho_\eta}$ smooth, $\rho_\eta(\varepsilon)\le(\varepsilon-\eta)_+$ for
all $\varepsilon$, and $\rho_\eta(\varepsilon)\ge\varepsilon-2\eta$ for $\varepsilon\ge3\eta$.""",
r"""\item[(W1)] A function $\rho_\eta:[0,\infty)\to[0,\infty)$ with $\sqrt{\rho_\eta}\in C^1([0,\infty))$, $\rho_\eta(\varepsilon)\le(\varepsilon-\eta)_+$ for
all $\varepsilon$, $\rho_\eta=0$ on $[0,\frac32\eta]$, and $\rho_\eta(\varepsilon)\ge\varepsilon-2\eta$ for $\varepsilon\ge3\eta$.
(Only $C^1$ of $\sqrt{\rho_\eta}$ is used: it makes $f$ below $C^2$ off $\pi/2$, since $\varepsilon(a)$ is real-analytic. As a
function of $a$, $\rho_\eta(\varepsilon(a))$ is symmetric under $a\mapsto\pi-a$ because $\varepsilon$ is.)"""))

R.append((r"""$f$ is smooth on $[0,\pi]\setminus\{\pi/2\}$, $|f'|\le\sqrt{2\varepsilon}\le L$, and $f$ has a concave kink at $\pi/2$.""",
r"""$f$ is $C^2$ on $[0,\pi]\setminus\{\pi/2\}$, $|f'|\le\sqrt{2\varepsilon}\le L$, and $f$ has a concave kink at $\pi/2$."""))

R.append((r"""The working file asserts that such $\rho_\eta$ and $\tilde f$ exist (``smooth the concave kink at $\pi/2$ on a window of
width $\tau$, keeping $|\tilde f'|\le|f'|$''); neither is constructed there, and neither is constructed here.""",
r"""The working file asserts that such $\rho_\eta$ and $\tilde f$ exist (``smooth the concave kink at $\pi/2$ on a window of
width $\tau$, keeping $|\tilde f'|\le|f'|$'') without constructing them. They are constructed in
Lemma~\ref{tu:U-W13}, which also gives the constants used below.

\begin{lemma}[Construction of $\rho_\eta$ and $\tilde f$]\label{tu:U-W13}
Let $\mathrm{Sm}(s)=0$ for $s\le0$, $\mathrm{Sm}(s)=3s^2-2s^3$ for $0\le s\le1$, $\mathrm{Sm}(s)=1$ for $s\ge1$; $\mathrm{Sm}\in C^1(\R)$,
$0\le\mathrm{Sm}\le1$, $0\le\mathrm{Sm}'\le\frac32$. Put $\psi(t)=\mathrm{Sm}\bigl(\frac23(t-\frac12)\bigr)$ (so $\psi=0$ for $t\le\frac12$,
$\psi=1$ for $t\ge2$, $0\le\psi'\le1$) and
\[
g_\eta(\varepsilon):=\sqrt{(\varepsilon-\eta)_+}\;\psi\Bigl(\frac{\varepsilon-\eta}{\eta}\Bigr),\qquad \rho_\eta:=g_\eta^2 .
\]
With $f$ as in (W2), $p(a):=f'(a)=\sqrt2\,g_\eta(\varepsilon(a))$ on $[0,\frac\pi2]$, and $\chi(a):=\mathrm{Sm}\bigl((\frac\pi2-a)/\frac\tau2\bigr)$, put
\[
\tilde f(a):=\int_0^a p(b)\chi(b)\,db\quad(0\le a\le\tfrac\pi2),\qquad \tilde f(\pi-a):=\tilde f(a).
\]
Then:
\begin{enumerate}
\item $\rho_\eta$ satisfies (W1), and $|g_\eta'|\le\frac{3}{\sqrt{2\eta}}$ on $[0,\infty)$.
\item $\tilde f$ satisfies (W3). Moreover $0\le\tilde f'\le f'$ on $[0,\frac\pi2]$, $f-\frac{L\tau}2\le\tilde f\le f$, and
\[
\sup_{(0,\pi)}|\tilde f''|\le\frac{6}{\sqrt\eta}+\frac{3L}{\tau},\qquad
\sup_{(0,\pi)}|\tilde f'(a)\cot a|\le\frac{L}{\sinh(3\eta/4)} .
\]
Consequently the constant $H$ of Lemma~\ref{tu:U-weight}(2) satisfies
$H\le(1-\delta)\max\bigl(\frac6{\sqrt\eta}+\frac{3L}\tau,\frac{L}{\sinh(3\eta/4)}\bigr)$, and $|\Phi'|\le(1-\delta)L\le L$.
\end{enumerate}
\end{lemma}

\begin{proof}
(1) $\mathrm{Sm}$ is $C^1$ because $\mathrm{Sm}'(s)=6s(1-s)$ vanishes at $s=0,1$; on $[0,1]$, $0\le3s^2-2s^3\le1$ and
$0\le6s-6s^2\le\frac32$. Put $t=(\varepsilon-\eta)/\eta$. Where $t\le\frac12$, i.e.\ $\varepsilon\le\frac32\eta$, $g_\eta=0$.
On the open set $\varepsilon>\eta$ both factors are $C^1$, and $g_\eta$ vanishes on the neighbourhood $\varepsilon<\frac32\eta$ of the
only point $\varepsilon=\eta$ where $\sqrt{(\varepsilon-\eta)_+}$ fails to be $C^1$; hence $g_\eta\in C^1([0,\infty))$.
$\rho_\eta=(\varepsilon-\eta)_+\psi^2\le(\varepsilon-\eta)_+$ since $0\le\psi\le1$. For $\varepsilon\ge3\eta$, $t\ge2$, $\psi=1$ and
$\rho_\eta=\varepsilon-\eta\ge\varepsilon-2\eta$. For the derivative, where $t>\frac12$ (so $\varepsilon-\eta>\frac\eta2$),
\[
g_\eta'(\varepsilon)=\frac{\psi(t)}{2\sqrt{\varepsilon-\eta}}+\frac{\sqrt{\varepsilon-\eta}}{\eta}\psi'(t),\qquad
\frac{\psi}{2\sqrt{\varepsilon-\eta}}\le\frac1{2\sqrt{\eta/2}}=\frac1{\sqrt{2\eta}},
\]
and the second term is nonzero only for $t\le2$, i.e.\ $\varepsilon-\eta\le2\eta$, where it is $\le\sqrt{2\eta}/\eta=\sqrt{2/\eta}$.
The sum is $\le(1+2)/\sqrt{2\eta}$.

(2) $p\in C^1([0,\frac\pi2])$ because $g_\eta\in C^1$ and $\varepsilon(a)=2\operatorname{asinh}(\sin a)$ is real-analytic with
$|\varepsilon'(a)|=2|\cos a|/\sqrt{1+\sin^2a}\le2$; hence $|p'|\le\sqrt2\cdot\frac3{\sqrt{2\eta}}\cdot2=\frac6{\sqrt\eta}$.
$\chi\in C^1$, $0\le\chi\le1$, $\chi=1$ on $[0,\frac\pi2-\frac\tau2]$, $\chi(\frac\pi2)=0$, $\chi'(\frac\pi2)=\chi'(\frac\pi2-\frac\tau2)=0$,
$|\chi'|\le\frac32\cdot\frac2\tau=\frac3\tau$. So $\tilde f'=p\chi\in C^1([0,\frac\pi2])$, $0\le\tilde f'\le p=f'$, and
$\tilde f=f$ on $[0,\frac\pi2-\frac\tau2]$ (same integrand). On $[0,\frac\pi2]$,
$\tilde f''=p'\chi+p\chi'$, so $|\tilde f''|\le\frac6{\sqrt\eta}+\frac{3L}\tau$ using $p\le\sqrt{2\varepsilon}\le L$.
\emph{Gluing at $\pi/2$.} $\tilde f'(\frac\pi2)=p\chi=0$ and $\tilde f''(\frac\pi2^-)=p'\cdot0+p\cdot0=0$. The reflection
$a\mapsto\tilde f(\pi-a)$ has derivative $-\tilde f'(\pi-a)$ and second derivative $\tilde f''(\pi-a)$; both one-sided values
agree at $\pi/2$ ($0$ and $0$), so $\tilde f\in C^2([0,\pi])$, symmetric, and $\tilde f=f$ outside
$(\frac\pi2-\frac\tau2,\frac\pi2+\frac\tau2)$ (by the symmetry of $f$). On the window $|\tilde f'|\le|f'|\le L$. Since
$0\le f'-\tilde f'=p(1-\chi)\le L$ and vanishes left of $\frac\pi2-\frac\tau2$, $0\le f-\tilde f\le L\frac\tau2$ on $[0,\frac\pi2]$, and by
symmetry on $[0,\pi]$. \emph{The $\cot$ term.} $\tilde f'\ne0$ only where $\varepsilon(a)>\frac32\eta$, i.e.\
$\sin a>\sinh(3\eta/4)$, where $|\cot a|\le1/\sin a<1/\sinh(3\eta/4)$; and $|\tilde f'|\le L$. The bound on $H$ follows
from $\Phi=(1-\delta)\tilde f$.
\end{proof}

\noindent\emph{Status.} Proved (written for this note; gap W1/W3 of the writer's report). Numerically checked
(\repo{prog/w1w3.py}: all predicates met for $\eta\in\{0.5,0.2,0.05,0.01\}$, $\tau\in\{0.5,0.1,0.02\}$; measured
$\max|g_\eta'|\sqrt{2\eta}/3=0.665$ and $\max|\tilde f''|/(6/\sqrt\eta+3L/\tau)\le0.90$); the smoothstep bounds are
Lean-checked. If $C^\infty$ is wanted, replace $\mathrm{Sm}$ by any $C^\infty$ step with $0\le\mathrm{Sm}'\le\frac32+\epsilon$;
only the numerical constants change. Note also that Lemma~\ref{tu:U-weight}(3) improves to $\tilde f\ge f-L\tau/2$
for this $\tilde f$; the weaker $f-L\tau$ is kept. For the second half (Section~\ref{tu:L-sec-sub}, ``Mass near the corners''):
$\tilde f>0$ where $\varepsilon>\frac32\eta$, so $\phi_{\min}(\eta)=\inf_{\varepsilon\ge2\eta}\Phi>0$."""))

R.append((r"""whose ingredients (W1) and (W3) are
asserted to exist and not constructed;""",
r"""whose ingredients (W1) and (W3) are
constructed in Lemma~\ref{tu:U-W13};"""))

for old, new in R:
    c = s.count(old)
    if c != 1:
        print("NOT UNIQUE/NOT FOUND", c, old[:80]); sys.exit(1)
    s = s.replace(old, new)
open(p, "w").write(s)
print("upper patched", len(R))
