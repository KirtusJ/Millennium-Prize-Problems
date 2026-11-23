# r7-wild child report

- Control: -ln(tanh(1)) = 0.272341 (matches known answer; control.txt)
- Register: `pcp/` created via pcp_os init (method not pinned / ACR absent note, as expected)

## Lean (KBound.lean, theorem KB_bound)
Run from C:/Users/donke/z4-lean: `PATH=$HOME/.elan/bin:$PATH lake env lean .../child/KBound.lean`
- Exit code: 0 (direct run, ~2.5 min; pcp_os check K1: exit 0 expected 0, 73947 ms, output 4a0cf450e5eb)
- No sorry. Axioms output verbatim:
  `'KB_bound' depends on axioms: [propext, Classical.choice, Quot.sound]`
- Proof: s = sqrt g, s*s = g; case g <= 16 (s <= 4): K <= 4, so <= 4(1+B) <= 38.75;
  case g >= 16 (s >= 4): K <= 8B/g, reduce to 8B(1+B) <= 43 s^2 via nlinarith with B <= 17s/8+3/16.
- Failed drafts: none (first draft passed; no KBound_draftN.lean files).

## Grid (kgrid.py, logspace 1e-6..1e8, 200001 points)
- `max K*(1+B) = 41.6096831615 at g = 18.80745364`
- pcp_os check K2: exit 0 expected 0, output 5aa48fd57f47

## Verify
Last line of `pcp_os.py verify --ws pcp`:
`result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
(register: 4 events, chain intact, head 6056e2a703ac...)
