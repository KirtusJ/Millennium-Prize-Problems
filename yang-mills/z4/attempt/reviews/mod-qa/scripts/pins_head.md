# Pinned Lean statements (corrected table, QA rerun of 24 November 2026)

Replacement proposed for `yang-mills/z4/infrared/LEAN_PINS.md`, whose last column held the instrument's name
instead of its result. Every row below was re-run with
`/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos instrument mathematics.statement '<JSON>'`
(keys `source`, `theorem`, `pinned`). Binary SHA-256 `d7c33c865d7cf4dea569b6eadaca726455ef4aa997718ab97869259ffc07c388`;
`pcp-os` checkout at `92623fa`. Driver: `scripts/run_pins.py`; full instrument output for every call:
`lean/pins_run1.jsonl`.

What the instrument establishes: the text of the named theorem's statement, comments removed and white space
collapsed, has the pinned SHA-256, and three textual probes are clear (no `sorry`/`admit` before the next
declaration; the conclusion is not true by its form; no hypothesis is `False`). It reads text. It does not run
Lean, and it does not say that the statement means what the paper says.

## Sources

| File | Deposited path (under `yang-mills/z4/attempt/reviews/`) | SHA-256 of the file | Byte-identical to worker copy |
|---|---|---|---|
| `Inheritance.lean` | `f2-lean/Inheritance.lean` | `74e9337dd18a9095754967635c18817780679eed46c3d1e8f8ea5634114ddf2b` | yes (`/home/user/z4-workers/f2-lean/Inheritance.lean`; also `g2-fid/lean/Inheritance.lean`) |
| `haar.lean` | `b2-haar/haar.lean` | `47ff4a24b0fb9dae1d84b6592eb658113c9fd763ae4e7ce2a744586d3d0f2eec` | yes (`/home/user/z4-workers/b2-haar/haar.lean`; also `g2-fid/lean/haar.lean`) |

## Instrument results

| File | Theorem (qualified name) | SHA-256 of the statement (pinned) | Instrument against the pin | Exit | Probes (a) open proof, (b) trivial conclusion, (c) False hypothesis |
|---|---|---|---|---|---|
