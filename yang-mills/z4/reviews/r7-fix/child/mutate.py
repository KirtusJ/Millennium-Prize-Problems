"""Mutation test of src/two_dim_control_v2.py (fixed list, no randomness).

Each mutant is one exact string replacement (old string asserted to occur exactly once) in a
copy of the program placed alone in a fresh directory mut/<name>/. Every program execution goes
through `pcp_os.py check` (workspace ./pcp); stdout is read back from the PCP object store.
Results go to mutation_results.json (refused if it exists).

PREDICTIONS (written before the first run)
 m1  P1 real gap I_1/I_0 -> I_2/I_1: CAUGHT, exit 1, P1 FAILED (gap -> 3/2, D grows ~N^2,
     doubling factor ~1/4, outside [3,5]; same computation as NC_P1).
 m2  u1_closed uses I_{n+1}: CAUGHT, exit 1, H_all_cases FAILED (every U(1) case fails H),
     so no U(1) N qualifies and P1 FAILED (needs >= 2 N). NC_H still fails, no exit 2.
 m3  U(1) beta N^2 -> N^2+1: CAUGHT, exit 1, P1 FAILED (M ~ 1/2 - 1/(4N^2) < 1/2).
 m4  SU(2) beta 4N^2 -> 2N^2: CAUGHT, exit 1, P2 FAILED (M -> 3/4, M-3/8 -> 3/8 does not
     shrink, factor ~1; same computation as NC_P2).
 m5  Z_n asymptote halved: CAUGHT, exit 1, P3 FAILED (M/A ~ 2 at N=16).
 m6  TOL_H 1e-25 -> 1e-19 in code only: CAUGHT, exit 2, self-check defects
     "TOL_H in use ... != table 1e-25" and "negative control NC_H passed" (H stays MET).
 m7  TOL_P3 1e-6 -> 1 in code only: CAUGHT, exit 2, self-check defects
     "TOL_P3 in use ... != table 1e-6" and "negative control NC_P3 passed" (P3 stays MET).
 m8  one digit changed in P1 M[N=8] of a result copy, unmutated program --verify: CAUGHT,
     exit 3, first difference at /P1/M[1]. Baseline --verify on the unmodified copy: exit 0.
"""
import json, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "src", "two_dim_control_v2.py")
SRC_RES = os.path.join(HERE, "src", "two_dim_control_v2_result.json")
SITE = "C:/Users/donke/AppData/Roaming/Python/Python314/site-packages"
PCP = "C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py"
WS = os.path.join(HERE, "pcp")
OUTF = os.path.join(HERE, "mutation_results.json")
PROG = "two_dim_control_v2.py"

MUTANTS = [
    ("m1", "U(1) real P1 gap I_1/I_0 -> I_2/I_1",
     "M = {N: -mp.mpf(N) ** 2 * mp.log(mp.besseli(1, mp.mpf(N) ** 2) / mp.besseli(0, mp.mpf(N) ** 2)) for N in qual_u1}",
     "M = {N: -mp.mpf(N) ** 2 * mp.log(mp.besseli(2, mp.mpf(N) ** 2) / mp.besseli(1, mp.mpf(N) ** 2)) for N in qual_u1}",
     1, "P1 FAILED"),
    ("m2", "u1_closed uses I_{n+1}",
     "def u1_closed(n, b):  return mp.besseli(n, b) * mp.exp(-b)",
     "def u1_closed(n, b):  return mp.besseli(n + 1, b) * mp.exp(-b)",
     1, "H_all_cases FAILED, P1 FAILED (no qualifying U(1) N)"),
    ("m3", "U(1) real P1 beta N^2 -> N^2+1",
     "M = {N: -mp.mpf(N) ** 2 * mp.log(mp.besseli(1, mp.mpf(N) ** 2) / mp.besseli(0, mp.mpf(N) ** 2)) for N in qual_u1}",
     "M = {N: -mp.mpf(N) ** 2 * mp.log(mp.besseli(1, mp.mpf(N) ** 2 + 1) / mp.besseli(0, mp.mpf(N) ** 2 + 1)) for N in qual_u1}",
     1, "P1 FAILED (M < 1/2)"),
    ("m4", "SU(2) real P2 beta 4N^2 -> 2N^2",
     "M2 = {N: -mp.mpf(N) ** 2 * mp.log(mp.besseli(2, 4 * mp.mpf(N) ** 2) / mp.besseli(1, 4 * mp.mpf(N) ** 2)) for N in qual_su2}",
     "M2 = {N: -mp.mpf(N) ** 2 * mp.log(mp.besseli(2, 2 * mp.mpf(N) ** 2) / mp.besseli(1, 2 * mp.mpf(N) ** 2)) for N in qual_su2}",
     1, "P2 FAILED"),
    ("m5", "Z_n asymptote halved",
     "A = b * k * d * mp.exp(-b * d)",
     "A = b * k * d / 2 * mp.exp(-b * d)",
     1, "P3 FAILED"),
    ("m6", "TOL_H x1e6 (code only)",
     "TOL_H = mp.mpf(10) ** -25",
     "TOL_H = mp.mpf(10) ** -19",
     2, "self-check: TOL_H in use != table; NC_H passed"),
    ("m7", "TOL_P3 x1e6 (code only)",
     "TOL_P3 = mp.mpf(10) ** -6",
     "TOL_P3 = mp.mpf(10) ** 0",
     2, "self-check: TOL_P3 in use != table; NC_P3 passed"),
]


