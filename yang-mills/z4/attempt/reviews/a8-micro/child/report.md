# Report
Control: 1/(3.74*0.3690) = 0.725 (control.txt).

| k | q | xi | P |
|---|---|----|---|
| 1 | 0.270 | 0.725 | 0.529 |
| 2 | 0.323 | 1.005 | 0.681 |
| 3 | 0.385 | 1.404 | 0.863 |

Exponents: pair(1,2)=0.77, pair(2,3)=0.71, pair(1,3)=0.74; log-log LSQ p=0.74 (C=0.674).

Predicates (defined in calc.py docstring before first run):
- P1 q in (0,1) for all k: MET (3/3 qualify)
- P2 xi increasing as s decreases: MET
- P3 xi_1 = 0.725 matches control (tol 5e-4, rounding): MET
- P4 all exponents positive: MET (measured)
- P5 LSQ exponent within pairwise range: MET (measured)
Failed predicates: none. Note: P in log-log is only approximately a power law (pairwise exponents differ 0.71-0.77).

Grandchild (grandchild/): control 1.012/3.751 = 0.270 (correct). Its q: 0.270, 0.323, 0.385; xi: 0.725, 1.005, 1.404 - agree with mine. I reread its calc.py/result.txt and reran it in rerun/ (output identical, check K2).

PCP: init reported method (ACR packet) not found, as expected. 
- `$P verify --ws pcp` last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl` last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

Rerun:
    cd /home/user/z4-workers/a8-micro/child
    P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
    mkdir t && cp calc.py t/ && (cd t && python3 calc.py)     # result.txt is write-once ("x")
    mkdir g && cp grandchild/calc.py g/ && (cd g && python3 calc.py)
    $P verify --ws pcp; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
