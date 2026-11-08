# -*- coding: utf-8 -*-
"""bakara_paket_md.py — sûre 2 (Bakara) TAM okumasının tek .md dosyası: her blok blok_goster_v2 çıktısı
(ek mercekler ◈K ◈B ◈D ◈A sûrenin tamamında) + kayıttaki blok bilançosu + sûre kapanış bilançosu,
çıpa tablosu ve esmâ profili. Sayı elle yazılmaz; hepsi okuma_metni.json'dan."""
import json, subprocess, sys
S = 2
BLOK_LISTESI_ELLE = [(21, 25), (26, 29), (30, 33), (34, 39), (40, 46), (47, 53), (54, 59), (60, 61), (62, 66), (67, 70), (71, 74), (75, 79), (80, 83), (84, 86), (87, 90), (91, 95), (96, 101), (102, 103), (104, 108), (109, 112), (113, 116), (117, 121), (122, 126), (127, 132), (133, 136), (137, 141), (142, 143), (144, 147), (148, 152), (153, 159), (160, 164), (165, 167), (168, 172), (173, 176), (177, 178), (179, 182), (183, 185), (186, 188), (189, 194), (195, 196), (197, 199), (200, 203), (204, 208), (209, 212), (213, 214), (215, 216), (217, 218), (219, 221), (222, 226), (227, 229), (230, 231), (232, 233), (234, 236), (237, 242), (243, 246), (247, 248), (249, 252), (253, 254), (255, 257), (258, 258), (259, 260), (261, 264), (265, 267), (268, 271), (272, 274), (275, 277), (278, 281), (282, 282), (283, 284), (285, 286)]
BL = BLOK_LISTESI_ELLE
OM = json.load(open('/home/claude/repo/notlar/okuma_metni.json', encoding='utf-8'))
out = ["# Sûre 2 (Bakara) — hesaplamalı okuma, 286 ayet (TAM; 1-20 eski kayıt, bloklar 21-286)\n\n",
       "Okuma sohbette yapıldı; bu dosya aynı betik çıktısının birleşimidir (`blok_goster_v2.py`; içerik `blok_goster.py` ile "
       "aynı, yalnız yerleşim: Arapça başlık boyutunda, ▽ dikey kök başına tablo). Ek mercekler (◈K ◈B ◈D ◈A) sûrenin "
       "tamamında (`notlar/ONKAYIT_mercekler.md`, a7e9628; §8 S1 tetik düzeltmesi uygulanıyor). Bilanço blokları `okuma_metni['2']['_bilanco']`, sûre bilançosu "
       "`_bilanco_sure`, çıpa tablosu `_cipa_tablosu_2`, esmâ profili `_esma_profil_2` kaydından basılır.\n"]
# eski kayıt (meal / not, aynen; kapanış kararı 2026-11-08)
import re
out.append('\n---\n\n## Eski kayıt (meal / not; ölçüm, mercek, dikey yok)\n\n')
for k, v in OM[str(S)].items():
    if re.fullmatch(r'%d:\d+(-\d+)?' % S, k) and set(v) == {'meal', 'not'}:
        out.append('### %s\n\n%s\n\n%s\n\n' % (k, v['meal'], v['not']))
for a, b in BL:
    g = subprocess.run([sys.executable, 'blok_goster_v2.py', str(S), str(a), str(b), 'bakara_metin_1'],
                       capture_output=True, text=True, check=True).stdout
    n = g.count('\n### ') + (1 if g.startswith('### ') else 0)
    assert n == b - a + 1, (a, b, n)
    out.append('\n---\n\n## Blok %d:%d-%d\n\n' % (S, a, b) + g)
    out.append('\n**Başlık sayısı: %d**\n\n### Blok bilançosu %d:%d-%d (kayıttan)\n\n```json\n%s\n```\n'
               % (n, S, a, b, json.dumps(OM[str(S)]['_bilanco']['%d-%d' % (a, b)], ensure_ascii=False, indent=1)))
duz = {k: v['duzeltildi'] for k, v in OM[str(S)].items() if isinstance(v, dict) and v.get('duzeltildi')}
out.append('\n---\n\n## Kayıt düzeltmeleri (özgün alan korunur)\n\n```json\n%s\n```\n' % json.dumps(duz, ensure_ascii=False, indent=1))
for k, t in [('_bilanco_sure', 'Sûre bilançosu (TAM SAYIM)'), ('_cipa_tablosu_2', 'Çıpa tablosu'),
             ('_esma_profil_2', 'Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)'), ('_eski_ozet', 'Eski blok özetleri (arşiv)'), ('_kapanis_notu', 'Kapanış notu')]:
    out.append('\n## %s\n\n```json\n%s\n```\n' % (t, json.dumps(OM[str(S)][k], ensure_ascii=False, indent=1)))
A = json.load(open('/home/claude/repo/bulgular/aday_bulgular.json', encoding='utf-8'))
out.append('\n## Sûre 2 aday kaydı (AX_bakara)\n\n```json\n%s\n```\n' % json.dumps(A['AX_bakara'], ensure_ascii=False, indent=1))
open('/home/claude/repo/notlar/sure2_bakara_okuma.md', 'w', encoding='utf-8').write(''.join(out))
print('yazıldı:', sum(len(x) for x in out), 'karakter ·', sum(b - a + 1 for a, b in BL), 'başlık')
