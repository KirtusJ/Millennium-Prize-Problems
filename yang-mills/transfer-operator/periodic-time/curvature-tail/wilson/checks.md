# Checks of the radial law and the shell predictor

The first Python checker integrates the radial likelihood ratio under two independent three-dimensional Gaussian radii. Composite Gauss–Legendre rules at orders 48 and 80 agreed at the tolerance in the source. At $u=0.25$ the mean total variation was $0.07656434$. At $u=10^{-5}$ the ratio $A(u)/u$ was $0.28525946$, compared with $18e^{-3}/\pi=0.28525889$. The integral of the signed density correction was below $3\times10^{-14}$ in absolute value at the tested parameters. [Radial and one-link controls](check.py)

The same checker integrates an original SU(2) Haar link with density proportional to $\exp(2\beta\operatorname{Re}(S^{-1}U))$. With staple angle $b/\sqrt\beta$ and action $y=\beta(1-\operatorname{Re}U)$, its exact marginal density is proportional to
$$
 \sqrt{y(2-y/\beta)}\,e^{-2y\cos(b/\sqrt\beta)}
 \operatorname{sinhc}\!\left(2\sqrt\beta\sin(b/\sqrt\beta)\sqrt{y(2-y/\beta)}\right),
 \quad 0<y<2\beta ,
$$
where $\operatorname{sinhc}(z)=\sinh(z)/z$. It includes the nonlinear compact Haar chart and a noncentral Gaussian limit. The reported TV distances include the Gaussian probability above the compact support.

| $\beta$ | One-link TV at $b=0$ | One-link TV at $b=0.75$ |
|---|---|---|
| 16 | 0.00371597 | 0.00832015 |
| 64 | 0.00090963 | 0.00205917 |
| 256 | 0.00022624 | 0.00051353 |

A second numerical control uses the actual radius-one four-dimensional Wilson conditional integral. It has seven unpinned interior links and 24 faces meeting the origin. Two noncommuting shell links have rescaled log vectors $(1.25,0,0)$ and $(0,1,0)$. The finite Dirichlet solve gives a central Gaussian action mean $0.840115017$ and one-color conditional variance $7/24$. Six digitally scrambled Sobol replicates of 2,048 points each sample the Gaussian link proposal. The density ratio uses the full compact Wilson weight and all seven Haar chart factors. Subtracting the paired Gaussian observation is a control variate. These numerical standard errors measure replicate scatter. The fixed-shell experiment tests the local kernel, independently of the distribution of shell data in the thermodynamic state. [Four-cube control](check_shell.py) · [Underlying group and geometry routines](../../../../z4/attempt/reviews/a8-BL34/child/su2lib.py)

| $\beta$ | Compact mean minus Gaussian prediction | Replicate standard error | Minimum effective sample fraction |
|---|---|---|---|
| 16 | −0.008631 | 0.000639 | 0.9720 |
| 64 | −0.002311 | 0.000237 | 0.9943 |
| 256 | −0.000654 | 0.000107 | 0.9987 |

## Three native PCP OS workers

The parent checked the two-loop trace formula on 2,304 rational quaternion pairs. The child enumerated 81 boundary laws for a finite noncommutative group, checked equality of group and conjugacy-class TV under a uniform orbit kernel, and tested contraction when exterior data were discarded. The grandchild checked angular cancellation and the quadratic radial density coefficient in 625 cases. The host relay admitted each requested successor on a distinct measured boot and compared its output bytes against the expected record. These are deterministic checks of individual steps. [Native source](worker.c) · [Expected output](checks.txt) · [Relay](../../../../observable-normalization/transfer-increments/replay-guests.py)

| Guest | Executable SHA-256 | Kernel register head (47 events) |
|---|---|---|
| Parent | 325e37053b1a6c1e725db06ba21e85f898451271a8ad0f82b675be8dd29d0e0f | 9b66a0c4686954b03b25c761e035ae639cf23019cd3af49e3cbbbca36bcd0ebf |
| Child | def873a581349fce93f96c241aa17324493667e9b525607292d643db24cb01fc | f38dafd3960e5f935d472f5894b648c41730cf3eec5d436ce32322b21c5cee8e |
| Grandchild | a7239ea4ff662289ce46d6dda99675af765552f9445a3c16f8befb1d45a1d500 | a786f405ca0fefa5fdf11539ae9d4c14a60e91982441aa8d30328f8461d085df |

Kernel file SHA-256 was d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f. The generated record SHA-256 was a314d632c399b1e764874755e6968d0f78ed20da1793de89869e677d39b3cfbb. To reproduce from this directory, use NumPy and SciPy for the numerical controls, and the pinned kernel with QEMU for the native programs.
```sh
python check.py
python check_shell.py
python ../../../../observable-normalization/transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof checks.txt
```
