# -*- coding: utf-8 -*-
"""iskele_5.py — sûre 5 (Mâide) blok başı kayıt dosya ailesini sûre 4 (nisa_*) dosyalarından kurar.
OTURUM DIŞI. calisma/ içinde koşar. Kullanıcı kararı 2026-11-15 (adlar 'maide'; blok planı onaylı:
yamalar/blok_plani_5.txt, 16 bölüm / 36 blok; okuma_metni.json tek dosyada kalır — seçenek A).

Kurallar (iskele_3 / iskele_4 dersi):
  * dosya eşlemesi ayrı yazılır; kaynak != hedef, kaynak var, hedef yok — assert'li
  * genel '4 → 5' değişimi YOK: ad eşlemeleri çapalı, sayısal alanlar ayrı çapalarla (assert'li)
  * boşaltılan: kok_ekle ISTEK, kayıt (CIPA / ARIZA / DUZELTME), metin sözlükleri, AX / AS, BLOKLAR / BASLIK
  * korunan: S:A kapsam sayımı ('A-B' eski blok özeti anahtarları okuma sayılmaz — okuma_metni['5']'te altı eski özet),
    mercek_kayit['5'] eski ◇ notlarının '_sikistirilmis_eski' arşivi (23 not)
  * cipa_tarama5_adaylari.json = cipa_tarama4_adaylari.json'un (tarayıcı v4, korpus koşusu) sûre 5 alt kümesi;
    blok_bilanco.py korpus dosyasını okumaya devam eder (içerik aynı, assert'li)
  * kapanış / paket: BLOK_LISTESI_ELLE tanımsız (sûre sonunda elle)
  * son denetim: hedef dosyalarda 'nisa', 'NISA', 'Nisâ', '\nS = 4\n', 'kok_ekle_4', 'duzeltme_4' kalmadı
"""
import os, re, ast, py_compile, importlib, sys, json

C = '/home/claude/calisma'
os.chdir(C)
ESLEME = [
    ('kok_ekle_4.py', 'kok_ekle_5.py'),
    ('nisa_metin_1.py', 'maide_metin_1.py'),
    ('nisa_kayit.py', 'maide_kayit.py'),
    ('uret_blok_4.py', 'uret_blok_5.py'),
    ('aday_ekle_4_nisa.py', 'aday_ekle_5_maide.py'),
    ('duzeltme_4.py', 'duzeltme_5.py'),
    ('yama_retroaktif_gloss_4.py', 'yama_retroaktif_gloss_5.py'),
    ('nisa_kapanis.py', 'maide_kapanis.py'),
    ('nisa_paket_md.py', 'maide_paket_md.py'),
]
for k, h in ESLEME:
    assert k != h and os.path.exists(k) and not os.path.exists(h), (k, h)


def d(t, eski, yeni, adet=1):
    assert t.count(eski) == adet, 'çapa sayısı %d (beklenen %d): %r' % (t.count(eski), adet, eski[:90])
    return t.replace(eski, yeni)


def kes(t, bas, son, yeni):
    i = t.index(bas); j = t.index(son, i) + len(son)
    return t[:i] + yeni + t[j:]


AD = [('aday_ekle_4_nisa', 'aday_ekle_5_maide'), ('nisa_metin_1', 'maide_metin_1'), ('nisa_kayit', 'maide_kayit'),
      ('nisa_kapanis', 'maide_kapanis'), ('nisa_paket_md', 'maide_paket_md'), ('sure4_nisa_okuma', 'sure5_maide_okuma'),
      ('AX_nisa', 'AX_maide'), ('AS_nisa', 'AS_maide'), ('NISA', 'MAIDE'),
      ('kok_ekle_4', 'kok_ekle_5'), ('duzeltme_4', 'duzeltme_5'), ('yama_retroaktif_gloss_4', 'yama_retroaktif_gloss_5'),
      ('uret_blok_4', 'uret_blok_5'), ('iskele_4', 'iskele_5'), ('Nisâ', 'Mâide'), ('nisâ', 'mâide'),
      ('sûre 4', 'sûre 5'), ('Sûre 4', 'Sûre 5'), ('SÛRE 4', 'SÛRE 5'), ("_cipa_tablosu_4", "_cipa_tablosu_5"),
      ("_esma_profil_4", "_esma_profil_5"), ("'_profil_4'", "'_profil_5'"), ("okuma_metni['4']", "okuma_metni['5']"),
      ("mercek_kayit['4']", "mercek_kayit['5']"), ('cipa_tarama4_adaylari', 'cipa_tarama5_adaylari')]


