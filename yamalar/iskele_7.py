# -*- coding: utf-8 -*-
"""iskele_7.py — sûre 7 (A'râf) blok başı kayıt dosya ailesini sûre 6 (enam_*) dosyalarından kurar.
OTURUM DIŞI. calisma/ içinde koşar. 2026-11-24 (adlar 'araf'; blok planı yamalar/blok_plani_7.txt,
20 bölüm / 54 blok — onaylı; okuma_metni.json bölünmeden kalır — 2026-11-24 kararı).

Kurallar (iskele_3 / 4 / 5 / 6 dersi):
  * dosya eşlemesi ayrı; kaynak != hedef, kaynak var, hedef yok — assert'li
  * genel '6 → 7' değişimi YOK: ad eşlemeleri çapalı, sayısal alanlar ayrı çapalarla (assert'li)
  * boşaltılan: kok_ekle ISTEK, kayıt (CIPA / ARIZA / DUZELTME), metin sözlükleri, AX / AS, BLOKLAR / BASLIK
  * korunan: okuma_metni['7']'deki on eski blok özeti ('1-20' … '181-206') okuma sayılmaz;
    mercek_kayit['7'] eski ◇ notları (35 not) '_sikistirilmis_eski' arşivine
  * cipa_tarama7_adaylari.json = cipa_tarama4_adaylari.json (korpus koşusu) sûre 7 alt kümesi
  * kapanış / paket: BLOK_LISTESI_ELLE tanımsız (sûre sonunda elle)
"""
import os, re, ast, py_compile, importlib, sys, json

C = '/home/claude/calisma'
os.chdir(C)
ESLEME = [
    ('kok_ekle_6.py', 'kok_ekle_7.py'),
    ('enam_metin_1.py', 'araf_metin_1.py'),
    ('enam_kayit.py', 'araf_kayit.py'),
    ('uret_blok_6.py', 'uret_blok_7.py'),
    ('aday_ekle_6_enam.py', 'aday_ekle_7_araf.py'),
    ('duzeltme_6.py', 'duzeltme_7.py'),
    ('yama_retroaktif_gloss_6.py', 'yama_retroaktif_gloss_7.py'),
    ('enam_kapanis.py', 'araf_kapanis.py'),
    ('enam_paket_md.py', 'araf_paket_md.py'),
]
for k, h in ESLEME:
    assert k != h and os.path.exists(k) and not os.path.exists(h), (k, h)


def d(t, eski, yeni, adet=1):
    assert t.count(eski) == adet, 'çapa sayısı %d (beklenen %d): %r' % (t.count(eski), adet, eski[:90])
    return t.replace(eski, yeni)


def kes(t, bas, son, yeni):
    i = t.index(bas); j = t.index(son, i) + len(son)
    return t[:i] + yeni + t[j:]


AD = [('aday_ekle_6_enam', 'aday_ekle_7_araf'), ('enam_metin_1', 'araf_metin_1'), ('enam_kayit', 'araf_kayit'),
      ('enam_kapanis', 'araf_kapanis'), ('enam_paket_md', 'araf_paket_md'), ('sure6_enam_okuma', 'sure7_araf_okuma'),
      ('AX_enam', 'AX_araf'), ('AS_enam', 'AS_araf'), ('ENAM', 'ARAF'),
      ('kok_ekle_6', 'kok_ekle_7'), ('duzeltme_6', 'duzeltme_7'), ('yama_retroaktif_gloss_6', 'yama_retroaktif_gloss_7'),
      ('uret_blok_6', 'uret_blok_7'), ('iskele_6', 'iskele_7'), ("En'âm", "A'râf"), ("en'âm", "a'râf"),
      ('sûre 6', 'sûre 7'), ('Sûre 6', 'Sûre 7'), ('SÛRE 6', 'SÛRE 7'), ("_cipa_tablosu_6", "_cipa_tablosu_7"),
      ("_esma_profil_6", "_esma_profil_7"), ("'_profil_6'", "'_profil_7'"), ("okuma_metni['6']", "okuma_metni['7']"),
      ("mercek_kayit['6']", "mercek_kayit['7']"), ('cipa_tarama6_adaylari', 'cipa_tarama7_adaylari')]


