"""Exact histogram regressions and outward-rounded compact-rotor calculation."""
from fractions import Fraction as Q
import json
from histogram import characteristic, count_above, estimate, spectrum_brackets
from rotor import calculate


def controls():
    for size,diag in ((2,3),(3,3),(5,2)):
        top = (diag+size-1)**2
        next_value = (diag-1)**2
        Z = top+(size-1)*next_value
        table = [[Q(diag**2 if i==j else 1,Z) for j in range(size)] for i in range(size)]
        result = estimate({"probabilities":table,"diameters":[0]*size,"beta_t":1,"half_period":1})
        for key,w in [("vacuum",Q(top,Z)),("first_excited",Q(next_value,Z)),
                      ("probability_ratio",Q(next_value,top))]:
            lo,hi = map(Q,result[key])
            assert lo <= w <= hi and hi-lo < Q(1,10**10)
        assert Q(result["tail_after_bins"]) == 0
    # Indefinite root table: the second singular value exceeds the middle eigenvalue.
    raw = [[1,2,0],[2,1,2],[0,2,1]]
    norm = sum(v*v for row in raw for v in row)
    table = [[Q(v*v,norm) for v in row] for row in raw]
    pair = spectrum_brackets(table,40)
    assert pair[1][0]**2 > Q(3,norm) and pair[1][1]**2 < Q(4,norm)
    # Shifted root exactly zero and repeated; strict count must omit equality.
    assert count_above(characteristic([[4,0,0],[0,4,0],[0,0,0]]),4)==0
    assert count_above(characteristic([[4,0,0],[0,4,0],[0,0,0]]),0)==2
    # One unresolved cell always observes [1]. Tensor powers hide vacuum probability.
    hidden_top = Q(121,202)  # positive kernel [[10,1],[1,10]]
    assert hidden_top**10 < Q(1,100)
    return {"exact_positive_tables":3,"indefinite_root_table":True,
            "repeated_thresholds":True,"rotor":calculate()}


if __name__ == "__main__":
    print(json.dumps(controls(),indent=2))
