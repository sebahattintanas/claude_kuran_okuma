# -*- coding: utf-8 -*-
"""iskele_3.py — sûre 3 (Âl-i İmrân) blok başı kayıt dosya ailesini sûre 2 (bakara_*) dosyalarından kurar.
OTURUM DIŞI (yükleme ağacına girmez). calisma/ içinde koşar. Kullanıcı kararı 2026-11-08 (adlar ve blok planı).

Kurallar (iskele_2 dersi):
  * dosya eşlemesi ayrı yazılır; kaynak != hedef, kaynak var, hedef yok — assert'li
  * genel '2 → 3' değişimi YOK: her dosyada yalnız çapalı (sayısı assert'li) değişimler
  * sûre 2'ye özgü onarımlar düşer: eski kayıt (sûre başı meal / not), KARAR_2_1_20, ESKI_KAYIT,
    'r['k'][0] == 2 and r['k'][1] <= 20' terimi; sûre 3'ün eski kayıtı YOK (okuma 1. ayetten)
  * korunan: S:A kapsam sayımı ('A-B' biçimli eski blok özeti anahtarları okuma sayılmaz — okuma_metni['3']'te
    on eski özet var), mercek_kayit['3'] eski ◇ notlarının '_sikistirilmis_eski' arşivi (52 not)
  * kok_ekle ISTEK, kayıt (CIPA / ARIZA / DUZELTME), metin sözlükleri, AX / AS, BLOKLAR / BASLIK boş — assert'li
  * kapanış / paket: BLOK_LISTESI_ELLE tanımsız (sûre sonunda elle); eski özet arşivi on anahtar
  * son denetim: hedef dosyalarda 'bakara', 'BAKARA', 'Bakara', 'S = 2', 'kok_ekle_2', 'duzeltme_2' kalmadı
"""
import os, re, ast, py_compile, importlib, sys

C = '/home/claude/calisma'
os.chdir(C)

ESLEME = [
    ('kok_ekle_2.py', 'kok_ekle_3.py'),
    ('bakara_metin_1.py', 'al_imran_metin_1.py'),
    ('bakara_kayit.py', 'al_imran_kayit.py'),
    ('uret_blok_2.py', 'uret_blok_3.py'),
    ('aday_ekle_2_bakara.py', 'aday_ekle_3_al_imran.py'),
    ('duzeltme_2.py', 'duzeltme_3.py'),
    ('yama_retroaktif_gloss_2.py', 'yama_retroaktif_gloss_3.py'),
    ('bakara_kapanis.py', 'al_imran_kapanis.py'),
    ('bakara_paket_md.py', 'al_imran_paket_md.py'),
]
for k, h in ESLEME:
    assert k != h and os.path.exists(k) and not os.path.exists(h), (k, h)


def d(t, eski, yeni, adet=1):
    assert t.count(eski) == adet, 'çapa sayısı %d (beklenen %d): %r' % (t.count(eski), adet, eski[:90])
    return t.replace(eski, yeni)


def kes(t, bas, son, yeni):
    """bas ile başlayan, son ile biten (ilk eşleşme) bölümü yeni ile değiştirir"""
    i = t.index(bas); j = t.index(son, i) + len(son)
    return t[:i] + yeni + t[j:]


T = {h: open(k, encoding='utf-8').read() for k, h in ESLEME}

# ---- kok_ekle_3: ISTEK boş
t = T['kok_ekle_3.py']
t = d(t, 'sûre 2 (Bakara) blokları', 'sûre 3 (Âl-i İmrân) blokları')
t = kes(t, 'ISTEK = [\n', '\n]\n',
        'ISTEK = [\n    # sûre 3 (Âl-i İmrân) — blok blok eklenir (2026-11-08); korpus geçişleri kok_envanteri ayet_sayisi ile\n]\n')
