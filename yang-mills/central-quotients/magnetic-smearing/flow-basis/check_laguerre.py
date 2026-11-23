"""Check the Laguerre expansion and the finite-degree concentration bound independently."""
from math import exp, factorial, gamma, sqrt
import numpy as np
from scipy.integrate import quad
from scipy.special import eval_genlaguerre, roots_genlaguerre


def run():
    p, center = 2.5, 2.
    nodes, weights = roots_genlaguerre(72,p-1)
    for s in (1.,1.5,3.,4.):
        h = (1+s/center)/2
        r = (s-center)/(s+center)
        errors = []
        for n in range(13):
            norm = sqrt(gamma(n+p)/factorial(n))
            tilt = (s/center)**(p/2)/(sqrt(gamma(p))*norm)
            actual = tilt*np.dot(weights,eval_genlaguerre(n,p-1,nodes/h))/h**p
            predicted = (1-r*r)**(p/2)*sqrt(gamma(n+p)/(factorial(n)*gamma(p)))*r**n
            errors.append(abs(actual-predicted))
        assert max(errors)<1e-12
        print(f"s={s:g}, 13 coefficient absolute errors bounded by {max(errors):.3g}")
    for N in (4,8,16,32):
        u=1/(8*N)
        def term(n):
            return quad(lambda x: x**(p-1)*exp(-x)*eval_genlaguerre(n,p-1,x)**2
                        *factorial(n)/gamma(n+p),0,u,epsabs=1e-15)[0]
        trace=sum(term(n) for n in range(N))
        upper=exp(p-1+2*N*u/p)*(N*u)**p/gamma(p+1)
        assert 0<trace<upper
        print(f"N={N}, x band endpoint={u:g}, trace={trace:.10g}, upper={upper:.10g}")


if __name__=="__main__":
    run()
