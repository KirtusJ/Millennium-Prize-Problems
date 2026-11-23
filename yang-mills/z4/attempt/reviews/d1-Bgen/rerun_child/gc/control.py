import numpy as np
s=1e-6
a=np.arccos(1-s)/np.pi/np.sqrt(s)
b=2*np.arcsin(np.sqrt(s/2))/np.pi/np.sqrt(s)
with open('control.txt','x') as f:
    f.write(f"arccos form: {a!r}\narcsin form (stable): {b!r}\nexact sqrt(2)/pi={np.sqrt(2)/np.pi!r}\n")
print(open('control.txt').read())
