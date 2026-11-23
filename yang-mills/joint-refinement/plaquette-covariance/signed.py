"""Exercise both of Z4's signed conventions on the same physical windings."""
from pathlib import Path
import importlib.util
import numpy as np

ROOT=Path(__file__).resolve().parents[2]/"z4/attempt/reviews"


def load(path):
    spec=importlib.util.spec_from_file_location(path.stem,path)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    site=load(ROOT/"i1-mc3/mc3.py")
    box=load(ROOT/"l1-mcw/mcp.py")
    box.BETA_OP=3.4
    angle=np.pi/4
    winds=np.array([[np.cos(angle),np.sin(angle),0,0]]*2+[[1,0,0,0]])
    old=site.operators(winds)["T2"][0,0]
    for n in (2,4):
        field=np.zeros((1,4,4,n,n,n,4))
        field[...,0]=1
        for axis in (1,2):
            field[:,axis,...,0]=np.cos(angle/n)
            field[:,axis,...,1]=np.sin(angle/n)
        current=box.operators(field)
        np.testing.assert_allclose(current["T2"][:,:,0,0],-1,atol=2e-14)
        np.testing.assert_allclose(current["PS"],0,atol=2e-12)
        np.testing.assert_allclose(old,.25,atol=2e-14)
        print(n,old,current["T2"][0,0,0,0])


if __name__=="__main__":
    main()
