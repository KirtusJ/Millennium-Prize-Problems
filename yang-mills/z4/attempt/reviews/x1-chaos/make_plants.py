"""make_plants.py -- build 8 planted copies and 2 control copies of note/ (x1-chaos, T188).

Predicates (fixed before the first run):
  P-uniq   for each plant, every `old` string occurs exactly once in the original file.
  P-diff   each planted copy differs from note/ in exactly the recorded file and exactly the recorded
           line numbers (1 or 2 lines); line count unchanged.
  P-ctrl   control copies c1, c2 are byte-identical to note/*.tex.
  P-tex    each of the 10 copies compiles: two pdflatex passes, exit 0, "Output written ... (32 pages".
Tolerances: none (exact string / exact integer checks).
No randomness. Result file plants_build.json opened with mode "x" (never overwritten).
"""
import json, os, shutil, subprocess, sys, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
NOTE = os.path.join(ROOT, "note")
SRC = ["main.tex", "preamble.tex", "tun_upper.tex", "tun_lower.tex"]

PLANTS = {
 1: ("tun_upper.tex", [
     (r"\emph{Denominator.} We have $1-\cos\theta\le\theta^2/2$",
      r"\emph{Denominator.} We have $1-\cos\theta\ge\theta^2/2$")]),
 2: ("tun_lower.tex", [
     (r"m_0:=\tfrac12\big(1-e^{-3\eta/4}\big),",
      r"m_0:=\big(1-e^{-3\eta/4}\big),")]),
 3: ("tun_upper.tex", [
     (r"$\beta\ge\beta_1$ and every real eigenfunction $u$ of $T$ with eigenvalue $\mu\ge e^{-\eta/4}$:",
      r"$\beta\ge\beta_1$ and every real eigenfunction $u$ of $T$ with eigenvalue $\mu>0$:")]),
 4: ("tun_lower.tex", [
     (r"\item $\Omega:=\{\varphi>0\}\cap\{a_1\in[a_-,\pi-a_-]\}$ and",
      r"\item $\Omega:=\{\varphi>0\}\cap\{a_1\in[a_-/2,\pi-a_-/2]\}$ and"),
     (r"$R_{\rm well}:=\{\varphi>0\}\cap\{a_1<a_-\text{ or }a_1>\pi-a_-\}$.",
      r"$R_{\rm well}:=\{\varphi>0\}\cap\{a_1<a_-/2\text{ or }a_1>\pi-a_-/2\}$.")]),
 5: ("tun_lower.tex", [
     (r"is $\sigma_1$-invariant, $\varphi=\max(\varphi_L,\varphi_R)=\mu e^{-\sqrt\beta\min(\Psi(a_1),\Psi(\pi-a_1))}(G-c_1)_+(E-c_2)_+$",
      r"is $\sigma_1$-invariant, $\varphi\ge\varphi_L=\mu e^{-\sqrt\beta\Psi(a_1)}(G-c_1)_+(E-c_2)_+$"),
     (r"and $\min(\Psi(a_1),\Psi(\pi-a_1))=\Psi(\min(a_1,\pi-a_1))\le\Psi(\pi/2)$ since $\Psi$ is",
      r"and $\Psi(a_1)\le\Psi(\pi/2)$ since $\Psi$ is")]),
 6: ("tun_lower.tex", [
     (r"\item $M=M(\eta)$ with $M^2:=M_A^2(\eta)$, so",
      r"\item $M=M(\eta,\beta)$ with $M^2:=M_A^2(\eta)+\log\beta$, so")]),
 7: ("tun_upper.tex", [
     (r"=\frac12\iint(\varsigma(x)-\varsigma(y))^2g(x)T(x,y)g(y)\,dx\,dy=4\,\langle",
      r"=\frac12\iint(\varsigma(x)-\varsigma(y))^2g(x)T(x,y)g(y)\,dx\,dy=2\,\langle"),
     (r"So the integral is $2\cdot2\langle",
      r"So the integral is $2\langle")]),
 8: ("tun_upper.tex", [
     (r"On $\{|W'|^2\le4\tau\}$:", r"On $\{|W'|^2\le2\tau\}$:"),
     (r"On $\{|W'|^2>4\tau\}$: since", r"On $\{|W'|^2>2\tau\}$: since")]),
}

def read(p):
    with open(p, encoding="ascii") as fh:
        return fh.read()

def compile_dir(d):
    out = ""
    rc = 0
    for _ in range(2):
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                           cwd=d, capture_output=True, text=True, timeout=240)
        rc = r.returncode
        out = r.stdout
        if rc != 0:
            break
    line = [l for l in out.splitlines() if l.startswith("Output written")]
    pages = line[0] if line else ""
    # remove build products so the referee sees only sources
    for ext in (".aux", ".log", ".out", ".pdf", ".toc"):
        p = os.path.join(d, "main" + ext)
        if os.path.exists(p):
            os.remove(p)
    return rc, pages

def main():
    res = {"plants": {}, "controls": {}, "predicates": {}}
    os.makedirs(os.path.join(ROOT, "planted"), exist_ok=True)
    fails = []
    for k, (fname, reps) in PLANTS.items():
        d = os.path.join(ROOT, "planted", str(k))
        os.makedirs(d)  # fails if exists: never overwrite
        for s in SRC:
            shutil.copy(os.path.join(NOTE, s), os.path.join(d, s))
        orig = read(os.path.join(NOTE, fname))
        txt = orig
        uniq = True
        for old, new in reps:
            n = orig.count(old)
            if n != 1:
                uniq = False
            txt = txt.replace(old, new, 1)
        with open(os.path.join(d, fname), "w", encoding="ascii") as fh:
            fh.write(txt)
        ol, nl = orig.splitlines(), txt.splitlines()
        changed = [i + 1 for i, (a, b) in enumerate(zip(ol, nl)) if a != b]
        diff_ok = len(ol) == len(nl) and 1 <= len(changed) <= 2 and len(changed) == len(reps)
        rc, pages = compile_dir(d)
        tex_ok = rc == 0 and "(32 pages" in pages
        res["plants"][k] = {"file": fname, "changed_lines": changed,
                            "old": [ol[i - 1] for i in changed], "new": [nl[i - 1] for i in changed],
                            "uniq": uniq, "diff_ok": diff_ok, "tex_rc": rc, "pages": pages, "tex_ok": tex_ok}
        for name, ok in (("P-uniq", uniq), ("P-diff", diff_ok), ("P-tex", tex_ok)):
            if not ok:
                fails.append(f"{name} plant {k}")
    for c in ("c1", "c2"):
        d = os.path.join(ROOT, "planted", c)
        os.makedirs(d)
        for s in SRC:
            shutil.copy(os.path.join(NOTE, s), os.path.join(d, s))
        same = all(read(os.path.join(NOTE, s)) == read(os.path.join(d, s)) for s in SRC)
        rc, pages = compile_dir(d)
        tex_ok = rc == 0 and "(32 pages" in pages
        res["controls"][c] = {"identical": same, "tex_rc": rc, "pages": pages, "tex_ok": tex_ok}
        if not same:
            fails.append(f"P-ctrl {c}")
        if not tex_ok:
            fails.append(f"P-tex {c}")
    res["predicates"] = {"failed": fails, "met_count": 3 * 8 + 2 * 2 - len(fails), "failed_count": len(fails)}
    with open(os.path.join(ROOT, "plants_build.json"), "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res["predicates"]))
    for k, v in res["plants"].items():
        print(k, v["file"], v["changed_lines"], v["tex_ok"], v["pages"])
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
