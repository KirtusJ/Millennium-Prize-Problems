import numpy as np
k=2*np.pi*np.arange(64)/64
v=np.mean(4*np.sin(k/2)**2)
with open("control.txt","x") as f: f.write("%.6f\n"%v)
print("%.6f"%v)
