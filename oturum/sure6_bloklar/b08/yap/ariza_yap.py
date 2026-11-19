# sûre 6 blok 8 (6:33-36) ARIZA oluşturucu — bölüm 4-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b08/olcum.txt'
os.environ['SAY2'] = '/home/claude/b08/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b07.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {}
BOL = "'Elçiye teselli; darlıkta çağrılan'"


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
 ("6:34", "'resûl min qabl'", 2, 'say 6:34 3-5', "harekesiz 'rusulun min qablik' (3-5. kelime)", ('dizi 6 34 3 5', "resûl min qabl", '3-5', "biçim farkı (dizi 6 34 3 5): 6:10 i'râb, önek")),
 ("6:35", "'lev şâ'e allâh'", 2, 'say 6:35 19-21 --on', "önek kesilmiş 'lev şâ'e'llâh' (19-21. kelime)", ('dizi 6 35 19 21', "lev şâ'e allâh", '19-21', "biçim farkı (dizi 6 35 19 21): basılmamış eş yazım eş; basılmamış eş yazım eş; basılmamış eş önek; biçim öğesi 've' (lemma dizisi sûre içi 4, nakarat3 2); öneksiz eş koşusu (dizi 6 35 19 21): basılmamış eş → önek kesilmiş sûre içi 3; basılmamış eş → önek kesilmiş sûre içi 3; basılmamış eş → önek kesilmiş sûre içi 4")),
 ("6:35", "'fe-lâ kâne min'", 2, 'say 6:35 25-27', "harekesiz 'fe-lâ tekûnenne mine' (25-27. kelime)", None),
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

K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}

