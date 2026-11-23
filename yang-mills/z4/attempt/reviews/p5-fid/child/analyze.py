"""T31 analysis. Predicates fixed before first run:
 A1 Overfull hbox: any 'Overfull \\hbox (Xpt too wide)' in build/main.log (2nd run) with X>10 (threshold from brief). Report file via paren-stack file tracking, and source lines.
 A2 undefined refs/cites: log lines matching 'undefined' in final run (main.log).
 A3 multiply defined: 'multiply defined' in main.log, plus independent scan of \\label duplicates in sources.
 A4 bib keys: \\bibitem{k} in refs.tex vs keys in \\cite-family commands (comma split) across all sources (comments stripped).
 A5 counts: hyps used by thm:conditional (\\ref{hyp:*} in the theorem env, sec_reduction) ; proved = 'proved' status in table rows; routes = \\subsection between sec:routes and sec:shared; properties = [P<n>] items in sec:shared; facts = \\item in the enumerate under pf:sec-standard.
 Hypothesis test for 'for all' style: not applicable (no universally quantified predicate); n cases reported.
Result file opened with mode x."""
import re,sys,os
B='build/'; S='paper/'
out=open('result_T31.txt','x')
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
log=open(B+'main.log',errors='replace').read()
# file tracking
stack=[];cur={}
lines=log.split('\n')
fileof={}
for i,l in enumerate(lines):
    for m in re.finditer(r'\((\./[\w./-]+\.tex)|\)',l):
        if m.group(1): stack.append(m.group(1))
        elif stack: stack.pop()
    fileof[i]=stack[-1] if stack else '?'
P('A1 overfull:')
n_over=0
for i,l in enumerate(lines):
    m=re.match(r'Overfull \\hbox \(([\d.]+)pt too wide\) (.*)',l)
    if m:
        w=float(m.group(1)); 
        P(f'  {w:.2f}pt {fileof[i]} {m.group(2)} {"(>10)" if w>10 else "(<=10)"}')
        n_over+= w>10
P('  count >10pt:',n_over)
P('A2 undefined:',[l for l in lines if 'undefined' in l.lower()] or 'none')
P('A3 multiply defined (log):',[l for l in lines if 'multiply' in l.lower()] or 'none')
src={f:open(S+f).read() for f in os.listdir(S) if f.endswith('.tex')}
def strip(t): return re.sub(r'(?<!\\)%.*','',t)
labs={}
for f,t in src.items():
    for i,l in enumerate(strip(t).split('\n'),1):
        for m in re.finditer(r'\\label\{([^}]*)\}',l): labs.setdefault(m.group(1),[]).append((f,i))
P('A3 duplicate labels (sources):',{k:v for k,v in labs.items() if len(v)>1} or 'none')
bib=set(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]*)\}',strip(src['refs.tex'])))
cites={}
for f,t in src.items():
    for i,l in enumerate(strip(t).split('\n'),1):
        for m in re.finditer(r'\\cite\w*(?:\[[^\]]*\])*\{([^}]*)\}',l):
            for k in m.group(1).split(','): cites.setdefault(k.strip(),[]).append((f,i))
P('A4 bibitems:',len(bib),'cited keys:',len(cites))
P('  bibitem never cited:',sorted(bib-set(cites)) or 'none')
P('  cited without bibitem:',{k:cites[k] for k in sorted(set(cites)-bib)} or 'none')
# A5
R=src['sec_reduction.tex'].split('\n')
txt='\n'.join(R)
a=txt.index(r'\begin{theorem}[Theorem S]'); b=txt.index(r'\end{theorem}',a)
used=sorted(set(re.findall(r'hyp:\w+',txt[a:b])))
P('A5a hyps in Theorem S:',used,'theorem at line',txt[:a].count('\n')+1)
for h in used:
    for i,l in enumerate(R,1):
        if r'\label{%s}'%h in l: P('   def',h,'sec_reduction.tex:%d'%i)
for i,l in enumerate(R,1):
    if re.match(r'H\d|H\d \= \(\w\)',l) and '&' in l: P('   status row line %d: %s'%(i,l.strip()))
N=src['sec_negative.tex'].split('\n')
ri=[i for i,l in enumerate(N,1) if 'label{sec:routes}' in l][0]; si=[i for i,l in enumerate(N,1) if 'label{sec:shared}' in l][0]
subs=[(i,l) for i,l in enumerate(N,1) if ri<i<si and l.startswith(r'\subsection')]
P('A5b routes (subsections in sec:routes):',len(subs)); [P('   negative.tex:%d %s'%(i,l)) for i,l in subs]
ci=[i for i,l in enumerate(N,1) if 'label{sec:CE}' in l][0]
props=[(i,l[:40]) for i,l in enumerate(N,1) if si<i<ci and re.match(r'\\item\[P\d\]',l)]
P('A5c properties P-items in sec:shared:',len(props)); [P('   negative.tex:%d %s'%x) for x in props]
Q=src['sec_proof.tex'].split('\n')
pi=[i for i,l in enumerate(Q,1) if 'label{pf:sec-standard}' in l][0]
items=[];on=False
for i,l in enumerate(Q,1):
    if i>pi and r'\begin{enumerate}' in l: on=True;continue
    if on and r'\end{enumerate}' in l: break
    if on and l.startswith(r'\item'): items.append((i,l[:45]))
P('A5d standard facts:',len(items)); [P('   proof.tex:%d %s'%x) for x in items]
P('sections:',sum(len(re.findall(r'\\section\{',strip(t))) for t in src.values()))
