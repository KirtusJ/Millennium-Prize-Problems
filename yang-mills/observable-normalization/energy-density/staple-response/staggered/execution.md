# Replay and independent controls

Two three-level PCP OS deployments generated the same authored source. Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked seven declarations. The reports contain only the standard kernel axioms or subsets of them. The finite-permutation proof moves incident face weights to the envelope, including its periodic seam, and proves the alternating cancellation. The other declarations check the second differences, their factor of two, and the reciprocal remainder after compensation. The Fourier summability, inverse expansion and four-mode argument are analytical. Reversing the sign in the second difference or in the compensated reciprocal identity failed the Lean check.

~~~sh
python ../../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof Staggered.lean --qemu /path/to/qemu-wrapper
python check_stencil.py
~~~

From the pinned Mathlib checkout run `lake env lean /absolute/path/to/Staggered.lean`. [Measured kernel and replay settings](../../../smeared-plaquettes/action-curvature/execution.md)

~~~text
w0.elf 17db8b477fbd043ef843b13eb2c669bc2d3a4d7a259ca7bcde8d48c515f711b8 kernel register: 47 events, head 3c3bb27685a7c8b893ceeaf95c3b6d16154babfe800dc76d04ee0890f227d3fa
w1.elf debc30713376a130696f6202cc937f25779bf06e83c3abdc401b011566ddc70c kernel register: 47 events, head 54b1cbf089df4a1f103481b514b8e1d7b483cec80d4f6480a37ad452a25ae2e0
w2.elf 452d67e34075c15aa3964dac95cbd485c02fa99eefc04ce323fe61ae2fe36941 kernel register: 47 events, head 5a86fbebad2204271a348786b30e08dd52c066098e0cb11776b5707b4b7022d7
generated source SHA-256 a980c6cce7b31628a64a75d500abc07f15c33ad99e9d63a4126b20a333a4fe2a
~~~

The arbitrary face-array control exercises the exact incidence identity with a nonconstant envelope. The full stagger uses an even torus. The inverse check uses independent evaluations of the Abel integral at each pair of trace arguments. The position-space covariance check omits the spatial zero mode of the scalar propagator on each grid. Its temporal electric numerator has vanishing positive-lag limit at that mode. Finite binomial packet sums are evaluated over centered mesh representatives, and convergence is compared on three grid sizes.

~~~text
arbitrary face array: translated-weight residual and constant-weight sum 0.0 3.552713678800501e-15
beta, fixed S, compensated inverse / target 10.0 3.0 1.0379353346610283
beta, fixed S, compensated inverse / target 40.0 3.0 1.009408079353305
beta, fixed S, compensated inverse / target 100.0 3.0 1.0037554569521394
two-leg corner vertex and four-leg absolute pairing sum 1.224646799147353e-16 5.999999999999997
spatial side, sign-summed H11^2/1536, second coordinate moment, binomial ratios 32 2.656874686068547e-06 2.6568746860685485e-06 [0.9844503614778111, 0.996138947738555, 0.9990366978723713, 0.9997592915496395]
spatial side, sign-summed H11^2/1536, second coordinate moment, binomial ratios 64 2.65690163772984e-06 2.656901637729839e-06 [0.9844504984574417, 0.9961389827424597, 0.9990367066699362, 0.9997592937502301]
spatial side, sign-summed H11^2/1536, second coordinate moment, binomial ratios 96 2.6569030793016947e-06 2.6569030793016955e-06 [0.9844505057733377, 0.9961389846116058, 0.999036707139865, 0.9997592938688532]
~~~
