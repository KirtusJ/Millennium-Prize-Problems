"""apply_repairs.py -- w1-fin (task T185). Applies the referees' repairs to the note, minimally, in place.

Usage: python3 prog/apply_repairs.py <result-file>      (run from /home/user/z4-workers/w1-fin)
Reads the untouched originals in orig_note/, writes the patched tun_upper.tex / tun_lower.tex to note/,
writes the change log (file, item, old, new) to <result-file> (opened with mode "x", never overwritten).

Predicates, fixed before the first run:
  E1  every edit's old string occurs in the file exactly the expected number of times (default 1)
      at the moment it is applied (exact string match; tolerance: none).
  E2  after all edits, tun_lower.tex contains no "\\varepsilon(\\sin " (notation nit of REFEREE_lower).
  E3  main.tex and preamble.tex are byte-identical to the originals (no edit lists them).
  C1  the explicit chi of the patched Section 8.1 satisfies, on a grid of 200001 points of [0,pi], for
      eta in {0.4,0.2,0.1,0.05,0.01}: chi=0 on [0,a_-/2] u [pi-a_-/4,pi], chi=1 on [a_-,pi-a_-/2], 0<=chi<=1.
      Tolerance 1e-12 (the step function is evaluated in closed form; only rounding).
  C2  the explicit Theta-tilde satisfies: Theta-tilde=Theta on [0,pi/2] (tolerance 1e-9: composite Simpson with
      200000 panels on a smooth integrand, error measured by halving < 1e-11), 0<=Theta-tilde'<=theta_0,
      Theta-tilde'=0 on [3pi/4,pi] (exact zeros, tolerance 0), Theta-tilde nondecreasing.
  C3  for the weight of Lemma tu:U-W13 with delta=tau=1/2: phi_min(eta)=inf_{eps(a)>=2 eta} Phi(a) > 0,
      for the same eta values (grid of 200001 points; we report the value; predicate: > 1e-12).
  C4  the window of (W3) with tau=1/2 does not meet I: 2 asinh(cos(1/4)) > eta for eta<=0.4 (exact arithmetic
      in double; margin reported).
  M1  measured only: the bound on H of Lemma tu:U-W13 with delta=tau=1/2, at the same eta values.
Fixed seeds: no randomness is used.
Exit code 0 iff every predicate is met; 1 otherwise (failures are printed, not hidden).
"""
import math, sys, os
import numpy as np

ROOT = os.getcwd()
ORIG = os.path.join(ROOT, "orig_note")
OUT = os.path.join(ROOT, "note")

# ---------------------------------------------------------------- edit list
# (file, item, old, new[, count])
E = []
def ed(f, item, old, new, count=1):
    E.append((f, item, old, new, count))

U, Lo = "tun_upper.tex", "tun_lower.tex"

# --- upper: Jentzsch (REFEREE_upper #1 nit)
ed(U, "upper #1 (nit: name Jentzsch's theorem)",
r"""(Hilbert--Schmidt), its largest eigenvalue $\lambda:=\|T\|$ is simple, and its eigenvector can be chosen
strictly positive.""",
r"""(Hilbert--Schmidt), and by Jentzsch's theorem (the Perron--Frobenius theorem for integral operators with
a strictly positive continuous kernel) its largest eigenvalue $\lambda:=\|T\|$ is simple, and its eigenvector
can be chosen strictly positive.""")

