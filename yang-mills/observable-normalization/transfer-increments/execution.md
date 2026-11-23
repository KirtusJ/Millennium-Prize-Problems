# Generation and verification

Three measured PCP OS guests emitted the theorem sources using A4-authored templates. The root requested the spectral-sum child. The child requested the limit worker. The Linux supervisor read back each terminated worker and launched its requested child. A fresh replay compiled the bundled worker, booted each role and compared the assembled bytes against the Lean file. This tests generation and handoff. Independent mathematical review of this revision remains open.

The replay requires GCC, QEMU x86-64 and the kernel image pinned in the parent directory’s execution receipt. Use a standard QEMU installation or pass a wrapper with its support libraries and firmware directory.

```sh
python replay-guests.py /path/to/kernel.elf32 --qemu qemu-system-x86_64
```

The new run under QEMU 10.0.13 printed

```text
w0.elf a139eb3063cbdbcfac641d9d0ae55f10292bb1445188f4149f7df9bffaddb807 kernel register: 47 events, head 8a0231ebfaab50e521c230504d7e2e481be72b9421cf7423ecb41a13b3c34119
w1.elf 5d3cbeded1c2241140cc077c2a2b7db6e8d029cd51cd493fb240935986b2addb kernel register: 47 events, head 17cb18daa6f98c89d88496e9e979d399a7f9f8272022a1ff746982cc57359a60
w2.elf 2e04d919be821110fd937f8c6b3507cb9acba93a3b64d169d49092df426df0b6 kernel register: 47 events, head d9bcd7231c1fb9bf6c013ebad4b95fda83d8b55b5d74c5c94de9118632b02daa
generated source SHA-256 fa08f9027cf5cbd0f1f568559bf30031fc241386e7068c4bf8150f902e30cda8
```

From the Mathlib v4.19.0 checkout at `c44e0c8ee63ca166450922a373c7409c5d26b00b`, `lake env lean /path/to/TransferIncrement.lean` exited zero using Lean 4.19.0 and cached Mathlib objects.

```text
'YangMills.Observable.powerLoss' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.Observable.spectralPowerLoss' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.Observable.positiveTransferLimit' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.Observable.productLoss' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.Observable.tangentMomentBound' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.Observable.sharpMomentBound' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Reversing the sign assumption on spectral weights made Lean reject the modified sum lemma. With one weight −1, transfer eigenvalue 0 and two steps, the modified inequality would read −1 ≤ −2. The unmodified hypotheses exclude this counterexample.

As a separate numerical check on the closed-loop formula, take k=L=N, γ=N², a=h=1/N and evaluate the scaled Bessel ratio with SciPy 1.17.0. For N=8,32,128 the correlations were 0.2205210182, 0.2229667548 and 0.2231199461. The analytic limit is exp(−3/2) ≈ 0.2231301601. This check evaluates the spectral prediction and does not independently simulate a gauge field.
