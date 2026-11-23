"""Check the exterior-state release and optionally deep-replay its PCP registers."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import runpy
import subprocess
import sys
from tempfile import TemporaryDirectory
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent
PIN = '43c7c130644cc95fc158b3f2dfbf907945125eb1abbb8984d7d45de118963b8c'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def verify_native(z, source):
    receipt = json.loads(z.read('native/receipt.json'))
    assert receipt['source_sha256'] == digest(source)
    cases = dict(exact=0,changed=1,truncated=1,appended=1,missing=2,denied=3,proof0=0,proof1=0,proof2=0)
    assert {c['case']:c['guest_exit'] for c in receipt['observations']} == cases
    parts = {}
    for case in receipt['observations']:
        name = case['case']
        raw = z.read(f'native/{name}/serial.log')
        assert case['exit_code'] == 33 and digest(raw) == case['serial_sha256']
        if name.startswith('proof'):
            frames = re.findall(rb'^G4 LEANHEX ([0-9a-f]+)\r?$',raw,re.M)
            parts[name] = bytes.fromhex(b''.join(frames).decode())
    assert b''.join(parts[f'proof{i}'] for i in range(3)) == source


def deep_replay(z, folders, runtime, method):
    sys.path.insert(0,str(runtime.resolve()))
    os.environ['PCPOS_METHOD'] = str(method.resolve())
    from pcpos.ops import Ops
    from pcpos.store import Workspace
    with TemporaryDirectory() as tmp:
        root = Path(tmp).resolve()
        for folder in folders:
            prefix = folder+'/register/'
            for name in z.namelist():
                if name.startswith(prefix):
                    path = (root/name).resolve()
                    assert path.is_relative_to(root)
                    path.parent.mkdir(parents=True,exist_ok=True)
                    path.write_bytes(z.read(name))
            result = Ops(Workspace(root/folder/'register'),'host').verify(deep=True)
            expected = json.loads(z.read(folder+'/receipt.json'))['verification']
            assert result['ok'] and result['head'] == expected['head']


def verify(runtime, method):
    source = (ROOT/'ExteriorStates.lean').read_bytes()
    assert digest(source) == PIN
    compiler_check = runpy.run_path(str(ROOT.parent/'contact-blocks/verify.py'))['check_compiler']
    with ZipFile(ROOT/'evidence.zip') as z:
        manifest = json.loads(z.read('manifest.json'))
        hashes = manifest['entries']
        assert set(z.namelist()) == set(hashes) | {'manifest.json'}
        assert len(z.namelist()) == len(hashes)+1
        assert all(digest(z.read(n)) == h for n,h in hashes.items())
        assert manifest['source_sha256'] == PIN
        assert manifest['control_sha256'] == digest((ROOT/'control.py').read_bytes())
        assert json.loads(subprocess.check_output([sys.executable,'-B',ROOT/'control.py'])) == json.loads(z.read('controls.json'))
        receipt, count = compiler_check(z,'compiler',source,'Millennium.G4.Exterior')
        assert count == 10
        mutations = (ROOT/'mutations.json').read_bytes()
        assert receipt['mutations_sha256'] == digest(mutations)
        accepted, *rejected = receipt['records']
        assert accepted['label'] == 'positive' and accepted['exit_code'] == 0
        for spec, run in zip(json.loads(mutations),rejected,strict=True):
            label = spec['label']
            assert run['label'] == label and run['exit_code'] != 0
            old, new = spec['find'].encode(), spec['replace'].encode()
            assert source.count(old) == 1
            assert z.read(f'compiler/child/{label}.lean') == source.replace(old,new)
            assert spec['diagnostic'].encode() in z.read(f'compiler/child/{label}.log')
        for name, passed in [('draft1',False),('draft2',False),('final1',True)]:
            assert json.loads(z.read(f'development/{name}/receipt.json'))['passed'] == passed
        registers = ['compiler','compiler/child']
        for task, packet in [('audit',z.read('inputs/audit.txt')),('formalizer',z.read('inputs/formalizer.txt')),
                             ('witness',z.read('inputs/spectral-test.md')),('review',source)]:
            parent = json.loads(z.read(task+'/receipt.json'))
            child = z.read(task+'/challenge/receipt.json')
            assert parent['passed'] and parent['candidate_sha256'] == digest(packet)
            assert parent['records'][0]['receipt_sha256'] == digest(child)
            assert json.loads(child)['readback_sha256'] == digest(z.read(task+'/challenge/model_reply.txt'))
            registers.extend([task,task+'/challenge'])
        verify_native(z,source)
        if runtime:
            deep_replay(z,registers,runtime,method)
    print(json.dumps(dict(reports=count,adverse=len(rejected),native_cases=9,
                          registers=len(registers) if runtime else 0,source_sha256=PIN)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runtime',type=Path)
    parser.add_argument('--method',type=Path)
    args = parser.parse_args()
    if bool(args.runtime) != bool(args.method):
        parser.error('Supply both --runtime and --method')
    verify(args.runtime,args.method)
