"""Recheck revision one's original Lean sources in its pinned Mathlib environment.

Run with "lake env python /path/to/replay_z4.py" in Mathlib at the revision below.
"""
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory

REV = "c705f2675a7ab5ca2b166fe3c1d4e3438d654ed4"
MATHLIB = "c44e0c8ee63ca166450922a373c7409c5d26b00b"
REPO = Path(__file__).resolve().parents[4]
Z4 = "yang-mills/z4/lean/"
PAPER = "yang-mills/z4/attempt/paper/lean/"

AUDIT = """
import Z4YM
import Lean.Util.CollectAxioms
open Lean Elab Command
set_option maxHeartbeats 0 in
run_cmd do
  let env ← getEnv
  let mut names : Array Name := #[]
  for i in [:env.header.moduleNames.size] do
    if env.header.moduleNames[i]!.getRoot == `Z4YM then
      for info in env.header.moduleData[i]!.constants do
        if info.isTheorem then names := names.push info.name
  if names.isEmpty then throwError "Empty audit"
  let (_, s) := ((names.forM CollectAxioms.collect).run env).run {}
  for a in s.axioms do
    if !([`propext, `Classical.choice, `Quot.sound] : List Name).contains a then
      throwError "Unexpected axiom {a}"
  logInfo m!"{names.size} Z4 theorem constants. Axioms: {s.axioms}."
"""


def git(*args):
    return subprocess.check_output(["git", "-C", REPO, *args])


def blob(path):
    return git("show", f"{REV}:{path}")


def main():
    mathrev = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    if mathrev != MATHLIB:
        raise ValueError("Run inside the pinned Mathlib checkout")
    lean = str(Path(shutil.which("lean")).resolve())
    with TemporaryDirectory() as tmp:
        src = Path(tmp)
        build = src / "out"
        (src / "Z4YM").mkdir()
        (build / "Z4YM").mkdir(parents=True)
        paths = [str(Path(p).resolve()) for p in os.environ["LEAN_PATH"].split(os.pathsep) if p]
        env = {**os.environ, "LEAN_PATH": os.pathsep.join([str(build)] + paths)}

        def check(name, compile_module=False):
            args = [lean]
            if compile_module:
                args += ["-o", str((build / name).with_suffix(".olean"))]
            return subprocess.check_output(args+[name], cwd=src, env=env, text=True)

        files = git("ls-tree", "-r", "--name-only", REV, Z4+"Z4YM/").decode().splitlines()
        for path in files+[Z4+"Z4YM.lean"]:
            if path.endswith(".lean"):
                name = path.removeprefix(Z4)
                (src / name).write_bytes(blob(path))
                check(name, compile_module=True)
        (src/"Audit.lean").write_text(AUDIT)
        print(check("Audit.lean").strip())

        for line in blob(PAPER+"SHA256SUMS").decode().splitlines():
            digest, name = line.split()
            data = blob(PAPER+name)
            assert hashlib.sha256(data).hexdigest() == digest
            (src/name).write_bytes(data)
            output = check(name)
            reports = [s for s in output.splitlines() if "depends on axioms:" in s
                       or "does not depend on any axioms" in s]
            expected = blob(PAPER+name+".axioms.txt").decode().splitlines()
            assert reports and reports == expected, name
            print(name, len(reports), "matching axiom reports")


if __name__ == "__main__":
    main()
