# -*- coding: utf-8 -*-
"""fatir_paket_md.py — sûre 35 okumasının tek .md dosyası: her blok blok_goster çıktısı + kayıttaki blok bilançosu
+ sûre kapanış bilançosu. Sayı elle yazılmaz; hepsi okuma_metni.json'dan."""
import json, subprocess, sys
S = 35
BL = [(1,10),(11,20),(21,30),(31,40),(41,45)]
OM = json.load(open('/home/claude/repo/notlar/okuma_metni.json', encoding='utf-8'))
out = ["# Sûre 35 (Fâtır) — hesaplamalı okuma, 45 ayet\n",
       "Okuma sohbette yapıldı; bu dosya aynı betik çıktısının birleşimidir (`blok_goster.py`). "
       "Bilanço blokları `okuma_metni['35']['_bilanco']` kaydından basılır.\n"]
for a, b in BL:
    g = subprocess.run([sys.executable, 'blok_goster.py', str(S), str(a), str(b), 'fatir_metin_1'],
                       capture_output=True, text=True, check=True).stdout
    n = g.count('\n### ')+ (1 if g.startswith('### ') else 0)
    assert n == b - a + 1, (a, b, n)
    out.append('\n---\n\n## Blok %d:%d-%d\n\n' % (S, a, b) + g)
    out.append('\n**Başlık sayısı: %d**\n\n### Blok bilançosu %d:%d-%d (kayıttan)\n\n```json\n%s\n```\n'
               % (n, S, a, b, json.dumps(OM[str(S)]['_bilanco']['%d-%d' % (a, b)], ensure_ascii=False, indent=1)))
out.append('\n---\n\n## Sûre bilançosu (kayıttan)\n\n```json\n%s\n```\n' % json.dumps(
    {k: OM[str(S)][k] for k in ('_bilanco_sure', '_cipa_tablosu_35', '_esma_profil_35', '_kapanis_notu')},
    ensure_ascii=False, indent=1))
out.append('\n### Düzeltme kaydı\n\n```json\n%s\n```\n' % json.dumps(OM[str(S)]['35:12'].get('duzeltildi'), ensure_ascii=False, indent=1))
open('/home/claude/sure35_fatir_okuma.md', 'w', encoding='utf-8').write(''.join(out))
print('yazıldı:', sum(len(x) for x in out), 'karakter')
