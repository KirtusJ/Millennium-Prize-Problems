import sys
from decimal import Decimal as D, getcontext
getcontext().prec=60
def I(n,x):
    x=D(x); h=x/2; t=h**n
    for i in range(1,n+1): t/=i
    s=t; k=0
    while True:
        k+=1; t=t*h*h/(k*(k+n))
        s+=t
        if t<s*D(10)**-45 and k>x: break
    return s
def f(v,d=8): return f"{v:.{d-1}e}"
if sys.argv[1]=='c':
    with open('control.txt','x') as o: o.write(f"{I(3,4)/I(1,4):.6f}\n")
else:
    out=[]
    out.append("a I201(8)/I1(8) = "+f(I(201,8)/I(1,8),15))
    x=512
    l=I(2,x)/I(1,x); r=(-(D(3)/2)/(x+D('1.5'))).exp()
    out+=["b lhs "+f(l,12),"b rhs "+f(r,12),"b log(rhs)-log(lhs) "+f(r.ln()-l.ln())]
    r2=(-(D(3)/2)/(2*x)).exp()
    out.append("c log(rhs)-log(lhs) "+f(r2.ln()-l.ln()))
    rr=I(1,x)/I(0,x); lo=x/(1+(1+D(x)**2).sqrt()); hi=x/(D('0.5')+(D('0.25')+D(x)**2).sqrt())
    out+=["d r "+f(rr,15),"d r-lo "+f(rr-lo),"d hi-r "+f(hi-rr)]
    with open('report.txt','x') as o: o.write("\n".join(out)+"\n")
