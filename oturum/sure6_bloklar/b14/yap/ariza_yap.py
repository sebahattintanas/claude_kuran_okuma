# sûre 6 blok 14 (6:59-61) ARIZA oluşturucu — bölüm 7-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b14/olcum.txt'
os.environ['SAY2'] = '/home/claude/b14/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b13.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {}
BOL = "'Gaybın anahtarları; karanlıklardan kurtaran'"


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
 ("6:60", "'summe nebbe'e mâ kâne'", 2, 'say 6:60 18-21', "harekesiz 'summe yunebbi'ukum bimâ kuntum' (18-21. kelime)", ('dizi 6 60 18 21', "summe nebbe'e mâ kâne", '18-21', "biçim farkı (dizi 6 60 18 21): basılmamış eş fiil çekimi, zamir eki")),
 ("6:60", "'nebbe'e mâ kâne 'amile'", 2, 'say 6:60 19-22 --on', "önek kesilmiş 'yunebbi'ukum bimâ kuntum ta'melûn' (19-22. kelime)", ('dizi 6 60 19 22', "nebbe'e mâ kâne 'amile", '19-22', "biçim farkı (dizi 6 60 19 22): basılmamış eş fiil çekimi, zamir eki, önek")),
 ("6:60", "'nebbe'e mâ kâne'", 4, 'say 6:60 19-21 --on', "önek kesilmiş 'yunebbi'ukum bimâ kuntum' (19-21. kelime)", ('dizi 6 60 19 21', "nebbe'e mâ kâne", '19-21', "biçim farkı (dizi 6 60 19 21): basılmamış eş fiil çekimi, zamir eki, önek; basılmamış eş fiil çekimi, zamir eki; basılmamış eş önek")),
 ("6:60", "'bi-mâ kâne 'amile'", 3, 'say 6:60 20-22', "harekesiz 'bimâ kuntum ta'melûn' (20-22. kelime)", ('dizi 6 60 20 22', "bi-mâ kâne 'amile", '20-22', "biçim farkı (dizi 6 60 20 22): 6:43 fiil çekimi, zamir eki, önek; basılmamış eş fiil çekimi, zamir eki, önek; basılmamış eş fiil çekimi, zamir eki; basılmamış eş fiil çekimi, zamir eki, önek; basılmamış eş fiil çekimi, zamir eki; biçim öğesi ''amile' çekimi (lemma dizisi sûre içi 6, nakarat3 3); öneksiz eş koşusu (dizi 6 60 20 22): 6:43 → önek kesilmiş sûre içi 5; basılmamış eş → önek kesilmiş sûre içi 5; basılmamış eş → önek kesilmiş sûre içi 2; basılmamış eş → önek kesilmiş sûre içi 5; basılmamış eş → önek kesilmiş sûre içi 2")),
 ("6:61", "'_ qâhir fevq 'abd'", 2, 'say 6:61 1-4', "harekesiz 've huve'l-qâhiru fevqa 'ibâdih' (1-4. kelime)", None),
 ("6:61", "'hattâ izâ câ'e'", 3, 'say 6:61 8-10', "harekesiz 'hattâ izâ câ'e' (8-10. kelime)", ('dizi 6 61 8 10', "hattâ izâ câ'e", '8-10', "biçim farkı (dizi 6 61 8 10): 6:25 fiil çekimi, zamir eki; 6:31 fiil çekimi, zamir eki")),
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