def adlar(t):
    for a, b in AD:
        t = t.replace(a, b)
    return t


T = {h: open(k, encoding='utf-8').read() for k, h in ESLEME}

t = T['kok_ekle_7.py']
t = kes(t, 'ISTEK = [\n', '\n]\n',
        "ISTEK = [\n    # sûre 7 (A'râf) — blok blok eklenir (2026-11-24); korpus geçişleri kok_envanteri ayet_sayisi ile\n]\n")
t = adlar(t)
i = t.index('ISTEK = ['); j = t.index('\n]\n', i) + 3
assert ast.literal_eval(t[i:j].split('=', 1)[1].strip()) == []
T['kok_ekle_7.py'] = t

t = T['araf_metin_1.py']
t = t[:t.index('MEAL = {}\nM = {}\n') + len('MEAL = {}\nM = {}\n')]
T['araf_metin_1.py'] = adlar(t)

t = T['araf_kayit.py']
t = t[:t.index('\nS = 6\n')]
t += ("\nS = 7\n\n# Sûre 7'nin eski ayet kaydı yok (okuma 1. ayetten). okuma_metni['7']'deki on eski blok özeti dizgesi\n"
      "# (sıkıştırılmış dönem) bu dosyada YOK; kapanışta '_eski_ozet' altına taşınır (sûre 2-6 emsali).\n"
      '\nCIPA = {}\n\nARIZA = {}\n\nDUZELTME = {}\n')
T['araf_kayit.py'] = adlar(t)

t = T['uret_blok_7.py']
t = d(t, "S = 6\nMETIN = 'enam_metin_1'\nKAYIT = 'enam_kayit'\n", "S = 7\nMETIN = 'araf_metin_1'\nKAYIT = 'araf_kayit'\n")
t = kes(t, 'BLOKLAR = [', '\n}\n', 'BLOKLAR = []\nBASLIK = {\n}\n')
t = d(t, "eski blok özeti anahtarları ('1-20' … '121-165', sıkıştırılmış dönem)", "eski blok özeti anahtarları ('1-20' … '181-206', sıkıştırılmış dönem)")
t = d(t, "# SÛRE 6: mercek_kayit['6']'da eski sıkıştırılmış ◇ notları var (26 not).",
         "# SÛRE 7: mercek_kayit['7']'de eski sıkıştırılmış ◇ notları var (35 not).")
T['uret_blok_7.py'] = adlar(t)

t = T['aday_ekle_7_araf.py']
t = kes(t, 'ENAM = [\n', '\n]\n', 'ENAM = [\n]\n')
t = kes(t, 'BAGLAR = {"AS_enam": [\n', '\n]}\n', 'BAGLAR = {"AS_enam": [\n]}\n')
T['aday_ekle_7_araf.py'] = adlar(t)

t = T['duzeltme_7.py']
t = d(t, 'S = 6\n', 'S = 7\n')
T['duzeltme_7.py'] = adlar(t)

t = T['yama_retroaktif_gloss_7.py']
t = d(t, 'if str(s) in OKUNAN and s != 6})', 'if str(s) in OKUNAN and s != 7})')
T['yama_retroaktif_gloss_7.py'] = adlar(t)

t = T['araf_kapanis.py']
t = re.sub(r"BLOK_LISTESI_ELLE = \[[^\]]*\][^\n]*\n", '', t)
t = d(t, 'S, N = 6, 165\n', 'S, N = 7, 206\n')
t = d(t, "# SÛRE 6 (iskele_6): eski kayıt YOK. okuma_metni['6']'daki yedi eski blok özeti dizgesi ('1-20' … '121-165') içerik\n",
         "# SÛRE 7 (iskele_7): eski kayıt YOK. okuma_metni['7']'deki on eski blok özeti dizgesi ('1-20' … '181-206') içerik\n")
