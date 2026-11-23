"""Predicates (fixed before first run), over pdftotext of arXiv 2610.08144:
P1 text contains 'Navier-Stokes lost in translation'
P2 text contains authors Bastounis, Circelli, Hansen
P3 a heading line starts with '3.2. When a statement and its proof in the NL paper are both mistranslated'
P4 the (8.19) discrepancy ('Example 3.1' and 'm+5' estimate) is located BEFORE heading 3.2 (i.e. not in 3.2)
P5 'exists_uniform_actual_pressure_flux_bound' (pdf renders underscores as spaces) appears after heading 3.2
P6 'norm_derivativeWord_inverse_le' (as spaces) appears before heading 3.2
Tolerance: none; exact substring tests (whitespace-normalised, underscores->spaces) since pdftotext drops underscores.
Exit 0 iff all hold. Failed predicates are printed, not hidden."""
import sys,re
t=open(sys.argv[1],errors='ignore').read().replace('_',' ')
n=re.sub(r'\s+',' ',t)
h=n.find('3.2. When a statement and its proof in the NL paper are both mistranslated')
r={'P1':'Navier-Stokes lost in translation' in n,
'P2':all(a in n for a in('BASTOUNIS','CIRCELLI','HANSEN')) or all(a in n for a in('Bastounis','Circelli','Hansen')),
'P3':h>0,
'P4':0<=n.find('Example 3.1')<h and n.find('Cym+5')<h if h>0 else False,
'P5':n.find('exists uniform actual pressure flux bound',h)>h>0,
'P6':0<=n.find('norm derivativeWord inverse le')<h}
for k,v in r.items():print(k,v)
sys.exit(0 if all(r.values()) else 1)