# --- upper: status paragraph (REFEREE_upper #4 DEFECT; brief (i))
ed(U, "upper #4 DEFECT (status paragraph); brief (i)",
r"""\item \emph{Status.} Theorem~\ref{tu:U-thm} is proved in writing in this note. The proofs were written
by sessions of one model family (Claude, Anthropic), working as a director and workers, and were
attacked by other sessions of the same family. Agreement among them is not independent review. The
note has not been read by a session of another model lineage or by a person.""",
r"""\item \emph{Status.} Both halves of Theorem~\ref{tu:U-thm} are written out in this note:
$\liminf\ge c^*$ in Sections~\ref{tu:U-sec-kernel}--\ref{tu:U-sec-agmon} (Theorem~\ref{tu:U-main}) and
$\limsup\le c^*$ in Sections~\ref{tu:L-sec-exact}--\ref{tu:L-sec-assembly} (Theorem~\ref{tu:L-main}). After the
patches no step of the second half is conditional on anything that is not on the page: it uses the results of
the first half, proved in Sections~\ref{tu:U-sec-kernel}--\ref{tu:U-sec-agmon}, and the gap bounds of
Lemma~\ref{tu:L-gauss} and the $\Delta h$ bound of Lemma~\ref{tu:L-taylor}, on which an earlier status line made
Theorem~\ref{tu:L-main} conditional and which are now derived in Section~\ref{tu:L-sec-sub}. This is all that is
established: a complete written proof that has been checked only by its authors' model family. All of it was
written, patched and refereed by sessions of one model family (Claude, Anthropic), working as director,
workers, challengers and referees, and by no one else. Agreement among them is not independent review. The
note has not been read by a session of another model lineage or by a person.""")

# --- upper: thresholds item (REFEREE_upper #5 imprecision, #23; brief (i) thresholds)
ed(U, "upper #5 / #23 (numbers of the thresholds item; tau, delta stated); brief (i)",
r"""$\sin a\in[0.1,1]$ only for $\beta$ of order $10^{13}$ to $10^{14}$; at $\beta\le4096$ its deficit is $8.6$
to $14$ nats.""",
r"""$\sin a\in[0.1,1]$ only from $\beta\approx2.0\cdot10^{13}$ on (with $\tau=\delta=\beta^{-1/3}$;
Remark~\ref{tu:U-F-num}); for $100\le\beta\le4096$ its deficit is $7.3$ to $14.2$ nats. All explicit
thresholds of this note are far beyond any $\beta$ at which $T$ can be computed.""")

# --- upper: Lean item (brief (i))
ed(U, "brief (i) (Lean covers scalar lemmas only; Lean files not part of the note)",
r"""working files. Nothing else in this note is formalised. These Lean files were not compiled in the
preparation of this text.""",
r"""working files. Lean covers these scalar lemmas only; the remarks ``Lean-checked'' elsewhere in this note
also refer to scalar steps in the working files. Nothing else in this note is formalised. The Lean files are
not part of this note and were not compiled in the preparation of this text.""")

# --- upper: Remark tu:U-R-rem (REFEREE_upper #11 DEFECT)
ed(U, "upper #11 DEFECT (Remark tu:U-R-rem: restrict to beta>=256)",
r"""$a=0.05,0.1,0.3,0.6,1.0,\pi/2$, the same at $\beta=64,256,1024$ to within $2\%$. A challenger""",
r"""$a=0.05,0.1,0.3,0.6,1.0,\pi/2$, the same at $\beta=256,1024$ to within $2\%$ (not at $\beta=64$: a referee
recomputation gives $c=1.04$ and $0.98$ at $a=0.05$ and $0.1$ there). A challenger""")

# --- upper: H-tilde at 0 (REFEREE_upper #20 nit)
ed(U, "upper #20 (nit: H-tilde_delta(0) undefined)",
r"""and $\tilde H_\delta$ is nonincreasing in $z$.
\end{lemma}""",
r"""and $\tilde H_\delta$ is nonincreasing in $z$. (We put $\tilde H_\delta(0):=1$; the bound and the monotonicity
then hold for $z\ge0$, since $e^{-0}I_0(0)=1$. The value at $0$ occurs in Theorem~\ref{tu:U-F-master} only
on the null set $r'=1$.)
\end{lemma}""")

