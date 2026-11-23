# CHANGES.md — w1-fin (task T185): referees' repairs applied to note/

Baseline: `orig_note/` (read-only copy of note/ as delivered). Patched: `note/tun_upper.tex`, `note/tun_lower.tex`.
`main.tex` and `preamble.tex` are unchanged (byte-identical; predicate E3).
Every change was applied by `prog/apply_repairs.py` (exact-string replacement, each old string checked to occur
exactly the expected number of times; run2 in register `pcp`, check K2, all 29 edit predicates met).
"Original line" = line number(s) in `orig_note/` of the first line of the old text (recomputed against the originals after the run).

Referee items with no change (and why):
- REFEREE_upper #6 ("I_n decreasing in n" used without proof): verdict STANDS, no repair or nit given; the note's own Remark already gives the alternative route. Not changed.
- REFEREE_upper #9 (ω values), #29 (measured excess): measurements, no repair.
- REFEREE_upper §7 items 2–5 and REFEREE_lower "look at first" items 1–5: pointers for a reader, not corrections. Upper §7 item 1 / lower item 1 are covered by Changes 2, 15 and 29 (status lines) and 19–21 (§8.1).
- REFEREE_lower #6 ((L2) not used): no repair given. Not changed.
- REFEREE_lower M7 (measured defects at β=1e4): measurement; the note already says no finite β₀ is exhibited.

Not done as the referee wrote it:
- REFEREE_lower #25 proposed "C = 1" for L=√(C log β). Done (Change 20). The same item asked that M be fixed; I set M² := M_A²(η) (Change 19). The referee did not ask for that explicitly, but without it β₀ would not be a function of η alone.
- The notation nit "ε(sin a)" occurs 11 times (the referee listed l.226, 229, 702). All 11 were changed (Change 11). Lines 249–250 are inside the proof of tu:L-M4 (notation only).

## Change 1: tun_upper.tex, original line 38
Referee item: upper #1 (nit: name Jentzsch's theorem)

Old:
```
(Hilbert--Schmidt), its largest eigenvalue $\lambda:=\|T\|$ is simple, and its eigenvector can be chosen
strictly positive.
```
New:
```
(Hilbert--Schmidt), and by Jentzsch's theorem (the Perron--Frobenius theorem for integral operators with
a strictly positive continuous kernel) its largest eigenvalue $\lambda:=\|T\|$ is simple, and its eigenvector
can be chosen strictly positive.
```

## Change 2: tun_upper.tex, original line 84
Referee item: upper #4 DEFECT (status paragraph); brief (i)

Old:
```
\item \emph{Status.} Theorem~\ref{tu:U-thm} is proved in writing in this note. The proofs were written
by sessions of one model family (Claude, Anthropic), working as a director and workers, and were
attacked by other sessions of the same family. Agreement among them is not independent review. The
note has not been read by a session of another model lineage or by a person.
```
New:
```
\item \emph{Status.} Both halves of Theorem~\ref{tu:U-thm} are written out in this note:
$\liminf\ge c^*$ in Sections~\ref{tu:U-sec-kernel}--\ref{tu:U-sec-agmon} (Theorem~\ref{tu:U-main}) and
$\limsup\le c^*$ in Sections~\ref{tu:L-sec-exact}--\ref{tu:L-sec-assembly} (Theorem~\ref{tu:L-main}). After the
patches no step of the second half is conditional on anything that is not on the page: it uses the results of
the first half, proved in Sections~\ref{tu:U-sec-kernel}--\ref{tu:U-sec-agmon}, and the gap bounds of
Lemma~\ref{tu:L-gauss} and the $\Delta h$ bound of Lemma~\ref{tu:L-taylor}, on which an earlier status line made
Theorem~\ref{tu:L-main} conditional and which are now derived in Section~\ref{tu:L-sec-sub}. This is all that is
established: a complete written proof that has been checked only by its authors' model family. All of it was
written, patched and refereed by sessions of one model family (Claude, Anthropic), working as director,
workers, challengers and referees, and by no one else. Agreement among them is not independent review. The
note has not been read by a session of another model lineage or by a person.
```

