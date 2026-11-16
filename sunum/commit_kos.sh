#!/bin/bash
# bölüm 9 kuralı 15: denetim aracını bir blok commit'indeki sunum/basilan.txt ve sunum/sinifla.py (SON) ile koşar; canlı dosyalar koşu sonunda geri yüklenir
# kullanım (/home/claude'dan): bash sunum/commit_kos.sh <commit> <komut ...>   örn. bash sunum/commit_kos.sh 18a5ceb python3 sunum/sonradan.py --plan 21
set -e
REV=$1; shift
cd /home/claude
T=$(mktemp -d)
cp sunum/basilan.txt sunum/sinifla.py "$T"/
geri() { cp "$T"/basilan.txt "$T"/sinifla.py sunum/; rm -rf "$T"; }
trap geri EXIT
git -C repo show "$REV":sunum/basilan.txt > sunum/basilan.txt
git -C repo show "$REV":sunum/sinifla.py > sunum/sinifla.py
"$@"
