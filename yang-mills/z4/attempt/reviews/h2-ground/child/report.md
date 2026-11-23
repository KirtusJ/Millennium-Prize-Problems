# T96 report: published spectrum of -(1/2)Lap + c|Y1xY2|^2 on SO(3)-invariants (Q3)

**Verdict: NOT FOUND** (limited search, see below). Control: control.txt = 0.036635 (-ln tanh 2).

## Sources table
| Address | Authors | Title | Year | Locator | How read |
|---|---|---|---|---|---|
| (none qualifying) | | | | | |
| INSPIRE listing only (not read): Koller & van Baal series, e.g. "Analytic Results in Intermediate Volumes for Pure SU(2) Gauge Theory" (1988), NPB302 "A Nonperturbative Analysis in Finite Volume Gauge Theory" (1988) | Koller, van Baal | as listed | 1986-88 | title only | **titles only (INSPIRE metadata); full text NOT read.** They treat 3+1 (three torus directions, 9 constant-mode variables), a different operator, so not a match for the 2-direction problem even if read. |

No full text, abstract or secondary quotation of any number was obtained, so no "theirs" values exist.

## Ours vs theirs vs difference
Theirs: none. Ours: e_0 = 3.3505330 (claimed); independently recomputed by grandchild T97: 3.35053305 (difference 5.5e-8, within stated tol 2.3e-6; honest error ~1e-7). e_1 not checked.
Conversion recipe (if a source is found): H_g = -(1/2)Lap + g|Y1xY2|^2. Put Y = sY'. Lap -> s^-2 Lap', potential -> g s^4 |Y'1xY'2|^2. Choose s with s^-2 = g s^4 => s = g^(-1/6); then H_g = g^(1/3) [-(1/2)Lap' + |..|^2]. So E(g) = g^(1/3) E(1), and E(2) = 2^(1/3) E(1); to convert a g-spectrum to ours multiply by (2/g)^(1/3). Also note a convention change -(1/2)Lap vs -Lap multiplies by a factor too.

## Grandchild (T97, admitted then released)
Question: independent Rayleigh-Ritz estimate of e_0 in invariant variables (a=|Y1|^2, b=|Y2|^2, c=Y1.Y2 polynomials times Gaussian, exact Gamma-function matrices). Its own control: grandchild/control.txt = 0.004958 (-ln tanh 3, I reread: correct). Outcome: E=3.35053305 at N=22 (dim 1222, 600 kept after 1e-12 conditioning cut), monotone convergence, harmonic-oscillator test 3.0000000000. I reread rr.py docstring (predicate stated before run) and reran it (check K2, results_rerun.txt, identical output). Caveat: basis restricted to even k (checked equal to all-k at N=6 only); Rayleigh-Ritz upper bound, ill-conditioning drops modes at N>=12.

## Failed predicates
None failed. (search.py predicate P1 was false = no candidate; that is a result, not a failure. Earlier ad hoc arXiv API queries and several INSPIRE queries returned empty output; I attribute this to my query syntax or API/rate behaviour, not verified, and did not retry at length.)

## What I did not check
Full text of any Koller-van Baal paper, Luscher's "Some analytic results concerning the mass spectrum of Yang-Mills gauge theories on a torus" (NPB219, 1983, from memory only, not fetched), B. Simon's 1983 x^2y^2 paper, Savvidy; any 2+1-specific literature (e.g. Weisz-Ziemann, Bruckmann et al.); e_1 and the O(2) doublet; arXiv full-text search; sciencedirect/projecteuclid/doi pages. Search budget was small (~8 INSPIRE title queries in search.py plus ~10 ad hoc), so NOT FOUND means "not found in this search", not "does not exist".

## Searches (endpoints)
- export.arxiv.org API: 5+ queries (Yang-Mills torus small volume SU(2); x^2y^2 matrix QM; Koller van Baal torus; Luscher small volume; constant modes 2+1) -> empty responses.
- inspirehep.net API: search.py's 8 queries (see search_out.txt) plus ad hoc: author Koller/van Baal (found 3+1 series), others with 0 hits.

## Rerun
cd /home/user/z4-workers/h2-ground/child
python3 -I search.py search_out2.txt          # needs network (inspirehep only)
cd grandchild && RESULTS=results3.txt python3 -I rr.py   # ~95 s
PCP: P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P verify --ws pcp

## PCP verify last lines
- Python `verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- Rust `pcpos verify pcp/register.jsonl` last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
