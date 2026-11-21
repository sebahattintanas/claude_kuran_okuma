# sûre 6 blok 22 (6:93-94) ARIZA oluşturucu — bölüm 11-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b22/olcum.txt'
os.environ['SAY2'] = '/home/claude/b22/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
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
 ("6:93", "'men ezlem mimmen iftarâ 'alâ allâh kezib ev'", 2, 'say 6:93 1-8', "harekesiz 've men ezlemu mimmeni'fterâ 'alâ'llâhi keziben ev' (1-8. kelime)", None),
 ("6:93", "'ezlem mimmen iftarâ 'alâ allâh kezib'", 3, 'say 6:93 2-7', "harekesiz 'ezlemu mimmeni'fterâ 'alâ'llâhi keziben' (2-7. kelime)", None),
 ("6:93", "'mâ enzele allâh'", 2, 'say 6:93 20-22', "harekesiz 'mâ enzela'llâhu' (20-22. kelime)", None),
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

VF_YAZI = {93: {1: "'ve men ezlemu'", 12: "'ve lem'", 16: "'ve men qâle'", 23: "'ve lev'", 30: "'ve'l-melâ'iketu'", 46: "'ve kuntum'"}, 94: {1: "'ve le-qad'", 8: "'ve teraktum'", 13: "'ve mâ'", 25: "'ve dalle'"}}
sys.path.insert(0, '/home/claude/b22/yap')
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
open('/home/claude/b22/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '22')
BLOKLAR = [str(i) for i in range(1, 23)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '22', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b22/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '93', '94', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b22/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b22/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '93', '94', '22').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_93_94.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:93', '6:94'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_93_94.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(93, 95))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:93 'izi' (25. kelime — zaman zarfı, morph T), kök نفس ('enfusekumu' 34. kelime — can); 6:94 kök أول ('evvele' 6. kelime — başlangıç, morph T), kök ظهر ('zuhûrikum' 12. kelime — sırt), kök قطع ('teqatta'a' 23. kelime — kopma): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '93', '94', '22')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b22/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 23)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(93, 95))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/bolum19_kurallar.py kuralı 5 (ESMA_LEMMA_BIR) — bu bloğun esma_el kaydı lemmanın önceki etiketlerinden biriyle eşse eski ayrılık yeniden raporlanmaz (6:94 'evvele merratin' — 6:14 etiketiyle eş; 6:14 / 6:25 ayrılığı blok 6'da raporlandı, sınaması sürüyor); sunum/mutasyon_sina.py — b19 kural 5 isabetsiz sınaması eklendi; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 229",
 "geriye dönük koşu (araç değişen blok — bekleyen_ariza_6_b13 elle önerisi (8) GERIYE_DONUK_ZORUNLU; komut 'python3 sunum/geriye_donuk.py b22 yamalar/geriye_donuk_6_b20k.txt'; metin ve karar kesinleştikten sonra): GERI_P; düşen / yeni çifti: blok 06 6:25 esmâ kural sapması iletisinde emsal kaydı bu bloğun 6:94 'evvele merratin' kaydına döndü (bir isabetin değişen metni; kayıt sayısı 3 → 4 — basılan değişti sınıfında, tam okuma sonu); blok 21 KAPSAMAYAN önceki koşudan sonra okunan blok, blok 22 satırları (KAPSAMAYAN, ZAMİR KAYITSIZ) önceki koşuda taranmamış blok",
 "kök tablosu: ölçümde '???' 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 93 94 22'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:93 esmâ yok; 6:94 'evvele merratin' (6-7. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge) (yamalar/esma_el_6_93_94.txt; liste farkı: ölçüm esmâ satırında 'evvele' yok, esma_kayit e_oto 1 — zaman zarfı 'evvel'); "
 "6:93 lafız (6., 22. ve 43. kelime); Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 93 94 22'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:93 '{{1|EDİLGEN 3/14 fiil, pas z=0,89}}', '{{1|fâsıla تستكبرون → ن, N sınıfı}}', '{{1|simetri \\[3, 1, 12, 1\\]}}', '{{1|harf 205 → harf3 199, isaret 6}}' ve '{{1|dış düğüm 5}}'; "
 "6:94 '{{2|fâsıla تزعمون → ن, N sınıfı}}', '{{2|simetri \\[3, 13, 17, 1\\]}}', '{{2|harf 129 → harf3 125, isaret 4}}' ve '{{2|dış düğüm 2}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 93 94 22'): KALAN_P",
 "ölçüm aktör: 6:93 ve 6:94 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:93 soru, emir, şart — COND 1 've lev' (23.), FUT 1 'se-unzilu' (18.), IMPV 1 'exricû' (33.), INTG 2 've men' (1.), 've men' (16.), NEG 1 've lem' (12.); "
 "6:94 haber — CERT 2 've le-qad' (1.), 'le-qad' (22.), EMPH 2 've le-qad' (1.), 'le-qad' (22.), NEG 1 've mâ' (13.); "
 "morph REM ('ve' 6:93 1., 23.), CIRC ('ve' 6:93 30.), T ('izi' 6:93 25.), SUB ('kemâ' 6:94 4.), ACC ('ennehum' 6:94 19.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:93 ★★★ (kaynak n, z=3,88); 6:94 ★ (kaynak n, z=1,76)",
 "fâsıla: 6:92 ن → 6:93 ن (تستكبرون) → 6:94 ن (تزعمون) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:93 46:20 (emsal olarak basıldı) ve okunmuş 4 ayet; 6:94 18:48 (emsal olarak basıldı) ve okunmuş 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:93 'men ezlem mimmen iftarâ 'alâ allâh kezib ev' süzgeç GEÇER, 'ezlem mimmen iftarâ 'alâ allâh kezib' süzgeç GEÇER ve 'mâ enzele allâh' süzgeç GEÇMEZ; 6:94 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:93 3MS ('fterâ', 'qâle', 'ileyhi' — gönderge 'mimmeni' 3. kelime; 17. kelimedeki 'qâle' — gönderge 've men' 16. kelime; 'enzela' 21. kelime — fail 22. kelime; 'âyâtihî' — söz içi, gönderge 'llâhi' 43. kelime), söz içi konuşan 1S ('ileyye', 'se-unzilu'), muhatap 2MS ('terâ'), 3MP ('eydîhim' — gönderge 've'l-melâ'iketu' 30. kelime), söz içi muhatap 2MP; "
 "6:94 konuşan 1P, muhatap 2MP, 3MP ('ennehum' — gönderge 'şufe'â'ekumu' 16. kelime), 3MS ('teqatta'a' — gönderge 'beynekum' 24. kelime, tartışmalı; 've dalle' — gönderge 'mâ' 27. kelime) — betik denetimi: KHATA_ADSIZ; "
 "edilgen: 6:93 'ûhiye' (10. kelime; naib-i faili adsız), 've lem yûha' (13. kelime; naib-i faili 'şey'un' 15. kelime), 'tuczevne' (36. kelime; naib-i faili muhatap 2MP) — ölçüm EDİLGEN 3/14 bu kelimelerden; 6:94 1P konuşan ve 2MP muhatap göndergesi adsız (okuma; 6:93 zalimler sürüyor, tartışmalı)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2; meleklerin sözü — söz fiili mahzuf (okuma), A3'te 'söz içi' aralığıyla): "
 "6:93 'qâle' (9.) ardından söz 10-11. kelime; 'qâle' (17.) ardından söz 18-22. kelime — ayet içi kapanış; söz fiili mahzuf söz 33-49. kelime (meleklerin sözü) — ayet içi kapanış; 6:94 söz yok — konuşan 1P, söz fiili yok (okuma); mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 93 94 22' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:93 've men' (1.) REM, 've lem' (12.) CONJ, 've men' (16.) CONJ, 've lev' (23.) REM, 've'l-melâ'iketu' (30.) CIRC, 've kuntum' (46.) CONJ; 6:94 've le-qad' (1.), 've teraktum' (8.), 've mâ' (13.), 've dalle' (25.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:93 ◈K يوم ('l-yevme' 35. kelime — K2); 6:93 ◈B يدي ('eydîhim' 32. kelime — B3); 6:93 ◈B موت ('l-mevti' 29. kelime — B4); 6:94 ◈B خلق ('xalaqnâkum' 5. kelime — B2)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 93 94 22'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 2 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:93 (46:20); 6:94 (18:48); ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş (6:93 'men ezlem mimmen iftarâ' — 6:21), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:93 söz açılır / kapanır (10. / 11., 18. / 22. ve 33. / 49. kelime), şart → cevap ('lev' 23. kelime — cevap hazif, mealde ünlem), şahıs geçişi 3 → 2, edim geçişi haber → soru, emir, şart; 6:94 şahıs geçişi yok, edim geçişi soru, emir, şart → haber, bölüm kapanışı; "
 "ölçüm iltifât 6:93-94 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:93 've men ezlemu' — inkâri soru ve üstünlük (morph REM + INTG); 've lem yûha ileyhi şey'un' — atıf, hâl okuması (morph CONJ + NEG; sapma: morph CIRC yok); 've men qâle' — atıf (morph CONJ + INTG); "
 "'ve lev terâ' — 'lev' şartı, cevap mahzuf (6:93 23. kelime) (morph REM + COND); 've'l-melâ'iketu bâsitû' — hâl cümlesi (morph CIRC); 'bi-mâ kuntum teqûlûne' — sebep, masdar 'mâ' (morph P + REL); "
 "6:94 've le-qad ci'tumûnâ' — kasem ve tahkik (morph CONJ + EMPH + CERT); 'kemâ xalaqnâkum' — teşbih (morph P + SUB); 'le-qad teqatta'a beynekum' — kasem ve tahkik (morph EMPH + CERT)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:93 'tuczevne 'azâbe'l-hûni' — 46:20 ile eş (sayım: 'say 6:93 36-38'; lemma dizisi 'dizi 6 93 35 40'); 6:94 'kemâ xalaqnâkum' — 18:48 ile eş (sayım: 'say 6:94 4-5'); "
 "6:93 kök أله, ظلم, قول, كون, نزل, وحي ikilemeleri; 6:94 kök زعم ikilemesi; 6:93 've men ezlemu mimmeni'fterâ 'alâ'llâhi keziben ev' — 6:21 ile sûre içi eş (nakarat3)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 22'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'tuczevne 'azâbe'l-hûni' 6:93 'aşağılık azabıyla cezalandırılacaksınız' / 46:20 'alçaltıcı azapla cezalandırılıyorsunuz' (emsal metninde) — çakışma — tam okuma sonu ('aşağılık' / 'alçaltıcı'; '-acaksınız' / '-ıyorsunuz'); "
 "'kemâ xalaqnâkum' 6:94 'yarattığımız gibi' / 18:48 'yarattığımız gibi' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:93 'fterâ' PERF — meal 'uydurandan'; 'qâle' PERF (9. ve 17. kelime) — meal 'diyenden'; 'ûhiye' PERF PASS — meal 'vahyedildi'; 'yûha' IMPF JUS PASS (olumsuz geçmiş) — meal 'vahyedilmemişken'; 'unzilu' IMPF IND (FUT) — meal 'indireceğim'; 'enzela' PERF — meal 'indirdiğinin'; "
 "'terâ' IMPF IND (şart) — meal 'görsen'; 'exricû' IMPV — meal 'çıkarın'; 'tuczevne' IMPF IND PASS — meal 'cezalandırılacaksınız'; 'kuntum' PERF — meal 'söylemeniz', 'büyüklenmeniz' içinde; 'teqûlûne' IMPF IND — meal 'söylemeniz'; 'testekbirûn' IMPF IND — meal 'büyüklenmeniz'; "
 "6:94 'ci'tum' PERF — meal 'geldiniz'; 'xalaqnâ' PERF — meal 'yarattığımız'; 'teraktum' PERF — meal 'bıraktınız'; 'xavvelnâ' PERF — meal 'verdiğimiz'; 'nerâ' IMPF IND — meal 'görmüyoruz'; 'za'amtum' PERF — meal 'iddia ettiğiniz'; 'teqatta'a' PERF — meal 'koptu'; 'dalle' PERF — meal 'kaybolup gitti'; 'tez'umûn' IMPF IND — meal 'iddia ettiğiniz'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 93 94 22'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:93 ve 6:94 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:93 ('ûhiye' / 've lem yûha'); 6:94 ('ci'tumûnâ' / 've teraktum'); ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök قول 6:93; kök زعم 6:94; kök كون 6:93, 6:94; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 11-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 21 ve 22; bu blok bölümü kapatıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b22/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 93 94 22'; lem_bozuk.py 22 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 93 94 → AYN_SONUC; sunum/bolum4_kurallar.py 93 94 22 → KHATA_HEPSI; sunum/bolum5_kurallar.py 93 94 22 → B5_HEPSI; sunum/bolum6_kurallar.py 93 94 22 → B6_HEPSI; sunum/bolum7_kurallar.py 93 94 22 → B7_HEPSI; sunum/bolum8_kurallar.py 93 94 22 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 93 94 22 → B9_HEPSI; sunum/bolum10_kurallar.py 93 94 22 → B10_HEPSI; sunum/bolum11_kurallar.py 93 94 22 → B11_HEPSI; sunum/bolum12_kurallar.py 93 94 22 → B12_HEPSI; sunum/bolum13_kurallar.py 93 94 22 → B13_HEPSI; sunum/bolum14_kurallar.py 93 94 22 → B14_HEPSI; sunum/bolum15_kurallar.py 93 94 22 → B15_HEPSI; sunum/bolum16_kurallar.py 93 94 22 → B16_HEPSI; sunum/bolum17_kurallar.py 93 94 22 → B17_HEPSI; sunum/bolum18_kurallar.py 93 94 22 → B18_HEPSI; sunum/bolum19_kurallar.py 93 94 22 → B19_HEPSI; sunum/bolum20_kurallar.py 93 94 22 → B20_HEPSI; sunum/bolum21_kurallar.py 93 94 22 → B21_HEPSI; sunum/bolum22_kurallar.py 93 94 22 → B22_HEPSI; sunum/bolum23_kurallar.py 93 94 22 → B23_HEPSI; sunum/bolum24_kurallar.py 93 94 22 → B24_HEPSI; sunum/bolum25_kurallar.py 93 94 22 → B25_HEPSI; sunum/bolum26_kurallar.py 93 94 22 → B26_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 22 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('men', 'ezlem', 'mimmen', 'iftarâ', ''alâ', 'allâh', 'kezib', 'ev', 'mâ', 'enzele', 'yevm', 'cezâ', ''azâb', 'hûn', 'kâne'); joker kullanılmadı; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (93, 94): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_93_94.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b22.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '93', '94'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '93', '94', '22'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '93', '94', '22'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '93', '94', '22', '--tazelik-yok')}
    for _n in range(7, 27): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '93', '94', '22')
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
