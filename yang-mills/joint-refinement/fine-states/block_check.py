"""Cross-check each native parity reading against actual coarse orbit holonomies."""
from itertools import product
import importlib.util
from pathlib import Path
import subprocess
import sys
import numpy as np
from box_operators import Z4


def check(ops, path, fields):
    _, _, nt, n = fields.shape[:4]
    raw = fields[0,1:].transpose(1,4,3,2,0,5).astype("<f8").tobytes()
    result = subprocess.check_output([path,"fields",str(n),str(nt)],input=raw)
    measured = np.frombuffer(result,"<f8").reshape(nt,8,3)
    for x,y,z in product(range(2),repeat=3):
        block = np.zeros((1,4,nt,n//2,n//2,n//2,4))
        block[...,0] = 1.
        for mu in range(1,4):
            link = fields[:,mu]
            product_link = ops.qm(link, np.roll(link,-1,axis=1+mu))
            block[:,mu] = product_link[:,:,x::2,y::2,z::2]
        e = ops.operators(block)["E"][0,:,:,0]
        axes = np.array([[1,-1,0],[1,1,-2]]) / np.sqrt([[2],[6]])
        cyclic = np.array([[0,1,-1],[-1,0,1],[1,-1,0]])
        np.testing.assert_allclose(measured[:,x+2*y+4*z],(4/3)*e@axes@cyclic.T,atol=5e-14,rtol=0)
    return measured


if __name__ == "__main__":
    exe = Path(sys.argv[1]).resolve()
    spec = importlib.util.spec_from_file_location("box", Z4)
    ops = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ops)
    rng = np.random.default_rng(229714)
    for n in (6,8,10):
        fields = rng.normal(size=(1,4,4,n,n,n,4))
        fields /= np.linalg.norm(fields,axis=-1,keepdims=True)
        gauge = rng.normal(size=fields[:,0].shape)
        gauge /= np.linalg.norm(gauge,axis=-1,keepdims=True)
        a = check(ops,exe,fields)
        b = check(ops,exe,ops.gauge_tr(fields,gauge))
        np.testing.assert_allclose(a,b,atol=5e-14,rtol=0)
        print(n,"eight actual coarse origins, four slices and site-gauge rotation passed")
