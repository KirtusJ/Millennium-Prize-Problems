"""Check compact plaquette Taylor coefficients and finite-coupling source cumulants."""
from itertools import combinations
from pathlib import Path
import sys
sys.dont_write_bytecode = True
sys.path.insert(0,str(Path(__file__).resolve().parent))
import numpy as np
from scipy.special import ive
from response import box


def quaternion_product(u,v):
    a,x = u[0],u[1:]
    b,y = v[0],v[1:]
    return np.r_[a*b-x@y, a*y+b*x+np.cross(x,y)]


def real_word(vectors,e):
    value = np.array([1.,0,0,0])
    for x in vectors:
        angle = e*np.linalg.norm(x)
        value = quaternion_product(value,np.r_[np.cos(angle),e*np.sinc(angle/np.pi)*x])
    return value[0]


def trace_coefficients(x):
    r2 = [v@v for v in x]
    total = sum(x)
    quadratic = -(total@total)/2
    cubic = -sum(x[a]@np.cross(x[b],x[c]) for a,b,c in combinations(range(len(x)),3))
    fourth = sum(r**2 for r in r2)/24
    for i,j in combinations(range(len(x)),2):
        fourth += r2[i]*r2[j]/4+(x[i]@x[j])*((r2[i]+r2[j])/6
                        +sum(r2[k] for k in range(len(x)) if k not in (i,j))/2)
    for i,j,k,l in combinations(range(len(x)),4):
        fourth += (x[i]@x[j])*(x[k]@x[l])-(x[i]@x[k])*(x[j]@x[l])+(x[i]@x[l])*(x[j]@x[k])
    return quadratic,cubic,fourth


def words():
    rng = np.random.default_rng(10973)
    _,paths,B = box((5,1,1,1))
    X = rng.normal(size=(B.shape[1],3)).astype(np.longdouble)/2
    worst = 0.
    for path in paths:
        x = [sign*X[i] for i,sign in path]
        a,b,c = trace_coefficients(x)
        even,odd = [],[]
        for e in np.array([.04,.02,.01],dtype=np.longdouble):
            plus,minus = real_word(x,e),real_word(x,-e)
            even.append(((plus+minus)/2-1-e**2*a)/e**4)
            odd.append((plus-minus)/(2*e**3))
        for estimates,target in [(even,c),(odd,b)]:
            rich = (4*estimates[-1]-estimates[-2])/3
            worst = max(worst,abs(rich-target))
    assert worst < 3e-7, worst
    print('96 compact oriented words, maximum absolute cubic/quartic extrapolation error',worst)


def sphere_sources():
    vals = []
    for beta in (128,256,512,1024):
        n = np.arange(1,1+int(16*np.sqrt(beta/6)))
        B = ive(n,beta)
        prob = n**2*B**6
        prob /= prob.sum()
        score = beta*((ive(n-1,beta)+ive(n+1,beta))/(2*B)-1)-1
        center = score-prob@score
        v = prob@center**2
        t = -prob@center**3
        vals.append(beta*np.array([v-1/24,t+1/72]))
    pred = np.array([7/288,-11/1728])
    residual = 2*vals[-1]-vals[-2]-pred
    assert np.max(abs(residual))<5e-8
    print('exact character sums of distinct face scores, extrapolation errors',residual.tolist())

if __name__=='__main__':
    words()
    sphere_sources()
