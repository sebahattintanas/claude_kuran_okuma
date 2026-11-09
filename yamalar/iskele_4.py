# -*- coding: utf-8 -*-
"""iskele_4.py — sûre 4 (Nisâ) blok başı kayıt dosya ailesini sûre 3 (al_imran_*) dosyalarından kurar.
OTURUM DIŞI. calisma/ içinde koşar. Kullanıcı kararı 2026-11-09 (adlar 'nisa'; blok planı taslağı onaya).

Kurallar (iskele_2 / iskele_3 dersi):
  * dosya eşlemesi ayrı yazılır; kaynak != hedef, kaynak var, hedef yok — assert'li
  * genel '3 → 4' değişimi YOK: ad eşlemeleri çapalı (her biri sayısı > 0 assert'li), sayısal alanlar ayrı çapalarla
  * boşaltılan: kok_ekle ISTEK, kayıt (CIPA / ARIZA / DUZELTME), metin sözlükleri, AX / AS, BLOKLAR / BASLIK — assert'li
  * korunan: S:A kapsam sayımı ('A-B' eski blok özeti anahtarları okuma sayılmaz — okuma_metni['4']'te sekiz eski özet),
    mercek_kayit['4'] eski ◇ notlarının '_sikistirilmis_eski' arşivi (19 not)
  * kapanış / paket: BLOK_LISTESI_ELLE tanımsız (sûre sonunda elle; sûre 3 kapanışındaki düzeltme: esmâ ön koşulu str(S))
  * son denetim: hedef dosyalarda 'al_imran', 'AL_IMRAN', 'Âl-i İmrân', '\nS = 3\n', 'kok_ekle_3', 'duzeltme_3' kalmadı
"""
import os, re, ast, py_compile, importlib, sys

C = '/home/claude/calisma'
os.chdir(C)
ESLEME = [
    ('kok_ekle_3.py', 'kok_ekle_4.py'),
    ('al_imran_metin_1.py', 'nisa_metin_1.py'),
    ('al_imran_kayit.py', 'nisa_kayit.py'),
    ('uret_blok_3.py', 'uret_blok_4.py'),
    ('aday_ekle_3_al_imran.py', 'aday_ekle_4_nisa.py'),
    ('duzeltme_3.py', 'duzeltme_4.py'),
    ('yama_retroaktif_gloss_3.py', 'yama_retroaktif_gloss_4.py'),
    ('al_imran_kapanis.py', 'nisa_kapanis.py'),
    ('al_imran_paket_md.py', 'nisa_paket_md.py'),
]
for k, h in ESLEME:
    assert k != h and os.path.exists(k) and not os.path.exists(h), (k, h)


def d(t, eski, yeni, adet=1):
    assert t.count(eski) == adet, 'çapa sayısı %d (beklenen %d): %r' % (t.count(eski), adet, eski[:90])
    return t.replace(eski, yeni)


def kes(t, bas, son, yeni):
    i = t.index(bas); j = t.index(son, i) + len(son)
    return t[:i] + yeni + t[j:]


AD = [('aday_ekle_3_al_imran', 'aday_ekle_4_nisa'), ('al_imran_metin_1', 'nisa_metin_1'), ('al_imran_kayit', 'nisa_kayit'),
      ('al_imran_kapanis', 'nisa_kapanis'), ('al_imran_paket_md', 'nisa_paket_md'), ('sure3_al_imran_okuma', 'sure4_nisa_okuma'),
      ('AX_al_imran', 'AX_nisa'), ('AS_al_imran', 'AS_nisa'), ('AL_IMRAN', 'NISA'),
      ('kok_ekle_3', 'kok_ekle_4'), ('duzeltme_3', 'duzeltme_4'), ('yama_retroaktif_gloss_3', 'yama_retroaktif_gloss_4'),
      ('uret_blok_3', 'uret_blok_4'), ('iskele_3', 'iskele_4'), ('Âl-i İmrân', 'Nisâ'), ('âl-i imrân', 'nisâ'),
      ('sûre 3', 'sûre 4'), ('Sûre 3', 'Sûre 4'), ('SÛRE 3', 'SÛRE 4'), ("_cipa_tablosu_3", "_cipa_tablosu_4"),
      ("_esma_profil_3", "_esma_profil_4"), ("'_profil_3'", "'_profil_4'"), ("okuma_metni['3']", "okuma_metni['4']"),
      ("mercek_kayit['3']", "mercek_kayit['4']")]


