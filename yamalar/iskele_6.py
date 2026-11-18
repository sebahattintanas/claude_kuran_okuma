# -*- coding: utf-8 -*-
"""iskele_6.py — sûre 6 (En'âm) blok başı kayıt dosya ailesini sûre 5 (maide_*) dosyalarından kurar.
OTURUM DIŞI. calisma/ içinde koşar. 2026-11-18 (adlar 'enam'; blok planı yamalar/blok_plani_6.txt,
19 bölüm / 40 blok — onaya açık taslak; okuma_metni.json tek dosyada kalır — sûre 5 kararı sürer).

Kurallar (iskele_3 / 4 / 5 dersi):
  * dosya eşlemesi ayrı; kaynak != hedef, kaynak var, hedef yok — assert'li
  * genel '5 → 6' değişimi YOK: ad eşlemeleri çapalı, sayısal alanlar ayrı çapalarla (assert'li)
  * boşaltılan: kok_ekle ISTEK, kayıt (CIPA / ARIZA / DUZELTME), metin sözlükleri, AX / AS, BLOKLAR / BASLIK
  * korunan: okuma_metni['6']'daki yedi eski blok özeti ('1-20' … '121-165') okuma sayılmaz;
    mercek_kayit['6'] eski ◇ notları (26 not) '_sikistirilmis_eski' arşivine
  * cipa_tarama6_adaylari.json = cipa_tarama4_adaylari.json (korpus koşusu) sûre 6 alt kümesi
  * kapanış / paket: BLOK_LISTESI_ELLE tanımsız (sûre sonunda elle)
"""
import os, re, ast, py_compile, importlib, sys, json

C = '/home/claude/calisma'
os.chdir(C)
ESLEME = [
    ('kok_ekle_5.py', 'kok_ekle_6.py'),
    ('maide_metin_1.py', 'enam_metin_1.py'),
    ('maide_kayit.py', 'enam_kayit.py'),
    ('uret_blok_5.py', 'uret_blok_6.py'),
    ('aday_ekle_5_maide.py', 'aday_ekle_6_enam.py'),
    ('duzeltme_5.py', 'duzeltme_6.py'),
    ('yama_retroaktif_gloss_5.py', 'yama_retroaktif_gloss_6.py'),
    ('maide_kapanis.py', 'enam_kapanis.py'),
    ('maide_paket_md.py', 'enam_paket_md.py'),
]
for k, h in ESLEME:
    assert k != h and os.path.exists(k) and not os.path.exists(h), (k, h)


def d(t, eski, yeni, adet=1):
    assert t.count(eski) == adet, 'çapa sayısı %d (beklenen %d): %r' % (t.count(eski), adet, eski[:90])
    return t.replace(eski, yeni)


def kes(t, bas, son, yeni):
    i = t.index(bas); j = t.index(son, i) + len(son)
    return t[:i] + yeni + t[j:]


AD = [('aday_ekle_5_maide', 'aday_ekle_6_enam'), ('maide_metin_1', 'enam_metin_1'), ('maide_kayit', 'enam_kayit'),
      ('maide_kapanis', 'enam_kapanis'), ('maide_paket_md', 'enam_paket_md'), ('sure5_maide_okuma', 'sure6_enam_okuma'),
      ('AX_maide', 'AX_enam'), ('AS_maide', 'AS_enam'), ('MAIDE', 'ENAM'),
      ('kok_ekle_5', 'kok_ekle_6'), ('duzeltme_5', 'duzeltme_6'), ('yama_retroaktif_gloss_5', 'yama_retroaktif_gloss_6'),
      ('uret_blok_5', 'uret_blok_6'), ('iskele_5', 'iskele_6'), ('Mâide', "En'âm"), ('mâide', "en'âm"),
      ('sûre 5', 'sûre 6'), ('Sûre 5', 'Sûre 6'), ('SÛRE 5', 'SÛRE 6'), ("_cipa_tablosu_5", "_cipa_tablosu_6"),
      ("_esma_profil_5", "_esma_profil_6"), ("'_profil_5'", "'_profil_6'"), ("okuma_metni['5']", "okuma_metni['6']"),
      ("mercek_kayit['5']", "mercek_kayit['6']"), ('cipa_tarama5_adaylari', 'cipa_tarama6_adaylari')]