## Change 3: tun_upper.tex, original line 92
Referee item: upper #5 / #23 (numbers of the thresholds item; tau, delta stated); brief (i)

Old:
```
$\sin a\in[0.1,1]$ only for $\beta$ of order $10^{13}$ to $10^{14}$; at $\beta\le4096$ its deficit is $8.6$
to $14$ nats.
```
New:
```
$\sin a\in[0.1,1]$ only from $\beta\approx2.0\cdot10^{13}$ on (with $\tau=\delta=\beta^{-1/3}$;
Remark~\ref{tu:U-F-num}); for $100\le\beta\le4096$ its deficit is $7.3$ to $14.2$ nats. All explicit
thresholds of this note are far beyond any $\beta$ at which $T$ can be computed.
```

## Change 4: tun_upper.tex, original line 104
Referee item: brief (i) (Lean covers scalar lemmas only; Lean files not part of the note)

Old:
```
working files. Nothing else in this note is formalised. These Lean files were not compiled in the
preparation of this text.
```
New:
```
working files. Lean covers these scalar lemmas only; the remarks ``Lean-checked'' elsewhere in this note
also refer to scalar steps in the working files. Nothing else in this note is formalised. The Lean files are
not part of this note and were not compiled in the preparation of this text.
```

## Change 5: tun_upper.tex, original line 327
Referee item: upper #11 DEFECT (Remark tu:U-R-rem: restrict to beta>=256)

Old:
```
$a=0.05,0.1,0.3,0.6,1.0,\pi/2$, the same at $\beta=64,256,1024$ to within $2\%$. A challenger
```
New:
```
$a=0.05,0.1,0.3,0.6,1.0,\pi/2$, the same at $\beta=256,1024$ to within $2\%$ (not at $\beta=64$: a referee
recomputation gives $c=1.04$ and $0.98$ at $a=0.05$ and $0.1$ there). A challenger
```

## Change 6: tun_upper.tex, original line 410
Referee item: upper #20 (nit: H-tilde_delta(0) undefined)

Old:
```
and $\tilde H_\delta$ is nonincreasing in $z$.
\end{lemma}
```
New:
```
and $\tilde H_\delta$ is nonincreasing in $z$. (We put $\tilde H_\delta(0):=1$; the bound and the monotonicity
then hold for $z\ge0$, since $e^{-0}I_0(0)=1$. The value at $0$ occurs in Theorem~\ref{tu:U-F-master} only
on the null set $r'=1$.)
\end{lemma}
```

## Change 7: tun_upper.tex, original line 548
Referee item: upper #23 DEFECT (Remark tu:U-F-num: state tau, delta; correct two numbers)

Old:
```
$\beta_0(\eta)$ is explicit but large. For $\eta=0.2$ (so $s_0=0.1$) the deficit $\log\max(M_{\rm in},AM_{\rm out})$, maximised
over $s\in[0.1,1]$ on a grid, first falls below $0.2$ at $\beta\approx2.2\cdot10^{13}$ (worst $s=0.1$); at $s=0.1$,
$\beta=10^{12}$ it is $24.9$; at $s=1$, $\beta=10^{11}$ it is $5\cdot10^{-4}$. At $\beta\le4096$ the deficit is $8.6$ to $14$ nats.
```
New:
```
$\beta_0(\eta)$ is explicit but large. For $\eta=0.2$ (so $s_0=0.1$) and $\tau=\delta=\beta^{-1/3}$ (as in
Corollary~\ref{tu:U-F-cor}(b)), the deficit $\log\max(M_{\rm in},AM_{\rm out})$, maximised
over $s\in[0.1,1]$ on a grid, first falls below $0.2$ at $\beta\approx2.03\cdot10^{13}$ (worst $s=0.1$); at $s=0.1$,
$\beta=10^{12}$ it is $24.9$; at $s=1$, $\beta=10^{11}$ it is $5\cdot10^{-4}$. For $100\le\beta\le4096$ the deficit is $7.33$ to
$14.23$ nats (for $\beta\le125$ the hypothesis $\tau<1/5$ fails, so there this is only a value of the formula). (Corrected
by a referee recomputation; the working file had $2.2\cdot10^{13}$ and $8.6$ to $14$.)
```

