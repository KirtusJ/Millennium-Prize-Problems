"""Control: 1-D HO ground state, FD. Expect 0.5 within 1e-5 (FD h^2 error, h=0.01 -> ~1e-6)."""
import numpy as np
n=2000;x=np.linspace(-10,10,n);h=x[1]-x[0]
H=np.diag(1/h**2+0.5*x**2)+np.diag(-0.5/h**2*np.ones(n-1),1)+np.diag(-0.5/h**2*np.ones(n-1),-1)
e=np.linalg.eigvalsh(H)[0]
open("control.txt","x").write("%.6f\n"%e);print(e)
