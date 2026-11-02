# -*- coding: utf-8 -*-
"""iskele_2.py — sûre 2 (Bakara, 21. ayetten) blok başı kayıt dosya ailesini nas_* (sûre 114) şablonlarından kurar.
OTURUM DIŞI (yükleme ağacına girmez). calisma/ içinde koşar.

Kurallar (oturum protokolü §3):
  * dosya eşlemesi ayrı yazılır; kaynak != hedef, kaynak var, hedef yok — assert'li (sûre 111 dersi)
  * ad değişimi harf sınırlı, yalnız nas -> bakara (NAS -> BAKARA, Nas -> Bakara); 'nasr' ve Latin 'en-nâs' etkilenmez
  * numara değişimi 114 -> 2 rakam sınırıyla; ÖNCE sayısal sabitler (round(...)) maskelenir; mevcut '2:1-20' ve
    "r['k'][0] == 2" geçişleri genel değişimden önce ve sonra sayılır
  * uret_blok ilerleme formülü onarımı: 2:1-20 terimi ile S terimi birleşir (çift sayım yok); kısmi aralık doğrulanır
  * 'sûre S zaten TAM' assert'i korunur
  * kok_ekle ISTEK, kayıt (CIPA / ARIZA / DUZELTME), metin sözlükleri, AX / AS boş — assert'li; BLOKLAR / BASLIK boş
  * kapanış (2 yer) ve paket (1 yer) blok listesi BLOK_LISTESI_ELLE; S, N = 2, 286; etiket '286 ayet'
  * I['not'] genel değişimden SONRA açıkça yazılır; 'eski numara kalmadı' denetimi o satırı hariç tutar
"""
import os, re, ast, py_compile

C = '/home/claude/calisma'
os.chdir(C)

ESLEME = [
    ('kok_ekle_114.py', 'kok_ekle_2.py'),
    ('nas_metin_1.py', 'bakara_metin_1.py'),
    ('nas_kayit.py', 'bakara_kayit.py'),
    ('uret_blok_114.py', 'uret_blok_2.py'),
    ('aday_ekle_114_nas.py', 'aday_ekle_2_bakara.py'),
    ('duzeltme_114.py', 'duzeltme_2.py'),
    ('yama_retroaktif_gloss_114.py', 'yama_retroaktif_gloss_2.py'),
    ('nas_kapanis.py', 'bakara_kapanis.py'),
    ('nas_paket_md.py', 'bakara_paket_md.py'),
]
for k, h in ESLEME:
    assert k != h, 'kaynak = hedef: %s' % k
    assert os.path.exists(k), 'kaynak yok: %s' % k
    assert not os.path.exists(h), 'hedef zaten var: %s' % h
assert len({h for _, h in ESLEME}) == len(ESLEME)

HARF = r'[^\W\d_]'
AD_RX = [(re.compile(r'(?<!%s)nas(?!%s)' % (HARF, HARF)), 'bakara'),
         (re.compile(r'(?<!%s)NAS(?!%s)' % (HARF, HARF)), 'BAKARA'),
         (re.compile(r'(?<!%s)Nas(?!%s)' % (HARF, HARF)), 'Bakara')]
NO_RX = re.compile(r'(?<!\d)114(?!\d)')
MASKE_RX = re.compile(r'round\([^()]*\([^()]*\)[^()]*\)|round\([^()]*\)')


def genel(t):
    once = (t.count('2:1-20'), t.count("r['k'][0] == 2"), len(re.findall(r'(?<!\d)2(?!\d)', t)))
    maske = {}
    def _m(m):
        anahtar = '\x00M%d\x00' % len(maske); maske[anahtar] = m.group(0); return anahtar
    t = MASKE_RX.sub(_m, t)
    for rx, y in AD_RX:
        t = rx.sub(y, t)
    n114 = len(NO_RX.findall(t))
    t = NO_RX.sub('2', t)
    for a, v in maske.items():
        t = t.replace(a, v)
    sonra = (t.count('2:1-20'), t.count("r['k'][0] == 2"))
    assert sonra == once[:2], 'mevcut 2 geçişleri bozuldu: %s -> %s' % (once[:2], sonra)
    assert len(re.findall(r'(?<!\d)2(?!\d)', t)) == once[2] + n114, 'rakam 2 sayısı tutmuyor'
    assert not maske or all(v in t for v in maske.values()), 'maske geri konmadı'
    return t


