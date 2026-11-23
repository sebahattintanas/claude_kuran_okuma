# sûre 6 blok 37 (6:151-152) ARIZA oluşturucu — bölüm 18-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b37/olcum.txt'
os.environ['SAY2'] = '/home/claude/b37/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b36.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {}
BOL = "'Gelin okuyayım; dosdoğru yol; Mûsâ'ya Kitap'"


def sd(key):
    return sayim.S2[key][1]


def sic(key):
    n, d = sayim.S2[key]
    return 1 + len([x for x in d['basilan'] if x.startswith('6:')]) + d['okunmus_si'] + d['henuz_si']


def taban(key, ay):
    n, d = sayim.S2[key]
    p = [ay] + [x for x in d['basilan'] if x.startswith('6:') and x != ay]
    if d['okunmus_si']: p.append('okunmus_si %d' % d['okunmus_si'])
    if d['henuz_si']: p.append('henuz_si %d' % d['henuz_si'])
    return ' + '.join(p)


R5 = [
 ("6:151", "'zâ vassâ _ le'alle'", 3, 'say 6:151 38-41', "harekesiz 'zâlikum vassâkum bihî le'allekum' (38-41. kelime)", None),
 ("6:152", "'zâ vassâ _ le'alle'", 3, 'say 6:152 31-34', "harekesiz 'zâlikum vassâkum bihî le'allekum' (31-34. kelime)", None),
]
r5 = []
for ay, kal, nk, key, ad, dz, *tr_ in R5:
    s = sic(key)
    h = "%s nakarat3 %s %d (tür %s) / %s sûre içi %d (%s)" % (ay, kal, nk, (tr_[0] if tr_ else 'ic'), ad, s, taban(key, ay))  # bölüm 11 denetimi kuralı 3
    if s == nk:
        h += ' — tutuyor'
    else:
        dk, dad, dar, ger = dz
        ds = sic(dk)
        if ds == nk:
            h += " — tutmuyor; eşit aralıkla lemma dizisi '%s' (%s. kelime) sûre içi %d (%s) — tutuyor; gerekçe %s" % (dad, dar, ds, taban(dk, ay), ger)
        else:
            h += " — tutmuyor; eşit aralıkla lemma dizisi '%s' (%s. kelime) sûre içi %d (%s) — tutmuyor; gerekçe %s" % (dad, dar, ds, taban(dk, ay), ger)
    r5.append(h)

K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k and not (k + ' --medde' in sayim.S2 and sayim.S2[k + ' --medde'][0] != n)}  # sûre 6 bölüm 5 denetimi kuralı 6 (TEKIL_MEDDE)

VF_YAZI = {151: {12: "'ve bi'l-vâlideyni'", 14: "'ve lâ'", 21: "'ve iyyâhum'", 22: "'ve lâ'", 28: "'ve mâ'", 30: "'ve lâ'"}, 152: {1: "'ve lâ'", 12: "'ve evfu'", 14: "'ve'l-mîzâne'", 21: "'ve izâ'", 24: "'ve lev'", 28: "'ve bi-'ahdi'"}}
sys.path.insert(0, '/home/claude/b37/yap')
from seg import meals
MEALS = meals()


def _bol(s, sep):
    out, d, cur, i = [], 0, '', 0
    while i < len(s):
        c = s[i]
        if c == '(': d += 1
        elif c == ')': d -= 1
        if d == 0 and s.startswith(sep, i):
            out.append(cur); cur = ''; i += len(sep); continue
        cur += c; i += 1
    out.append(cur)
    return out


MK = {}
for blok in MEALS:
    n = int(blok.split(' ', 1)[0].split(':')[1]); govde = blok.split(' ', 1)[1]
    for seg in _bol(govde, "; '"):
        seg = seg if seg.startswith("'") else "'" + seg
        j = seg.index("' (")
        tr = seg[1:j]; ic = seg[j + 3:].rstrip(')')
        parca = _bol(ic, ', ')
        MK.setdefault(n, []).append((tr, parca[0].strip("'"), parca[1:]))