# --- upper: Remark tu:U-F-num (REFEREE_upper #23 DEFECT)
ed(U, "upper #23 DEFECT (Remark tu:U-F-num: state tau, delta; correct two numbers)",
r"""$\beta_0(\eta)$ is explicit but large. For $\eta=0.2$ (so $s_0=0.1$) the deficit $\log\max(M_{\rm in},AM_{\rm out})$, maximised
over $s\in[0.1,1]$ on a grid, first falls below $0.2$ at $\beta\approx2.2\cdot10^{13}$ (worst $s=0.1$); at $s=0.1$,
$\beta=10^{12}$ it is $24.9$; at $s=1$, $\beta=10^{11}$ it is $5\cdot10^{-4}$. At $\beta\le4096$ the deficit is $8.6$ to $14$ nats.""",
r"""$\beta_0(\eta)$ is explicit but large. For $\eta=0.2$ (so $s_0=0.1$) and $\tau=\delta=\beta^{-1/3}$ (as in
Corollary~\ref{tu:U-F-cor}(b)), the deficit $\log\max(M_{\rm in},AM_{\rm out})$, maximised
over $s\in[0.1,1]$ on a grid, first falls below $0.2$ at $\beta\approx2.03\cdot10^{13}$ (worst $s=0.1$); at $s=0.1$,
$\beta=10^{12}$ it is $24.9$; at $s=1$, $\beta=10^{11}$ it is $5\cdot10^{-4}$. For $100\le\beta\le4096$ the deficit is $7.33$ to
$14.23$ nats (for $\beta\le125$ the hypothesis $\tau<1/5$ fails, so there this is only a value of the formula). (Corrected
by a referee recomputation; the working file had $2.2\cdot10^{13}$ and $8.6$ to $14$.)""")
ed(U, "upper #23 (provenance of the corrected numbers)",
r"""$-4.1\cdot10^{-4}$ and $-2\cdot10^{-4}$ at $\beta=4096$ for $s\ge0.1$). These are measurements by the author and a challenger
of the working file, not recomputed here.""",
r"""$-4.1\cdot10^{-4}$ and $-2\cdot10^{-4}$ at $\beta=4096$ for $s\ge0.1$). These are measurements by the author and a challenger
of the working file, recomputed only by a referee of the same model family (who reproduced them with the corrections
above).""")

# --- upper: Lemma tu:U-weight (1) at pi/2 (REFEREE_upper #27 nit)
ed(U, "upper #27 (nit: tu:U-weight(1) at a=pi/2)",
r"""$\Phi'^2/2\le(1-\delta)^2f'^2/2\le(1-\delta)^2\rho_\eta(\varepsilon)\le(1-\delta)^2(\varepsilon-\eta)$, using (W3) and (W1).""",
r"""$\Phi'^2/2\le(1-\delta)^2f'^2/2\le(1-\delta)^2\rho_\eta(\varepsilon)\le(1-\delta)^2(\varepsilon-\eta)$, using (W3) and (W1).
At $a=\pi/2$, where $f'$ is not defined, the bound follows by continuity of $\tilde f'$ (for the $\tilde f$ of
Lemma~\ref{tu:U-W13}, $\tilde f'(\pi/2)=0$).""")

# --- upper: Remark tu:U-uses (REFEREE_upper #34 nit)
ed(U, "upper #34 (nit: name tu:U-schur and tu:U-A in Remark tu:U-uses)",
r"""constructed in Lemma~\ref{tu:U-W13}; Proposition~\ref{tu:U-B}(1) for $u=g$; Lemma~\ref{tu:U-flux}; and the lower""",
r"""constructed in Lemma~\ref{tu:U-W13}; Proposition~\ref{tu:U-B}(1) for $u=g$, and through it
Lemmas~\ref{tu:U-schur} and~\ref{tu:U-A}; Lemma~\ref{tu:U-flux}; and the lower""")

# --- lower: notation eps(sin a) -> eps(a) (REFEREE_lower notation nit 1); count fixed after inspection
ed(Lo, "lower notation nit (epsilon(sin a) -> epsilon(a), 11 occurrences)",
r"""\varepsilon(\sin """, r"""\varepsilon(""", count=11)

# --- lower: q at S=0 (REFEREE_lower #10 nit)
ed(Lo, "lower #10 (nit: q at S=0)",
r"""S^2:=|u_1|^2+|u_2|^2,\qquad w:=u_1\times u_2,\qquad q:=|w|^2/S^2,\qquad\text{so } V=2\beta S^2q .
\]""",
r"""S^2:=|u_1|^2+|u_2|^2,\qquad w:=u_1\times u_2,\qquad q:=|w|^2/S^2,\qquad\text{so } V=2\beta S^2q .
\]
(At $S=0$ we put $q:=0$; there $w=0$ and $V=0$.)""")

