"""numpy shim: eigvalsh with subset_by_index; symmetrizes nothing, uses numpy.linalg.eigvalsh (lower triangle)."""
import numpy as np
def eigvalsh(a, subset_by_index=None):
    w = np.linalg.eigvalsh(np.asarray(a))
    if subset_by_index is None:
        return w
    lo, hi = subset_by_index
    return w[lo:hi+1]