## Change 8: tun_upper.tex, original line 553
Referee item: upper #23 (provenance of the corrected numbers)

Old:
```
$-4.1\cdot10^{-4}$ and $-2\cdot10^{-4}$ at $\beta=4096$ for $s\ge0.1$). These are measurements by the author and a challenger
of the working file, not recomputed here.
```
New:
```
$-4.1\cdot10^{-4}$ and $-2\cdot10^{-4}$ at $\beta=4096$ for $s\ge0.1$). These are measurements by the author and a challenger
of the working file, recomputed only by a referee of the same model family (who reproduced them with the corrections
above).
```

## Change 9: tun_upper.tex, original line 673
Referee item: upper #27 (nit: tu:U-weight(1) at a=pi/2)

Old:
```
$\Phi'^2/2\le(1-\delta)^2f'^2/2\le(1-\delta)^2\rho_\eta(\varepsilon)\le(1-\delta)^2(\varepsilon-\eta)$, using (W3) and (W1).
```
New:
```
$\Phi'^2/2\le(1-\delta)^2f'^2/2\le(1-\delta)^2\rho_\eta(\varepsilon)\le(1-\delta)^2(\varepsilon-\eta)$, using (W3) and (W1).
At $a=\pi/2$, where $f'$ is not defined, the bound follows by continuity of $\tilde f'$ (for the $\tilde f$ of
Lemma~\ref{tu:U-W13}, $\tilde f'(\pi/2)=0$).
```

## Change 10: tun_upper.tex, original line 866
Referee item: upper #34 (nit: name tu:U-schur and tu:U-A in Remark tu:U-uses)

Old:
```
constructed in Lemma~\ref{tu:U-W13}; Proposition~\ref{tu:U-B}(1) for $u=g$; Lemma~\ref{tu:U-flux}; and the lower
```
New:
```
constructed in Lemma~\ref{tu:U-W13}; Proposition~\ref{tu:U-B}(1) for $u=g$, and through it
Lemmas~\ref{tu:U-schur} and~\ref{tu:U-A}; Lemma~\ref{tu:U-flux}; and the lower
```

## Change 11: tun_lower.tex, original line 226,227,230,249,250,702,703,934,966 (x11)
Referee item: lower notation nit (epsilon(sin a) -> epsilon(a), 11 occurrences)

Old:
```
\varepsilon(\sin 
```
New:
```
\varepsilon(
```

## Change 12: tun_lower.tex, original line 172
Referee item: lower #10 (nit: q at S=0)

Old:
```
S^2:=|u_1|^2+|u_2|^2,\qquad w:=u_1\times u_2,\qquad q:=|w|^2/S^2,\qquad\text{so } V=2\beta S^2q .
\]
```
New:
```
S^2:=|u_1|^2+|u_2|^2,\qquad w:=u_1\times u_2,\qquad q:=|w|^2/S^2,\qquad\text{so } V=2\beta S^2q .
\]
(At $S=0$ we put $q:=0$; there $w=0$ and $V=0$.)
```

## Change 13: tun_lower.tex, original line 234
Referee item: lower #8 GAP (tu:L-M4: phi_min(eta)>0); brief (iii)

Old:
```
$\|e^{\sqrt\beta\Phi(a_2)}u\|^2\le C(\eta)$. The proof of (B) uses no positivity of $u$, so it applies to
$u=f$.
```
New:
```
$\|e^{\sqrt\beta\Phi(a_2)}u\|^2\le C(\eta)$ (this is Proposition~\ref{tu:U-B}(2)). The proof of (B) uses no positivity of $u$, so it applies to
$u=f$. That $\phi_{\min}(\eta)>0$ is not stated in Lemma~\ref{tu:U-weight}; it follows from the construction of
Lemma~\ref{tu:U-W13}: $\Phi=(1-\delta)\tilde f$ with $\tilde f'=p\chi$ on $[0,\pi/2]$, where $p>0$ wherever
$\varepsilon>\frac32\eta$ (there $\psi>0$) and $\chi>0$ on $[0,\pi/2)$. Since $\varepsilon$ is increasing on $[0,\pi/2]$, every
$a\le\pi/2$ with $\varepsilon(a)\ge2\eta$ has $\varepsilon>\frac32\eta$ on an interval $(a',a)$ with $a'<a$, so $\tilde f(a)>0$; by symmetry
$\tilde f>0$ on the compact set $\{\varepsilon\ge2\eta\}$, which is nonempty ($2\eta\le0.8<\varepsilon(\pi/2)$), and the continuous
$\Phi$ attains a positive minimum there.
```

