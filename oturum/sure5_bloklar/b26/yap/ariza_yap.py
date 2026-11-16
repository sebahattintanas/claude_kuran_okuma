# blok 26 (5:82-86) ARIZA oluşturucu — bölüm 11-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b26/olcum.txt'
os.environ['SAY2'] = '/home/claude/b26/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {33: {6: "'ve rasûlehû'", 7: "'ve yes'avne'", 18: "'ve erculuhum'", 30: "'ve lehum fi'l-âxirati'"}, 34: {9: "'fa'lemû'"}, 35: {6: "'ve'bteğû'", 9: "'ve câhidû'"}, 36: {11: "'ve mislehû'", 22: "'ve lehum 'azâbun'"}}
BOL = "'Lanetlenenler; Nasârâ'nın yakınlığı; gözyaşı dökenler'"


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
 ("5:82", "'ellezî qâle inne nasrânî'", 2, 'say 5:82 15-18', "harekesiz 'llezîne qâlû innâ nasârâ' (15-18. kelime; biçim öğesi 'innâ' — ölçüm kalıbında bitişik zamirli yazım)", None),
 ("5:84", "'mâ câ'e min'", 2, 'say 5:84 6-8 --on', "önek kesilmiş 've mâ câ'enâ min' (6-8. kelime)", ('dizi 5 84 6 8', "mâ câ'e min", '6-8', "biçim farkı (dizi 5 84 6 8): basılmamış eş önek")),
 ("5:84", "'câ'e min haqq'", 2, 'say 5:84 7-9', "harekesiz 'câ'enâ mine'l-haqq' (7-9. kelime)", ('dizi 5 84 7 9', "câ'e min haqq", '7-9', "biçim farkı (dizi 5 84 7 9): basılmamış eş zamir eki")),
 ("5:84", "'âmene allâh mâ'", 2, 'say 5:84 4-6', "harekesiz 'nu'minu bi'llâhi ve mâ' (4-6. kelime)", ('dizi 5 84 4 6', "âmene allâh mâ", '4-6', "biçim farkı (dizi 5 84 4 6): basılmamış eş zamir eki")),
 ("5:85", "'cenne cerey min taht neher xâlid fî' (LEM 'cerey' (morph LEM ham biçim))", 2, 'say 5:85 5-11', "harekesiz 'cennâtin tecrî min tahtihe'l-enhâru xâlidîne fîhâ' (5-11. kelime)", ('dizi 5 85 5 11', "cenne cerey min taht neher xâlid fî", '5-11', "biçim farkı (dizi 5 85 5 11): basılmamış eş yazım eş")),
 ("5:85", "'cenne cerey min taht neher' (LEM 'cerey' (morph LEM ham biçim))", 3, 'say 5:85 5-9', "harekesiz 'cennâtin tecrî min tahtihe'l-enhâr' (5-9. kelime)", None),
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

