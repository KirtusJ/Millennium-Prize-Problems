"""Cross-check A4's radial Wilson-staple coefficients by direct Haar integration."""
from fractions import Fraction as Q
from math import exp,sqrt
from scipy.integrate import quad


def moment(R,k):
    def density(y):
        return y**(k+0.5)*sqrt(1-y/(2*R))*exp(-y)
    return quad(density,0, min(2*R,90),epsabs=2e-13,epsrel=3e-13)[0]


def main():
    # Coefficients of unnormalized angular integrals: divide the square-root tilt
    # against the gamma moments term by term; no input from Bessel expansions.
    def gamma(k):
        v=Q(1)
        for i in range(k): v*=Q(3+2*i,2)
        return v
    triples=[[gamma(k),-gamma(k+1)/4,-gamma(k+2)/32] for k in range(3)]
    def divide(a,b):
        q=[a[0]/b[0]]
        for j in (1,2):
            q.append((a[j]-sum(b[i]*q[j-i] for i in range(1,j+1)))/b[0])
        return q
    mean,second=[divide(row,triples[0]) for row in triples[1:]]
    variance=[x-sum(mean[i]*mean[j-i] for i in range(j+1)) for j,x in enumerate(second)]
    assert variance==[Q(3,2),Q(-3,4),Q(-9,8)]
    for R in (80,160,320,640):
        z=moment(R,0)
        v=moment(R,2)/z-(moment(R,1)/z)**2
        corrected=R*R*(v-1.5+0.75/R)
        assert abs(corrected+9/8)<2.4/R
        print(f"R={R} radial second coefficient {corrected:.8f}")
    # E(delta)->3 is the local Wilson input. It is not inferred from radial quadrature.
    frozen=variance[2]/36
    environment=3*variance[1]/36
    assert (frozen,environment,frozen+environment)==(Q(-1,32),Q(-1,16),Q(-3,32))
    print(f"frozen={frozen}, environment={environment}, Wilson={frozen+environment}")


if __name__ == "__main__":
    main()
