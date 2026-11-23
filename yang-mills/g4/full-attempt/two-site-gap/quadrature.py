"""Independent deterministic check on the three-dimensional cube's eight center sectors.

The six angular variables integrate four S^3 spins modulo common O(4).
Floating quadrature checks the exact rational enclosures in cube.py.
"""
from itertools import combinations
from math import factorial, pi
import numpy as np
from numpy.polynomial.legendre import leggauss


def integrate(order, beta):
    index = np.arange(order)
    angle = (index+1)*pi/(order+1)
    coord = np.cos(angle)
    semi = 2*np.sin(angle)**2/(order+1)
    leg, uniform = leggauss(order)
    uniform /= 2
    circ = np.cos((index+.5)*pi/order)
    # Jacobi angles for S^3, then S^2, then S^1.
    w,u,v = np.meshgrid(coord,leg,circ,indexing="ij")
    w,u,v = (a.ravel() for a in (w,u,v))
    fourth_x = w
    fourth_y = np.sqrt(1-w*w)*u
    fourth_z = np.sqrt((1-w*w)*(1-u*u))*v
    fourth_weights = np.broadcast_to(semi[:,None,None]*uniform[None,:,None]/order,
                                     (order,)*3).ravel()
    odd = [1,2,4,7]
    pairs = list(combinations(range(4),2))
    functions = {}
    for magnetic_flux in (False,True):
        for seam in range(8):
            rows = []
            for even in [0,3,5,6]:
                signed = {}
                for axis in range(3):
                    # On the 2-cell each negative seam cancels one doubled direction.
                    if seam >> axis & 1:
                        continue
                    j=odd.index(even^(1<<axis))
                    sign=(-1)**((even&((1<<axis)-1)).bit_count()) if magnetic_flux else 1
                    signed[j]=sign
                terms=tuple((k,2*signed[i]*signed[j]) for k,(i,j) in enumerate(pairs)
                            if i in signed and j in signed)
                rows.append((len(signed),terms))
            functions[magnetic_flux,seam]=rows
    coeffs=[beta**(2*m)/(factorial(m)*factorial(m+1)) for m in range(15)]
    sums=dict.fromkeys(functions,0.)
    for i,x in enumerate(coord):
        sx=np.sqrt(1-x*x)
        for j,y in enumerate(coord):
            sy=np.sqrt(1-y*y)
            for k,z in enumerate(leg):
                sz=np.sqrt(1-z*z)
                gram=[x,y,fourth_x,x*y+sx*sy*z,x*fourth_x+sx*fourth_y,
                      y*fourth_x+sy*(z*fourth_y+sz*fourth_z)]
                cap={}
                for key,rows in functions.items():
                    val=1.
                    for row in rows:
                        if row not in cap:
                            count,terms=row
                            t=count+sum(sign*gram[a] for a,sign in terms)
                            cap[row]=np.polynomial.polynomial.polyval(t,coeffs)
                        val=val*cap[row]
                    sums[key]+=semi[i]*semi[j]*uniform[k]*np.dot(fourth_weights,
                                           np.broadcast_to(val,fourth_weights.shape))
    diagonal=sum(sums[False,s] for s in range(8))/8
    mixed=sum(sums[True,s] for s in range(8))/8
    return diagonal,mixed,diagonal/mixed


if __name__=="__main__":
    for beta in (.25,.5):
        for order in (5,8):
            print(beta,order,*(f"{v:.14g}" for v in integrate(order,beta)))
