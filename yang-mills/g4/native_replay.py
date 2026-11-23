"""Windows-portable calibration and source emission in measured PCP OS guests.

Readback code is pinned upstream. The host compiles freestanding ELF programs
with LLVM, observes guest exit, then reads each serial result. Three guests emit
pre-authored source portions; this is not independent mathematical reasoning.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time
import urllib.request

p = argparse.ArgumentParser()
for key in ('native','leanbin','method','source','out'):
    p.add_argument('--'+key,type=Path,required=True)
p.add_argument('--split-markers',nargs=2,
    default=['theorem kernel_limit_nonneg','-- Every squared test norm'])
a = p.parse_args()
a.out.mkdir(parents=True,exist_ok=False)
PIN = '92623fa6759bbb4e4f27ce5aa381de213a55ae0c'
EXPECTED_KERNEL = 'd2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f'
MEASUREMENT = '0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3'

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

kernel = a.native/'kernel/kernel.elf32'
if sha(kernel.read_bytes()) != EXPECTED_KERNEL:
    raise ValueError('Kernel pin mismatch')
core = (a.method/'MODULES/01_Core/SOURCE/Specification.md').read_bytes()
manifest = (a.method/'MANIFEST.json').read_bytes()
manifest_id = sha(manifest)
if manifest_id != '3949b2401d0a835cb116c22e44821993cbac59bbd2b281572ebb1b04e8296c18':
    raise ValueError('Expected the installed Enterprise method, not the older Python host method')
entry = [r for r in json.loads(manifest)['files'] if r['path']=='MODULES/01_Core/SOURCE/Specification.md']
if len(entry)!=1 or sha(core)!=entry[0]['sha256']:
    raise ValueError('Core source digest mismatch')
for name, path in [('readback.c','examples/method-readback/readback.c'),
                   ('link.ld','PCP_OS_Rust/crates/pcpos-kernel/programs/pcp-fib/link.ld')]:
    with urllib.request.urlopen(f'https://raw.githubusercontent.com/KirtusJ/pcp-os/{PIN}/{path}',timeout=30) as r:
        (a.out/name).write_bytes(r.read())
(a.out/'reference').write_bytes(core)
(a.out/'include').mkdir()
(a.out/'include/stddef.h').write_text('typedef __SIZE_TYPE__ size_t;\n')
(a.out/'include/stdint.h').write_text('typedef __UINTPTR_TYPE__ uintptr_t;\n')
(a.out/'reference.S').write_text('.section .rodata\n.global _binary_reference_start\n.global _binary_reference_end\n_binary_reference_start:\n.incbin "reference"\n_binary_reference_end:\n')

def command(argv):
    r = subprocess.run([str(x) for x in argv],cwd=a.out,capture_output=True,timeout=60,
        creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    if r.returncode:
        raise RuntimeError(r.stdout.decode(errors='replace')+r.stderr.decode(errors='replace'))

clang = a.leanbin/'clang.exe'
lld = a.leanbin/'ld.lld.exe'
command([clang,'--target=x86_64-unknown-linux-gnu','-c','reference.S','-o','reference.o'])
flags = [clang,'--target=x86_64-unknown-linux-gnu','-std=c11','-O2','-Wall','-Wextra','-Werror',
    '-ffreestanding','-fno-stack-protector','-fno-pie','-mno-red-zone','-mcmodel=large','-Iinclude','-c']
command(flags+['readback.c','-o','readback.o'])
command([lld,'-m','elf_x86_64','--build-id=none','-z','noexecstack','-T','link.ld','readback.o','reference.o','-o','core-read.elf'])
observations=[]

def boot(label, elf, files, expected_exit, grant=True):
    folder = a.out/label
    folder.mkdir()
    (folder/elf.name).write_bytes(elf.read_bytes())
    for name,raw in files.items():
        (folder/name).write_bytes(raw)
    argv=[str(a.native/'qemu/qemu-system-x86_64.exe'),'-L',str(a.native/'qemu/share'),
        '-machine','microvm,isa-serial=on,pic=on,pit=on,rtc=on','-accel','tcg,tb-size=4',
        '-icount','shift=3,align=off,sleep=off','-cpu','max','-m','32M','-nodefaults',
        '-nic','none','-display','none','-monitor','none','-serial','stdio','-no-reboot',
        '-kernel',str(kernel),'-initrd',','.join([elf.name,*files]),'-append',
        f'auto={elf.name} then=off image={MEASUREMENT}'+('' if grant else ' grant=none'),
        '-device','isa-debug-exit,iobase=0xf4,iosize=0x04']
    started=time.time_ns()
    proc=subprocess.run(argv,cwd=folder,capture_output=True,timeout=120,
        creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    exited=time.time_ns()
    (folder/'serial.log').write_bytes(proc.stdout)
    (folder/'emulator.log').write_bytes(proc.stderr)
    log=(folder/'serial.log').read_text(encoding='utf8',errors='replace').replace('\r','')
    starts=[s for s in log.splitlines() if s.startswith(f'starting {elf.name} (')]
    exits=re.findall(r'^'+re.escape(elf.name)+r' ended \w+: exit (\d+)\b',log,re.M)
    if proc.returncode!=33 or len(starts)!=1 or sha(elf.read_bytes()) not in starts[0] or exits!=[str(expected_exit)] or MEASUREMENT+' (measured; equal to the value the loader named)' not in log:
        raise RuntimeError(f'{label} failed: qemu={proc.returncode}\n'+log[-3000:]+'\n'+proc.stderr.decode(errors='replace'))
    heads=re.findall(r'head[:= ]+([0-9a-f]{64})',log)
    observations.append({'case':label,'exit_code':proc.returncode,'guest_exit':expected_exit,
        'start_ns':started,'exit_observed_ns':exited,'readback_ns':time.time_ns(),
        'serial_sha256':sha(proc.stdout),'worker_sha256':sha(elf.read_bytes()),'heads':heads})
    return log

for name,data,expected,status in [('exact',core,'MATCH',0),('changed',core[:-1]+bytes([core[-1]^1]),'DIFFERENT',1),
    ('truncated',core[:-1],'DIFFERENT',1),('appended',core+b'x','DIFFERENT',1),
    ('missing',None,'MISSING',2),('denied',core,'DENIED',3)]:
    log=boot(name,a.out/'core-read.elf',{} if data is None else {'core-spec.md':data},status,expected!='DENIED')
    if re.findall(r'^CORE READBACK (.+)$',log,re.M)!=[expected]:
        raise RuntimeError('Unexpected readback marker')
    print('PASS',name,expected,flush=True)

wrapper=r'''
#define READBACK_EMBEDDED
#include "readback.c"
static void line(const char *s) { long n=0; while(s[n]) ++n; call(1,1,(long)s,n); }
__attribute__((used,noreturn)) static void emit(void) {
  int check=read_core(); if(check) { call(60,10+check,0,0); __builtin_unreachable(); }
  long f=call(2,(long)"proof-part",0,0); if(f<0) { call(60,20,0,0); __builtin_unreachable(); }
  static unsigned char b[48]; static char h[98]; const char *digits="0123456789abcdef";
  for(;;) { long n=call(0,f,(long)b,48); if(n<0) { call(60,21,0,0); __builtin_unreachable(); }
    if(!n) break; for(long i=0;i<n;++i) { h[2*i]=digits[b[i]>>4]; h[2*i+1]=digits[b[i]&15]; }
    h[2*n]='\n'; h[2*n+1]=0; line("G4 LEANHEX "); line(h); }
  call(3,f,0,0);
#if ROLE == 0
  line("G4 NEXT 1\n");
#elif ROLE == 1
  line("G4 NEXT 2\n");
#else
  line("G4 COMPLETE\n");
#endif
  call(60,0,0,0); __builtin_unreachable();
}
__asm__(".global _start\n_start:\nandq $-16,%rsp\ncall emit\nud2");
'''
(a.out/'emit.c').write_text(wrapper)
source=a.source.read_bytes()
cuts=[0,*(source.index(marker.encode('utf8')) for marker in a.split_markers),len(source)]
if not all(left < right for left,right in zip(cuts,cuts[1:])):
    raise ValueError('Source split markers must be distinct and ordered')
parts=[]
for role in range(3):
    command(flags+[f'-DROLE={role}','emit.c','-o',f'emit{role}.o'])
    command([lld,'-m','elf_x86_64','--build-id=none','-z','noexecstack','-T','link.ld',f'emit{role}.o','reference.o','-o',f'g4-{role}.elf'])
    raw=source[cuts[role]:cuts[role+1]]
    log=boot('proof'+str(role),a.out/f'g4-{role}.elf',{'core-spec.md':core,'proof-part':raw},0)
    frames=re.findall(r'^G4 LEANHEX ([0-9a-f]+)$',log,re.M)
    emitted=bytes.fromhex(''.join(frames))
    if emitted!=raw or (role<2 and f'G4 NEXT {role+1}' not in log) or (role==2 and 'G4 COMPLETE' not in log):
        raise RuntimeError('Source/child request readback failed')
    parts.append(emitted)
    print('PASS source-emitter',role,sha(emitted),flush=True)
assembled=b''.join(parts)
(a.out/a.source.name).write_bytes(assembled)
if assembled!=source:
    raise AssertionError('Native source assembly mismatch')
receipt={'kernel_sha256':EXPECTED_KERNEL,'kernel_measurement':MEASUREMENT,
    'method_manifest_sha256':manifest_id,'core_sha256':sha(core),
    'source_sha256':sha(assembled),'source_generation':'Three measured native workers emit pre-authored portions; host supervises child requests and reads back after exit.',
    'independence':'No independent mathematical review claimed for the native emitters.',
    'upstream_readback_source_commit':PIN,'observations':observations}
(a.out/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print('PASS assembled-source',sha(assembled),flush=True)