def degistir(t, eski, yeni, adet=1):
    assert t.count(eski) == adet, 'çapa sayısı %d (beklenen %d): %r' % (t.count(eski), adet, eski[:80])
    return t.replace(eski, yeni)


T = {h: genel(open(k, encoding='utf-8').read()) for k, h in ESLEME}

# ---- kok_ekle_2: ISTEK boş
t = T['kok_ekle_2.py']
i = t.index('ISTEK = ['); j = t.index('\n]\n', i) + 3
assert ast.literal_eval(t[i:j].split('=', 1)[1].strip()) == [], 'ISTEK boş değil'
t = degistir(t, "# sûre 2 (Bakara) — blok blok eklenir (2026-11-01)",
             "# sûre 2 (Bakara, 21. ayetten) — blok blok eklenir (2026-11-01)")
T['kok_ekle_2.py'] = t

# ---- bakara_metin_1: sözlükler boş
t = T['bakara_metin_1.py']
t = t[:t.index('MEAL = {}\nM = {}\n') + len('MEAL = {}\nM = {}\n')]
t = degistir(t, 'sûre 2 (Bakara) meal', 'sûre 2 (Bakara, 21. ayetten) meal')
T['bakara_metin_1.py'] = t

# ---- bakara_kayit: CIPA / ARIZA / DUZELTME boş
t = T['bakara_kayit.py']
t = t[:t.index('\nS = 2\n') + len('\nS = 2\n')]
t += ('\n# Sûre 2 eski kaydı (2:1-20 meal / not; okuma_metni[\'2\'] eski blok özeti anahtarları) bu dosyada YOK —\n'
      '# kapanışla birleşimi karar bekliyor (bekleyenler; bakara_kapanis.py KARAR_2_1_20).\n'
      '\nCIPA = {}\n\nARIZA = {}\n\nDUZELTME = {}\n')
T['bakara_kayit.py'] = t

# ---- aday_ekle_2_bakara: AX / AS boş
t = T['aday_ekle_2_bakara.py']
t = degistir(t, 'BAKARA = [\n]\n', 'BAKARA = [\n]\n')
i = t.index('BAGLAR = {"AS_bakara": ['); j = t.index('\n]}\n', i) + 4
t = t[:i] + 'BAGLAR = {"AS_bakara": [\n]}\n' + t[j:]
T['aday_ekle_2_bakara.py'] = t

# ---- uret_blok_2: BLOKLAR / BASLIK boş, ilerleme formülü onarımı, mercek arşivi
t = T['uret_blok_2.py']
i = t.index('BLOKLAR = ['); j = t.index('\n}\n', i) + 3
t = t[:i] + 'BLOKLAR = []\nBASLIK = {\n}\n' + t[j:]
ESKI_ILER = (
    "oku_S = sorted(int(k.split(':')[1]) for k in OM[str(S)] if not k.startswith('_'))\n"
    "OM['ilerleme']['kismi'][str(S)] = '%%d-%%d ayet düzeyinde (blok başı kayıt; %%d ayet)' %% (oku_S[0], oku_S[-1], len(oku_S))\n"
    "# eski kural aynen korunur (secde_kapanis): TAM sûreler + 2:1-20; üstüne yalnız S'nin kayıtlı ayetleri\n"
    "okunan = (sum(1 for r in D if r['k'][0] in TAM or (r['k'][0] == 2 and r['k'][1] <= 20))\n"
    "          + sum(1 for r in D if r['k'][0] == S and r['k'][1] in set(oku_S)))\n")
