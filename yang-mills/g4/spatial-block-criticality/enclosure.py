"""Outward rational bounds for the continuum block at s=1 and lags 0, 1, 2."""
from fractions import Fraction as Q
from math import factorial, isqrt

CELL = 12                   # cells per unit in the positive octant
LIMIT = 16
UNIT = 2**54                # fixed point for positive factors
RAD = 256                   # steps per unit for radii and exponentials


def ceil(v):
    return -(-v.numerator // v.denominator)


def fixed(lo, hi):
    return int(max(0, lo)*UNIT), ceil(hi*UNIT)


def pi_bounds():
    def atan(x):
        s = sum((-1)**j*x**(2*j+1)/(2*j+1) for j in range(10))
        return s, s+x**21/21
    a,b = atan(Q(1,5))
    c,d = atan(Q(1,239))
    # Machin's identity. Interval signs switch for the subtracted term.
    return 16*a-4*d, 16*b-4*c


def filters():
    sides = []
    for i in range(LIMIT*CELL):
        x = Q(2*i+1,4*CELL)  # midpoint of the cell in argument z/2
        s = sum((-1)**j*x**(2*j+1)/factorial(2*j+1) for j in range(40))
        remainder = x**80/factorial(80)
        # |d sinc(z/2)/dz| <= 1/4 from its cosine integral.
        err = remainder/x + Q(1,8*CELL)
        lo,hi = max(0,abs(s/x)-err), min(1,abs(s/x)+err)
        w = fixed(lo**8,hi**8)
        err = 2*remainder + Q(1,2*CELL)
        lo,hi = max(0,2*abs(s)-err), min(2,2*abs(s)+err)
        d = fixed(lo**6,hi**6)
        wd = (w[0]*d[0]//UNIT, (w[1]*d[1]+UNIT-1)//UNIT)
        sides.append((w,wd))
    return sides


def exp_table(n):
    step = Q(1,RAD)
    hi = sum((-step)**k/factorial(k) for k in range(13))
    a,b = fixed(hi-step**13/factorial(13),hi)
    lo,hi = [UNIT],[UNIT]
    for _ in range(n):
        lo.append(lo[-1]*a//UNIT)
        hi.append((hi[-1]*b+UNIT-1)//UNIT)
    return lo,hi


def outward(x, digits, upper=False):
    m = 10**digits
    i = ceil(x*m) if upper else x.numerator*m//x.denominator
    return f"{i//m}.{i%m:0{digits}d}"


def run():
    side = filters()
    pi_lo,pi_hi = pi_bounds()
    n = len(side)
    radius = [isqrt(j*RAD*RAD)//CELL for j in range(3*n*n+1)]
    elo,ehi = exp_table(2*(radius[-1]+1))
    lows, highs = [0]*3,[0]*3
    for i,((xlo,xhi),_) in enumerate(side):
        for j in range(i+1):
            (ylo,yhi),_ = side[j]
            xy0,xy1 = i*i+j*j,(i+1)**2+(j+1)**2
            factor = 1 if i==j else 2
            for k,(_,(zlo,zhi)) in enumerate(side):
                r0,r1 = radius[xy0+k*k],radius[xy1+(k+1)**2]+1
                # Narrow integral bounds for (x*x+y*y)/(2*r).
                alo = xy0*RAD*UNIT//(2*CELL*CELL*r1)
                ahi = (r1*UNIT+2*RAD-1)//(2*RAD)
                if r0:
                    den = 2*CELL*CELL*r0
                    ahi = min(ahi,(xy1*RAD*UNIT+den-1)//den)
                lo,hi = factor*xlo*ylo*zlo*alo,factor*xhi*yhi*zhi*ahi
                for t in (0,1,2):
                    lows[t] += lo*elo[t*r1]
                    highs[t] += hi*ehi[t*r0]
    vol = Q(1,CELL**3*UNIT**5)
    # The exterior is covered by three coordinate tails. In each use the
    # first two moments of u(x)=min(1,(2/x)^8), A <= (x+y+z)/2.
    I0,I1 = Q(16,7),Q(8,3)
    T0,T1 = Q(2**8,7*LIMIT**7),Q(2**8,6*LIMIT**6)
    tail = 96*(T1*I0**2+2*T0*I1*I0)/pi_lo**3
    c = [(lows[t]*vol/pi_hi**3,highs[t]*vol/pi_lo**3+tail/2**(t*LIMIT))
         for t in (0,1,2)]
    dlo,dhi = 1+2*c[0][0],1+2*c[0][1]
    def connected_bounds(pair):
        x,y = pair
        u = (2*y/dlo)**2
        assert u < 1
        # Mean value bounds for (1-u)^(-3/2)-1; round exponent 5/2 up to 3.
        return 6*x*x/dhi**5,6*y*y/(dlo**5*(1-u)**3)
    b1,b2 = connected_bounds(c[1]),connected_bounds(c[2])
    # Both lags share exactly the same marginal D. Bound their difference in
    # one mean-value estimate so its denominator is shared as well.
    lower = 6*(c[1][0]**2-c[2][1]**2)/dhi**5
    gap = max(lower,b1[0]-b2[1]), b1[1]-b2[0]
    def display(p):
        return [outward(p[0],9),outward(p[1],9,True)]
    assert gap[0]>Q(1,1000000)
    return {"s":1,"cube":LIMIT,"cells_per_unit":CELL,
            "one_color_covariances":[display(v) for v in c],
            "connected_at_1":display(b1),"connected_at_2":display(b2),
            "connected_difference":display(gap)}


if __name__=="__main__":
    import json
    print(json.dumps(run(),indent=2))
