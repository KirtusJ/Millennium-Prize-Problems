"""Exact finite-state transfer controls for adjacent-slice prediction and time sums."""
import numpy as np
from numpy.polynomial.legendre import leggauss


def main():
    h, w = leggauss(5)
    pi = w/2
    g = h*h-1/3
    identity = np.eye(len(h))
    uniform = np.broadcast_to(pi,identity.shape)
    for alpha in (0.21,0.07):
        P = (1-alpha)*uniform+alpha*identity
        for u in (h,g):
            prediction = P@u
            two = (pi*u)@(P@prediction)
            np.testing.assert_allclose(two,pi@(prediction**2),atol=2e-15)
            assert (pi*u)@prediction > 4*two and two>0
        # Identical modes attain the l1 estimate. Treating them as independent would fail.
        copies=7
        coherent=np.sum(np.stack([h]*copies),axis=0)
        true_mass=pi@((P@coherent)**2)
        diagonal_mass=copies*(pi@((P@h)**2))
        np.testing.assert_allclose(true_mass,copies*diagonal_mass,atol=1e-14)
        assert true_mass>6.9*diagonal_mass
        inn = h[None,:]-(P@h)[:,None]
        np.testing.assert_allclose(np.sum(P*inn,axis=1),0,atol=2e-15)
        conditional = np.sum(P*inn**2,axis=1)
        np.testing.assert_allclose(conditional,P@(h**2)-(P@h)**2,atol=2e-15)
        print(f"finite transfer alpha={alpha:g} one={float((pi*h)@(P@h)):.8f} two={float(pi@((P@h)**2)):.8f}")
    for r in (40,160,640):
        alpha=1/r
        P=(1-alpha)*uniform+alpha*identity
        u=1.1
        kernel=P@np.diag(np.exp(1j*u*h/np.sqrt(r)))
        cf=pi@np.linalg.matrix_power(kernel,r)@np.ones_like(h)
        var=(1+2*sum((1-n/r)*alpha**n for n in range(1,r)))/3
        target=np.exp(-u*u/6)
        assert abs(cf.imag)<1e-11 and abs(cf.real-target)<1/r and abs(var-1/3)<1/r
        assert abs(cf.real-np.exp(-u*u/3))>0.1
        print(f"r={r}: sum variance={var:.8f}; characteristic error={abs(cf-target):.8f}")
    print("Finite reversible comparison; the Wilson estimates use conditional integration.")


if __name__ == "__main__":
    main()