YENI_ILER = (
    "# SÛRE 2 ONARIMI (iskele_2): S'nin kayıtlı ayetleri 'S:A' ve eski birleşik 'S:A-B' anahtarlarından\n"
    "# (eski kayıt 1-20: iki birleşik anahtar). 'A-B' biçimli eski blok özeti anahtarları okuma SAYILMAZ.\n"
    "# 2:1-20 bu kümenin içinde olduğu için ayrıca eklenmez — çift sayım yok (şablonun 2:1-20 terimi kaldırıldı).\n"
    "oku_S = set()\n"
    "for k in OM[str(S)]:\n"
    "    m = re.fullmatch(r'%%d:(\\d+)(?:-(\\d+))?' %% S, k)\n"
    "    if m:\n"
    "        oku_S.update(range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1))\n"
    "oku_S = sorted(oku_S)\n"
    "assert oku_S == list(range(1, oku_S[-1] + 1)), 'sûre %%d kayıtlı ayetleri kesintili — DUR' %% S\n"
    "OM['ilerleme']['kismi'][str(S)] = '1-%%d ayet düzeyinde (1-20 eski kayıt + 21-%%d blok başı kayıt; %%d ayet)' %% (oku_S[-1], oku_S[-1], len(oku_S))\n"
    "okunan = (sum(1 for r in D if r['k'][0] in TAM)\n"
    "          + sum(1 for r in D if r['k'][0] == S and r['k'][1] in set(oku_S)))\n")
t = degistir(t, ESKI_ILER, YENI_ILER)
ESKI_MK = ("for n in range(A1, A2 + 1):\n"
           "    MK[str(S)]['%%d:%%d' %% (S, n)] = gloss_gecis.gecir(M[n])\n")
YENI_MK = ("# SÛRE 2: mercek_kayit['2']'de eski sıkıştırılmış ◇ notları var (2:22, 2:24 …). Üstüne yazmadan önce\n"
           "# '_sikistirilmis_eski' altına bir kez arşivlenir (blok ilk kez yazılırken; yeniden koşuda arşivlenmez).\n"
           "for n in range(A1, A2 + 1):\n"
           "    k = '%%d:%%d' %% (S, n)\n"
           "    if k not in OM_ONCE and k in MK[str(S)]:\n"
           "        MK[str(S)].setdefault('_sikistirilmis_eski', {}).setdefault(k, MK[str(S)][k])\n"
           "    MK[str(S)][k] = gloss_gecis.gecir(M[n])\n")
t = degistir(t, ESKI_MK, YENI_MK)
t = degistir(t, "OM.setdefault(str(S), {})\n", "OM.setdefault(str(S), {})\nOM_ONCE = set(OM[str(S)])\n")
T['uret_blok_2.py'] = t

# ---- bakara_kapanis: blok listesi 2 yer, S/N, etiket, 2:1-20 karar kalkanı, bekleyen
t = T['bakara_kapanis.py']
t = degistir(t, 'for a, b in [(1, 6)]:\n    subprocess', 'for a, b in BLOK_LISTESI_ELLE:\n    subprocess')
t = degistir(t, 'for a, b in [(1, 6)] for k, v', 'for a, b in BLOK_LISTESI_ELLE for k, v')
t = degistir(t, 'S, N = 2, 6\n', 'S, N = 2, 286\n')
t = degistir(t, "'TAM SAYIM — sûre 2, 6 ayet'", "'TAM SAYIM — sûre 2, 286 ayet'")
t = degistir(t, "import subprocess, sys\n",
             "import subprocess, sys\n"
             "# SÛRE 2 (iskele_2): 2:1-20 eski kaydı ('S:A' + iki birleşik 'S:A-B' anahtarı, yalnız meal / not; olcum,\n"
             "# mercek, dikey, esma, _bilanco YOK; esma_kayit'ta 2:1-20 yok) ve okuma_metni['2'] eski blok özeti\n"
             "# anahtarları ('21-60' …) kapanışla nasıl birleşecek — KARAR BEKLİYOR (bekleyenler). Aşağıdaki kayıt sayısı\n"
             "# assert'i ve esmâ profili bu karar olmadan tutmaz. Karar verilmeden kapanış (--kuru dahil) koşulmaz.\n"
             "KARAR_2_1_20 = None\n"
             "assert KARAR_2_1_20 is not None, 'sûre 2:1-20 eski kayıt birleşimi karara bağlanmadı — DUR'\n")
