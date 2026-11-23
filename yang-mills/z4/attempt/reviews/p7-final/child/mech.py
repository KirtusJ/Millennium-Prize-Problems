"""Mechanics. Predicates fixed before run:
P1: LaTeX errors (lines starting '!') in final log == 0
P2: undefined refs/citations in final log == 0
P3: no overfull \\hbox > 15pt (15pt from brief)
P4: 'Theorem 1.1' in page 1 text of new PDF
Result file mech.json opened with 'x'."""
import subprocess,shutil,re,json,os
shutil.copytree("paper","build")
for i in range(3):
    subprocess.run(["pdflatex","-interaction=nonstopmode","main.tex"],cwd="build",stdout=subprocess.DEVNULL,stdin=subprocess.DEVNULL)
log=open("build/main.log",errors="replace").read().splitlines()
errs=[l for l in log if l.startswith("!")]
undef=[l for l in log if re.search(r"undefined|Citation .* undefined|Reference .* undefined",l)]
ov=[]
for i,l in enumerate(log):
    m=re.match(r"Overfull \\hbox \(([\d.]+)pt too wide\) (.*)",l)
    if m and float(m.group(1))>15: ov.append((float(m.group(1)),m.group(2)))
pages=int(re.search(r"Pages:\s+(\d+)",subprocess.run(["pdfinfo","build/main.pdf"],capture_output=True,text=True).stdout).group(1))
p1=subprocess.run(["pdftotext","-f","1","-l","1","build/main.pdf","-"],capture_output=True,text=True).stdout
res=dict(errors=len(errs),error_lines=errs,undefined=len(undef),undef_lines=undef,overfull_gt15=ov,pages=pages,thm11_page1="Theorem 1.1" in p1)
res["P1"]=len(errs)==0;res["P2"]=len(undef)==0;res["P3"]=not ov;res["P4"]=res["thm11_page1"]
with open("mech.json","x") as f: json.dump(res,f,indent=1)
print(json.dumps(res,indent=1))
