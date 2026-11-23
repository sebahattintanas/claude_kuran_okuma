# sûre 6 blok 38 (6:153-157) ARIZA oluşturucu — bölüm 18-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b38/olcum.txt'
os.environ['SAY2'] = '/home/claude/b38/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Gelin okuyayım; dosdoğru yol; Mûsâ'ya Kitap'"


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
 ("6:153", "'zâ vassâ _ le'alle'", 3, 'say 6:153 13-16', "harekesiz 'zâlikum vassâkum bihî le'allekum' (13-16. kelime)", None),
 ("6:155", "'zâ kitâb enzele mubârak'", 2, 'say 6:155 1-4', "harekesiz 've hâzâ kitâbun enzelnâhu mubârakun' (1-4. kelime)", None),
 ("6:157", "''azâb mâ kâne'", 3, 'say 6:157 32-34', "harekesiz 'l-'azâbi bimâ kânû' (32-34. kelime)", ('dizi 6 157 32 34', "'azâb mâ kâne", '32-34', "biçim farkı (dizi 6 157 32 34): 6:30 fiil çekimi, zamir eki; 6:49 yazım eş")),
 ("6:157", "'beyyine min rabb'", 2, 'say 6:157 13-15', "harekesiz 'beyyinetun min rabbikum' (13-15. kelime)", ('dizi 6 157 13 15', "beyyine min rabb", '13-15', "biçim farkı (dizi 6 157 13 15): 6:57 zamir eki")),
 ("6:157", "'fe-men ezlem mimmen'", 2, 'say 6:157 18-20', "harekesiz 'fe-men ezlemu mimmen' (18-20. kelime)", None),
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

