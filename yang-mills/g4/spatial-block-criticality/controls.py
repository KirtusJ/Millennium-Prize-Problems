"""Independent, reproducible arithmetic, finite-cochain and free-profile checks."""
from fractions import Fraction as Q
from math import factorial
from itertools import product
import json

import enclosure
import heat_checks
import path_checks
import profile_checks


def correlation_clock():
    """Bound two positive transfer laws at exactly one inverse gap."""
    hi=sum(Q(-1,2)**j/factorial(j) for j in range(13))
    lo=hi-Q(1,2)**13/factorial(13)
    rows=[]
    for D in (12,24,48):
        q=Q(1,D**2)
        # At the half-clock the three transfer eigenvalues are h,h^D,h^(2D)
        # where lo < h=exp(-1/2) < hi. At the full clock they are squared.
        good_upper=(q*hi+(1-q)*hi**(2*D))/(q*lo**2)
        bad_num=q*(1-hi**(4*D))*lo**D
        bad_den=q*hi**(4*D+2)+q*hi**(2*D)+(1-q)*hi**(4*D)
        assert good_upper<2 and bad_num>2**(D//3)*bad_den
        rows.append({"D":D,"good_ratio_below":2,"bad_ratio_above":2**(D//3)})
    return rows


def harmonic_energy():
    # A uniform random shift makes the field stationary, including its second
    # moment. Expand both sides even when the field has a nonzero residual.
    sites=list(product(range(3),repeat=4))
    def check(f):
        energy,drift=0,0
        for x in sites:
            u=f(x)
            adjacent=[]
            for j in range(4):
                for sign in (-1,1):
                    y=list(x)
                    y[j]=(y[j]+sign)%3
                    adjacent.append(f(y))
            energy+=sum((v-u)**2 for v in adjacent)
            drift+=2*u*(8*u-sum(adjacent))
        assert energy==drift
        return energy
    constant=check(lambda x: 5)
    varying=check(lambda x: x[0]**2-2*x[2]+x[1]*x[3])
    assert constant==0 and varying>0
    return {"translated_sites":len(sites),"constant_energy":constant,"nonharmonic_energy":varying}


def main():
    return {"paths":path_checks.run(),"heat":heat_checks.run(),
            "illustrative_gaussian":profile_checks.table(),
            "enclosed_gaussian":enclosure.run(),
            "one_inverse_gap":correlation_clock(),
            "log_four_inverse_gap":profile_checks.information_control(),
            "stationary_field":harmonic_energy(),
            "unfiltered_plaquette":profile_checks.free_plaquette()}


if __name__=="__main__":
    print(json.dumps(main(),indent=2))
