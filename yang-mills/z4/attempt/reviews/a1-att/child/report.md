# T2 report: MK recursion, d=4, SU(2) vs U(1)

Control (control.txt): `4`. Written from memory before any source was read. Ito–Seiler (below) says "D = 4 becomes the critical dimension" for the r=1 MK formula, which agrees.

## Verdict table
| Item | Verdict | Evidence |
|---|---|---|
| MK, d=4, SU(2): flows to strong coupling (confinement) | STANDS | 10/10 cases (β0 ∈ {0.5,1,2,4,8} × 2 orderings) reach c_{1/2}<1e-8 in ≤32 steps (`result_mk.json`). Ito–Seiler state c_j(n)→0 for unmodified MK at dimension ≤4. |
| MK, d=4, U(1): predicts confinement at all couplings (full character recursion) | NOT CHECKED (only partly supported) | 4 of the 10 U(1) cases flow to strong coupling within 400 steps (A: β0=0.5; B: β0=0.5, 1, 2). The other 6 stall at non-zero c_1 within 400 steps. The tail probe shows A at β0=1 collapses to 0 between n=400 and n=1600. A at β0=4,8 are constant to double precision up to n=6400. A at β0=2 changes by 1.5e-8 over 4800 steps. So the claim "flows to 0 for all β" is not demonstrated numerically. U(1) at weak coupling is marginal/near-fixed in d=4, and any flow is nonperturbatively slow. The claim rests on Ito–Seiler's statement, which is a citation, not my computation. |
| MK cannot distinguish U(1) from SU(2) in d=4 | STANDS (as a statement about the asymptotic prediction) | Ito–Seiler Sec. 4: "MK RG recursion formulae cannot distinguish non-abelian groups from abelian ones". Numerically the speeds differ hugely: SU(2) is done in ≤32 steps, U(1) at weak coupling is practically frozen. This matches their remark that the velocities of convergence are very different. |
| U(1) MK prediction is wrong | STANDS (secondary source only) | Ito–Seiler: "this cannot possibly be correct ... there exists a deconfining transition in 4D lattice gauge theory based on abelian gauge groups". Their Thm 2.2(2): deconfinement for U(1) at β>β0, a variation of Fröhlich–Spencer CMP 83 (1982) 411 and Guth PRD 21 (1980) 2291. I did not read Guth or Fröhlich–Spencer. |
| Consequence: a confinement argument based only on MK-type bounds cannot be valid as stated | STANDS (secondary source) | The same MK flow applies to U(1), which is deconfined at weak coupling, so MK bounds alone cannot imply the area law. Any such proof must use a group-specific ingredient. Ito–Seiler show this for Tomboulis' scheme: for U(1) at large β with r=1 the needed t* does not exist, and for r<1 t* may exist but "does not imply confinement". |
| Lower critical dimension is 4 | STANDS | Ito 1984 abstract (D<4: U(1) uniformly driven to high temperature) plus Ito–Seiler (D=4 critical for r=1). My code in d=3: 5/5 cases strong. In d=5: β0=8 does not flow (c_1→1, weak phase). |

## Sources
| Address | Authors | Title | Year | Locator | How read |
|---|---|---|---|---|---|
| arXiv:0803.3019 | K. R. Ito, E. Seiler | Further discussion of Tomboulis' approach to the confinement problem | 2008 | Sec. 2 after eq. (2.2) and Thm 2.1; Thm 2.2; Remarks 2.1; Sec. 4; refs [6],[7],[11],[12] | FULL TEXT (pdftotext of the PDF; I read the quoted passages, not every page) |
| https://link.springer.com/article/10.1007/BF01468144 | K. R. Ito | Analytic study of the Migdal-Kadanoff recursion formula, Commun. Math. Phys. 95 | 1984 | page meta description | ABSTRACT ONLY |
| web search summary | n/a | n/a | n/a | n/a | SUMMARY ONLY (leads only; not cited as evidence) |
| Migdal JETP 69 (1975) 810; Kadanoff Ann. Phys. 100 (1976) 359; Ito PRL 55 (1985) 558; Guth PRD 21 (1980) 2291; Fröhlich–Spencer CMP 83 (1982) 411 | n/a | n/a | n/a | n/a | NOT READ. They appear only as references in Ito–Seiler, so any claim about their content is second-hand. |

Quotes (≤2 sentences each) are taken from Ito–Seiler, "Sec. 2" and "Sec. 4": "for the (unmodified) Migdal-Kadanoff RG ... {c_j(n)} → 0 ... if the dimension is ≤ 4, whether G is abelian or non-abelian". "this cannot possibly be correct, however, since there exists a deconfining transition in 4D lattice gauge theory based on abelian gauge groups."