def adlar(t):
    for a, b in AD:
        t = t.replace(a, b)
    return t


T = {h: open(k, encoding='utf-8').read() for k, h in ESLEME}

t = T['kok_ekle_6.py']
t = kes(t, 'ISTEK = [\n', '\n]\n',
        "ISTEK = [\n    # sûre 6 (En'âm) — blok blok eklenir (2026-11-18); korpus geçişleri kok_envanteri ayet_sayisi ile\n]\n")
t = adlar(t)
i = t.index('ISTEK = ['); j = t.index('\n]\n', i) + 3
assert ast.literal_eval(t[i:j].split('=', 1)[1].strip()) == []
T['kok_ekle_6.py'] = t

t = T['enam_metin_1.py']
t = t[:t.index('MEAL = {}\nM = {}\n') + len('MEAL = {}\nM = {}\n')]
T['enam_metin_1.py'] = adlar(t)

t = T['enam_kayit.py']
t = t[:t.index('\nS = 5\n')]
t += ("\nS = 6\n\n# Sûre 6'nın eski ayet kaydı yok (okuma 1. ayetten). okuma_metni['6']'daki yedi eski blok özeti dizgesi\n"
      "# (sıkıştırılmış dönem) bu dosyada YOK; kapanışta '_eski_ozet' altına taşınır (sûre 2-5 emsali).\n"
      '\nCIPA = {}\n\nARIZA = {}\n\nDUZELTME = {}\n')
T['enam_kayit.py'] = adlar(t)

t = T['uret_blok_6.py']
t = d(t, "S = 5\nMETIN = 'maide_metin_1'\nKAYIT = 'maide_kayit'\n", "S = 6\nMETIN = 'enam_metin_1'\nKAYIT = 'enam_kayit'\n")
t = kes(t, 'BLOKLAR = [', '\n}\n', 'BLOKLAR = []\nBASLIK = {\n}\n')
t = d(t, "eski blok özeti anahtarları ('1-20' … '101-120', sıkıştırılmış dönem)", "eski blok özeti anahtarları ('1-20' … '121-165', sıkıştırılmış dönem)")
t = d(t, "# SÛRE 5: mercek_kayit['5']'te eski sıkıştırılmış ◇ notları var (23 not).",
         "# SÛRE 6: mercek_kayit['6']'da eski sıkıştırılmış ◇ notları var (26 not).")
T['uret_blok_6.py'] = adlar(t)

t = T['aday_ekle_6_enam.py']
t = kes(t, 'MAIDE = [\n', '\n]\n', 'MAIDE = [\n]\n')
t = kes(t, 'BAGLAR = {"AS_maide": [\n', '\n]}\n', 'BAGLAR = {"AS_maide": [\n]}\n')
T['aday_ekle_6_enam.py'] = adlar(t)

t = T['duzeltme_6.py']
t = d(t, 'S = 5\n', 'S = 6\n')
T['duzeltme_6.py'] = adlar(t)

t = T['yama_retroaktif_gloss_6.py']
t = d(t, 'if str(s) in OKUNAN and s != 5})', 'if str(s) in OKUNAN and s != 6})')
T['yama_retroaktif_gloss_6.py'] = adlar(t)

t = T['enam_kapanis.py']
t = re.sub(r"BLOK_LISTESI_ELLE = \[[^\]]*\][^\n]*\n", '', t)
t = d(t, 'S, N = 5, 120\n', 'S, N = 6, 165\n')
t = d(t, "# SÛRE 5 (iskele_5): eski kayıt YOK. okuma_metni['5']'teki altı eski blok özeti dizgesi ('1-20' … '101-120') içerik\n",
         "# SÛRE 6 (iskele_6): eski kayıt YOK. okuma_metni['6']'daki yedi eski blok özeti dizgesi ('1-20' … '121-165') içerik\n")
