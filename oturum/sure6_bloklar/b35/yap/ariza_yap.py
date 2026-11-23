# sûre 6 blok 35 (6:145-147) ARIZA oluşturucu — bölüm 17-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b35/olcum.txt'
os.environ['SAY2'] = '/home/claude/b35/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b34.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {}
BOL = "'Haram kılınanlar; şahitlerinizi getirin'"


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
 ("6:145", "'mâ evhâ ilâ'", 2, 'say 6:145 5-7', "harekesiz 'mâ ûhiye ileyye' (5-7. kelime); biçim öğesi 'evhâ' çekimi (lemma dizisi sûre içi 3, nakarat3 2)", ('dizi 6 145 5 7', "mâ evhâ ilâ", '5-7', "biçim farkı (dizi 6 145 5 7): 6:50 yazım eş; 6:106 zamir eki; öneksiz eş koşusu (dizi 6 145 5 7): 6:50 → önek kesilmiş sûre içi 1; 6:106 → önek kesilmiş sûre içi 1")),
 ("6:145", "'en kâne meyte'", 2, 'say 6:145 13-15', "harekesiz 'en yekûne meyteten' (13-15. kelime); biçim öğesi 'en' edatı (lemma dizisi sûre içi 1, nakarat3 2)", ('dizi 6 145 13 15', "en kâne meyte", '13-15', "biçim farkı (dizi 6 145 13 15): sûre içi eş yok; öneksiz eş koşusu (dizi 6 145 13 15): sûre içi eş yok")),
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

