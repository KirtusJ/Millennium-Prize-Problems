"""Sensitivity fits for a measured open-slab slope. Requires NumPy."""
import csv
import sys
import numpy as np
from calibration import TABLE,tune

def results(rows):
    selected=sorted((int(r["N"]),float(r["value"]),float(r["se"])) for r in rows
        if (r["phase"],r["starts"],r["margin_L"],r["stat"],r["probe"],r["tau_over_L"])
        ==("production","all","1","eff","E_wind","0.5-1.0"))
    n,y,se=np.array(selected).T
    assert len(n)==5 and np.isfinite(y).all() and np.all(se>0)
    beta=np.array([tune(TABLE[int(k)]) for k in n])
    for label,matrix in (("constant",np.ones((len(n),1))),
                         ("bare",(beta/beta[0])[:,None]**(-1/3)),
                         ("linear_a",np.stack((n**0,1/n),axis=1)),
                         ("quadratic_a",np.stack((n**0,1/n**2),axis=1))):
        x=matrix/se[:,None]
        coeff=np.linalg.lstsq(x,y/se,rcond=None)[0]
        cov=np.linalg.inv(x.T@x)
        chi=np.sum(((y-matrix@coeff)/se)**2)
        yield label,float(coeff[0]),float(cov[0,0]**.5),float(chi),len(y)-len(coeff)

if __name__=="__main__":
    with open(sys.argv[1],newline="",encoding="utf8") as f:
        for name,y,e,chi,dof in results(csv.DictReader(f)):
            print(f"{name} {y:.6f} {e:.6f} {chi:.6f} {dof}")