# --- lower: M4 phi_min > 0 (REFEREE_lower #8 GAP; brief (iii))
ed(Lo, "lower #8 GAP (tu:L-M4: phi_min(eta)>0); brief (iii)",
r"""$\|e^{\sqrt\beta\Phi(a_2)}u\|^2\le C(\eta)$. The proof of (B) uses no positivity of $u$, so it applies to
$u=f$.""",
r"""$\|e^{\sqrt\beta\Phi(a_2)}u\|^2\le C(\eta)$ (this is Proposition~\ref{tu:U-B}(2)). The proof of (B) uses no positivity of $u$, so it applies to
$u=f$. That $\phi_{\min}(\eta)>0$ is not stated in Lemma~\ref{tu:U-weight}; it follows from the construction of
Lemma~\ref{tu:U-W13}: $\Phi=(1-\delta)\tilde f$ with $\tilde f'=p\chi$ on $[0,\pi/2]$, where $p>0$ wherever
$\varepsilon>\frac32\eta$ (there $\psi>0$) and $\chi>0$ on $[0,\pi/2)$. Since $\varepsilon$ is increasing on $[0,\pi/2]$, every
$a\le\pi/2$ with $\varepsilon(a)\ge2\eta$ has $\varepsilon>\frac32\eta$ on an interval $(a',a)$ with $a'<a$, so $\tilde f(a)>0$; by symmetry
$\tilde f>0$ on the compact set $\{\varepsilon\ge2\eta\}$, which is nonempty ($2\eta\le0.8<\varepsilon(\pi/2)$), and the continuous
$\Phi$ attains a positive minimum there.""")

# --- lower: Taylor Delta S^2 definition (REFEREE_lower notation nit 4)
ed(Lo, "lower notation nit (Delta S^2 is a definition)",
r"""$\Delta S^2\le2\sum_i(\sin a_i\,r_b+r_b^2)$, and $\Delta h\le""",
r"""$\Delta S^2:=2\sum_i(\sin a_i\,r_b+r_b^2)$, and $\Delta h\le""")

# --- lower: E13 status (brief (i) reconcile status lines)
ed(Lo, "brief (i) (E13 status line reconciled with the gap bounds now on the page)",
r"""\noindent\emph{Status.} Proved in writing in the working file and checked by one challenger (all items
stand except the gap bounds, not checked);""",
r"""\noindent\emph{Status.} Proved in writing in the working file and checked by one challenger (all items
stand except the gap bounds, which that challenger did not check; they are now derived on the page in
Lemma~\ref{tu:L-gauss}, and a referee of the same model family rederived them);""")

# --- lower: S4 step 4 a_1 rename (REFEREE_lower notation nit 3)
ed(Lo, "lower notation nit (a_1 = e^{-3eta/4} renamed bar a in S4 Step 4)",
r"""$u=a_1x_c$, $a_1:=e^{-3\eta/4}$, $v=(Pa_1^{-\gamma})^{k}$ (note $1/(1-\gamma)=k$),
\[
Px_c^\gamma\le\gamma a_1x_c+\tfrac1kP^ka_1^{1-k}\le a_1x_c+R,""",
r"""$u=\bar ax_c$, $\bar a:=e^{-3\eta/4}$, $v=(P\bar a^{-\gamma})^{k}$ (note $1/(1-\gamma)=k$),
\[
Px_c^\gamma\le\gamma\bar ax_c+\tfrac1kP^k\bar a^{1-k}\le\bar ax_c+R,""")
ed(Lo, "lower notation nit (a_1 renamed bar a, cont.)",
r"""(using $k>1$). Hence, with $a\le a_1$,
\[
a(1-x_c)+Px_c^\gamma\le a_1(1-x_c)+a_1x_c+R\le1-2m_0+m_0=1-m_0 .""",
r"""(using $k>1$). Hence, with $a\le\bar a$,
\[
a(1-x_c)+Px_c^\gamma\le\bar a(1-x_c)+\bar ax_c+R\le1-2m_0+m_0=1-m_0 .""")

