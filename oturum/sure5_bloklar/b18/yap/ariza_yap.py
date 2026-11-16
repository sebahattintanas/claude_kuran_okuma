# blok 18 (5:51-54) ARIZA oluşturucu — bölüm 7-3
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b18/olcum.txt'
os.environ['SAY2'] = '/home/claude/b18/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b17.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {33: {6: "'ve rasûlehû'", 7: "'ve yes'avne'", 18: "'ve erculuhum'", 30: "'ve lehum fi'l-âxirati'"}, 34: {9: "'fa'lemû'"}, 35: {6: "'ve'bteğû'", 9: "'ve câhidû'"}, 36: {11: "'ve mislehû'", 22: "'ve lehum 'azâbun'"}}
BOL = "'Velî edinme; Allah'ın sevdiği kavim; dinle alay edenler'"


def sd(key):
    return sayim.S2[key][1]


def sic(key):
    n, d = sayim.S2[key]
    return 1 + len([x for x in d['basilan'] if x.startswith('5:')]) + d['okunmus_si'] + d['henuz_si']


def taban(key, ay):
    n, d = sayim.S2[key]
    p = [ay] + [x for x in d['basilan'] if x.startswith('5:') and x != ay]
    if d['okunmus_si']: p.append('okunmus_si %d' % d['okunmus_si'])
    if d['henuz_si']: p.append('henuz_si %d' % d['henuz_si'])
    return ' + '.join(p)


