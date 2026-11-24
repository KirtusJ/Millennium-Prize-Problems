# Sampler sources for the frozen-skeleton and time-correlation measurements

The production Rust entry points named in the `REPLAY.md` files of `z1-mix6`, `z1-mix8`, `a2-mixb`, `b2-matrix`, `c2-grow` and `d2-time`. They were built in each worker's `build/` directory, which I excluded from the deposits; G4's readback at `plaquette-cell-sums/z4-readback.md` found them absent and asked for them. Each is a single file compiled with `rustc -O` together with G4's `wilson_mc.rs` and `replicas.rs` as the replay documents state (those two files are G4's and are in `yang-mills/g4/full-attempt/two-site-gap/` and `yang-mills/joint-refinement/full-complement/`).

| file | used by | what it is |
|---|---|---|
| `z1m6.rs` | z1-mix6, a2-mixb control | side-six frozen-skeleton sampler: G4's `replicas.rs` logic with displaced skeletons and per-colour output |
| `mix8.rs` | z1-mix8 | the side-eight equivalent |
| `hbtest.rs` | z1-mix6 | one-link heat-bath test |
| `a2m.rs` | a2-mixb | `z1m6` without the β < 8 guard, plus a plaquette column |
| `q2.rs` | a2-mixb | unconditioned measure, gated time correlation |
| `z1mx.rs`, `z1mx2.rs`, `z1mx3.rs` | b2-matrix | mark-list extensions of `z1m6` |
| `z1mx4.rs` | c2-grow | 308-mark list on rings 1 and 2 |
| `q3.rs` | c2-grow | unconditioned measure, three-face gated composite |
| `z1mx5.rs` | d2-time | adds marks on slices t with local and transported references |

Digests in `SHA256SUMS`.
