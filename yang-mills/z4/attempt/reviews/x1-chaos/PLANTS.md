# PLANTS.md -- x1-chaos (T188). Written before any referee was launched.

Source: note/ (tun_upper.tex = Sections 1-4, tun_lower.tex = Sections 5-8). Each copy planted/k/ differs from
note/ only in the lines below (checked by make_plants.py, predicate P-diff; all copies compile to 32 pages, P-tex).
Controls planted/c1, planted/c2 are byte-identical to note/ (P-ctrl).
Referee half: plants in tun_upper.tex -> "Sections 1-4"; plants in tun_lower.tex -> "Sections 5-8".
c1 -> Sections 1-4, c2 -> Sections 5-8.

## Plant 1 -- kind (a) inequality direction, scalar step
- File/line: planted/1/tun_upper.tex:215 (Lemma K = Lemma tu:U-K, proof, "Denominator").
- Old: `\emph{Denominator.} We have $1-\cos\theta\le\theta^2/2$, ...`
- New: `\emph{Denominator.} We have $1-\cos\theta\ge\theta^2/2$, ...`
- Why an error: 1-cos t <= t^2/2 is the true direction; the new claim is false for every t != 0. The step needs the
  <= direction to get e^{-beta(1-cos)} >= e^{-beta theta^2/2} and hence the lower bound on Z.
- Downstream: the lower bound Z >= e^beta (2pi)^{-2}(2pi/beta)^{3/2}(1-1/beta) (line 223) becomes unproved, hence both
  bounds of Lemma K, Remark tu:U-K-rem (omega, C_L), Lemma tu:U-schur, Prop. B and Theorem tu:U-main.

## Plant 2 -- kind (b) constant changed so the corner absorption fails
- File/line: planted/2/tun_lower.tex:661 (definition of m_0 before Lemma S4-alg).
- Old: `m_0:=\tfrac12\big(1-e^{-3\eta/4}\big),\qquad ...`
- New: `m_0:=\big(1-e^{-3\eta/4}\big),\qquad ...`
- Why an error: Step 3(a) then claims a <= e^{-3eta/4} = 1-2m_0, false (e^{-3eta/4} = 1-m_0). Step 4 needs
  bar a = 1-2m_0 to conclude a(1-x_c)+P x_c^gamma <= 1-m_0; with the new m_0 the honest bound is
  (1-m_0) + m_0 = 1, i.e. no margin, and e^delta F <= 1 (Step 7) fails for delta>0. Also M_A^2 now uses log(1/m_0)
  with the larger m_0, so (M_A) is weaker. Text "m=m_0 ~ 3eta/8" (line 667) left unchanged (now inconsistent).
- Downstream: Lemma tu:L-S4 (S4-alg) unproved, hence Prop. tu:L-sub, Lemma tu:L-balls(II), Theorem tu:L-main.

## Plant 3 -- kind (c) hypothesis dropped from a statement whose proof uses it
- File/line: planted/3/tun_upper.tex:788 (Proposition tu:U-B, Estimate (B)).
- Old: `... every real eigenfunction $u$ of $T$ with eigenvalue $\mu\ge e^{-\eta/4}$:`
- New: `... every real eigenfunction $u$ of $T$ with eigenvalue $\mu>0$:`
- Why an error: the proof (line 807) uses mu - e^q >= e^{-eta/4} - e^{-eta/2} > 0 on I^c, which needs mu >= e^{-eta/4}.
  For eigenfunctions with small eigenvalue the weighted bound is unproved (and false in general: no decay is forced).
  Line 793-794 ("In particular ... once beta is so large that lambda_ee, lambda_eo >= e^{-eta/4}") left unchanged.
- Downstream: Prop. B as stated is unproved/false; Theorem tu:U-main still only uses u = g with lambda >= e^{-eta/4},
  so the main theorem survives -- the defect is in the statement of Prop. B.

