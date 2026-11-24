# T218 report: shell weights on (Z/2m)^d

Control: sum k^2, k=1..10 = 385 (control.txt).

## Verdicts
- d=3 claim: **STANDS** (w_r = 8r^2+2/3 for r<m, w_m = 4m^2-2m+1/3), m=1..12.
- d=2 claim: **STANDS** (w_r = 4r for r<m, w_m = 2m-1/2), m=1..12.

## Counts (exact Fraction equality, no tolerance)
- Hypothesis check (rule 4): all 156 (d,m,r) cases qualify (1<=r<=m). d=3: 78, d=2: 78.
- P1 (brute vs claim): met 156, failed 0, measured only 0. d=3: 78/78, d=2: 78/78.
- Failed predicate kept: P2 in shell_check.py (sum_r w_r == (n^d-(n-1)^d)/d) failed 22 of 24 (d,m) pairs. **My own wrong expectation**: that quantity is the last-shell value. Total axis-1 weight is ((2m)^d-1)/d by symmetry. Not a defect of the claim.
- P2' (corrected, shell_check2.py): 24/24 met, 0 failed.

## Grandchild
- Task T219 (b2-shell-grandchild, parent T218), admitted and released. Control 56 correct.
- Hand-listed m=1: w_1=7/3; m=2: w_1=26/3, w_2=37/3. All match the claims. I reread result.md and checked it against my results.jsonl: identical.

## PCP OS
- `pcp verify`: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- `pcpos verify pcp/register.jsonl` last line: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
- Checks recorded: K1 shell_check, K2 shell_check2 (both exit 0). Method not pinned (expected).

## Rerun
cd /home/user/z4-workers/b2-shell/child
python3 shell_check.py results_new.jsonl   # P1 156/156; P2 failures are my own expectation error
python3 shell_check2.py p2_new.flag        # P2' 24 ok
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