def adlar(t):
    for a, b in AD:
        t = t.replace(a, b)
    return t


T = {h: open(k, encoding='utf-8').read() for k, h in ESLEME}

# ---- kok_ekle_4: ISTEK boş
t = T['kok_ekle_4.py']
t = kes(t, 'ISTEK = [\n', '\n]\n',
        'ISTEK = [\n    # sûre 4 (Nisâ) — blok blok eklenir (2026-11-09); korpus geçişleri kok_envanteri ayet_sayisi ile\n]\n')
t = adlar(t)
i = t.index('ISTEK = ['); j = t.index('\n]\n', i) + 3
assert ast.literal_eval(t[i:j].split('=', 1)[1].strip()) == []
T['kok_ekle_4.py'] = t

# ---- nisa_metin_1: başlık + boş sözlükler
t = T['nisa_metin_1.py']
t = t[:t.index('MEAL = {}\nM = {}\n') + len('MEAL = {}\nM = {}\n')]
T['nisa_metin_1.py'] = adlar(t)

# ---- nisa_kayit: başlık + boş kayıt
t = T['nisa_kayit.py']
t = t[:t.index('\nS = 3\n')]
t += ('\nS = 4\n\n# Sûre 4\'ün eski ayet kaydı yok (okuma 1. ayetten). okuma_metni[\'4\']\'teki sekiz eski blok özeti dizgesi\n'
      '# (sıkıştırılmış dönem) bu dosyada YOK; kapanışta \'_eski_ozet\' altına taşınır (sûre 2 ve 3 emsali).\n'
      '\nCIPA = {}\n\nARIZA = {}\n\nDUZELTME = {}\n')
T['nisa_kayit.py'] = adlar(t)

# ---- uret_blok_4
t = T['uret_blok_4.py']
t = d(t, "S = 3\nMETIN = 'al_imran_metin_1'\nKAYIT = 'al_imran_kayit'\n", "S = 4\nMETIN = 'nisa_metin_1'\nKAYIT = 'nisa_kayit'\n")
t = kes(t, 'BLOKLAR = [', '\n}\n', 'BLOKLAR = []\nBASLIK = {\n}\n')
t = d(t, "# SÛRE 3 (iskele_3): S'nin kayıtlı ayetleri", "# SÛRE 4 (iskele_4): S'nin kayıtlı ayetleri")
t = d(t, "eski blok özeti anahtarları ('1-20' …, sıkıştırılmış dönem)", "eski blok özeti anahtarları ('1-20' … '141-176', sıkıştırılmış dönem)")
t = d(t, "# SÛRE 3: mercek_kayit['3']'te eski sıkıştırılmış ◇ notları var (52 not).",
         "# SÛRE 4: mercek_kayit['4']'te eski sıkıştırılmış ◇ notları var (19 not).")
T['uret_blok_4.py'] = adlar(t)

# ---- aday_ekle_4_nisa: AX / AS boş
t = T['aday_ekle_4_nisa.py']
t = kes(t, 'AL_IMRAN = [\n', '\n]\n', 'AL_IMRAN = [\n]\n')
t = kes(t, 'BAGLAR = {"AS_al_imran": [\n', '\n]}\n', 'BAGLAR = {"AS_al_imran": [\n]}\n')
T['aday_ekle_4_nisa.py'] = adlar(t)

# ---- duzeltme_4
t = T['duzeltme_4.py']
t = d(t, 'S = 3\n', 'S = 4\n')
T['duzeltme_4.py'] = adlar(t)

# ---- yama_retroaktif_gloss_4
t = T['yama_retroaktif_gloss_4.py']
t = d(t, 'if str(s) in OKUNAN and s != 3})', 'if str(s) in OKUNAN and s != 4})')
T['yama_retroaktif_gloss_4.py'] = adlar(t)

# ---- nisa_kapanis
t = T['nisa_kapanis.py']
t = re.sub(r"BLOK_LISTESI_ELLE = \[[^\]]*\]  # [^\n]*\n", '', t)
t = d(t, 'S, N = 3, 200\n', 'S, N = 4, 176\n')
t = d(t, "# SÛRE 3 (iskele_3): eski kayıt YOK. okuma_metni['3']'teki on eski blok özeti dizgesi ('1-20' …) içerik\n",
         "# SÛRE 4 (iskele_4): eski kayıt YOK. okuma_metni['4']'teki sekiz eski blok özeti dizgesi ('1-20' … '141-176') içerik\n")
