#!/bin/bash
# kullanım: bash denetim.sh A B   (blok §5 denetimleri; SÛRE 4 — sûre 3 sürümü denetim_3.sh, sûre 2 sürümü denetim_2.sh)
A=$1; B=$2; cd /home/claude
echo "origin: $(git -C k ls-remote origin HEAD | cut -c1-7)"
(cd repo/tablolar && python3 ../betikler/turkce_denetim.py | tail -3)
(cd repo && PYTHONHASHSEED=0 timeout 600 python3 betikler/anahtar_denetim.py > /home/claude/anahtar_son.txt 2>&1); grep taranan anahtar_son.txt
diff <(grep -v taranan anahtar_taban.txt) <(grep -v taranan anahtar_son.txt) >/dev/null && echo "anahtar diff 0" || echo "ANAHTAR DIFF VAR"
(cd calisma && echo "e_el=? $(python3 esma_kayit.py 4 $A $B | grep -c 'e_el=?')"; python3 -c "ns={};exec(open('esma_el.py').read(),ns);print('KARAR',len(ns['KARAR']))")
(cd calisma && python3 oturum_tetik.py 4 $A $B nisa_metin_1 | tail -1; python3 oturum_xy.py 4 $A $B nisa_metin_1 | tail -1)
for f in betikler/nisa_kayit.py betikler/nisa_metin_1.py betikler/esma_el.py betikler/kok_ekle_4.py; do
 { if [ -f k/$f ]; then python3 sunum/sizinti.py k/$f; fi; } | grep ^SIZINTI | cut -d' ' -f2- | sed -E 's/^[^ ]*:[0-9]+ //' | sort > /tmp/sz_a.txt
 { if [ -f repo/$f ]; then python3 sunum/sizinti.py repo/$f; else python3 sunum/sizinti.py calisma/$(basename $f); fi; } | grep ^SIZINTI | cut -d' ' -f2- | sed -E 's/^[^ ]*:[0-9]+ //' | sort > /tmp/sz_b.txt
 echo "$f yeni sızıntı: $(comm -13 /tmp/sz_a.txt /tmp/sz_b.txt | wc -l)"; done
python3 sunum/sizinti.py yamalar/*_4_${A}_${B}.txt | tail -1
python3 - "$A" "$B" <<'EOF'
import json,sys
A,B=map(int,sys.argv[1:3])
a=json.load(open('/home/claude/om_once_%d.json'%A)); b=json.load(open('/home/claude/repo/notlar/okuma_metni.json'))
def flat(d,p=''):
    out={}
    for k,v in d.items():
        if isinstance(v,dict) and not ('ar' in v or 'meal' in v): out.update(flat(v,p+k+'/'))
        else: out[p+k]=v
    return out
fa,fb=flat(a),flat(b)
sil=[k for k in fa if k not in fb]; deg=[k for k in fa if k in fb and fa[k]!=fb[k]]
ek=[k for k in fb if k not in fa]
blok={'4/4:%d'%n for n in range(A,B+1)}
yabanci=[k for k in ek if k not in blok and not k.startswith('4/_bilanco/%d-%d/'%(A,B)) and k != 'ilerleme/kismi/4']  # kismi['4'] ilk blokta doğar
print('om: silinen',len(sil),'| değişen',deg,'| eklenen ayet',sorted(k for k in ek if k in blok),'| yabancı ek',yabanci)
m0=json.load(open('/home/claude/k/notlar/mercek_kayit.json'))['4'].get('_sikistirilmis_eski',{}); m1=json.load(open('/home/claude/repo/notlar/mercek_kayit.json'))['4'].get('_sikistirilmis_eski',{})
mt=json.load(open('/home/claude/k/notlar/mercek_kayit.json'))['4']
print('mercek arşivi',len(m0),'→',len(m1),'| eskiler aynı',all(m0[k]==m1[k] for k in m0),'| arşiv = taban notu',all(mt.get(k)==v for k,v in m1.items()))
EOF
