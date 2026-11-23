from math import *
out=[]
def P_(s): out.append(s); print(s)
P_("control asinh(1)=%.6f"%asinh(1))
e=lambda S:2*asinh(S)
k=lambda S:sqrt(1+S*S)/S
def MA2(eta):
    r02=eta*sinh(eta)/4
    m0=(1-exp(-3*eta/4))/2; m1=(1-exp(-1/16))/2
    c=1/tanh(eta)
    return 2*sqrt(2+r02)+max(c*log(1/m1),0.75*eta*c+log(1/m0))
def Mc2(eta):
    C=e(sqrt(2))+eta+1/8+1
    return sqrt(2)/sinh(eta)*(e(sqrt(2))+1)+log(4)-log(exp(eta/2)-1)+C
def P(S,eta): return exp(e(S)-MA2(eta)/k(S))
for eta in (0.4,0.01):
    P_("eta=%g MA2=%.12f Mc2=%.12f"%(eta,MA2(eta),Mc2(eta)))
eta=0.01;S=sinh(eta)
p=P(S,eta)
P_("eta=0.01 S=s_lo=%.12g P(s_lo)=%.12e  P+exp(-1/16)=%.12f"%(S,p,p+exp(-1/16)))
open("result.txt","x").write("\n".join(out)+"\n")
