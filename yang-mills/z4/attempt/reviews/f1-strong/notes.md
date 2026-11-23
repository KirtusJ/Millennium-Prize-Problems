# notes f1-strong (T63)
step0: control.txt = 0.272341 (-ln tanh 1)
step1: Hessian derived. Q(s)=e^{sX1}..e^{sX4}Q, X transported. d2/ds2 V_p = -(b/2)ReTr[(Y^2+C)Q], C=sum_{i<j}[Xi,Xj].
 SU(2): = (b/2)[cos(th)|Y|^2 + <C,A>], A=(Q-Q^+)/2, |A|=sqrt2 sin th, ReTrQ=2cos th.
 per-plaquette max of -[..]/sum|X|^2 = h(th)=2s(1+s), s=sin(th/2) (eigenvalues of Toeplitz N_jk=e^{i th sgn(k-j)}: 4cos^2(th/4),4sin^2(th/4),+-2sin(th/2), proved by z^4=e^{-2i th} ansatz). h<=4, =4 only at Q=-1 -> c=12, same as SZZ.
 pi-flux (all Q_p=-1, Z2 links): Ad(Q)=id, Hess=-(b/2)|curl t|^2 -> lambda_min=-8b (|k|^2 max 16 in d=4). Critical point -> gauge dirs in kernel -> horizontal gives nothing. Method ceiling beta<1/8.
step2: child admitted T69, launched child-run1 (item 4 on 2^4)
step3: wrote hess.py (predicates P1-P5, M1 fixed in docstring), timing check only (piflux -8, horiz -8) before registered run
step4: hess-run1 (registered K1, exit 0, 324 s > 5 min budget slightly): P1-P5 met; pi-flux -8 (L=2,4), horizontal -8 (L=2); one-flip 4.676 (L=2), 4.314 (L=3) both full=horizontal; Haar max 4.54; hill-climb from Haar ~5.5-5.9, from pi-flux stays 8.
step5: literature: SZZ 2204.12737 v1 full text pdftotext (outside dir): Ass 1.1 (1.3), Lemma 4.1 (4.2) |Hess S| <= 8(d-1)N|b||v|^2, Cor 1.6 mass gap. CNS 2509.04688 v2: Def 1.4 beta*_SU(N)=1/(8(d-1)), Thm 1.6 area law, Rem 1.5 SZZ threshold = half; method: BE on vertex sigma-model (Prop 3.2), not YM gap. CNS 2505.16585 abstract only (U(N), master loop eq). Nissim 2510.22788 abstract only.
step6: child control graded PASS (1-2b x3, 1 x9).
step7: STRONG_COUPLING.md written
step8: child returned (K2 exit 0, 664 s): control PASS, c_max found 8 at pi-flux, random starts <=7.29 (unconverged), grandchild T70 FD 7.99999866. Reran pi-flux spectrum with my code (rerun-child). Released T69.
step9: report.md written; verify PASS (both).
