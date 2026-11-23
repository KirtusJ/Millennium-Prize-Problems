#!/bin/sh
# runs lake env lean on the given absolute file from C:/Users/donke/z4-lean
cd /c/Users/donke/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean "$1"
