from fractions import Fraction as F
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pos=lambda x:max(x,F(0))
K=[F(2),F(3)]; eps=[F(1,10),F(1,20)]; kap=[F(1,50),F(1,100)]; d=F(1,2)
for i in range(2):
    b=d-eps[i]; d=pos(b-kap[i])/K[i]
d2=d
M=[F(1),K[0],K[0]*K[1]]  # M_0..M_2
def Mm(j): return F(1) if j<0 else M[j]
def rhs(inv,idx):
    s=sum(Mm(idx(i))*(eps[i-1]+kap[i-1]) for i in (1,2))
    return pos(F(1,2)-s)/Mm(inv)
R={"C":rhs(2,lambda i:i-1),"C'":rhs(2,lambda i:i),"C''":rhs(2,lambda i:i-2)}
lines=[f"d_2 = {d2}"]+[f"RHS {k} = {v}  d2>=RHS: {d2>=v}" for k,v in R.items()]
with open("result.txt","x") as f: f.write("\n".join(lines)+"\n")
print("\n".join(lines))
