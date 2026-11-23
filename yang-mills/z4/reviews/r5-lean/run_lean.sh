#!/bin/bash
# usage: run_lean.sh <absolute path of .lean file>; exit code = lean exit code
cd /c/Users/donke/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean "$1"
