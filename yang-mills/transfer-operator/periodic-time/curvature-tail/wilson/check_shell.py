"""Radius-one Wilson conditional integral, with two noncommuting shell links."""
import importlib.util
from pathlib import Path

import numpy as np
from scipy.special import ndtri
from scipy.stats import qmc

source = Path(__file__).resolve().parents[4]/"z4/attempt/reviews/a8-BL34/child/su2lib.py"
spec = importlib.util.spec_from_file_location("z4_quaternions", source)
q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q)


def main():
    curl = q.Dmatrix()
    inverse = np.linalg.inv(curl.T@curl)
    projection = curl@inverse@curl.T
    face = q.plaq_index(1, 2, 1, 1)
    other = q.plaq_index(1, 3, 1, 1)
    shell = np.zeros((24, 3))
    shell[face], shell[other] = [1.25, 0, 0], [0, 1.0, 0]
    shift = -inverse@curl.T@shell
    smooth = (np.eye(24)-projection)@shell
    c, m = projection[face, face], smooth[face]
    target = (3*c+m@m)/2
    assert abs(c-7/24) < 1e-13 and m@m > .3
    cholesky = np.linalg.cholesky(inverse)
    print(f"Gaussian shell prediction {target:.9f}, conditional variance per color {c:.9f}")
    for beta in [16, 64, 256]:
        differences, efficiencies = [], []
        for seed in range(6):
            unit = qmc.Sobol(21, scramble=True, seed=2748+seed).random_base2(11)
            normal = ndtri(unit).reshape(-1, 7, 3)
            phi = shift+cholesky@normal
            linear = curl@phi+shell
            reference = (linear[:, face]**2).sum(axis=1)/2
            links = np.zeros((len(unit), 8, 4))
            links[:, 0, 0] = 1
            links[:, 1:] = q.qexp(phi/np.sqrt(beta))
            # V2=identity. Each V1 is a shell edge of the indicated signed face.
            loops = q.qmul(q.qmul(links[:, q.PA], q.qexp(shell/np.sqrt(beta))),
                           q.qinv(links[:, q.PB]))
            actions = beta*(1-loops[:, :, 0])
            angles = np.linalg.norm(phi, axis=2)/np.sqrt(beta)
            log_weight = (-actions.sum(axis=1)+(linear**2).sum(axis=(1, 2))/2
                          + 2*np.log(np.abs(np.sinc(angles/np.pi))).sum(axis=1))
            log_weight[np.any(angles >= np.pi, axis=1)] = -np.inf
            weight = np.exp(log_weight-np.max(log_weight))
            weight /= weight.sum()
            # Use the same sampled Gaussian observable as a control variate.
            differences.append(weight@actions[:, face]-reference.mean())
            efficiencies.append(1/(len(unit)*(weight@weight)))
        error = np.std(differences, ddof=1)/np.sqrt(len(differences))
        print(f"beta={beta:3}: compact minus Gaussian mean {np.mean(differences):+.7f}, "
              f"replicate SE {error:.7f}, minimum ESS fraction {min(efficiencies):.4f}")
        assert min(efficiencies) > .8
        if beta == 256:
            assert abs(np.mean(differences)) + 4*error < .005


if __name__ == "__main__":
    main()