t = degistir(t, "I['kismi'].pop(str(S), None)\n", "I['kismi'].pop(str(S), None)\nI.get('bekleyen', {}).pop(str(S), None)\n")
satir = [l for l in t.split('\n') if l.startswith("I['not'] = ")]
assert len(satir) == 1
t = t.replace(satir[0], "I['not'] = \"Sûre 1, 2, 9-114 TAM. Devam: sûre 3'ten.\"")   # genel değişimden SONRA
for p in ("'_cipa_tablosu_2'", "'_esma_profil_2'", "E['_profil_2']", "'bakara_kapanis_notu.txt'", "'duzeltme_2.py'"):
    assert p in t, 'profil / ad anahtarı yok: %s' % p
T['bakara_kapanis.py'] = t

# ---- bakara_paket_md: blok listesi 1 yer, başlık
t = T['bakara_paket_md.py']
t = degistir(t, 'BL = [(1, 6)]\n', 'BL = BLOK_LISTESI_ELLE\n')
t = degistir(t, 'hesaplamalı okuma, 6 ayet (TAM)', 'hesaplamalı okuma, 286 ayet (TAM; 1-20 eski kayıt, bloklar 21-286)')
for p in ("'_cipa_tablosu_2'", "'_esma_profil_2'", "A['AX_bakara']", 'sure2_bakara_okuma.md'):
    assert p in t, 'paket anahtarı yok: %s' % p
T['bakara_paket_md.py'] = t

# ---- son denetimler
for h, t in T.items():
    for rx, _ in AD_RX:
        assert not rx.search(t), 'eski ad kaldı: %s' % h
    kalan = [l for l in t.split('\n') if NO_RX.search(l) and not l.startswith("I['not'] = ")]
    assert not kalan, 'eski numara kaldı: %s %s' % (h, kalan[:2])
    assert 'felak' not in t and 'nasr' not in t, h
    open(h, 'w', encoding='utf-8').write(t)
    py_compile.compile(h, doraise=True)

import importlib, sys
sys.path.insert(0, C)
M = importlib.import_module('bakara_metin_1'); assert M.MEAL == {} and M.M == {}
K = importlib.import_module('bakara_kayit'); assert K.CIPA == {} and K.ARIZA == {} and K.DUZELTME == {} and K.S == 2
s = open('aday_ekle_2_bakara.py', encoding='utf-8').read()
assert 'BAKARA = [\n]\n' in s and 'BAGLAR = {"AS_bakara": [\n]}\n' in s
s = open('uret_blok_2.py', encoding='utf-8').read()
assert 'BLOKLAR = []\nBASLIK = {\n}\n' in s and "S = 2\n" in s and "assert S not in TAM" in s
assert "r['k'][0] == 2 and r['k'][1] <= 20" not in s
assert s.count('BLOK_LISTESI_ELLE') == 0
assert open('bakara_kapanis.py', encoding='utf-8').read().count('BLOK_LISTESI_ELLE') == 2
assert open('bakara_paket_md.py', encoding='utf-8').read().count('BLOK_LISTESI_ELLE') == 1
print('iskele_2: %d dosya kuruldu' % len(T))
for k, h in ESLEME:
    print('  %-30s -> %s' % (k, h))
