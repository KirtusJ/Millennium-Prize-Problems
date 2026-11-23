# Verification and numerical controls

Three measured PCP OS guests formed a root, child and grandchild hierarchy. The supervisor admitted each worker and launched the requested child after the parent returned. These deterministic payloads emitted the authored Lean source. A fresh three-guest replay reproduced it. Host Lean 4.19.0 and Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` verified fourteen declarations, each with only `propext`, `Classical.choice` and `Quot.sound`. [Kernel and replay settings](../../smeared-plaquettes/action-curvature/execution.md)

From this directory run

```sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof MomentumTransport.lean --qemu /path/to/qemu-wrapper
OPENBLAS_NUM_THREADS=1 python check_transport.py
```

From the pinned Mathlib checkout run `lake env lean /absolute/path/to/MomentumTransport.lean`. The separate replay returned

```text
w0.elf f8c9d6a7e52e15f602752877bff2355ade5f7061a52a015227c412e7f7509d38 kernel register: 47 events, head 5b347a78a678798bed6abeaa7a5a36c972ecc797b6b87f0851cb026d4479ad61
w1.elf 745ca64aa56b667b10c544b349cbf8c0f1257ccef5065f009e7657db6119d759 kernel register: 47 events, head dd89d39b316ae989f74e3a0ec3e485ececcfd2606f8b7b59a58902abe3ca446a
w2.elf 5ba3f7c9bc62df35c75b6d573d2efdae15500af04d2c9a1160e7ae6e4b582eaa kernel register: 47 events, head b3b45581fa693a7fa2abef87d6a109bc4264dea51f192af7667b77d404fbe948
generated source SHA-256 f4b78e26520b2b2c33c972c8525d9e11e6d98cd5210f565bb4aa122401a446e1
```

Lean checks the shell time derivative and mixed derivative, their finite-sum calculation, the exponential series interchange under an arbitrary positive auxiliary measure, the grid primitive, three momentum coefficients, the two-momentum ambiguity, tensor error, zero-scalar implication, packet algebra and below-threshold bound. The covariant shell disintegration, Gaussian representation, full time-operator iteration, finite remainders and infinite-grid converse are mathematical arguments in the notes. Reversing the mixed derivative sign failed (take $s=u=t=1$). Deleting the final second-moment correction in scalar packet recovery also failed (take the second moment to be one and both other terms zero).

## Controls

One computation forms a positive matrix spectrum with a null shell, massive shells and negative real cross weights. Integrating the Bessel kernel against each measured positive time curve reproduces a direct shell re-evaluation. Fitting the three raw values before transport gives the wrong sign for the cross term. A separate calculation bounds the shifted readings using 80 positive summands and up to 4,800 cells of a finite time grid, supplying simultaneous relative input envelopes of one part in a million for the analytic test curves. Nonnegative remainders and the monotonicity brackets give the analytic enclosure; the printed numerical intervals use floating-point evaluation.

Further tests use the continuous Maxwell spectrum, finite-width smooth annuli, periodic sampling at link and face offsets, and two nearby positive Grams that agree at two momenta. A two-shell control shows that both individual fields can miss a subthreshold signal visible in their sum. These tests use known spectral laws. They do not supply measured covariances of an interacting Wilson continuum.

```text
squared momentum, shifted reading, finite interval 0.9 0.5423087719826236 0.5423082296738516 0.5423093142913955
squared momentum, shifted reading, finite interval 1.4500000000000002 1.307405858669886 1.3030309780596758 1.3118338146300745
squared momentum, shifted reading, finite interval 2.0 2.6246672262906254 2.6088772908182762 2.6406829792516264
tensor, cross, scalar 0.9126682329478958 -0.37684236763444795 0.4813637650368343
uncorrected at the three momenta 0.13977668487162614 0.1659296484144159 0.1304162900906578
Maxwell reconstruction 0.0009882178179061866 3.942553354492743e-18 0.009531541663889817
finite-width packet 0.043149113864633964 -0.017685798348682155 0.023171279178971188
staggered zero-mode residual 1.734723475976807e-17
subthreshold weight detected by the cross term 0.6559561143081757
two-momentum ambiguity at the third 0.06050000000000039
```
