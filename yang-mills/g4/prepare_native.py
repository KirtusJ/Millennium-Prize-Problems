"""Download pinned native boot inputs; extract a portable QEMU without installation."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import urllib.request

out = Path(sys.argv[1]).resolve()
out.mkdir(parents=True, exist_ok=False)

def download(url, name):
    dest = out/name
    with urllib.request.urlopen(url, timeout=120) as src, dest.open('wb') as dst:
        while chunk := src.read(1024*1024):
            dst.write(chunk)
    return dest

base = 'https://qemu.weilnetz.de/w64/'
checksum = download(base+'qemu-w64-setup-20260811.sha512', 'qemu.sha512').read_text().split()[0]
installer = download(base+'qemu-w64-setup-20260811.exe', 'qemu.exe')
if hashlib.sha512(installer.read_bytes()).hexdigest() != checksum:
    raise ValueError('QEMU published checksum mismatch')
seven = Path(r'C:\Program Files\7-Zip\7z.exe')
subprocess.run([str(seven),'x','-y',str(installer),'-o'+str(out/'qemu'),
    'qemu-system-x86_64.exe','*.dll','share/*'], check=True, stdout=subprocess.DEVNULL)
iso = download('https://raw.githubusercontent.com/KirtusJ/pcp/e23784155622311cfff697468beb0ba8bbe83194/PCP-OS.iso','PCP-OS.iso')
iso_hash = hashlib.sha256(iso.read_bytes()).hexdigest()
if iso_hash != '93ed3b599ad7be0e1e88a64813b1f2b5299d51507df2edca691aaf6189d10d15':
    raise ValueError('PCP ISO digest differs from the pinned upstream workflow')
subprocess.run([str(seven),'x','-y',str(iso),'-o'+str(out/'kernel'),'kernel.elf32'],check=True,stdout=subprocess.DEVNULL)
kernel_hash = hashlib.sha256((out/'kernel/kernel.elf32').read_bytes()).hexdigest()
if kernel_hash != 'd2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f':
    raise ValueError('Extracted kernel differs from B4 pinned runner')
record = {'qemu_source':base+'qemu-w64-setup-20260811.exe','qemu_sha512':checksum,
    'iso_sha256':iso_hash,'kernel_sha256':kernel_hash,
    'qemu_version':subprocess.check_output([str(out/'qemu/qemu-system-x86_64.exe'),'--version'],text=True)}
(out/'inputs.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
