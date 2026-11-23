# Execution receipt

A4 executed the Enterprise method check. The native release binary matched SHA-256 `dd68d895f11fa419f5508377106d18a2beeda0676c6441c017d987b5b8aaf93a`. The method manifest was `3949b2401d0a835cb116c22e44821993cbac59bbd2b281572ebb1b04e8296c18`, with all 57 listed files present and equal. The Fidelity Audit Lab supplied separate governing Core and Mathematics reference texts.

Three sequential x86-64 PCP OS boots under QEMU 10.0.13 emitted the Lean source. The root requested the bounds worker, which requested the positivity worker. The host launched each requested guest after reading its predecessor’s serial and gathered their output after exit. The workers emitted A4-authored templates. This is a supervised logical hierarchy, with source generation inside the guests and Lean checking on the Linux host. The three workers do not provide independent mathematical reviews.

Kernel file SHA-256 `e1b3d972eea2e7825fee09bf8f792e06260f132144ca97d1cf2d81bfa645c414`, measured text and rodata `e90d5278060aaae6bef083d6e45d7b182206db7ac8fe6402b7e16b667c886dc6`. The reused kernel came with a build receipt identifying source revision `a521c39005db64f516b24ff661478943f75f9955`. A4 verified the image digest and ran the kernel.

| Guest | ELF SHA-256 | Kernel register head |
|---|---|---|
| 0 | `6195b492409365f2bda273c6013d10e49a0fcdf34a05a7f31879b0878d14c8b0` | `d9dc565cf310643b670d3479128c85ad94a5f0e7cd31caf321cf6050366b29e6` |
| 1 | `04989e9955edbc77915e1ad396b77439cd6f15e490703f72bd68986f42decebf` | `aee181521301093ee2404fbe75cb99cb3f829ecb9157b6aed3609d3ecc9af2bd` |
| 2 | `e153cd8d5a0434635e15af325bc6b2c6c7c89203babf5d1d27e7cb74e8bc5cca` | `ced2c7c008a5267fa17ebf315d7fdce1d1baa93723f279e405478551bc143fdb` |

Each kernel reported exit zero for its worker and passed its self-tests. An earlier ELF with an empty load segment was rejected by the guest loader. Only the successful fresh boots contributed source.

Rebuild each guest ELF with GCC and the included linker script, replacing N with 0, 1, or 2.

```sh
gcc -Os -ffreestanding -mcmodel=large -fno-pie -nostdlib -static -Wl,--build-id=none,-T,link.ld -DROLE=N worker.c -o wN.elf
```

For each role, boot the measured kernel with that ELF as the multiboot module, the module basename as its program name and kernel arguments `auto=wN.elf image=<measurement> then=off`. Match the admitted ELF digest, child request and successful exit before collecting the payload of each serial line beginning with `A4 LEAN `. Concatenate in role order. The resulting file SHA-256 is `17695d996f978b2c13ed1ac6e3cc98498fb5e58eacbd0dda573e83fc893609fd`.

Lean 4.19.0 at `6caaee842e94` and Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked the source with `lake env lean /path/to/SeparatedTime.lean` from the pinned Mathlib checkout. Compiled dependencies came from Mathlib’s cache. Lean exited zero.

```text
'YangMills.Observable.separatedTimeWitness' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.Observable.momentLowerBound' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Adverse check: changing the strict lower-bound premise to nonnegative made the proof fail at the strict-positivity step. The constant zero correlator with both bounds zero satisfies the weakened assumptions and refutes its conclusion.