# --- lower: ansatz mu wording (part of #25)
ed(Lo, "lower #25 (mu is defined, not fixed, in Section 8.1)",
r"""$\varphi=\max(\varphi_L,\varphi_R)$, with $\mu>0$ fixed in Section~\ref{tu:L-sec-assembly};""",
r"""$\varphi=\max(\varphi_L,\varphi_R)$, with $\mu>0$ defined in Section~\ref{tu:L-sec-assembly} (it depends on $\beta$);""")

# --- lower: Section 8.1 parameter list (REFEREE_lower #25 DEFECT, #15 nit; brief (iv))
ed(Lo, "lower #25 DEFECT (8.1: M fixed as a function of eta); brief (iv)",
r"""\item $M=M(\eta)$ with $M^2\ge M_A^2(\eta)$ (condition""",
r"""\item $M=M(\eta)$ with $M^2:=M_A^2(\eta)$, so $M^2\ge M_A^2(\eta)$ (condition""")
ed(Lo, "lower #25 DEFECT, #15 nit (8.1: delta, tau, (W1)/(W3), chi, Theta-tilde, C; mu moved out); brief (iv)",
r"""\item $\eta'=a_-$ (change C1);
\item $\mu:=\exp\big(-35(a_-+r_0)\sqrt\beta-R_\beta\big)$ (Corollary~\ref{tu:L-H4cor}).
\end{itemize}""",
r"""\item $\eta'=a_-$ (change C1);
\item the weight of Proposition~\ref{tu:U-B}: $\delta=\tau=\frac12$ in (W3), (W4) (these are the parameters of
\S\ref{tu:U-sec-weight}, not the $\delta=\tau=\beta^{-1/3}$ of Corollary~\ref{tu:U-F-cor}(b)), and $\rho_\eta$, $\tilde f$ the explicit
functions of Lemma~\ref{tu:U-W13} with this $\tau$, so $\Phi=\frac12\tilde f$; Proposition~\ref{tu:U-B} applies since
$\eta\le0.4\le\frac12$ and $\delta,\tau\in(0,1)$;
\item with the fixed $C^\infty$ step $s_\infty(t)=e^{-1/t}/(e^{-1/t}+e^{-1/(1-t)})$ on $(0,1)$, $s_\infty=0$ for $t\le0$,
$s_\infty=1$ for $t\ge1$:
$\chi(a):=s_\infty\big(\frac{a-a_-/2}{a_-/2}\big)\,s_\infty\big(\frac{\pi-a_-/4-a}{a_-/4}\big)$ and
$\tilde\Theta(a):=\int_0^a\frac{\theta_0b}{\sqrt{b^2+\ell^2}}\,s_\infty\big(\frac{3\pi/4-b}{\pi/4}\big)\,db$; they have the properties
required in Section~\ref{tu:L-ansatz} ($\tilde\Theta=\Theta$ on $[0,\pi/2]$, $\tilde\Theta'=0$ on $[3\pi/4,\pi]$);
\item $C=1$ in $L=\sqrt{C\log\beta}$ of Proposition~\ref{tu:L-E13} (any fixed $C>0$ would do).
\end{itemize}
The amplitude $\mu:=\exp\big(-35(a_-+r_0)\sqrt\beta-R_\beta\big)$ (Corollary~\ref{tu:L-H4cor}) is not among the fixed parameters:
it depends on $\beta$ (through $\sqrt\beta$ and $R_\beta$). No threshold below depends on it.""")
ed(Lo, "lower #25 DEFECT (8.1: every beta_0 a function of eta alone, checked threshold by threshold); brief (iv)",
r"""$\int_{C_\eta\cap\{V\le1\}}f^2\ge1/2$ (Lemma~\ref{tu:L-M4}); and the finitely many ``$\beta$ large'' conditions below.""",
r"""$\int_{C_\eta\cap\{V\le1\}}f^2\ge1/2$ (Lemma~\ref{tu:L-M4}); and the finitely many ``$\beta$ large'' conditions below.
With the choices above every one of these thresholds is a function of $\eta$ alone: the constants of
Proposition~\ref{tu:L-E13} and $m(\eta)$ depend on $\eta',r_0,\ell,\theta_0,M,C$ and on $H_\Psi,\Lambda,\tilde\Theta$, which are now
fixed functions of $\eta$; the conditions of Lemma~\ref{tu:L-balls} on $\rho_B,r_0,\ell,\theta_0$; the threshold of
Lemma~\ref{tu:L-L4} on $\eta$; that of Lemma~\ref{tu:U-F} on $\eta/2$; $\beta_1(\eta,\delta,\tau)$ of (B) on $\eta$, $\delta=\tau=\frac12$ and
the explicit choices of Lemma~\ref{tu:U-W13} (through $\beta_0(\eta/4)$ of Lemma~\ref{tu:U-F} and $\omega(\beta)$, which depends on $H$);
and $m_B\ge\frac18$, $\int f^2\ge\frac12$ on $C(\eta)$, $\phi_{\min}(\eta)$ and $\varkappa=1$.""")

