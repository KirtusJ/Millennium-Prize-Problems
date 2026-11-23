"""Run Z4's extended box instrument and G4's sampler on the same fields."""
import argparse
import importlib.util
from itertools import product
from pathlib import Path
import runpy
from tempfile import TemporaryDirectory
import numpy as np

ROOT = Path(__file__).resolve().parent
box = runpy.run_path(str(ROOT.parent/"fine-states/box_operators.py"))
loop = runpy.run_path(str(ROOT/"plaquette_check.py"))["loop"]


def main(rustc):
    src = ROOT.parents[1]/"z4/attempt/reviews/l1-mcw/mcp.py"
    spec = importlib.util.spec_from_file_location("z4_mcw",src)
    z4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(z4)
    rng = np.random.default_rng(240613)
    with TemporaryDirectory() as tmp:
        exe = box["build"](Path(tmp),rustc)
        for n in (2,4):
            field = rng.normal(size=(4,4,6,n,n,n,4))
            field /= np.linalg.norm(field,axis=-1,keepdims=True)
            frame = rng.normal(size=field[:,0].shape)
            frame /= np.linalg.norm(frame,axis=-1,keepdims=True)
            z4.BETA_OP = 3.4
            g = box["check"](z4,exe,field)
            rotated = box["check"](z4,exe,z4.gauge_tr(field,frame))
            np.testing.assert_allclose(g,rotated,rtol=0,atol=3e-14)
            ps = z4.operators(field)["PS"][0,:,:,0]
            local = field[0,[1,2,3,0]].transpose(2,3,4,1,0,5)
            for t in range(6):
                planes = [(1,2),(0,2),(0,1)]
                ref = [sum(z4.BETA_OP*(1-loop(local,xyz+(t,),i,j))
                           for xyz in product(range(n),repeat=3)) for i,j in planes]
                np.testing.assert_allclose(ps[t],ref,rtol=3e-14,atol=3e-14)
            print(n, "signed winding slices",2*len(g),"plane sums",ps.size)


if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--rustc",default="rustc")
    main(p.parse_args().rustc)
