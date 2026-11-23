"""Compare direct Wilson integration, the exact Bessel series and the discrete Gaussian."""
from math import ceil, log2, pi, sqrt
import numpy as np
from scipy.special import ive


def compare(beta, k):
    h = sqrt(beta/2)
    norm = np.hypot(1, k)
    spacing = 2*pi*h/norm
    # Resolve the narrowest peak on the entire original circle.
    size = 2**ceil(log2(max(8192, 32*k*h)))
    angle = 2*pi*np.arange(size)/size
    action = beta*(np.sin(angle/2)**2 + np.sin(k*angle/2)**2)
    score = h*(np.sin(angle) + k*np.sin(k*angle))/norm
    weight = np.exp(-action)
    z = weight.mean()

    modes = np.arange(1, ceil(16*h/k)+16)
    z_bessel = ive(0,h*h)**2 + 2*np.sum(ive(modes*k,h*h)*ive(modes,h*h))
    assert abs(z/z_bessel-1) < 1e-10

    cutoff = ceil(14/spacing)
    transverse = spacing*np.arange(-cutoff, cutoff+1)
    normal_weight = np.exp(-transverse**2/2)
    theta = normal_weight.sum()
    z_prediction = theta/(sqrt(2*pi)*h*norm)
    energy = np.dot(weight, action)/weight.sum()
    predicted_energy = .5 + .5*np.dot(normal_weight, transverse**2)/theta
    score_variance = np.dot(weight, score**2)/weight.sum()
    score_ibp = np.dot(weight, (np.cos(angle)+k*k*np.cos(k*angle))/(norm*norm))/weight.sum()
    assert abs(score_variance-score_ibp) < 1e-10
    laplace = np.dot(weight, np.exp(-action))/weight.sum()
    predicted_laplace = np.exp(-transverse**2).sum()/(sqrt(2)*theta)
    errors = [abs(z/z_prediction-1), abs(energy-predicted_energy),
              abs(score_variance-1), abs(laplace-predicted_laplace)]
    # A regression check on this finite grid; the proof uses an unspecified constant.
    assert beta*max(errors) < 3, (beta,k,errors)
    return energy, predicted_energy, score_variance, beta*max(errors)


if __name__ == '__main__':
    print('beta k     E[Y]      prediction   E[score^2]  beta*max_error')
    for beta in (64,256,1024):
        for k in (1,3,round(sqrt(beta)),round(3*sqrt(beta)),round(9*sqrt(beta))):
            energy,predicted,score,error = compare(beta,k)
            print(f'{beta:4d} {k:3d}   {energy:.8f}  {predicted:.8f}  {score:.8f}  {error:.6f}')
