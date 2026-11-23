"""Verify the release evidence, optionally replaying the selected PCP registers."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from tempfile import TemporaryDirectory
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parent
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def check_compiler(archive, name, source, namespace):
    receipt = json.loads(archive.read(f'{name}/child/receipt.json'))
    supervisor = json.loads(archive.read(f'{name}/receipt.json'))
    assert receipt['passed'] and supervisor['passed']
    assert receipt['source_sha256'] == supervisor['source_sha256'] == digest(source)
    assert receipt['checker_sha256'] == supervisor['checker_sha256'] == digest(
        (ROOT.parent/'site/check_site.py').read_bytes())
    for folder, record in [(name,supervisor), (f'{name}/child',receipt)]:
        for item in record['records']:
            assert item['control_passed']
            assert item['start_ns'] <= item['exit_observed_ns'] <= item['post_exit_readback_ns']
            assert digest(archive.read(f"{folder}/{item['label']}.log")) == item['output_sha256']
    expected = re.findall(r'^#print axioms (\w+)\r?$',source.decode(),re.M)
    log = archive.read(f'{name}/child/positive.log').decode()
    reports = re.findall(r"^'" + re.escape(namespace) +
                         r"\.(\w+)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)",log,re.M)
    assert 'sorryAx' not in log and 'error:' not in log
    assert [symbol for symbol,_ in reports] == expected
    assert all({x.strip() for x in axioms.split(',') if x.strip()} <= ALLOWED for _,axioms in reports)
    return receipt, len(reports)


def verify(runtime, method):
    source = (ROOT/'ReflectedTails.lean').read_bytes()
    with ZipFile(ROOT/'evidence.zip') as archive:
        manifest = json.loads(archive.read('manifest.json'))
        entries = manifest['entries']
        assert len(archive.namelist()) == len(entries)+1
        assert set(archive.namelist()) == set(entries) | {'manifest.json'}
        assert all(digest(archive.read(n)) == value for n,value in entries.items())
        assert digest(source) == manifest['source_sha256']
        assert digest((ROOT/'control.py').read_bytes()) == manifest['control_sha256']
        result = subprocess.check_output([sys.executable,'-B',ROOT/'control.py'])
        assert json.loads(result) == json.loads(archive.read('controls/output.json'))

        c4 = archive.read('inputs/MagneticSmearing.lean')
        assert digest(c4) == '7e201b7275b6bb4dc2ee90c650addda474923ce889cfaeb2d4ad163d4e43c643'
        receipt, count = check_compiler(archive,'compiler',source,'Millennium.G4.ReflectedTails')
        _, c4count = check_compiler(archive,'c4-compiler',c4,'YangMills.MagneticSmearing')
        assert (count,c4count) == (16,21)
        mutations = (ROOT/'mutations.json').read_bytes()
        assert receipt['mutations_sha256'] == digest(mutations)
        records = receipt['records']
        assert records[0]['label'] == 'positive' and records[0]['exit_code'] == 0
        for mutation,record in zip(json.loads(mutations),records[1:],strict=True):
            label = mutation['label']
            assert record['label'] == label and record['exit_code'] != 0
            assert source.count(mutation['find'].encode()) == 1
            assert source.replace(mutation['find'].encode(),mutation['replace'].encode()) == archive.read(
                f'compiler/child/{label}.lean')
            assert mutation['diagnostic'] in archive.read(f'compiler/child/{label}.log').decode()

        registers = ['compiler','compiler/child','c4-compiler','c4-compiler/child']
        for folder,raw_candidate in [('audit',archive.read('inputs/block-math1.txt')),
                                     ('formalizer',archive.read('inputs/block-form1.txt')),
                                     ('rate',(ROOT/'README.md').read_bytes().replace(b'\r\n',b'\n')),
                                     ('review',source)]:
            parent = json.loads(archive.read(f'{folder}/receipt.json'))
            child = archive.read(f'{folder}/challenge/receipt.json')
            assert parent['passed'] and parent['candidate_sha256'] == digest(raw_candidate)
            assert parent['records'][0]['receipt_sha256'] == digest(child)
            assert json.loads(child)['readback_sha256'] == digest(archive.read(f'{folder}/challenge/model_reply.txt'))
            registers.extend([folder, f'{folder}/challenge'])

        native = json.loads(archive.read('native/receipt.json'))
        assert native['source_sha256'] == digest(source)
        cases = dict(exact=0,changed=1,truncated=1,appended=1,missing=2,denied=3,proof0=0,proof1=0,proof2=0)
        assert {obs['case']:obs['guest_exit'] for obs in native['observations']} == cases
        fragments = {}
        for obs in native['observations']:
            log = archive.read(f"native/{obs['case']}/serial.log")
            assert digest(log) == obs['serial_sha256'] and obs['exit_code']==33
            if obs['case'].startswith('proof'):
                fragments[obs['case']] = bytes.fromhex(''.join(re.findall(
                    r'^G4 LEANHEX ([0-9a-f]+)$',log.decode().replace('\r\n','\n'),re.M)))
        assert b''.join(fragments[f'proof{i}'] for i in range(3)) == source
        if runtime:
            sys.path.insert(0,str(runtime.resolve()))
            os.environ['PCPOS_METHOD'] = str(method.resolve())
            from pcpos.ops import Ops
            from pcpos.store import Workspace
            with TemporaryDirectory() as tmp:
                base = Path(tmp).resolve()
                for folder in registers:
                    prefix = folder+'/register/'
                    for name in entries:
                        if name.startswith(prefix):
                            p = (base/name).resolve()
                            assert p.is_relative_to(base)
                            p.parent.mkdir(parents=True,exist_ok=True)
                            p.write_bytes(archive.read(name))
                    replay = Ops(Workspace(base/folder/'register'),'host').verify(deep=True)
                    recorded = json.loads(archive.read(folder+'/receipt.json'))
                    assert replay['ok'] and replay['head']==recorded['verification']['head']
    print(json.dumps({'reports':count,'c4_reports':c4count,'adverse_variants':len(records)-1,
                      'native_cases':len(cases),'deep_registers':len(registers) if runtime else 0,
                      'source_sha256':digest(source)}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runtime',type=Path)
    parser.add_argument('--method',type=Path)
    args = parser.parse_args()
    if bool(args.runtime) != bool(args.method):
        parser.error('Supply both --runtime and --method')
    verify(args.runtime,args.method)
