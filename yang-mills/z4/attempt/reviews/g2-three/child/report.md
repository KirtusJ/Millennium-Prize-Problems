# T83 report (Yang-Mills SU(2) three-link, Q1/Q2)

| Item | Verdict | Evidence |
|---|---|---|
| Control I_2(2)/I_1(2) | done | 0.433127 (control.txt) |
| Q1 k_j/k_0 = I_{2j+1}/I_1 | PASS | k_j=(2/beta)I_{2j+1}(beta) from e^{beta cos a}=sum I_n e^{ina} and chi_j=sin((2j+1)a)/sin a; 400-pt Gauss-Legendre agrees with Bessel to <=6e-17 at j=1/2,1 |
| Q2 sampler | PASS | <chi_1>=0.00041±0.00050, <chi_1^2>=1.00041 |
| Q2 bounds S2-S4 | PASS | 0<Z(2)<Z(1)<1, |X|<=9Z, finite |
| Delegated Z(1) | AGREES | 0.176840±0.000126 (Euler angles) vs 0.176791±0.000089 (quaternions); diff 0.00005 < 1 combined SE (0.00015) |

## Numbers
Q1 (beta=2): k_0=1.590636854637; k_{1/2}/k_0=0.43312742672; k_1/k_0=0.13374514656; **-ln(k_1/k_0)=2.0118191813** (also equals -ln(I_3(2)/I_1(2))).

Q2 (N=4e6, seed 2024, explicit 2x2 complex matrices, same samples for both beta; SE = sample std/sqrt(N)):
- beta=1: Z = 0.176791 ± 0.000089, X = 0.014744 ± 0.000232
- beta=2: Z = 0.062870 ± 0.000061, X = 0.019672 ± 0.000160

## Failed predicates
- My own: none failed (q1.py, q2.py all PASS). Caveat: the S1 chi_1^2 tolerance used a loose, hand-set bound (4*sqrt(8/N)), not a sample-derived SE.
- Grandchild (T84) failures, all errors in its own expectations, not target defects: P0 (it expected 0.565159, which is I_1(1) alone; correct ratio 0.446390 = 0.565159/1.266066); P2 for beta=0.01 and 0.001 (expected Z within 4 SE of 1; Z≈1-2.25 beta since E[(1/2)ReTr commutator]=1/4 gives <S>=2.25; observed 0.977807, 0.997753 match this). X->0 holds (X=-0.00054±0.00070, 0.00018±0.00071).

## Not checked
Beta dependence beyond beta=1,2; any exact value of Z or X (no analytic/character-expansion cross-check of Z, X); X statistical independence across beta (same samples, correlated); bias of ratio estimators (none formed); the quaternion sampler is checked only through low moments of chi_1.

## Delegation
Task T84 (g2-three-grandchild, parent T83), admitted then released (event 165). Grandchild in grandchild/ ; control I_1(1)/I_0(1)=0.446390. I reread results.md and reran run.py in a clean copy (gc_rerun/): output byte-identical.

## PCP OS
Register pcp: checks K1 (q1) and K2 (q2) exit 0 as expected (K for grandchild rerun not run through check).
- `pcp_os.py verify --ws pcp` last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl` last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

## Rerun (from this directory; result files open with mode "x", so delete q1_result.txt/q2_result.txt first)
    export OMP_NUM_THREADS=1
    python3 q1.py ; python3 q2.py          # ~11 s
    cd grandchild && rm control.txt results.md && python3 run.py
