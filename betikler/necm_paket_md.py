# -*- coding: utf-8 -*-
"""necm_paket_md.py — sûre 53 (Necm) TAM okumasının tek .md dosyası: her blok blok_goster_v2 çıktısı
(ek mercekler ◈K ◈B ◈D ◈A sûrenin tamamında) + kayıttaki blok bilançosu + sûre kapanış bilançosu,
çıpa tablosu ve esmâ profili. Sayı elle yazılmaz; hepsi okuma_metni.json'dan."""
import json, subprocess, sys
S = 53
BL = [(1,10),(11,20),(21,30),(31,40),(41,50),(51,62)]
OM = json.load(open('/home/claude/repo/notlar/okuma_metni.json', encoding='utf-8'))
out = ["# Sûre 53 (Necm) — hesaplamalı okuma, 62 ayet (TAM)\n\n",
       "Okuma sohbette yapıldı; bu dosya aynı betik çıktısının birleşimidir (`blok_goster_v2.py`; içerik `blok_goster.py` ile "
       "aynı, yalnız yerleşim: Arapça başlık boyutunda, ▽ dikey kök başına tablo). Ek mercekler (◈K ◈B ◈D ◈A) sûrenin "
       "tamamında (`notlar/ONKAYIT_mercekler.md`, a7e9628; §8 S1 tetik düzeltmesi uygulanıyor). Bilanço blokları `okuma_metni['53']['_bilanco']`, sûre bilançosu "
       "`_bilanco_sure`, çıpa tablosu `_cipa_tablosu_53`, esmâ profili `_esma_profil_53` kaydından basılır.\n"]
for a, b in BL:
    g = subprocess.run([sys.executable, 'blok_goster_v2.py', str(S), str(a), str(b), 'necm_metin_1'],
                       capture_output=True, text=True, check=True).stdout
    n = g.count('\n### ') + (1 if g.startswith('### ') else 0)
    assert n == b - a + 1, (a, b, n)
    out.append('\n---\n\n## Blok %d:%d-%d\n\n' % (S, a, b) + g)
    out.append('\n**Başlık sayısı: %d**\n\n### Blok bilançosu %d:%d-%d (kayıttan)\n\n```json\n%s\n```\n'
               % (n, S, a, b, json.dumps(OM[str(S)]['_bilanco']['%d-%d' % (a, b)], ensure_ascii=False, indent=1)))
duz = {k: v['duzeltildi'] for k, v in OM[str(S)].items() if isinstance(v, dict) and v.get('duzeltildi')}
out.append('\n---\n\n## Kayıt düzeltmeleri (özgün alan korunur)\n\n```json\n%s\n```\n' % json.dumps(duz, ensure_ascii=False, indent=1))
for k, t in [('_bilanco_sure', 'Sûre bilançosu (TAM SAYIM)'), ('_cipa_tablosu_53', 'Çıpa tablosu'),
             ('_esma_profil_53', 'Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)'), ('_kapanis_notu', 'Kapanış notu')]:
    out.append('\n## %s\n\n```json\n%s\n```\n' % (t, json.dumps(OM[str(S)][k], ensure_ascii=False, indent=1)))
A = json.load(open('/home/claude/repo/bulgular/aday_bulgular.json', encoding='utf-8'))
out.append('\n## Sûre 53 aday kaydı (AX_necm)\n\n```json\n%s\n```\n' % json.dumps(A['AX_necm'], ensure_ascii=False, indent=1))
open('/home/claude/repo/notlar/sure53_necm_okuma.md', 'w', encoding='utf-8').write(''.join(out))
print('yazıldı:', sum(len(x) for x in out), 'karakter ·', sum(b - a + 1 for a, b in BL), 'başlık')
