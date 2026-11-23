#!/usr/bin/env python3
"""diffan.py -- POST-HOC variant (declared after the beta=4 floor was found, notes step8/9).
Replaces every connected correlator C(t) by the differenced correlator D(t) = C(t) - C(t+1), which removes a t-independent
floor (center-sector term, hypothesis H-floor) and keeps each exponential e^{-mt} with the same m. Everything else
(GEVP, t0, plateau rule PLAT, CTRL/LIM/MONO predicates and tolerances) is exactly as fixed in mc3.py / analyse3.py / ctrl0.py.
Additional predicate FLOOR (fixed before running this file): for the controls, the ctrl0-style result from D(t) at beta=4
is within 3 sigma of 0.96893 (if met, H-floor is supported; if not, the floor is not the whole story).
Usage: python3 diffan.py main OUT.md OUT.json runs...   |   python3 diffan.py ctrl OUT.md runs...
"""
import sys, importlib
sys.path.insert(0, '.')
import analyse3
_conn = analyse3.connected
def dconn(C, M, idx):
    c = _conn(C, M, idx)
    return c[..., :-1] - c[..., 1:]
analyse3.connected = dconn
mode = sys.argv.pop(1)
if mode == 'main':
    analyse3.main()
else:
    import ctrl0  # runs on import with sys.argv[1:] = OUT.md runs...