def adlar(t):
    for a, b in AD:
        t = t.replace(a, b)
    return t


T = {h: open(k, encoding='utf-8').read() for k, h in ESLEME}

t = T['kok_ekle_5.py']
t = kes(t, 'ISTEK = [\n', '\n]\n',
        'ISTEK = [\n    # sûre 5 (Mâide) — blok blok eklenir (2026-11-15); korpus geçişleri kok_envanteri ayet_sayisi ile\n]\n')
t = adlar(t)
i = t.index('ISTEK = ['); j = t.index('\n]\n', i) + 3
assert ast.literal_eval(t[i:j].split('=', 1)[1].strip()) == []
T['kok_ekle_5.py'] = t

t = T['maide_metin_1.py']
t = t[:t.index('MEAL = {}\nM = {}\n') + len('MEAL = {}\nM = {}\n')]
T['maide_metin_1.py'] = adlar(t)

t = T['maide_kayit.py']
t = t[:t.index('\nS = 4\n')]
t += ('\nS = 5\n\n# Sûre 5\'in eski ayet kaydı yok (okuma 1. ayetten). okuma_metni[\'5\']\'teki altı eski blok özeti dizgesi\n'
      '# (sıkıştırılmış dönem) bu dosyada YOK; kapanışta \'_eski_ozet\' altına taşınır (sûre 2, 3 ve 4 emsali).\n'
      '\nCIPA = {}\n\nARIZA = {}\n\nDUZELTME = {}\n')
T['maide_kayit.py'] = adlar(t)

t = T['uret_blok_5.py']
t = d(t, "S = 4\nMETIN = 'nisa_metin_1'\nKAYIT = 'nisa_kayit'\n", "S = 5\nMETIN = 'maide_metin_1'\nKAYIT = 'maide_kayit'\n")
t = kes(t, 'BLOKLAR = [', '\n}\n', 'BLOKLAR = []\nBASLIK = {\n}\n')
t = d(t, "# SÛRE 4 (iskele_4): S'nin kayıtlı ayetleri", "# SÛRE 5 (iskele_5): S'nin kayıtlı ayetleri")
t = d(t, "eski blok özeti anahtarları ('1-20' … '141-176', sıkıştırılmış dönem)", "eski blok özeti anahtarları ('1-20' … '101-120', sıkıştırılmış dönem)")
t = d(t, "# SÛRE 4: mercek_kayit['4']'te eski sıkıştırılmış ◇ notları var (19 not).",
         "# SÛRE 5: mercek_kayit['5']'te eski sıkıştırılmış ◇ notları var (23 not).")
T['uret_blok_5.py'] = adlar(t)

t = T['aday_ekle_5_maide.py']
t = kes(t, 'NISA = [\n', '\n]\n', 'NISA = [\n]\n')
t = kes(t, 'BAGLAR = {"AS_nisa": [\n', '\n]}\n', 'BAGLAR = {"AS_nisa": [\n]}\n')
T['aday_ekle_5_maide.py'] = adlar(t)

t = T['duzeltme_5.py']
t = d(t, 'S = 4\n', 'S = 5\n')
T['duzeltme_5.py'] = adlar(t)

t = T['yama_retroaktif_gloss_5.py']
t = d(t, 'if str(s) in OKUNAN and s != 4})', 'if str(s) in OKUNAN and s != 5})')
T['yama_retroaktif_gloss_5.py'] = adlar(t)

t = T['maide_kapanis.py']
t = re.sub(r"BLOK_LISTESI_ELLE = \[[^\]]*\][^\n]*\n", '', t)
t = d(t, 'S, N = 4, 176\n', 'S, N = 5, 120\n')
t = d(t, "# SÛRE 4 (iskele_4): eski kayıt YOK. okuma_metni['4']'teki sekiz eski blok özeti dizgesi ('1-20' … '141-176') içerik\n",
         "# SÛRE 5 (iskele_5): eski kayıt YOK. okuma_metni['5']'teki altı eski blok özeti dizgesi ('1-20' … '101-120') içerik\n")
