import numpy as np
def cstar(n=400):
    x,w=np.polynomial.legendre.leggauss(n)
    t=(x+1)*np.pi/2; w=w*np.pi/2
    a=np.pi/2*(1-np.cos(t)); da=np.pi/2*np.sin(t)
    return np.sum(w*da*np.sqrt(4*np.arcsinh(np.sin(a))))
if __name__=="__main__":
    print(cstar(200),cstar(800),file=__import__('sys').stderr)
    open("control.txt","x").write("%.6f\n"%cstar(800))
