# T177 report: grid check of N1, N2, N3

Control: c* = 4.605413 (control.txt; Gauss-Legendre after a sqrt-singularity substitution; n=200, 400 and 800 agree to 1e-13).

## Verdicts (all on a grid; this is not a proof)
Tolerance is 1e-12, float64 roundoff. A predicate fails if slack < -1e-12.

| | verdict | met, failed, measured only | worst point |
|---|---|---|---|
| N1 | HOLDS ON GRID | cases (eta,S): 10200 met, 0 failed. About 2.9e8 (x,y,a,b) points. 85 etas x 120 S. | min slack 3.75e-5 at eta=1e-4, S=s_lo, x=0, y=0, b=0, a=exp(-3eta/4). F=a and the slack is (1-a)/2. It shrinks toward 0 as eta->0 but stays positive. |
| N2 | HOLDS ON GRID | cases: 10200 met, 0 failed. Same grid. | min slack 5.62e-5 at eta=1e-4, S=s_lo, x=0, a=amax, b=1, y=m/2 |
| N3 | HOLDS ON GRID | 4005 etas in [1e-6, 0.4]: 4005 met, 0 failed | min slack Mc2-MA2 = 5.9866 at eta=0.4 |

Grid details:
- a, b and y were sampled at the corners, with 2001 x-points. F is linear or bilinear in a, b and y, and concave in x.
- A 5^3 interior lattice of (a,b,y) with 101 x-points found nothing worse than the corners.
- Measured only (not pass/fail): the N1 slacks, the N3 table, and the N2 slacks at the four named etas.

N1 minimum slack (1-m)-F:
- eta=0.4: 7.5269e-3
- eta=0.1: 2.3872e-3
- eta=0.01: 3.7360e-3
- eta=0.001: 3.7486e-4

N2 min slack at the same etas, for reference:
- eta=0.4: 0.2401
- eta=0.1: 0.05602
- eta=0.01: 5.590e-3
- eta=0.001: 5.621e-4

N3 values:

| eta | Mc2 | eta*Mc2 | MA2 | eta*MA2 |
|---|---|---|---|---|
| 0.4 | 18.0473 | 7.2189 | 12.0607 | 4.8243 |
| 0.2 | 30.3824 | 6.0765 | 20.5522 | 4.1104 |
| 0.1 | 54.3589 | 5.4359 | 37.9149 | 3.7915 |
| 0.05 | 101.6153 | 5.0808 | 72.8236 | 3.6412 |
| 0.01 | 475.7219 | 4.7572 | 352.5224 | 3.5252 |

## Failed predicates and runs (kept in notes.md)
- `control.py` re-run under `pcp check` exited 1. This was my expectation: control.txt already existed and mode "x" refuses to overwrite. It is not a target defect.
- `grid1` exited 1 because of a bug in my program: np.bool_ is not JSON-serialisable.
- `grid2` exited 1 because of a bug in my program: numpy 2 repr() of np.float64 gave wrong dict keys, a KeyError after the JSON was written.
- result1.json, result2.json, result3.json and result_dbg.json are leftovers from those runs. result4.json is the clean run (`grid4`, exit 0).
- No inequality failed at any point. The reported results are from result4.json only.

## Grandchild
- Task id: T178 (admitted with --parent T177, released after it returned).
- Question: independently recompute MA2 and Mc2 at eta=0.4 and 0.01, and P(s_lo)+exp(-1/16) at eta=0.01.
- Control: asinh(1)=0.881374, matched.
- Outcome: MA2(0.4)=12.060726371361, Mc2(0.4)=18.047286402488, MA2(0.01)=352.522415570200, Mc2(0.01)=475.721934138243. P(s_lo)=0.030043569 and P+exp(-1/16)=0.969456631752 (below 1).
- I reran all of these in grid.py (predicate G). All match to relative 1e-9.
- Its files are in grandchild/.

## PCP OS
- `init`: the method was not found, as expected.
- Checks: K1 control (exit 1, expected), K2 grid1 (exit 1, expected 0, my bug), K3 grid2 (exit 1, expected 0, my bug), K4 grid4 (exit 0).
- `pcp_os.py verify` last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify` last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

## Rerun
Result files refuse to be overwritten, so use new names:
```
cd /home/user/z4-workers/u1-gapB/child
python3 grid.py result_new.json
python3 grandchild/calc.py   # may need a new output name (mode x)
```
Under the register:
```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name grid_re --expect-exit 0 -- python3 grid.py result_re.json
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
