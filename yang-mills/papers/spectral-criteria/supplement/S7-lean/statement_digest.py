"""SHA-256 of the statement of a Lean theorem, by the convention of the pins in LEAN_PINS.md: the text between
`theorem <name>` and the first `:=` after it, comments removed, white space collapsed to single spaces.
It reads text; it does not run Lean. Usage: python3 statement_digest.py FILE NAME [PIN]
With PIN the exit code is 0 if the digest equals it and 1 otherwise; without PIN the digest is printed, exit 0.
The convention was recovered by matching known pins (controls are recorded in LEAN_PINS.md)."""
import re, sys, hashlib
def digest(path, name):
    t = open(path, encoding='utf-8').read()
    t = re.sub(r'/-.*?-/', '', t, flags=re.S); t = re.sub(r'--[^\n]*', '', t)
    m = re.search(r'\b(?:theorem|lemma)\s+' + re.escape(name) + r'(?![\w\'.])', t)
    if not m: raise SystemExit('no theorem ' + name)
    body = t[m.end(): t.index(':=', m.end())]
    return hashlib.sha256(' '.join(body.split()).encode()).hexdigest()
if __name__ == '__main__':
    d = digest(sys.argv[1], sys.argv[2].split('.')[-1])
    if len(sys.argv) > 3: sys.exit(0 if d == sys.argv[3] else 1)
    print(d)