t = d(t, "# aynen '_eski_ozet' altına taşınır (sûre 2 ve 3 kapanış emsali; silinen 0).\n",
         "# aynen '_eski_ozet' altına taşınır (sûre 2, 3 ve 4 kapanış emsali; silinen 0).\n")
t = d(t, "'TAM SAYIM — sûre 4, 176 ayet'", "'TAM SAYIM — sûre 5, 120 ayet'")
t = d(t, "assert len(ESKI) == 8 and", "assert len(ESKI) == 6 and")
t = d(t, "I['not'] = \"Sûre 1, 2, 3, 4, 9-114 TAM. Devam: sûre 5'ten.\"", "I['not'] = \"Sûre 1, 2, 3, 4, 5, 9-114 TAM. Devam: sûre 6'dan.\"")
t = d(t, "I['son_oturum'] = 'OTURUM_PROMPT_sure4 (sûre 4 nisâ sonu)'", "I['son_oturum'] = 'OTURUM_PROMPT_sure5 (sûre 5 mâide sonu)'")
t = d(t, "'sûre 4 kaydı eksik — DUR'", "'sûre 5 kaydı eksik — DUR'")
t = d(t, "'sûre 4 anahtar sayısı — DUR'", "'sûre 5 anahtar sayısı — DUR'")
t = adlar(t)
assert 'BLOK_LISTESI_ELLE = ' not in t and "esma_kayit.py', str(S)" in t
T['maide_kapanis.py'] = t

t = T['maide_paket_md.py']
t = re.sub(r"BLOK_LISTESI_ELLE = \[[^\]]*\][^\n]*\n", '', t)
t = d(t, 'S = 4\n', 'S = 5\n')
t = d(t, '"# Sûre 4 (Nisâ) — hesaplamalı okuma, 176 ayet (TAM; blok başı kayıt)\\n\\n"',
         '"# Sûre 5 (Mâide) — hesaplamalı okuma, 120 ayet (TAM; blok başı kayıt)\\n\\n"')
t = adlar(t)
assert 'BL = BLOK_LISTESI_ELLE\n' in t and 'BLOK_LISTESI_ELLE = ' not in t
T['maide_paket_md.py'] = t

YASAK = ['nisa', 'NISA', 'Nisâ', 'nisâ', '\nS = 4\n', 'S, N = 4', 'kok_ekle_4', 'duzeltme_4', 'uret_blok_4',
         "'_profil_4'", '_esma_profil_4', '_cipa_tablosu_4', "okuma_metni['4']", "mercek_kayit['4']", 'sûre 4', 'Sûre 4',
         'cipa_tarama4_adaylari']
for h, t in T.items():
    kalan = [y for y in YASAK if y in t]
    assert not kalan, 'sûre 4 izi kaldı: %s %s' % (h, kalan)
    open(h, 'w', encoding='utf-8').write(t)
    py_compile.compile(h, doraise=True)

# cipa_tarama5: korpus koşusunun sûre 5 alt kümesi
TV = json.load(open('cipa_tarama4_adaylari.json', encoding='utf-8'))
T5 = [x for x in TV if x['ayet'].startswith('5:')]
assert not os.path.exists('cipa_tarama5_adaylari.json')
json.dump(T5, open('cipa_tarama5_adaylari.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

sys.path.insert(0, C)
M = importlib.import_module('maide_metin_1'); assert M.MEAL == {} and M.M == {}
K = importlib.import_module('maide_kayit'); assert K.CIPA == {} and K.ARIZA == {} and K.DUZELTME == {} and K.S == 5
s = open('aday_ekle_5_maide.py', encoding='utf-8').read()
assert 'MAIDE = [\n]\n' in s and 'BAGLAR = {"AS_maide": [\n]}\n' in s and "1043'ten" in s
s = open('uret_blok_5.py', encoding='utf-8').read()
assert 'BLOKLAR = []\nBASLIK = {\n}\n' in s and "\nS = 5\n" in s and "assert S not in TAM" in s
assert open('maide_kapanis.py', encoding='utf-8').read().count('BLOK_LISTESI_ELLE') == 3
assert open('maide_paket_md.py', encoding='utf-8').read().count('BLOK_LISTESI_ELLE') == 1
print('iskele_5: %d dosya kuruldu; cipa_tarama5 %d aday' % (len(T), len(T5)))
for k, h in ESLEME:
    print('  %-30s -> %s' % (k, h))
