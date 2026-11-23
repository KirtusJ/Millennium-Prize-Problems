"""numpy-only shim for scipy.special.ive with integer order(s), written by h1-a4 (scipy not installed)."""
import sys, numpy as np
sys.path.insert(0, "/home/user/z4-workers/h1-a4")
from besselnp import ive0, ratio
def _one(k, x):
    v = float(ive0(np.array([float(x)]))[0])
    for n in range(1, int(k)+1): v *= ratio(n, float(x), extra=1000+int(x))
    return v
def ive(k, x):
    if np.ndim(k) == 0: return _one(k, x)
    return np.array([_one(kk, x) for kk in np.asarray(k)])