VF_YAZI = {82: {8: "'ve'llezîne'", 10: "'ve le-tecidenne'", 23: "'ve ruhbânen'", 24: "'ve ennehum'"}, 83: {1: "'ve izâ'", 19: "'fe'ktubnâ'"}, 84: {1: "'ve mâ lenâ'", 6: "'ve mâ câ'enâ'", 10: "'ve natma'u'"}, 85: {1: "'fe-esâbehumu'", 12: "'ve zâlike'"}, 86: {1: "'ve'llezîne'", 3: "'ve kezzebû'"}}
sys.path.insert(0, '/home/claude/b26/yap')
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
open('/home/claude/b26/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '26')
BLOKLAR = [str(i) for i in range(1, 27)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '26', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b26/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '82', '86', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b26/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else " — FARK VAR: 'say 5:86 2-4' meddesiz koşusu okunmamış 2 ayet (sûre içi 0) daha buluyor ('bi-âyâtinâ' medde yazım farkı); sûre içi sayı değişmiyor, sayım cümlesi meddeli koşuyla; tam okuma sonu"
GLS = run('/home/claude/sunum/gloss_tara.py', '82', '86', '26').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_82_86.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:82', '5:83', '5:84', '5:85', '5:86'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_82_86.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '5:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '5:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(82, 87))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "5:83 'izâ' ('ve izâ' 1. kelime — morph T, zaman); 5:83 kök رأي ('terâ' 7. kelime — görme) ve kök دمع ('d-dem'i' 11. kelime — gözyaşı): tetik listesinde yok; 5:85 kök جنن ('cennâtin' 5. kelime — cennet) ve kök تحت ('tahtihe' 8. kelime — alt): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '82', '86', '26')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b26/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 27)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(82, 87))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/ham_elle.txt — 5:84 'yudxilenâ' (12. kelime) LEM 'udxile' (morph LEM ham biçim), edilgen görünümlü, lem_bozuk.py bayraklamıyor, elle listeye eklendi (bölüm 5 kuralı 5); "
 "sunum/bolum10_kurallar.py kural 6 — ölçüm xref alanında ' · ' ile ayrılmış sonraki kalıpların hedefleri okunmuyordu (5:83'te iki kalıp; düzeltme sonrası 'okunmuş 3 ayet'), sunum/mutasyon_sina.py bu düzeltmenin sınaması (5:83) ve 5:77 sınamasının beklenen sayısının düzeltmeyle güncellenmesi ('okunmuş 8 ayet'); sunum/sinifla.py SON ve sunum/basilan.txt blok akışı (§3 adım 2 ve emsal işaretlemesi); mutasyon_sina — MUT_SONUC; geriye dönük koşu son araç değişikliğinden sonra yeniden üretildi (GERI_P) — yeni 30 — bolum10_kurallar 22 (kural 6 düzeltmesi: okunmuş bloklarda xref alanının sonraki kalıp hedefleri eski kayıtlarda sayılmamıştı), bolum5_kurallar 3 (sunum/ham_elle.txt'e 'udxile' eklenmesi: eski kayıtlarda bu LEM notsuz), bolum9_kurallar 4 (sonradan basılan 5:14, 5:82 ve 5:84 r5_gerekce çıktısını değiştirdi), gloss_tara KAPSAMAYAN 1 (bu bloğun satırı, tam okuma sonu); düşen 12 — araç değişti; kayıtlar geriye dönük yeniden yazılmadı",
 "kök tablosu: ölçümde '???' 5:82 için 2 (HAPAKS alanı ve kökler alanı; kök قسس — 22. kelime 'qissîsîne') — kök tabloya eklendi (yamalar/yama_kok_5_82.py → kok_ekle_5.py; anlam 'keşiş, rahip; kıssîs'; 1 ayet; docstring dosya adı ve bölümle — bölüm 4 kuralı 16), ölçüm yeniden alındı, '???' 0; 5:83, 5:84, 5:85 ve 5:86 '???' 0; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 82 86 26'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: bu blokta esmâ yok (5:82, 5:83, 5:84, 5:85 ve 5:86); lafız 5:84 ve 5:85; Rab 5:83 ve 5:84; 5:82 ve 5:86 lafız yok, Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 82 86 26'): " + EMH,
 "ölçüm: 5:82 '{{1|HAPAKS: قسس}}', '{{1|hapaks z=3,28}}', '{{1|fâsıla يستكبرون → ن, N sınıfı}}', '{{1|simetri \\[3, 5, 13, 1\\]}}', '{{1|harf 138 → harf3 128, isaret 10}}' ve '{{1|dış düğüm 0}}'; "
 "5:83 '{{2|fâsıla ٱلشهدين → ن, N sınıfı}}', '{{2|EDİLGEN 1/8 fiil, pas z=0,38}}', '{{2|simetri \\[3, 1, 10, 1\\]}}', '{{2|harf 92 → harf3 89, isaret 3}}' ve '{{2|dış düğüm 3}}'; "
 "5:84 '{{3|fâsıla ٱلصلحين → ن, N sınıfı}}', '{{3|simetri \\[3, 1, 6, 1\\]}}', '{{3|harf 62 → harf3 62, isaret 0}}' ve '{{3|dış düğüm 0}}'; "
 "5:85 '{{4|fâsıla ٱلمحسنين → ن, N sınıfı}}', '{{4|harf 66 → harf3 63, isaret 3}}' ve '{{4|dış düğüm 1}}'; "
 "5:86 '{{5|fâsıla ٱلجحيم → م, N sınıfı}}', '{{5|harf 42 → harf3 39, isaret 3}}', '{{5|dış düğüm 1}}', '{{5|nakarat 2 \\(temsil \\[5, 10\\]\\)}}' ve '{{5|esit2 → 5:10 oran 1,0000 kademe TAM}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 82 86 26'): KALAN_P",
 "ölçüm aktör: 5:82 '{{1|adlı يَهُود 7\\. sırada \\(cins, rol meful\\)}}' — 'tecidenne' 2. mef'ûlü, '{{1|adlı نَصْرانِيّ 18\\. sırada \\(cins, rol fail\\)}}' — söz içi 'innâ' haberi (ölçüm rolü 'fail'; araç tanımı farkı, okuma); 5:83, 5:84, 5:85 ve 5:86 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 5:82 haber — EMPH 4 'le' ve 'nne' (1. ve 10.), NEG 1 'lâ' (25.); 5:83 emir — IMPV 1 'ktubnâ' (19.); 5:84 soru — INTG 1 'mâ' (1.), NEG 1 'lâ' (3.); 5:85 haber — kip yok; 5:86 haber — kip yok; "
 "morph REM ('fe' 5:83 19.; 've' 5:84 1., 5:85 12., 5:86 1.), CIRC ('ve natma'u' 5:84 10.) ve CAUS ('fe-esâbehumu' 5:85 1.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:82 ★★★ (kaynak hapaks, z=3,28); 5:83, 5:84, 5:85 ve 5:86 yıldız yok",
 "fâsıla: 5:82 ن (يستكبرون) → 5:83 ن (ٱلشهدين) → 5:84 ن (ٱلصلحين) → 5:85 ن (ٱلمحسنين) → 5:86 م (ٱلجحيم); bölüm kapanışında kafiye م'ye kırılıyor (5:86, 5:10 ile eş kapanış); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6 — basılmamış hedefler sinifla sayısıyla): 5:82 xref yok (bağ yalnız nakarat3); 5:83 okunmuş 3 ayet (iki xref kalıbı); 5:84 xref yok; 5:85 okunmuş 1 ayet; 5:86 5:10 (emsal olarak basıldı) ve okunmuş 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' ile; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:82 'ellezî qâle inne nasrânî' süzgeç GEÇER; 5:83 nakarat3 yok; 5:84 'mâ câ'e min', 'câ'e min haqq' ve 'âmene allâh mâ' GEÇMEZ; 5:85 'cenne cerey min taht neher xâlid fî' ve 'cenne cerey min taht neher' GEÇER; 5:86 'ellezî kefera kezzebe âye _ ashâb cahîm' GEÇER (tür tam — R5 satırı yok, R5 yalnız 'tür ic'; 5:10 emsal olarak basıldı, kalıp eşi bag'de)",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş): "
 "5:82 muhatap 2MS (adsız — 'tecidenne' 1. ve 10. kelime), 3MP (adsız — 'âmenu', 'eşrakû', 'qâlû', 'yestekbirûn' failleri; 'aqrabehum', 'minhum', 'ennehum'), Yahudiler (adlı cins), söz içi konuşan 1P (adsız — 'innâ'), Nasârâ (adlı cins); "
 "5:83 3MP (adsız — 'semi'û', ''arafû', 'yeqûlûne' failleri; 'a'yunehum'), 'unzile' (3MS edilgen; naib-i fail mevsûl), muhatap 2MS (adsız — 'terâ'), 'tefîdu' (3FS, adsız), söz içi Rab, söz içi konuşan 1P (adsız) ve muhatap 2MS (adsız — 'fe'ktubnâ'); "
 "5:84 söz içi konuşan 1P (adsız), Allah (lafız), 'câ'enâ' (3MS, adsız), Rab ('yudxilenâ' faili — 3MS fiil uyumu); "
 "5:85 Allah (lafız; 'esâbe' faili — 3MS fiil uyumu), 3MP (adsız — 'esâbehumu' mef'ûlü, 'qâlû' faili), 'l-enhâru' ('tecrî' faili — 3FS fiil uyumu), 3FS (adsız — 'tahtihe', 'fîhâ'); "
 "5:86 3MP (adsız — 'keferû', 'kezzebû' failleri), 1P (adsız — 'âyâtinâ'), 'ulâ'ike' (işaret) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): 5:82 'qâlû innâ nasârâ' — söz içi 'innâ nasârâ' (17-18. kelime), mealde tırnak, ayet içinde açılıp kapanıyor; "
 "5:83 'yeqûlûne rabbenâ âmennâ' — söz 17. kelimede açılıyor, 5:84 sonunda kapanıyor (5:83 A3 '5:84 sonuna dek', 5:84 A3 'söz sürüyor'; mealde tırnak 5:83'te açılır, 5:84'te kapanır); 'qul' yok (bölüm 10 denetimi kuralı 8); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 82 86 26' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:82 've'llezîne' (8.), 've le-tecidenne' (10.), 've ruhbânen' (23.), 've ennehum' (24.) CONJ; 5:83 've izâ' (1.) CONJ, 'fe'ktubnâ' (19.) REM; 5:84 've mâ lenâ' (1.) REM, 've mâ câ'enâ' (6.) CONJ, 've natma'u' (10.) CIRC; 5:85 'fe-esâbehumu' (1.) CAUS, 've zâlike' (12.) REM; 5:86 've'llezîne' (1.) REM, 've kezzebû' (3.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:82 ◈B أنس ('n-nâsi' 3. kelime — B1; anlam notu: düşmanlığı ölçülen insanlar); 5:83 ◈B سمع ('semi'û' 2. kelime — B3; anlam notu: indirileni işitme); 5:83 ◈B عين ('a'yunehum' 8. kelime — B3; anlam notu: yaşla taşan gözler); 5:85 ◈K نهر ('l-enhâru' 9. kelime — K1; anlam notu: cennetlerin altından akan ırmaklar); 5:84 ve 5:86 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 82 86 26'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:82 (5:14), 5:83 (3:53), 5:86 (5:10) (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); 5:84 ve 5:85 D3 eşi yok; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:82 edim geçişi şart → haber; şahıs geçişi yok; söz açılır / söz kapanır (ayet içi); 5:83 edim geçişi haber → emir; söz açılır (17. kelime); 5:84 edim geçişi emir → soru; şahıs geçişi 3 → 1; söz kapanır; "
 "5:85 edim geçişi soru → haber; şahıs geçişi 1 → 3; 5:86 bölüm kapanışı (bölüm 10 denetimi kuralı 2); edim geçişi yok (haber → haber); şahıs geçişi yok",
 "sözdizimi (okuma; morph etiketiyle): 5:82 'le-tecidenne … le-tecidenne' — kasem cevabı tekidi (morph EMPH 'le' + 'nne'); 'eşedde'n-nâsi 'adâveten' ve 'aqrabehum meveddeten' — ism-i tafdîl + temyiz; 'zâlike bi-enne minhum qissîsîne ve ruhbânen' — 'enne' ismi muahhar, haber 'minhum' (morph ACC); "
 "5:83 'izâ semi'û … terâ' — zaman şartı ve cevabı ('izâ' morph T, ölçüm edim alanında şart yok); 'yeqûlûne' — muzâri söz fiili; 'ktubnâ' — dua emri (morph IMPV); "
 "5:84 'mâ lenâ lâ nu'minu' — soru ve olumsuz muzâri (morph INTG + NEG); 'natma'u en yudxilenâ' — hâl (morph CIRC), 'en' masdar (morph SUB); "
 "5:85 'fe-esâbehumu'llâhu bi-mâ qâlû' — sebep (morph CAUS), 'mâ' masdar; 'xâlidîne fîhâ' — mansub çoğul etken ortaç (morph ACC); 've zâlike cezâ'u'l-muhsinîn' — istînâf (morph REM); "
 "5:86 've'llezîne keferû … ulâ'ike ashâbu'l-cahîm' — mübteda ve işaretle başlayan haber cümlesi (morph REM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:82 kök وجد ikilemesi 'tecidenne' (1., 10. kelime) ve kök أمن ikilemesi 'âmenu' (6., 14. kelime); "
 "5:82 'le-tecidenne' ile açılıyor; 5:83 ve 5:84'te söz içi 'rabbenâ' / 'rabbunâ' (17. ve 13. kelime); 5:83 'mine'l-haqqi' (14-15. kelime) ve 5:84 'mine'l-haqqi' (8-9. kelime)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 26'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp): 'llezîne qâlû innâ nasârâ' 5:82 ''Biz Nasârâ'yız' diyenler' / 5:14 ''Biz Nasârâ'yız' diyenler' (emsal metninde) — çakışma değil; "
 "'fe'ktubnâ ma'a'ş-şâhidîn' 5:83 'bizi şahitlerle birlikte yaz' / 3:53 'bizi şahitlerle birlikte yaz' (emsal metninde) — çakışma değil; 'rabbenâ âmennâ' 5:83 'Rabbimiz, iman ettik' / 3:53 'Rabbimiz, … inandık' — karşılık farkı (tam okuma sonu; 'âmene' kararı meal karşılık farkı maddesinde); "
 "'ve'llezîne keferû ve kezzebû bi-âyâtinâ ulâ'ike ashâbu'l-cahîm' 5:86 / 5:10 (emsal metninde) — meal birebir, çakışma değil; 'qissîs' karşılığı 'keşiş', 'ruhbân' karşılığı 'rahip' (kök رهب tablo anlamı 'korku, çekinme' — gloss taraması KAPSAMAYAN listesinde)",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük): " + (MKK or 'yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 82 86 26'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:82, 5:83, 5:84, 5:85 ve 5:86 tarayıcı vermedi (cipa_tarama5_adaylari.json); doğa iddiası yok (olgu=False); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:82 ('eşedde'n-nâsi 'adâveten' / 'aqrabehum meveddeten') — okuma; ayetler arası 5:85 / 5:86 ('cennâtin' / 'ashâbu'l-cahîm'); 5:83, 5:84, 5:85 ve 5:86 ayet içi karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök وجد 5:82 'tecidenne' (1. ve 10. kelime) — düşmanlık ve sevgi karşıtlığında bir fiil; kök حقق 5:83 ve 5:84 'mine'l-haqqi' — tanınan hak / gelen hak; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 11-2 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (25, 26); bu blok bölümü kapatıyor; başlıktaki 'Nasârâ'nın yakınlığı' 5:82, 'gözyaşı dökenler' 5:83; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b26/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9 — betikle: komut 'python3 sunum/bolum5_kurallar.py 82 86 26'; lem_bozuk.py 26 çıktısı): 5:83:9 'tefîdu', 5:84:10 'yatma'u', 5:85:6 'cerey' — lem_bozuk bayrağı; 5:84:12 'udxile' (sunum/ham_elle.txt) — elle ham listesi; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 82 86 → AYN_SONUC; sunum/bolum4_kurallar.py 82 86 26 → KHATA_HEPSI; sunum/bolum5_kurallar.py 82 86 26 → B5_HEPSI; sunum/bolum6_kurallar.py 82 86 26 → B6_HEPSI; sunum/bolum7_kurallar.py 82 86 26 → B7_HEPSI; sunum/bolum8_kurallar.py 82 86 26 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 82 86 26 → B9_HEPSI; sunum/bolum10_kurallar.py 82 86 26 → B10_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 26 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('ellezî', 'qâle', 'inne', 'nasrânî', ''ayn', 'tefîdu' (morph LEM ham biçim), 'min', 'dem'', 'rabb', 'âmene', 'mâ', 'câ'e', 'haqq', 'allâh', 'cenne', 'cerey' (morph LEM ham biçim), 'taht', 'neher', 'xâlid', 'fî', 'kefera', 'kezzebe', 'âye', 'ashâb', 'cahîm'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (82, 86): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_82_86.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b26.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '82', '86').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '82', '86', '26').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '82', '86', '26').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '82', '86', '26', '--tazelik-yok').splitlines()
    B7 = run('/home/claude/sunum/bolum7_kurallar.py', '82', '86', '26').splitlines()
    B8 = run('/home/claude/sunum/bolum8_kurallar.py', '82', '86', '26').splitlines()
    B9 = run('/home/claude/sunum/bolum9_kurallar.py', '82', '86', '26').splitlines()
    B10 = run('/home/claude/sunum/bolum10_kurallar.py', '82', '86', '26').splitlines()
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI), 'B6_ESMA': ('; '.join(l[5:] for l in B6 if 'esmâ kural' in l and l.startswith('HATA')) or 'sapma 0')}
    I_cur = list(I_HAM)
    for k, v in REP.items(): I_cur = I_cur[:len(BEK)] + [x.replace(k, v) for x in I_cur[len(BEK):]]  # bölüm 9 kuralı 9: taşınan denetim maddelerine yer tutucu değişimi uygulanmaz
    I_cur[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3, bölüm 6 kuralı 2 — komut 'python3 sunum/cakisma.py' + sûre 5'in okunmuş bütün ARIZA dosyaları; bu bloğun karşılıklarına dokunan gruplar ve son dosyaya dokunan KÖK grupları; grup başına tam bir kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
                  + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
    if I_cur == onceki: break
    onceki = list(I_cur)
yaz(I_cur)
print('yazıldı', len(I_cur), 'tur', tur)
print('\n'.join(CAK_L))
print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)
