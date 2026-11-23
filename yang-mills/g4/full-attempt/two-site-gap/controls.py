"""Independent integer shift and SU(2) action controls on finite periodic boxes."""
from itertools import product
from math import cos, exp, expm1, factorial, log, log1p, pi, sin, sqrt
from random import Random


def torus(x,i,n,L):
    y=list(x)
    y[i]=(y[i]+n)%L
    return tuple(y)


def sign(x,i,seam,L):
    return (-1)**(sum(x[:i])+int(x[i]==L-1 and bool(seam & (1<<i))))


def shifts(L):
    points=list(product(range(L),repeat=3))
    f={x:11*x[0]**2-5*x[1]*x[2]+x[2]**3-2 for x in points}
    for seam in range(8):
        def shift(v,i):
            return {x:sign(x,i,seam,L)*v[torus(x,i,1,L)]
                    +sign(torus(x,i,-1,L),i,seam,L)*v[torus(x,i,-1,L)] for x in points}
        for i in range(3):
            for j in range(i):
                a,b=shift(shift(f,i),j),shift(shift(f,j),i)
                assert all(a[x]+b[x]==0 for x in points)
    odd=[1,2,4,7]
    spins={}
    for x in points:
        index=sum((n%2)<<i for i,n in enumerate(x))
        if index in odd:
            spins[x]=[int(j==index) for j in odd]
        else:
            spins[x]=[sum(sign(x,i,0,L) for i in range(3) if index^(1<<i)==j) for j in odd]
    for x in points:
        for i in range(3):
            y=torus(x,i,1,L)
            numerator=sum(a*b for a,b in zip(spins[x],spins[y]))
            assert numerator==sign(x,i,0,L)
            assert sum(a*a for a in spins[x])*sum(a*a for a in spins[y])==3


def mul(x,y):
    a,b,c,d=x
    e,f,g,h=y
    return a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e


def adj(q):
    return q[0],-q[1],-q[2],-q[3]


def trace_loss(a,b):
    return 1-sum(x*y for x,y in zip(a,b))


def slab(L,n,theta):
    points=list(product(range(L),repeat=3))
    rng=Random(571+L+n)
    def haar():
        v=[rng.gauss(0,1) for _ in range(4)]
        return tuple(a/sqrt(sum(b*b for b in v)) for a in v)
    # Independently gauge rotate all spacetime sites. Temporal plaquettes must retain their value.
    gauge={(t,x):haar() for x in points for t in range(n+1)}
    links={}
    one=(1.,0.,0.,0.)
    for t in range(n+1):
        for x in points:
            for i in range(4):
                if i==3 and t==n:
                    continue
                other=(t+1,x) if i==3 else (t,torus(x,i,1,L))
                angle=t*theta/(n*L) if i==0 else 0.
                u=(cos(angle),sin(angle),0.,0.) if i==0 else one
                links[t,x,i]=mul(mul(gauge[t,x],u),adj(gauge[other]))
    def action():
        total=0.
        for (t,x,i),u in links.items():
            for j in range(i):
                a=links[t+1,x,j] if i==3 else links[t,torus(x,i,1,L),j]
                b=links[t,torus(x,j,1,L),i]
                weight=.5 if i!=3 and t in (0,n) else 1.
                total+=weight*trace_loss(mul(u,a),mul(links[t,x,j],b))
        return total
    exact=n*L**3*2*sin(theta/(2*n*L))**2
    assert abs(action()-exact)<3e-10
    if n>1:
        links[1,points[0],1]=haar()
        assert action()>exact+1e-4
    return exact


def gap_bracket(L,b):
    def bess(n,x):
        return sum((x/2)**(2*k+n)/(factorial(k)*factorial(k+n)) for k in range(45))
    p=3*L**3
    k=(bess(2,b)/bess(1,b))**4
    z=(2*bess(1,4*b)/(4*b))**(p/4)
    electric=-log(k)
    lower=max(electric+log(1+p*b*b/8)-b*p,log((exp(b*p)+1)/(exp(b*p)-1)))
    upper=electric+log(min(exp(b*p),z+k*exp(b*p)))
    return lower,upper


def one_site_log_ratio(beta,theta):
    def logcosh(x):
        return x+log1p(exp(-2*x))-log(2)
    s=beta*sin(theta)**2
    logsinhc=s+log(-expm1(-2*s))-log(2*s) if s else 0.
    return (logcosh(beta)+logcosh(beta*cos(theta)**2)+logsinhc)/2-logcosh(beta*cos(theta))


if __name__=="__main__":
    for L in (2,4,6):
        shifts(L)
    for L in (2,4):
        for n in (1,2,4):
            for theta in (0.,.31,pi/2):
                slab(L,n,theta)
    for beta in (.125,.25,.5):
        print(f"L=2 beta={beta} gap bounds",*(f"{v:.8f}" for v in gap_bracket(2,beta)))
    for beta in (1e3,1e6,1e9):
        print("one-site exact Haar control",beta,one_site_log_ratio(beta,beta**(-1/3))/beta**(1/3))