open('/home/claude/b37/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '37')
BLOKLAR = [str(i) for i in range(1, 38)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '37', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b37/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '151', '152', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b37/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b37/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '151', '152', '37').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_151_152.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:151', '6:152'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_151_152.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(151, 153))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:151 kök ولد ('l-vâlideyni' 12. kelime — ana baba; 'evlâdekum' 16. kelime — çocuk), kök قتل ('taqtulû' 15. kelime — öldürme), kök ملق ('imlâq' 18. kelime — yoksulluk), kök نفس ('n-nefse' 32. kelime — can), kök ظهر ('zahera' 26. kelime — açık olma), kök بطن ('batan' 29. kelime — gizli olma); 6:152 kök يتم ('l-yetîmi' 4. kelime — yetim), kök شدد ('eşuddeh' 11. kelime — rüşt), kök كيل ('l-keyle' 13. kelime — ölçü), kök وزن ('l-mîzâne' 14. kelime — tartı), kök نفس ('nefsen' 18. kelime — can), kök قرب ('qurbâ' 27. kelime — akrabalık): tetik listesinde yok; 6:152 'izâ' (21. kelime — morph T, zaman)"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '151', '152', '37')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b37/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 38)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(151, 153))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 17 kapanışında sunum/bolum33_kurallar.py eklendi (kural 1-5), sunum/bolum23_kurallar.py kural 3 yalnız A4'e bakar ve 'toplam farkı'nı kabul eder, sunum/satir_aynen_kontrol.py ve sunum/satir_aynen_tam.py 'araç kuralı önerileri' BEK satırını süzer, sunum/bolum19_kurallar.py KURAL_ATIF bölüm 17, sunum/geriye_donuk.py bolum33 satırı, sunum/mutasyon_sina.py b33 sınamaları (354 / 354); bu blokta araç değişikliği yok; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 328",
 "geriye dönük koşu (bölüm 17 kapanışı, komut 'python3 sunum/geriye_donuk.py b36k yamalar/geriye_donuk_6_b34k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 151 152 37'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:151 ve 6:152 esmâ yok; 6:151 lafız (35. kelime) ve Rab (6. kelime), 6:152 lafız (29. kelime) (bölüm 6 kuralı 14 — betikle: B6_ESMA); esma_el kaydı yok; A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 151 152 37'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:151 '{{1|fâsıla تعقلون → ن, N sınıfı}}', '{{1|simetri \\[6, 17, 36, 2\\]}}', '{{1|harf 193 → harf3 175, isaret 18}}' ve '{{1|dış düğüm 4}}'; "
 "6:152 '{{2|fâsıla تذكرون → ن, N sınıfı}}', '{{2|simetri \\[3, 5, 19, 1\\]}}', '{{2|harf 160 → harf3 149, isaret 11}}' ve '{{2|dış düğüm 2}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 151 152 37'): KALAN_P",
 "ölçüm aktör: 6:151 ve 6:152 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:151 emir, yasak — IMPV 2 'qul' (1.), 'te'âlev' (2.), PRO 4 'lâ' (8.), 'lâ' (14.), 'lâ' (22.), 'lâ' (30.); ölçüm biçim ISTISNA + NEHY (D2'de yazılmadı); "
 "6:152 emir, yasak, şart — COND 1 'lev' (24.), IMPV 3 'evfu' (12.), 'a'dilû' (23.), 'evfû' (30.), NEG 1 'lâ' (16.), PRO 1 'lâ' (1.), RES 1 'illâ' (5.); ölçüm biçim HASR + ISTISNA + NEHY (D2'de yazılmadı); "
 "morph EXP ('illâ' 6:151 36., 6:152 19.), INT ('ellâ' 6:151 8.), ACC ('le'allekum' 6:151 41., 6:152 34.), T ('izâ' 6:152 21.), RSLT ('fa'dilû' 6:152 23.), CIRC ('ve lev' 6:152 24.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:151 ★★★ (kaynak n, z=3,14); 6:152 ★★ (kaynak n, z=2,40)",
 "fâsıla: 6:150 ن → 6:151 ن (تعقلون) → 6:152 ن (تذكرون) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:151 4:36 (emsal olarak basıldı), 17:33 (emsal olarak basıldı), 25:68 (emsal olarak basıldı) ve okunmamış 1 ayet; 6:152 17:34 (emsal olarak basıldı) ve okunmamış 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:151 'zâ vassâ _ le'alle' süzgeç GEÇER; 6:152 'zâ vassâ _ le'alle' süzgeç GEÇER",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "6:151 muhatap 2MS ('qul'), muhatap 2MP ('te'âlev', 'tuşrikû', 'taqtulû', 'taqrabu', 'taqtulu', 'ta'qilûn' — söz içi; ekler 'rabbukum', ''aleykum', 'evlâdekum', 'nerzuqukum', 'zâlikum', 'vassâkum', 'le'allekum'), konuşan 1S ('etlu' — söz içi), konuşan 1P ('nahnu', 'nerzuqu' — söz içi), "
 "3MS ('harrame' — söz içi, fiil uyumu, fail 6. ve 35. kelime; 'zahera', 'batan' — gönderge 'mâ' 25. ve 28. kelime; 'vassâkum' — gönderge 'rabbukum' 6. kelime; 'bihî' ekleri — gönderge 'rabbukum' 6. kelime ve 'zâlikum' 38. kelime), 3MP ('iyyâhum' — gönderge 'evlâdekum' 16. kelime), 3FS ('minhâ' eki — gönderge 'l-fevâhişe' 24. kelime); "
 "6:152 muhatap 2MP ('taqrabû', 'evfu', 'qultum', 'a'dilû', 'evfû', 'tezekkerûn' — söz içi; ekler 'zâlikum', 'vassâkum', 'le'allekum'), konuşan 1P ('nukellifu' — söz içi), 3MS ('yebluğa', 'eşuddeh' eki — gönderge 'l-yetîmi' 4. kelime; 'kâne' — tartışmalı; 'vassâkum' — gönderge 6:151 6. kelime; 'bihî' eki — gönderge 'zâlikum' 31. kelime), 3FS ('hiye' — gönderge 'lletî' 6. kelime; 'vus'ahâ' eki — gönderge 'nefsen' 18. kelime)",
 "6:151-152 gönderge zinciri: 6:151 'qul' (1. kelime) muhatabı muhatap 2MS (adsız); 'te'âlev' (2. kelime) ile açılan söz 6:152 sonuna dek sürer, muhatap 2MP; 6:152 'kâne' (25. kelime) öznesi söz hakkında olunan kişi ya da söylenen söz (okuma; tartışmalı)",
 "edilgen: blokta edilgen fiil yok (ölçüm EDİLGEN alanı yok)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:151 'qul' (1.) ardından söz 2. kelimede açılır ve ayet sonunda kapanmaz; 6:152 söz 1-35. kelime sürer, ayet sonunda kapanmaz (morph sözün bittiğini göstermiyor); mealde 'De ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 151 152 37' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; REM sapması 6:152 (21. kelime) — 've izâ' söz içinde istînâf, muhatap 2MP sürer, söz ayet sonuna dek sürer; "
 "morph 've' konumlarıyla kontrol edildi: 6:151 've bi'l-vâlideyni' (12.), 've lâ' (14.), 've iyyâhum' (21.), 've lâ' (22.), 've mâ' (28.), 've lâ' (30.) CONJ; 6:152 've lâ' (1.), 've evfu' (12.), 've'l-mîzâne' (14.), 've bi-'ahdi' (28.) CONJ, 've izâ' (21.) REM, 've lev' (24.) CIRC; "
 "'fe' konumları: 6:152 'fa'dilû' (23.) RSLT",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:151-152 ◈K / ◈B tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 151 152 37'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 2 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:151 (4:36, 17:33, 25:68); 6:152 (17:34); D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 6:151 حرم ×2, قتل ×2, ولد ×2; 6:152 قرب ×2, وفي ×2; ayetler arası kalıp 'zâlikum vassâkum bihî le'allekum' (6:151, 6:152) — sayım 'say 6:151 38-41' ve lemma dizisi 'dizi 6 151 38 41' / 'dizi 6 152 31 34' (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:151 söz açılır (2. kelime), muhatap geçişi 2MS → 2MP (ayet içi), şahıs geçişi 3 → 2, edim geçişi emir, yasak, şart → emir, yasak; bölüm açılışı; "
 "6:152 şart → cevap (ayet içi; zaman şartı 'izâ' 21. kelime), şart → cevap (ayet içi; COND 'lev' 24. kelime — cevap hazif), şahıs geçişi yok, edim geçişi emir, yasak → emir, yasak, şart; "
 "ölçüm iltifât 6:151-152 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:151 'etlu' — emre bağlı muzari (morph JUS); 6:151 'ellâ tuşrikû' — tefsir edatı ve nehiy (morph INT + PRO); 6:151 'illâ bi'l-haqq' — istisna (morph EXP); "
 "6:152 'illâ bi'lletî hiye ahsenu' — hasr (morph RES); 6:152 'fa'dilû' — zaman şartının cevabı (morph T + RSLT); 6:152 've lev kâne zâ qurbâ' — hâl ve şart (morph CIRC + COND), cevap mahzuf (6:152 24. kelime)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:151 9-13. kelime — 4:36 ile harekesiz eş (sayım: 'say 6:151 9-13'); 6:151 30-37. kelime — 17:33 ile harekesiz eş (sayım: 'say 6:151 30-37'); "
 "6:151 32-37. kelime — 17:33 ve 25:68 ile harekesiz eş (sayım: 'say 6:151 32-37'); 6:152 1-11. kelime — 17:34 ile harekesiz eş (sayım: 'say 6:152 1-11'); 6:151 kök حرم, قتل, ولد ikilemeleri; 6:152 kök قرب, وفي ikilemeleri",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 37'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'tuşrikû bihî şey'â, ve bi'l-vâlideyni ihsânâ' 6:151 'O'na hiçbir şeyi ortak koşmayın. Ana babaya iyilik edin' / 4:36 'O'na hiçbir şeyi ortak koşmayın. Ana babaya iyilik edin' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve lâ taqtulu'n-nefse'lletî harrame'llâhu illâ bi'l-haqq' 6:151 'Allah'ın haram kıldığı canı haksız yere öldürmeyin' / 17:33 'Allah'ın haram kıldığı canı haksız yere öldürmeyin' (emsal metninde) — çakışma değil (bayt eşit); "
 "'n-nefse'lletî harrame'llâhu illâ bi'l-haqq' 6:151 'Allah'ın haram kıldığı canı haksız yere' / 25:68 'Allah'ın haram kıldığı canı haksız yere' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve lâ taqrabû mâle'l-yetîmi illâ bi'lletî hiye ahsenu hattâ yebluğa eşuddeh' 6:152 'Yetimin malına, rüşdüne erişinceye kadar, en güzel biçimde olması dışında yaklaşmayın' / 17:34 'Yetimin malına, rüşdüne erişinceye kadar, en güzel biçimde olması dışında yaklaşmayın' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:151 'qul' IMPV — meal 'De'; 'te'âlev' IMPV — meal 'Gelin'; 'etlu' IMPF JUS — meal 'okuyayım'; 'harrame' PERF — meal 'kıldığı'; 'tuşrikû' IMPF JUS ('lâ' ile) — meal 'koşmayın'; 'taqtulû' IMPF JUS ('lâ' ile) — meal 'öldürmeyin'; 'nerzuqu' IMPF IND — meal 'rızıklandırırız'; "
 "'taqrabu' IMPF JUS ('lâ' ile) — meal 'yaklaşmayın'; 'zahera' PERF — meal 'açık olanına'; 'batan' PERF — meal 'gizli olanına'; 'taqtulu' IMPF JUS ('lâ' ile) — meal 'öldürmeyin'; 'vassâ' PERF — meal 'ettiğidir'; 'ta'qilûn' IMPF IND — meal 'erdirirsiniz'; "
 "6:152 'taqrabû' IMPF JUS ('lâ' ile) — meal 'yaklaşmayın'; 'yebluğa' IMPF SUBJ ('hattâ' ile) — meal 'erişinceye'; 'evfu' IMPV — meal 'yapın'; 'nukellifu' IMPF IND ('lâ' ile) — meal 'yüklemeyiz'; 'qultum' PERF ('izâ' ile) — meal 'Söylediğinizde'; 'a'dilû' IMPV — meal 'olun'; 'kâne' PERF ('lev' ile) — meal 'olsa'; 'evfû' IMPV — meal 'getirin'; 'vassâ' PERF — meal 'ettiğidir'; 'tezekkerûn' IMPF IND — meal 'düşünürsünüz'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'harrame', 'zahera', 'batan', 'vassâ' PERF 6:151 ve 6:152'de sıfat-fiil ('-dığı', '-an', '-tiği') ile; 'qultum' PERF 6:152'de zaman zarf-fiili ('-diğinizde') ile; 'kâne' PERF 6:152'de şart ('-sa') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; ayetler arası kalıp 'zâlikum vassâkum bihî le'allekum' — çakışma değil (6:151 ve 6:152 eş karşılık 'Bu, size tavsiye ettiğidir; ola ki')",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 151 152 37'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:151 ve 6:152 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:151 ('zahera' / 'batan'); 6:152 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök وصي 6:151 ('vassâkum') ve 6:152 ('vassâkum'); kök قرب 6:151 ('taqrabu') ve 6:152 ('taqrabû', 'qurbâ'); kök نفس 6:151 ('n-nefse') ve 6:152 ('nefsen'); kök حسن 6:151 ('ihsânâ') ve 6:152 ('ahsenu'); kök أله 6:151 ('llâhu') ve 6:152 ('llâhi'); kök قول 6:151 ('qul') ve 6:152 ('qultum'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 18-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 37 ve 38; bölüm açılışı bu blokta; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b37/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 151 152 37'; lem_bozuk.py 37 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 151 152 → AYN_SONUC; sunum/bolum4_kurallar.py 151 152 37 → KHATA_HEPSI; sunum/bolum5_kurallar.py 151 152 37 → B5_HEPSI; sunum/bolum6_kurallar.py 151 152 37 → B6_HEPSI; sunum/bolum7_kurallar.py 151 152 37 → B7_HEPSI; sunum/bolum8_kurallar.py 151 152 37 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 151 152 37 → B9_HEPSI; sunum/bolum10_kurallar.py 151 152 37 → B10_HEPSI; sunum/bolum11_kurallar.py 151 152 37 → B11_HEPSI; sunum/bolum12_kurallar.py 151 152 37 → B12_HEPSI; sunum/bolum13_kurallar.py 151 152 37 → B13_HEPSI; sunum/bolum14_kurallar.py 151 152 37 → B14_HEPSI; sunum/bolum15_kurallar.py 151 152 37 → B15_HEPSI; sunum/bolum16_kurallar.py 151 152 37 → B16_HEPSI; sunum/bolum17_kurallar.py 151 152 37 → B17_HEPSI; sunum/bolum18_kurallar.py 151 152 37 → B18_HEPSI; sunum/bolum19_kurallar.py 151 152 37 → B19_HEPSI; sunum/bolum20_kurallar.py 151 152 37 → B20_HEPSI; sunum/bolum21_kurallar.py 151 152 37 → B21_HEPSI; sunum/bolum22_kurallar.py 151 152 37 → B22_HEPSI; sunum/bolum23_kurallar.py 151 152 37 → B23_HEPSI; sunum/bolum24_kurallar.py 151 152 37 → B24_HEPSI; sunum/bolum25_kurallar.py 151 152 37 → B25_HEPSI; sunum/bolum26_kurallar.py 151 152 37 → B26_HEPSI; sunum/bolum27_kurallar.py 151 152 37 → B27_HEPSI; sunum/bolum28_kurallar.py 151 152 37 → B28_HEPSI; sunum/bolum29_kurallar.py 151 152 37 → B29_HEPSI; sunum/bolum30_kurallar.py 151 152 37 → B30_HEPSI; sunum/bolum31_kurallar.py 151 152 37 → B31_HEPSI; sunum/bolum32_kurallar.py 151 152 37 → B32_HEPSI; sunum/bolum33_kurallar.py 151 152 37 → B33_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 37 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; 6:151 ve 6:152 ölçüm xref'lerindeki okunmamış ayetler (ayet başına 1) emsal alınmadı — okunmamış sûre; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('eşrake', 'şey'', 'vâlid', 'ihsân', 'lâ', 'qatele', 'nefs', 'ellezî', 'harrame', 'allâh', 'illâ', 'haqq', 'zâ', 'vassâ', 'le'alle', 'yaqrabu' (morph LEM ham biçim), 'mâl', 'yetîm', 'ahsen', 'hattâ', 'beleğa', 'eşudd', 'evfâ'); joker '_' yalnız lemmasız öğelerde ('bihî' — 'dizi 6 151 9 13', 'dizi 6 151 38 41', 'dizi 6 152 31 34'; 'hiye' — 'dizi 6 152 1 12'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (151, 152): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_151_152.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b36k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '151', '152'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '151', '152', '37'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '151', '152', '37'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '151', '152', '37', '--tazelik-yok')}
    for _n in range(7, 34): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '151', '152', '37')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33 = [_R['B%d' % _n].splitlines() for _n in range(6, 34)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI), 'B6_ESMA': ('; '.join(l[5:] for l in B6 if 'esmâ kural' in l and l.startswith('HATA')) or 'sapma 0')}
    I_cur = list(I_HAM)
    for k, v in REP.items(): I_cur = I_cur[:len(BEK)] + [x.replace(k, v) for x in I_cur[len(BEK):]]  # bölüm 9 kuralı 9: taşınan denetim maddelerine yer tutucu değişimi uygulanmaz
    I_cur[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3, bölüm 6 kuralı 2 — komut 'python3 sunum/cakisma.py' + sûre 6'nın okunmuş bütün ARIZA dosyaları; bu bloğun karşılıklarına dokunan gruplar ve son dosyaya dokunan KÖK grupları; grup başına tam bir kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
                  + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
    if I_cur == onceki: break
    onceki = list(I_cur)
yaz(I_cur)
print('yazıldı', len(I_cur), 'tur', tur)
print('\n'.join(CAK_L))
print(GLS)
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
