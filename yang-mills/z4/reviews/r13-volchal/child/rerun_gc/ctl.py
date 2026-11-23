import numpy as np
def g(v):
    n=np.linalg.norm(v,axis=-1); s=v[...,0]**2+v[...,1]**2
    return np.where(n>0,s/(2*np.where(n>0,n,1)),0.0)
def L(p,q):
    return 4*g(p+q/2)*g(q/2-p)
if __name__=="__main__":
    l=float(L(np.array([1.,2,2]),np.zeros(3)))
    with open("control.txt","x") as f: f.write("%.6f\n"%l)
