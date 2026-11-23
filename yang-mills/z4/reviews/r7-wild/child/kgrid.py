import numpy as np
g = np.logspace(-6, 8, 200001)
B = np.minimum(g, 17*np.sqrt(g)/8 + 3/16)
K = np.minimum(4, 8*B/g)
v = K*(1+B)
i = int(np.argmax(v))
print(f"max K*(1+B) = {v[i]:.10f} at g = {g[i]:.10g}")