## Change 14: tun_lower.tex, original line 437
Referee item: lower notation nit (Delta S^2 is a definition)

Old:
```
$\Delta S^2\le2\sum_i(\sin a_i\,r_b+r_b^2)$, and $\Delta h\le
```
New:
```
$\Delta S^2:=2\sum_i(\sin a_i\,r_b+r_b^2)$, and $\Delta h\le
```

## Change 15: tun_lower.tex, original line 612
Referee item: brief (i) (E13 status line reconciled with the gap bounds now on the page)

Old:
```
\noindent\emph{Status.} Proved in writing in the working file and checked by one challenger (all items
stand except the gap bounds, not checked);
```
New:
```
\noindent\emph{Status.} Proved in writing in the working file and checked by one challenger (all items
stand except the gap bounds, which that challenger did not check; they are now derived on the page in
Lemma~\ref{tu:L-gauss}, and a referee of the same model family rederived them);
```

## Change 16: tun_lower.tex, original line 718
Referee item: lower notation nit (a_1 = e^{-3eta/4} renamed bar a in S4 Step 4)

Old:
```
$u=a_1x_c$, $a_1:=e^{-3\eta/4}$, $v=(Pa_1^{-\gamma})^{k}$ (note $1/(1-\gamma)=k$),
\[
Px_c^\gamma\le\gamma a_1x_c+\tfrac1kP^ka_1^{1-k}\le a_1x_c+R,
```
New:
```
$u=\bar ax_c$, $\bar a:=e^{-3\eta/4}$, $v=(P\bar a^{-\gamma})^{k}$ (note $1/(1-\gamma)=k$),
\[
Px_c^\gamma\le\gamma\bar ax_c+\tfrac1kP^k\bar a^{1-k}\le\bar ax_c+R,
```

## Change 17: tun_lower.tex, original line 722
Referee item: lower notation nit (a_1 renamed bar a, cont.)

Old:
```
(using $k>1$). Hence, with $a\le a_1$,
\[
a(1-x_c)+Px_c^\gamma\le a_1(1-x_c)+a_1x_c+R\le1-2m_0+m_0=1-m_0 .
```
New:
```
(using $k>1$). Hence, with $a\le\bar a$,
\[
a(1-x_c)+Px_c^\gamma\le\bar a(1-x_c)+\bar ax_c+R\le1-2m_0+m_0=1-m_0 .
```

## Change 18: tun_lower.tex, original line 308
Referee item: lower #25 (mu is defined, not fixed, in Section 8.1)

Old:
```
$\varphi=\max(\varphi_L,\varphi_R)$, with $\mu>0$ fixed in Section~\ref{tu:L-sec-assembly};
```
New:
```
$\varphi=\max(\varphi_L,\varphi_R)$, with $\mu>0$ defined in Section~\ref{tu:L-sec-assembly} (it depends on $\beta$);
```

## Change 19: tun_lower.tex, original line 940
Referee item: lower #25 DEFECT (8.1: M fixed as a function of eta); brief (iv)

Old:
```
\item $M=M(\eta)$ with $M^2\ge M_A^2(\eta)$ (condition
```
New:
```
\item $M=M(\eta)$ with $M^2:=M_A^2(\eta)$, so $M^2\ge M_A^2(\eta)$ (condition
```

## Change 20: tun_lower.tex, original line 941
Referee item: lower #25 DEFECT, #15 nit (8.1: delta, tau, (W1)/(W3), chi, Theta-tilde, C; mu moved out); brief (iv)

