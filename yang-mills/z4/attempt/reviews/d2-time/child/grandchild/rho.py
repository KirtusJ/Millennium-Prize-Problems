# Predicate stated before running: |rho| <= 1 (and Var(w.Y) > 0).
import math, sys
D='../data/'; S=32; N1=1152; U=308
w=[float(t) for t in open(D+'w.txt').read().split()]
assert len(w)==U
def ctrl():
    xs=[0,1,2,3]; ys=[0,1,1,3]; n=4
    mx=math.fsum(xs)/n; my=math.fsum(ys)/n
    sxy=math.fsum((x-mx)*(y-my) for x,y in zip(xs,ys))
    sxx=math.fsum((x-mx)**2 for x in xs); syy=math.fsum((y-my)**2 for y in ys)
    return sxy*sxy/(sxx*syy)
c=ctrl()
sm=[];smm=[];swy=[];smwy=[];swyy=[]
for s in range(S):
    sm_=smm_=sy=smy=None; syy_terms=None
    with open(f'{D}s{s}.mom.txt') as f:
        for line in f:
            p=line.split()
            if not p or p[0]=='#': continue
            if p[0]=='sm': sm_=float(p[1])
            elif p[0]=='smm': smm_=float(p[1])
            elif p[0]=='sy' and p[1]=='0':
                v=p[2:]; assert len(v)==U
                sy=math.fsum(w[u]*float(v[u]) for u in range(U))
            elif p[0]=='smy' and p[1]=='0':
                v=p[2:]; assert len(v)==3*U
                smy=math.fsum(w[u]*float(v[u]) for u in range(U))  # j=0
            elif p[0]=='syy' and p[1]=='0':
                v=p[2:]; assert len(v)==U*(U+1)//2
                terms=[]; k=0
                for u in range(U):
                    for vv in range(u,U):
                        f_=1.0 if u==vv else 2.0
                        terms.append(f_*w[u]*w[vv]*float(v[k])); k+=1
                syy_terms=math.fsum(terms)
    sm.append(sm_);smm.append(smm_);swy.append(sy);smwy.append(smy);swyy.append(syy_terms)
N=S*N1
Ex=math.fsum(sm)/N; Exx=math.fsum(smm)/N; Ey=math.fsum(swy)/N
Eyy=math.fsum(swyy)/N; Exy=math.fsum(smwy)/N
cov=Exy-Ex*Ey; vx=Exx-Ex*Ex; vy=Eyy-Ey*Ey
rho=cov/math.sqrt(vx*vy)
out=f'control_R2={c:.6f}\nN={N}\nvarx={vx!r}\nvary={vy!r}\ncov={cov!r}\nrho={rho:.10g}\nrho_repr={rho!r}\n|rho|<=1: {abs(rho)<=1}\n'
with open(sys.argv[1],'x') as f: f.write(out)
print(out)