R5 = [
 ("5:51", "'eyy ellezî âmene'", 16, 'say 5:51 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
 ("5:51", "'eyy ellezî âmene lâ'", 6, 'say 5:51 1-4', "harekesiz 'yâ eyyuhe'llezîne âmenû lâ' (1-4. kelime)", None),
 ("5:51", "'eyy ellezî âmene lâ ittexaze'", 2, 'say 5:51 1-5', "harekesiz 'yâ eyyuhe'llezîne âmenû lâ tettexizu' (1-5. kelime)", None),
 ("5:51", "'inne allâh lâ hedâ qavm'", 2, 'say 5:51 17-21', "harekesiz 'inne'llâhe lâ yehdi'l-qavm' (17-21. kelime)", None),
 ("5:51", "'allâh lâ hedâ qavm'", 3, 'say 5:51 18-21 --on', "önek kesilmiş 'llâhe lâ yehdi'l-qavm' (18-21. kelime)", None),
 ("5:51", "'inne allâh lâ'", 3, 'say 5:51 17-19', "harekesiz 'inne'llâhe lâ' (17-19. kelime)", None),
 ("5:54", "'eyy ellezî âmene'", 16, 'say 5:54 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
]
r5 = []
for ay, kal, nk, key, ad, dz in R5:
    s = sic(key)
    h = "%s nakarat3 %s %d (tür ic) / %s sûre içi %d (%s)" % (ay, kal, nk, ad, s, taban(key, ay))
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

VF_YAZI = {51: {7: "'ve'n-nasârâ'", 12: "'ve men'", 15: "'fe-innehû'"}, 52: {1: "'fe-tera'", 13: "'fe-'asa'", 22: "'fe-yusbihû'"}, 53: {1: "'ve yeqûlu'", 14: "'fe-asbahû'"}, 54: {9: "'fe-sevfe'", 14: "'ve yuhibbûnehû'", 25: "'ve lâ'", 35: "'ve'llâhu'"}}
sys.path.insert(0, '/home/claude/b18/yap')
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
open('/home/claude/b18/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '18')
BLOKLAR = [str(i) for i in range(1, 19)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR).replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '18').replace('\n', '; ')
EMS = open('/home/claude/b18/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '51', '54', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b18/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'
GLS = run('/home/claude/sunum/gloss_tara.py', '51', '54', '18').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_51_54.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:1', '5:2', '5:6', '5:8', '5:11', '5:35', '5:51', '5:52', '5:53', '5:54'}
D3DISI = ', '.join(sorted(_U - _BAG - _ON, key=lambda x: tuple(map(int, x.split(':')))))
ANILIS = "5:51 kök ولي ('evliyâ'e' 8., 'evliyâ'u' 10., 'yetevellehum' 13. kelime — velîlik); 5:52 kök صبح ('fe-yusbihû' 22. kelime — 'ol-' anlamında), نفس ('enfusihim' 27. kelime — kendi, iç); 5:53 kök يمن ('eymânihim' 9. kelime — yemin), صبح ('fe-asbahû' 14. kelime — 'ol-' anlamında)"
ARAC = run('/home/claude/sunum/arac_degisim.py')
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; bölüm 7 denetiminden kurallar araçlara işlendi: sunum/bolum7_kurallar.py (kurallar 1, 2, 3, 4, 7, 9, 10, 12), sunum/es_lemma.py ve sunum/gloss_tara.py (kural 5), sunum/kontrol.py ve sunum/translit_kontrol.py (kural 6), sunum/bolum5_kurallar.py (kural 11), sunum/arac_degisim.py (kural 10), sunum/geriye_donuk.py (bolum7 eklendi); "
 "mutasyon_sina — MUT_SONUC; geriye dönük koşu yeniden üretildi (GERI_P); kural 6 düzeltmesi: blok 17 bag alıntıları 'ummeten vâhide' ve 'fe'stebiqu'l-xayrât' (yamalar/bag_5_48_50.txt, calisma/aday_ekle_5_maide.py, notlar/okuma_baglantilari.json)",
 "kök tablosu: ölçümde '???' 5:51-54 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 51 54 18'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:51:8 ve 5:51:10 وَلِيّ 'degil' — 'evliyâ'', kural 'çoğul insan göndergeli → degil' (Yahudi ve Nasârâ velîleri); 5:54:17 مُؤْمِن 'degil' — ''ale'l-mu'minîne', kural 'çoğul insan göndergeli → degil'; 5:54:18 عَزِيز 'degil' — 'e'izzetin', kural 'çoğul insan göndergeli → degil' (kavmin sıfatı); "
 "5:54:36 واسِع ve 5:54:37 عَلِيم 'ilahi' — 've'llâhu vâsi'un 'alîm', kural ''ve'llâhu X' kuralı → ilahi' (esma_el_ekle → esma_kayit; bölüm 6 kuralı 14 — betikle, B6_ESMA); 5:52 ve 5:53 esmâ yok; lafız 5:51, 5:52, 5:53, 5:54; Rab yok",
 "esma_kayit: 5:51 'mühür hayır' (sınıf A/A; ölçüm MÜHÜRSÜZ — uyuşuyor), 5:52 'mühür hayır' (uyuşuyor), 5:53 'mühür hayır' (uyuşuyor), 5:54 'mühür EVET (ÇİFT)', ton denge (ölçüm 36. ve 37. sırada 'SON konum, MÜHÜR' — uyuşuyor); ölçüm 17. ve 18. sıradaki adları da 'ORTA konum, MÜHÜR' yazıyor, el kararı 'degil' — ölçüm satırı aynen, tam okuma sonu",
 "ölçüm: 5:51 '{{1|fâsıla ٱلظلمين → ن, N sınıfı}}', '{{1|simetri \\[3, 2, 12, 1\\]}}', '{{1|harf 110 → harf3 102, isaret 8}}' ve '{{1|dış düğüm 0}}'; 5:52 '{{2|fâsıla ندمين → ن, N sınıfı}}', '{{2|simetri \\[3, 2, 23, 1\\]}}', '{{2|harf 121 → harf3 114, isaret 7}}' ve '{{2|dış düğüm 2}}'; "
 "5:53 '{{3|fâsıla خسرين → ن, N sınıfı}}', '{{3|simetri \\[3, 4, 10, 1\\]}}', '{{3|harf 83 → harf3 78, isaret 5}}' ve '{{3|dış düğüm 0}}'; 5:54 '{{4|fâsıla عليم → م, N sınıfı}}', '{{4|simetri \\[3, 2, 7, 1\\]}}', '{{4|harf 162 → harf3 155, isaret 7}}' ve '{{4|dış düğüm 5}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 51 54 18'): KALAN_P",
 "ölçüm aktör: 5:51 adlı Yahudi, Nasârâ (cins, meful); 5:52, 5:53 ve 5:54 aktör yok — A1'de 'adlı aktör' etiketiyle",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:51 yasak, nida, şart — VOC 1 'yâ' (1.), PRO 1 'lâ' (4.), COND 1 'men' (12.), NEG 1 'lâ' (19.), biçim DIKKAT + NEHY; 5:52 haber, kip yok; 5:53 soru — INTG 1 'e' (4.), EMPH 1 'le' (11.), biçim DIKKAT + QASEM; 5:54 nida, şart — VOC 1 'yâ' (1.), COND 1 'men' (4.), FUT 1 'sevfe' (9.), NEG 1 'lâ' (25.), biçim DIKKAT",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:52 ★ (kaynak n, z=1,65); 5:54 ★★ (kaynak n, z=2,61; eşiği geçen başka: allah z=1,63); 5:51 ve 5:53 yıldız yok",
 "fâsıla: 5:50 ن (يوقنون) → 5:51 ن (الظلمين) → 5:52 ن (ندمين) → 5:53 ن (خسرين) → 5:54 م (عليم); hepsi N sınıfı; 5:54'te ن → م geçişi esmâ çiftiyle ('vâsi'un 'alîm'); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:52 47:20 (emsal olarak basıldı) ve okunmuş başka ayet; 5:54 62:4 (emsal olarak basıldı) ve okunmuş başka ayetler; 5:51 ve 5:53 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' ile; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 7 kuralı 8: önek kesilmiş sayım öneksiz taraftan da koşuldu): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:51 'eyy ellezî âmene lâ ittexaze', 'inne allâh lâ hedâ qavm', 'eyy ellezî âmene lâ', 'allâh lâ hedâ qavm', 'eyy ellezî âmene' ve 'inne allâh lâ' süzgeç GEÇER; 5:54 'eyy ellezî âmene' GEÇER, 'men şâ'e allâh' ve 'câhede fî sebîl' GEÇMEZ; 5:52 ve 5:53 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3 — ölçüt: 1P / 1S / 2MS / 2FS / 2MP / 2FP / 2D / 3MS / 3FS / 3D / 3MD / 3FD / 3MP / 3FP zamirlerin hepsi 'adsız', etiketin kendi parantezinde; etiket, kelimeyi anan alt maddede; adlı aktör ölçümün 'aktör: adlı' alanından): "
 "5:51 3MP (adsız — 'âmenû' faili; 'ba'duhum', 'yetevellehum', 'minhum'), muhatap 2MP (adsız), 3MS (adsız — 'yetevellehum', 'yehdi' failleri; 'fe-innehû'), Yahudi, Nasârâ (adlı aktör), Allah (lafız), 'men'; "
 "5:52 muhatap 2MS (adsız), 3MP (adsız — 'yusâri'ûne', 'yeqûlûne', 'yusbihû', 'eserrû' failleri; 'qulûbihim', 'fîhim', 'enfusihim'), konuşan 1P (adsız; söz içi), 3FS (adsız — 'tusîbe' faili), 3MS (adsız — ''asa', 'ye'tiye' failleri; ''indihî'), Allah (lafız); "
 "5:53 3MS (adsız — 'yeqûlu' faili), 3MP (adsız — 'âmenû', 'eqsemû', 'asbahû' failleri; 'eymânihim', 'innehum', 'a'mâluhum'), muhatap 2MP (adsız; söz içi), 3FS (adsız — 'habitat' faili), Allah (lafız); "
 "5:54 3MP (adsız — 'âmenû', 'yuhibbûnehû', 'yucâhidûne', 'yexâfûne' failleri; 'yuhibbuhum' mef'ûlü), muhatap 2MP (adsız), 3MS (adsız — 'yertedde', 'ye'ti', 'yuhibbuhum', 'yu'tîhi', 'yeşâ'u' failleri; 'dînihî', 'yuhibbûnehû' ve 'yu'tîhi' mef'ûlleri), Allah (lafız), 'men' — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): 5:52 'yeqûlûne' sözü 'naxşâ en tusîbenâ dâ'ira' (A3, 9-12. kelime; söyleyen 3MP); 5:53 'yeqûlu'llezîne âmenû' sözü 'e-hâ'ulâ'i'llezîne eqsemû … le-me'akum' (A3, 4-11. kelime); 5:51 ve 5:54 nida muhataba doğrudan; REM sapması (komut 'python3 sunum/bolum4_kurallar.py 51 54 18' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:51 've'n-nasârâ' (7.) CONJ, 've men' (12.) REM, 'fe-innehû' (15.) RSLT; 5:52 'fe-tera' (1.) ve 'fe-'asa' (13.) REM, 'fe-yusbihû' (22.) CONJ; 5:53 've yeqûlu' (1.) REM, 'fe-asbahû' (14.) CONJ; 5:54 'fe-sevfe' (9.) RSLT, 've yuhibbûnehû' (14.) CONJ, 've lâ' (25.) CIRC, 've'llâhu' (35.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:52 ◈B قلب ('qulûbihim' 4. kelime — B3; anlam notu: kalpte hastalık, mecaz); 5:51, 5:53 ve 5:54 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 51 54 18'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:51 (4:144, 45:19, 28:50), 5:52 (47:20), 5:53 (24:53), 5:54 (62:4, 2:268) (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6); blok geçişi 5:50 → 5:51: ayetler arası kalıp 'yâ eyyuhe'llezîne âmenû' (5:51, 5:54 ve sûre içi basılmış 5:1, 5:2, 5:6, 5:8, 5:11, 5:35) — sayım 'say 5:51 1-3' / 'say 5:54 1-3'; "
 "ayetler arası kalıp 'yâ eyyuhe'llezîne âmenû lâ' (5:2, 5:51) — sayım 'say 5:51 1-4'; bölüm içi tekrar, ardışık bağ yerine sayımla kayıt; D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7 — betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:51 edim geçişi soru → yasak, nida, şart; şahıs geçişi yok; şart → cevap (ayet içi; COND 'men' 12. kelime: 've men yetevellehum minkum' / 'fe-innehû minhum' (15. kelime)); 5:52 edim geçişi yasak, nida, şart → haber; şahıs geçişi yok; "
 "5:53 edim geçişi haber → soru; şahıs geçişi yok; 5:54 edim geçişi soru → nida, şart; şahıs geçişi yok; şart → cevap (ayet içi; COND 'men' 4. kelime: 'men yertedde minkum 'an dînih' / 'fe-sevfe ye'ti'llâhu bi-qavm' (9. kelime))",
 "sözdizimi (okuma; morph etiketiyle): 5:51 've men yetevellehum' — istînâf (morph REM) + şart (COND); 'fe-innehû minhum' — cevap (morph RSLT); 5:52 'fe-tera'llezîne' — istînâf (morph REM); 'yusâri'ûne fîhim' — 'terâ' fiilinin mef'ûlüne bağlı cümle (morph etiketi yok, okuma); 'fe-yusbihû' — atıf (morph CONJ); "
 "5:53 've yeqûlu' — istînâf (morph REM); 'e-hâ'ulâ'i' — soru (morph INTG); 'fe-asbahû' — atıf (morph CONJ); 5:54 'fe-sevfe ye'ti'llâhu' — cevap (morph RSLT); 've lâ yexâfûne' — hâl (morph CIRC); 've'llâhu vâsi'un' — istînâf (morph REM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:51 ve 5:54 'yâ eyyuhe'llezîne âmenû' ile açılıyor; 5:51 kök ولي üçlemesi 'evliyâ'e' / 'evliyâ'u' / 'yetevellehum' — velîlik yasağı; "
 "5:52 'fî qulûbihim marad' kalbin hastalığı, mecaz (◈B B3); 5:52 ve 5:53 'yeqûlûne' / 'yeqûlu' sözleri karşılıklı: korku sözü / yemin sorgusu; 5:54 kök حبب ikilemesi 'yuhibbuhum ve yuhibbûneh' — karşılıklı sevgi; kök لوم ikilemesi 'levmete lâ'im'; 5:54 karşıt çift 'ezilletin' / 'e'izzetin' (aday 1039)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 18'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + "'; çıktı aynen): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle): 'evliyâ'' 5:51 'velî' / 4:144 ve 45:19 'dost' (emsal metninde) — tam okuma sonu; 'qavme'z-zâlimîn' 5:51 'zalimler kavmi' / 28:50 'zalimler topluluğu' — tam okuma sonu; 'cehde eymânihim' 5:53 'yeminlerinin olanca gücüyle' / 24:53 'var güçleriyle' — tam okuma sonu; 've'llâhu vâsi'un 'alîm' 5:54 'geniş olandır' / 2:268 'geniştir' — tam okuma sonu",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 51 54 18'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:51-54 tarayıcı adayı yok; L3 / L4 adayı yok",
 "aday 1039: 5:54 ('ezilletin 'ale'l-mu'minîne' / 'e'izzetin 'ale'l-kâfirîn'); ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök ولي 5:51 'evliyâ'' (insan velîleri) / 'yetevellehum' (velî edinme); kök حبب 5:54 'yuhibbuhum' (Allah sever) / 'yuhibbûneh' (kavim sever); kök أمن 5:54 'âmenû' / 'l-mu'minîne' — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 8-1 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (18, 19); başlıktaki 'velî edinme' 5:51, 'Allah'ın sevdiği kavim' 5:54 ('yuhibbuhum ve yuhibbûneh'); 'dinle alay edenler' blok 19'da; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b18/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11 — betikle: komut 'python3 sunum/bolum5_kurallar.py 51 54 18'; lem_bozuk.py 18 çıktısı): 5:52:6 'yusâri'u', 5:53:6 'aqsemu', 5:54:13 'ahbeb' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 51 54 → AYN_SONUC; sunum/bolum4_kurallar.py 51 54 18 → KHATA_HEPSI; sunum/bolum5_kurallar.py 51 54 18 → B5_HEPSI; sunum/bolum6_kurallar.py 51 54 18 → B6_HEPSI; sunum/bolum7_kurallar.py 51 54 18 → B7_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (sunum/sonradan.py --plan 18): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('eyy', 'ellezî', 'âmene', 'ittexaze', 'yehûd', 'nasrâniyy', 'veliyy', 'ba'd', 'tevellâ', 'hedâ', 'qavm', 'zâlim', 're'â', 'qalb', 'marad', 'yusâri'u' (morph LEM ham biçim), 'qâle', 'xaşiye', 'esâbe', 'dâ'ira', ''asâ', 'etâ', 'feth', 'emr', ''ind', 'asbaha', 'eserra', 'nefs', 'nâdim', "
 "'aqsemu' (morph LEM ham biçim), 'cehd', 'yemîn', 'me'a', 'habita', ''amel', 'xâsir', 'irtedde', 'dîn', 'ahbeb' (morph LEM ham biçim), 'ezille', 'mu'min', ''azîz', 'kâfir', 'câhede', 'sebîl', 'xâfe', 'levme', 'lâ'im', 'fadl', 'âtâ', 'şâ'e', 'vâsi'', ''alîm'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (51, 54): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_51_54.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b17.txt', encoding='utf-8').read().splitlines()[:2]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '51', '54').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '51', '54', '18').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '51', '54', '18').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '51', '54', '18', '--tazelik-yok').splitlines()
    B7 = run('/home/claude/sunum/bolum7_kurallar.py', '51', '54', '18').splitlines()
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI), 'B6_ESMA': ('; '.join(l[5:] for l in B6 if 'esmâ kural' in l and l.startswith('HATA')) or 'sapma 0')}
    I_cur = list(I_HAM)
    for k, v in REP.items(): I_cur = [x.replace(k, v) for x in I_cur]
    I_cur[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3, bölüm 6 kuralı 2 — komut 'python3 sunum/cakisma.py' + sûre 5'in okunmuş bütün ARIZA dosyaları; bu bloğun karşılıklarına dokunan gruplar ve son dosyaya dokunan KÖK grupları; grup başına tam bir kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
                  + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
    if I_cur == onceki: break
    onceki = list(I_cur)
yaz(I_cur)
print('yazıldı', len(I_cur), 'tur', tur)
print('\n'.join(CAK_L))
print(GLS); print(KUR); print(B5); print(B6)
