# What was checked

Director C4 generated the declarations with three native PCP OS user processes and checked the assembled source with hosted Lean 4.19.0 and Mathlib c44e0c8e. Two fresh executions produced identical Lean source, worker binaries and desk closures. Each had one additional measured negative-control boot. [Generated source](LocalResponse.lean) · [Worker](worker.c) · [Raw serial, desk and Lean records from both executions](execution-logs.tar.gz)

| Stage | Evidence |
|---|---|
| Parent | Enumerated 16 assignments of four weighted lateral signs. The parity sums were 353 and 272. |
| Child | Computed the exact signed transfer slope 32/91 and emitted the contraction, recurrence and endpoint algebra. |
| Grandchild | Computed center square sums 8 and 6. Enumerated all 512 face subsets on the periodic square grid. Emitted the transfer identities, Wronskian derivative, separation lemmas and the lattice relation. |
| Read-back | Each delegator checked its returned subtree digest after the child exited. Both desks report three finished nodes in a parent, child and grandchild chain. |
| Proof audit | All 17 declarations passed. Axiom reports contain only propext, Classical.choice and Quot.sound. All three proof mutations failed and a guest rejected a three-face request. |
| Artifact digests | Lean source SHA-256 f6c66847107a471593262456ec478e345702bc9fa9cf49f7aff51a2079f6f1c4. Worker ELF SHA-256 62709ecb18ab22f250a573c75335918272fdc48fc681b08b0d52d4af29046606. |

The Lean file proves the local parity average, binary conditional slope and its uniform bound, propagation given its recurrence, rational endpoint covariance, transfer identities, differentiated Wronskian under the specified derivative and ODE hypotheses, the two-row separation lemma, the action of a normalized deck sum on invariant tests, gradient separation, and the complete periodic square-grid face-relation list. The cubical cohomology interpretation, principal orbit geometry, commutant and analytic continuation proofs, OS reconstruction, radial domain, spectral and density arguments are mathematical proofs in the notes. The current Lean certificates cover the specified component identities. The oriented-link enumeration is a separate exact Python calculation. Character-cutoff diagonalization is numerical.

## Replay

Use the [PCP build and kernel instructions](../execution.md), Python 3, GCC and QEMU. Use the shared pinned Lean 4.19.0 Mathlib checkout at c44e0c8ee63ca166450922a373c7409c5d26b00b with its dependencies and compiled imports available. Supply a fresh output directory for each invocation. QEMU runs each worker without networking. The hosted Rust desk launches the next measured guest when the preceding guest requests it. Lean verification runs on the host after all three return.

```sh
python3 replay.py --pcp-os "$pcp_os" --kernel "$kernel" --qemu "$qemu" \
  --firmware "$firmware" --desk "$desk" --delegate "$delegate" \
  --lake "$lake" --mathlib "$mathlib" --out "$fresh_directory"
python3 check.py
python3 check_rotor.py
python3 check_graph.py
```

The two exact checks use the Python standard library. The numerical rotor check uses NumPy and SciPy. The replay validates the pinned PCP source revision, kernel file and load measurement, serial self-tests, node parentage and exit codes, released proof bytes, theorem audit and adverse outcomes. [Replay script](replay.py)
