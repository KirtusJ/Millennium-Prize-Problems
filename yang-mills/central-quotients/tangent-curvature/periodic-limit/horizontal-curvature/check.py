"""Check the horizontal witness using the manuscript's gauge and Hessian matrices."""
import argparse
import hashlib
import importlib.util
from pathlib import Path

import numpy as np


def check(lat):
    for side in (2, 3):
        box = lat.Lattice(side)
        for beta in (3., 12., 48.):
            for u in (1/beta, beta**(-.75), .5):
                angle = np.arcsin(np.sqrt(u))
                links = np.repeat(np.eye(2, dtype=complex)[None], box.nE, axis=0)
                tangent = np.zeros((box.nE, 3))
                for axis, sign in ((0,1),(1,-1)):
                    edges = box.links[:,2] == axis
                    links[edges] = np.cos(angle)*np.eye(2) + 1j*np.sin(angle)*lat.SIG[axis]
                    tangent[edges,axis] = sign*np.sqrt(2)
                v = tangent.ravel()
                half_traces = np.trace(lat.plaquettes(box,links),axis1=1,axis2=2).real/2
                gauge = lat.gauge_matrix(box,links,2)
                hessian = lat.hessV(box,links,beta,2)
                assert np.linalg.norm(gauge.T @ v, ord=np.inf) < 1e-12
                assert abs(v@v-4*side**4) < 1e-10
                assert abs(half_traces.min()-(1-2*u**2)) < 1e-12
                quotient = 1+(v@hessian@v)/(v@v)
                assert abs(quotient-(1-2*beta*u)) < 1e-11
    print('18 horizontal Rayleigh quotients and minimum plaquette traces verified')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('lat_py', type=Path, help='archived a4-chalcurv/lat.py from Z4')
    path = parser.parse_args().lat_py
    if hashlib.sha256(path.read_bytes()).hexdigest() != 'a088b530f1337711a6dbee2e707f88048d5bf63262e2c182bef82f22427d6470':
        raise ValueError('unexpected Z4 lattice source')
    spec = importlib.util.spec_from_file_location('z4_curvature', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    check(module)
