"""Free spatial-block checks. Midpoint integrals are numerical illustrations."""
from fractions import Fraction as Q
from math import asinh, exp, expm1, log1p, pi, sin, sqrt


def covariance(R,N=72,edge=18):
    """Integrate scaled lags 0,1,2 in the positive octant; R=None denotes the limit."""
    bound = min(edge,pi*R) if R is not None else edge
    step = bound/N
    grid = [(i+0.5)*step for i in range(N)]
    sides = []
    for z in grid:
        h = z if R is None else 2*R*sin(z/(2*R))
        spline = (2*sin(z/2)/h)**8
        sides.append((h*h,spline,(2*sin(z/2))**6))
    values=[0.,0.,0.]
    for i,(x,sx,_) in enumerate(sides):
        for j in range(i+1):
            y,sy,_ = sides[j]
            xy = x+y
            planar = sx*sy*xy*(1 if i==j else 2)/2
            for z,sz,diff in sides:
                sq = xy+z
                rad = sqrt(sq)
                if R is None:
                    den,energy=rad,rad
                else:
                    den=rad*sqrt(1+sq/(4*R**2))
                    energy=2*R*asinh(rad/(2*R))
                term = planar*sz*diff/den
                one=exp(-energy)
                values[0]+=term
                values[1]+=term*one
                values[2]+=term*one*one
    return [v*step**3/pi**3 for v in values]


def connected(values,s=1):
    D=1+2*s*values[0]
    # expm1 preserves a small connected reading in the presence of D^-3.
    return [expm1(-1.5*log1p(-(2*s*x/D)**2))/D**3 for x in values]


def table():
    hs=[]
    for R in (4,8,16,32,None):
        c=covariance(R)
        b=connected(c)
        assert 0<b[2]<b[1]<b[0]<=1
        hs.append({"R":R if R is not None else "continuum",
                   "gaussian_variance":round(c[0],8),
                   "centered_lag_R":float(f"{b[1]:.7g}"),
                   "centered_lag_2R":float(f"{b[2]:.7g}")})
    # Square-mesh convergence check for an illustration. The proof gives the
    # analytic lower and tail bounds independently of these approximate values.
    fine=connected(covariance(None,96,22))
    coarse=connected(covariance(None,72,18))
    assert all(abs(x/y-1)<0.005 for x,y in zip(fine,coarse))
    return hs


def information_control():
    # Finite discrete Laplace values at an energetic cutoff epsilon. Use the
    # transfer variable λ=e^(-E/e0) at one inverse-gap interval, so there
    # are no floating point exponentials in these good/bad ratio checks.
    rows=[]
    for D in (12,24,48):
        q = Q(1,D**2)
        # The gap atom has λ=1/4 (a fixed log-gap clock of log 4). Middle and
        # high levels have λ=4^-D and λ=4^(-2D); their half-lags are rational.
        gap = Q(1,2)
        mid = Q(1,2**D)
        high = mid**2
        def ratio(weights):
            vals=(gap,mid,high)
            return sum(w*r for w,r in zip(weights,vals))/sum(w*r*r for w,r in zip(weights,vals))
        good = ratio((q,0,1-q))
        bad = ratio((q*mid**4,q*(1-mid**4),1-q))
        assert good<3 and bad>2**(D-1)
        rows.append({"clock_in_gap_units":"log(4)","D":D,"tail_mass":str(q),
                     "good_ratio_below_3":True,"bad_ratio_above":str(2**(D-1))})
    return rows


def free_plaquette():
    """Check the leading one-color coefficient for Z4's undifferenced plaquette."""
    results = []
    for lag in (8,16,32):
        N,edge = 72,22
        step = edge/N
        squares = [(2*lag*sin((i+0.5)*step/(2*lag)))**2 for i in range(N)]
        total = 0.
        for i,x in enumerate(squares):
            for j in range(i+1):
                xy = x+squares[j]
                for z in squares:
                    r = sqrt(xy+z)
                    energy = 2*lag*asinh(r/(2*lag))
                    total += (1 if i==j else 2)*xy*exp(-energy)/(2*r*sqrt(1+(r/(2*lag))**2))
        results.append(total*step**3/pi**3)
    target = 1/pi**2
    deviations = [abs(x-target) for x in results]
    assert deviations[2] < deviations[1] < deviations[0] and deviations[2]<0.001
    return {"lags":[8,16,32],"lag_fourth_times_covariance":[round(x,7) for x in results],
            "asymptotic":round(target,7)}
