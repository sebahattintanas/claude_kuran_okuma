# -*- coding: utf-8 -*-
"""zuhruf_paket_md.py — sûre 43 (Zuhruf) TAM okumasının tek .md dosyası: her blok blok_goster_v2 çıktısı
(ek mercekler ◈K ◈B ◈D ◈A sûrenin tamamında) + kayıttaki blok bilançosu + sûre kapanış bilançosu,
çıpa tablosu ve esmâ profili. Sayı elle yazılmaz; hepsi okuma_metni.json'dan."""
import json, subprocess, sys
S = 43
BL = [(1,10),(11,20),(21,30),(31,40),(41,50),(51,60),(61,70),(71,80),(81,89)]
OM = json.load(open('/home/claude/repo/notlar/okuma_metni.json', encoding='utf-8'))
out = ["# Sûre 43 (Zuhruf) — hesaplamalı okuma, 89 ayet (TAM)\n\n",
       "Okuma sohbette yapıldı; bu dosya aynı betik çıktısının birleşimidir (`blok_goster_v2.py`; içerik `blok_goster.py` ile "
       "aynı, yalnız yerleşim: Arapça başlık boyutunda, ▽ dikey kök başına tablo). Ek mercekler (◈K ◈B ◈D ◈A) sûrenin "
       "tamamında (`notlar/ONKAYIT_mercekler.md`, a7e9628; §8 S1 tetik düzeltmesi uygulanıyor). Bilanço blokları `okuma_metni['43']['_bilanco']`, sûre bilançosu "
       "`_bilanco_sure`, çıpa tablosu `_cipa_tablosu_43`, esmâ profili `_esma_profil_43` kaydından basılır.\n"]
for a, b in BL:
    g = subprocess.run([sys.executable, 'blok_goster_v2.py', str(S), str(a), str(b), 'zuhruf_metin_1'],
                       capture_output=True, text=True, check=True).stdout
    n = g.count('\n### ') + (1 if g.startswith('### ') else 0)
    assert n == b - a + 1, (a, b, n)
    out.append('\n---\n\n## Blok %d:%d-%d\n\n' % (S, a, b) + g)
    out.append('\n**Başlık sayısı: %d**\n\n### Blok bilançosu %d:%d-%d (kayıttan)\n\n```json\n%s\n```\n'
               % (n, S, a, b, json.dumps(OM[str(S)]['_bilanco']['%d-%d' % (a, b)], ensure_ascii=False, indent=1)))
duz = {k: v['duzeltildi'] for k, v in OM[str(S)].items() if isinstance(v, dict) and v.get('duzeltildi')}
out.append('\n---\n\n## Kayıt düzeltmeleri (özgün alan korunur)\n\n```json\n%s\n```\n' % json.dumps(duz, ensure_ascii=False, indent=1))
for k, t in [('_bilanco_sure', 'Sûre bilançosu (TAM SAYIM)'), ('_cipa_tablosu_43', 'Çıpa tablosu'),
             ('_esma_profil_43', 'Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)'), ('_kapanis_notu', 'Kapanış notu')]:
    out.append('\n## %s\n\n```json\n%s\n```\n' % (t, json.dumps(OM[str(S)][k], ensure_ascii=False, indent=1)))
A = json.load(open('/home/claude/repo/bulgular/aday_bulgular.json', encoding='utf-8'))
out.append('\n## Sûre 43 aday kaydı (AX_zuhruf)\n\n```json\n%s\n```\n' % json.dumps(A['AX_zuhruf'], ensure_ascii=False, indent=1))
open('/home/claude/repo/notlar/sure43_zuhruf_okuma.md', 'w', encoding='utf-8').write(''.join(out))
print('yazıldı:', sum(len(x) for x in out), 'karakter ·', sum(b - a + 1 for a, b in BL), 'başlık')
