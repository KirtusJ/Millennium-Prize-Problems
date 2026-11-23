"""Reproduce the ratio enclosures, electric-loop packing constants, and hidden-sector tests."""
from fractions import Fraction as Q
import json
from math import atan, exp, pi, sinh

from cylinder import cylinder
from relative import estimate


def paired_control():
    # Half-transfer K has positive eigenvalues 9,5,1,1. The diagonal
    # two-state blocks have entries 4 and 3. The off-diagonal blocks are ones.
    k = [[4,3,1,1],[3,4,1,1],[1,1,4,3],[1,1,3,4]]
    norm2 = sum(v*v for row in k for v in row)
    cells = [[0,1],[2],[3]]
    table = [[sum(Q(k[i][j]**2,norm2) for i in block for j in other)
              for other in cells] for block in cells]
    data = {"probabilities":table,"log_oscillations":["1/3",0,0],"physical_period":1}
    exact = Q(25,81)
    exact_cell = estimate(data)
    assert exact_cell["geometry_used"] == "uniform and cellwise"
    # Positive, symmetric, normalized perturbation. Each probability is at
    # least 1/108; |sqrt(x+v)-sqrt(x)| <= |v|/sqrt(x) <= 11|v|.
    change = Q(1,100000)
    table[0][0] += change
    table[0][1] -= change/2
    table[1][0] -= change/2
    # Frobenius norm of the absolute error <= 22*change; measured norm >= 1/3.
    data["relative_error"] = 66*change
    signed = estimate(data)
    envelope = estimate(dict(data,error_kind="entrywise_envelope"))
    assert signed["geometry_used"]=="uniform" and envelope["geometry_used"]=="uniform and cellwise"
    for result in [exact_cell,signed,envelope]:
        lo,hi = map(Q,result["probability_ratio"])
        assert lo < exact < hi
    assert Q(envelope["probability_ratio"][1]) < Q(signed["probability_ratio"][1])
    trivial = estimate(dict(data,log_oscillations=[4,4,4],relative_error=2))
    assert list(map(Q,trivial["probability_ratio"]))==[0,1]
    return {"actual_ratio":str(exact),"unequal_cell_improves_upper":True,
            "signed_error_uses_uniform":True,"large_errors_allow_unit_ratio":True}


def tensor_control():
    # Visible eigenvalues 1,1/2. Each extra independent two-state system
    # below has normalized trace on the second half with no effect on the
    # observed joint law after marginalization.
    v = [[Q(3,4),Q(1,4)],[Q(1,4),Q(3,4)]]
    norm = sum(x*x for row in v for x in row)
    visible = [[x*x/norm for x in row] for row in v]
    vac = Q(4,5)**100
    for side in [4,20,100]:
        u = 1-Q(1,side)
        h = [[(1+u)/2,(1-u)/2],[(1-u)/2,(1+u)/2]]
        full_norm = norm*sum(x*x for row in h for x in row)
        observed = [[sum((x*y)**2 for row in h for y in row)/full_norm for x in row] for row in v]
        assert observed == visible and u*u > Q(1,4)
    return {"hundred_fully_resolved_identical_factors":{"vacuum_below_1e_9":vac<Q(1,10**9),
            "gibbs_ratio":"1/4"},"unresolved_hidden_ratio":"(1-1/L)^2",
            "same_visible_histogram":True}


def main():
    eta,d,a,h = Q(1,1000),Q(1,200),Q(1,20),Q(199,200)
    ratio = (((1+eta)*(Q(23,25)+d)+2*eta)/(1-eta)+d)**2
    upper = (ratio+2*a*a)/(h*h)
    assert 32**32 < 24*29**32 and 25**13 < 3*23**13
    assert Q(1,100)-Q(1,128)==Q(7,3200) and upper < Q(9,10)
    q,z,err = Q(8,11)**8,Q(72,1000),Q(1,10**9)
    loss = z*z/2
    r_upper = ((1+err)*(q+loss)+2*err)/(1-err)
    assert ((r_upper+loss)**2+2*(z/2)**2)/(1-loss)**2 < Q(1,100)
    ws = [cylinder(side) for side in (4,8,16,None)]
    assert all(w["oscillation_below_0_072"] and w["relative_operator_error_below_1e_9"] for w in ws)
    # Floating values are illustrations only. The period and ratios in the
    # analytic controls are exact and the integer millionths above are outward.
    photon = []
    for side in (8,32,128):
        x = pi/side
        photon.append({"side":side,"fixed_period_ratio":round(exp(-2*x),6),
                       "fixed_period_sign_disagreement":round(atan(sinh(x))/pi,6)})
    return {"cylinder_32_bins":ws,"four_dimensional_exact_upper":str(upper),
            "finite_matrix":paired_control(),"tensor":tensor_control(),
            "free_photon_period_one_illustration":photon}


if __name__=="__main__":
    print(json.dumps(main(), indent=2))