Old:
```
\item $\eta'=a_-$ (change C1);
\item $\mu:=\exp\big(-35(a_-+r_0)\sqrt\beta-R_\beta\big)$ (Corollary~\ref{tu:L-H4cor}).
\end{itemize}
```
New:
```
\item $\eta'=a_-$ (change C1);
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
it depends on $\beta$ (through $\sqrt\beta$ and $R_\beta$). No threshold below depends on it.
```

## Change 21: tun_lower.tex, original line 948
Referee item: lower #25 DEFECT (8.1: every beta_0 a function of eta alone, checked threshold by threshold); brief (iv)

Old:
```
$\int_{C_\eta\cap\{V\le1\}}f^2\ge1/2$ (Lemma~\ref{tu:L-M4}); and the finitely many ``$\beta$ large'' conditions below.
```
New:
```
$\int_{C_\eta\cap\{V\le1\}}f^2\ge1/2$ (Lemma~\ref{tu:L-M4}); and the finitely many ``$\beta$ large'' conditions below.
With the choices above every one of these thresholds is a function of $\eta$ alone: the constants of
Proposition~\ref{tu:L-E13} and $m(\eta)$ depend on $\eta',r_0,\ell,\theta_0,M,C$ and on $H_\Psi,\Lambda,\tilde\Theta$, which are now
fixed functions of $\eta$; the conditions of Lemma~\ref{tu:L-balls} on $\rho_B,r_0,\ell,\theta_0$; the threshold of
Lemma~\ref{tu:L-L4} on $\eta$; that of Lemma~\ref{tu:U-F} on $\eta/2$; $\beta_1(\eta,\delta,\tau)$ of (B) on $\eta$, $\delta=\tau=\frac12$ and
the explicit choices of Lemma~\ref{tu:U-W13} (through $\beta_0(\eta/4)$ of Lemma~\ref{tu:U-F} and $\omega(\beta)$, which depends on $H$);
and $m_B\ge\frac18$, $\int f^2\ge\frac12$ on $C(\eta)$, $\phi_{\min}(\eta)$ and $\varkappa=1$.
```

## Change 22: tun_lower.tex, original line 960
Referee item: lower notation nit (set S renamed mathcal S in Section 8)

Old:
```
$\int_Sf^2\ge\frac12$ and $m_B\ge\frac18$, where $S:=C_\eta\cap\{V\le1\}$.
\item Corollary~\ref{tu:L-H4cor} gives $g\ge\mu$ on $D_M\cup\sigma_1D_M\supset R_{\rm well}$ and on $S$.
```
New:
```
$\int_{\mathcal S}f^2\ge\frac12$ and $m_B\ge\frac18$, where $\mathcal S:=C_\eta\cap\{V\le1\}$ (a set; not the radius $S$).
\item Corollary~\ref{tu:L-H4cor} gives $g\ge\mu$ on $D_M\cup\sigma_1D_M\supset R_{\rm well}$ and on $\mathcal S$.
```

## Change 23: tun_lower.tex, original line 966
Referee item: lower notation nit (set S renamed, cont.)

Old:
```
$S$ is $\sigma_1$-invariant, since $\varepsilon(a_1)$ and $V$ are. Corollary~\ref{tu:L-B} needs, for each $x\in S$, centres
```
New:
```
$\mathcal S$ is $\sigma_1$-invariant, since $\varepsilon(a_1)$ and $V$ are. Corollary~\ref{tu:L-B} needs, for each $x\in\mathcal S$, centres
```

## Change 24: tun_lower.tex, original line 976
Referee item: lower #26 nit (8.2: chains padded to a common n)

Old:
```
The number of steps is $n\le(\pi+2a_-)\sqrt\beta/d+O(\beta^{1/4})=O(\sqrt\beta)$.
```
New:
```
The number of steps is $n\le(\pi+2a_-)\sqrt\beta/d+O(\beta^{1/4})=O(\sqrt\beta)$. Lemma~\ref{tu:L-Pc} needs one $n$ for all
$x\in\mathcal S$; the chains are padded with zero steps to this common bound, as in Lemma~\ref{tu:L-geom}.
```

