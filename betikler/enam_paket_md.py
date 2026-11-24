# -*- coding: utf-8 -*-
"""enam_paket_md.py — sûre 6 (En'âm) TAM okumasının tek .md dosyası: her blok blok_goster_v2 çıktısı
(ek mercekler ◈K ◈B ◈D ◈A sûrenin tamamında) + kayıttaki blok bilançosu + sûre kapanış bilançosu,
çıpa tablosu ve esmâ profili. Sayı elle yazılmaz; hepsi okuma_metni.json'dan."""
import json, subprocess, sys
BLOK_LISTESI_ELLE = [(1, 5), (6, 11), (12, 15), (16, 19), (20, 24), (25, 28), (29, 32), (33, 36), (37, 41), (42, 45), (46, 49), (50, 53), (54, 58), (59, 61), (62, 67), (68, 70), (71, 73), (74, 78), (79, 83), (84, 90), (91, 92), (93, 94), (95, 99), (100, 103), (104, 108), (109, 113), (114, 117), (118, 121), (122, 125), (126, 130), (131, 135), (136, 138), (139, 141), (142, 144), (145, 147), (148, 150), (151, 152), (153, 157), (158, 160), (161, 165)]
S = 6
BL = BLOK_LISTESI_ELLE
OM = json.load(open('/home/claude/repo/notlar/okuma_metni.json', encoding='utf-8'))
out = ["# Sûre 6 (En'âm) — hesaplamalı okuma, 165 ayet (TAM; blok başı kayıt)\n\n",
       "Okuma sohbette yapıldı; bu dosya aynı betik çıktısının birleşimidir (`blok_goster_v2.py`; içerik `blok_goster.py` ile "
       "aynı, yalnız yerleşim: Arapça başlık boyutunda, ▽ dikey kök başına tablo). Ek mercekler (◈K ◈B ◈D ◈A) sûrenin "
       "tamamında (`notlar/ONKAYIT_mercekler.md`, a7e9628; §8 S1 tetik düzeltmesi uygulanıyor). Bilanço blokları `okuma_metni['6']['_bilanco']`, sûre bilançosu "
       "`_bilanco_sure`, çıpa tablosu `_cipa_tablosu_6`, esmâ profili `_esma_profil_6` kaydından basılır.\n"]
for a, b in BL:
    g = subprocess.run([sys.executable, 'blok_goster_v2.py', str(S), str(a), str(b), 'enam_metin_1'],
                       capture_output=True, text=True, check=True).stdout
    n = g.count('\n### ') + (1 if g.startswith('### ') else 0)
    assert n == b - a + 1, (a, b, n)
    out.append('\n---\n\n## Blok %d:%d-%d\n\n' % (S, a, b) + g)
    out.append('\n**Başlık sayısı: %d**\n\n### Blok bilançosu %d:%d-%d (kayıttan)\n\n```json\n%s\n```\n'
               % (n, S, a, b, json.dumps(OM[str(S)]['_bilanco']['%d-%d' % (a, b)], ensure_ascii=False, indent=1)))
duz = {k: v['duzeltildi'] for k, v in OM[str(S)].items() if isinstance(v, dict) and v.get('duzeltildi')}
out.append('\n---\n\n## Kayıt düzeltmeleri (özgün alan korunur)\n\n```json\n%s\n```\n' % json.dumps(duz, ensure_ascii=False, indent=1))
for k, t in [('_bilanco_sure', 'Sûre bilançosu (TAM SAYIM)'), ('_cipa_tablosu_6', 'Çıpa tablosu'),
             ('_esma_profil_6', 'Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)'), ('_eski_ozet', 'Eski blok özetleri (arşiv)'), ('_kapanis_notu', 'Kapanış notu')]:
    out.append('\n## %s\n\n```json\n%s\n```\n' % (t, json.dumps(OM[str(S)][k], ensure_ascii=False, indent=1)))
A = json.load(open('/home/claude/repo/bulgular/aday_bulgular.json', encoding='utf-8'))
out.append('\n## Sûre 6 aday kaydı (AX_enam)\n\n```json\n%s\n```\n' % json.dumps(A['AX_enam'], ensure_ascii=False, indent=1))
open('/home/claude/repo/notlar/sure6_enam_okuma.md', 'w', encoding='utf-8').write(''.join(out))
print('yazıldı:', sum(len(x) for x in out), 'karakter ·', sum(b - a + 1 for a, b in BL), 'başlık')
