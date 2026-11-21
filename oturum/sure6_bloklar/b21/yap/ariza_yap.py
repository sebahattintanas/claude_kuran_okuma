# sûre 6 blok 21 (6:91-92) ARIZA oluşturucu — bölüm 11-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b21/olcum.txt'
os.environ['SAY2'] = '/home/claude/b21/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b20.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {}
BOL = "'Kitap indirmeyi inkâr edenler; ölüm sarhoşlukları'"


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
 ("6:91", "'mâ enzele allâh'", 2, 'say 6:91 8-10', "harekesiz 'mâ enzela'llâhu' (8-10. kelime)", None),
 ("6:92", "'zâ kitâb enzele mubârak'", 2, 'say 6:92 1-4', "harekesiz 've hâzâ kitâbun enzelnâhu mubârakun' (1-4. kelime)", None),
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

VF_YAZI = {91: {1: "'ve mâ'", 24: "'ve huden'", 29: "'ve tuxfûne'", 31: "'ve 'ullimtum'", 36: "'ve lâ'"}, 92: {1: "'ve hâzâ'", 9: "'ve li-tunzira'", 12: "'ve men'", 14: "'ve'llezîne'", 19: "'ve hum'"}}
sys.path.insert(0, '/home/claude/b21/yap')
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
open('/home/claude/b21/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '21')
BLOKLAR = [str(i) for i in range(1, 22)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '21', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b21/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '91', '92', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b21/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b21/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '91', '92', '21').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_91_92.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:91', '6:92'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_91_92.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(91, 93))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:91 'iz' (6. kelime — zaman zarfı, morph T); 6:92 kök أخر ('bi'l-âxirati' 16. kelime — ahiret): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '91', '92', '21')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b21/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 22)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(91, 93))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 10 kapanışında sunum/bolum26_kurallar.py eklendi (kural 1-5), sunum/bolum5_kurallar.py kuralı 9 sıkılaştırıldı, sunum/bolum19_kurallar.py KURAL_ATIF bölüm 10, sunum/geriye_donuk.py bolum26 satırı, sunum/mutasyon_sina.py b26 sınamaları — bu blokta araç değişikliği yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 225",
 "geriye dönük koşu (bölüm 10 kapanışı, komut 'python3 sunum/geriye_donuk.py b20k yamalar/geriye_donuk_6_b20.txt'): GERI_P",
 "kök tablosu: ölçümde '???' 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 91 92 21'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:91 'nûran ve huden li'n-nâsi' (23-25. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge) (yamalar/esma_el_6_91_92.txt); 6:92 'yu'minûne bi'l-âxirati' (15-16. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge) (yamalar/esma_el_6_91_92.txt); "
 "6:91 lafız (3., 10. ve 39. kelime); Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 91 92 21'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 6:92 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı): " + EMH,
 "ölçüm: 6:91 '{{1|EDİLGEN 1/14 fiil, pas z=0,08}}', '{{1|sayı işareti كَثِير}}', '{{1|fâsıla يلعبون → ن, N sınıfı}}', '{{1|simetri \\[7, 7, 15, 2\\]}}', '{{1|harf 187 → harf3 171, isaret 16}}' ve '{{1|dış düğüm 2}}'; "
 "6:92 '{{2|biçim DIKKAT}}', '{{2|fâsıla يحافظون → ن, N sınıfı}}', '{{2|simetri \\[3, 12, 18, 1\\]}}', '{{2|harf 105 → harf3 101, isaret 4}}', '{{2|dış düğüm 2}}' ve '{{2|İÇ düğüm 1}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 91 92 21'): KALAN_P",
 "ölçüm aktör: 6:91 '{{1|aktör: adlı مُوسَى 22\\. sırada \\(kisi, rol fail\\)}}'; 6:92 '{{2|aktör: adsız `karye` 11\\. sırada}}'",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:91 soru, emir — IMPV 3 'qul' (15.), 'quli' (38.), 'zerhum' (41.), INTG 1 'men' (16.), NEG 4 've mâ' (1.), 'mâ' (8.), 'lem' (33.), 've lâ' (36.); 6:92 haber — kip yok; "
 "morph REM ('ve' 6:91 1., 31.; 6:92 1., 14.), T ('iz' 6:91 6.), PRP ('li' 6:92 9.), ATT ('hâ' 6:92 1.), DEM ('zâ' 6:92 1.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:91 ★★★ (kaynak n, z=3,35); 6:92 yıldız yok",
 "fâsıla: 6:90 ن → 6:91 ن (يلعبون) → 6:92 ن (يحافظون) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:91 22:74 (emsal olarak basıldı) ve okunmuş 1 ayet; 6:92 42:7 (emsal olarak basıldı), okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:91 'mâ enzele allâh' süzgeç GEÇMEZ; 6:92 'zâ kitâb enzele mubârak' süzgeç GEÇER",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:91 3MP ('qaderu', 'qâlû', 'zerhum', 'xavdihim', 'yel'abûn' — gönderge 6:89 10. kelime, tartışmalı), 3MS ('qadrihî' — gönderge 'llâhe' 3. kelime; 'enzela' 9. kelime — fail 10. kelime; 'câ'e' 20. kelime — fail 22. kelime; söz içi 'enzele', 'bihî', 'tec'alûnehû'), 3FS ('tubdûnehâ' — gönderge 'qarâtîse' 27. kelime), muhatap 2MS ('qul', 'quli', 'zerhum'), söz içi muhatap 2MP; "
 "6:92 konuşan 1P, 3MS ('enzelnâhu', 'yedeyhi', 'bihî' — gönderge 'kitâbun' 2. kelime), muhatap 2MS ('ve li-tunzira'), 3FS ('havlehâ' — gönderge 'umme' 10. kelime), 3MP (gönderge 've'llezîne' 14. kelime) — betik denetimi: KHATA_ADSIZ; "
 "''ullimtum' (6:91 31. kelime) morph PASS — naib-i faili (adsız) muhatap 2MP, ölçüm EDİLGEN 1/14 bu kelimeden; 6:91 3MP göndergesi 6:89 10. kelime — inkâr edenler (okuma, tartışmalı); 6:92 1P konuşan göndergesi adsız (okuma)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:91 'qâlû' (7.) ardından söz 8-14. kelime; 'qul' (15.) ardından söz 16-37. kelime (REM sapması 6:91 (31. kelime) — 've 'ullimtum' söz içinde istînâf, muhatap 2MP sürer, söz 37. kelimeye dek sürer); 'quli' (38.) ardından söz 39. kelime — hepsi ayet içi kapanış; "
 "6:92 söz yok; mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 91 92 21' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:91 've mâ' (1.) REM, 've huden' (24.) CONJ, 've tuxfûne' (29.) CONJ, 've 'ullimtum' (31.) REM, 've lâ' (36.) CONJ; 6:92 've hâzâ' (1.) REM, 've li-tunzira' (9.) CONJ, 've men' (12.) CONJ, 've'llezîne' (14.) REM, 've hum' (19.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:91 ◈B أنس ('n-nâsi' 25. kelime — B1); 6:92 ◈B يدي ('yedeyhi' 8. kelime — B3; 'beyne yedeyhi' kalıbı, organ anlamı yok (okuma))",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 91 92 21'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 2 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:91 (22:74); 6:92 (42:7); ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:91 söz açılır / kapanır (8. / 14., 16. / 37., 39. / 39. kelime), şahıs geçişi 3 → 2, edim geçişi emir → soru, emir, bölüm açılışı; 6:92 şahıs geçişi 2 → 3, edim geçişi soru, emir → haber; "
 "ölçüm iltifât 6:91-92 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:91 've mâ qaderu'llâhe haqqa qadrihî' — mefûl-i mutlak (morph REM + NEG; 'haqqa qadrihî' ACC); 'iz qâlû' — zaman zarfı (morph T); 'mâ enzela'llâhu … min şey'in' — nefy ve 'min' tekidi (morph NEG + P); 'qul men enzele' — soru (morph INTG); "
 "'tec'alûnehû qarâtîse' — hâl cümlesi okuması (sapma: morph CIRC yok; okuma); 've 'ullimtum' — istînâf (morph REM); 'quli'llâhu' — mahzûf fiilli cevap (okuma); 'summe zerhum … yel'abûn' — emir (morph CONJ + IMPV), 'yel'abûn' hâl okuması (sapma: morph CIRC yok; okuma); "
 "6:92 've hâzâ kitâbun' — işaret ve haber (morph REM + ATT + DEM); 'mubârakun musaddiqu' — sıfatlar (morph ADJ); 've li-tunzira' — atıf ve gaye lâmı (morph CONJ + PRP + SUBJ); 've'llezîne yu'minûne … yu'minûne bihî' — mübteda ve haber (morph REM + REL)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:91 'qaderu'llâhe haqqa qadrihî' — 22:74 ile eş (sayım: 'say 6:91 2-5'; lemma dizisi 'dizi 6 91 1 5'); 6:92 'li-tunzira umme'l-qurâ ve men havlehâ' — 42:7 ile eş (sayım: 'say 6:92 10-13'; lemma dizisi 'dizi 6 92 9 13'); 6:91 kök أله, علم, قدر, قول, نزل ikilemeleri; 6:92 kök أمن ikilemesi; kök نزل 6:91 ve 6:92'de",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 21'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'qaderu'llâhe haqqa qadrihî' 6:91 'Allah'ı takdirinin hakkıyla takdir etmediler' / 22:74 'Allah'ı gereği gibi takdir edemediler' (emsal metninde) — çakışma — tam okuma sonu ('takdirinin hakkıyla' / 'gereği gibi'; 'etmediler' / 'edemediler'); 'umme'l-qurâ ve men havlehâ' 6:92 'şehirlerin anasını ve çevresindekileri' / 42:7 'şehirlerin anasını ve çevresindekileri' (emsal metninde) — çakışma değil (bayt eşit; fiil karşılığı 'uyarman için' / 'uyarasın' kalıp dışında); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:91 'qaderu' PERF — meal 'takdir etmediler'; 'qâlû' PERF — meal 'dedikleri'; 'enzela' PERF — meal 'indirmedi'; 'qul' IMPV — meal 'De'; 'enzele' PERF — meal 'indirdi'; 'câ'e' PERF — meal 'getirdiği'; "
 "'tec'alûne' IMPF IND — meal 'dönüştürüyorsunuz'; 'tubdûne' IMPF IND — meal 'açığa vuruyor'; 'tuxfûne' IMPF IND — meal 'gizliyorsunuz'; ''ullimtum' PERF PASS — meal 'öğretildi'; 'ta'lemû' IMPF JUS (olumsuz geçmiş) — meal 'bilmediğiniz'; 'quli' IMPV — meal 'De'; 'zerhum' IMPV — meal 'bırak'; 'yel'abûn' IMPF IND — meal 'oynar'; "
 "6:92 'enzelnâ' PERF — meal 'indirdiğimiz'; 'tunzira' IMPF SUBJ — meal 'uyarman'; 'yu'minûne' IMPF IND — meal 'iman edenler', 'iman ederler'; 'yuhâfizûn' IMPF IND — meal 'korurlar'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 91 92 21'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:91 ve 6:92 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:91 ('tubdûnehâ' / 've tuxfûne'); 6:92 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök نزل 6:91, 6:92; kök كتب 6:91, 6:92; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 11-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 21 ve 22; bu blok bölümü açıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b21/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 91 92 21'; lem_bozuk.py 21 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 91 92 → AYN_SONUC; sunum/bolum4_kurallar.py 91 92 21 → KHATA_HEPSI; sunum/bolum5_kurallar.py 91 92 21 → B5_HEPSI; sunum/bolum6_kurallar.py 91 92 21 → B6_HEPSI; sunum/bolum7_kurallar.py 91 92 21 → B7_HEPSI; sunum/bolum8_kurallar.py 91 92 21 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 91 92 21 → B9_HEPSI; sunum/bolum10_kurallar.py 91 92 21 → B10_HEPSI; sunum/bolum11_kurallar.py 91 92 21 → B11_HEPSI; sunum/bolum12_kurallar.py 91 92 21 → B12_HEPSI; sunum/bolum13_kurallar.py 91 92 21 → B13_HEPSI; sunum/bolum14_kurallar.py 91 92 21 → B14_HEPSI; sunum/bolum15_kurallar.py 91 92 21 → B15_HEPSI; sunum/bolum16_kurallar.py 91 92 21 → B16_HEPSI; sunum/bolum17_kurallar.py 91 92 21 → B17_HEPSI; sunum/bolum18_kurallar.py 91 92 21 → B18_HEPSI; sunum/bolum19_kurallar.py 91 92 21 → B19_HEPSI; sunum/bolum20_kurallar.py 91 92 21 → B20_HEPSI; sunum/bolum21_kurallar.py 91 92 21 → B21_HEPSI; sunum/bolum22_kurallar.py 91 92 21 → B22_HEPSI; sunum/bolum23_kurallar.py 91 92 21 → B23_HEPSI; sunum/bolum24_kurallar.py 91 92 21 → B24_HEPSI; sunum/bolum25_kurallar.py 91 92 21 → B25_HEPSI; sunum/bolum26_kurallar.py 91 92 21 → B26_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 21 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('mâ', 'enzele', 'allâh', 'zâ', 'kitâb', 'mubârak', 'qadere', 'haqq', 'qadr', 'enzere', 'umm', 'qarye', 'men', 'havl'); joker kullanılmadı; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (91, 92): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_91_92.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b20k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '91', '92'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '91', '92', '21'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '91', '92', '21'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '91', '92', '21', '--tazelik-yok')}
    for _n in range(7, 27): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '91', '92', '21')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26 = [_R['B%d' % _n].splitlines() for _n in range(6, 27)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