t = d(t, "# aynen '_eski_ozet' altına taşınır (sûre 2, 3 ve 4 kapanış emsali; silinen 0).\n",
         "# aynen '_eski_ozet' altına taşınır (sûre 2-5 kapanış emsali; silinen 0).\n")
t = d(t, "'TAM SAYIM — sûre 5, 120 ayet'", "'TAM SAYIM — sûre 6, 165 ayet'")
t = d(t, "assert len(ESKI) == 6 and", "assert len(ESKI) == 7 and")
t = d(t, "I['not'] = \"Sûre 1, 2, 3, 4, 5, 9-114 TAM. Devam: sûre 6'dan.\"", "I['not'] = \"Sûre 1-6, 9-114 TAM. Devam: sûre 7'den.\"")
t = d(t, "I['son_oturum'] = 'OTURUM_PROMPT_sure5 (sûre 5 mâide sonu)'", "I['son_oturum'] = 'OTURUM_PROMPT_sure6 (sûre 6 enam sonu)'")
t = d(t, "'sûre 5 kaydı eksik — DUR'", "'sûre 6 kaydı eksik — DUR'")
t = d(t, "'sûre 5 anahtar sayısı — DUR'", "'sûre 6 anahtar sayısı — DUR'")
t = adlar(t)
assert 'BLOK_LISTESI_ELLE = ' not in t and "esma_kayit.py', str(S)" in t
T['enam_kapanis.py'] = t

t = T['enam_paket_md.py']
t = re.sub(r"BLOK_LISTESI_ELLE = \[[^\]]*\][^\n]*\n", '', t)
t = d(t, 'S = 5\n', 'S = 6\n')
t = d(t, '"# Sûre 5 (Mâide) — hesaplamalı okuma, 120 ayet (TAM; blok başı kayıt)\\n\\n"',
         '"# Sûre 6 (En\'âm) — hesaplamalı okuma, 165 ayet (TAM; blok başı kayıt)\\n\\n"')
t = adlar(t)
assert 'BL = BLOK_LISTESI_ELLE\n' in t and 'BLOK_LISTESI_ELLE = ' not in t
T['enam_paket_md.py'] = t

YASAK = ['maide', 'MAIDE', 'Mâide', 'mâide', '\nS = 5\n', 'S, N = 5', 'kok_ekle_5', 'duzeltme_5', 'uret_blok_5',
         "'_profil_5'", '_esma_profil_5', '_cipa_tablosu_5', "okuma_metni['5']", "mercek_kayit['5']", 'sûre 5', 'Sûre 5',
         'cipa_tarama5_adaylari']
for h, t in T.items():
    kalan = [y for y in YASAK if y in t]
    assert not kalan, 'sûre 5 izi kaldı: %s %s' % (h, kalan)
for h, t in T.items():
    open(h, 'w', encoding='utf-8').write(t)
    py_compile.compile(h, doraise=True)

TV = json.load(open('cipa_tarama4_adaylari.json', encoding='utf-8'))
T6 = [x for x in TV if x['ayet'].startswith('6:')]
assert not os.path.exists('cipa_tarama6_adaylari.json')
json.dump(T6, open('cipa_tarama6_adaylari.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

sys.path.insert(0, C)
M = importlib.import_module('enam_metin_1'); assert M.MEAL == {} and M.M == {}
K = importlib.import_module('enam_kayit'); assert K.CIPA == {} and K.ARIZA == {} and K.DUZELTME == {} and K.S == 6
s = open('aday_ekle_6_enam.py', encoding='utf-8').read()
assert 'ENAM = [\n]\n' in s and 'BAGLAR = {"AS_enam": [\n]}\n' in s
s = open('uret_blok_6.py', encoding='utf-8').read()
assert 'BLOKLAR = []\nBASLIK = {\n}\n' in s and "\nS = 6\n" in s
print('iskele_6: %d dosya kuruldu; cipa_tarama6 %d aday' % (len(T), len(T6)))