VF_YAZI = {145: {34: "'ve lâ'"}, 146: {1: "'ve 'ale'", 8: "'ve mine'", 10: "'ve'l-ğanemi'", 27: "'ve innâ'"}, 147: {8: "'ve lâ'"}}
sys.path.insert(0, '/home/claude/b35/yap')
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
open('/home/claude/b35/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '35')
BLOKLAR = [str(i) for i in range(1, 36)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '35', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b35/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '145', '147', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b35/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b35/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '145', '147', '35').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_145_147.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:145', '6:146', '6:147'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_145_147.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(145, 148))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:145 kök دمو ('demen' 17. kelime — kan), kök لحم ('lahme' 20. kelime — et), kök خنزر ('xinzîrin' 21. kelime — domuz); 6:146 kök ظفر ('zufur' 7. kelime — tırnak), kök بقر ('l-baqari' 9. kelime — sığır), kök غنم ('l-ğanemi' 10. kelime — koyun), kök شحم ('şuhûmehumâ' 13. kelime — iç yağ), kök ظهر ('zuhûruhumâ' 17. kelime — sırt), kök حوي ('l-havâyâ' 19. kelime — bağırsak), kök عظم (''azm' 23. kelime — kemik): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '145', '147', '35')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b35/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 36)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(145, 148))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 16 kapanışında sunum/bolum32_kurallar.py eklendi (kural 1-5), sunum/bolum19_kurallar.py KURAL_ATIF bölüm 16, sunum/geriye_donuk.py bolum32 satırı, sunum/mutasyon_sina.py b32 sınamaları (343 / 343); bu blokta araç değişikliği yok; yeni kök: yamalar/yama_kok_6_145.py (شحم) → kok_ekle_6.py, ölçüm yeniden koşuldu; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 317",
 "geriye dönük koşu (bölüm 16 kapanışı, komut 'python3 sunum/geriye_donuk.py b34k yamalar/geriye_donuk_6_b31k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 145 147 35'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "kök tablosu: 6:146 شحم (iç yağ (şahm)) yeni kök — yamalar/yama_kok_6_145.py; ölçüm HAPAKS alanı yeni karşılıkla yeniden koşuldu; kok_envanteri شحم 1 ayet",
 "esmâ: 6:145 'fe-inne rabbeke ğafûrun rahîm' (36-39. kelime) — esma_el 'ilahi', kural ''inne/enne' haberi' (Rab) ve 'rahîm' (39. kelime) için kural ''inne/enne' haberi' (Rab; morph ADJ ile 'ğafûr'un sıfatı) (yamalar/esma_el_6_145_147.txt); غَفُور ve رَحِيم lemmalarında önceki 'ilahi' kayıtlarıyla karar eş; 6:146 ve 6:147 esmâ yok; 6:145 lafız (28. kelime) ve Rab (37. kelime), 6:147 Rab (4. kelime); 6:146 lafız ve Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 145 147 35'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 6:145 esma_kayit 'mühür EVET (ÇİFT)' — ölçüm MÜHÜR ile uyuşuyor, muhur_el EVET): " + EMH,
 "ölçüm: 6:145 '{{1|EDİLGEN 3/7 fiil, pas z=2,12}}', '{{1|fâsıla رحيم → م, N sınıfı}}', '{{1|simetri \\[3, 2, 5, 1\\]}}', '{{1|harf 139 → harf3 128, isaret 11}}' ve '{{1|dış düğüm 5}}'; "
 "6:146 '{{2|HAPAKS: شحم \\*\\(iç yağ \\(şahm\\)\\)\\* — hapaks z=3,28}}', '{{2|fâsıla لصدقون → ن, N sınıfı}}', '{{2|simetri \\[4, 12, 18, 1\\]}}', '{{2|harf 126 → harf3 120, isaret 6}}' ve '{{2|dış düğüm 0}}'; "
 "6:147 '{{3|EDİLGEN 1/3 fiil, pas z=1,57}}', '{{3|fâsıla ٱلمجرمين → ن, N sınıfı}}', '{{3|harf 53 → harf3 50, isaret 3}}' ve '{{3|dış düğüm 1}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 145 147 35'): KALAN_P",
 "ölçüm aktör: 6:145, 6:146 ve 6:147 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:145 emir, şart — COND 1 'meni' (30.), IMPV 1 'qul' (1.), NEG 2 'lâ' (2.), 'lâ' (34.); ölçüm biçim ISTISNA (D2'de yazılmadı); "
 "6:146 haber — EMPH 1 'le-sâdiqûn' (28.); ölçüm biçim ISTISNA (D2'de yazılmadı); 6:147 emir, şart — COND 1 'in' (1.), IMPV 1 'qul' (3.), NEG 1 'lâ' (8.); "
 "morph EXP ('illâ' 6:145 12., 6:146 14.), SUB ('en' 6:145 13.), REM ('fe-innehû' 6:145 22., 'fe-meni' 6:145 30., 've innâ' 6:146 27., 'fe-in' 6:147 1., 've lâ' 6:147 8.), RSLT ('fe-inne' 6:145 36., 'fe-qul' 6:147 3.), ACC ('innehû' 6:145 22., 'inne' 6:145 36., 'innâ' 6:146 27.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:145 ★★ (kaynak n, z=2,82; eşiği geçen öbür ölçüler pas z=2,12); 6:146 ★★★ (kaynak hapaks, z=3,28; eşiği geçen öbür ölçüler n z=1,65); 6:147 ★ (kaynak pas, z=1,57)",
 "fâsıla: 6:144 ن → 6:145 م (رحيم) → 6:146 ن (لصدقون) → 6:147 ن (ٱلمجرمين) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:145 2:173 (emsal olarak basıldı), 16:115 (emsal olarak basıldı) ve okunmuş 3 ayet; 6:146 xref yok; 6:147 12:110 (emsal olarak basıldı)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:145 'mâ evhâ ilâ' süzgeç GEÇMEZ, 'en kâne meyte' süzgeç GEÇMEZ; 6:146 ve 6:147 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; edilgen fiil 'naib-i faili'): "
 "6:145 muhatap 2MS ('qul', 'rabbeke' eki), konuşan 1S ('ecidu', 'ileyye' — söz içi), 3MS ('ûhiye' — söz içi, edilgen, naib-i faili 'mâ' 5. kelime; 'yat'amuhû' — söz içi, gönderge 'tâ'imin' 10. kelime; 'yekûne' ve 'yat'amuhû' eki — söz içi, gönderge 'muharramen' 8. kelime; 'fe-innehû' eki — söz içi, gönderge 'lahme' 20. kelime; 'uhille' — söz içi, edilgen, naib-i faili 'fisqan' 25. kelime; 'bih' eki — söz içi, gönderge 'fisqan' 25. kelime; 'dturra' — edilgen, naib-i faili 'meni' 30. kelime); "
 "6:146 3MP ('hâdû' — gönderge 'llezîne' 2. kelime; ''aleyhim', 'cezeynâhum', 'bi-bağyihim' ekleri — gönderge 'llezîne' 2. kelime), konuşan 1P ('harramnâ', 'harramnâ', 'cezeynâhum', 'innâ'), 3D ('şuhûmehumâ', 'zuhûruhumâ' ekleri — gönderge 'l-baqari', 'l-ğanemi' 9. ve 10. kelime), 3FS ('hamelet' — fiil uyumu, fail 17. kelime), 3MS ('xteleta' — gönderge 'mâ' 21. kelime); "
 "6:147 3MP ('kezzebûke' — tartışmalı, gönderge 6:146 2. kelime), muhatap 2MS ('kezzebûke' eki, 'qul'), muhatap 2MP ('rabbukum' eki — söz içi), 3MS ('yureddu' — söz içi, fiil uyumu, edilgen, naib-i faili 10. kelime; 'be'suhû' eki — söz içi, gönderge 'rabbukum' 4. kelime)",
 "6:145-147 gönderge zinciri: 6:145 'qul' (1. kelime) muhatabı nebi; 6:146 ''ale'llezîne hâdû' konuşan 1P ile yeni hüküm grubu; 6:147 'kezzebûke' 3MP öznesi 6:146 2. kelimedeki topluluğa ya da bölümün muhatap topluluğuna bağlanabilir (okuma; tartışmalı)",
 "edilgen: 6:145 'ûhiye' (6. kelime; naib-i faili 'mâ' 5. kelime), 'uhille' (26. kelime; naib-i faili 'fisqan' 25. kelime), 'dturra' (31. kelime) — ölçüm EDİLGEN 3/7 bu kelimelerden; 6:147 'yureddu' (9. kelime; naib-i faili 10. kelime) — ölçüm EDİLGEN 1/3 bu kelimeden",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:145 'qul' (1.) ardından söz 2-29. kelime — 'bih' (29.) ile kapanır, 'fe-meni' (30.) morph REM ile anlatı; 6:147 'fe-qul' (3.) ardından söz 4-13. kelime — ayet sonuna kadar; 6:146 söz yok — söz fiili yok (okuma); mealde 'De ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 145 147 35' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; REM sapması 6:145 (22. kelime) — 'fe-innehû' söz içinde gerekçe cümlesi, konuşan 1S sürer, söz 29. kelimeye dek sürer; REM sapması 6:147 (8. kelime) — 've lâ' söz içinde istînâf, muhatap 2MP sürer, söz 13. kelimeye dek sürer; "
 "morph 've' konumlarıyla kontrol edildi: 6:145 've lâ' (34.) CONJ; 6:146 've 'ale' (1.), 've mine' (8.), 've'l-ğanemi' (10.) CONJ, 've innâ' (27.) REM; 6:147 've lâ' (8.) REM; "
 "'fe' konumları: 6:145 'fe-innehû' (22.) ve 'fe-meni' (30.) REM, 'fe-inne' (36.) RSLT; 6:147 'fe-in' (1.) REM, 'fe-qul' (3.) RSLT",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:145 ◈B موت ('meyteten' 15. kelime — B4); 6:146 ◈B حمل ('hamelet' 16. kelime — B2; taşıma anlamında, üreme anlamı yok (okuma)); 6:147 ◈K / ◈B tetik yok; 6:145-147 ◈K tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 145 147 35'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:145 (2:173, 16:115); 6:147 (12:110); 6:146 bağ yok; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11); medde sayımının basılmış eşi (yazım farkı ile, D3 dışı): 'say 6:145 1-2 --medde' 5:100",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:145 söz açılır (2. kelime), söz kapanır (29. kelime, ayet içi), şart → cevap (ayet içi; COND 'meni' 30. kelime), şahıs geçişi yok, edim geçişi soru, emir → emir, şart; bölüm açılışı; "
 "6:146 şahıs geçişi 3 → 1, edim geçişi emir, şart → haber; 6:147 şart → cevap (ayet içi; COND 'in' 1. kelime), söz açılır (4. kelime), söz kapanır (13. kelime, ayet içi), muhatap geçişi 2MS → 2MP (ayet içi; bölüm 16 denetimi MUHATAP_A4), şahıs geçişi 1 → 3, edim geçişi haber → emir, şart; "
 "ölçüm iltifât 6:145-147 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:145 'illâ en yekûne meyteten' — istisna ve masdar edatı (morph EXP + SUB); 6:145 'fe-meni'dturra … fe-inne rabbeke' — şart ve cevap bağlacı (morph COND + RSLT); 6:146 'illâ mâ hamelet zuhûruhumâ' — istisna ve ilgi zamiri (morph EXP + REL); "
 "6:146 'innâ le-sâdiqûn' — pekiştirme (morph ACC + EMPH); 6:147 'fe-in kezzebûke fe-qul' — şart ve cevap bağlacı (morph COND + RSLT)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:145 30-35. kelime — 2:173 ve 16:115 ile harekesiz eş (sayım: 'say 6:145 30-35'); 6:145 26-35. kelime — 16:115 ile harekesiz eş (sayım: 'say 6:145 26-35'); "
 "6:147 11-13. kelime — 12:110 ile harekesiz eş (sayım: 'say 6:147 11-13'); 6:145 kök طعم, غير ikilemeleri; 6:146 kök حرم ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 35'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'fe-meni'dturra ğayra bâğin ve lâ 'âdin' 6:145 'Kim saldırmadan ve sınırı aşmadan zorda kalırsa' / 2:173 'Kim saldırmadan ve sınırı aşmadan zorda kalırsa' (emsal metninde) — çakışma değil (bayt eşit); "
 "'fe-meni'dturra ğayra bâğin ve lâ 'âdin' 6:145 'Kim saldırmadan ve sınırı aşmadan zorda kalırsa' / 16:115 'Kim saldırmadan ve sınırı aşmadan zorda kalırsa' (emsal metninde) — çakışma değil (bayt eşit); "
 "'uhille li-ğayri'llâhi bih' 6:145 'Allah'tan başkası adına kesilmiş' / 16:115 'Allah'tan başkası adına kesileni' (emsal metninde) — çakışma — tam okuma sonu (sıfat-fiil / ad çekimi); "
 "''ani'l-qavmi'l-mucrimîn' 6:147 'suçlu kavimden' / 12:110 'Suçlu topluluktan' (emsal metninde) — çakışma — tam okuma sonu ('kavim' / 'topluluk' bağlam karşılığı); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:145 'qul' IMPV — meal 'De'; 'ecidu' IMPF IND ('lâ' ile) — meal 'bulmuyorum'; 'ûhiye' PERF PASS — meal 'vahyedilende'; 'yat'amu' IMPF IND — meal 'yiyeceği'; 'yekûne' IMPF SUBJ ('en' ile) — meal 'olması'; 'uhille' PERF PASS — meal 'kesilmiş'; 'dturra' PERF PASS (şart) — meal 'kalırsa'; "
 "6:146 'hâdû' PERF — meal 'olanlara'; 'harramnâ' PERF — meal 'kıldık'; 'hamelet' PERF — meal 'taşıdığı'; 'xteleta' PERF — meal 'karışan'; 'cezeynâ' PERF — meal 'cezalandırmamızdır'; "
 "6:147 'kezzebû' PERF (şart) — meal 'yalanlarlarsa'; 'qul' IMPV — meal 'de'; 'yureddu' IMPF IND PASS ('lâ' ile) — meal 'çevrilmez'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'ûhiye', 'uhille' PERF PASS 6:145'te sıfat-fiil ('-en', '-miş') ile; 'cezeynâ' PERF 6:146'da ad-fiil ('-mamızdır') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 145 147 35'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:145 tarayıcı adayı (kök لحم, موت; A_şart, D_yeti) çıpa değil — yiyecek hükmü, ölçü / mekanizma yok; 6:146 ve 6:147 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:147 ('rahmetin' / 'be'suhû'); 6:145 ve 6:146 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök حرم 6:145 ('muharramen') ve 6:146 ('harramnâ', 'harramnâ'); kök ربب 6:145 ('rabbeke') ve 6:147 ('rabbukum'); kök رحم 6:145 ('rahîm') ve 6:147 ('rahmetin'); kök بغي 6:145 ('bâğin') ve 6:146 ('bi-bağyihim'); kök قول 6:145 ('qul') ve 6:147 ('fe-qul'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 17-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 35 ve 36; bölüm açılışı bu blokta; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b35/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 145 147 35'; lem_bozuk.py 35 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 145 147 → AYN_SONUC; sunum/bolum4_kurallar.py 145 147 35 → KHATA_HEPSI; sunum/bolum5_kurallar.py 145 147 35 → B5_HEPSI; sunum/bolum6_kurallar.py 145 147 35 → B6_HEPSI; sunum/bolum7_kurallar.py 145 147 35 → B7_HEPSI; sunum/bolum8_kurallar.py 145 147 35 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 145 147 35 → B9_HEPSI; sunum/bolum10_kurallar.py 145 147 35 → B10_HEPSI; sunum/bolum11_kurallar.py 145 147 35 → B11_HEPSI; sunum/bolum12_kurallar.py 145 147 35 → B12_HEPSI; sunum/bolum13_kurallar.py 145 147 35 → B13_HEPSI; sunum/bolum14_kurallar.py 145 147 35 → B14_HEPSI; sunum/bolum15_kurallar.py 145 147 35 → B15_HEPSI; sunum/bolum16_kurallar.py 145 147 35 → B16_HEPSI; sunum/bolum17_kurallar.py 145 147 35 → B17_HEPSI; sunum/bolum18_kurallar.py 145 147 35 → B18_HEPSI; sunum/bolum19_kurallar.py 145 147 35 → B19_HEPSI; sunum/bolum20_kurallar.py 145 147 35 → B20_HEPSI; sunum/bolum21_kurallar.py 145 147 35 → B21_HEPSI; sunum/bolum22_kurallar.py 145 147 35 → B22_HEPSI; sunum/bolum23_kurallar.py 145 147 35 → B23_HEPSI; sunum/bolum24_kurallar.py 145 147 35 → B24_HEPSI; sunum/bolum25_kurallar.py 145 147 35 → B25_HEPSI; sunum/bolum26_kurallar.py 145 147 35 → B26_HEPSI; sunum/bolum27_kurallar.py 145 147 35 → B27_HEPSI; sunum/bolum28_kurallar.py 145 147 35 → B28_HEPSI; sunum/bolum29_kurallar.py 145 147 35 → B29_HEPSI; sunum/bolum30_kurallar.py 145 147 35 → B30_HEPSI; sunum/bolum31_kurallar.py 145 147 35 → B31_HEPSI; sunum/bolum32_kurallar.py 145 147 35 → B32_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 35 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; 6:145 ölçüm xref'teki okunmuş 3 ayet ('ربّ غفور رحيم' kalıbı) emsal alınmadı — geniş esmâ kalıbı; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('mâ', 'evhâ', 'ilâ', 'en', 'kâne', 'meyte', 'uhille' (morph LEM ham biçim), 'ğayr', 'allâh', 'men', 'idturra', 'bâğ', 'lâ', ''âd', 'inne', 'radde', 'be's', ''an', 'qavm', 'mucrim'); joker '_' yalnız lemmasız 'bih' öğesinde ('dizi 6 145 26 35'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (145, 147): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_145_147.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b34k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '145', '147'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '145', '147', '35'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '145', '147', '35'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '145', '147', '35', '--tazelik-yok')}
    for _n in range(7, 33): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '145', '147', '35')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32 = [_R['B%d' % _n].splitlines() for _n in range(6, 33)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