# --- lower: S (set) renamed mathcal S in Section 8 (REFEREE_lower notation nit 2)
ed(Lo, "lower notation nit (set S renamed mathcal S in Section 8)",
r"""$\int_Sf^2\ge\frac12$ and $m_B\ge\frac18$, where $S:=C_\eta\cap\{V\le1\}$.
\item Corollary~\ref{tu:L-H4cor} gives $g\ge\mu$ on $D_M\cup\sigma_1D_M\supset R_{\rm well}$ and on $S$.""",
r"""$\int_{\mathcal S}f^2\ge\frac12$ and $m_B\ge\frac18$, where $\mathcal S:=C_\eta\cap\{V\le1\}$ (a set; not the radius $S$).
\item Corollary~\ref{tu:L-H4cor} gives $g\ge\mu$ on $D_M\cup\sigma_1D_M\supset R_{\rm well}$ and on $\mathcal S$.""")
ed(Lo, "lower notation nit (set S renamed, cont.)",
r"""$S$ is $\sigma_1$-invariant, since $\varepsilon(a_1)$ and $V$ are. Corollary~\ref{tu:L-B} needs, for each $x\in S$, centres""",
r"""$\mathcal S$ is $\sigma_1$-invariant, since $\varepsilon(a_1)$ and $V$ are. Corollary~\ref{tu:L-B} needs, for each $x\in\mathcal S$, centres""")
ed(Lo, "lower #26 nit (8.2: chains padded to a common n)",
r"""The number of steps is $n\le(\pi+2a_-)\sqrt\beta/d+O(\beta^{1/4})=O(\sqrt\beta)$.""",
r"""The number of steps is $n\le(\pi+2a_-)\sqrt\beta/d+O(\beta^{1/4})=O(\sqrt\beta)$. Lemma~\ref{tu:L-Pc} needs one $n$ for all
$x\in\mathcal S$; the chains are padded with zero steps to this common bound, as in Lemma~\ref{tu:L-geom}.""")
ed(Lo, "lower #26 nit (mu' defined)",
r"""g(z)\ge\min\big(\mu',\ \tfrac\mu4e^{-1.5\rho_B^2}e^{-\sqrt\beta\Psi(\pi/2)}\big),\qquad
-\log\mu'\le35a_-\sqrt\beta+R'_\beta,""",
r"""g(z)\ge\min\big(\mu',\ \tfrac\mu4e^{-1.5\rho_B^2}e^{-\sqrt\beta\Psi(\pi/2)}\big),\qquad
\mu':=e^{-35a_-\sqrt\beta-R'_\beta},""")
ed(Lo, "lower notation nit (set S renamed, cont.)",
r"""$n=O(\sqrt\beta)$; $|S|\le1$.""",
r"""$n=O(\sqrt\beta)$; $|\mathcal S|\le1$.""")
ed(Lo, "lower notation nit (set S renamed, cont.)",
r"""Corollary~\ref{tu:L-B} with $\sigma=\sigma_1$, the set $S$,
$r_\beta=\rho_B/\sqrt\beta$, and Lemma~\ref{tu:L-balls} (with $g\ge\mu$ on $S$ for the end points) give
\[
-\log\Delta\le2\sup_{\rm balls\cup S}(-\log g)+O(\log\beta)-\log\Big(2\int_Sf^2\Big)""",
r"""Corollary~\ref{tu:L-B} with $\sigma=\sigma_1$, the set $\mathcal S$,
$r_\beta=\rho_B/\sqrt\beta$, and Lemma~\ref{tu:L-balls} (with $g\ge\mu$ on $\mathcal S$ for the end points) give
\[
-\log\Delta\le2\sup_{\rm balls\cup\mathcal S}(-\log g)+O(\log\beta)-\log\Big(2\int_{\mathcal S}f^2\Big)""")
ed(Lo, "lower notation nit (set S renamed, cont.)",
r"""using $\int_Sf^2\ge\frac12$ and $-\log\mu\le35(a_-+r_0)\sqrt\beta+R_\beta$.""",
r"""using $\int_{\mathcal S}f^2\ge\frac12$ and $-\log\mu\le35(a_-+r_0)\sqrt\beta+R_\beta$.""")