VF_YAZI = {153: {1: "'ve enne'", 6: "'ve lâ'"}, 154: {9: "'ve tafsîlen'", 12: "'ve huden'", 13: "'ve rahmeten'"}, 155: {1: "'ve hâzâ'", 6: "'ve'ttaqû'"}, 156: {10: "'ve in'"}, 157: {16: "'ve huden'", 17: "'ve rahmeh'", 24: "'ve sadefe'"}}
sys.path.insert(0, '/home/claude/b38/yap')
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
open('/home/claude/b38/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '38')
BLOKLAR = [str(i) for i in range(1, 39)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '38', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b38/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '153', '157', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b38/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b38/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '153', '157', '38').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_153_157.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:153', '6:154', '6:155', '6:156', '6:157'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_153_157.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(153, 158))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:153 kök سبل ('s-subule' 8. kelime — yol), kök فرق ('teferraqa' 9. kelime — ayırma); 6:154 kök تمم ('temâmen' 5. kelime — tamamlama); 6:156 kök طوف ('tâ'ifeteyni' 7. kelime — topluluk), kök درس ('dirâsetihim' 13. kelime — okuma), kök غفل ('le-ğâfilîn' 14. kelime — gaflet), kök قبل ('qablinâ' 9. kelime — önce); 6:157 kök صدف ('sadefe' 24. kelime — yüz çevirme), kök سوأ ('sû'e' 31. kelime — kötü): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '153', '157', '38')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b38/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 39)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(153, 158))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 17 kapanışında sunum/bolum33_kurallar.py eklendi (kural 1-5), sunum/bolum23_kurallar.py kural 3 yalnız A4'e bakar, satir_aynen araçları BEK satırını süzer, sunum/bolum19_kurallar.py KURAL_ATIF bölüm 17, sunum/geriye_donuk.py bolum33 satırı, sunum/mutasyon_sina.py b33 sınamaları (354 / 354); bu blokta sunum/bolum15_kurallar.py kural 14 düzenli ifadesine sayı sınırı eklendi (uzun konum listesinde geri izleme; işlev eş); yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 336",
 "geriye dönük koşu (bölüm 17 kapanışı, komut 'python3 sunum/geriye_donuk.py b36k yamalar/geriye_donuk_6_b34k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 153 157 38'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:153-157 esmâ yok; esma_el kaydı yok; 6:154 Rab (16. kelime), 6:157 lafız (23. kelime) ve Rab (15. kelime); 6:153, 6:155 ve 6:156 lafız ve Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 153 157 38'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:153 '{{1|fâsıla تتقون → ن, N sınıfı}}', '{{1|simetri \\[3, 1, 10, 1\\]}}', '{{1|harf 80 → harf3 74, isaret 6}}' ve '{{1|dış düğüm 0}}'; "
 "6:154 '{{2|aktör: adlı مُوسَى 3\\. sırada \\(kisi, rol meful\\)}}', '{{2|fâsıla يؤمنون → ن, N sınıfı}}', '{{2|harf 79 → harf3 75, isaret 4}}' ve '{{2|dış düğüm 3}}'; "
 "6:155 '{{3|EDİLGEN 1/4 fiil, pas z=1,10}}', '{{3|fâsıla ترحمون → ن, N sınıfı}}', '{{3|harf 44 → harf3 42, isaret 2}}', '{{3|dış düğüm 1}}' ve '{{3|İÇ düğüm 1}}'; "
 "6:156 '{{4|aktör: adsız `tâife` 7\\. sırada}}', '{{4|EDİLGEN 1/3 fiil, pas z=1,57}}', '{{4|fâsıla لغفلين → ن, N sınıfı}}', '{{4|simetri \\[3, 1, 6, 1\\]}}', '{{4|harf 60 → harf3 59, isaret 1}}' ve '{{4|dış düğüm 0}}'; "
 "6:157 '{{5|EDİLGEN 1/10 fiil, pas z=0,24}}', '{{5|fâsıla يصدفون → ن, N sınıfı}}', '{{5|simetri \\[3, 1, 4, 1\\]}}', '{{5|harf 151 → harf3 143, isaret 8}}' ve '{{5|dış düğüm 6}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 153 157 38'): KALAN_P",
 "ölçüm aktör: 6:154 adlı مُوسَى 3. sırada ('mûse'; kisi, rol meful); 6:156 adsız 'tâ'ifeteyni' 7. sırada; 6:153, 6:155 ve 6:157 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:153 emir, yasak — IMPV 1 'ttebi'û' (5.), PRO 1 'lâ' (6.); ölçüm biçim DIKKAT + NEHY (D2'de yazılmadı); 6:154 haber — kip yok; "
 "6:155 emir — IMPV 2 'ttebi'û' (5.), 'ttaqû' (6.); ölçüm biçim DIKKAT (D2'de yazılmadı); 6:156 şart — COND 1 'in' (10.), EMPH 1 'le-ğâfilîn' (14.); "
 "6:157 soru, şart — CERT 1 'qad' (11.), COND 1 'lev' (3.), EMPH 1 'le-kunnâ' (8.), FUT 1 'se-neczi' (26.), INTG 1 'men' (18.); "
 "morph ACC ('enne' 6:153 1., 'le'allekum' 6:153 16., 'le'allehum' 6:154 14., 'le'allekum' 6:155 7., 'innemâ' 6:156 3., 'ennâ' 6:157 4.), CAUS ('fe'ttebi'ûh' 6:153 5., 'fe-teferraqa' 6:153 9.), REM ('ve hâzâ' 6:155 1., 'fe'ttebi'ûhu' 6:155 5., 'fe-men' 6:157 18.), SUB ('en' 6:156 1.), RSLT ('fe-qad' 6:157 11.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:153, 6:154 ve 6:155 yıldız yok; 6:156 ★ (kaynak pas, z=1,57); 6:157 ★★ (kaynak n, z=2,40)",
 "fâsıla: 6:152 ن → 6:153 ن (تتقون) → 6:154 ن (يؤمنون) → 6:155 ن (ترحمون) → 6:156 ن (لغفلين) → 6:157 ن (يصدفون) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:153 xref yok; 6:154 12:111 (emsal olarak basıldı), 16:89 (emsal olarak basıldı) ve okunmamış 1 ayet; 6:155 6:92 (basılmış), 38:29 (emsal olarak basıldı); 6:156 xref yok; 6:157 40:66 (basılmış), okunmuş 1 ayet ve okunmamış 4 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:153 'zâ vassâ _ le'alle' süzgeç GEÇER; 6:155 'zâ kitâb enzele mubârak' süzgeç GEÇER; 6:157 ''azâb mâ kâne' süzgeç GEÇER, 'beyyine min rabb' süzgeç GEÇMEZ, 'fe-men ezlem mimmen' süzgeç GEÇMEZ; 6:154 ve 6:156 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; edilgen fiil 'naib-i faili'; ekler fiillerden ayrı grupta): "
 "6:153 konuşan 1S eki ('sırâtî' — söz içi), muhatap 2MP ('ttebi'û', 'tettebi'u', 'tettaqûn' — söz içi; ekler 'bikum', 'vassâkum', 'le'allekum'), 3FS ('teferraqa' — gönderge 's-subule' 8. kelime), 3MS ('fe'ttebi'ûh' eki — gönderge 'sırâtî' 3. kelime; 'sebîlih' eki ve 'vassâkum' — gönderge 6:151 6. kelime; 'bihî' eki — gönderge 'zâlikum' 13. kelime); "
 "6:154 konuşan 1P ('âteynâ'), aktör adlı 'mûse', 3MS ('ahsene' — tartışmalı, gönderge 'llezî' 7. kelime), 3MP ('le'allehum', 'rabbihim' ekleri, 'yu'minûn' — tartışmalı); "
 "6:155 konuşan 1P ('enzelnâ'), 3MS eki ('enzelnâhu', 'fe'ttebi'ûhu' — gönderge 'kitâbun' 2. kelime), muhatap 2MP ('ttebi'û', 'ttaqû'; 'le'allekum' eki; 'turhamûn' — edilgen, naib-i faili muhatap); "
 "6:156 muhatap 2MP ('taqûlû'), 3MS ('unzile' — söz içi, edilgen, naib-i faili 5. kelime), konuşan 1P ('kunnâ' — söz içi; 'qablinâ' eki), 3MP eki ('dirâsetihim' — söz içi, cins uyumsuz, gönderge 'tâ'ifeteyni' 7. kelime), aktör adsız 'tâ'ifeteyni'; "
 "6:157 muhatap 2MP ('taqûlû'; 'câ'ekum', 'rabbikum' ekleri), konuşan 1P ('kunnâ' — söz içi; 'ennâ', ''aleyne' ekleri — söz içi; 'neczi'; 'âyâtinâ' eki), 3MS ('unzile' — söz içi, edilgen, naib-i faili 7. kelime; 'câ'ekum' — fiil uyumu, fail 13. kelime; 'kezzebe', 'sadefe' — gönderge 'mimmen' 20. kelime), 3FS eki (''anhâ' — gönderge 'âyâti' 22. kelime), 3MP ('minhum' eki — söz içi, cins uyumsuz, gönderge 6:156 7. kelime; 'yasdifûne', 'kânû', 'yasdifûn' — gönderge 'llezîne' 27. kelime)",
 "6:153-157 gönderge zinciri: 6:153 söz 6:151 2. kelimeden süren tavsiye listesinin sonu; 6:154 konuşan 1P ile anlatı, 3MP göndergesi metinde adsız (tartışmalı); 6:155-157 muhatap 2MP, 6:156-157 'en taqûlû' / 'ev taqûlû' ile gerekçe sözleri (okuma)",
 "edilgen: 6:155 'turhamûn' (8. kelime; naib-i faili muhatap) — ölçüm EDİLGEN 1/4; 6:156 'unzile' (4. kelime; naib-i faili 'l-kitâbu' 5. kelime) — ölçüm EDİLGEN 1/3; 6:157 'unzile' (5. kelime; naib-i faili 'l-kitâbu' 7. kelime) — ölçüm EDİLGEN 1/10",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:153 söz 6:151 2. kelimeden sürer ve 17. kelimede kapanır; 6:154 'summe' (1.) ile anlatı; 6:156 'taqûlû' (2.) ardından söz 3-14. kelime; 6:157 'taqûlû' (2.) ardından söz 3-10. kelime, 'fe-qad' (11.) morph RSLT ile muhatap 2MP'ye dönüş (okuma); mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 153 157 38' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:153 've enne' (1.), 've lâ' (6.) CONJ; 6:154 've tafsîlen' (9.), 've huden' (12.), 've rahmeten' (13.) CONJ; 6:155 've hâzâ' (1.) REM, 've'ttaqû' (6.) CONJ; 6:156 've in' (10.) CONJ; 6:157 've huden' (16.), 've rahmeh' (17.), 've sadefe' (24.) CONJ; "
 "'fe' konumları: 6:153 'fe'ttebi'ûh' (5.), 'fe-teferraqa' (9.) CAUS; 6:155 'fe'ttebi'ûhu' (5.) REM; 6:157 'fe-qad' (11.) RSLT, 'fe-men' (18.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:153-157 ◈K / ◈B tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 153 157 38'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:154 (12:111, 16:89); 6:155 (38:29); 6:153, 6:156 ve 6:157 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 6:153 تبع ×2, سبل ×2; 6:157 أيي ×2, صدف ×3, كون ×2, هدي ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:153 söz kapanır (17. kelime), cevap edatı kapsam dışı (morph CAUS 5. ve 9. kelime), şahıs geçişi yok, edim geçişi emir, yasak, şart → emir, yasak; 6:154 şahıs geçişi 2 → 3, edim geçişi emir, yasak → haber; 6:155 şahıs geçişi 3 → 2, edim geçişi haber → emir; "
 "6:156 söz açılır (3. kelime), söz kapanır (14. kelime, ayet içi), şart → cevap (ayet içi; COND 'in' 10. kelime — cevap hazif), şahıs geçişi 2 → 1, edim geçişi emir → şart; "
 "6:157 söz açılır (3. kelime), söz kapanır (10. kelime, ayet içi), şart → cevap (ayet içi; COND 'lev' 3. kelime), cevap edatı kapsam dışı (morph RSLT 11. kelime), şahıs geçişi 1 → 3, edim geçişi şart → soru, şart; bölüm kapanışı; "
 "ölçüm iltifât 6:153-157 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:153 'fe-teferraqa bikum' — nehyin cevabı, sebebiyye 'fe' (morph CAUS); 6:156 'en taqûlû' — masdar edatı, gerekçe (morph SUB); 6:156 've in kunnâ … le-ğâfilîn' — muhaffefe okuması, cevap mahzuf (6:156 10. kelime) (morph COND + EMPH); "
 "6:157 'lev ennâ unzile … le-kunnâ' — şart ve cevap lâmı (morph COND + EMPH); 6:157 'fe-men ezlemu mimmen' — soru ve ism-i tafdîl (morph INTG)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:154 11-13. kelime — 12:111 ve 16:89 ile harekesiz eş (sayım: 'say 6:154 11-13'); 6:154 10-13. kelime — 16:89 ile harekesiz eş (sayım: 'say 6:154 10-13'); "
 "6:155 2-3. kelime — 38:29 ile harekesiz eş (sayım: 'say 6:155 2-3'); 6:153 kök تبع, سبل ikilemeleri; 6:157 kök أيي, صدف, كون, هدي ikilemeleri",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 38'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'şey'in ve huden ve rahmeten' 6:154 'her şeyi ayrıntılı açıklayan, doğru yol ve rahmet' / 12:111 'her şeyi ayrıntılandıran ve inanan bir topluluk için hidayet ve rahmet' (emsal metninde) — çakışma — tam okuma sonu ('doğru yol' / 'hidayet' bağlam karşılığı); "
 "'li-kulli şey'in ve huden ve rahmeten' 6:154 'her şeyi ayrıntılı açıklayan, doğru yol ve rahmet' / 16:89 'her şeyi açıklayan, müslümanlar için yol gösterici, rahmet' (emsal metninde) — çakışma — tam okuma sonu ('doğru yol' / 'yol gösterici' bağlam karşılığı); "
 "'kitâbun enzelnâhu' 6:155 'indirdiğimiz bereketli bir kitaptır' / 38:29 'indirdiğimiz bereketli bir kitaptır' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:153 'ttebi'û' IMPV — meal 'uyun'; 'tettebi'u' IMPF JUS ('lâ' ile) — meal 'uymayın'; 'teferraqa' IMPF SUBJ ('fe' ile) — meal 'ayırır'; 'vassâ' PERF — meal 'ettiğidir'; 'tettaqûn' IMPF IND — meal 'sakınırsınız'; "
 "6:154 'âteynâ' PERF — meal 'verdik'; 'ahsene' PERF — meal 'davranana'; 'yu'minûn' IMPF IND — meal 'inanırlar'; 6:155 'enzelnâ' PERF — meal 'indirdiğimiz'; 'ttebi'û' IMPV — meal 'uyun'; 'ttaqû' IMPV — meal 'sakının'; 'turhamûn' IMPF PASS IND — meal 'olunursunuz'; "
 "6:156 'taqûlû' IMPF SUBJ ('en' ile) — meal 'demeyesiniz'; 'unzile' PERF PASS — meal 'indirildi'; 'kunnâ' PERF — meal 'gafildik'; "
 "6:157 'taqûlû' IMPF SUBJ ('en' ile) — meal 'demeyesiniz'; 'unzile' PERF PASS ('lev' ile) — meal 'indirilseydi'; 'kunnâ' PERF ('le' ile) — meal 'olurduk'; 'câ'e' PERF ('qad' ile) — meal 'geldi'; 'kezzebe' PERF — meal 'yalanlayan'; 'sadefe' PERF — meal 'çevirenden'; 'neczi' IMPF IND ('se' ile) — meal 'cezalandıracağız'; 'yasdifûne' IMPF IND — meal 'çevirenleri'; 'kânû' PERF — meal 'çevirmelerinden'; 'yasdifûn' IMPF IND — meal 'çevirmelerinden'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'ahsene', 'enzelnâ', 'kezzebe', 'sadefe' PERF 6:154, 6:155 ve 6:157'de sıfat-fiil ('-ana', '-diğimiz', '-yan', '-enden') ile; 'kunnâ' PERF 6:157'de şart cevabı ('-urduk') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'lev' ('-seydi' / '-sa') — çakışma değil (şart kipi, geçmiş / geniş zaman); 'zâ' ('bu' / 'Bu') — çakışma değil (büyük harf, cümle başı)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 153 157 38'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:153-157 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:153 ('sırâtî' / 's-subule'); 6:154-157 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök تبع 6:153 ('ttebi'û', 'tettebi'u') ve 6:155 ('ttebi'û'); kök وقي 6:153 ('tettaqûn') ve 6:155 ('ttaqû'); kök كتب 6:154 ('l-kitâbe'), 6:155 ('kitâbun'), 6:156 ('l-kitâbu') ve 6:157 ('l-kitâbu'); kök نزل 6:155 ('enzelnâhu'), 6:156 ('unzile') ve 6:157 ('unzile'); "
 "kök هدي 6:154 ('huden') ve 6:157 ('ehdâ', 'huden'); kök رحم 6:154 ('rahmeten'), 6:155 ('turhamûn') ve 6:157 ('rahmeh'); kök ربب 6:154 ('rabbihim') ve 6:157 ('rabbikum'); kök قول 6:156 ('taqûlû') ve 6:157 ('taqûlû'); kök كون 6:156 ('kunnâ') ve 6:157 ('le-kunnâ', 'kânû'); kök قبل 6:156 ('qablinâ'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 18-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 37 ve 38; bölüm kapanışı bu blokta; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b38/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 153 157 38'; lem_bozuk.py 38 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 153 157 → AYN_SONUC; sunum/bolum4_kurallar.py 153 157 38 → KHATA_HEPSI; sunum/bolum5_kurallar.py 153 157 38 → B5_HEPSI; sunum/bolum6_kurallar.py 153 157 38 → B6_HEPSI; sunum/bolum7_kurallar.py 153 157 38 → B7_HEPSI; sunum/bolum8_kurallar.py 153 157 38 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 153 157 38 → B9_HEPSI; sunum/bolum10_kurallar.py 153 157 38 → B10_HEPSI; sunum/bolum11_kurallar.py 153 157 38 → B11_HEPSI; sunum/bolum12_kurallar.py 153 157 38 → B12_HEPSI; sunum/bolum13_kurallar.py 153 157 38 → B13_HEPSI; sunum/bolum14_kurallar.py 153 157 38 → B14_HEPSI; sunum/bolum15_kurallar.py 153 157 38 → B15_HEPSI; sunum/bolum16_kurallar.py 153 157 38 → B16_HEPSI; sunum/bolum17_kurallar.py 153 157 38 → B17_HEPSI; sunum/bolum18_kurallar.py 153 157 38 → B18_HEPSI; sunum/bolum19_kurallar.py 153 157 38 → B19_HEPSI; sunum/bolum20_kurallar.py 153 157 38 → B20_HEPSI; sunum/bolum21_kurallar.py 153 157 38 → B21_HEPSI; sunum/bolum22_kurallar.py 153 157 38 → B22_HEPSI; sunum/bolum23_kurallar.py 153 157 38 → B23_HEPSI; sunum/bolum24_kurallar.py 153 157 38 → B24_HEPSI; sunum/bolum25_kurallar.py 153 157 38 → B25_HEPSI; sunum/bolum26_kurallar.py 153 157 38 → B26_HEPSI; sunum/bolum27_kurallar.py 153 157 38 → B27_HEPSI; sunum/bolum28_kurallar.py 153 157 38 → B28_HEPSI; sunum/bolum29_kurallar.py 153 157 38 → B29_HEPSI; sunum/bolum30_kurallar.py 153 157 38 → B30_HEPSI; sunum/bolum31_kurallar.py 153 157 38 → B31_HEPSI; sunum/bolum32_kurallar.py 153 157 38 → B32_HEPSI; sunum/bolum33_kurallar.py 153 157 38 → B33_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 38 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; 6:157 ölçüm xref'teki okunmuş 1 ayet harekesiz sayımla bulunmadı, okunmamış ayetler okunmamış sûrede — emsal alınmadı; 6:92 ve 40:66 önceden basılmış; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('zâ', 'vassâ', 'le'alle', 'tafsîl', 'kull', 'şey'', 'hudâ', 'rahme', 'kitâb', 'enzele', 'mubârak', ''azâb', 'mâ', 'kâne', 'beyyine', 'min', 'rabb', 'fe-men', 'men', 'ezlem', 'mimmen'); joker '_' yalnız lemmasız 'bihî' öğesinde ('dizi 6 153 13 16'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (153, 157): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_153_157.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b36k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '153', '157'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '153', '157', '38'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '153', '157', '38'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '153', '157', '38', '--tazelik-yok')}
    for _n in range(7, 34): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '153', '157', '38')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33 = [_R['B%d' % _n].splitlines() for _n in range(6, 34)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