VF_YAZI = {33: {10: "'ve lâkinne'"}, 34: {1: "'ve le-qad'", 10: "'ve ûzû'", 14: "'ve lâ'", 18: "'ve le-qad'"}, 35: {1: "'ve in'", 19: "'ve lev'"}, 36: {5: "'ve'l-mevtâ'"}}
sys.path.insert(0, '/home/claude/b08/yap')
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
open('/home/claude/b08/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '08')
BLOKLAR = [str(i) for i in range(1, 9)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '8', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b08/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '33', '36', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b08/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b08/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '33', '36', '08').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_33_36.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:33', '6:34', '6:35', '6:36'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_33_36.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(33, 37))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:34 kök قبل ('qablike' 5. kelime — önce): tetik listesinde yok; 6:35 kök عرض ('i'râduhum' 5. kelime — yüz çevirme), kök جمع ('le-ceme'ahum' 22. kelime — topla-): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '33', '36', '08')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b08/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 9)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(33, 37))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/bolum19_kurallar.py — sûre 6 bölüm 3 denetimi kural 1-5 (bekleyen_ariza_6_b07 araç önerileri: KOMUT_BLOK, OZ_DENETIM_SIFIR, IZA_CEVAP, KURAL_ATIF, ESMA_LEMMA_BIR; elle kalanlar başlıkta); mutasyon_sina var6 sınamaları ve geriye_donuk listesi bolum19 ile genişledi; geriye dönük koşu geriye_donuk_6_b08 (yeni isabet 106; kayıtlar yeniden yazılmadı); sunum/bolum19_kurallar.py kural 2 — öz atıf kilidi: kural kendi bayat sonucunu atlar (sûre 6 blok 8); sunum/yasakli.sh bölüm 6 kuralı 10 — art arda eş sözcük izni 'bile bile' (meal deyimi); mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 145",
 "kök tablosu: ölçümde '???' 6:33-36 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 33 36 08'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: blokta esmâ yok (ölçüm 6:33-36); esma_el kaydı yok; "
 "lafız 6:33, 6:34, 6:35 ve 6:36; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 33 36 08'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:33 '{{1|fâsıla يجحدون → ن, N sınıfı}}', '{{1|simetri \\[3, 1, 5, 1\\]}}', '{{1|harf 67 → harf3 65, isaret 2}}' ve '{{1|dış düğüm 1}}'; "
 "6:34 '{{2|fâsıla ٱلمرسلين → ن, N sınıfı}}', '{{2|simetri \\[4, 1, 8, 1\\]}}', '{{2|harf 97 → harf3 90, isaret 7}}', '{{2|dış düğüm 2}}' ve '{{2|EDİLGEN 3/6 fiil, pas z=2,52}}'; "
 "6:35 '{{3|fâsıla ٱلجهلين → ن, N sınıfı}}', '{{3|simetri \\[3, 1, 25, 1\\]}}', '{{3|harf 119 → harf3 114, isaret 5}}' ve '{{3|dış düğüm 0}}'; "
 "6:36 '{{4|fâsıla يرجعون → ن, N sınıfı}}', '{{4|harf 52 → harf3 50, isaret 2}}', '{{4|dış düğüm 0}}' ve '{{4|EDİLGEN 1/4 fiil, pas z=1,10}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 33 36 08'): KALAN_P",
 "ölçüm aktör: 6:33-36 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:33 haber — CERT 1 'qad' (1.), EMPH 1 'le-yahzunuke' (4.), NEG 1 'lâ' (8.); 6:34 haber — CERT 2 ve EMPH 2 've le-qad' (1., 18.), NEG 1 'lâ' (14.); "
 "6:35 şart — COND 3 've in' (1.), 'fe-in' (6.), 've lev' (19.), EMPH 2 'le-ceme'ahum' (22.), 'tekûnenne' (26.), NEG 1 'lâ' (25.); 6:36 haber, kip yok; "
 "morph ACC ('inne' 6:33 3. ve 7.; 'lâkinne' 6:33 10.; 'innemâ' 6:36 1.), PREV ('mâ' 6:36 1.), REM ('ve' 6:33 10.; 6:34 1., 14. ve 18.; 6:35 1.; 6:36 5.), INC ('hattâ' 6:34 11.), SUB ('en' 6:35 8.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:34 ★★ (kaynak pas, z=2,52); 6:35 ★ (kaynak n, z=1,65); 6:33 ve 6:36 yıldız yok",
 "fâsıla: 6:32 ن → 6:33 ن (يجحدون) → 6:34 ن (ٱلمرسلين) → 6:35 ن (ٱلجهلين) → 6:36 ن (يرجعون) — N sınıfı sürüyor; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:33 40:63 (emsal olarak basıldı); 6:34 35:4 (emsal olarak basıldı) ve okunmuş 1 ayet; "
 "6:35 yok; 6:36 yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:34 'resûl min qabl' süzgeç GEÇMEZ; 6:35 'lev şâ'e allâh' ve 'fe-lâ kâne min' GEÇMEZ; "
 "6:33 ve 6:36 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; edilgen fiilde naib-i faili zamir 'adsız' ile — sûre 6 bölüm 2 denetimi kuralı 5; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8): "
 "6:33 konuşan 1P, muhatap 2MS, 3MP (adsız — gönderge 'z-zâlimîne'), 3MS ('innehû' şan zamiri; 'le-yahzunuke' 4. kelime — fail 5. kelime); 6:34 3FS ('kuzzibet' edilgen — naib-i faili 'rusulun' 3. kelime), 3MP (adsız; 'kuzzibû', 've ûzû' edilgen — naib-i faili zamir), 3MS ('etâhum' 12. kelime — fail 13. kelime; 'câ'eke' 19. kelime — fail 21. kelime); "
 "6:35 3MS ('kebure' 3. kelime — fail 5. kelime; 'şâ'e' 20. kelime — fail 21. kelime; 'kâne' şan zamiri), muhatap 2MS, 3MP (adsız — gönderge 6:33 11. kelime); "
 "6:36 3MS ('yestecîbu' 2. kelime — fail 3. kelime; 'yeb'asuhumu' 6. kelime — fail 7. kelime), 3MP (adsız; 'yurce'ûn' edilgen — naib-i faili zamir) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): "
 "6:33-36 söz yok; mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 33 36 08' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 6:33 'fe-innehum' (7.) CONJ, 've lâkinne' (10.) REM; 6:34 've le-qad' (1., 18.), 've lâ' (14.) REM, 'fe-saberû' (6.), 've ûzû' (10.) CONJ; 6:35 've in' (1.), 'fe-in' (6.), 'fe-lâ' (25.) REM, 've lev' (19.), 'fe-te'tiyehum' (17.) CONJ; 6:36 've'l-mevtâ' (5.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:35 ◈K أرض ('l-ardi' 12. kelime — K1); 6:35 ◈K سمو ('s-semâ'i' 16. kelime — K1; anlam notu: yerde tünel, gökte merdiven); 6:36 ◈B سمع ('yesme'ûn' 4. kelime — B3); 6:36 ◈B موت ('l-mevtâ' 5. kelime — B4; anlam notu: işitenler ve ölüler)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 33 36 08'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:33 (40:63); 6:34 (35:4); 6:35 ve 6:36 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp yok; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:33 edim geçişi soru → haber, bölüm açılışı; 6:34 şahıs ve edim geçişi yok; 6:35 şart → cevap ('in' 1. kelime / 'fe-ini'steta'te' 6. kelime; 'in' 6. kelime — cevap hazif; 'lev' 19. kelime / 'le-ceme'ahum' 22. kelime), şahıs geçişi 3 → 2, edim geçişi haber → şart; "
 "6:36 şahıs geçişi 2 → 3, edim geçişi şart → haber; şahıs beraberliği yok (sûre 6 bölüm 1 denetimi kuralı 9); ölçüm iltifât 6:33-36 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:33 'qad na'lemu' — tahkik (morph CERT); 'innehû le-yahzunuke' — tekit (morph ACC + EMPH); 'lâkinne' — istidrak (morph ACC); "
 "6:34 've le-qad' — istînâf ve yemin tekidi (morph REM + EMPH + CERT); 'lâ mubeddile' — cins nefyi (morph NEG); 'hattâ' — gaye (morph INC); 6:35 'in … fe-in' — iç içe şart (morph COND); 'lev … le-' — şart ve cevap (morph COND + EMPH); 'fe-lâ tekûnenne' — tekitli yasak (morph NEG + EMPH); "
 "6:36 'innemâ' — kasr (morph ACC + PREV)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:33 'bi-âyâti'llâhi yechadûn' — 40:63 ile eş (sayım: 'say 6:33 12-14'); "
 "6:34 'kuzzibet rusulun min qablik' — 35:4 ile eş (sayım: 'say 6:34 2-5'); 6:34 kök رسل ve كذب ikilemesi; "
 "6:35 'fi'l-ardi' / 'fi's-semâ'i' karşıtlığı; 6:36 'yesme'ûn' / 'l-mevtâ' karşıtlığı",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 08'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'bi-âyâti'llâhi yechadûn' 6:33 'Allah'ın âyetlerini bile bile inkâr ediyorlar' / 40:63 'Allah'ın ayetlerini bile bile inkâr edegelenler' (emsal metninde) — çakışma — tam okuma sonu (yazım 'âyet' / 'ayet' ve kip farkı); "
 "'bi-âyâti'llâh' 6:33 'Allah'ın âyetlerini' / 40:63 'Allah'ın ayetlerini' (emsal metninde) — çakışma — tam okuma sonu (yazım 'âyet' / 'ayet'); "
 "'kuzzibet rusulun min qablik' 6:34 'senden önce de elçiler yalanlandı' / 35:4 'senden önce de elçiler yalanlandı' (emsal metninde) — çakışma değil; "
 "'kuzzibet rusul' 6:34 'elçiler yalanlandı' / 35:4 'elçiler yalanlandı' (emsal metninde) — çakışma değil; "
 "'rusulun min qablik' 6:34 'senden önce de elçiler' / 35:4 'senden önce de elçiler' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:33 'na'lemu' IMPF IND — meal şimdiki zaman 'biliyoruz'; 'yahzunu' IMPF IND — meal 'üzüyor'; 'yeqûlûne' IMPF IND — meal '-dikleri'; 'yukezzibûneke', 'yechadûn' IMPF IND — meal şimdiki zaman; "
 "6:34 'kuzzibet', 'kuzzibû', 'ûzû' PERF edilgen — meal geçmiş edilgen; 'saberû' PERF — meal '-tiler'; 'etâ' PERF (hattâ ile) — meal '-inceye'; 'câ'eke' PERF — meal '-miştir'; 6:35 'kâne kebure' PERF (şart) — meal 'geldiyse'; 'steta'te' PERF (şart) — meal 'yeterse'; 'tebteğiye', 'te'tiye' IMPF SUBJ — meal '-ıp' / '-meye'; 'şâ'e' PERF (lev ile) — meal '-seydi'; 'ceme'a' PERF (lev cevabı) — meal '-ardı'; 'tekûnenne' IMPF (tekitli yasak) — meal 'sakın … olma'; "
 "6:36 'yestecîbu', 'yesme'ûn', 'yeb'asu' IMPF IND — meal geniş zaman; 'yurce'ûn' IMPF IND edilgen — meal 'döndürülürler'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 33 36 08'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:33-36 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:33 ('lâ yukezzibûneke' / 'yechadûn'); 6:35 ('fi'l-ardi' / 'fi's-semâ'i'; 'l-hudâ' / 'l-câhilîn'); 6:36 ('yesme'ûn' / 'l-mevtâ'); ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök كذب 6:33 ('yukezzibûneke') ve 6:34 ('kuzzibet', 'kuzzibû') — yalanlama bağı; lafız 6:33, 6:34, 6:35, 6:36; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 4-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm iki blok (8, 9); "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b08/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 33 36 08'; lem_bozuk.py 08 çıktısı): lem_bozuk bayrağı 6:33 4. kelime يَحْزُن, 6:33 14. kelime جَحَدُ, 6:34 10. kelime أُوذِيَ — meal maddelerinde (morph LEM ham biçim) notu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 33 36 → AYN_SONUC; sunum/bolum4_kurallar.py 33 36 08 → KHATA_HEPSI; sunum/bolum5_kurallar.py 33 36 08 → B5_HEPSI; sunum/bolum6_kurallar.py 33 36 08 → B6_HEPSI; sunum/bolum7_kurallar.py 33 36 08 → B7_HEPSI; sunum/bolum8_kurallar.py 33 36 08 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 33 36 08 → B9_HEPSI; sunum/bolum10_kurallar.py 33 36 08 → B10_HEPSI; sunum/bolum11_kurallar.py 33 36 08 → B11_HEPSI; sunum/bolum12_kurallar.py 33 36 08 → B12_HEPSI; sunum/bolum13_kurallar.py 33 36 08 → B13_HEPSI; sunum/bolum14_kurallar.py 33 36 08 → B14_HEPSI; sunum/bolum15_kurallar.py 33 36 08 → B15_HEPSI; sunum/bolum16_kurallar.py 33 36 08 → B16_HEPSI; sunum/bolum17_kurallar.py 33 36 08 → B17_HEPSI; sunum/bolum18_kurallar.py 33 36 08 → B18_HEPSI; sunum/bolum19_kurallar.py 33 36 08 → B19_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 8 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('resûl', 'min', 'qabl', 'lev', 'şâ'e', 'allâh', 'lâ', 'fe-lâ', 'kâne'); lemmasız öğe joker yok; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (33, 36): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_33_36.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b08.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '33', '36'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '33', '36', '08'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '33', '36', '08'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '33', '36', '08', '--tazelik-yok')}
    for _n in range(7, 20): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '33', '36', '08')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19 = [_R['B%d' % _n].splitlines() for _n in range(6, 20)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
