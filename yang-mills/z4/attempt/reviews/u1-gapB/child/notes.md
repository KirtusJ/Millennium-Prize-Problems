# notes
- control: c*=4.605413 (GL, converged n=200..800) written control.txt
- grandchild T178 returned (asinh control ok); released; to be rerun by me in check_gc.py
- control.py re-run under pcp check exited 1 as expected (control.txt already exists, mode x refuses overwrite); not a target defect
- grid.py written with predicates in docstring; running
- grid1 failed exit 1: my own bug (np.bool_ not JSON serializable) in G; fixed; result1.json/result_dbg.json are partial/empty leftovers, kept. rerun as result2.json
- grid2 exit 1: my own bug (repr of np.float64 keys in numpy2 -> KeyError after json write); fixed with float(); result2.json, result3.json kept as leftovers (complete N1/N2 data but crashed at print). rerun result4.json
- grid4 exit 0: N1,N2,N3,G all hold on grid; see result4.json
- report.md written