i = t.index('ISTEK = ['); j = t.index('\n]\n', i) + 3
assert ast.literal_eval(t[i:j].split('=', 1)[1].strip()) == []
T['kok_ekle_3.py'] = t

# ---- al_imran_metin_1: başlık + boş sözlükler
t = T['al_imran_metin_1.py']
t = t[:t.index('MEAL = {}\nM = {}\n') + len('MEAL = {}\nM = {}\n')]
t = d(t, 'bakara_metin_1.py — sûre 2 (Bakara, 21. ayetten) meal', 'al_imran_metin_1.py — sûre 3 (Âl-i İmrân) meal')
T['al_imran_metin_1.py'] = t

# ---- al_imran_kayit: başlık + boş kayıt
t = T['al_imran_kayit.py']
t = t[:t.index('\nS = 2\n')]
t = d(t, 'bakara_kayit.py — sûre 2 (Bakara) okumasının', 'al_imran_kayit.py — sûre 3 (Âl-i İmrân) okumasının')
t += ('\nS = 3\n\n# Sûre 3\'ün eski kaydı yok (okuma 1. ayetten). okuma_metni[\'3\']\'teki on eski blok özeti dizgesi\n'
      '# (sıkıştırılmış dönem) bu dosyada YOK; kapanışta \'_eski_ozet\' altına taşınır (sûre 2 kararı emsali).\n'
      '\nCIPA = {}\n\nARIZA = {}\n\nDUZELTME = {}\n')
T['al_imran_kayit.py'] = t

# ---- uret_blok_3
t = T['uret_blok_3.py']
t = d(t, 'uret_blok_2.py — sûre 2 (Bakara) blok', 'uret_blok_3.py — sûre 3 (Âl-i İmrân) blok')
t = d(t, "S = 2\nMETIN = 'bakara_metin_1'\nKAYIT = 'bakara_kayit'\n", "S = 3\nMETIN = 'al_imran_metin_1'\nKAYIT = 'al_imran_kayit'\n")
t = kes(t, 'BLOKLAR = [', '\n}\n', 'BLOKLAR = []\nBASLIK = {\n}\n')
t = d(t, ("# SÛRE 2 ONARIMI (iskele_2): S'nin kayıtlı ayetleri 'S:A' ve eski birleşik 'S:A-B' anahtarlarından\n"
          "# (eski kayıt 1-20: iki birleşik anahtar). 'A-B' biçimli eski blok özeti anahtarları okuma SAYILMAZ.\n"
          "# 2:1-20 bu kümenin içinde olduğu için ayrıca eklenmez — çift sayım yok (şablonun 2:1-20 terimi kaldırıldı).\n"),
         ("# SÛRE 3 (iskele_3): S'nin kayıtlı ayetleri 'S:A' anahtarlarından ('S:A-B' birleşik biçimi de tanınır);\n"
          "# 'A-B' biçimli eski blok özeti anahtarları ('1-20' …, sıkıştırılmış dönem) okuma SAYILMAZ.\n"))
t = d(t, "OM['ilerleme']['kismi'][str(S)] = '1-%%d ayet düzeyinde (1-20 eski kayıt + 21-%%d blok başı kayıt; %%d ayet)' %% (oku_S[-1], oku_S[-1], len(oku_S))\n",
         "OM['ilerleme']['kismi'][str(S)] = '1-%%d ayet düzeyinde (blok başı kayıt; %%d ayet)' %% (oku_S[-1], len(oku_S))\n")
t = d(t, "# SÛRE 2: mercek_kayit['2']'de eski sıkıştırılmış ◇ notları var (2:22, 2:24 …). Üstüne yazmadan önce\n",
         "# SÛRE 3: mercek_kayit['3']'te eski sıkıştırılmış ◇ notları var (52 not). Üstüne yazmadan önce\n")
assert "r['k'][1] <= 20" not in t and '2:1-20' not in t
T['uret_blok_3.py'] = t