## Program and predicates
- `mk_recursion.py` implements two orderings of the MK step (full character coefficients, no truncation). A is bond-moving power then convolution. B is convolution then power, as in Ito–Seiler eq. (2.2). I did not settle which ordering matches Migdal/Kadanoff and Ito's papers, because I did not read them.
- The predicates are fixed in the program docstring.
- **Predicates that passed:**
  - P0 passed (grid c_1 matches the Bessel series to 1e-16; the d=2 control is exact).
  - P1 passed (N=2048 vs N=4096 agree to 6e-16).
  - P3 passed (the d=3 and d=5 controls behave as expected).
- **P2 failed ("for all" over 20 cases): 14/20 qualify.**
  - All 6 failures are U(1): A at β0=1,2,4,8 and B at β0=4,8.
  - This was my partial expectation, not a target defect. I predicted marginality for U(1), but I had not fixed how slow the flow would be, and NMAX=400 was a budget choice.
  - I added a tail probe (`probe_u1_tail.py`, run to n=6400). It shows A at β0=1 does flow eventually and A at β0=4,8 are frozen to double precision. That probe's predicate gave a "fixed point" verdict at β0=1 only because the c_1 value is 0.0 at both n=1600 and n=6400. The label is misleading there and should read "already collapsed".
- P4 gave no pass/fail: for A at β0=8, c_1 stays at 0.9387, so there is no logarithmic running at n≤80.
- The d=2 control showed c_1'=c_1^4 exactly.
- **Tolerances:** 1e-9 and 1e-16 come from double-precision spectral accuracy. 1e-8 is the strong-coupling threshold, because c→c^4 makes the decay super-exponential once c is small. 1e-6 is the drift tolerance, well above the rounding drift. NMAX=400 comes from the budget.

## Delegated sub-agent (grandchild/)
- **Question:** independently recompute the U(1) Villain MK recursion in d=4. Does the coupling run logarithmically to strong coupling?
- **Control:** I_1(1)/I_0(1) = 0.4464. The sub-agent got 0.4464, and I reran its code, which gives 0.44639.
- **Outcome:** it used the truncated recursion β' = refit of [I_1(4β)/I_0(4β)]^4 and found a drift of about 3/8 per step toward weak coupling for β0 ≥ 1. Strong coupling occurs only for β0 below about 0.525. It also found Villain β'=β exactly (marginal).
- **My check:** I reran its `mk.py`, and the output was byte-identical to its `result.txt`. Its first-step c_1 (0.7650 at β0=2) equals my order-A first step.
- **Where they disagree:** its truncation to one coefficient disagrees with my full-character result, which does not drift to weak coupling. The sub-agent flagged this itself as a truncation artefact. I treat its "flows weak" as not a prediction of MK, and its Villain marginality as consistent with my finding of a near-frozen U(1) flow.
- **Open point:** the sub-agent's "exponent b^2 fixed by requiring Villain β'=β" was a consistency choice, not a derivation.

## Not checked
- The content of Guth 1980 and Fröhlich–Spencer 1982, which I did not read.
- Migdal 1975, Kadanoff 1976 and Ito 1985, none of which I read.
- Which ordering (A or B) is the authentic MK, or whether Migdal and Kadanoff differ.
- Whether the U(1) weak-coupling asymptotic flow is truly to 0 (only the Ito–Seiler citation supports it).
- Anything about SU(2) beyond Wilson action, b=2, and 4 ordering/β choices.

## PCP OS
- `init` printed that the method (ACR packet) was not found, as expected.
- Check K1 (`mk_recursion.py`) exit 0 as expected. Check K2 (the `probe_u1_tail.py` wrapper) exit 0 as expected. **Caveat:** K2 pipes the program through `tail` and then runs `ls`, so its exit code is masked. `result_tail.json` already existed, so a fresh `mode='x'` run would have raised. K2 therefore does not certify that the probe ran. The probe's own run, whose output is shown above, is the evidence.
- Last line of `pcp_os.py verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)".
- Last line of `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

## Rerun commands
```
cd /home/user/z4-workers/a1-att/child
python3 -I mk_recursion.py result_mk_NEW.json        # new filename: result files are mode 'x'
python3 -I probe_u1_tail.py                          # fails if result_tail.json exists; rename first
cd <empty dir> && python3 -I /home/user/z4-workers/a1-att/child/grandchild/mk.py   # sub-agent code
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P verify --ws pcp
```
