"""extract_reports.py -- extract each referee's final text and audit its tool calls (x1-chaos, T188).

Predicates (fixed before the first run):
  E-final  each reports/<k>.jsonl contains a final "result" event with nonempty text.
  E-leak   no tool call of the child references PLANTS, plants.sha256, plants_build, make_plants, notes.md,
           report.md, prompts/, reports/, or a path outside its own planted/<k>/ ("..", "/home/user/z4-workers/x1-chaos/"
           not followed by "planted/<k>"), and no tool call references note/ (the unplanted original).
  E-calls  number of tool calls is measured only (the instruction said about 12).
Writes reports/<k>.final.md (mode "x") and audit.json (mode "x"). Measured: tool-call count, duration, cost.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
KEYS = ["1", "2", "3", "4", "5", "6", "7", "8", "c1", "c2"]
BAD = re.compile(r"PLANTS|plants\.sha256|plants_build|make_plants|notes\.md|report\.md|prompts/|reports/|\.\./|/note/|/note\b")

def main():
    audit = {}
    fails = []
    for k in KEYS:
        p = os.path.join(ROOT, "reports", f"{k}.jsonl")
        if not os.path.exists(p):
            audit[k] = {"present": False}
            fails.append(f"E-final {k} (missing)")
            continue
        calls, final, meta = [], None, {}
        for line in open(p, encoding="utf-8", errors="replace"):
            try:
                ev = json.loads(line)
            except Exception:
                continue
            if ev.get("type") == "assistant":
                for c in ev.get("message", {}).get("content", []):
                    if c.get("type") == "tool_use":
                        calls.append(json.dumps(c.get("input", {})))
            if ev.get("type") == "result":
                final = ev.get("result")
                meta = {kk: ev.get(kk) for kk in ("duration_ms", "num_turns", "total_cost_usd", "is_error", "subtype")}
        mine = f"/home/user/z4-workers/x1-chaos/planted/{k}"
        leaks = []
        for c in calls:
            if BAD.search(c):
                leaks.append(c[:200])
            for m in re.finditer(r"/home/user/z4-workers/x1-chaos[^\"' ]*", c):
                if not m.group(0).startswith(mine):
                    leaks.append(m.group(0))
        audit[k] = {"present": True, "tool_calls": len(calls), "final_present": bool(final), "leaks": leaks, **meta}
        if final:
            with open(os.path.join(ROOT, "reports", f"{k}.final.md"), "x") as fh:
                fh.write(final)
        else:
            fails.append(f"E-final {k}")
        if leaks:
            fails.append(f"E-leak {k}")
    with open(os.path.join(ROOT, "audit.json"), "x") as fh:
        json.dump({"audit": audit, "failed": fails}, fh, indent=1)
    for k, v in audit.items():
        print(k, {kk: v.get(kk) for kk in ("tool_calls", "final_present", "duration_ms", "num_turns", "is_error")}, "leaks:", len(v.get("leaks", [])))
    print("failed:", fails)
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
