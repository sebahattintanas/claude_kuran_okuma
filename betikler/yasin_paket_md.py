# -*- coding: utf-8 -*-
"""yasin_paket_md.py — sûre 36 (ARA: 1-20) okumasının tek .md dosyası: her blok blok_goster çıktısı + kayıttaki blok bilançosu
+ sûre kapanış bilançosu. Sayı elle yazılmaz; hepsi okuma_metni.json'dan."""
import json, subprocess, sys
S = 36
BL = [(1,10),(11,20)]
OM = json.load(open('/home/claude/repo/notlar/okuma_metni.json', encoding='utf-8'))
out = ["# Sûre 36 (Yâsîn) — hesaplamalı okuma, ayet 1-20 (ara kayıt)\n",
       "Okuma sohbette yapıldı; bu dosya aynı betik çıktısının birleşimidir (`blok_goster.py`). "
       "Bilanço blokları `okuma_metni['36']['_bilanco']` kaydından basılır.\n"]
for a, b in BL:
    g = subprocess.run([sys.executable, 'blok_goster.py', str(S), str(a), str(b), 'yasin_metin_1'],
                       capture_output=True, text=True, check=True).stdout
    n = g.count('\n### ')+ (1 if g.startswith('### ') else 0)
    assert n == b - a + 1, (a, b, n)
    out.append('\n---\n\n## Blok %d:%d-%d\n\n' % (S, a, b) + g)
    out.append('\n**Başlık sayısı: %d**\n\n### Blok bilançosu %d:%d-%d (kayıttan)\n\n```json\n%s\n```\n'
               % (n, S, a, b, json.dumps(OM[str(S)]['_bilanco']['%d-%d' % (a, b)], ensure_ascii=False, indent=1)))
open('/home/claude/sure36_yasin_1_20_okuma.md', 'w', encoding='utf-8').write(''.join(out))
print('yazıldı:', sum(len(x) for x in out), 'karakter')
