# sûre 6 blok 23 (6:95-99) ARIZA oluşturucu — bölüm 12-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b23/olcum.txt'
os.environ['SAY2'] = '/home/claude/b23/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b22.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {}
BOL = "'Taneyi ve çekirdeği yaran; gözler O'nu idrak etmez'"


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
 ("6:97", "'qad fassale âye qavm'", 3, 'say 6:97 12-15', "harekesiz 'qad fassalne'l-âyâti li-qavmin' (12-15. kelime)", None),
 ("6:97", "'zulme berr bahr'", 2, 'say 6:97 9-11', "harekesiz 'zulumâti'l-berri ve'l-bahr' (9-11. kelime)", None),
 ("6:97", "'_ ellezî ce'ale'", 2, 'say 6:97 1-3', "harekesiz 've huve'llezî ce'ale' (1-3. kelime)", ('dizi 6 97 1 3', "_ ellezî ce'ale", '1-3', "biçim farkı (dizi 6 97 1 3): basılmamış eş zamir eki")),
 ("6:98", "'qad fassale âye qavm'", 3, 'say 6:98 9-12', "harekesiz 'qad fassalne'l-âyâti li-qavmin' (9-12. kelime)", None),
 ("6:98", "'_ ellezî enşe'e'", 2, 'say 6:98 1-3', "harekesiz 've huve'llezî enşe'ekum' (1-3. kelime)", ('dizi 6 98 1 3', "_ ellezî enşe'e", '1-3', "biçim farkı (dizi 6 98 1 3): basılmamış eş zamir eki")),
 ("6:99", "'semer izâ esmera'", 2, 'say 6:99 35-37', "harekesiz 'semerihî izâ esmera' (35-37. kelime)", None),
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

