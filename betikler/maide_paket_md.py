# -*- coding: utf-8 -*-
"""maide_paket_md.py — sûre 5 (Mâide) TAM okumasının tek .md dosyası: her blok blok_goster_v2 çıktısı
(ek mercekler ◈K ◈B ◈D ◈A sûrenin tamamında) + kayıttaki blok bilançosu + sûre kapanış bilançosu,
çıpa tablosu ve esmâ profili. Sayı elle yazılmaz; hepsi okuma_metni.json'dan."""
import json, subprocess, sys
S = 5
BLOK_LISTESI_ELLE = [(1, 2), (3, 4), (5, 6), (7, 11), (12, 14), (15, 17), (18, 19), (20, 23), (24, 26), (27, 30), (31, 32), (33, 36), (37, 40), (41, 41), (42, 44), (45, 47), (48, 50), (51, 54), (55, 58), (59, 63), (64, 66), (67, 70), (71, 74), (75, 77), (78, 81), (82, 86), (87, 89), (90, 93), (94, 96), (97, 100), (101, 105), (106, 108), (109, 110), (111, 115), (116, 117), (118, 120)]
BL = BLOK_LISTESI_ELLE
OM = json.load(open('/home/claude/repo/notlar/okuma_metni.json', encoding='utf-8'))
out = ["# Sûre 5 (Mâide) — hesaplamalı okuma, 120 ayet (TAM; blok başı kayıt)\n\n",
       "Okuma sohbette yapıldı; bu dosya aynı betik çıktısının birleşimidir (`blok_goster_v2.py`; içerik `blok_goster.py` ile "
       "aynı, yalnız yerleşim: Arapça başlık boyutunda, ▽ dikey kök başına tablo). Ek mercekler (◈K ◈B ◈D ◈A) sûrenin "
       "tamamında (`notlar/ONKAYIT_mercekler.md`, a7e9628; §8 S1 tetik düzeltmesi uygulanıyor). Bilanço blokları `okuma_metni['5']['_bilanco']`, sûre bilançosu "
       "`_bilanco_sure`, çıpa tablosu `_cipa_tablosu_5`, esmâ profili `_esma_profil_5` kaydından basılır.\n"]
for a, b in BL:
    g = subprocess.run([sys.executable, 'blok_goster_v2.py', str(S), str(a), str(b), 'maide_metin_1'],
                       capture_output=True, text=True, check=True).stdout
    n = g.count('\n### ') + (1 if g.startswith('### ') else 0)
    assert n == b - a + 1, (a, b, n)
    out.append('\n---\n\n## Blok %d:%d-%d\n\n' % (S, a, b) + g)
    out.append('\n**Başlık sayısı: %d**\n\n### Blok bilançosu %d:%d-%d (kayıttan)\n\n```json\n%s\n```\n'
               % (n, S, a, b, json.dumps(OM[str(S)]['_bilanco']['%d-%d' % (a, b)], ensure_ascii=False, indent=1)))
duz = {k: v['duzeltildi'] for k, v in OM[str(S)].items() if isinstance(v, dict) and v.get('duzeltildi')}
out.append('\n---\n\n## Kayıt düzeltmeleri (özgün alan korunur)\n\n```json\n%s\n```\n' % json.dumps(duz, ensure_ascii=False, indent=1))
for k, t in [('_bilanco_sure', 'Sûre bilançosu (TAM SAYIM)'), ('_cipa_tablosu_5', 'Çıpa tablosu'),
             ('_esma_profil_5', 'Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)'), ('_eski_ozet', 'Eski blok özetleri (arşiv)'), ('_kapanis_notu', 'Kapanış notu')]:
    out.append('\n## %s\n\n```json\n%s\n```\n' % (t, json.dumps(OM[str(S)][k], ensure_ascii=False, indent=1)))
A = json.load(open('/home/claude/repo/bulgular/aday_bulgular.json', encoding='utf-8'))
out.append('\n## Sûre 5 aday kaydı (AX_maide)\n\n```json\n%s\n```\n' % json.dumps(A['AX_maide'], ensure_ascii=False, indent=1))
open('/home/claude/repo/notlar/sure5_maide_okuma.md', 'w', encoding='utf-8').write(''.join(out))
print('yazıldı:', sum(len(x) for x in out), 'karakter ·', sum(b - a + 1 for a, b in BL), 'başlık')