# ---- aday_ekle_3_al_imran: AX / AS boş
t = T['aday_ekle_3_al_imran.py']
t = d(t, 'aday_ekle_2_bakara.py — sûre 2 (Bakara) adayları (AX_bakara) ve okuma bağları (AS_bakara).',
         'aday_ekle_3_al_imran.py — sûre 3 (Âl-i İmrân) adayları (AX_al_imran) ve okuma bağları (AS_al_imran).')
t = d(t, "havuzun sonundan devam eder (1042'den)", "havuzun sonundan devam eder (1043'ten)")
t = kes(t, 'BAKARA = [\n', '\n]\n', 'AL_IMRAN = [\n]\n')
t = kes(t, 'BAGLAR = {"AS_bakara": [\n', '\n]}\n', 'BAGLAR = {"AS_al_imran": [\n]}\n')
t = d(t, "AD.pop('AX_bakara', None)", "AD.pop('AX_al_imran', None)")
t = d(t, "nos = [x['no'] for x in BAKARA]", "nos = [x['no'] for x in AL_IMRAN]")
t = d(t, "AD['AX_bakara'] = BAKARA", "AD['AX_al_imran'] = AL_IMRAN")
t = d(t, "print('AX_bakara', len(BAKARA),", "print('AX_al_imran', len(AL_IMRAN),")
t = d(t, "print('okuma_baglantilari: AS_bakara', len(BAGLAR['AS_bakara']))",
         "print('okuma_baglantilari: AS_al_imran', len(BAGLAR['AS_al_imran']))")
T['aday_ekle_3_al_imran.py'] = t

# ---- duzeltme_3
t = T['duzeltme_3.py']
t = d(t, 'duzeltme_2.py — sûre 2 okumasında', 'duzeltme_3.py — sûre 3 okumasında')
t = d(t, "(bakara_kayit.DUZELTME'den)", "(al_imran_kayit.DUZELTME'den)")
t = d(t, 'from bakara_kayit import DUZELTME\nS = 2\n', 'from al_imran_kayit import DUZELTME\nS = 3\n')
T['duzeltme_3.py'] = t

# ---- yama_retroaktif_gloss_3
t = T['yama_retroaktif_gloss_3.py']
t = d(t, 'yama_retroaktif_gloss_2.py — sûre 2 okumasında eklenen kökler (kok_ekle_2.ISTEK',
         'yama_retroaktif_gloss_3.py — sûre 3 okumasında eklenen kökler (kok_ekle_3.ISTEK')
t = d(t, "open('kok_ekle_2.py'", "open('kok_ekle_3.py'")
t = d(t, "print('sûre 2 yeni kök:'", "print('sûre 3 yeni kök:'")
t = d(t, 'if str(s) in OKUNAN and s != 2})', 'if str(s) in OKUNAN and s != 3})')
T['yama_retroaktif_gloss_3.py'] = t

# ---- al_imran_kapanis
t = T['al_imran_kapanis.py']
t = d(t, 'bakara_kapanis.py — sûre 2 (Bakara) BAKARA SONU', 'al_imran_kapanis.py — sûre 3 (Âl-i İmrân) SÛRE SONU')
t = d(t, '(defter.json · esma_kayit.json · bakara_kayit.py · cipa_tarama4_adaylari.json)',
         '(defter.json · esma_kayit.json · al_imran_kayit.py · cipa_tarama4_adaylari.json)')
t = d(t, 'İlerleme eski kuralla: TAM sûreler + 2:1-20 (secde_kapanis ile aynı), elle artırma YOK.',
         'İlerleme: TAM sûreler (sûre 2 artık TAM; 2:1-20 terimi yok), elle artırma YOK.')
