import numpy as np
def cvals(N, M=32):
    """c(m), m=0..M-1, midpoint rule on N^3 grid of q in [-pi,pi]^3 (N even => q=0 not a node)."""
    q = -np.pi + (np.arange(N)+0.5)*2*np.pi/N
    h2 = 4*np.sin(q/2)**2
    g = np.zeros(N)
    for i in range(N):
        a = h2[i]
        s = a + h2[:,None] + h2[None,:]          # |h|^2
        w = 2*np.arcsinh(np.sqrt(s)/2)
        g[i] = np.sum((a+h2[:,None])/(2*np.sinh(w))*np.ones_like(s))
    g /= N**3
    m = np.arange(M)
    return np.array([np.sum(g*np.cos(mm*q)) for mm in m])
