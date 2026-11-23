# Report
Control: I2(1)/I1(1)=0.240194 (control.txt).
| number | verdict | source line |
|---|---|---|
| a sqrt(sigma) 2.3/2.4/2.5 = 0.3690(30)/0.2660(20)/0.1905(8) (also 2.2, 2.6, 2.7) | FOUND | FHK hep-lat/9208012 Table 3 (compiled from older work) |
| a sqrt(sigma) at 2.2986..2.5115 | FOUND | LTW hep-lat/0307017 Table 1 |
| plaquette at nearby 2.2986, 2.3726, 2.4265, 2.5115 | FOUND (1-<U_p> = 0.39746(1), 0.37661(2), 0.36352(1), 0.34564(1)) | FHK Table 8 |
| plaquette at exactly 2.3, 2.4, 2.5 | NOT FOUND | |
| m_0++/sqrt(sigma) continuum 3.74(12) | FOUND | T98 hep-th/9812187 Table 1 |
| m_0++/sqrt(sigma) at a sqrt(sigma)=0.197,0.228,0.296: 3.67(10),3.62(7),3.49(3) | FOUND (not at fixed beta) | T98 Table 8 |
Full detail in results.md.

Matched pairs (<=5%): (2.3,6)-(2.5,12) +3.25%; (2.3,8)-(2.5,16) +3.25%; (2.4,6)-(2.6,12) +2.26%; (2.4,8)-(2.6,16) +2.26%. Tolerance 5% from task. Hypothesis "every coarse case has a partner" tested per case: 2 of 6 qualify (failure = my expectation, not a target defect; I also had not predicted the 2.4->2.6 match).
Not checked: other plaquette sources at exact beta, Bloch et al., Lucini-Teper-Wenger 0404008, FHK Table 3's underlying primary refs; FHK values are a compilation with possibly differing lattice-size systematics; web search was refused so only arXiv PDFs were used.
Sub-agent: question = independently re-locate a sqrt(sigma) at beta=2.5. Control 0.876282 matched (I reread grandchild/control.txt). Outcome: 0.1905(8), FHK Table 3, same as mine.
PCP: see verify lines below.
PCP python verify last line: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
Rust verify last line: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
Only one program (match) was run through check; the literature lookups were done with curl/pdftotext by hand and are not in the register.
