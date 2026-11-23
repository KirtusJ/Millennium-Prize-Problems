"""T57 part B. Predicates fixed before first run (seed 20240002):
PB1 (for-all hypothesis): among random 6-angle vectors in (-pi,pi] with sum=2*pi*m, count those with m!=0 ("qualifying");
    for all qualifying, max|theta|>=pi/3 - 1e-12 and s>=1/2 - 1e-12. Tolerance 1e-12: double rounding of cos/sums (~1e-15) with margin.
PB2: all-equal pi/3 example: sum==2pi (tol 1e-12), m=1, s==1/2 within 1e-12. Expectation (mine): in raw floats 1-cos(pi/3) may be 0.5-eps, so exact >= fails; tolerance needed.
PB3: exponent: exp(D-(beta/2)/8)==exp(D-beta/16) and exp(D - beta*eta/K^2/8)==exp(D-beta*eta/(8K^2)) over 1000 random params (rel tol 1e-12).
PB4: chi(V)<=K max chi(U_q), s(V)>=eta  => max s(U_q)>=eta/K^2 on 10000 random cases (tol 1e-12).
PB5 (strict control, expectation): raw float test 'min s >= 0.5' without tolerance on the equal-pi/3 example -- recorded, not required.
"""
import numpy as np, json, math
rng=np.random.default_rng(20240002); pi=math.pi; tol=1e-12
nq=0; bad=0; mins=9; minmax=9; tries=0
while nq<5000:
    tries+=1
    th=rng.uniform(-pi,pi,6)
    # force sum to a nonzero multiple of 2pi half the time by adjusting last angle then wrapping check
    if tries%2==0:
        m=int(rng.choice([-2,-1,1,2])); last=2*pi*m-th[:5].sum()
        if not(-pi<last<=pi): continue
        th[5]=last
    S=th.sum(); m=round(S/(2*pi))
    if abs(S-2*pi*m)>1e-9: continue   # not a valid cube configuration
    if m==0: continue
    nq+=1
    mx=np.abs(th).max(); s=(1-np.cos(th)).max()
    minmax=min(minmax,mx); mins=min(mins,s)
    if mx<pi/3-tol or s<0.5-tol: bad+=1
th=np.full(6,pi/3); ex_sum=th.sum(); ex_s=1-math.cos(pi/3)
PB2=abs(ex_sum-2*pi)<tol and abs(ex_s-0.5)<tol
raw=(ex_s>=0.5)
e3=0
for _ in range(1000):
    D,b,eta,K=rng.uniform(0,5),rng.uniform(1,50),rng.uniform(.01,2),rng.uniform(1,5)
    e3=max(e3,abs(math.exp(D-(b/2)/8)/math.exp(D-b/16)-1),abs(math.exp(D-b*(eta/K**2)/8)/math.exp(D-b*eta/(8*K*K))-1))
b4=0
for _ in range(10000):
    s=rng.uniform(0,2,int(rng.integers(1,7))); K=rng.uniform(1,4)
    chiV=rng.uniform(0,1)*K*math.sqrt(s.max())        # chi(V)<=K max chi
    sV=chiV**2; eta=sV*rng.uniform(0.5,1)             # s(V)>=eta
    if eta<=0: continue
    if s.max()<eta/K**2-tol: b4+=1
res={"qualifying_cases":nq,"draws_total":tries,"min_max_abs_angle":minmax,"pi/3":pi/3,"min_s_max":mins,"PB1_violations":bad,
 "example_sum_minus_2pi":ex_sum-2*pi,"example_s":ex_s,"example_s_repr":repr(ex_s),"PB2":PB2,"PB5_raw_s_ge_half":raw,
 "PB3_maxrelerr":e3,"PB4_violations":b4}
with open("result_B.json","x") as f: json.dump(res,f,indent=1)
print(res)
import sys; sys.exit(0 if bad==0 and PB2 and e3<1e-12 and b4==0 else 1)
