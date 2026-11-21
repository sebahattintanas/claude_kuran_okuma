# sûre 6 blok 17 (6:71-73) ARIZA oluşturucu — bölüm 8-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b17/olcum.txt'
os.environ['SAY2'] = '/home/claude/b17/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Ayetler hakkında dalanlar; doğru yol Allah'ın yolu'"


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
 ("6:71", "'de'â _ dûn allâh'", 3, 'say 6:71 2-5', "harekesiz 'e-ned'û min dûni'llâh' (2-5. kelime)", ('dizi 6 71 2 5', "de'â min dûn allâh", '2-5', "biçim farkı (dizi 6 71 2 5): 6:56 fiil çekimi, zamir eki, önek; basılmamış eş fiil çekimi, zamir eki, önek")),
 ("6:71", "'_ dûn allâh'", 4, 'say 6:71 3-5', "harekesiz 'min dûni'llâh' (3-5. kelime)", None),
 ("6:73", "'_ xalaqa semâ' ard'", 2, 'say 6:73 2-5', "harekesiz 'llezî xalaqa's-semâvâti ve'l-ard' (2-5. kelime)", None),
 ("6:73", "'_ _ xalaqa'", 2, 'say 6:73 1-3', "harekesiz 've huve'llezî xalaqa' (1-3. kelime)", ('dizi 6 73 1 3', "_ ellezî xalaqa", '1-3', "biçim farkı (dizi 6 73 1 3): 6:2 zamir eki, önek")),
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

