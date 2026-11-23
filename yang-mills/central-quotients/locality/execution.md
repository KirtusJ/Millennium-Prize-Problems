# Execution and scope

Two native PCP OS worker hierarchies independently emitted identical Lean source bytes. Each used three fresh network-isolated x86-64 QEMU guests, a hosted Rust recursion desk, and one extra adverse-input guest. Hosted Lean 4.19.0 accepted fourteen declarations with only propext, Classical.choice and Quot.sound in the axiom reports. The operator domains, operator inequalities, two-cut argument, cube derivative, real-time spectral comparison and transfer to limiting correlations are established by the mathematical arguments in this directory. Their full formalization remains open. [Generated Lean](Locality.lean) · [Native worker](worker.c) · [Raw logs](execution-logs.tar.gz)

| Stage | Observed result |
|---|---|
| Method calibration | All 57 Enterprise manifest payloads matched their SHA-256 values. Six new native Core reads produced match, changed byte, truncation, append, absence and permission-denied outcomes as expected. |
| Parent | Built the periodic faces at side five, then measured the doubled squared midpoint displacement for each incident link. Counts at 0, 2 and 4 were 4, 8 and 4, with multiplicity. Requested child with dimension three and face count four. |
| Child | Revalidated the inherited geometry and counted 28 two-step returns to the starting link. Emitted the general weighted path and finite propagation support proofs and requested the grandchild. |
| Grandchild | Revalidated the inherited task and computed the three iterated-integral denominators 6, 120 and 5040. Emitted the Taylor, integral and real-time comparison lemmas. |
| Supervisor | Read and hashed each returning subtree after exit. Both hosted desks closed with the three expected parent IDs and finished states. |
| Adverse controls | The native worker rejected a task with wrong dimension and face count before emitting any mathematical result. Lean rejected a missing corner, a missing two-step return, an even factorial substituted for the odd factorial, and a falsely halved phase cost. The phase counterexample is $r=y=2$. |
| SHA-256 | Source a8a1e98696adc1d462a1c985726c96f710735bdde3c9b89e71aec20debe214d2. Worker ELF 6a98ec42089500ee12eca604e6a470f1c788fd8ec647b67a988131ccabad8e60. |

The source formalizes algebraic cancellation for differentiated conjugation and inverse words, domination by tilted path weights, vanishing below graph distance, two consecutive interval integrals, the uniform finite exponential-series majorant, cancellation of the bare coupling in $b^2\kappa\lambda$, and domination of polynomial growth outside a strict cone. The executable Python checks independently build every link-incidence row for sides 3, 5 and 9, evaluate unrestricted Fourier iterates for two types of probe, differentiate the actual $SU(2)$ cube at gauge-related configurations, and test twelve pairs of finite noncommuting spectral propagators. [Python controls](checks.py)

The PCP OS revision is 92623fa6759bbb4e4f27ce5aa381de213a55ae0c. The kernel SHA-256 is d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f and its load measurement is 0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3. The Enterprise manifest is 3949b2401d0a835cb116c22e44821993cbac59bbd2b281572ebb1b04e8296c18 and Core is 39efd83b4122545455124f20420f212590a06064f391b259e93ea968449e6b7f. Mathlib is c44e0c8ee63ca166450922a373c7409c5d26b00b. [Upstream kernel and calibration instructions](../execution.md)

## Independent replay of the G4 interface

At G4 revision 0f04f57170dbcb2ecd5e74d6fa683618ec0ce133, I recompiled its complex reflection-positivity module and then its integral module against that dependency. The first integral attempt found a missing local Mathlib object. After fetching the pinned dependencies, 33 and 31 declaration reports respectively passed with the same axiom allowlist. The unchanged integral source produced two unused-variable warnings. The three pushforward statements cover equality of reflected integrals, equivalence of integrability, and inheritance of complex nonnegativity when the quotient map commutes with the reflections and the stated measurability and integrability conditions hold. This checks the interface for the inherited measure. The quotient dynamics and real-time propagation require separate arguments. Both compiler outputs are in the archive. [G4 integral source](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/0f04f57170dbcb2ecd5e74d6fa683618ec0ce133/yang-mills/g4/integral/IntegralReflectionPositivity.lean)

## Reproduction

Use the pinned toolchains above, NumPy for the independent controls, and a new output directory for each run. The runner verifies the kernel and toolchain identities, every worker exit, the assembled source and each negative control.

~~~sh
python3 verify.py --pcp-os "$pcp_os" --kernel "$kernel" --qemu "$qemu" \
  --firmware "$firmware" --desk "$desk" --delegate "$delegate" \
  --lake "$lake" --mathlib "$mathlib" --out "$out"
python3 checks.py
~~~
