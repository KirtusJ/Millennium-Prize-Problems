"""Size matching of SU(2) lattices from a*sqrt(sigma) (FHK hep-lat/9208012 Table 3).
l*sqrt(sigma) = N * a*sqrt(sigma), N in {6,8,12,16}, beta in {2.3,2.4,2.5} (+2.2,2.6,2.7 tabulated).
Pairs: (beta_c,N_c),(beta_f,N_f), N_f=2*N_c. Mismatch m = (l_f - l_c)/l_c.
Predicates (fixed before first run; tolerance 5% is given by the task):
 P1: pairs with |m|<=0.05 are listed. (Hypothesis 'every N_c=6,8 coarse lattice at 2.3..2.5 has a partner within 5%'
     is tested per case; count reported.)
 P2: expectation (mine): at beta_c=2.3, N=6 -> 2.214; at 2.4 N=12 -> 3.19;  a match needs a ratio ~0.5 in a, e.g. 2.3->2.4 gives
     0.369/0.266=1.387, 2.4->2.5 gives 1.396, so 2*a_f/a_c ~ 1.4 -> expect NO matches within 5% for adjacent betas;
     2.3->2.5 ratio 1.937 ~ 2 -> expect match for 2.3(N)->2.5(2N) (mismatch ~ +3%... l_f/l_c = 2*0.1905/0.369=1.0325).
 Error propagation: relative errors of a*sqrt(sigma) added in quadrature (tabulated errors, no extra).
Output file opened mode 'x'. No randomness (no seeds needed).
"""
import itertools, sys
S = {2.2:(0.4690,0.0100),2.3:(0.3690,0.0030),2.4:(0.2660,0.0020),2.5:(0.1905,0.0008),2.6:(0.1360,0.0040),2.7:(0.1015,0.0010)}
Ns = [6,8,12,16]
rows=[]; cases=0; qual=0
for bc,bf in itertools.product(S,S):
    for Nc in Ns:
        Nf=2*Nc
        if Nf not in Ns: continue
        lc=Nc*S[bc][0]; lf=Nf*S[bf][0]
        m=(lf-lc)/lc
        err=abs(lf/lc)*((S[bc][1]/S[bc][0])**2+(S[bf][1]/S[bf][0])**2)**.5
        cases+=1
        rows.append((bc,Nc,bf,Nf,lc,lf,m,err))
core=[r for r in rows if r[0] in (2.3,2.4,2.5) and r[2] in (2.3,2.4,2.5)]
# P1 hypothesis test per coarse case
for bc in (2.3,2.4,2.5):
    for Nc in (6,8):
        ok=[r for r in core if r[0]==bc and r[1]==Nc and abs(r[6])<=0.05]
        qual+= bool(ok)
with open("match_out.txt","x") as f:
    f.write("bc Nc bf Nf l_c l_f mismatch(l_f/l_c-1) ratio_err\n")
    for r in sorted(rows):
        if abs(r[6])<=0.05:
            f.write("%.1f %d %.1f %d %.4f %.4f %+.4f %.4f\n"%r)
    f.write("coarse cases (bc in 2.3,2.4,2.5; Nc=6,8) with >=1 partner within 5%% among 2.3-2.5: %d of 6\n"%qual)
    f.write("all pairs (any listed beta) within 5%%: %d of %d\n"%(sum(abs(r[6])<=0.05 for r in rows),len(rows)))
print(open("match_out.txt").read())
