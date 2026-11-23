from decimal import Decimal as D, getcontext
getcontext().prec=60
def I(n,x):
    x=D(x); q=(x/2)**2
    t=(x/2)**n
    for k in range(1,n+1): t/=k
    s=t;k=0
    while True:
        t=t*q/((k+1)*(k+1+n)); k+=1; s+=t
        if k>x/2 and t<s*D(10)**-55: break
    return s
def f(v,d=14): return format(v,'.%dg'%d)
out=[]
r=I(1,1)/I(0,1)
with open('control.txt','x') as c: c.write('%.6f\n'%r)
out.append('# T92 results\n\nControl I1(1)/I0(1) = %s (known 0.446390)\n'%f(r,12))
out.append('I0(10)=%s (ref 2815.716628466254)\nI1(10)=%s (ref 2670.988303701255)\n'%(f(I(0,10),16),f(I(1,10),16)))
out.append('\n## Claim (C): -ln kappa_n, kappa_n=I_{n+1}/I_1\n')
for b in (1000,10000):
    for n in (1,2):
        v=-(I(n+1,b)/I(1,b)).ln()
        B=D(b); lo=D(n*(n+2))/(2*(B+n+D('0.5'))); hi=D(n*(n+3))/(2*B)
        out.append('beta=%d n=%d: value=%s lower=%s upper=%s slack_lower(v-lo)=%s slack_upper(hi-v)=%s ok=%s'%(b,n,f(v),f(lo),f(hi),f(v-lo,8),f(hi-v,8),lo<=v<=hi))
out.append('\n## Claim (B): r_nu(x)=I_{nu+1}/I_nu <= x/(nu+1/2+sqrt((nu+1/2)^2+x^2))\n')
for nu,x in [(0,1000),(0,10000),(1,10000),(2,10000),(3,10000)]:
    r=I(nu+1,x)/I(nu,x); a=D(nu)+D('0.5'); X=D(x)
    bd=X/(a+(a*a+X*X).sqrt())
    out.append('nu=%d x=%d: r=%s bound=%s slack_abs=%s slack_rel=%s ok=%s'%(nu,x,f(r,14),f(bd,14),f(bd-r,8),f((bd-r)/r,8),r<=bd))
out.append('\nNot verified: only these finite cases; no proof; Decimal prec 60 power series only (single method, series truncated at rel 1e-55); no independent continued-fraction cross-check; other nu/x untested.\n')
open('result.md','x').write('\n'.join(out))
print('\n'.join(out))
