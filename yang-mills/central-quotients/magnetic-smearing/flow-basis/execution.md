# Proof scope and numerical checks

Two fresh measured PCP boot hierarchies executed a parent, child and grandchild. The parent computed local complex-clock ODE bounds, the child evaluated the absolute coefficient sum of a five-clock filter, and the grandchild calculated a coefficient of its squared polynomial. The hosted supervisor verified the returned subtree identities and desk closure. Hosted Lean 4.19.0 on Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b accepted 21 declarations in each run. The reported axioms lie within propext, Classical.choice and Quot.sound. Source SHA-256 50b74db70b0a232ba40a3701c8ae50313b6bd4dd2ef4497dc43718dc3319ce96. Native ELF SHA-256 a3fc188d1ff6e6a50b6cc06bf30ae9758b5657642c3aeed6b71e3d85550e3872. [Generated Lean](FlowBasis.lean) · [Native source](worker.c) · [Logs](execution-logs.tar.gz)

The finite-matrix bound quantifies over arbitrary finite index sets. Its sign-vector extremizer is checked symbolically. For the five-clock filter at $a=1,b=4$, expanding $81K_3^2$ gives coefficients $(1,-16,96,-256,256)$ with absolute sum 625. The denominator of the spectral Rayleigh quotient is positive by its integral. Subtracting its equal-time moment from twice its second energy moment and dropping a common positive factor gives nine signed terms $(5r-1)r^2\sqrt r$ with $r=8/(8+3j)$. Lean proves their weighted sum is strictly negative by checking rational bounds on each square root from squared integers. The reduction from the Gaussian integrals to those terms is written; the radical conclusion requires no numerical hypotheses. The Laguerre lower bound, Fejér limit, conditional-density asymptotic, and Wilson analytic continuation are written proofs. Each release rejected an incorrect guest callback and five altered Lean conclusions involving a derivative bound, polynomial coefficient, integral constant, energy-window width and reversed five-clock comparison. All 57 pinned method payloads matched the manifest.

The [integer Gram calculation](check_basis.py) uses exact polynomial coefficients. It encloses inverse half powers using integer square roots of rational squares at increasing precision and certifies both signs and ratios with rational endpoints. Separately it evaluates the nonnegative trigonometric amplitude by quadrature before squaring the norm. On $[1,4]$ the limiting $m\langle E^2\rangle$ is $5/2$. The conditioning column uses numerical fourth roots.

| $m$ | Grid clocks | Nonzero coefficients | $m\langle E^2\rangle$ | $\log_{10}\chi$ |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 5 | 5 | 1.38440972 | 1.14 |
| 4 | 7 | 5 | 1.50180465 | 2.27 |
| 8 | 15 | 13 | 1.75303151 | 7.49 |
| 16 | 31 | 29 | 1.94268005 | 18.86 |
| 32 | 63 | 61 | 2.08428368 | 42.51 |
| 64 | 127 | 125 | 2.19184319 | 90.66 |
| 128 | 255 | 253 | 2.27363170 | 187.82 |

For every row the rational interval width in $m\langle E^2\rangle$ is below $10^{-18}$. At $m=128$ the program proves $m\langle E^2\rangle<8/3$. The [Laguerre calculation](check_laguerre.py) independently integrates the first 13 basis coefficients at four distinct clocks and checks the low-degree trace estimate. The [fixed-momentum computation](check_window.py) integrates the conditional weight and searches the smooth pieces and endpoints. At $k=1,E_0=2$ the computed supremum divided by $\sqrt\delta$ changes from 2.36887 at width 0.05 to 2.495245 at width $10^{-6}$; the analytic limit is 2.495248. This numerical optimization illustrates the analytic upper and lower proof.

Replay in a fresh directory with the [pinned kernel, desk and Mathlib settings](../../clustering/execution.md). Numerical checks use Python, SciPy and NumPy.

```sh
python verify.py --pcp-os "$PCP_OS" --kernel "$KERNEL" --desk "$DESK" \
  --delegate "$DELEGATE" --qemu "$QEMU" --firmware "$FIRMWARE" \
  --lake "$LAKE" --mathlib "$MATHLIB" --out "$FRESH_OUT"
python check_basis.py
python check_laguerre.py
python check_window.py
```
