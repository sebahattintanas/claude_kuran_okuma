# blok 17 (5:48-50) ARIZA oluşturucu — bölüm 7-3
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b17/olcum.txt'
os.environ['SAY2'] = '/home/claude/b17/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {33: {6: "'ve rasûlehû'", 7: "'ve yes'avne'", 18: "'ve erculuhum'", 30: "'ve lehum fi'l-âxirati'"}, 34: {9: "'fa'lemû'"}, 35: {6: "'ve'bteğû'", 9: "'ve câhidû'"}, 36: {11: "'ve mislehû'", 22: "'ve lehum 'azâbun'"}}
BOL = "'Küfürde yarışanlar; Tevrat, İncil ve Kitap ile hüküm'"


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
 ("5:48", "'ilâ allâh merci' cemî' nebbe'e mâ kâne'", 2, 'say 5:48 43-49', "harekesiz 'ile'llâhi merci'ukum cemî'an fe-yunebbi'ukum bi-mâ kuntum' (43-49. kelime)", None),
 ("5:48", "'musaddiq mâ beyn yed min'", 2, 'say 5:48 5-9', "harekesiz 'musaddiqan li-mâ beyne yedeyhi min' (5-9. kelime)", None),
 ("5:48", "'hakeme beyn mâ enzele allâh'", 2, 'say 5:48 13-17 --on', "önek kesilmiş 'fa'hkum beynehum bi-mâ enzele'llâh' (13-17. kelime)",
  ('dizi 5 48 13 17', "hakeme beyn mâ enzele allâh", '13-17', "önek kesilmiş sayım ('say 5:48 13-17 --on') sûre içi 1, lemma dizisi ('dizi 5 48 13 17') sûre içi 2 (5:48, 5:49) — fark açıklanmadı, tam okuma sonu")),
 ("5:48", "'mâ enzele allâh'", 5, 'say 5:48 15-17', "harekesiz 'bi-mâ enzele'llâh' (15-17. kelime)", None),
 ("5:49", "'hakeme beyn mâ enzele allâh'", 2, 'say 5:49 2-6', "harekesiz 'hkum beynehum bi-mâ enzele'llâh' (2-6. kelime)",
  ('dizi 5 49 2 6', "hakeme beyn mâ enzele allâh", '2-6', "harekesiz sayım ('say 5:49 2-6') sûre içi 1, lemma dizisi ('dizi 5 49 2 6') sûre içi 2 (5:48, 5:49) — fark açıklanmadı, tam okuma sonu")),
 ("5:49", "'in tevellâ 'alime ennemâ'", 2, 'say 5:49 19-22 --on', "önek kesilmiş 'fe-in tevellev fa'lem ennemâ' (19-22. kelime)",
  ('dizi 5 49 19 22', "in tevellâ 'alime ennemâ", '19-22', "önek kesilmiş sayım ('say 5:49 19-22 --on') sûre içi 1, lemma dizisi ('dizi 5 49 19 22') sûre içi 2 — fark açıklanmadı, tam okuma sonu")),
 ("5:49", "'mâ enzele allâh'", 5, 'say 5:49 4-6', "harekesiz 'bi-mâ enzele'llâh' (4-6. kelime)", None),
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

