import math
pi=math.pi
def direct(j,c,M=200):
    s=0.0
    for m in range(1,M+1):
        s+=2*(m**(2*j))*math.exp(-c*m*m)
    return s+(1.0 if j==0 else 0.0)
def poisson(j,c,K=20):
    s=0.0
    for k in range(-K,K+1):
        b=pi*pi*k*k
        g=c**-0.5; g1=-0.5*c**-1.5; g2=0.75*c**-2.5
        h=math.exp(-b/c); h1=b/c**2*h; h2=(b*b/c**4-2*b/c**3)*h
        f=[g*h, g1*h+g*h1, g2*h+2*g1*h1+g*h2][j]
        s+=math.sqrt(pi)*f*(-1)**j
    return s
with open("control.txt","x") as f:
    f.write("%.6f\n"%direct(0,pi))
out=[]
for j,c in [(2,0.01),(1,0.3),(0,0.01)]:
    a=direct(j,c); b=poisson(j,c)
    out.append("theta_%d(%g): direct=%.12e poisson=%.12e reldiff=%.3e"%(j,c,a,b,abs(a-b)/abs(a)))
with open("results.txt","x") as f: f.write("\n".join(out)+"\n")
print(open("control.txt").read()); print("\n".join(out))