t = d(t, 'from bakara_kayit import CIPA\n', 'from al_imran_kayit import CIPA\n')
i = t.index('# SÛRE 2 (iskele_2): 2:1-20 eski kaydı'); j = t.index('# önkoşul: esmâ kaydı')
t = t[:i] + ('# SÛRE 3 (iskele_3): eski kayıt YOK. okuma_metni[\'3\']\'teki on eski blok özeti dizgesi (\'1-20\' …) içerik\n'
             '# aynen \'_eski_ozet\' altına taşınır (sûre 2 kapanış kararı emsali, 2026-11-08; silinen 0).\n'
             '# BLOK_LISTESI_ELLE sûre sonunda elle doldurulur (uret_blok_3.BLOKLAR ile birebir).\n') + t[j:]
t = d(t, 'for a, b in [ESKI_KAYIT] + BLOK_LISTESI_ELLE:', 'for a, b in BLOK_LISTESI_ELLE:')
t = d(t, 'S, N = 2, 286\n', 'S, N = 3, 200\n')
t = d(t, "'TAM SAYIM — sûre 2, 286 ayet'", "'TAM SAYIM — sûre 3, 200 ayet'")
t = d(t, "assert len(ESKI) == 7 and", "assert len(ESKI) == 10 and")
t = d(t, "assert len([k for k in OM[str(S)] if not k.startswith('_')]) == N - 2, 'sûre 2 anahtar sayısı (iki birleşik eski anahtar) — DUR'\n",
         "assert len([k for k in OM[str(S)] if not k.startswith('_')]) == N, 'sûre 3 anahtar sayısı — DUR'\n")
t = d(t, "assert kap == set(range(1, N + 1)), 'sûre 2 kaydı eksik — DUR'", "assert kap == set(range(1, N + 1)), 'sûre 3 kaydı eksik — DUR'")
t = d(t, "I.get('bekleyen', {}).pop(str(S), None)\n",
         "I.get('bekleyen', {}).pop(str(S), None)\nI['sikistirilmis'] = [x for x in I.get('sikistirilmis', []) if x != S]\n")
t = d(t, "okunan = sum(1 for r in D.values() if r['k'][0] in set(I['tam']) or (r['k'][0] == 2 and r['k'][1] <= 20))",
         "okunan = sum(1 for r in D.values() if r['k'][0] in set(I['tam']))")
t = d(t, "I['not'] = \"Sûre 1, 2, 9-114 TAM. Devam: sûre 3'ten.\"", "I['not'] = \"Sûre 1, 2, 3, 9-114 TAM. Devam: sûre 4'ten.\"")
t = d(t, "I['son_oturum'] = 'OTURUM_PROMPT_sure3_1.md (sûre 2 bakara sonu)'", "I['son_oturum'] = 'OTURUM_PROMPT_sure3 (sûre 3 âl-i imrân sonu)'")
t = d(t, "open('bakara_kapanis_notu.txt'", "open('al_imran_kapanis_notu.txt'")
t = d(t, "KAP = {'_bilanco_sure': bil, '_cipa_tablosu_2': cipa, '_esma_profil_2': esma, '_kapanis_notu': NOT}",
         "KAP = {'_bilanco_sure': bil, '_cipa_tablosu_3': cipa, '_esma_profil_3': esma, '_kapanis_notu': NOT}")
t = d(t, "subprocess.run([sys.executable, 'duzeltme_2.py'], check=True)", "subprocess.run([sys.executable, 'duzeltme_3.py'], check=True)")
t = d(t, "E['_profil_2'] = esma", "E['_profil_3'] = esma")
t = d(t, "'kesinlik': '%d/%d' % (sum(1 for a in tar if CIPA.get(int(a.split(':')[1]), {}).get('cipa')), len(tar)),",
         "'kesinlik': '%d/%d' % (sum(1 for a in tar if CIPA.get(int(a.split(':')[1]), {}).get('cipa')), len(tar)),")
