import numpy as np
n=4_000_001  # Simpson, even intervals
chi=np.linspace(0,np.pi,n); f=(2/np.pi)*np.sin(chi)**2
def simpson(y,x):
    h=x[1]-x[0]; return h/3*(y[0]+y[-1]+4*y[1:-1:2].sum()+2*y[2:-1:2].sum())
norm=simpson(f,chi)
# theta=pi-chi ; theta<pi/2 <=> chi>pi/2
m=chi>=np.pi/2; m2=chi[m]
P=simpson(f[m],chi[m]) if (m.sum()%2==1) else None
if P is None: P=simpson(f[m][:-1],chi[m][:-1])
with open('control_result.txt','x') as o:
    s=f"norm={norm:.9f}\nP(theta<pi/2)={P:.9f}\n"; o.write(s); print(s)
