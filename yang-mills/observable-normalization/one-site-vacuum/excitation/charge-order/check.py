"""Recompute the angular metric and the extrapolation sensitivity."""
from itertools import combinations
import numpy as np

rng = np.random.default_rng(275)
for _ in range(200):
    x, y = rng.normal(size=(2, 3))
    t, u, v = x@x+y@y, x@x-y@y, 2*x@y
    rho = np.hypot(u, v)
    gt, gu, gv = 2*np.r_[x,y], 2*np.r_[x,-y], 2*np.r_[y,x]
    gr = (u*gu+v*gv)/rho
    gp = (u*gv-v*gu)/rho**2
    np.testing.assert_allclose([gp@gt, gp@gr, gp@gp], [0,0,4*t/rho**2], atol=1e-12)
    np.testing.assert_allclose(t*t-rho*rho, 4*np.linalg.norm(np.cross(x,y))**2, atol=1e-12)

b = np.array([128.,256.,512.,1024.])
y = np.array([1.836969,1.886615,1.918586,1.939100])
for p in [1., 4/3]:
    design = np.column_stack([np.ones_like(b), b**(-2/3), b**(-p)])
    c = np.linalg.lstsq(design,y,rcond=None)[0]
    print(f"p={p:.6f} intercept={c[0]:.9f} rms={np.sqrt(np.mean((design@c-y)**2)):.9f}")
    for keep in combinations(range(4),3):
        fitted = np.linalg.solve(design[list(keep)],y[list(keep)])
        print(keep, f"{fitted[0]:.9f}")
