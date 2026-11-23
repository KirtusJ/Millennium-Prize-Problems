# Verification and reproduction

Two fresh deployments of the pinned native PCP OS executed a parent, its child and its grandchild. The parent selected the dyadic lower constant for the capped positive clock. The child enumerated the signed modular flux through all 36 faces of a periodic two-dimensional cross-section with its seam. The grandchild computed a Haar character coefficient from the second and fourth spherical moments. Each guest emitted its portion of the Lean source; the hosted supervisor checked the child output digests and closed the three-node desk. Lean was then run on the assembled source on the host. Both runs produced the same ELF and source. [Guest program](worker.c) · [Generated Lean](TransferClock.lean) · [Supervisor](verify.py) · [Logs and checksums](execution-logs.tar.gz)

| Item | Result |
| --- | --- |
| Lean and Mathlib | Lean 4.19.0, Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b. All 18 declared theorem axiom reports accepted in each release. The reported axioms are within propext, Classical.choice and Quot.sound. |
| Source SHA-256 | e48e509634f43e75950c4bf9ff899e9b73e3a98cd02ec128a07c77d2470feacd |
| Native worker ELF SHA-256 | 98dda7826ba67aa79598915ef6ec6a00c15bb5e210dbc84546bc0c6637ff3fc1 |
| Adverse controls | Both releases rejected an incorrect native callback and four altered Lean conclusions. They changed the cap constant, periodic face count, raw character normalization and Haar coefficient. The archive also preserves the superseded development log with the original failed positivity step. |
| Calibration | All 57 method payloads matched the pinned manifest. The existing fidelity fixture distinguished exact content, changed bytes, truncation, appended bytes, an absent file and a denied read. |

The integrated one-clock inequality and the squared-integral estimate on two separated events quantify over measures and functions. The quadratic root equation, comparison of deficits, modular corner identity, conditional-range arithmetic and character inequalities are supporting Lean results. The walk law, its optimal truncation order, conditional Haar minorization for the Wilson vacuum, uniform spatial-flow locality, square reduction, coefficient asymptotics and weak diagonal are proved in the mathematical notes. End-to-end formalization of those arguments remains open.

| Independent calculation | Observed result |
| --- | --- |
| [Clock distribution](check_clock.py) | Bessel quadrature normalized to one for $n=1,2,4,8$. At each index four Laplace transforms matched both the analytic root and a killed tridiagonal walk. For $n=2$, the two-frequency error certificate times $\sqrt U/n$ went from 0.04482 at $U=16$ to 0.04471 at $U=1024$. The rescaled clipping-tail upper estimates were 0.5533 and 0.5640. |
| [Periodic flux](check_flux.py) | Integer enumeration tested every orientation and every link velocity for even sides 4, 6, 8 and 10. The largest case had 3,000 positive faces and 3,000 stationary spatial links. |
| [Square characters](check_square.py) | At $n=1$ the first four coefficients divided by $q(4)^{2n}$ were approximately $(1.07951,-0.53999,-0.02835,0.04247)$. At $n=32$ they were $(6.00000,-8.00000,8.00000,-8.00000)$ to five decimals. The largest two-grid change among the six index values was below $2.0\times10^{-5}$. |
| [Escape rate](check_escape.py) | Direct quadrature with the original Haar and Bessel measures and Fourier inversion with the $v=3$ tilt agreed within $10^{-12}$ relative for $n=1,2,4$. The uncentered fourth-moment integral divided by its leading asymptotic was 0.83114, 0.94848 and 0.98628 at $n=128,512,2048$. |

The numerical rows are checks at the stated parameters. The asymptotic statements use the analytic arguments. Replay with the [pinned kernel and toolchain](../../clustering/execution.md) in a fresh output directory. The numerical programs use Python, NumPy and SciPy.

```sh
python verify.py --pcp-os "$PCP_OS" --kernel "$KERNEL" --desk "$DESK" \
  --delegate "$DELEGATE" --qemu "$QEMU" --firmware "$FIRMWARE" \
  --lake "$LAKE" --mathlib "$MATHLIB" --out "$FRESH_OUT"
python check_clock.py
python check_flux.py
python check_square.py
python check_escape.py
```