# --- lower: main theorem status (brief (i) reconcile; REFEREE_upper #4 cross-reference)
ed(Lo, "brief (i) + upper #4 (status line of tu:L-main reconciled)",
r"""\noindent\emph{Status.} Proved in writing, conditional on the results of the first half (Lemmas~\ref{tu:U-kernel},
\ref{tu:U-K}, \ref{tu:U-R}, \ref{tu:U-F}, Proposition~\ref{tu:U-B}), on the gap bounds of Lemma~\ref{tu:L-gauss} and the $\Delta h$
bound of Lemma~\ref{tu:L-taylor} as stated. (The absorption step in Lemma~\ref{tu:L-S4} is now quantified.) Not independently
reviewed: the working files and the assembly were written by sessions of the same model family.""",
r"""\noindent\emph{Status.} Proved in writing. It uses the results of the first half (Lemmas~\ref{tu:U-kernel},
\ref{tu:U-K}, \ref{tu:U-R}, \ref{tu:U-F}, Proposition~\ref{tu:U-B}), proved in Sections~\ref{tu:U-sec-kernel}--\ref{tu:U-sec-agmon}, and the gap bounds of
Lemma~\ref{tu:L-gauss} and the $\Delta h$ bound of Lemma~\ref{tu:L-taylor}, which are derived in Section~\ref{tu:L-sec-sub}. (An earlier
version of this line said ``conditional on'' these; they are now on the page. The absorption step in Lemma~\ref{tu:L-S4} is now
quantified.) Not independently reviewed: the working files, the assembly, the patches and the referee reports were written by
sessions of the same model family (Claude, Anthropic).""")