## Plant 4 -- kind (d) lemma used outside its hypotheses (domain changed)
- File/lines: planted/4/tun_lower.tex:315-316 (definition of Omega and R_well in Section "The ansatz").
- Old: `$\Omega:=\{\varphi>0\}\cap\{a_1\in[a_-,\pi-a_-]\}$` and `R_well ... a_1<a_- or a_1>\pi-a_-`
- New: `$\Omega:=\{\varphi>0\}\cap\{a_1\in[a_-/2,\pi-a_-/2]\}$` and `R_well ... a_1<a_-/2 or a_1>\pi-a_-/2`
- Why an error: Prop. tu:L-sub (ii) applies Lemma tu:L-S4 at every x in Omega with a_1 <= pi/2, but S4 assumes
  a_1 in [a_-, pi/2] (there chi = 1, Psi'^2/2 = eps+eta, Step 3(a)); points with a_1 in [a_-/2, a_-) are now in Omega
  and outside the lemma. Lemma tu:L-norm uses 1_Omega = 1_Omega P with P = 1{a_1 in [a_-, pi-a_-]} and eps(a_1) >= 2eta on
  Omega: both false. Lemma tu:L-ansatz-props(iv) ("on Omega both a_1 and pi-a_1 lie in [a_-,pi-a_-]") false.
- Downstream: Lemma tu:L-norm, Prop. tu:L-sub (comparison), hence Theorem tu:L-main unproved.

## Plant 5 -- kind (e) exponent bookkeeping: honest conclusion is 2c*, theorem still says c*
- File/lines: planted/5/tun_lower.tex:1039-1040 (Lemma tu:L-balls, proof part (II), valley balls).
- Old 1039: `... is $\sigma_1$-invariant, $\varphi=\max(\varphi_L,\varphi_R)=\mu e^{-\sqrt\beta\min(\Psi(a_1),\Psi(\pi-a_1))}(G-c_1)_+(E-c_2)_+$`
- New 1039: `... is $\sigma_1$-invariant, $\varphi\ge\varphi_L=\mu e^{-\sqrt\beta\Psi(a_1)}(G-c_1)_+(E-c_2)_+$`
- Old 1040: `and $\min(\Psi(a_1),\Psi(\pi-a_1))=\Psi(\min(a_1,\pi-a_1))\le\Psi(\pi/2)$ since $\Psi$ is`
- New 1040: `and $\Psi(a_1)\le\Psi(\pi/2)$ since $\Psi$ is`
- Why an error: valley balls have a_1 anywhere in [0, pi-a]; Psi nondecreasing gives Psi(a_1) >= Psi(pi/2) for
  a_1 > pi/2, not <=. With only phi_L (the "monotone reading" that change C6 removed) the honest bound is
  -log g <= sqrt(beta) Psi(pi-a) ~ sqrt(beta) 2Psi(pi/2) ~ c* sqrt(beta), so -log Delta <= 2 c* sqrt(beta) + o and
  the honest conclusion is limsup <= 2c*. Theorem tu:L-main and Corollary tu:L-limit still say c*.
- Downstream: Lemma tu:L-balls (statement's second term), Theorem tu:L-main, Corollary tu:L-limit.

## Plant 6 -- kind (f) quantifier order: a fixed parameter made to depend on beta
- File/line: planted/6/tun_lower.tex:947 (Section "Parameters and the order of limits").
- Old: `\item $M=M(\eta)$ with $M^2:=M_A^2(\eta)$, so $M^2\ge M_A^2(\eta)$ ...`
- New: `\item $M=M(\eta,\beta)$ with $M^2:=M_A^2(\eta)+\log\beta$, so $M^2\ge M_A^2(\eta)$ ...`
- Why an error: M must be fixed before beta -> infinity: it determines the tube T, c_1 = e^{-M^2}, the constants of
  Prop. tu:L-E13 and hence beta_0(eta) (sup_T Delta_i <= m/2), and R_beta. With M depending on beta the threshold
  beta_0 depends on beta (circular); the text "every one of these thresholds is a function of eta alone" (l.967) and
  "M ... all fixed before beta -> infinity" (l.978-979) become false; sup_T Delta_i -> 0 is no longer justified since
  the tube grows with beta.
- Downstream: choice of beta_0(eta) in the assembly, hence Theorem tu:L-main unproved.

## Plant 7 -- kind (g) flux identity prefactor back to 2
- File/lines: planted/7/tun_upper.tex:829 and 839 (Lemma tu:U-flux statement and proof).
- Old 829: `...g(y)\,dx\,dy=4\,\langle g\mathbf 1_{A_-},...` ; New: `...=2\,\langle ...`
- Old 839: `So the integral is $2\cdot2\langle ...` ; New: `So the integral is $2\langle ...`
- Why an error: (varsigma(x)-varsigma(y))^2/2 = 2 on cross pairs and both orderings contribute: the correct prefactor
  is 4. The new lemma statement is false by a factor 2. Remark after it (l.843, "correct prefactor is 4") and
  Theorem tu:U-main (uses 4) left unchanged, so the note now contradicts itself.
- Downstream: Lemma tu:U-flux false; Theorem tu:U-main unaffected in exponent (it uses 4).

## Plant 8 -- kind (h) fibre lemma (master bound of Lemma F)
- File/lines: planted/8/tun_upper.tex:504 and 506 (Theorem tu:U-F-master, proof, interior region).
- Old 504: `On $\{|W'|^2\le4\tau\}$:` ; New: `On $\{|W'|^2\le2\tau\}$:`
- Old 506: `On $\{|W'|^2>4\tau\}$: since` ; New: `On $\{|W'|^2>2\tau\}$: since`
- Why an error: with |w/A| <= sqrt(tau) and |W'| > sqrt(2 tau) one only gets |W'-w/A| > (sqrt2-1) sqrt(tau), not
  > sqrt(tau); the tail probability is e^{-beta A (sqrt2-1)^2 tau/2} = e^{-0.0858 beta A tau}, not e^{-beta A tau/2}.
  The claimed third term of M_in is too small. (The first-region bound (1-tau)(1-4tau) remains valid.)
- Downstream: Theorem tu:U-F-master as stated unproved (third term of M_in); Remark tu:U-F-num numbers; Lemma F
  itself survives with a corrected constant (the term still vanishes as beta -> infinity).

## Expected severity (my prior, before testing)
Statement-level consequences: plants 2, 4, 5, 6 break Theorem tu:L-main's proof; plant 1 breaks Lemma K (and so
Theorem tu:U-main's proof); plants 3, 7, 8 make a stated lemma/proposition false but the main theorem survives with a
local repair.
