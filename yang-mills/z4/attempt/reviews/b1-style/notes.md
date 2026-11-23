# notes b1-style
- step0: control.txt = 0.272341
- step1: register pcp init; child admitted as T3 (parent T2); child/PROMPT.txt written (item 3 only, control: number of alternatives = four)
- step2: fetched PDF to /tmp/b1-style-dl/ns.pdf (HTTP 200, 2959204 bytes); pdftotext -layout
- step3: PDF read: front matter, intro (pp1-3), refs, last page. PDF contains 0 occurrences of 'Lean', 'AI', 'Acknowledg', 'GPT', 'github', 'axiom'. Single author line 'OPENAI'. Abstract = 1 sentence.
- step4: github.com (page + api) returns 403 from proxy 'access not enabled for this session'; web-fetch agent also 403. Repo README NOT READ. openai.com blog not in allowed network -> not fetched. Web search snippets only (secondhand): blog openai.com/index/navier-stokes-solution, news (TNW, ScienceNews, NYU Shanghai RITS) on forcing question & credit dispute & 'will not claim prize'.
- step5: style_audit.py run1 via pcp check K2 (expect-exit 1 because grep had already shown no 'Lean'/AI in PDF before the run; disclosed). Results in result_style_audit_run1.txt
- step6: v2 run K3: met 7 failed 2 (P5 Lean, P6 AI statement). P9 failure in v1 was MY regex defect.
- step7: child control graded 'four' = correct. Child report reread; reran myself: fetched arXiv:2610.08144 (sha 3282e2c4..., 25pp). Confirmed title/authors; §3.2 = Example 3.3 on (10.19) pressure-flux bound vs Lean PressureFlux.lean @f9e8bc5; m+4 vs m+5 for (8.19) is §3.1/Example 3.1 (brief's locator partly wrong). Both (8.19) and (10.19) appear verbatim-in-form in our copy of the PDF. Lean side NOT checked (github 403). T3 released; T4 admitted+released by child (graph).
- step8: report.md written (STANDS 10, DEFECT 2, NOT CHECKED 3); registers verified PASS.