t = d(t, "# aynen '_eski_ozet' altına taşınır (sûre 2 kapanış kararı emsali, 2026-11-08; silinen 0).\n",
         "# aynen '_eski_ozet' altına taşınır (sûre 2 ve 3 kapanış emsali; silinen 0).\n")
t = d(t, "'TAM SAYIM — sûre 3, 200 ayet'", "'TAM SAYIM — sûre 4, 176 ayet'")
t = d(t, "assert len(ESKI) == 10 and", "assert len(ESKI) == 8 and")
t = d(t, "I['not'] = \"Sûre 1, 2, 3, 9-114 TAM. Devam: sûre 4'ten.\"", "I['not'] = \"Sûre 1, 2, 3, 4, 9-114 TAM. Devam: sûre 5'ten.\"")
t = d(t, "I['son_oturum'] = 'OTURUM_PROMPT_sure3 (sûre 3 âl-i imrân sonu)'", "I['son_oturum'] = 'OTURUM_PROMPT_sure4 (sûre 4 nisâ sonu)'")
t = d(t, "'sûre 3 kaydı eksik — DUR'", "'sûre 4 kaydı eksik — DUR'")
t = d(t, "'sûre 3 anahtar sayısı — DUR'", "'sûre 4 anahtar sayısı — DUR'")
t = adlar(t)
assert 'BLOK_LISTESI_ELLE = ' not in t and "esma_kayit.py', str(S)" in t
T['nisa_kapanis.py'] = t

# ---- nisa_paket_md
t = T['nisa_paket_md.py']
t = re.sub(r"BLOK_LISTESI_ELLE = \[[^\]]*\]  # [^\n]*\n", '', t)
t = d(t, 'S = 3\n', 'S = 4\n')
t = d(t, '"# Sûre 3 (Âl-i İmrân) — hesaplamalı okuma, 200 ayet (TAM; blok başı kayıt)\\n\\n"',
         '"# Sûre 4 (Nisâ) — hesaplamalı okuma, 176 ayet (TAM; blok başı kayıt)\\n\\n"')
t = d(t, "`okuma_metni['3']['_bilanco']`", "`okuma_metni['4']['_bilanco']`")
t = d(t, "'\\n## Sûre 3 aday kaydı (AX_al_imran)", "'\\n## Sûre 4 aday kaydı (AX_al_imran)")
t = adlar(t)
assert 'BL = BLOK_LISTESI_ELLE\n' in t and 'BLOK_LISTESI_ELLE = ' not in t
T['nisa_paket_md.py'] = t

# ---- son denetimler
YASAK = ['al_imran', 'AL_IMRAN', 'Âl-i İmrân', 'âl-i imrân', '\nS = 3\n', 'kok_ekle_3', 'duzeltme_3', 'uret_blok_3',
         "'_profil_3'", '_esma_profil_3', '_cipa_tablosu_3', "okuma_metni['3']", "mercek_kayit['3']", 'sûre 3', 'Sûre 3']
for h, t in T.items():
    kalan = [y for y in YASAK if y in t]
    assert not kalan, 'sûre 3 izi kaldı: %s %s' % (h, kalan)
    open(h, 'w', encoding='utf-8').write(t)
    py_compile.compile(h, doraise=True)

sys.path.insert(0, C)
M = importlib.import_module('nisa_metin_1'); assert M.MEAL == {} and M.M == {}
K = importlib.import_module('nisa_kayit'); assert K.CIPA == {} and K.ARIZA == {} and K.DUZELTME == {} and K.S == 4
s = open('aday_ekle_4_nisa.py', encoding='utf-8').read()
assert 'NISA = [\n]\n' in s and 'BAGLAR = {"AS_nisa": [\n]}\n' in s and "1043'ten" in s
s = open('uret_blok_4.py', encoding='utf-8').read()
assert 'BLOKLAR = []\nBASLIK = {\n}\n' in s and "\nS = 4\n" in s and "assert S not in TAM" in s
assert open('nisa_kapanis.py', encoding='utf-8').read().count('BLOK_LISTESI_ELLE') == 3
assert open('nisa_paket_md.py', encoding='utf-8').read().count('BLOK_LISTESI_ELLE') == 1
print('iskele_4: %d dosya kuruldu' % len(T))
for k, h in ESLEME:
    print('  %-30s -> %s' % (k, h))
