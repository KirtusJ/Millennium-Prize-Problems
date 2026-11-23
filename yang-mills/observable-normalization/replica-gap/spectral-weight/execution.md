# Reproduction and proof scope

Two measured three-generation PCP OS runs emitted identical Lean source. Host Lean 4.19.0 with Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b checked seven declarations, with standard kernel axioms only. They cover the squared difference of the probe and eigenvector derivatives, cancellation at the product eigenvalue, the finite-lag bias difference and its sign, and the three exact Hamiltonian constants. The isolation of the scalar symmetry sector, perturbation of the physical transfer, and the identification of the three intermediate spin sectors are mathematical arguments in the [derivation](README.md). Changing the lag in the bias or the denominator of the Hamiltonian leakage coefficient caused Lean to reject the altered file.

~~~sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof ScalarWeight.lean --qemu /path/to/qemu-wrapper
OPENBLAS_NUM_THREADS=1 python check_weight.py
~~~

Use the [pinned measured kernel, QEMU wrapper and Mathlib instructions](../execution.md). The second sequence produced

~~~text
w0.elf dd8370ebe2d3a338c580969c2bfa5913c4433c7cdf94d2f5ade2fdb8f2e326f3 kernel register: 47 events, head 51ebb8e94e9f0181495309e610617e938ec7013b274a045b0cf0e4fd90bd1800
w1.elf b93875afc08293e08d001c9a4a328850242064e1da58c3e924f63b1668c35e41 kernel register: 47 events, head 01c70a44d31ca255e29e6d34a60d9b2180cc2ef4f00969bc36a737706a504a3b
w2.elf 51a735dafa50c568fa72eda12cbc476d4ea53606400cc1192d2e181e535a729e kernel register: 47 events, head c3934957307c037ec816e7e38ba7ab172453d37f92d15df950a7a95a1f57779b
generated source SHA-256 9bd1ccf3e44fcb9cf5e4146cb1efa1ea9d5707d69615be7364d2df3d299eafe3
~~~

The SU(2) theta graph has two adjacent squares and one neighbor per square. The control independently inserts their sum into the actual split-weight transfer, finds its vacuum and center-subtracts, then projects on the entire numerical eigenbasis. It tests the missing first-state probability and the effective-mass bias at lags zero, one and two. The finite-difference runs use twice-spin cutoff four and the symmetric step sizes 0.012 and 0.006. Both signs are included to remove odd errors, followed by Richardson extrapolation. A separate continuous-time Hamiltonian diagonalization uses 0.06 and 0.03. The cubic evaluation in the last three lines checks the large temporal coupling limit of the exact coefficients. [Numerical control](check_weight.py)

~~~text
gamma 1  predicted [4.210011581e-04 3.968345651e-04 2.277247314e-05 1.313689065e-06]  measured [4.210011581e-04 3.968345650e-04 2.277247314e-05 1.313689065e-06]
gamma 3  predicted [0.018226073 0.012917315 0.003619504 0.001145487]  measured [0.018226073 0.012917315 0.003619504 0.001145487]
gamma 6  predicted [0.1242671   0.06274931  0.027743358 0.014517827]  measured [0.124267099 0.06274931  0.027743358 0.014517827]
theta Hamiltonian mass shift and leakage [0.046428571 0.004795918]  targets [0.046428571 0.004795918]
cubic Wilson leakage/gamma^2 at 100: 0.044861448; Hamiltonian 0.045328798
cubic Wilson leakage/gamma^2 at 1000: 0.045283329; Hamiltonian 0.045328798
cubic Wilson leakage/gamma^2 at 10000: 0.045324264; Hamiltonian 0.045328798
~~~
