"""Control T153. Predicate C1: |I - exp(rho^2/2)| < 1e-6 (closed form: Gaussian mgf; tolerance = 6-decimal answer)."""
import numpy as np
b=4.0; rho=1.0
t=np.linspace(-20,20,4000001)
I=np.trapezoid(np.sqrt(b/2/np.pi)*np.exp(-b*t*t/2-rho*np.sqrt(b)*t),t)
print("I=%.6f exact=%.6f"%(I,np.exp(rho**2/2)))
assert abs(I-np.exp(rho**2/2))<1e-6
with open("control.txt","x") as f: f.write("%.6f\n"%I)