VF_YAZI = {59: {1: "'ve 'indehû'", 8: "'ve ya'lemu'", 12: "'ve'l-bahr'", 13: "'ve mâ'", 19: "'ve lâ'", 24: "'ve lâ'", 26: "'ve lâ'"}, 60: {1: "'ve huve'", 5: "'ve ya'lemu'"}, 61: {1: "'ve huve'", 5: "'ve yursilu'", 15: "'ve hum'"}}
sys.path.insert(0, '/home/claude/b14/yap')
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
open('/home/claude/b14/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '14')
BLOKLAR = [str(i) for i in range(1, 15)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '14', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b14/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '59', '61', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b14/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b14/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '59', '61', '14').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_59_61.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:59', '6:60', '6:61'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_59_61.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(59, 62))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:60 kök جرح ('cerahtum' 7. kelime — işleme, kazanma); 6:61 'izâ' (9. kelime — morph T, zaman): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '59', '61', '14')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b14/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 15)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(59, 62))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/yasakli.sh IZIN (bölüm 10 denetimi kuralı 10) — 23:99 emsal alıntısında 'ehad' karşılığı (sayma değil); sunum/bolum12_kurallar.py kural 4 ve sunum/bolum8_kurallar.py kural 5 'bi-' önekini karşılaştırmada düşürür — bolum7 kural 12 'ب' önekli nakarat3 kalıbına 'bi-' adı ister (6:60 'bi-mâ kâne 'amile'); sunum/bolum22_kurallar.py kural 3 (LEMMA_YAZIM_BIR) yalnız bu bloğun kayıtlarında yeni giren üyeyi içeren a / e çiftini işaretler — kayıtlar geriye dönük yeniden yazılmadığı için eski kayıtlardaki 'câ'a' / 'câ'e' çifti bekleyen_ariza_6_b13 kaydında (sûre 6 bölüm 6 denetimi kuralı 3); mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 182",
 "geriye dönük koşu (araç değişen blok — bekleyen_ariza_6_b13 elle önerisi (8) GERIYE_DONUK_ZORUNLU; komut 'python3 sunum/geriye_donuk.py b14 yamalar/geriye_donuk_6_b13.txt'): düşen 8 (araç değişti 7, basılan değişti 1, kayıt değişti 0), yeni 27; kayıtlar geriye dönük yeniden yazılmadı; isabetler tam okuma sonu listesinde (yamalar/geriye_donuk_6_b14.txt)",
 "kök tablosu: ölçümde '???' 6:59-61 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 59 61 14'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:59 'mâ fi'l-berri ve'l-bahr' (9-12. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge); 6:59 'illâ fî kitâbin mubîn' (28-31. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge); "
 "6:61 've yursilu 'aleykum hafaza' (5-7. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge); 6:61 'câ'e ehadekumu'l-mevt' (10-12. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge); 6:60 esmâ yok; "
 "lafız yok; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 59 61 14'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 6:59, 6:61 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı): " + EMH,
 "ölçüm: 6:59 '{{1|fâsıla مبين → ن, N sınıfı}}', '{{1|simetri \\[4, 4, 17, 1\\]}}', '{{1|harf 119 → harf3 111, isaret 8}}', '{{1|dış düğüm 0}}' ve '{{1|biçim HASR}}'; "
 "6:60 '{{2|fâsıla تعملون → ن, N sınıfı}}', '{{2|simetri \\[3, 1, 15, 1\\]}}', '{{2|harf 97 → harf3 94, isaret 3}}', '{{2|dış düğüm 0}}' ve '{{2|EDİLGEN 1/8 fiil, pas z=0,38}}'; "
 "6:61 '{{3|fâsıla يفرطون → ن, N sınıfı}}', '{{3|simetri \\[3, 8, 15, 1\\]}}', '{{3|harf 73 → harf3 71, isaret 2}}', '{{3|dış düğüm 1}}' ve '{{3|sayı işareti أَحَد}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 59 61 14'): KALAN_P",
 "ölçüm aktör: 6:59-61 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:59 haber — NEG 5 'lâ' (4.), 'mâ' (13.), 've lâ' (19., 24., 26.), RES 3 'illâ' (6., 17., 28.); 6:60 haber — kip yok; 6:61 haber — NEG 1 'lâ' (16.); "
 "morph LOC (''indehû' 6:59 1.), PRP ('li' 6:60 12.), INC ('hattâ' 6:61 8.), T ('izâ' 6:61 9.), CIRC ('ve' 6:61 15.), REM ('ve' 6:59 1.; 've' 6:61 5.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:59 ★ (kaynak n, z=1,97); 6:60 ve 6:61 yıldız yok",
 "fâsıla: 6:58 ن → 6:59 ن (مبين) → 6:60 ن (تعملون) → 6:61 ن (يفرطون) — N sınıfı sürüyor; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:61 23:99 (emsal olarak basıldı); 6:59 xref yok; 6:60 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:60 'summe nebbe'e mâ kâne', 'nebbe'e mâ kâne 'amile', 'nebbe'e mâ kâne' ve 'bi-mâ kâne 'amile' süzgeç GEÇER; 6:61 '_ qâhir fevq 'abd' ve 'hattâ izâ câ'e' süzgeç GEÇER; 6:59 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; edilgen fiilde naib-i fail — sûre 6 bölüm 2 denetimi kuralı 5; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:59 3MS (adsız — gönderge 6:58 12. kelime), 3FS ('tesqutu' 14. kelime — fail 16. kelime; zamirler adsız — gönderge 'mefâtihu' ve 'veraqatin'); "
 "6:60 3MS (adsız — gönderge 6:58 12. kelime ve 'n-nehâri'; 'li-yuqdâ' edilgen — naib-i faili 'ecelun' 13. kelime), muhatap 2MP; "
 "6:61 3MS (adsız — gönderge 6:58 12. kelime; 'teveffethu' nesne zamiri 'ehadekumu'ya döner; 'câ'e' 10. kelime — fail 12. kelime), 3FS ('teveffethu' 13. kelime — fail 14. kelime), muhatap 2MP, konuşan 1P, 3MP (adsız — gönderge 'rusulunâ' 14. kelime) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:59-61 söz yok; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 59 61 14' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:59 've 'indehû' (1.) REM, 've ya'lemu' (8.), 've'l-bahr' (12.), 've mâ' (13.), 've lâ' (19., 24., 26.) CONJ; 6:60 've huve' (1.), 've ya'lemu' (5.) CONJ; 6:61 've huve' (1.) CONJ, 've yursilu' (5.) REM, 've hum' (15.) CIRC",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:59 ◈K بحر ('l-bahr' 12. kelime — K1); 6:59 ◈K أرض ('l-ardi' 23. kelime — K1); 6:60 ◈K ليل ('l-leyli' 4. kelime — K1); 6:60 ◈K نهر ('n-nehâri' 8. kelime — K1); 6:60 ◈K أجل ('ecelun' 13. kelime — K2; anlam notu: belirlenmiş süre); 6:61 ◈B موت ('l-mevtu' 12. kelime — B4)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 59 61 14'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:59 (10:61); 6:61 (23:99); 6:60 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş (6:61 '_ qâhir fevq 'abd' — 6:18), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:59 şahıs geçişi 2 → 3, edim geçişi emir, şart → haber, bölüm açılışı; 6:60 şahıs geçişi 3 → 2, edim geçişi yok; 6:61 şahıs geçişi 2 → 3, edim geçişi yok; "
 "şahıs beraberliği yok (sûre 6 bölüm 1 denetimi kuralı 9); ölçüm iltifât 6:59-61 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:59 've 'indehû mefâtihu'l-ğayb' — istînâf, haber öne (morph REM + LOC); 'lâ ya'lemuhâ illâ huve' — hasr (morph NEG + RES); 've mâ tesqutu min veraqatin illâ ya'lemuhâ' — atıf, nefy ve istisna (morph CONJ + NEG + RES), 'min' zâid; "
 "6:60 'li-yuqdâ ecelun musemmâ' — amaç (morph PRP), edilgen; 6:61 'hattâ izâ câ'e ehadekumu'l-mevt' — zaman (morph INC + T); 've hum lâ yufarritûn' — hâl (morph CIRC)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:59 'illâ fî kitâbin mubîn' — 10:61 ile eş (sayım: 'say 6:59 28-31'); 6:59 kök علم ikilemesi (×3); "
 "6:60 'summe' 9., 15. ve 18. kelimede sıralıyor; 6:61 'hattâ izâ câ'e' — 23:99 ile eş (sayım: 'say 6:61 8-10'); 6:61 kök رسل ikilemesi; 6:60 ve 6:61 'vefat ettir-' ('yeteveffâkum' / 'teveffethu') ortak lemma",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 14'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'illâ fî kitâbin mubîn' 6:59 'ki apaçık bir kitapta olmasın' / 10:61 'mutlaka apaçık bir kitaptadır' (emsal metninde) — çakışma — tam okuma sonu ('ki … olmasın' / 'mutlaka' istisna karşılığı); "
 "'hattâ izâ câ'e' 6:61 'Nihayet birinize ölüm geldiğinde' / 23:99 'Nihayet onlardan birine ölüm geldiğinde' (emsal metninde) — çakışma — tam okuma sonu ('birinize' / 'onlardan birine' zamir farkı); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:59 'ya'lemuhâ' IMPF IND — meal 'bilir'; 've ya'lemu' IMPF IND — meal 'bilir'; 'tesqutu' IMPF IND — meal 'düşen'; 'ya'lemuhâ' IMPF IND — meal 'bilmesin'; "
 "6:60 'yeteveffâkum' IMPF IND — meal 'vefat ettiren'; 've ya'lemu' IMPF IND — meal 'bilen'; 'cerahtum' PERF — meal 'işlediğiniz'; 'yeb'asukum' IMPF IND — meal 'uyandırır'; 'li-yuqdâ' IMPF SUBJ edilgen — meal 'tamamlansın'; 'yunebbi'ukum' IMPF IND — meal 'haber verir'; 'kuntum' PERF — meal 'olduklarınız'; 'ta'melûn' IMPF IND — meal 'yapmakta'; "
 "6:61 've yursilu' IMPF IND — meal 'gönderir'; 'câ'e' PERF — meal 'geldiğinde'; 'teveffethu' PERF — meal 'vefat ettirir'; 'yufarritûn' IMPF IND — meal 'ihmal etmezler'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 59 61 14'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:60 tarayıcı adayı (kök أجل, ليل, نهر; B_ta’lîl) — çıpa değil: gece vefat ettirme ve gündüz diriltme uyku / uyanış benzetmesi, doğa iddiası yok (olgu=False); 6:59 ve 6:61 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:59 ('l-berri' / 've'l-bahr'; 'ratbin' / 'yâbisin'); 6:60 ('bi'l-leyli' / 'bi'n-nehâri'; 'yeteveffâkum' / 'yeb'asukum'); 6:61 yok; "
 "ayetler arası çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök علم 6:58 ('a'lemu'), 6:59 ('ya'lemuhâ') ve 6:60 ('ve ya'lemu'); kök عند 6:58 (''indî') ve 6:59 ('ve 'indehû'); kök وفي 6:60 ('yeteveffâkum') ve 6:61 ('teveffethu'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 7-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 14 ve 15; bu blok bölümü açıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b14/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 59 61 14'; lem_bozuk.py 14 çıktısı): lem_bozuk bayrağı 6:59 14. kelime (سُقِطَ — 'tesqutu') ve 6:60 7. kelime (جَرَحْ — 'cerahtum'), meal kayıtlarında '(morph LEM ham biçim)' notu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 59 61 → AYN_SONUC; sunum/bolum4_kurallar.py 59 61 14 → KHATA_HEPSI; sunum/bolum5_kurallar.py 59 61 14 → B5_HEPSI; sunum/bolum6_kurallar.py 59 61 14 → B6_HEPSI; sunum/bolum7_kurallar.py 59 61 14 → B7_HEPSI; sunum/bolum8_kurallar.py 59 61 14 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 59 61 14 → B9_HEPSI; sunum/bolum10_kurallar.py 59 61 14 → B10_HEPSI; sunum/bolum11_kurallar.py 59 61 14 → B11_HEPSI; sunum/bolum12_kurallar.py 59 61 14 → B12_HEPSI; sunum/bolum13_kurallar.py 59 61 14 → B13_HEPSI; sunum/bolum14_kurallar.py 59 61 14 → B14_HEPSI; sunum/bolum15_kurallar.py 59 61 14 → B15_HEPSI; sunum/bolum16_kurallar.py 59 61 14 → B16_HEPSI; sunum/bolum17_kurallar.py 59 61 14 → B17_HEPSI; sunum/bolum18_kurallar.py 59 61 14 → B18_HEPSI; sunum/bolum19_kurallar.py 59 61 14 → B19_HEPSI; sunum/bolum20_kurallar.py 59 61 14 → B20_HEPSI; sunum/bolum21_kurallar.py 59 61 14 → B21_HEPSI; sunum/bolum22_kurallar.py 59 61 14 → B22_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine ekleme: ariza_6_59_61.txt — 23:99 emsal alıntısı (emsal meali aynen; sayı sözcüğü değil, 'ehad' karşılığı)",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 14 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('summe', 'nebbe'e', 'mâ', 'kâne', ''amile', 'qâhir', 'fevq', ''abd', 'hattâ', 'izâ', 'câ'e', 'ehad', 'mevt'); lemmasız öğe 'huve' için joker '_' ('_ qâhir fevq 'abd' — 6:18 adıyla eş); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (59, 61): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_59_61.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b13.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '59', '61'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '59', '61', '14'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '59', '61', '14'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '59', '61', '14', '--tazelik-yok')}
    for _n in range(7, 23): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '59', '61', '14')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22 = [_R['B%d' % _n].splitlines() for _n in range(6, 23)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
