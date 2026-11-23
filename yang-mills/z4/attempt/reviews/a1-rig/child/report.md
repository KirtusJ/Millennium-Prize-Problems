# Report (child literature reader)
Control: control.txt = "three" (answer from memory; consistent with the INSPIRE-relayed title "Three-Dimensional U(1)"; no full text read).
Caveat: no WebFetch tool here; all web reads went through web-fetch sub-agents, so "read" = relayed by an agent, never my own eyes. No full text of any paper was read by me.

## (a) 4D compact U(1), weak coupling
| address | authors | title | year | locator | how read | statement | hypotheses | NOT given |
|---|---|---|---|---|---|---|---|---|
| 10.1103/PhysRevD.21.2291 | Guth | Existence proof of a nonconfining phase in 4D U(1) LGT | 1980 | INSPIRE abstract | ABSTRACT ONLY | "A rigorous lower bound is obtained for the Wilson loop expectation value" | exact beta range, volume: unread | whether perimeter law, massless photon: unverified (memory: lower bound = non-confinement) |
| 10.1007/BF01213610 | Fröhlich, Spencer | Massless phases and symmetry restoration in abelian gauge theories and spin systems | 1982 | INSPIRE abstract | ABSTRACT ONLY | "We give a new, elementary proof for the existence of a deconfining transition to a massless (QED) phase" | unread; power-law decay of which correlation: FROM MEMORY only | exact decay exponents, beta range |
The requested exact statements (perimeter law, massless photon, which correlation decays as a power) are NOT established by what I read.

## (b) 3D U(1)
| 10.1007/BF01961240 | Göpfert, Mack | Proof of confinement of static quarks in 3-dim U(1) LGT for all values of the coupling constant | 1981 per INSPIRE (CMP 82) | INSPIRE abstract | ABSTRACT ONLY | "We show that its string tension α is nonzero for all values of the coupling constant g2" | 3D, U(1), all couplings | size of tension / gap vs beta: abstract mentions a bound, not relayed; NOT known to me. Mass gap statement not read. |

## (c) finite groups, 4D
| arXiv:2202.10375 | Adhikari, Cao | Correlation decay for finite lattice gauge theories at weak coupling | 2022 (v3 2024, AOP) | abs page; Thm 1.1, Sec 1.3, Rem 1.2 | SUMMARY ONLY (agent read arxiv html v3; PDF unreadable) | beta ≥ (1/Δ_G)(114+4 log|G|); covariance of conjugacy-invariant functions of holonomies in rectangles B1,B2 at ℓ∞ distance ≥ L is ≤ 4(4·10^24|G|²)^(|B1|+|B2|)‖f1‖‖f2‖ e^{-(β/2)Δ_G(L-1)} | finite G (nonabelian allowed), boxes in Z^4, Δ_G from a unitary rep character | no infinite volume statement verified; no confinement/deconfinement conclusion; theorem constants not rechecked by me |
Note: an earlier sub-agent summary said no numeric beta threshold; the later agent's verbatim-theorem read contradicts it. Unresolved by me; I report the later one with SUMMARY ONLY status.

## (d) 2D
| arXiv:2006.16229 | Chatterjee | A probabilistic mechanism for quark confinement | 2021 | abs page | ABSTRACT ONLY | unbroken center symmetry ⇒ confinement; sufficient: nontrivial center + exponential decay under arbitrary b.c. | lattice | not a 2D result |
| Lévy (Mem. AMS 2003); Driver (CMP 1989); Sengupta | | | | none | FROM MEMORY | 2D YM exactly solvable, continuum measure exists on surfaces, area law | | nothing verified |

## (e) SU(2) d=4,5
Nothing read. FROM MEMORY: no rigorous result on a 4D SU(2) phase transition or its absence (only strong-coupling confinement, Osterwalder–Seiler); 5D unknown to me. Not searched.

## Delegation
Grandchild (grandchild/): control "2022" correct; asked for AC abstract: returned ABSTRACT ONLY, "no numeric beta range, dimension not stated, exponential decay". Reran with a separate agent: Theorem 1.1 with explicit threshold found in html. Disagreement noted above; the grandchild's "no numeric beta" was a limit of its abstract-only reading.

## Programs / predicates
tools/check_table.py (P1-P5 in docstring). Run 1 on results.json: 7 rows complete, 0 fails — but that table was too optimistic (rows were FROM MEMORY with placeholders). Run 2 on results2.json: 7/7, 0 fails. Note: I edited the script in place (filename results.json→results2.json) between runs, so run 1 is not byte-reproducible with the final script. The predicate checks only completeness, not truth. No failed predicates occurred; P4 qualifying rows 7/7, of which only 4 have any source read (abstract/summary).
## Not checked
Full texts of all; Guth/FS perimeter-law and decay details; Göpfert–Mack string tension bound; item (d) and (e) beyond Chatterjee; Springer/APS pages blocked (403/login).
## PCP verify last lines
- pcp_os verify: "A pass is a fact about these bytes... result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- pcpos verify: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