## Change 25: tun_lower.tex, original line 986
Referee item: lower #26 nit (mu' defined)

Old:
```
g(z)\ge\min\big(\mu',\ \tfrac\mu4e^{-1.5\rho_B^2}e^{-\sqrt\beta\Psi(\pi/2)}\big),\qquad
-\log\mu'\le35a_-\sqrt\beta+R'_\beta,
```
New:
```
g(z)\ge\min\big(\mu',\ \tfrac\mu4e^{-1.5\rho_B^2}e^{-\sqrt\beta\Psi(\pi/2)}\big),\qquad
\mu':=e^{-35a_-\sqrt\beta-R'_\beta},
```

## Change 26: tun_lower.tex, original line 1032
Referee item: lower notation nit (set S renamed, cont.)

Old:
```
$n=O(\sqrt\beta)$; $|S|\le1$.
```
New:
```
$n=O(\sqrt\beta)$; $|\mathcal S|\le1$.
```

## Change 27: tun_lower.tex, original line 1041
Referee item: lower notation nit (set S renamed, cont.)

Old:
```
Corollary~\ref{tu:L-B} with $\sigma=\sigma_1$, the set $S$,
$r_\beta=\rho_B/\sqrt\beta$, and Lemma~\ref{tu:L-balls} (with $g\ge\mu$ on $S$ for the end points) give
\[
-\log\Delta\le2\sup_{\rm balls\cup S}(-\log g)+O(\log\beta)-\log\Big(2\int_Sf^2\Big)
```
New:
```
Corollary~\ref{tu:L-B} with $\sigma=\sigma_1$, the set $\mathcal S$,
$r_\beta=\rho_B/\sqrt\beta$, and Lemma~\ref{tu:L-balls} (with $g\ge\mu$ on $\mathcal S$ for the end points) give
\[
-\log\Delta\le2\sup_{\rm balls\cup\mathcal S}(-\log g)+O(\log\beta)-\log\Big(2\int_{\mathcal S}f^2\Big)
```

## Change 28: tun_lower.tex, original line 1047
Referee item: lower notation nit (set S renamed, cont.)

Old:
```
using $\int_Sf^2\ge\frac12$ and $-\log\mu\le35(a_-+r_0)\sqrt\beta+R_\beta$.
```
New:
```
using $\int_{\mathcal S}f^2\ge\frac12$ and $-\log\mu\le35(a_-+r_0)\sqrt\beta+R_\beta$.
```

## Change 29: tun_lower.tex, original line 1055
Referee item: brief (i) + upper #4 (status line of tu:L-main reconciled)

Old:
```
\noindent\emph{Status.} Proved in writing, conditional on the results of the first half (Lemmas~\ref{tu:U-kernel},
\ref{tu:U-K}, \ref{tu:U-R}, \ref{tu:U-F}, Proposition~\ref{tu:U-B}), on the gap bounds of Lemma~\ref{tu:L-gauss} and the $\Delta h$
bound of Lemma~\ref{tu:L-taylor} as stated. (The absorption step in Lemma~\ref{tu:L-S4} is now quantified.) Not independently
reviewed: the working files and the assembly were written by sessions of the same model family.
```
New:
```
\noindent\emph{Status.} Proved in writing. It uses the results of the first half (Lemmas~\ref{tu:U-kernel},
\ref{tu:U-K}, \ref{tu:U-R}, \ref{tu:U-F}, Proposition~\ref{tu:U-B}), proved in Sections~\ref{tu:U-sec-kernel}--\ref{tu:U-sec-agmon}, and the gap bounds of
Lemma~\ref{tu:L-gauss} and the $\Delta h$ bound of Lemma~\ref{tu:L-taylor}, which are derived in Section~\ref{tu:L-sec-sub}. (An earlier
version of this line said ``conditional on'' these; they are now on the page. The absorption step in Lemma~\ref{tu:L-S4} is now
quantified.) Not independently reviewed: the working files, the assembly, the patches and the referee reports were written by
sessions of the same model family (Claude, Anthropic).
```

RESULT: ALL MET