def run(name, dirpath, extra, expect):
    cmd = [sys.executable, PCP, "check", "--ws", WS, "--name", name, "--expect-exit", str(expect),
           "--cwd", dirpath, "--timeout", "3600", "--json", "--",
           sys.executable, "-I", os.path.join(dirpath, PROG), SITE] + extra
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    rec = json.loads(p.stdout)
    b = rec["body"]
    h = b["stdout"]
    with open(os.path.join(WS, "objects", h[:2], h), encoding="utf-8") as f:
        out = f.read()
    lines = out.splitlines()
    verdict_keys = ("H_all_cases", "P1 ", "P2 ", "P3 ", "negative_controls", "tolerance_table")
    return {"pcp_check_id": b["id"], "exit": b["exit"], "expected_exit": expect, "timeout": b["timeout"],
            "duration_ms": b["duration_ms"], "stdout_sha256": h,
            "verdict_lines": [l for l in lines if l.startswith(verdict_keys)],
            "self_check_defect_lines": [l for l in lines if l.startswith("SELF-CHECK DEFECT")],
            "verify_lines": [l for l in lines if l.startswith("VERIFY")]}


def main():
    if os.path.exists(OUTF):
        print("mutation_results.json exists; refusing to overwrite"); sys.exit(4)
    with open(SRC, encoding="utf-8") as f:
        src = f.read()
    results = {}
    for name, desc, old, new, expect, mech in MUTANTS:
        assert src.count(old) == 1, (name, src.count(old))
        d = os.path.join(HERE, "mut", name)
        os.makedirs(d)                                   # fails if not fresh
        with open(os.path.join(d, PROG), "w", encoding="utf-8", newline="\n") as f:
            f.write(src.replace(old, new))
        r = run(name, d, [], expect)
        r.update({"description": desc, "old": old, "new": new, "predicted_mechanism": mech})
        results[name] = r
        print(name, r["exit"], r["verdict_lines"], r["self_check_defect_lines"], flush=True)
    # m8: changed digit in a result copy, verified by the unmutated program
    d8 = os.path.join(HERE, "mut", "m8"); prog = os.path.join(d8, "prog")
    os.makedirs(prog)
    shutil.copyfile(SRC, os.path.join(prog, PROG))
    with open(SRC_RES, encoding="utf-8") as f:
        rs = f.read()
    o8, n8 = "0.503963426931821535322121931884", "0.503963426931821535322121931885"
    assert rs.count(o8) == 1, rs.count(o8)
    assert json.loads(rs)["P1"]["M"][1] == o8 and json.loads(rs)["P1"]["N"][1] == 8
    changed = os.path.join(d8, "changed.json"); base = os.path.join(d8, "unmodified.json")
    with open(changed, "w", encoding="utf-8", newline="\n") as f:
        f.write(rs.replace(o8, n8))
    shutil.copyfile(SRC_RES, base)
    rb = run("m8_baseline", prog, ["--verify", base], 0)
    rb.update({"description": "unmutated program --verify on unmodified result copy", "predicted_mechanism": "identical, exit 0"})
    results["m8_baseline"] = rb
    print("m8_baseline", rb["exit"], rb["verify_lines"], flush=True)
    rc = run("m8", prog, ["--verify", changed], 3)
    rc.update({"description": "unmutated program --verify on result with P1 M[N=8] last digit 4->5",
               "old": o8, "new": n8, "predicted_mechanism": "verify exit 3, first difference /P1/M[1]"})
    results["m8"] = rc
    print("m8", rc["exit"], rc["verify_lines"], flush=True)
    with open(OUTF, "x", encoding="utf-8", newline="\n") as f:
        json.dump(results, f, indent=1); f.write("\n")


if __name__ == "__main__":
    main()
