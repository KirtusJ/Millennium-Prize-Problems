"""check1.py  (predicates fixed before first run; results written with mode "x" to check1_result.txt)
P1  D* := 48+3 log((pi/2)^{5/2} 2^{3/2}) - 3 log c_H, c_H=2 sin^2(1)/(3 pi): |D*-60.1922|<5e-5 and D*<60.2.   (60.1922 = value printed in sec_proof.tex Lemma free; 60.19 in PROOF_B_v2)
P2  c_H = 0.150258 to 6 digits (sec_proof.tex) : |c_H-0.150258|<1e-6.
P3  Cube word identity eq-cube: the six words, built from the plaquette definition U_ab(y)=U_{y,a}U_{y+e_a,b}U_{y+e_b,a}^-1 U_{y,b}^-1 with
    conjugations u_a, reduce in the free group on edges to the empty word; AND the six words equal the strings printed in sec_proof.tex.
P4  G(n)=int_{[-pi,pi]^3} (k1hat^2+k2hat^2)/(2 sinh m) e^{-m n} dk/(2pi)^3, cosh m=1+a/2, a=sum khat_i^2.
    Midpoint rule, M=64 vs M=128 per axis (tolerance source: grid refinement; accept if |G128-G64|<=2e-3*G128 for the case).
    Then: G(0)=0.5 within 5e-3 (integrand ~|k| near 0 so midpoint error ~1/M^2; tolerance 5e-3 chosen by me, not by source);
          G(1)=0.0688747 within 1e-3 relative-to-grid tolerance 2e-3*G;  pi^2 n^4 G(n)=1.092 at n=8 within 5e-3 absolute (tex prints 3 decimals);
          G(n)>G(n+1)>0 for n=0..9 (Lemma G(2));
          G(n) >= lower bound of Lemma G(3) for n=1..8.
P5  14400/pi^2 equals (1/(2 pi^2))[3*5!*2^6 + (1/16)*6!*2^7] (constant in Lemma G(4)).
"""
import math, numpy as np, sys
out=open("check1_result.txt","x")
def log(*a):
    s=" ".join(str(x) for x in a); print(s); out.write(s+"\n")
fails=0
def pred(name,ok,detail):
    global fails
    log(("MET   " if ok else "FAILED"),name,detail)
    if not ok: fails+=1
cH=2*math.sin(1)**2/(3*math.pi)
D=48+3*math.log((math.pi/2)**2.5*2**1.5)-3*math.log(cH)
pred("P1",abs(D-60.1922)<5e-5 and D<60.2,f"D*={D:.6f}")
pred("P2",abs(cH-0.150258)<1e-6,f"c_H={cH:.8f}")
# P3
def inv(w): return [(e,-s) for (e,s) in reversed(w)]
def red(w):
    st=[]
    for l in w:
        if st and st[-1][0]==l[0] and st[-1][1]==-l[1]: st.pop()
        else: st.append(l)
    return st
def E(a,eps): return ((a,eps),1)
def e(a,eps): return (a,tuple(eps))
def U(a,b,y):   # plaquette word at corner y in directions a<b
    ya=list(y); ya[a-1]+=1; yb=list(y); yb[b-1]+=1
    return [((a,tuple(y)),1),((b,tuple(ya)),1),((a,tuple(yb)),-1),((b,tuple(y)),-1)]
x=[0,0,0]
def sh(y,d): z=list(y); z[d-1]+=1; return z
u=lambda a:[((a,(0,0,0)),1)]
w=[]
parts=[inv(U(2,3,x)), u(2)+inv(U(1,3,sh(x,2)))+inv(u(2)), inv(U(1,2,x)), u(1)+U(2,3,sh(x,1))+inv(u(1)), U(1,3,x), u(3)+U(1,2,sh(x,3))+inv(u(3))]
full=[l for p in parts for l in p]
pred("P3a",red(full)==[],f"reduced length {len(red(full))} from {len(full)}")
def fmt(w): return " ".join(f"{e[0]}_{''.join(map(str,e[1]))}"+("^{-1}" if s<0 else "") for e,s in w)
printed=["3_000 2_001 3_010^{-1} 2_000^{-1}","2_000 3_010 1_011 3_110^{-1} 1_010^{-1} 2_000^{-1}","2_000 1_010 2_100^{-1} 1_000^{-1}",
 "1_000 2_100 3_110 2_101^{-1} 3_100^{-1} 1_000^{-1}","1_000 3_100 1_001^{-1} 3_000^{-1}","3_000 1_001 2_101 1_011^{-1} 2_001^{-1} 3_000^{-1}"]
for i,(p,pr) in enumerate(zip(parts,printed)):
    pred(f"P3b.{i+1}",fmt(p)==pr,f"computed '{fmt(p)}' printed '{pr}'")
# P4
def G(n,M):
    k=(np.arange(M)+0.5)/M*2*np.pi-np.pi
    kh2=4*np.sin(k/2)**2
    tot=0.0
    for i in range(M):
        a=kh2[i]+kh2[:,None]+kh2[None,:]
        m=np.arccosh(1+a/2)
        num=kh2[i]+kh2[:,None]+0*kh2[None,:]      # k1hat^2 + k2hat^2 with k1 = axis i, k2 = axis j
        tot+=np.sum(num/(2*np.sinh(m))*np.exp(-m*n))
    return tot*(2*np.pi/M)**3/(2*np.pi)**3
res={}
for n in range(0,10):
    g64=G(n,64); g128=G(n,128); res[n]=g128
    pred(f"P4.grid.n={n}",abs(g128-g64)<=2e-3*g128,f"G64={g64:.7f} G128={g128:.7f}")
pred("P4.G0",abs(res[0]-0.5)<5e-3,f"G(0)={res[0]:.5f}")
pred("P4.G1",abs(res[1]-0.0688747)<=2e-3*res[1],f"G(1)={res[1]:.7f}")
pred("P4.n8",abs(math.pi**2*8**4*res[8]-1.092)<5e-3,f"pi^2 n^4 G(8)={math.pi**2*8**4*res[8]:.4f}")
pred("P4.mono",all(res[n]>res[n+1]>0 for n in range(9)),str([round(res[n],6) for n in range(10)]))
okb=True
for n in range(1,9):
    r=1/(math.sqrt(3)*n); lb=4/math.pi**2*16*r**5/3*math.exp(-1)/(2*math.sinh(1))/(2*math.pi)**3
    okb&=res[n]>=lb
pred("P4.lowerbound",okb,"n=1..8")
c=(3*120*64+720*128/16)/(2*math.pi**2)
pred("P5",abs(c-14400/math.pi**2)<1e-9,f"{c:.6f}")
log("FAILED_COUNT",fails)
out.close()
sys.exit(0 if fails==0 else 1)
