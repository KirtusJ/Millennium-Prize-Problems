"""Check G4's cube and flow audit evidence and optionally replay its PCP registers."""
import argparse
import json
from pathlib import Path
import runpy
import subprocess
import sys
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent
PIN = '72b42a6271d5503d164dfb9dad162ef29a92074b8f778538726688918a6e2e74'
C4 = 'f4f42ea8512f3f973435e041ec09c31dd2b2767b2108940dc69f5b9b12d03f89'


def verify(runtime,method):
    common = runpy.run_path(str(ROOT.parent/'exterior/verify.py'))
    compiler = runpy.run_path(str(ROOT.parent/'contact-blocks/verify.py'))['check_compiler']
    digest = common['digest']
    source = (ROOT/'FlowChecks.lean').read_bytes()
    with ZipFile(ROOT/'evidence.zip') as z:
        m = json.loads(z.read('manifest.json'))
        entries = m['entries']
        assert set(z.namelist()) == set(entries) | {'manifest.json'}
        assert len(z.namelist()) == len(entries)+1
        assert all(digest(z.read(n)) == h for n,h in entries.items())
        assert m['source_sha256'] == digest(source) == PIN
        assert m['control_sha256'] == digest((ROOT/'control.py').read_bytes())
        assert m['c4_sha'] == '04370b2e92106cd77f45e1c5e020bc12c36e6356'
        assert digest(z.read('inputs/wilson.md')) == C4
        assert json.loads(z.read('controls.json')) == json.loads(
            subprocess.check_output([sys.executable,'-B',ROOT/'control.py']))
        receipt,count = compiler(z,'compiler',source,'Millennium.G4.FlowChecks')
        assert count == 7
        mutations = (ROOT/'mutations.json').read_bytes()
        assert receipt['mutations_sha256'] == digest(mutations)
        positive,*adverse = receipt['records']
        assert positive['label'] == 'positive' and positive['exit_code'] == 0
        for spec,run in zip(json.loads(mutations),adverse,strict=True):
            old,new = spec['find'].encode(),spec['replace'].encode()
            label = spec['label']
            assert run['label'] == label and run['exit_code'] != 0
            assert source.count(old) == 1
            assert z.read(f'compiler/child/{label}.lean') == source.replace(old,new)
            assert spec['diagnostic'].encode() in z.read(f'compiler/child/{label}.log')
        for job in ('draft1','draft2'):
            assert not json.loads(z.read(f'development/{job}/receipt.json'))['passed']
        folders = ['compiler','compiler/child']
        c4 = z.read('inputs/wilson.md')
        for task,packet in [('cube',c4),('euler',c4),('sign',z.read('inputs/moments.txt')),
                            ('seam',z.read('inputs/seam.txt')),('review',source)]:
            parent = json.loads(z.read(task+'/receipt.json'))
            child = z.read(task+'/challenge/receipt.json')
            assert parent['passed'] and parent['candidate_sha256'] == digest(packet)
            assert parent['records'][0]['receipt_sha256'] == digest(child)
            assert json.loads(child)['readback_sha256'] == digest(z.read(task+'/challenge/model_reply.txt'))
            folders.extend([task,task+'/challenge'])
        common['verify_native'](z,source)
        if runtime:
            common['deep_replay'](z,folders,runtime,method)
    print(json.dumps(dict(reports=count,adverse=len(adverse),native_cases=9,
                          registers=len(folders) if runtime else 0,source_sha256=PIN)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runtime',type=Path)
    parser.add_argument('--method',type=Path)
    args = parser.parse_args()
    if bool(args.runtime) != bool(args.method):
        parser.error('Supply both --runtime and --method')
    verify(args.runtime,args.method)
