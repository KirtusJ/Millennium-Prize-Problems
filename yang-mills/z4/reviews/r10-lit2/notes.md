# notes.md (r10-lit2 literature reader)
Step 0: control.txt = 0.272341 (-ln tanh 1). ref/ fetched.
Step 1 (hypothesis first: fetched files). All five fetches exit 0. pypdf text extraction worked for all (fontTools warnings only):
| file | bytes | pages | chars extracted |
| 0810.2183 Makeenko | 279724 | 32 | 55942 |
| 1006.4518 Luscher | 195981 | 21 | 36805 |
| 1101.0963 Luscher-Weisz | 265323 | 28 | 47063 |
| 2205.07376 FdV-O'C | 744630 | 54 | 180258 |
| 2611.11534 Mihajlovic | 2819183 | 414 | 1056294 |
Text in txt/<id>.txt with === PAGE n === markers.

Step 2 (Q1, FdV-O'C 2205.07376v2, 26 Aug 2024; read pp.1-3,7,11-13,23-24,27-32,38).
- Setting (abstract p.1; p.2): Wilson lattice Λ ⊂ aZ^d, d=2,3,4, a∈(0,1], L even sites per side, G=U(N),SU(N); action Σ_p A_p(U_p)·a^{d-4}/g², A_p=2ReTr(1-U_p) (eq.7), g²∈(0,g0²]; free and periodic b.c.
- Scaling (p.7 eq.17): A^c = a^{(d-2)/2} A^{u,c}; U_b = exp[i g a^{-(d-4)/2} A_b]. Scaled plaquette field (p.11 eq.30,32): TrF^u_p = ImTr(U_p-1)/(a²g); TrF^s_p = a^{d/2} TrF^u_p = a^{(d-4)/2} ImTr(U_p-1)/g (pypdf renders fractions as "num den"; eq.84 confirms the 1/g).
- Thm1 (p.28): factorized stability z_l^{Λr(+Λe)} ≤ Z^u ≤ z_u^{Λr}. Thm2 (p.29): z_u ≤ (a^{d-4}/g²)^{-N²/2} e^{c_u}, z_l ≥ (a^{d-4}/g²)^{-N²/2} e^{c_l}; constants independent of a, g≤g0 (z_l via U(N) Weyl formula eq.75).
- Thm3 (p.29): "TUV" = scaled free energy f^s=(1/Λr)ln[(a^{d-4}/g²)^{N²Λr/2} Z^u] obeys c_l ≤ f^s ≤ c_u uniformly in L, a, g; subsequential thermodynamic and a→0 limits (Bolzano-Weierstrass). Bound per lattice site, not per physical volume (p.11).
- Thm4 (p.31, periodic b.c., multireflection): |G_r(J)| ≤ Π_j |z_u(rJ_j)|^{...}/z_l^{...}, with |z_u(J)| ≤ (a^{d-4}/g²)^{-N²/2} exp(c'_u + π²N|J|²/8): Gaussian in J, uniform in L,a,g, positions. Cauchy bounds -> r-point scaled correlations bounded; unscaled coincident two-plaquette correlation ≤ const·a^{-d} (Remark 19 p.32); "exactly a^{-d}h(g)" for d=4 (p.12, p.38: a^{-d}M(g), M bounded).
- Remark 20 p.32: in d=4 the scaled correlations are independent of a. REASON (my reading, by inspection of eq.6): a^{d-4}/g² = 1/g² in d=4, so the lattice measure does not depend on a at all; a is a label, and the a^{-4} is the conversion factor in eq.30. The uniformity in a in d=4 is therefore definitional; the content is uniformity in L and in g∈(0,g0].
- KEY: the plaquette field is the IMAGINARY part of the trace. For SU(2) TrU is real, so TrF_p ≡ 0 identically; for SU(N≥3) ImTr e^{iX}=Tr sin X has no linear term (TrX=0), it starts at TrX³. For U(N) it is the abelian U(1) part. So the generating-function theorem does not concern the action density ReTr(1-U_p) at all.
- No running coupling: g is fixed in (0,g0] as a→0 (asymptotic freedom is "characterized" by free-field comparison, p.12, not imposed).
- Scope (p.2): "this ﬁniteness properties do not lead directly to the construction of the UV limit". Gap: p.2 they are "not able to give a complete answer"; no gap claim.

Step 3 (rule 7, delegated Q4). Question given to sub-agent: Makeenko 0810.2183 statements on perimeter divergence, cusp anomalous dimension, multiplicative renormalization, attributions, and meaning for a square loop normalized by its mean; control question: number of components of F for SU(2) in 4D (18). It answered 18; its register replays PASS (its claim); it could not write report_child.md (harness), I saved its text as child/report_child.md.
Checked two of its statements against txt/0810.2183.txt pages 2-3 myself: (a) §1.2 eq.1.3 and attribution Gervais-Neveu, Polyakov, Vergeles-Dotsenko (1980): FOUND p.2. (b) §1.3 eq.1.4 BNS 1981 multiplicative renormalization, valid only without light-cone segments: FOUND p.3. Also confirmed 0 hits for "ntersect" (self-intersecting loops not treated here; input/LITERATURE.md's "self-intersecting loops mix" is NOT supported by this source). My addition: Makeenko's θ is the Minkowskian cusp angle (cosh θ); a Euclidean square corner corresponds to θ → iπ/2 continuation, i.e. Euclidean angle π/2; the source does not evaluate it.

Step 4 (Q2, Mihajlovic 2611.11534v1, arXiv 8 Nov 2026, manuscript "5 November 2026 Version 5", 414 pp, unrefereed preprint). Read pp.1-10, 234-239.
- Abstract p.1 ends: a nontrivial 4D spatial-cutoff construction and positive spectral bound along it "are not established; no exact continuum mass is asserted".
- Formal verification: none claimed for its own results; "certified" = exact-rational / interval checker programs (p.10 §1.4, p.234, p.240). Lean appears only in ref [5] (Bhattacharjee-Bhattacharya Zenodo archive, p.408), to which the β_W<1/3 forest framework and sharp single-link transport estimate are attributed (p.8).
- Thm 40.1 (p.235): Hamiltonian H = (s/2a)ΣC_e + (4/(sa))Σ(1-F_p), s=g²≤1, spatial periodic L³: D_KL(ν‖Haar) ≥ n[b(s)]_+, b(s) = (3/2)log(1/s) + log(2√π) - 3/2, n ≥ L³/9 edge-disjoint plaquettes. So entropy per plaquette ≥ (3/2) log(1/g²) - const = 3 log(1/g) - const.
- Thm 41.1 + §41.4 (pp.237-239): hard Peter-Weyl cutoff j≤J on one link, d_J=Σ_{r≤2J+1} r²; B = C d_J s^{3/2}; F_max ≤ min{1, 4B^{2/5}}; g→0, gJ→0 ⇒ F_max→0. Necessary growth: d_J ≳ s^{-3/2} = g^{-3}, i.e. J ≳ 1/g.
- §1.2 eq.(1.2) p.9, Thm 24.1: finite-box gap ≥ (3s/8a)(π/16)^{3L³} exp(-48πL³/s), explicitly NOT volume-uniform; Thm 28.1 local floor for q deleted links independent of volume; §35-38 collective criteria "isolate the additional input needed for a volume-uniform gap" (abstract).
- Strong coupling: Thm 10.10 (p.~97, line 4358): forest-gauge comparison, SU(2), 4D, 0≤β_W<1/3, lattice mass gap bound (attributed to [5]).

Step 5 (Q3 reading). Luscher 1006.4518v3: flow eq.(1.1)-(1.2) p.1 dB/dt = D_ν G_νμ, B|_{t=0}=A; Wilson flow eq.(1.4) p.2 (existence/uniqueness/smoothness on finite lattice, ref [2]); E = ¼ G^a G^a eq.(2.1) p.3; leading order heat kernel smoothing, mean-square radius sqrt(8t) in 4D, p.4 after eq.(2.12); <E> to O(g0^4) eq.(2.28) p.7, LO: <E> = ½ g0² (N²−1)(D−1)/(8πt)^{D/2}; after MSbar renormalization eq.(2.32) p.8: <E> = 3(N²−1)g²/(128π²t²){1+c̄1 g²+...}; "does not need to be renormalized" to this order (one loop), p.8; (2.34): 3(N²−1)α/(32π t²). SU(2): t²<E> = 9g²/(128π²) = 0.0071244 g² = (9/(32π))α = 0.089525 α. SU(3): 3α/(4π) (2.36). Conclusions p.17: all-order analysis "will probably be required"; one-loop "suggests" renormalized fields.
Luscher-Weisz 1101.0963v2 abstract p.1: to all loop orders, for any matter multiplet, correlation functions of the flowed gauge field are finite once the 4D theory is renormalized as usual (dimensional regularization; proof by power counting + BRS symmetry of the D+1 theory, §§6-7, conclusions p.26). §8.2 p.24: gauge-invariant local fields (and Wilson loops) at positive flow time need no renormalization; E(t,x) = <E> + c_E(t){¼F²}_R(x) + O(t) as t→0 (eq.8.6). §8.4 p.25: lattice regularization only "expected" (not proved). Nonperturbative finiteness: not claimed anywhere in either paper.

Step 6 (Q3 program, scripts/flow_bench.py). Trial run (scratch, result file deleted, recorded here): P1,P2,P3,P4 met; P5 FAILED (position-space 2∫D² = 1.2701e-4 vs closed form 2.8060e-4) and P6 failed. Cause: MY defect: D = -[(G''-G'/r) sin²θ + 2G'/r]; the code squared (A sin²θ + C) instead of (A sin²θ + 2C). Fixed (ang = 16A²/15 + 16AC/3 + 8C²); predicates unchanged. Rerun through PCP as flow_bench run1.

Step 7. flow_bench run1 (PCP K1): 6 met, 0 failed, 3 measured. <B3²> 3D flow = 1/(48π²t²); 4D flow <F12²> = 1/(128π²t²) = Luscher LO; Var finite at every t>0, t·Var = 2.2347e-5, 6.1107e-4, 8.9142e-3, 9.0206e-2, 0.77809, 6.3547 for σ/√t = 0.5,1,2,4,8,16; Var → c_flow ∫f² t^{-5/2}, c_flow = √π/(640π²) = 2.806e-4, deviation ≈ 1.8 t/σ². P4 is close to tautological (grids scale with √t and σ), say so.
Step 8. extract replayed via PCP (K2), five text files byte-identical. imtr_check (K3): Im Tr U ≡ 0 on SU(2) (10^4 Haar samples, max 0); SU(3) Im Tr e^{iεX} ∝ ε³, action ∝ ε². PCP verify: PASS.
