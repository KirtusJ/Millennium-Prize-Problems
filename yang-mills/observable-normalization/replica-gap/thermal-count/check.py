"""Certify the observable multiplicity windows including all spins of the spatial cube."""
from fractions import Fraction as F
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0,str(Path(__file__).resolve().parents[3]/"transfer-operator/girth-shell"))
from cube_bounds import certified_intervals


def count(n):
    lo = (F("0.8836")/F("0.9040"))**n
    hi = (F("0.8883")/F("0.8993"))**n
    tail = 10**6*(F(11,10)/F(9,10)**3)**12*(729/(400**2*F("0.8993")))**n
    # Conservative rational caps keep exact powers small during later divisions.
    assert tail < F(1,10**10)
    tail = F(1,10**10)
    s = (F("0.9040")/400**4)**n*(6+tail)
    assert s < F(1,10**80)
    s = F(1,10**80)
    loss = (5*(1-lo)**2+10*(hi-lo)**2)/(1+5*lo**2)
    rank_lo = max(F(1),(6-loss)/(1+tail**2))
    rank_hi = min(6*(1+tail)**2,(1+5*hi+tail)**2)
    return rank_lo/(1+s)**4, rank_hi*(1+s**2)**2


if __name__ == "__main__":
    certified_intervals()
    for n,bottom,top in [(8,F("5.95"),F("6.000001")), (600,F("1.000007"),F("1.0063"))]:
        lower, upper = count(n)
        assert bottom < lower <= upper < top
        print(n,float(lower),float(upper))