VF_YAZI = {95: {5: "'ve'n-nevâ'", 10: "'ve muxricu'"}, 96: {3: "'ve ce'ale'", 6: "'ve'ş-şemse'", 7: "'ve'l-qamera'"}, 97: {1: "'ve huve'", 11: "'ve'l-bahri'"}, 98: {1: "'ve huve'", 8: "'ve mustevda'un'"}, 99: {1: "'ve huve'", 19: "'ve mine'n-naxli'", 25: "'ve cennâtin'", 28: "'ve'z-zeytûne'", 29: "'ve'r-rummâne'", 31: "'ve ğayra'", 38: "'ve yen'ihî'"}}
sys.path.insert(0, '/home/claude/b23/yap')
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
open('/home/claude/b23/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '23')
BLOKLAR = [str(i) for i in range(1, 24)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '23', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b23/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '95', '99', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b23/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b23/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '95', '99', '23').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_95_99.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:95', '6:96', '6:97', '6:98', '6:99'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_95_99.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(95, 100))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:96 kök صبح ('l-isbâhi' 2. kelime — sabah); 6:98 kök نفس ('nefsin' 5. kelime — can); 6:99 kök دنو ('dâniyetun' 24. kelime — yakınlık), 'izâ' (36. kelime — zaman zarfı, morph T): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '95', '99', '23')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b23/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 24)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(95, 100))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 11 kapanışında sunum/bolum27_kurallar.py eklendi (kural 1-5), sunum/bolum19_kurallar.py kuralı 5 sıkılaştırıldı ve KURAL_ATIF bölüm 11, sunum/geriye_donuk.py bolum27 satırı, sunum/mutasyon_sina.py b27 sınamaları — bu blokta araç değişikliği yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 236",
 "geriye dönük koşu (bölüm 11 kapanışı, komut 'python3 sunum/geriye_donuk.py b22k yamalar/geriye_donuk_6_b22.txt'): GERI_P",
 "kök tablosu: ölçümde '???' 6:95 5. kelime için 1, 6:99 23. ve 38. kelime için 2 — yeni kökler نوي ('çekirdek (nevâ)'), قنو ('hurma salkımı (qinvân)'), ينع ('olgunlaşma (yen')'); yamalar/yama_kok_6_95.py → kok_ekle_6.ISTEK; kok_turkce 1629); ölçüm yeniden alındı, '???' 0; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 95 99 23'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:95 'yuxricu'l-hayye mine'l-meyyit' (6-9. kelime) ve 'muxricu'l-meyyiti mine'l-hayy' (10-13. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge) (yamalar/esma_el_6_95_99.txt; liste farkı: ölçüm esmâ satırında 'hayy' yok, esma_kayit e_oto 1); "
 "6:96 'zâlike taqdîru'l-'azîzi'l-'alîm' (9-12. kelime) — tamlama içinde ad (tamlayan), göndergesi Allah; kapalı listede kural yok (protokol: DUR-sor), oturum ortasında sorulmadı — esma_el'e girmedi, e_el=? 1, kullanıcı kararı (tam okuma sonu; oturum ortasında sorulmadı); "
 "6:97 'fî zulumâti'l-berri ve'l-bahr' (8-11. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge); 6:98 ve 6:99 esmâ yok; "
 "6:95 lafız (2. ve 15. kelime); 6:96, 6:97, 6:98 ve 6:99 lafız yok; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 95 99 23'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:95 '{{1|EDİLGEN 1/2 fiil, pas z=2,52}}', '{{1|HAPAKS: نوي}}', '{{1|fâsıla تؤفكون → ن, N sınıfı}}', '{{1|simetri \\[3, 1, 14, 1\\]}}', '{{1|harf 73 → harf3 69, isaret 4}}' ve '{{1|dış düğüm 0}}'; "
 "6:96 '{{2|fâsıla ٱلعليم → م, N sınıfı}}', '{{2|harf 64 → harf3 61, isaret 3}}' ve '{{2|dış düğüm 3}}'; "
 "6:97 '{{3|fâsıla يعلمون → ن, N sınıfı}}', '{{3|simetri \\[3, 1, 7, 1\\]}}', '{{3|harf 71 → harf3 68, isaret 3}}', '{{3|dış düğüm 1}}' ve '{{3|İÇ düğüm 1}}'; "
 "6:98 '{{4|sayı işareti واحِدَة}}', '{{4|fâsıla يفقهون → ن, N sınıfı}}', '{{4|harf 64 → harf3 58, isaret 6}}' ve '{{4|dış düğüm 0}}'; "
 "6:99 '{{5|HAPAKS: قنو}}', '{{5|fâsıla يؤمنون → ن, N sınıfı}}', '{{5|simetri \\[3, 1, 39, 1\\]}}', '{{5|harf 203 → harf3 185, isaret 18}}' ve '{{5|dış düğüm 0}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 95 99 23'): KALAN_P",
 "ölçüm aktör: 6:95, 6:96, 6:97, 6:98 ve 6:99 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:95 soru — INTG 1 'fe-ennâ' (16.); 6:96 haber — kip yok; 6:97 haber — CERT 1 'qad' (12.); 6:98 haber — CERT 1 'qad' (9.); "
 "6:99 emir — EMPH 1 'le-âyâtin' (42.), IMPV 1 'unzurû' (33.); "
 "morph REM ('fe' 6:95 16., 6:98 7.; 've' 6:99 19.), ACC ('inna' 6:95 1., 'inne' 6:99 39.), PRP ('li' 6:97 6.), T ('izâ' 6:99 36.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:95 ★★★ (kaynak hapaks, z=3,28; eşiği geçen öbür ölçüler allah z=1,82, pas z=2,52); 6:99 ★★★ (kaynak hapaks, z=6,79; eşiği geçen öbür ölçüler n z=3,35); 6:96, 6:97 ve 6:98 yıldız yok",
 "fâsıla: 6:94 ن → 6:95 ن (تؤفكون) → 6:96 م (ٱلعليم) → 6:97 ن (يعلمون) → 6:98 ن (يفقهون) → 6:99 ن (يؤمنون) — N sınıfı (ölçüm); 6:96 harf değişimi م; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:95 xref yok; 6:96 36:38 (emsal olarak basıldı) ve okunmuş 2 ayet; 6:97 6:63 (basılmış) ve 27:63 (emsal olarak basıldı); 6:98 xref yok; 6:99 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:95 ve 6:96 nakarat3 yok; 6:97 'qad fassale âye qavm' süzgeç GEÇER, 'zulme berr bahr' süzgeç GEÇMEZ ve '_ ellezî ce'ale' süzgeç GEÇMEZ; 6:98 'qad fassale âye qavm' süzgeç GEÇER ve '_ ellezî enşe'e' süzgeç GEÇMEZ; 6:99 'semer izâ esmera' süzgeç GEÇMEZ",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:95 3MS ('yuxricu' — gönderge 'llâhe' 2. kelime), muhatap 2MP ('tu'fekûn'); 6:96 3MS ('ce'ale' — gönderge 6:95 2. kelime); "
 "6:97 3MS ('ve huve', 'ce'ale' — gönderge 6:95 2. kelime), muhatap 2MP, 3FS ('bihâ' — gönderge 'n-nucûme' 5. kelime), konuşan 1P ('fassalne'), 3MP ('ya'lemûn' — gönderge 'li-qavmin' 15. kelime); "
 "6:98 3MS ('ve huve', 'enşe'ekum' — gönderge 6:95 2. kelime), muhatap 2MP, konuşan 1P ('fassalne'), 3MP ('yefqahûn' — gönderge 'li-qavmin' 12. kelime); "
 "6:99 3MS ('ve huve', 'enzele' — gönderge 6:95 2. kelime; 'bihî' — gönderge 'mâ'en' 6. kelime; 'minhu' — gönderge 'nebâte' 9. kelime, tartışmalı, ve 'xadiran' 14. kelime; 'semerihî', 'esmera', 've yen'ihî' — gönderge 'muteşâbihin' 32. kelime, tartışmalı), konuşan 1P, 3FS ('tal'ihâ' — gönderge 'n-naxli' 20. kelime, tartışmalı), muhatap 2MP ('unzurû'), 3MP ('yu'minûn' — gönderge 'li-qavmin' 43. kelime) — betik denetimi: KHATA_ADSIZ; "
 "edilgen: 6:95 'tu'fekûn' (17. kelime; naib-i faili muhatap 2MP) — ölçüm EDİLGEN 1/2 bu kelimeden; 6:97-99 3MS 'huve' ile 1P konuşan dönüşü (okuma; tartışmalı)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:95-99 söz yok — söz fiili yok (okuma); mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 95 99 23' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:95 've'n-nevâ' (5.), 've muxricu' (10.) CONJ; 6:96 've ce'ale' (3.), 've'ş-şemse' (6.), 've'l-qamera' (7.) CONJ; 6:97 've huve' (1.), 've'l-bahri' (11.) CONJ; 6:98 've huve' (1.), 've mustevda'un' (8.) CONJ; "
 "6:99 've huve' (1.), 've cennâtin' (25.), 've'z-zeytûne' (28.), 've'r-rummâne' (29.), 've ğayra' (31.), 've yen'ihî' (38.) CONJ, 've mine'n-naxli' (19.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:95 ◈B حيي ('l-hayye' 7. kelime — B4); 6:95 ◈B موت ('l-meyyiti' 9. kelime — B4); 6:96 ◈K ليل ('l-leyle' 4. kelime — K1); 6:96 ◈K شمس ('ş-şemse' 6. kelime — K1); 6:96 ◈K قمر ('l-qamera' 7. kelime — K1); 6:97 ◈K نجم ('n-nucûme' 5. kelime — K1); 6:97 ◈K بحر ('l-bahri' 11. kelime — K1); 6:99 ◈K سمو ('s-semâ'i' 5. kelime — K1); 6:99 ◈K موه ('mâ'en' 6. kelime — K1); 6:99 ◈B نبت ('nebâte' 9. kelime — B1)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 95 99 23'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:96 (36:38); 6:97 (27:63); 6:95, 6:98 ve 6:99 bağ yok; ayetler arası kalıp 'qad fassalne'l-âyâti li-qavmin' (6:97, 6:98) — sayım 'dizi 6 97 12 15', 'dizi 6 98 9 12'; blok içi tekrar (bölüm 9 kuralı 6), ardışık bağ yerine sayımla kayıt (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:95 şahıs geçişi yok, edim geçişi haber → soru, bölüm açılışı; 6:96 şahıs geçişi 2 → 3, edim geçişi soru → haber; 6:97 şahıs geçişi 3 → 2, şahıs sayısında beraberlik yok (ölçüm baskın 2), edim geçişi yok; 6:98 şahıs geçişi 2 → 3, edim geçişi yok; 6:99 şahıs geçişi yok, edim geçişi haber → emir; "
 "ölçüm iltifât 6:95-99 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:95 'inna'llâhe fâliqu'l-habbi' — 'inne' cümlesi, haber etken ortaç (morph ACC); 'fe-ennâ tu'fekûn' — sonuç fâsı ve soru (morph REM + INTG); "
 "6:96 'zâlike taqdîru'l-'azîzi'l-'alîm' — işaret ve tamlama (morph DEM); 6:97 've huve'llezî ce'ale' — atıf, zamir ve ilgi (morph CONJ + REL); 'li-tehtedû' — amaç lâmı (morph PRP); 6:98 'fe-mustaqarrun ve mustevda'un' — isim cümlesi, haber mahzuf (morph REM + CONJ); "
 "6:99 've mine'n-naxli' — yeni cümle (morph REM); 'izâ esmera' — zaman (morph T); 'inne fî zâlikum le-âyâtin' — 'inne' ve tekit lâmı (morph ACC + EMPH)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:96 'zâlike taqdîru'l-'azîzi'l-'alîm' — 36:38 ile eş (sayım: 'say 6:96 9-12'; lemma dizisi 'dizi 6 96 9 12'); 6:97 'zulumâti'l-berri ve'l-bahr' — 27:63 ile eş (sayım: 'say 6:97 9-11'; lemma dizisi 'dizi 6 97 9 11'); 6:97 ve 6:98 'qad fassalne'l-âyâti li-qavmin' — sûre içi eş (nakarat3); 6:95 kök أله, حيي, خرج, موت ikilemeleri; 6:99 kök ثمر, خرج, شبه ikilemeleri",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 23'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'zâlike taqdîru'l-'azîzi'l-'alîm' 6:96 'Bu, Azîz ve Alîm olanın takdiridir' / 36:38 'Bu, Azîz ve Alîm olanın takdiridir' (emsal metninde) — çakışma değil (bayt eşit); 'zulumâti'l-berri ve'l-bahr' 6:97 'karanın ve denizin karanlıklarında' / 27:63 'karanın ve denizin karanlıklarında' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:95 'yuxricu' IMPF IND — meal 'çıkarır'; 'tu'fekûn' IMPF IND PASS — meal 'döndürülüyorsunuz'; 6:96 'ce'ale' PERF — meal 'kıldı'; "
 "6:97 'ce'ale' PERF — meal 'kılandır'; 'tehtedû' IMPF SUBJ — meal 'yol bulasınız'; 'fassalnâ' PERF — meal 'açıkladık'; 'ya'lemûn' IMPF IND — meal 'Bilen'; 6:98 'enşe'a' PERF — meal 'inşa edendir'; 'fassalnâ' PERF — meal 'açıkladık'; 'yefqahûn' IMPF IND — meal 'Anlayan'; "
 "6:99 'enzele' PERF — meal 'indirendir'; 'axracnâ' PERF (7. ve 12. kelime) — meal 'çıkardık'; 'nuxricu' IMPF IND — meal 'çıkarırız'; 'unzurû' IMPV — meal 'bakın'; 'esmera' PERF — meal 'verdiğinde'; 'yu'minûn' IMPF IND — meal 'inanan'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 95 99 23'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:97 tarayıcı adayı (kök بحر, ظلم, نجم; B_ta’lîl) — çıpa değil: yıldızlarla yol bulma amaç bildirimi, ölçü / mekanizma yok (olgu=False); 6:99 tarayıcı adayı (kök ثمر, حبب, رمن, زيت, سمو, عنب, موه, نبت, نخل; G_bakış) — çıpa değil: bakma emri, ölçü / mekanizma yok (olgu=False); 6:95, 6:96 ve 6:98 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:95 ('l-hayye' / 'l-meyyiti'); 6:96 ('l-isbâhi' / 'l-leyle'); 6:97 ('l-berri' / 've'l-bahri'); 6:98 ('fe-mustaqarrun' / 've mustevda'un'); 6:99 ('muştebihen' / 've ğayra muteşâbihin'); ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök فلق 6:95 ('fâliqu') ve 6:96 ('fâliqu'); kök جعل 6:96 ('ce'ale') ve 6:97 ('ce'ale'); kök فصل 6:97 ('fassalne') ve 6:98 ('fassalne'); kök أيي 6:97, 6:98, 6:99; kök قوم 6:97, 6:98, 6:99; kök خرج 6:95, 6:99; kök حبب 6:95 ('l-habbi') ve 6:99 ('habben'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 12-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 23 ve 24; bu blok bölümü açıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b23/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 95 99 23'; lem_bozuk.py 23 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 95 99 → AYN_SONUC; sunum/bolum4_kurallar.py 95 99 23 → KHATA_HEPSI; sunum/bolum5_kurallar.py 95 99 23 → B5_HEPSI; sunum/bolum6_kurallar.py 95 99 23 → B6_HEPSI; sunum/bolum7_kurallar.py 95 99 23 → B7_HEPSI; sunum/bolum8_kurallar.py 95 99 23 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 95 99 23 → B9_HEPSI; sunum/bolum10_kurallar.py 95 99 23 → B10_HEPSI; sunum/bolum11_kurallar.py 95 99 23 → B11_HEPSI; sunum/bolum12_kurallar.py 95 99 23 → B12_HEPSI; sunum/bolum13_kurallar.py 95 99 23 → B13_HEPSI; sunum/bolum14_kurallar.py 95 99 23 → B14_HEPSI; sunum/bolum15_kurallar.py 95 99 23 → B15_HEPSI; sunum/bolum16_kurallar.py 95 99 23 → B16_HEPSI; sunum/bolum17_kurallar.py 95 99 23 → B17_HEPSI; sunum/bolum18_kurallar.py 95 99 23 → B18_HEPSI; sunum/bolum19_kurallar.py 95 99 23 → B19_HEPSI; sunum/bolum20_kurallar.py 95 99 23 → B20_HEPSI; sunum/bolum21_kurallar.py 95 99 23 → B21_HEPSI; sunum/bolum22_kurallar.py 95 99 23 → B22_HEPSI; sunum/bolum23_kurallar.py 95 99 23 → B23_HEPSI; sunum/bolum24_kurallar.py 95 99 23 → B24_HEPSI; sunum/bolum25_kurallar.py 95 99 23 → B25_HEPSI; sunum/bolum26_kurallar.py 95 99 23 → B26_HEPSI; sunum/bolum27_kurallar.py 95 99 23 → B27_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 23 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('axraca', 'hayy', 'min', 'meyyit', 'zâ', 'taqdîr', ''azîz', ''alîm', 'qad', 'fassale', 'âye', 'qavm', 'zulme', 'berr', 'bahr', 'ellezî', 'ce'ale', 'enşe'e', 'semer', 'izâ', 'esmera'); joker '_' lemmasız öğede ('dizi 6 97 1 3', 'dizi 6 98 1 3' — 'huve'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (95, 99): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_95_99.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b22k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '95', '99'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '95', '99', '23'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '95', '99', '23'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '95', '99', '23', '--tazelik-yok')}
    for _n in range(7, 28): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '95', '99', '23')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27 = [_R['B%d' % _n].splitlines() for _n in range(6, 28)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
