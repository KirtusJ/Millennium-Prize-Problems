# Formal scope and reproducible checks

Two three-level PCP deployments generated the identical [Lean source](TangentCurvature.lean). Each native worker booted in a fresh guest with the pinned measured kernel. The hosted Rust desk delegated and closed the parent, child and grandchild in order; the returning supervisors hashed their children's output. Hosted Lean 4.19.0 and Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b accepted all 22 named declarations in each run. The recorded axioms are drawn from propext, Classical.choice and Quot.sound. Native source and logs are included. [Worker](worker.c) · [Evidence archive](execution-logs.tar.gz) · [Enterprise calibration and kernel pins](../clustering/execution.md)

The parent enumerates the cells of a four-dimensional unit cube. The child computes the cubical incidence ranks over the field of two elements by elimination and checks the vertex-edge rank. The grandchild counts Fourier polarizations at an axial momentum. Lean separately computes the incidence ranks from face definitions, proves the integrating-factor solution of the characteristic ODE, checks scalar projection and Green-function identities, proves the nonpositive-square reflection implication and proves iteration of the reflection moment bound. The full compact-group change of variables, infinite-volume probability argument, periodic site-reflection construction and spectral limit are written mathematical proofs. Their end-to-end formalization and independent director review remain open.

Each final run rejects one incorrect native task and five corrupted Lean conclusions (face count, incidence rank, extra polarization, incorrect convolution factor and doubled infrared coefficient). SHA-256 of the Lean source is 95ee640c0e5dc33d0f51b945e4c3007830a63db106359c3ddd3ba6bfc9e58474. The guest ELF hashes to d7d6438f2dee7a024634821376b75eb6f94fa600f25467abc256826e6ed4b381. An early analytic draft had an unavailable derivative lemma and an incomplete ring proof. An earlier native request changed its geometry witness between levels and the hosted supervisor rejected it. The final workers carry an unchanged witness and the negative-control logs retain the compiler diagnostics. The archive also records the source calibration and reread of all 57 manifest payloads.

The independent signed real boundary matrices have ranks 15, 17, 7 and 1, with all successive products zero. Direct $S^3$ Haar quadrature over a conditional Wilson link gives $-0.07781563346649$ on both sides of its six-face variation identity. Flipping the inverse-occurrence score gives $1.21954317060061$. Separate complex Fourier projections are idempotent of rank three. The odd-period reflection quadratic form for an exact binary-link history is 7834.651137886627 by both direct enumeration and the far-seam kernel. Mixed-parity reflected blocks respect the four-copy face bound in all six orientations. A constant color offset of 0.7 gives a negative reflected sine test of $-0.2315020$. [Haar and signed-incidence checks](checks.py) · [Reflection and block checks](check_reflection.py)

Two orders of deterministic momentum quadrature give single-face $C_1(0)=0.5$ and $C_1(1)=0.06887475$. At separation 256 the computed $n^4 C_1(n)$ is 0.10132891, approaching $1/\pi^2$. For the dipole $n^6 C(n)$ is 0.40537133 at the same separation, approaching $4/\pi^2$. The bounded-correlation asymptotic ratios there are 1.000153 and 1.000427 respectively. These checks integrate the limiting covariance. They do not simulate a continuum interacting Yang–Mills field.

For reproduction use the pinned releases in the calibration record and a fresh output directory.

~~~sh
python3 verify.py --pcp-os "$pcp_os" --kernel "$kernel" --qemu "$qemu" \
  --firmware "$firmware" --desk "$desk" --delegate "$delegate" \
  --lake "$lake" --mathlib "$mathlib" --out "$out"
python3 checks.py
python3 check_reflection.py
~~~
