"""Independent quadratures for a compact translated magnetic packet and its angular mode."""
from math import pi, sqrt
from pathlib import Path
import sys
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import ndtri, roots_jacobi
from scipy.stats import qmc

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from check_scales import profile_hat


def magnetic(order, times):
    # The fourfold bump convolution has each coordinate supported in [-4,4].
    # The two identical copies have centers 10 physical units apart.
    z, w = leggauss(order)
    p, wp = (z+1)*9, w*9
    axis = wp*profile_hat(p)**2/pi
    p1, p2, p3 = np.ix_(p,p,p)
    e = np.sqrt(p1**2+p2**2+p3**2)
    density = np.einsum("i,j,k->ijk", axis, axis, axis)*(p1**2+p2**2)/(2*e)
    shift = np.cos(10*p1)
    return np.array([[(density*np.exp(-t*e)*factor).sum() for factor in (1+shift,1-shift)]
                     for t in times])


def harmonic(d, rho, order):
    # q divides the total Gaussian squared radius, u is the directional cosine.
    x, wx = roots_jacobi(order,d/2-1,d/2-1)
    u, wu = roots_jacobi(order,(d-3)/2,(d-3)/2)
    q = (x[:,None]+1)/2
    a,b = (1+rho)*q, (1-rho)*(1-q)
    h = (a-b)/np.sqrt((a+b)**2-4*a*b*u**2)
    weight = np.outer(wx/wx.sum(),wu/wu.sum())
    mean = np.sum(weight*h)
    bplus = sqrt(d/2)*np.sum(weight*x[:,None]*h)
    return mean,bplus,np.sum(weight*(h-mean)**2)


def angle(p,m,rho):
    f = sqrt(1+rho)*p+sqrt(1-rho)*m
    g = sqrt(1+rho)*p-sqrt(1-rho)*m
    return np.sum(f*g,axis=1)/(np.linalg.norm(f,axis=1)*np.linalg.norm(g,axis=1))


def main():
    times = [0,0.3,1,20,200]
    high = magnetic(152,times)
    mid = magnetic(128,times)
    np.testing.assert_allclose(mid[:3],high[:3], rtol=8e-7)
    sums = high[0]
    rho = (sums[0]-sums[1])/sums.sum()
    assert -1 < rho < 1
    lambdas = high/sums
    assert np.all((lambdas[1:] > 0) & (lambdas[1:] < 1))
    mu,b,var = harmonic(3,rho,512)
    np.testing.assert_allclose(harmonic(3,rho,384),[mu,b,var], atol=2e-6)
    m0, b0, v0 = harmonic(3,0,512)
    np.testing.assert_allclose([m0,b0,v0],[0,8/(3*pi*sqrt(6)),1/3],atol=2e-7)
    print(f"compact packet v+w={sums[0]:.10g} v-w={sums[1]:.10g} w/v={rho:.10g}")
    print(f"Haar-independent benchmark b+={b0:.10g}; packet mean={mu:.10g}, b+={b:.10g}, variance={var:.10g}")
    for index in (1,2):
        lp,lm = lambdas[index]
        bounds = b**2*np.sum(lambdas[index]**2)
        estimates=[]
        for seed in (107,331,791,2179):
            X=ndtri(qmc.Sobol(12,scramble=True,seed=seed).random_base2(17)).reshape(-1,4,3)
            p,m,a,c = (X[:,i] for i in range(4))
            y=angle(p,m,rho)
            yt=angle(lp*p+sqrt(1-lp*lp)*a,lm*m+sqrt(1-lm*lm)*c,rho)
            estimates.append(np.mean((y-mu)*(yt-mu)))
        corr=np.mean(estimates)
        assert bounds-0.0007 < corr < var and bounds>0
        print(f"t={times[index]:g}, sum/difference correlations {lp:.8f} {lm:.8f}; angular covariance {corr:.7f}, quadratic lower bound {bounds:.7f}, scramble spread {np.ptp(estimates):.6f}")
    # Near zero the normalized angular density average for the plus weight is twice
    # the unsplit one, and the minus density has two additional powers of energy.
    x, wx = leggauss(100)
    # After azimuthal integration about axis 1, theta_1^2+theta_2^2 averages to (1+x^2)/2.
    for E in (0.01,0.001,0.0001):
        u = E*10*x
        a = np.sum(wx*(1+x*x)*(1+np.cos(u)))/(8/3)
        minus = np.sum(wx*(1+x*x)*2*np.sin(u/2)**2)/(8/3)
        assert abs(2-a-minus)<1e-13
        np.testing.assert_allclose(minus/E**2,20,rtol=0.001)
    # The leading profile is unity in this independent angular-only threshold check.
    print("angular threshold factors 2 and 20*E^2; raw low-window exponent 8")


if __name__ == "__main__":
    main()