# BLOK_LISTESI_ELLE literal'i (sûre 2'nin) kaldırılır — sûre 3 sonunda yazılır
t = re.sub(r'ESKI_KAYIT = \(1, 20\)\nBLOK_LISTESI_ELLE = \[[^\]]*\]\n', '', t)
assert 'ESKI_KAYIT' not in t and 'KARAR_2_1_20' not in t and 'BLOK_LISTESI_ELLE = ' not in t
T['al_imran_kapanis.py'] = t

# ---- al_imran_paket_md
t = T['al_imran_paket_md.py']
t = d(t, 'bakara_paket_md.py — sûre 2 (Bakara) TAM okumasının', 'al_imran_paket_md.py — sûre 3 (Âl-i İmrân) TAM okumasının')
t = d(t, 'S = 2\n', 'S = 3\n')
t = re.sub(r'BLOK_LISTESI_ELLE = \[[^\]]*\]\n', '', t)
assert 'BL = BLOK_LISTESI_ELLE\n' in t
i = t.index('# eski kayıt (meal / not, aynen'); j = t.index('for a, b in BL:\n')
t = t[:i] + t[j:]
t = d(t, '"# Sûre 2 (Bakara) — hesaplamalı okuma, 286 ayet (TAM; 1-20 eski kayıt, bloklar 21-286)\\n\\n"',
         '"# Sûre 3 (Âl-i İmrân) — hesaplamalı okuma, 200 ayet (TAM; blok başı kayıt)\\n\\n"')
t = d(t, "'bakara_metin_1'", "'al_imran_metin_1'")
t = d(t, "`okuma_metni['2']['_bilanco']`", "`okuma_metni['3']['_bilanco']`")
t = d(t, "_cipa_tablosu_2", "_cipa_tablosu_3", 2)
t = d(t, "_esma_profil_2", "_esma_profil_3", 2)
t = d(t, "'\\n## Sûre 2 aday kaydı (AX_bakara)\\n\\n```json\\n%s\\n```\\n' % json.dumps(A['AX_bakara']",
         "'\\n## Sûre 3 aday kaydı (AX_al_imran)\\n\\n```json\\n%s\\n```\\n' % json.dumps(A['AX_al_imran']")
t = d(t, "notlar/sure2_bakara_okuma.md", "notlar/sure3_al_imran_okuma.md")
T['al_imran_paket_md.py'] = t

# ---- son denetimler
YASAK = ['bakara', 'BAKARA', 'Bakara', '\nS = 2\n', 'kok_ekle_2', 'duzeltme_2', "'_profil_2'", '_esma_profil_2', '_cipa_tablosu_2']
for h, t in T.items():
    kalan = [y for y in YASAK if y in t]
    assert not kalan, 'sûre 2 izi kaldı: %s %s' % (h, kalan)
    open(h, 'w', encoding='utf-8').write(t)
    py_compile.compile(h, doraise=True)

sys.path.insert(0, C)
M = importlib.import_module('al_imran_metin_1'); assert M.MEAL == {} and M.M == {}
K = importlib.import_module('al_imran_kayit'); assert K.CIPA == {} and K.ARIZA == {} and K.DUZELTME == {} and K.S == 3
s = open('aday_ekle_3_al_imran.py', encoding='utf-8').read()
assert 'AL_IMRAN = [\n]\n' in s and 'BAGLAR = {"AS_al_imran": [\n]}\n' in s
s = open('uret_blok_3.py', encoding='utf-8').read()
assert 'BLOKLAR = []\nBASLIK = {\n}\n' in s and "\nS = 3\n" in s and "assert S not in TAM" in s
assert open('al_imran_kapanis.py', encoding='utf-8').read().count('BLOK_LISTESI_ELLE') == 3
assert open('al_imran_paket_md.py', encoding='utf-8').read().count('BLOK_LISTESI_ELLE') == 1
print('iskele_3: %d dosya kuruldu' % len(T))
for k, h in ESLEME:
    print('  %-30s -> %s' % (k, h))