VF_YAZI = {48: {1: "'ve enzelnâ'", 11: "'ve muheyminen'", 13: "'fa'hkum'", 18: "'ve lâ'", 29: "'ve minhâcâ'", 30: "'ve lev'", 36: "'ve lâkin'", 41: "'fe'stebiqu'", 47: "'fe-yunebbi'ukum'"}, 49: {1: "'ve eni'hkum'", 7: "'ve lâ'", 10: "'ve'hzerhum'", 19: "'fe-in'", 21: "'fa'lem'", 29: "'ve inne'"}, 50: {1: "'e-fe-hukme'", 4: "'ve men'"}}
sys.path.insert(0, '/home/claude/b17/yap')
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
open('/home/claude/b17/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '17')
BLOKLAR = [str(i) for i in range(1, 18)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR).replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '17').replace('\n', '; ')
EMS = open('/home/claude/b17/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '48', '50', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b17/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'
GLS = run('/home/claude/sunum/gloss_tara.py', '48', '50', '17').splitlines()

I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11): bu blokta araç değişmedi; sunum/sinifla.py (SON 50); yeni kök yamalar/yama_kok_5_48.py ile (şablon yama_kok_5_33.py); bölüm 6 kurallarının araçları (bolum4 / bolum5 / bolum6_kurallar, mutasyon_sina — MUT_SONUC) koşuldu",
 "kök tablosu: ölçümde '???' 5:48 için 1 — kök نهج ('minhâcâ' 29. kelime) eklendi (yamalar/yama_kok_5_48.py → kok_ekle_5.py; karşılık 'açık yol, yöntem'); yeniden ölçümde '???' 5:48-50 için 0; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 48 50 17'): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:48:11 مُهَيْمِن 'degil' — 've muheyminen 'aleyh', kural 'esmâ adı esmâ dışı göndergeyle → degil' (Kitap için gözetici) (esma_el_ekle → esma_kayit; bölüm 6 kuralı 14 — betikle, sapma B6_ESMA); 5:49 ve 5:50 esmâ yok; lafız 5:48, 5:49, 5:50; Rab yok",
 "esma_kayit: 5:48 'mühür hayır' (sınıf A/A; ölçüm MÜHÜRSÜZ — uyuşuyor), 5:49 'mühür hayır' (uyuşuyor), 5:50 'mühür hayır' (uyuşuyor)",
 "ölçüm: 5:48 '{{1|fâsıla تختلفون → ن, N sınıfı}}', '{{1|simetri \\[3, 2, 9, 1\\]}}', '{{1|harf 239 → harf3 225, isaret 14}}' ve '{{1|dış düğüm 5}}'; 5:49 '{{2|fâsıla لفسقون → ن, N sınıfı}}', '{{2|simetri \\[6, 4, 15, 2\\]}}', '{{2|harf 140 → harf3 135, isaret 5}}' ve '{{2|dış düğüm 0}}'; "
 "5:50 '{{3|aktör: adlı \\S+ 2\\. sırada \\(cins, rol mecrur\\)}}', '{{3|fâsıla يوقنون → ن, N sınıfı}}', '{{3|harf 47 → harf3 44, isaret 3}}' ve '{{3|dış düğüm 0}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 48 50 17'): KALAN_P",
 "ölçüm aktör: 5:48 ve 5:49 aktör yok; 5:50 adlı cahiliye (cins, mecrur) — A1'de 'adlı aktör' etiketiyle",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:48 emir, yasak, şart — IMPV 2 'fa'hkum' (13.), 'fe'stebiqu' (41.), PRO 1 'lâ' (18.), COND 1 'lev' (30.), EMPH 1 'le' (33.), biçim NEHY; 5:49 emir, yasak, şart — IMPV 3 'hkum' (2.), 've'hzerhum' (10.), 'fa'lem' (21.), PRO 1 'lâ' (7.), COND 1 'in' (19.), EMPH 1 'le' (33.), biçim NEHY; 5:50 soru — INTG 2 'e' (1.), 'men' (4.)",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:48 ★★★ (kaynak n, z=4,10; eşiği geçen başka: hapaks z=3,28); 5:49 ★★ (kaynak n, z=2,19); 5:50 yıldız yok",
 "fâsıla: 5:47 ن (الفاسقون) → 5:48 ن (تختلفون) → 5:49 ن (لفسقون) → 5:50 ن (يوقنون); hepsi N sınıfı; 5:47 ve 5:49 kapanışları 'fâsiqûn' (5:49 'le-fâsiqûn'); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:48 16:93 (emsal olarak basıldı) ve okunmuş ve henüz okunmamış başka ayetler; 5:49 ve 5:50 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' ile; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:48 'ilâ allâh merci' cemî' nebbe'e mâ kâne', 'musaddiq mâ beyn yed min', 'hakeme beyn mâ enzele allâh' ve 'mâ enzele allâh' süzgeç GEÇER, 'câ'e min haqq' GEÇMEZ; 5:49 'hakeme beyn mâ enzele allâh', 'in tevellâ 'alime ennemâ' ve 'mâ enzele allâh' GEÇER, 'erâde allâh en', 'lâ ittebe'a ehvâ'' ve 'mâ enzele allâh' (3 kelime / 2 ayet) GEÇMEZ; 5:50 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15 — ölçüt: 1P / 1S / 2MS / 2FS / 2MP / 2FP / 2D / 3MS / 3FS / 3D / 3MD / 3FD / 3MP / 3FP zamirlerin hepsi 'adsız', etiketin kendi parantezinde; adlı aktör ölçümün 'aktör: adlı' alanından): "
 "5:48 konuşan 1P (adsız), muhatap 2MS (adsız), muhatap 2MP (adsız), 3MP (adsız — 'beynehum', 'ehvâ'ehum'), 3MS (adsız — 'enzele', 'câ'eke', 'şâ'e', 'ce'ale', 'yebluve', 'âtâ', 'yunebbi'u' failleri; 'yedeyhi', ''aleyhi', 'fîhi'), Allah (lafız), 'kullin'; 5:49 muhatap 2MS (adsız), 3MP (adsız — 'yeftinûke', 'tevellev' failleri; 'beynehum', 'ehvâ'ehum', 've'hzerhum', 'yusîbehum', 'zunûbihim'), 3MS (adsız — 'enzele', 'yurîdu', 'yusîbe' failleri), Allah (lafız); "
 "5:50 'l-câhiliyyeti' (adlı aktör), 3MP (adsız — 'yebğûn', 'yûqinûn' failleri), Allah (lafız), 'men' — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): blokta 'qâle' yok, söz aralığı yok (A3 —); 5:48 konuşan 1P doğrudan anlatım; REM sapması (komut 'python3 sunum/bolum4_kurallar.py 48 50 17' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:48 've' (1., 11., 29.) CONJ, 've' (18., 30., 36.) REM, 'fa'hkum' (13.) CONJ, 'fe'stebiqu' (41.) ve 'fe-yunebbi'ukum' (47.) REM; 5:49 've' (1., 7., 10.) CONJ, 've inne' (29.) REM, 'fe-in' (19.) REM, 'fa'lem' (21.) RSLT; 5:50 'e-fe' (1.) SUP, 've men' (4.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:48 ◈B يدي ('yedeyhi' 8. kelime — B3; anlam notu: 'beyne yedeyh' — önündeki, mecaz); 5:49 ◈B أنس ('n-nâsi' 32. kelime — B1; anlam notu: insanlar, 'kesîran mine'n-nâs'); 5:50 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 48 50 17'): TETIKDISI; anılış: 5:48 kök جمع ('cemî'an' 46. kelime — hep birlikte, toplanma); 5:49 kök ولي ('tevellev' 20. kelime — yüz çevirme); oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:48 (16:93, 2:148), 5:50 (2:138) (kontrol.py ile); 5:49 D3 eşi yok; blok geçişi 5:47 → 5:48: ayetler arası kalıp 'bi-mâ enzele'llâh' (5:44, 5:45, 5:47, 5:48, 5:49) — sayım 'say 5:48 15-17' / 'say 5:49 4-6'; "
 "ayetler arası kalıp 'musaddiqan li-mâ beyne yedeyhi min' (5:46, 5:48) — sayım 'say 5:48 5-9'; ayetler arası kalıp 'hkum beynehum bi-mâ enzele'llâh' (5:48, 5:49) — lemma dizisi 'dizi 5 48 13 17'; ayetler arası kalıp 'tettebi' ehvâ'ehum' (5:48, 5:49) — sayım 'say 5:48 19-20'; bölüm içi tekrar, ardışık bağ yerine sayımla kayıt; "
 "D3 dışı bırakılan basılmış sayım eşleri: 5:48 'şâ'e'llâh' 10:49, 28:27 ve başkaları; 5:49 'yurîdu'llâh' 2:185, 3:176, 4:28, 5:6 ve başkaları — kalıp başına ölçüt: geniş kalıp, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:48 edim geçişi emir, şart → emir, yasak, şart; şahıs geçişi 3 → 2; şart → cevap (ayet içi; COND 'lev' 30. kelime: 've lev şâ'e'llâh' / 'le-ce'alekum ummeten vâhide' (33. kelime)); "
 "5:49 edim geçişi yok (emir, yasak, şart); şahıs geçişi 2 → 3; şart → cevap (ayet içi; COND 'in' 19. kelime: 'fe-in tevellev' / 'fa'lem ennemâ yurîdu'llâhu en yusîbehum bi-ba'di zunûbihim' (21. kelime)); 5:50 edim geçişi emir, yasak, şart → soru; şahıs geçişi yok",
 "sözdizimi (okuma; morph etiketiyle): 5:48 'musaddiqan' (5. kelime) ve 'muheyminen' (11. kelime) — nekre ACC (morph etiketi yalnız ACC; işlev okuması tam okuma sonu); 'fa'hkum' — emir (morph CONJ 'fe'); 've lâ tettebi'' — istînâf (morph REM) + olumsuz emir (PRO); 've lev şâ'e'llâh' — istînâf (morph REM) + şart (COND), 'le-ce'alekum' cevap (EMPH); 'li-yebluvekum' — amaç (morph PRP); "
 "5:49 've eni'hkum' — 'enzelnâ'ya atıf (morph CONJ), 'en' masdar (SUB); 'fe-in tevellev' — istînâf (morph REM) + şart (COND); 'fa'lem' — cevap (morph RSLT); 've inne kesîran' — istînâf (morph REM); 5:50 'e-fe-hukme' — 'fe' (morph SUP) + soru (INTG); 've men ahsenu' — istînâf (morph REM) + soru (INTG)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:48 'musaddiqan li-mâ beyne yedeyhi min' kalıbı 5:46'da İsa ve İncil için, 5:48'de Kitap için (sayım 'say 5:48 5-9'); 'hkum beynehum bi-mâ enzele'llâh' emri 5:48 ve 5:49'da muhataba (lemma dizisi 'dizi 5 48 13 17'); "
 "'tettebi' ehvâ'ehum' yasağı 5:48 ve 5:49'da (sayım 'say 5:48 19-20'); 5:48 kök جعل ikilemesi 'ce'alnâ' (1P; şeriat ve yol) / 'le-ce'alekum' (3MS; ümmet); bölümün 'Kitap ile hüküm' kısmı 5:48-50'de ('l-kitâbe', 'hkum'); 5:50 kök حكم ikilemesi — cahiliye hükmü / Allah'tan hüküm",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 17'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + "'; çıktı aynen): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle): 'le-ce'alekum ummeten vâhide' 5:48 'sizi bir ümmet kılardı' / 16:93 (emsal metninde) — tam okuma sonu; 'fe'stebiqu'l-xayrât' 5:48 'hayırlarda yarışın' / 2:148 — tam okuma sonu; 'ahsenu mine'llâh' 5:50 'Allah'tan daha güzel' / 2:138 — tam okuma sonu",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 48 50 17'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:48-50 tarayıcı adayı yok; L3 / L4 adayı yok",
 "aday 1039: blokta ayet içi ve ayetler arası karşıt çift kaydı yok; eşleme betikle: ADAY_P",
 "aday 1041: kök حكم 5:48-49 'hkum' (muhatap, emir) / 5:50 'hukme'l-câhiliyye' ve 'mine'llâhi hukman' — hükmün kaynakları karşılaştırılıyor; kök جعل 5:48 'ce'alnâ' (1P) / 'le-ce'alekum' (3MS, lafız) — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 7-3 — bölüm dört blok (14, 15, 16, 17); bu blok bölümü kapatıyor; başlıktaki 'Kitap ile hüküm' 5:48-50 ('l-kitâbe', 'hkum'); "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b17/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3 — betikle: komut 'python3 sunum/bolum5_kurallar.py 48 50 17'; lem_bozuk.py 17 çıktısı): 5:48:37 'belev', 5:49:10 'yahzeru', 5:49:12 'fetenu', 5:50:10 'yûqinu' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 48 50 → AYN_SONUC; sunum/bolum4_kurallar.py 48 50 17 → KHATA_HEPSI; sunum/bolum5_kurallar.py 48 50 17 → B5_HEPSI; sunum/bolum6_kurallar.py 48 50 17 → B6_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (sunum/sonradan.py --plan 17): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('enzele', 'kitâb', 'haqq', 'musaddiq', 'beyn', 'yed', 'muheymin', 'hakeme', 'ittebe'a', 'ehvâ'', 'câ'e', 'kull', 'ce'ale', 'şir'a', 'minhâc', 'şâ'e', 'umme', 'vâhide', 'belev' (morph LEM ham biçim), 'âtâ', 'istebeqa', 'xayra', 'merci'', 'cemî'', 'nebbe'e', 'kâne', 'ixtelefe', 'yahzeru' (morph LEM ham biçim), 'fetenu' (morph LEM ham biçim), 'ba'd', 'erâde', 'esâbe', 'zenb', 'kesîr', 'nâs', 'fâsiq', 'hukm', 'câhiliyye', 'beğâ', 'ahsen', 'qavm', 'yûqinu' (morph LEM ham biçim), 'tevellâ', ''alime'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (48, 50): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_48_50.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b13.txt', encoding='utf-8').read().splitlines()[:2]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '48', '50').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '48', '50', '17').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '48', '50', '17').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '48', '50', '17', '--tazelik-yok').splitlines()
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'),
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
