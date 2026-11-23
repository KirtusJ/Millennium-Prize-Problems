import math
atoms=[(1.0,2.0)]
C=lambda t:sum(w*math.exp(-t*E) for w,E in atoms)
T=lambda K:sum(w*math.exp(-E) for w,E in atoms if E>K)
a=C(0.5)/C(1)
D=math.exp(1);K=1.5
lhs=T(K);rhs=D*math.exp(-K)*C(1)
holds=lhs<=rhs
with open('results.md','x') as f:
    f.write(f"# Results\n\n- C(1/2)/C(1) = {a!r} (exp(1) = {math.exp(1)!r})\n- T(1.5) = {lhs!r}\n- D*exp(-K)*C(1) = {rhs!r}\n- T(K) <= RHS holds: {holds}\n\nVerdict: mutated inequality {'HOLDS' if holds else 'FAILS'} (LHS/RHS = {lhs/rhs!r}, exp(0.5)).\n")
print(a,lhs,rhs,holds)
