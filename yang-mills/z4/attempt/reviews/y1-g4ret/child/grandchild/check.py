import numpy as np
def simpson(f,a,b,n):
    x=np.linspace(a,b,n+1);y=f(x);h=(b-a)/n
    return h/3*(y[0]+y[-1]+4*y[1:-1:2].sum()+2*y[2:-1:2].sum())
k=6*3.399810242
g=lambda r: np.sin(r)**2*np.exp(k*(np.cos(r)-1))
p=simpson(g,0,0.2,20000)/simpson(g,0,np.pi,20000)
s='%.12f'%p
try:
    with open('result.txt','x') as f: f.write(s+'\n')
except FileExistsError:
    print('result.txt exists; recomputed matches:',open('result.txt').read().strip()==s)
print(s)
