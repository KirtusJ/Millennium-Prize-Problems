"""Control: Z2 gauge theory on 2x2 torus (N=4 plaquettes, 8 links), brute force 2^8.
Predicate C1: brute-force F at beta=0.5 equals analytic -ln[(c^4-s^4)/(c^4+s^4)] to 1e-12
(tolerance = float rounding). Usage: control.py [write]  -- write mode opens control.txt with 'x'."""
import itertools, math, sys
def links(x,y,mu):  # index
    return ((x%2)*2+(y%2))*2+mu
def plaqs():
    P=[]
    for x in range(2):
        for y in range(2):
            P.append([links(x,y,0),links(x+1,y,1),links(x,y+1,0),links(x,y,1)])
    return P
P=plaqs()
def Z(beta,twist):
    z=0.0
    for s in itertools.product([1,-1],repeat=8):
        e=0
        for i,p in enumerate(P):
            v=s[p[0]]*s[p[1]]*s[p[2]]*s[p[3]]
            e+=(-beta if (twist and i==0) else beta)*v
        z+=math.exp(e)
    return z
b=0.5
F=-math.log(Z(b,1)/Z(b,0))
c,s=math.cosh(b),math.sinh(b)
Fa=-math.log((c**4-s**4)/(c**4+s**4))
assert abs(F-Fa)<1e-12,(F,Fa)
print("%.6f"%F, "analytic %.6f"%Fa)
if len(sys.argv)>1:
    with open("control.txt","x") as f: f.write("%.6f\n"%F)
