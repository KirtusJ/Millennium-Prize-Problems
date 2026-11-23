"""T110 recomputation. Predicates fixed BEFORE first run (tolerance = half unit of last claimed digit unless noted):
Q1 |v-4.1167196|<=0.5e-7; Q2 |v-1.89778|<=0.5e-5; Q3 |v-2.26965|<=0.5e-5;
Q4a |v-1.5e-7|<=0.05e-7 (2 sig digits); Q4b v<0.5e-6/4^(1/3)  (strict);
Q5 |v-1.974964|<=0.5e-6; Q6 each |v-claim|<=0.005; Q7 each |v-claim|<=0.05 (percent);
Q8 |v-1.8|<=0.05; Q9 max abs diff <=1e-12 at 1000 pts (double rounding, my choice), count qualifying pts;
Q10 |c-4.6054132|<=0.5e-7; Q11 |d-2.6828|<=0.5e-4; Q12 |v-8.99|<=0.005 (uses 3.3505330*d computed);
Q13 |v-4.7926|<=0.5e-4; Q14 both ratios within 0.5 of 12 (integer 'about 12').
Quadrature: own Gauss-Legendre (numpy nodes), 400 nodes, substitution a=(pi/2)u^2 on [0,pi/2], doubled by symmetry
a->pi-a (removes sqrt endpoint singularity). Convergence check with 200 nodes (|diff|<=1e-10).
Q1-Q4 use decimal with 40 digits."""
import numpy as np, math, json
from decimal import Decimal as D, getcontext
getcontext().prec=40
R={}
def cbrt4():
    return D(4)**(D(1)/D(3))
c4=cbrt4()
def rec(k,val,claim,tol,ok,src): R[k]=dict(value=str(val),claim=claim,tol=tol,ok=bool(ok),src=src)
q1=D('6.534885')/c4; q2=D('3.012539')/c4; q3=D('3.602838')/c4
rec('Q1',q1,'4.1167196',5e-8,abs(q1-D('4.1167196'))<=D('5e-8'),'half unit of 7th decimal')
rec('Q2',q2,'1.89778',5e-6,abs(q2-D('1.89778'))<=D('5e-6'),'half unit of 5th decimal')
rec('Q3',q3,'2.26965',5e-6,abs(q3-D('2.26965'))<=D('5e-6'),'half unit of 5th decimal')
q4=abs(D('4.116719735')-q1)
rec('Q4a',q4,'1.5e-7',5e-9,abs(q4-D('1.5e-7'))<=D('5e-9'),'half unit of 2nd sig digit')
lim=D('0.5e-6')/c4
rec('Q4b',f'{q4} < {lim}','smaller than rounding bound',None,q4<lim,'propagated rounding of 6.534885 = 0.5e-6/4^(1/3)')
q5=D('5.3254970')-D('3.3505330'); rec('Q5',q5,'1.974964',5e-7,abs(q5-D('1.974964'))<=D('5e-7'),'half unit of 6th decimal')
for nm,x,cl in [('Q6a',D('2.876117'),2.88),('Q6b',D('1.621505')*D(2)**(D(1)/3),2.04),('Q6c',D('0.968930')*c4,1.54)]:
    rec(nm,x,cl,0.005,abs(float(x)-cl)<=0.005,'half unit of 2nd decimal')
for nm,a,b,cl in [('Q7a','2.992','3.0125',-0.7),('Q7b','2.989','3.0125',-0.8),('Q7c','3.544','3.6028',-1.6)]:
    v=(D(a)/D(b)-1)*100; rec(nm,v,cl,0.05,abs(float(v)-cl)<=0.05,'half unit of 1st decimal (percent)')
q8=(D('1.9019')-D('1.887'))/D('0.0084'); rec('Q8',q8,1.8,0.05,abs(float(q8)-1.8)<=0.05,'half unit of 1st decimal')
a=np.linspace(0,math.pi,1000); diff=np.abs(np.arccosh(1+2*np.sin(a)**2)-2*np.arcsinh(np.sin(a)))
rec('Q9',f'max diff {diff.max():.3e}; {int((diff<=1e-12).sum())}/1000 points qualify','identity',1e-12,(diff<=1e-12).all(),'double-precision rounding, my choice')
def gl(n): return np.polynomial.legendre.leggauss(n)
def integ(f,n):
    x,w=gl(n); u=(x+1)/2; w=w/2   # u in (0,1)
    a=(math.pi/2)*u**2; da=math.pi*u
    return 2*float(np.sum(w*f(a)*da))
eps=lambda a: 2*np.arcsinh(np.sin(a))
fc=lambda a: np.sqrt(2*eps(a)); fd=lambda a: 1/np.sqrt(2*eps(a)); f13=lambda a: np.sqrt(4*np.sin(a))
vals={}
for nm,f in [('c',fc),('d',fd),('q13',f13)]:
    v4,v2=integ(f,400),integ(f,200); vals[nm]=v4; R['conv_'+nm]=dict(value=f'{v4:.10f} vs200 {v2:.10f} diff {abs(v4-v2):.2e}',ok=abs(v4-v2)<=1e-10)
rec('Q10',f"{vals['c']:.9f}",'4.6054132',5e-8,abs(vals['c']-4.6054132)<=5e-8,'half unit of 7th decimal')
rec('Q11',f"{vals['d']:.9f}",'2.6828',5e-5,abs(vals['d']-2.6828)<=5e-5,'half unit of 4th decimal')
q12=3.3505330*vals['d']; rec('Q12',f'{q12:.6f}','8.99',0.005,abs(q12-8.99)<=0.005,'half unit of 2nd decimal')
rec('Q13',f"{vals['q13']:.9f}",'4.7926',5e-5,abs(vals['q13']-4.7926)<=5e-5,'half unit of 4th decimal')
r1=(8.99-8.1)/8.99*100; r2=(8.99-8.1)/8.1*100
rec('Q14',f'{r1:.3f}% and {r2:.3f}%','about 12%',0.5,abs(r1-12)<=0.5 and abs(r2-12)<=0.5,"'about 12' read as 12 +-0.5 (integer rounding); neither matches")
rec('Q14_either',f'{r1:.3f}% / {r2:.3f}%','about 12%',0.5,abs(r1-12)<=0.5 or abs(r2-12)<=0.5,'same, either ratio')
with open('results.json','x') as fh: json.dump(R,fh,indent=1)
for k,v in R.items(): print(k,v['value'],'| claim',v.get('claim'),'|', 'REPRODUCED' if v['ok'] else 'NOT REPRODUCED')