VF_YAZI = {71: {9: "'ve lâ'", 11: "'ve nuraddu'", 36: "'ve umirnâ'"}, 72: {1: "'ve en'", 4: "'ve'ttaqûh'", 5: "'ve huve'"}, 73: {1: "'ve huve'", 5: "'ve'l-arda'", 7: "'ve yevme'", 13: "'ve lehu'l-mulku'", 21: "'ve'ş-şehâdeh'", 22: "'ve huve'"}}
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
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '17', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b17/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '71', '73', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b17/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b17/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '71', '73', '17').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_71_73.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:71', '6:72', '6:73'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_71_73.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(71, 74))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:71 kök بعد ('ba'de' 14. kelime — ard), 'iz' (15. kelime — morph T, zaman), kök نفع ('yenfe'unâ' 8. kelime — fayda), kök ضرر ('yedurrunâ' 10. kelime — zarar), kök هوي ('stehvethu' 19. kelime — ayartma), kök حير ('hayrâna' 23. kelime — şaşkınlık); 6:72 kök حشر ('tuhşerûn' 8. kelime — toplanma); 6:73 kök نفخ ('yunfaxu' 16. kelime — üfürme), kök صور ('s-sûr' 18. kelime — sûr), kök غيب ('l-ğaybi' 20. kelime — gayb): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '71', '73', '17')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b17/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 18)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(71, 74))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/mutasyon_sina.py bölüm 23 kuralı 2 sınaması — 6:62 kullanıcı kararıyla e_el=? 0 olunca beklenen dize sayısız yazıldı (isabet maddedeki 'kapalı listede kural yok' notundan), b22 kural 1 sınamaları eklendi; sunum/bolum22_kurallar.py kural 1 (EMSAL_KAPSAM_DIZI) — kelime aralığı ◇'de wasl birleşmeli belirteci bir kelime sayıyordu (6:71 'dûni'llâhi', 'ke'llezi'stehvethu' — 2:120 kalıbı 27-29 sanıldı, gerçek 31-35), aralık bölüm 8 kuralı 14'ün kelime sayımıyla eşlendi; düzeltmeyle 6:71 'min dûni'llâh' / 10:106 gerçek eksik kaydı açığa çıktı ve bu blokta karara bağlandı; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 200",
 "geriye dönük koşu (araç değişen blok — bekleyen_ariza_6_b13 elle önerisi (8) GERIYE_DONUK_ZORUNLU; komut 'python3 sunum/geriye_donuk.py b17 yamalar/geriye_donuk_6_b15k.txt'; metin ve karar kesinleştikten sonra): GERI_P; "
 "araç değişti sınıfı: blok 10 6:45 'say 6:45 6-9' / 37:182 emsal kapsamı — eski aralık sayımı yanlışlıkla örtüyordu, gerçek eksik (tam okuma sonu); blok 15 esmâ satırı e_el=? 1 → 0 (6:62 kullanıcı kararı; isabet 'kapalı listede kural yok' notundan sürüyor); "
 "basılan değişti: blok 01, 07 ve 13 R5 gerekçe çıktıları 6:70, 6:71 ve 6:73 basılınca değişti; blok 16 ve 17 ZAMİR KAYITSIZ — kelime_kontrol kesim sorunu (bekleyen); kayıtlar geriye dönük yeniden yazılmadı; isabetler tam okuma sonu listesinde (yamalar/geriye_donuk_6_b17.txt)",
 "kök tablosu: ölçümde '???' 6:71 23. kelime için 1 — yeni kök حير ('şaşırma, şaşkınlık (hayrân)'; yamalar/yama_kok_6_71.py → kok_ekle_6.ISTEK; kok_turkce 1626); ölçüm yeniden alındı, '???' 0; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 71 73 17'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:73 ''âlimu'l-ğaybi ve'ş-şehâdeh' (19-21. kelime) ve 've huve'l-hakîmu'l-xabîr' (22-24. kelime) — esma_el 'ilahi', kural 'zamirin haberi' (Allah); 6:71 ve 6:72 esmâ yok; "
 "lafız 6:71; Rab 6:71 (38. kelime) (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 71 73 17'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:71 '{{1|fâsıla ٱلعلمين → ن, N sınıfı}}', '{{1|simetri \\[6, 15, 31, 2\\]}}', '{{1|harf 164 → harf3 158, isaret 6}}', '{{1|dış düğüm 6}}', '{{1|EDİLGEN 2/12 fiil, pas z=0,62}}', '{{1|HAPAKS: حير}}' ve '{{1|hapaks z=3,28}}'; "
 "6:72 '{{2|fâsıla تحشرون → ن, N sınıfı}}', '{{2|harf 40 → harf3 38, isaret 2}}', '{{2|dış düğüm 0}}' ve '{{2|EDİLGEN 1/3 fiil, pas z=1,57}}'; "
 "6:73 '{{3|fâsıla ٱلخبير → ر, R sınıfı — KAFİYE KIRILMASI}}', '{{3|harf 107 → harf3 102, isaret 5}}', '{{3|dış düğüm 0}}' ve '{{3|EDİLGEN 1/5 fiil, pas z=0,81}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 71 73 17'): KALAN_P",
 "ölçüm aktör: 6:71 '{{1|aktör: adlı شَيْطان 20\\. sırada \\(gayb, rol fail\\)}}'; 6:72 ve 6:73 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:71 soru, emir — IMPV 3 'qul' (1.), 'i'tinâ' (29.), 'qul' (30.), INTG 1 'e-ned'û' (2.), NEG 2 'lâ' (7.), 've lâ' (9.); "
 "6:72 emir — IMPV 2 'eqîmu' (2.), 've'ttaqûh' (4.); 6:73 emir — IMPV 1 'kun' (9.); "
 "morph T ('ba'de' 6:71 14., 'iz' 6:71 15.), ACC ('inne' 6:71 31.), PRP ('li' 6:71 37.), SUB ('en' 6:72 1.), REM ('ve' 6:72 5.; 6:73 13., 22.; 'fe' 6:73 10.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:71 ★★★ (kaynak hapaks, z=3,28; eşiği geçen öbür ölçüler n z=2,82); 6:72 ★ (kaynak pas, z=1,57); 6:73 ★ (kaynak n, z=1,23; kafiye kırığı)",
 "fâsıla: 6:70 ن → 6:71 ن (ٱلعلمين) → 6:72 ن (تحشرون) → 6:73 ر (ٱلخبير) — N sınıfı, 6:73 R sınıfı (ölçüm KAFİYE KIRILMASI); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:71 2:120 ve 10:106 (emsal olarak basıldı), 40:66 (basılmış) ve okunmuş 3 ayet; 6:72 xref yok; 6:73 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:71 'de'â _ dûn allâh' ve '_ dûn allâh' süzgeç GEÇER; 6:73 '_ xalaqa semâ' ard' süzgeç GEÇER, '_ _ xalaqa' GEÇMEZ; 6:72 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; edilgen fiilde naib-i fail — sûre 6 bölüm 2 denetimi kuralı 5; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:71 muhatap 2MS, konuşan 1P (söz içi), 3MS ('yenfe'unâ', 'yedurrunâ' — gönderge 'mâ' 6. kelime; 'hedânâ'llâh' 16. kelime — fail 17. kelime; 'lehû' — gönderge 'ke'llezi' 18. kelime), 3FS ('stehvethu' 19. kelime — fail 20. kelime), 3MP ('yed'ûnehû' — gönderge 'ashâbun' 25. kelime); "
 "6:72 muhatap 2MP ('tuhşerûn' edilgen — naib-i faili zamir), 3MS (gönderge 6:71 38. kelime); 6:73 3MS (gönderge 6:72 5. kelime; 'yunfaxu' edilgen — naib-i faili zamir), muhatap 2MS ('kun', söz içi) — betik denetimi: KHATA_ADSIZ; "
 "ileri / tartışmalı gönderge (bekleyen_ariza_6_b15 elle önerisi (10)): 6:71 'huve' (34. kelime) — ayırma zamiri, 'hude'llâhi' (32. kelime); 6:72 3MS — 6:71 'li-rabbi'l-'âlemîn' (38. kelime) (okuma); "
 "6:73 'fe-yekûn' 3MS — 'kun' muhatabı, ayet içinde adı yok (okuma, tam okuma sonu)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:71 söz 2-29. kelime ve 31-39. kelime ('qul' 1. ve 30. kelime); 6:73 söz 9. kelime ('kun'); 6:72 söz yok; mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 71 73 17' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:71 've lâ' (9.), 've nuraddu' (11.), 've umirnâ' (36.) CONJ; 6:72 've en' (1.), 've'ttaqûh' (4.) CONJ, 've huve' (5.) REM; "
 "6:73 've huve' (1.), 've'l-arda' (5.), 've yevme' (7.), 've'ş-şehâdeh' (21.) CONJ, 've lehu'l-mulku' (13.), 've huve' (22.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:71 ◈K أرض ('l-ardi' 22. kelime — K1); 6:73 ◈K سمو ('s-semâvâti' 4. kelime — K1); 6:73 ◈K أرض ('l-arda' 5. kelime — K1); 6:73 ◈K يوم ('yevme' 7. ve 15. kelime — K2); 6:73 ◈B خلق ('xalaqa' 3. kelime — B2)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 71 73 17'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:71 (2:120, 10:106); 6:72 ve 6:73 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş (6:73 've huve'l-hakîmu'l-xabîr' — 6:18; 6:71 'li-rabbi'l-'âlemîn' — 40:66 geniş kalıp), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:71 söz açılır / kapanır (2. / 29. kelime; 31. / 39. kelime), şahıs geçişi 3 → 1, edim geçişi emir, şart → soru, emir; "
 "6:72 şahıs geçişi 1 → 2, edim geçişi soru, emir → emir; 6:73 söz açılır / kapanır (9. kelime), şahıs geçişi 2 → 3, edim geçişi yok, bölüm kapanışı; "
 "şahıs beraberliği 6:71 (kişi toplamı 1. şahıs 10 / 3. şahıs 10, ölçüm baskın 1 — bölüm 23 denetimi kuralı 3, sûre 6 bölüm 1 denetimi kuralı 9); ölçüm iltifât 6:71-73 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:71 'e-ned'û' — inkâri soru (morph INTG); 'ba'de iz hedânâ'llâh' — zaman zarfı (morph T + T); 'ke'llezi'stehvethu' — benzetme (morph P + REL); 'inne hude'llâhi huve'l-hudâ' — tekit ve ayırma zamiri (morph ACC); "
 "'li-nuslime' — amaç lâmı (morph PRP); 6:72 've en eqîmu' — masdar cümleciği, 6:71 'li-nuslime' ile atıf (morph CONJ + SUB); 've huve'llezî' — isim cümlesi (morph REM); "
 "6:73 'kun fe-yekûn' — emir ve sonuç (morph REM); ''âlimu'l-ğaybi' — mübteda takdirli haber",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:71 'inne hude'llâhi huve'l-hudâ' — 2:120 ile eş (sayım: 'say 6:71 31-35'); "
 "6:71 'mâ lâ yenfe'unâ ve lâ yedurrunâ' — 10:106 ile lemma dizisi eşi (sayım: 'dizi 6 71 6 10', 'dizi 6 71 2 10'); 6:71 kök هدي ×4, أله ×3; 6:73 've huve'l-hakîmu'l-xabîr' — 6:18 ile sûre içi eş (sayım: 'say 6:73 22-24'); "
 "6:73 'llezî xalaqa's-semâvâti ve'l-ard' — 6:1 ile sûre içi kalıp (sayım: 'say 6:73 2-5'); 6:73 kök حقق, قول, كون, يوم ikilemeleri; 6:73 kafiye kırılması ر — bölüm kapanışı",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 17'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'inne hude'llâhi huve'l-hudâ' 6:71 'Şüphesiz Allah'ın doğru yolu, asıl doğru yoldur' / 2:120 'Allah'ın yolu, asıl yol odur' (emsal metninde) — çakışma — tam okuma sonu ('doğru yol' / 'yol' karşılığı, 'Şüphesiz' / karşılıksız 'inne'); "
 "'mâ lâ yenfe'unâ ve lâ yedurrunâ' 6:71 'fayda vermeyen ve zarar vermeyen şeyleri' / 10:106 'ne fayda ne zarar verebilecek olana' (emsal metninde) — çakışma — tam okuma sonu ('vermeyen' / 'ne … ne'; 'şeyleri' / 'olana'); 'min dûni'llâh' 6:71 'Allah'tan başka' / 10:106 'Allah'tan başka' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:71 'qul' IMPV — meal 'De'; 'e-ned'û' IMPF IND (soru) — meal 'çağıralım'; 'yenfe'unâ' IMPF IND — meal 'fayda vermeyen'; "
 "'yedurrunâ' IMPF IND — meal 'zarar vermeyen'; 've nuraddu' IMPF IND edilgen (soru) — meal 'geri mi döndürülelim'; 'hedânâ'llâh' PERF — meal 'ilettikten'; 'stehvethu' PERF — meal 'ayarttığı'; 'yed'ûnehû' IMPF IND — meal 'çağıran'; "
 "'i'tinâ' IMPV — meal 'gel'; 've umirnâ' PERF edilgen — meal 'emredildik'; 'li-nuslime' IMPF SUBJ — meal 'teslim olalım diye'; 6:72 'eqîmu' IMPV — meal 'kılın'; 've'ttaqûh' IMPV — meal 'sakının'; 'tuhşerûn' IMPF IND edilgen — meal 'toplanacağınız'; "
 "6:73 'xalaqa' PERF — meal 'yaratandır'; 'yeqûlu' IMPF IND — meal 'dediği'; 'kun' IMPV — meal 'Ol'; 'fe-yekûn' IMPF IND — meal 'oluverir'; 'yunfaxu' IMPF IND edilgen — meal 'üfürüleceği'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 71 73 17'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:71, 6:72 ve 6:73 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:71 ('yenfe'unâ' / 'yedurrunâ'; 'hedânâ'llâh' / 'stehvethu'); 6:73 ('s-semâvâti' / 've'l-arda'; 'l-ğaybi' / 've'ş-şehâdeh'); 6:72 karşıt çift yok; "
 "ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök هدي 6:71 ('hedânâ'llâh', 'l-hudâ', 'hude'llâhi'); kök دعو 6:71 ('e-ned'û', 'yed'ûnehû'); kök حقق 6:73 ('bi'l-haqq', 'l-haqq'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 8-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 16 ve 17; bu blok bölümü kapatıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b17/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 71 73 17'; lem_bozuk.py 17 çıktısı): lem_bozuk bayrağı 6:71 10. kelime (يَضُرَّ — 'yedurrunâ') ve 19. kelime (اسْتَهْوَتْ — 'stehvethu'), meal kayıtlarında '(morph LEM ham biçim)' notu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 71 73 → AYN_SONUC; sunum/bolum4_kurallar.py 71 73 17 → KHATA_HEPSI; sunum/bolum5_kurallar.py 71 73 17 → B5_HEPSI; sunum/bolum6_kurallar.py 71 73 17 → B6_HEPSI; sunum/bolum7_kurallar.py 71 73 17 → B7_HEPSI; sunum/bolum8_kurallar.py 71 73 17 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 71 73 17 → B9_HEPSI; sunum/bolum10_kurallar.py 71 73 17 → B10_HEPSI; sunum/bolum11_kurallar.py 71 73 17 → B11_HEPSI; sunum/bolum12_kurallar.py 71 73 17 → B12_HEPSI; sunum/bolum13_kurallar.py 71 73 17 → B13_HEPSI; sunum/bolum14_kurallar.py 71 73 17 → B14_HEPSI; sunum/bolum15_kurallar.py 71 73 17 → B15_HEPSI; sunum/bolum16_kurallar.py 71 73 17 → B16_HEPSI; sunum/bolum17_kurallar.py 71 73 17 → B17_HEPSI; sunum/bolum18_kurallar.py 71 73 17 → B18_HEPSI; sunum/bolum19_kurallar.py 71 73 17 → B19_HEPSI; sunum/bolum20_kurallar.py 71 73 17 → B20_HEPSI; sunum/bolum21_kurallar.py 71 73 17 → B21_HEPSI; sunum/bolum22_kurallar.py 71 73 17 → B22_HEPSI; sunum/bolum23_kurallar.py 71 73 17 → B23_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 17 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('mâ', 'lâ', 'nefe'a', 'yedurre' (morph LEM ham biçim), 'inne', 'hudâ', 'allâh', 'de'â', 'min', 'dûn', 'ellezî', 'xalaqa', 'semâ'', 'ard', 'hakîm', 'xabîr'); joker '_' yalnız lemmasız öğede; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (71, 73): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_71_73.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b17.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '71', '73'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '71', '73', '17'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '71', '73', '17'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '71', '73', '17', '--tazelik-yok')}
    for _n in range(7, 24): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '71', '73', '17')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23 = [_R['B%d' % _n].splitlines() for _n in range(6, 24)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
