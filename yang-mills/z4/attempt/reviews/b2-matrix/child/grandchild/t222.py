import numpy as np
d='../data/'
def C(r):
    X=np.vstack([np.loadtxt(d+f's{i}.X.csv',delimiter=',',skiprows=1) for i in r])
    Y=X-X.mean(0); return Y.T@Y/len(X)
def D(r):
    s=0
    for i in r:
        A=np.loadtxt(d+f's{i}.Dc.txt',skiprows=1); assert A.shape==(24,196)
        s=s+A.mean(0).reshape(14,14)
    return s/len(r)
c=C(range(16,32));dd=D(range(16,32))
print("D00 %.10g C00 %.10g q %.10g"%(dd[0,0],c[0,0],dd[0,0]/c[0,0]))
s=np.linalg.svd(C(range(16)),compute_uv=False)
print("cond %.10g smin %.6g smax %.6g n<1e-12 %d"%(s[0]/s[-1],s[-1],s[0],(s<1e-12).sum()))
