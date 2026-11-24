"""Re-run pcpos instrument mathematics.statement for each row of LEAN_PINS.md. Usage: python3 -I run_pins.py OUT.jsonl"""
import sys, json, subprocess, re, hashlib
R = "/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos"
D = "/home/user/Millennium-Prize-Problems/yang-mills/z4/attempt/reviews/"
SRC = {"Inheritance.lean": D + "f2-lean/Inheritance.lean", "haar.lean": D + "b2-haar/haar.lean"}
pins = open("/home/user/Millennium-Prize-Problems/yang-mills/z4/infrared/LEAN_PINS.md").read()
rows = re.findall(r"\| `(\S+)` \| `(\S+)` \| `([0-9a-f]{64})` \|", pins)
fo = open(sys.argv[1], "x")
for f, thm, pin in rows:
    src = open(SRC[f]).read()
    rec = {"file": f, "path": SRC[f], "file_sha256": hashlib.sha256(src.encode()).hexdigest(), "theorem": thm, "pinned": pin}
    for key, inp in (("with_pin", {"source": src, "theorem": thm, "pinned": pin}), ("no_pin", {"source": src, "theorem": thm}),
                     ("wrong_pin", {"source": src, "theorem": thm, "pinned": "0" * 64})):
        p = subprocess.run([R, "instrument", "mathematics.statement", json.dumps(inp)], capture_output=True, text=True)
        rec[key] = {"exit": p.returncode, "stdout": p.stdout, "stderr": p.stderr}
    fo.write(json.dumps(rec) + "\n")
    print("=====", f, thm, "exit with pin", rec["with_pin"]["exit"], "| no pin", rec["no_pin"]["exit"], "| wrong pin", rec["wrong_pin"]["exit"])
    print(rec["with_pin"]["stdout"], rec["with_pin"]["stderr"])
