"""T246. Predicates fixed before first run:
P0 control: I_1(1) rounds to 0.565159104 (series, written to control.txt).
P1 enclosure: 0.036885895 < R'(6) < 0.036885896 with R' = 1-3R/k-R^2, R from CF (depth 200 vs 400 agree to 1e-40).
P2 numerical diff: Richardson of central differences (h=1e-4,1e-5) agrees with P1 value to 1e-10.
Rerun: python3 t246.py  (needs control.txt/result.txt absent; opens with 'x')
"""
from decimal import Decimal as D, getcontext
getcontext().prec=60
def I1_1():
    s=D(0);t=D(1)/2  # (x/2)^1/1!, x=1
    for m in range(40):
        s+=t; t=t/D(4)/((m+1)*(m+2))
    return s
c=I1_1(); cs=f"{c:.9f}"
with open('control.txt','x') as f: f.write(cs+'\n')
print('control',cs)
assert cs=='0.565159104'
def R(k,depth):
    r=D(0)
    for v in range(depth,0,-1):
        r=1/(D(2*(v+1))/k+r)
    return r
k=D(6)
R200,R400=R(k,200),R(k,400)
Rp=lambda d:1-3*R(k,d)/k-R(k,d)**2
p1a,p1b=Rp(200),Rp(400)
def cd(h):
    h=D(h);return (R(k+h,300)-R(k-h,300))/(2*h)
d4,d5=cd('1e-4'),cd('1e-5')
rich=(4*d5-d4)/3
ok1=D('0.036885895')<p1b<D('0.036885896') and abs(p1a-p1b)<D('1e-40')
ok2=abs(rich-p1b)<D('1e-10')
out=f"R(6)={R400:.15f}\nR'(6)={p1b:.15f}\nCD1e-4={d4:.15f}\nCD1e-5={d5:.15f}\nRichardson={rich:.15f}\nP1={'PASS' if ok1 else 'FAIL'}\nP2={'PASS' if ok2 else 'FAIL'}\n"
with open('result.txt','x') as f: f.write(out)
print(out)
