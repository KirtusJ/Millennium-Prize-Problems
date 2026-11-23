import itertools, math
L=2
def lk(x,y,d): return ((x%L)*L+(y%L))*2+d
def plaq(x,y): return [lk(x,y,0),lk(x+1,y,1),lk(x,y+1,0),lk(x,y,1)]
P=[plaq(x,y) for x in range(L) for y in range(L)]
b=0.5; Z=Zt=0.0
for c in range(256):
    s=[1-2*((c>>i)&1) for i in range(8)]
    sp=[s[a]*s[b_]*s[c_]*s[d] for a,b_,c_,d in P]
    Z+=math.exp(b*sum(sp)); Zt+=math.exp(b*(sum(sp)-2*sp[0]))
with open('control.txt','x') as f:
    f.write(f"2D 2x2 torus beta={b} Z={Z:.6f} Z_tw={Zt:.6f} F=-ln(Z_tw/Z)={-math.log(Zt/Z):.6f}\n")
print(open('control.txt').read())
