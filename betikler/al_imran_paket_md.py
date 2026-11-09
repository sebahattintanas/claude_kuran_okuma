# -*- coding: utf-8 -*-
"""al_imran_paket_md.py — sûre 3 (Âl-i İmrân) TAM okumasının tek .md dosyası: her blok blok_goster_v2 çıktısı
(ek mercekler ◈K ◈B ◈D ◈A sûrenin tamamında) + kayıttaki blok bilançosu + sûre kapanış bilançosu,
çıpa tablosu ve esmâ profili. Sayı elle yazılmaz; hepsi okuma_metni.json'dan."""
import json, subprocess, sys
S = 3
BLOK_LISTESI_ELLE = [(1, 6), (7, 9), (10, 14), (15, 20), (21, 25), (26, 28), (29, 32), (33, 37), (38, 41), (42, 47), (48, 51), (52, 56), (57, 63), (64, 68), (69, 73), (74, 77), (78, 80), (81, 85), (86, 91), (92, 96), (97, 101), (102, 106), (107, 112), (113, 117), (118, 120), (121, 125), (126, 129), (130, 136), (137, 143), (144, 148), (149, 153), (154, 155), (156, 159), (160, 164), (165, 169), (170, 175), (176, 179), (180, 184), (185, 189), (190, 194), (195, 200)]  # uret_blok_3.BLOKLAR ile birebir (sûre 3 kapanışı, 2026-11-09)
BL = BLOK_LISTESI_ELLE
OM = json.load(open('/home/claude/repo/notlar/okuma_metni.json', encoding='utf-8'))
out = ["# Sûre 3 (Âl-i İmrân) — hesaplamalı okuma, 200 ayet (TAM; blok başı kayıt)\n\n",
       "Okuma sohbette yapıldı; bu dosya aynı betik çıktısının birleşimidir (`blok_goster_v2.py`; içerik `blok_goster.py` ile "
       "aynı, yalnız yerleşim: Arapça başlık boyutunda, ▽ dikey kök başına tablo). Ek mercekler (◈K ◈B ◈D ◈A) sûrenin "
       "tamamında (`notlar/ONKAYIT_mercekler.md`, a7e9628; §8 S1 tetik düzeltmesi uygulanıyor). Bilanço blokları `okuma_metni['3']['_bilanco']`, sûre bilançosu "
       "`_bilanco_sure`, çıpa tablosu `_cipa_tablosu_3`, esmâ profili `_esma_profil_3` kaydından basılır.\n"]
for a, b in BL:
    g = subprocess.run([sys.executable, 'blok_goster_v2.py', str(S), str(a), str(b), 'al_imran_metin_1'],
                       capture_output=True, text=True, check=True).stdout
    n = g.count('\n### ') + (1 if g.startswith('### ') else 0)
    assert n == b - a + 1, (a, b, n)
    out.append('\n---\n\n## Blok %d:%d-%d\n\n' % (S, a, b) + g)
    out.append('\n**Başlık sayısı: %d**\n\n### Blok bilançosu %d:%d-%d (kayıttan)\n\n```json\n%s\n```\n'
               % (n, S, a, b, json.dumps(OM[str(S)]['_bilanco']['%d-%d' % (a, b)], ensure_ascii=False, indent=1)))
duz = {k: v['duzeltildi'] for k, v in OM[str(S)].items() if isinstance(v, dict) and v.get('duzeltildi')}
out.append('\n---\n\n## Kayıt düzeltmeleri (özgün alan korunur)\n\n```json\n%s\n```\n' % json.dumps(duz, ensure_ascii=False, indent=1))
for k, t in [('_bilanco_sure', 'Sûre bilançosu (TAM SAYIM)'), ('_cipa_tablosu_3', 'Çıpa tablosu'),
             ('_esma_profil_3', 'Esmâ sûre profili (KAYIT; H1-H4 KOŞULMADI)'), ('_eski_ozet', 'Eski blok özetleri (arşiv)'), ('_kapanis_notu', 'Kapanış notu')]:
    out.append('\n## %s\n\n```json\n%s\n```\n' % (t, json.dumps(OM[str(S)][k], ensure_ascii=False, indent=1)))
A = json.load(open('/home/claude/repo/bulgular/aday_bulgular.json', encoding='utf-8'))
out.append('\n## Sûre 3 aday kaydı (AX_al_imran)\n\n```json\n%s\n```\n' % json.dumps(A['AX_al_imran'], ensure_ascii=False, indent=1))
open('/home/claude/repo/notlar/sure3_al_imran_okuma.md', 'w', encoding='utf-8').write(''.join(out))
print('yazıldı:', sum(len(x) for x in out), 'karakter ·', sum(b - a + 1 for a, b in BL), 'başlık')
