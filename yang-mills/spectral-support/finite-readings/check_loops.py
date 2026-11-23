"""Class-function rotor on one isolated SU(2) cycle. Electric coefficient is one."""
import math

import numpy as np
from scipy.linalg import eigh_tridiagonal


def inspect(size, length, g):
    labels = np.arange(size)
    energies, states = eigh_tridiagonal(
        length*labels*(labels+2)/4+g, np.full(size-1, -g/2))
    vacuum = states[:, 0]
    energies -= energies[0]
    link_distance = np.linalg.norm(vacuum[1:])
    link_kinetic = np.sum(labels*(labels+2)*vacuum**2)
    assert link_distance <= 4*g/3 + 1e-12
    assert link_kinetic <= 16*g*g/3 + 1e-12

    fundamental = np.diag(np.ones(size-1), 1)+np.diag(np.ones(size-1), -1)
    adjoint = fundamental@fundamental-np.eye(size)
    result = [link_distance, link_kinetic]
    for n, operator, slope, fraction in ((1, fundamental, 2, 1/6), (2, adjoint, 4, 1/8)):
        vector = operator@vacuum
        vector -= np.dot(vacuum, vector)*vacuum
        mass = (states.T@vector)**2
        center = length*n*(n+2)/4
        residual = np.sqrt(mass@(energies-center)**2)
        # Use the sharper one-face incident-potential budget of this isolated cycle.
        assert residual <= length*slope*2*g/math.sqrt(3) + 1e-10
        radius = fraction*center
        outside = mass[np.abs(energies-center) > radius].sum()
        inside = mass.sum()-outside
        assert outside <= (residual/radius)**2+1e-12
        if g <= math.sqrt(3)/512:
            assert inside >= .75 and outside <= 1/16+1e-12
        clock = 4*math.log(2)/length
        transfer = np.exp(-clock*energies)
        excess = mass@((transfer-1/16)*(1-transfer))
        if n == 1 and g <= math.sqrt(3)/512:
            assert excess >= 1/128
        result.extend([residual, inside, outside, excess])
    return np.array(result)


if __name__ == "__main__":
    for length in (4, 6, 12):
        for g in (0., .0001, .003, .1):
            coarse = inspect(48, length, g)
            fine = inspect(80, length, g)
            np.testing.assert_allclose(coarse, fine, rtol=1e-8, atol=5e-12)
            print(f"length={length} g={g:g}  K_link={fine[1]:.9g}  "
                  f"residuals=({fine[2]:.8g},{fine[6]:.8g})  "
                  f"band masses=({fine[3]:.9g},{fine[7]:.9g})  D_F={fine[5]:.9g}")
    weak = inspect(80, 4, .0001)
    assert weak[1] > .0001**2/64 and weak[4] > 0
    print("False stronger kinetic constant and exact interacting single-energy support rejected.")
