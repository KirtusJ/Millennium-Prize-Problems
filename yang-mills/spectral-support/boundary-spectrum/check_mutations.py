"""Compile eight adverse claims together and require an error at each target theorem."""
import argparse
from pathlib import Path
import re
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mathlib', type=Path, required=True)
    mathlib = parser.parse_args().mathlib
    source = Path(__file__).with_name('BoundarySpectrum.lean').read_text()
    declarations = {m.group(2): m.group(0).rstrip() for m in re.finditer(
        r'^(def|theorem) (\w+)\b.*?(?=\n\n|\Z)', source, flags=re.S|re.M)}
    # Load the same definitions and the checked return-walk integers once. Each altered
    # claim below remains independent of every other adverse claim.
    preamble = source[:source.index('/--')]
    definitions = [v for v in declarations.values() if v.startswith('def ')]
    body = preamble + '\n\n'.join(definitions + [declarations['walkSums']]) + '\n\n'
    changes = [
        ('quadratic energy factor', 'rowEnergy', None, '2*((∑ i, ∑ j, K', '3*((∑ i, ∑ j, K'),
        ('surface area budget', 'boundaryTrace', None, '= 6*n^2 :=', '= 5*n^2 :='),
        ('potential row diagonal', 'checkedRow00', 'potential00', '#[497165963436325583,',
         '#[497165963436325584,'),
        ('central bond orbit', 'patchLayout', 'orbitRows', 'if i/4=3 then 4 else 8',
         'if i/4=3 then 8 else 8'),
        ('flat patch lower bound', 'surfaceBound', None, '(40119/10000:ℚ) <', '(40119/10000:ℚ) >'),
        ('corner covariance sign', 'cornerBound', None, '2*(6682304780825183191939141957321/',
         '-2*(6682304780825183191939141957321/'),
        ('large flat patch bound', 'largeSurface', None, '(40816/10000 : ℚ) <', '(40816/10000 : ℚ) >'),
        ('measured modular energy', 'modularPatch', 'measured', '[42, 46, 37, 149, 121, 151]',
         '[42, 46, 38, 149, 121, 151]'),
    ]
    expected = []
    for label, theorem, helper, old, new in changes:
        claim = declarations[theorem]
        target = declarations[helper] if helper else claim
        assert target.count(old) == 1, label
        altered = target.replace(old, new)
        if helper:
            alternate = helper + 'Altered'
            body += altered.replace('def '+helper+' ', 'def '+alternate+' ', 1) + '\n\n'
            claim = re.sub(r'\b'+helper+r'\b', alternate, claim)
        else:
            claim = altered
        start = body.count('\n')+1
        body += claim+'\n\n'
        expected.append((label, theorem, start, start+claim.count('\n')))
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp)/'Adverse.lean'
        p.write_text(body+'end Millennium.YangMills.D4.BoundarySpectrum\n')
        run = subprocess.run(['lake', 'env', 'lean', str(p)], cwd=mathlib, capture_output=True, text=True)
        errors = [int(x) for x in re.findall(re.escape(str(p))+r':(\d+):\d+: error:', run.stdout+run.stderr)]
        if run.returncode == 0 or any(not any(lo<=x<=hi for _,_,lo,hi in expected) for x in errors):
            raise RuntimeError('unexpected compiler result\n'+(run.stdout+run.stderr)[-1500:])
        for label, theorem, lo, hi in expected:
            if not any(lo<=x<=hi for x in errors):
                raise RuntimeError(f'{label} did not fail at {theorem}')
            print(label, 'rejected at', theorem)


if __name__=='__main__':
    main()
