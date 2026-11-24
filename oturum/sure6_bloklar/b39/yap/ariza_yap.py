# sûre 6 blok 39 (6:158-160) ARIZA oluşturucu — bölüm 19-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b39/olcum.txt'
os.environ['SAY2'] = '/home/claude/b39/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b38.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {}
BOL = "'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'"


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
 ("6:159", "'summe nebbe'e mâ kâne'", 2, 'say 6:159 15-18', "harekesiz 'summe yunebbi'uhum bimâ kânû' (15-18. kelime)", ('dizi 6 159 15 18', "summe nebbe'e mâ kâne", '15-18', "biçim farkı (dizi 6 159 15 18): 6:60 fiil çekimi, zamir eki")),
 ("6:159", "'nebbe'e mâ kâne'", 4, 'say 6:159 16-18 --on', "önek kesilmiş 'yunebbi'uhum bimâ kânû' (16-18. kelime)", ('dizi 6 159 16 18', "nebbe'e mâ kâne", '16-18', "biçim farkı (dizi 6 159 16 18): 6:60 fiil çekimi, zamir eki; 6:108 önek; basılmamış eş fiil çekimi, zamir eki, önek")),
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

VF_YAZI = {158: {}, 159: {5: "'ve kânû'"}, 160: {7: "'ve men'", 14: "'ve hum'"}}
sys.path.insert(0, '/home/claude/b39/yap')
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
open('/home/claude/b39/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '39')
BLOKLAR = [str(i) for i in range(1, 40)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '39', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b39/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '158', '160', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b39/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b39/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '158', '160', '39').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_158_160.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:158', '6:159', '6:160'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_158_160.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(158, 161))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:158 kök نفس ('nefsen' 22. kelime — can), kök قبل ('qablu' 28. kelime — önce); 6:160 kök سوأ ('s-seyyi'eti' 9. kelime — kötülük)"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '158', '160', '39')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b39/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 40)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(158, 161))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 18 kapanışında sunum/bolum34_kurallar.py eklendi (kural 1-5), sunum/bolum19_kurallar.py KURAL_ATIF bölüm 18, sunum/geriye_donuk.py bolum34 satırı, sunum/mutasyon_sina.py b34 sınamaları (364 / 364); blok 38'de sunum/bolum15_kurallar.py kural 14 düzenli ifadesine sayı sınırı eklendi; bu blokta sunum/yasakli.sh Türkçe ikileme listesine 'bölük bölük' eklendi (bölüm 8 kuralı 16); yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 343",
 "geriye dönük koşu (bölüm 18 kapanışı, komut 'python3 sunum/geriye_donuk.py b38k yamalar/geriye_donuk_6_b36k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 158 160 39'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:158-160 esmâ yok; esma_el kaydı yok; 6:158 Rab (9., 14. ve 19. kelime), 6:159 lafız (14. kelime); 6:160 lafız ve Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 158 160 39'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:158 '{{1|fâsıla منتظرون → ن, N sınıfı}}', '{{1|simetri \\[5, 9, 14, 1\\]}}', '{{1|harf 140 → harf3 136, isaret 4}}' ve '{{1|dış düğüm 2}}'; "
 "6:159 '{{2|fâsıla يفعلون → ن, N sınıfı}}', '{{2|simetri \\[3, 1, 8, 1\\]}}', '{{2|harf 82 → harf3 77, isaret 5}}' ve '{{2|dış düğüm 1}}'; "
 "6:160 '{{3|EDİLGEN 2/4 fiil, pas z=2,52}}', '{{3|fâsıla يظلمون → ن, N sınıfı}}', '{{3|sayı işareti عَشْر}}', '{{3|simetri \\[4, 1, 7, 1\\]}}', '{{3|harf 66 → harf3 64, isaret 2}}' ve '{{3|dış düğüm 2}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 158 160 39'): KALAN_P",
 "ölçüm aktör: 6:158-160 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:158 soru, emir — IMPV 2 'quli' (34.), 'ntezirû' (35.), INTG 1 'hel' (1.), NEG 2 'lâ' (20.), 'lem' (24.), RES 1 'illâ' (3.); ölçüm biçim HASR (D2'de yazılmadı); "
 "6:159 haber — kip yok; 6:160 şart — COND 2 'men' (1.), 'men' (7.), NEG 2 'lâ' (10.), 'lâ' (15.), RES 1 'illâ' (12.); ölçüm biçim HASR (D2'de yazılmadı); "
 "morph SUB ('en' 6:158 4.), ACC ('innâ' 6:158 36., 'inne' 6:159 1., 'innemâ' 6:159 11.), RSLT ('fe-lehû' 6:160 4., 'fe-lâ' 6:160 10.), CIRC ('ve hum' 6:160 14.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:158 ★★ (kaynak n, z=2,61); 6:159 yıldız yok; 6:160 ★★ (kaynak pas, z=2,52)",
 "fâsıla: 6:157 ن → 6:158 ن (منتظرون) → 6:159 ن (يفعلون) → 6:160 ن (يظلمون) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:158 16:33 (emsal olarak basıldı) ve okunmuş 1 ayet; 6:159 30:32 (emsal olarak basıldı); 6:160 28:84 (emsal olarak basıldı), 40:40 (emsal olarak basıldı)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:159 'summe nebbe'e mâ kâne' süzgeç GEÇER, 'nebbe'e mâ kâne' süzgeç GEÇER; 6:158 ve 6:160 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "6:158 3MP ('yenzurûne'; 'te'tiyehumu' eki — gönderge 6:157 27. kelime), 3FS ('te'tiyehumu' — fiil uyumu, fail 6. kelime; 'tekun', 'âmenet', 'kesebet'; 'îmânuhâ', 'îmânihâ' ekleri — gönderge 'nefsen' 22. kelime), 3MS ('ye'tiye', 'ye'tiye', 'ye'tî', 'yenfe'u' — fiil uyumu, fail 9., 12., 17. ve 23. kelime), "
 "muhatap 2MS ('quli'; ekler 'rabbuke', 'rabbik', 'rabbike'), muhatap 2MP ('ntezirû' — söz içi), konuşan 1P eki ('innâ' — söz içi); "
 "6:159 3MP ('ferraqû', 'kânû', 'kânû', 'yef'alûn'; 'dînehum', 'minhum', 'emruhum', 'yunebbi'uhum' ekleri — gönderge 'llezîne' 2. kelime), muhatap 2MS ('leste'), 3MS ('yunebbi'uhum' — gönderge 'llâhi' 14. kelime); "
 "6:160 3MS ('câ'e', 'câ'e' — gönderge 'men' 1. ve 7. kelime; 'fe-lehû' — gönderge 'men' 1. kelime; 'yuczâ' — edilgen, naib-i faili 'men' 7. kelime), 3FS ('emsâlihâ', 'mislehâ' ekleri — gönderge 'l-haseneti' 3. kelime ve 's-seyyi'eti' 9. kelime), 3MP ('hum' — tartışmalı, gönderge 'men' 1. kelime; 'yuzlemûn' — edilgen, naib-i faili 'hum' 14. kelime)",
 "6:158-160 gönderge zinciri: 6:158 3MP göndergesi 6:157 27. kelime (okuma); 'quli' (34. kelime) muhatabı muhatap 2MS (adsız), söz 35-37. kelimede muhatap 2MP; 6:159 muhatap 2MS, 3MP göndergesi 'llezîne' (2. kelime); 6:160 'hum' (14. kelime) göndergesi iyilikle ve kötülükle gelenler (okuma; tartışmalı)",
 "edilgen: 6:160 'yuczâ' (11. kelime; naib-i faili 'men' 7. kelime) ve 'yuzlemûn' (16. kelime; naib-i faili 'hum' 14. kelime) — ölçüm EDİLGEN 2/4; 6:158 ve 6:159 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:158 'quli' (34.) ardından söz 35-37. kelime, ayet sonunda kapanır; 6:159 ve 6:160 söz yok; mealde 'De ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 158 160 39' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:158 've' yok; 6:159 've kânû' (5.) CONJ; 6:160 've men' (7.) CONJ, 've hum' (14.) CIRC; "
 "'fe' konumları: 6:160 'fe-lehû' (4.), 'fe-lâ' (10.) RSLT",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:158 ◈K يوم ('yevme' 15. kelime — K2); 6:159 ve 6:160 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 158 160 39'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:158 (16:33); 6:159 (30:32); 6:160 (28:84, 40:40); D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 6:158 أتي ×4, أمن ×3, أيي ×2, بعض ×2, ربب ×3, نظر ×3; 6:159 كون ×2; 6:160 جيأ ×2, مثل ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:158 söz açılır (35. kelime), söz kapanır (37. kelime, ayet içi), muhatap geçişi 2MS → 2MP (ayet içi), şahıs geçişi yok, edim geçişi soru, şart → soru, emir; bölüm açılışı; "
 "6:159 şahıs geçişi yok, edim geçişi soru, emir → haber; 6:160 şart → cevap (ayet içi; COND 'men' 1. kelime), şart → cevap (ayet içi; COND 'men' 7. kelime), şahıs geçişi yok, edim geçişi haber → şart; "
 "ölçüm iltifât 6:158-160 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:158 'hel yenzurûne illâ en' — soru ve hasr (morph INTG + RES); 6:158 'lem tekun âmenet min qablu' — 'nefsen' sıfat cümlesi (morph NEG); 6:159 'inne'llezîne ferraqû dînehum' — konu ve haber (morph ACC); "
 "6:160 'men câ'e bi'l-haseneti fe-lehû' — şart ve cevap (morph COND + RSLT); 6:160 've hum lâ yuzlemûn' — hâl (morph CIRC)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:158 1-8. kelime — 16:33 ile harekesiz eş (sayım: 'say 6:158 1-8'); 6:159 2-6. kelime — 30:32 ile harekesiz eş (sayım: 'say 6:159 2-6'); "
 "6:160 7-11. kelime — 28:84 ile harekesiz eş (sayım: 'say 6:160 7-11'); 6:160 1-4. kelime — 28:84 ile harekesiz eş (sayım: 'say 6:160 1-4'); 6:160 10-13. kelime — 40:40 ile harekesiz eş (sayım: 'say 6:160 10-13'); 6:158 kök أتي, أمن, أيي, بعض, ربب, نظر ikilemeleri; 6:159 kök كون ikilemesi; 6:160 kök جيأ, مثل ikilemeleri",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 39'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'hel yenzurûne illâ en te'tiyehumu'l-melâ'iketu ev ye'tiye' 6:158 'Onlar, kendilerine meleklerin gelmesinden ya da' / 16:33 'Onlar, kendilerine meleklerin gelmesinden ya da' (emsal metninde) — çakışma değil (bayt eşit); "
 "'hel yenzurûne illâ' 6:158 'başka bir şey mi bekliyorlar' / 16:33 'başka bir şey mi bekliyorlar' (emsal metninde) — çakışma değil (bayt eşit); 'yenzurûne illâ' 6:158 'başka bir şey mi bekliyorlar' / 16:33 'başka bir şey mi bekliyorlar' (emsal metninde) — çakışma değil (bayt eşit); "
 "'llezîne ferraqû dînehum ve kânû şiya'an' 6:159 'Dinlerini parçalayıp bölük bölük olanlar' / 30:32 'Dinlerini parçalayıp bölük bölük olanlar' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve men câ'e bi's-seyyi'eti fe-lâ yuczâ' 6:160 'Kim de bir kötülükle gelirse, yalnızca onun dengiyle karşılık görür' / 28:84 'Kim de bir kötülükle gelirse, kötülük işleyenler ancak yaptıklarının karşılığını görürler' (emsal metninde) — çakışma — tam okuma sonu ('karşılık gör-' / 'karşılığını gör-' bağlam karşılığı); "
 "'men câ'e bi'l-haseneti fe-lehû' 6:160 'Kim bir iyilikle gelirse ona' / 28:84 'Kim bir iyilikle gelirse ona' (emsal metninde) — çakışma değil (bayt eşit); "
 "'fe-lâ yuczâ illâ mislehâ' 6:160 'yalnızca onun dengiyle karşılık görür' / 40:40 'yalnızca onun dengiyle karşılık görür' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 6:158 'yenzurûne' IMPF IND — meal 'bekliyorlar'; 'te'tiye' IMPF SUBJ ('en' ile) — meal 'gelmesinden'; 'ye'tiye' IMPF SUBJ (8. kelime) — meal 'gelmesinden'; 'ye'tiye' IMPF SUBJ (11. kelime) — meal 'gelmesinden'; 'ye'tî' IMPF IND — meal 'geldiği'; "
 "'yenfe'u' IMPF IND ('lâ' ile) — meal 'vermez'; 'tekun' IMPF JUS ('lem' ile) — meal 'olan'; 'âmenet' PERF — meal 'inanmamış'; 'kesebet' PERF — meal 'kazanmamış'; 'quli' IMPV — meal 'De'; 'ntezirû' IMPV — meal 'Bekleyin'; "
 "6:159 'ferraqû' PERF — meal 'parçalayıp'; 'kânû' PERF (5. kelime) — meal 'olanlara'; 'leste' PERF — meal 'değilsin'; 'yunebbi'u' IMPF IND — meal 'verecektir'; 'kânû' PERF (18. kelime) — meal 'olduklarını'; 'yef'alûn' IMPF IND — meal 'yapmakta'; "
 "6:160 'câ'e' PERF (2. kelime) — meal 'gelirse'; 'câ'e' PERF (8. kelime) — meal 'gelirse'; 'yuczâ' IMPF PASS SUBJ ('lâ' ile) — meal 'görür'; 'yuzlemûn' IMPF PASS JUS ('lâ' ile) — meal 'zulmedilmez'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'ye'tî' IMPF 6:158'de sıfat-fiil ('-diği') ile; 'âmenet', 'kesebet' PERF 6:158'de sıfat-fiil ('-mış') ile; 'ferraqû' PERF 6:159'da zarf-fiil ('-yıp') ile; 'kânû' PERF 6:159'da sıfat-fiil ('-anlar', '-dukları') ile; 'leste' PERF 6:159'da şimdiki zaman ('değilsin') ile; 'câ'e' PERF 6:160'ta şart ('-irse') ile; 'yuczâ' (morph SUBJ) ve 'yuzlemûn' (morph JUS) 6:160'ta geniş zaman ile (morph MOOD ham etiketi)",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 158 160 39'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:158-160 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:160 ('bi'l-haseneti' / 'bi's-seyyi'eti'); 6:158 ve 6:159 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök كون 6:158 ('tekun') ve 6:159 ('kânû', 'kânû'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 19-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 39 ve 40; bölüm açılışı bu blokta; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b39/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 158 160 39'; lem_bozuk.py 39 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 158 160 → AYN_SONUC; sunum/bolum4_kurallar.py 158 160 39 → KHATA_HEPSI; sunum/bolum5_kurallar.py 158 160 39 → B5_HEPSI; sunum/bolum6_kurallar.py 158 160 39 → B6_HEPSI; sunum/bolum7_kurallar.py 158 160 39 → B7_HEPSI; sunum/bolum8_kurallar.py 158 160 39 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 158 160 39 → B9_HEPSI; sunum/bolum10_kurallar.py 158 160 39 → B10_HEPSI; sunum/bolum11_kurallar.py 158 160 39 → B11_HEPSI; sunum/bolum12_kurallar.py 158 160 39 → B12_HEPSI; sunum/bolum13_kurallar.py 158 160 39 → B13_HEPSI; sunum/bolum14_kurallar.py 158 160 39 → B14_HEPSI; sunum/bolum15_kurallar.py 158 160 39 → B15_HEPSI; sunum/bolum16_kurallar.py 158 160 39 → B16_HEPSI; sunum/bolum17_kurallar.py 158 160 39 → B17_HEPSI; sunum/bolum18_kurallar.py 158 160 39 → B18_HEPSI; sunum/bolum19_kurallar.py 158 160 39 → B19_HEPSI; sunum/bolum20_kurallar.py 158 160 39 → B20_HEPSI; sunum/bolum21_kurallar.py 158 160 39 → B21_HEPSI; sunum/bolum22_kurallar.py 158 160 39 → B22_HEPSI; sunum/bolum23_kurallar.py 158 160 39 → B23_HEPSI; sunum/bolum24_kurallar.py 158 160 39 → B24_HEPSI; sunum/bolum25_kurallar.py 158 160 39 → B25_HEPSI; sunum/bolum26_kurallar.py 158 160 39 → B26_HEPSI; sunum/bolum27_kurallar.py 158 160 39 → B27_HEPSI; sunum/bolum28_kurallar.py 158 160 39 → B28_HEPSI; sunum/bolum29_kurallar.py 158 160 39 → B29_HEPSI; sunum/bolum30_kurallar.py 158 160 39 → B30_HEPSI; sunum/bolum31_kurallar.py 158 160 39 → B31_HEPSI; sunum/bolum32_kurallar.py 158 160 39 → B32_HEPSI; sunum/bolum33_kurallar.py 158 160 39 → B33_HEPSI; sunum/bolum34_kurallar.py 158 160 39 → B34_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 39 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; 6:158 ölçüm xref'indeki okunmuş 1 ayet harekesiz sayımla bulunmadı — emsal alınmadı; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('hel', 'nazara', 'illâ', 'en', 'etâ', 'melek', 'ev', 'ellezî', 'ferraqu' (morph LEM ham biçim), 'dîn', 'kâne', 'şî'a', 'summe', 'nebbe'e', 'mâ', 'men', 'câ'e', 'seyyi'e', 'lâ', 'cezâ', 'misl'); joker '_' kullanılmadı; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (158, 160): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_158_160.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '158', '160'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '158', '160', '39'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '158', '160', '39'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '158', '160', '39', '--tazelik-yok')}
    for _n in range(7, 35): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '158', '160', '39')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