def main():
    out = sys.argv[1]
    log = open(out, "x")
    ok = True
    def P(name, cond, msg):
        nonlocal ok
        ok &= bool(cond)
        line = f"{name}: {'MET' if cond else 'FAILED'} {msg}"
        print(line); log.write(line + "\n")

    texts = {f: open(os.path.join(ORIG, f)).read() for f in (U, Lo)}
    changes = []
    for i, (f, item, old, new, count) in enumerate(E, 1):
        n = texts[f].count(old)
        P(f"E1[{i}]", n == count, f"{f} occurrences={n} expected={count} ({item})")
        if n == count:
            line = texts[f][:texts[f].index(old)].count("\n") + 1
            texts[f] = texts[f].replace(old, new)
            changes.append((i, f, line, item, old, new, count))
    P("E2", "\\varepsilon(\\sin " not in texts[Lo], "no epsilon(sin ...) left in tun_lower.tex")
    for f in ("main.tex", "preamble.tex"):
        P("E3", open(os.path.join(ORIG, f), "rb").read() == open(os.path.join(OUT, f), "rb").read(), f)
    for f in (U, Lo):
        with open(os.path.join(OUT, f), "w") as fh:
            fh.write(texts[f])

    # ---- C1..C4, M1
    def sinf(t):
        t = np.asarray(t, float)
        r = np.where(t >= 1, 1.0, 0.0)
        m = (t > 0) & (t < 1)
        tm = t[m]
        a, b = np.exp(-1 / tm), np.exp(-1 / (1 - tm))
        r[m] = a / (a + b)
        return r
    L = math.sqrt(4 * math.asinh(1))
    for eta in (0.4, 0.2, 0.1, 0.05, 0.01):
        am = math.asin(math.sinh(eta)); r0 = math.sqrt(eta * math.sin(am) / 4); ell = r0 / 3; th0 = 0.5
        a = np.linspace(0, math.pi, 200001)
        chi = sinf((a - am / 2) / (am / 2)) * sinf((math.pi - am / 4 - a) / (am / 4))
        z = (a <= am / 2) | (a >= math.pi - am / 4); o = (a >= am) & (a <= math.pi - am / 2)
        P("C1", np.all(np.abs(chi[z]) <= 1e-12) and np.all(np.abs(chi[o] - 1) <= 1e-12) and chi.min() >= -1e-12 and chi.max() <= 1 + 1e-12,
          f"eta={eta}")
        dTh = th0 * a / np.sqrt(a**2 + ell**2) * sinf((3 * math.pi / 4 - a) / (math.pi / 4))
        h = a[1] - a[0]
        cum = np.concatenate([[0], np.cumsum((dTh[1:] + dTh[:-1]) / 2 * h)])  # trapezoid for monotonicity/shape
        half = a <= math.pi / 2
        # Simpson check of Theta-tilde(pi/2) vs Theta(pi/2)
        k = np.searchsorted(a, math.pi / 2)
        aa = a[:k + 1]; ff = dTh[:k + 1]
        n = len(aa) - 1
        if n % 2: aa, ff, n = aa[:-1], ff[:-1], n - 1
        simp = (aa[1] - aa[0]) / 3 * (ff[0] + ff[-1] + 4 * ff[1:-1:2].sum() + 2 * ff[2:-1:2].sum())
        Th = th0 * (math.sqrt(aa[-1]**2 + ell**2) - ell)
        P("C2", abs(simp - Th) <= 1e-9 and dTh.min() >= 0 and dTh.max() <= th0 and np.all(dTh[a >= 3 * math.pi / 4] == 0)
          and np.all(np.diff(cum) >= 0), f"eta={eta} |Simpson-Theta|={abs(simp-Th):.2e}")
        # W13 weight, delta=tau=1/2
        tau = 0.5; delta = 0.5
        b = np.linspace(0, math.pi / 2, 200001)
        eps = 2 * np.arcsinh(np.sin(b))
        t = (eps - eta) / eta
        s2 = np.clip(2 / 3 * (t - 0.5), 0, 1); psi = 3 * s2**2 - 2 * s2**3
        g = np.sqrt(np.clip(eps - eta, 0, None)) * psi
        p = math.sqrt(2) * g
        s3 = np.clip((math.pi / 2 - b) / (tau / 2), 0, 1); chiW = 3 * s3**2 - 2 * s3**3
        integ = p * chiW
        ft = np.concatenate([[0], np.cumsum((integ[1:] + integ[:-1]) / 2 * (b[1] - b[0]))])
        Phi = (1 - delta) * ft
        sel = eps >= 2 * eta
        phimin = Phi[sel].min()
        P("C3", phimin > 1e-12, f"eta={eta} phi_min~{phimin:.4e} (attained at a={b[sel][Phi[sel].argmin()]:.4f})")
        Hb = (1 - delta) * max(6 / math.sqrt(eta) + 3 * L / tau, L / math.sinh(3 * eta / 4))
        line = f"M1: measured only eta={eta} H<= {Hb:.4f}"; print(line); log.write(line + "\n")
    marg = 2 * math.asinh(math.cos(0.25)) - 0.4
    P("C4", marg > 0, f"2asinh(cos(1/4)) - 0.4 = {marg:.4f}")

    log.write("\n# CHANGE LOG\n")
    for (i, f, line, item, old, new, count) in changes:
        log.write(f"\n## Change {i}: {f}, original line {line}{' (x%d)' % count if count > 1 else ''}\nReferee item: {item}\n\nOld:\n```\n{old}\n```\nNew:\n```\n{new}\n```\n")
    log.write(f"\nRESULT: {'ALL MET' if ok else 'SOME FAILED'}\n")
    log.close()
    print("RESULT:", "ALL MET" if ok else "SOME FAILED")
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