t = d(t, "# aynen '_eski_ozet' altına taşınır (sûre 2-5 kapanış emsali; silinen 0).\n",
         "# aynen '_eski_ozet' altına taşınır (sûre 2-6 kapanış emsali; silinen 0).\n")
t = d(t, "'TAM SAYIM — sûre 6, 165 ayet'", "'TAM SAYIM — sûre 7, 206 ayet'")
t = d(t, "assert len(ESKI) == 7 and", "assert len(ESKI) == 10 and")
t = d(t, "I['not'] = \"Sûre 1-6, 9-114 TAM. Devam: sûre 7'den.\"", "I['not'] = \"Sûre 1-7, 9-114 TAM. Devam: sûre 8'den.\"")
t = d(t, "I['son_oturum'] = 'OTURUM_PROMPT_sure6 (sûre 6 enam sonu)'", "I['son_oturum'] = 'OTURUM_PROMPT_sure7 (sûre 7 araf sonu)'")
t = d(t, "'sûre 6 kaydı eksik — DUR'", "'sûre 7 kaydı eksik — DUR'")
t = d(t, "'sûre 6 anahtar sayısı — DUR'", "'sûre 7 anahtar sayısı — DUR'")
t = adlar(t)
assert 'BLOK_LISTESI_ELLE = ' not in t and "esma_kayit.py', str(S)" in t
T['araf_kapanis.py'] = t

t = T['araf_paket_md.py']
t = re.sub(r"BLOK_LISTESI_ELLE = \[[^\]]*\][^\n]*\n", '', t)
t = d(t, 'S = 6\n', 'S = 7\n')
t = d(t, '"# Sûre 6 (En\'âm) — hesaplamalı okuma, 165 ayet (TAM; blok başı kayıt)\\n\\n"',
         '"# Sûre 7 (A\'râf) — hesaplamalı okuma, 206 ayet (TAM; blok başı kayıt)\\n\\n"')
t = adlar(t)
assert 'BL = BLOK_LISTESI_ELLE\n' in t and 'BLOK_LISTESI_ELLE = ' not in t
T['araf_paket_md.py'] = t

YASAK = ['enam', 'ENAM', "En'âm", "en'âm", '\nS = 6\n', 'S, N = 6', 'kok_ekle_6', 'duzeltme_6', 'uret_blok_6',
         "'_profil_6'", '_esma_profil_6', '_cipa_tablosu_6', "okuma_metni['6']", "mercek_kayit['6']", 'sûre 6', 'Sûre 6',
         'cipa_tarama6_adaylari']
for h, t in T.items():
    kalan = [y for y in YASAK if y in t]
    assert not kalan, 'sûre 6 izi kaldı: %s %s' % (h, kalan)
for h, t in T.items():
    open(h, 'w', encoding='utf-8').write(t)
    py_compile.compile(h, doraise=True)

TV = json.load(open('cipa_tarama4_adaylari.json', encoding='utf-8'))
T7 = [x for x in TV if x['ayet'].startswith('7:')]
assert not os.path.exists('cipa_tarama7_adaylari.json')
json.dump(T7, open('cipa_tarama7_adaylari.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

sys.path.insert(0, C)
M = importlib.import_module('araf_metin_1'); assert M.MEAL == {} and M.M == {}
K = importlib.import_module('araf_kayit'); assert K.CIPA == {} and K.ARIZA == {} and K.DUZELTME == {} and K.S == 7
s = open('aday_ekle_7_araf.py', encoding='utf-8').read()
assert 'ARAF = [\n]\n' in s and 'BAGLAR = {"AS_araf": [\n]}\n' in s
s = open('uret_blok_7.py', encoding='utf-8').read()
assert 'BLOKLAR = []\nBASLIK = {\n}\n' in s and "\nS = 7\n" in s
print('iskele_7: %d dosya kuruldu; cipa_tarama7 %d aday' % (len(T), len(T7)))
