# Verification of the frozen transverse calculation

The [quaternion control](check.py) builds all 24 links and all 24 positively oriented spatial plaquettes. It independently differences the exact plaquette action in 42 real directions. One basis comes from the ordinary lattice divergence. The other uses the singular vectors of the 21 infinitesimal site gauge directions at the chosen background. At the center the 42 Hessian eigenvalues agree with the $18,18,6$ multiplicities. At a generic commuting triple of angles $(0.13,-0.17,0.08)$ every eigenvalue on each plane agrees with the corresponding flat formula within $3\times10^{-7}$.

At $r=0.005$ the table gives the finite-difference Gaussian energy change divided by $r^2$ alongside its analytic limit. Parallel and antiparallel refer to backgrounds $(r e_1,\pm r e_1,0)$. Orthogonal refers to $(r e_1,r e_2,r e_3)$.

| Background | Fixed, measured | Fixed, limit | Horizontal, measured | Horizontal, limit |
|---|---:|---:|---:|---:|
| Parallel | −4.204932 | −4.204889 | 0.040655 | 0.040733 |
| Antiparallel | −5.406323 | −5.406285 | 0.040655 | 0.040733 |
| Orthogonal | −7.209019 | −7.208381 | 0.059943 | 0.061100 |

Along one seeded transverse direction in a noncommuting background, the antisymmetric spatial difference divided by $2s^3$ approaches 0.06009. This tests a detail of the written proof: the spatial cubic is present before parity averaging. The exact transfer norm and eigenvalue remainder estimates are analytic; these numerical controls evaluate the plaquette Hessian and cubic directly.

Three native [PCP OS proof-template workers](worker.c) booted in parent, child and grandchild order, with the host following the first two requests. The parent counted the real curl polarizations. The child checked the cancellation of cubic projections on a symmetric grid. The grandchild tested the complementary-gap inequality on bounded integers. Generation and separate replay each produced the same [Lean source](HardVacuum.lean), SHA-256 `800be4bd0a258feb8967ddaf110684786e5b64aa2a1b93bbcfb47d0a1052e9dd`, with 47 kernel register events in each boot. The kernel SHA-256 was `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`.

| Guest | ELF SHA-256 |
|---|---|
| Parent | `adb27808d7e2cf6f0c0fac2cd8c35e2c4fe6335a027483e3eec453a11be45a88` |
| Child | `ae879e0b35834a9728c9d424a36e53c5239745203e4aaafe043e55a264e37b28` |
| Grandchild | `b9adb4f9eaaccc609fe3eccdc838f0ed9a7ec6dd8b4491fea6b13be32c271db9` |

Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` verified eight declarations, including both curvature sign inequalities and the scalar variational estimate. A sign error in the curl symbol and an excessively negative fixed-plane bound both failed compilation as separate mutations. The theorem on the nonlinear Wilson kernel has a written proof. Replay the [host driver](../../transfer-increments/replay-guests.py) and controls from this directory.

```sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof HardVacuum.lean
lake env lean HardVacuum.lean
python check.py
```
