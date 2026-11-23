# Check F6: x^(2j) exp(-c x^2) <= (j/(e c))^j, equality at x^2=j/c. 50-digit decimal (mpmath unavailable).
from decimal import Decimal as D, getcontext
getcontext().prec = 50
def sin(x):
    s=t=x; n=1
    while abs(t)>D(10)**-60:
        t=-t*x*x/((2*n)*(2*n+1)); s+=t; n+=1
    return s
ctrl = sin(D(1)) - 1 + D(1)/6
with open('control.txt','w') as f: f.write('%.6f\n' % ctrl)
E = D(1).exp()
def lhs(x2,j,c): return x2.sqrt()**(2*j) * (-c*x2).exp()
def rhs(j,c): return (D(j)/(E*c))**j
maxeq = D(0); allok = True; minslack = None
with open('results.txt','x') as out:
    out.write('j c factor lhs rhs rel=(lhs-rhs)/rhs\n')
    for j in (1,2,3,5,10,50,200):
        for cs in ('0.01','1','37'):
            c = D(cs); r = rhs(j,c)
            for name,fac in (('eq',D(1)),('minus',D('0.999')),('plus',D('1.001'))):
                x2 = D(j)/c*fac
                l = lhs(x2,j,c); rel = (l-r)/r
                if name=='eq': maxeq = max(maxeq, abs(rel))
                else:
                    allok &= (l<r); s=-rel; minslack = s if minslack is None else min(minslack,s)
                out.write(f'{j} {cs} {name} {l:.15e} {r:.15e} {rel:.6e}\n')
    out.write(f'\nmax|rel diff| at equality: {maxeq:.6e}\nperturbed all lhs<rhs: {allok}\nmin perturbed slack: {minslack:.6e}\n')
print(open('control.txt').read().strip(), f'{maxeq:.3e}', allok, f'{minslack:.3e}')
