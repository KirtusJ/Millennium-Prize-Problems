# Results (numbers only; SU(2), Wilson action)
Sources: FHK = Fingberg, Heller, Karsch, "Scaling and Asymptotic Scaling in the SU(2) Gauge Theory", https://arxiv.org/abs/hep-lat/9208012
LTW = Lucini, Teper, Wenger, "The high temperature phase transition in SU(N) gauge theories", https://arxiv.org/abs/hep-lat/0307017
T98 = Teper, "Glueball masses and other physical properties of SU(N) gauge theories in D=3+1: a review of lattice results for theorists", https://arxiv.org/abs/hep-th/9812187

| quantity | beta | value | source / location |
|---|---|---|---|
| a sqrt(sigma) | 2.2 | 0.4690(100) | FHK Table 3 (compilation of refs 5,6,21-23) |
| a sqrt(sigma) | 2.3 | 0.3690(30) | FHK Table 3 |
| a sqrt(sigma) | 2.4 | 0.2660(20) | FHK Table 3 |
| a sqrt(sigma) | 2.5 | 0.1905(8) | FHK Table 3 |
| a sqrt(sigma) | 2.6 | 0.1360(40) | FHK Table 3 |
| a sqrt(sigma) | 2.7 | 0.1015(10) | FHK Table 3 |
| a sqrt(sigma) | 2.2986 | 0.3667(18) | LTW Table 1 (L=10) |
| a sqrt(sigma) | 2.3726 | 0.2879(10) | LTW Table 1 |
| a sqrt(sigma) | 2.4265 | 0.2388(9) | LTW Table 1 |
| a sqrt(sigma) | 2.5115 | 0.17680(76) | LTW Table 1 |
| 1-<U_p> (plaquette = 1 - this) | 2.2986 | 0.39746(1) | FHK Table 8 |
| 1-<U_p> | 2.3726 | 0.37661(2) | FHK Table 8 |
| 1-<U_p> | 2.4265 | 0.36352(1) | FHK Table 8 |
| 1-<U_p> | 2.5115 | 0.34564(1) | FHK Table 8 |
| plaquette at exactly 2.3, 2.4, 2.5 | | NOT FOUND (nearby betas only, above) | |
| m_0++/sqrt(sigma), continuum | - | 3.74(12) | T98 Table 1 |
| m_0++/sqrt(sigma) | a sqrt(sigma)=0.197(8) / 0.228(7) / 0.296(15) | 3.67(10) / 3.62(7) / 3.49(3) | T98 Table 8 |
| m_0++ at beta=2.3,2.4,2.5 | | NOT FOUND directly (Table 8 is indexed by a sqrt(sigma)) | |

U_p in FHK is (1/N) Tr of plaquette, i.e. (1/2)Tr U_p for SU(2).
Size matching (match.py, match_out.txt; l sqrt(sigma)=N a sqrt(sigma), FHK Table 3), N_f=2N_c, |mismatch|<=5%:
(2.3,6)-(2.5,12) +3.25% ; (2.3,8)-(2.5,16) +3.25% ; (2.4,6)-(2.6,12) +2.26% ; (2.4,8)-(2.6,16) +2.26%. (error on ratio ~0.9% and ~3.1%.)
No other pair among 2.2-2.7 qualifies (4 of 72). N_c=12 has no partner (N_f=24 not requested).
