import numpy as np
N=4096
k=np.pi*(2*np.arange(N)+1)/N-np.pi
v=np.mean(4*np.sin(k/2)**2)  # midpoint rule: sum f*dk/(2pi) = mean
with open('control.txt','x') as f: f.write(f"{v!r}\nabs err {abs(v-2):.3e} PASS={abs(v-2)<1e-10}\n")
print(v)
