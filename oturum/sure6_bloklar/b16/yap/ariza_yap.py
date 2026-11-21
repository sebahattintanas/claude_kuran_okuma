# sûre 6 blok 16 (6:68-70) ARIZA oluşturucu — bölüm 8-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b16/olcum.txt'
os.environ['SAY2'] = '/home/claude/b16/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b15.txt', encoding='utf-8').read() + ']')
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
 ("6:69", "'_ hisâb _ şey''", 2, 'say 6:69 5-8', "harekesiz 'min hisâbihim min şey'' (5-8. kelime)", None),
 ("6:70", "'_ dûn allâh'", 4, 'say 6:70 19-21', "harekesiz 'min dûni'llâh' (19-21. kelime)", None),
 ("6:70", "'bi-mâ kâne kefera'", 2, 'say 6:70 43-45', "harekesiz 'bimâ kânû yekfurûn' (43-45. kelime)", ('dizi 6 70 43 45', "mâ kâne kefera", '43-45', "biçim farkı (dizi 6 70 43 45): 6:30 fiil çekimi, zamir eki")),
 ("6:70", "'veliyy _ şefî''", 2, 'say 6:70 22-24', "harekesiz 'veliyyun ve lâ şefî'' (22-24. kelime)", None),
 ("6:70", "'ğarra hayât dunyâ'", 2, 'say 6:70 7-9', "harekesiz 'ğarrathumu'l-hayâtu'd-dunyâ' (7-9. kelime)", None),
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

VF_YAZI = {68: {1: "'ve izâ'", 14: "'ve immâ'"}, 69: {1: "'ve mâ'", 9: "'ve lâkin'"}, 70: {1: "'ve zeri'", 6: "'ve lahven'", 7: "'ve ğarrathumu'", 10: "'ve zekkir'", 23: "'ve lâ'", 25: "'ve in'", 41: "'ve 'azâbun'"}}
sys.path.insert(0, '/home/claude/b16/yap')
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
open('/home/claude/b16/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '16')
BLOKLAR = [str(i) for i in range(1, 17)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '16', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b16/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '68', '70', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b16/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b16/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '68', '70', '16').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_68_70.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:68', '6:69', '6:70'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_68_70.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(68, 71))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:68 'izâ' (1. kelime — morph T, zaman); 6:68 kök عرض ('fe-a'rid' 7. kelime — yüz çevirme), kök بعد ('ba'de' 19. kelime — ard); 6:70 kök دنو ('d-dunyâ' 9. kelime — dünya), kök نفس ('nefsun' 14. kelime — can), kök ولي ('veliyyun' 22. kelime — dost), kök شرب ('şarâbun' 38. kelime — içme), kök حمم ('hamîmin' 40. kelime — kaynar su): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '68', '70', '16')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b16/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 17)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(68, 71))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: araç değişmedi ise yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 195",
 "kök tablosu: ölçümde '???' 6:70 13. ve 34. kelime için 1 — yeni kök بسل ('helâke teslim etme, rehin bırakma (ibsâl)'; yamalar/yama_kok_6_70.py → kok_ekle_6.ISTEK; kok_turkce 1625); ölçüm yeniden alındı, '???' 0; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 68 70 16'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:62 'ile'llâhi mevlâhumu'l-haqq' (3-6. kelime; blok 15) — kapalı listede kural yoktu, e_el=? 1 idi; kullanıcı kararı: 'ilahi değil' — esma_el 'degil' bu blokta eklendi (yamalar/esma_el_6_68_70.txt), e_el=? 0; "
 "6:70 'min dûni'llâhi veliyyun' (19-22. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge); 6:68 ve 6:69 esmâ yok; "
 "lafız 6:70; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 68 70 16'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:68 '{{1|fâsıla ٱلظلمين → ن, N sınıfı}}', '{{1|simetri \\[6, 3, 9, 2\\]}}', '{{1|harf 104 → harf3 101, isaret 3}}', '{{1|dış düğüm 1}}' ve '{{1|biçim NEHY}}'; "
 "6:69 '{{2|fâsıla يتقون → ن, N sınıfı}}', '{{2|simetri \\[4, 1, 9, 1\\]}}', '{{2|harf 48 → harf3 47, isaret 1}}' ve '{{2|dış düğüm 0}}'; "
 "6:70 '{{3|fâsıla يكفرون → ن, N sınıfı}}', '{{3|simetri \\[6, 11, 31, 2\\]}}', '{{3|harf 193 → harf3 175, isaret 18}}', '{{3|dış düğüm 3}}', '{{3|EDİLGEN 3/13 fiil, pas z=0,99}}', '{{3|HAPAKS: بسل}}' ve '{{3|hapaks z=3,28}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 68 70 16'): KALAN_P",
 "ölçüm aktör: 6:68 '{{1|aktör: adlı شَيْطان 16\\. sırada \\(gayb, rol fail\\)}}'; 6:69 ve 6:70 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:68 emir, yasak, şart — COND 1 've immâ' (14.), EMPH 1 'yunsiyenneke' (15.), IMPV 1 'fe-a'rid' (7.), PRO 1 'fe-lâ' (17.); "
 "6:69 haber — NEG 1 've mâ' (1.); 6:70 emir, şart — COND 1 've in' (25.), IMPV 2 've zeri' (1.), 've zekkir' (10.), NEG 2 've lâ' (23.), 'lâ' (29.); "
 "morph T ('izâ' 6:68 1.), RSLT ('fe' 6:68 7., 17.), SUP ('mâ' 6:68 14.), AMD ('lâkin' 6:69 9.), ACC ('le'alle' 6:69 11.), SUB ('en' 6:70 12.), DEM ('ulâ'i' 6:70 32.), REM ('ve' 6:68 1.; 6:69 1., 9.; 6:70 1., 25.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:70 ★★★ (kaynak n, z=3,46; eşiği geçen öbür ölçüler hapaks z=3,28); 6:68 ve 6:69 yıldız yok",
 "fâsıla: 6:67 ن → 6:68 ن (ٱلظلمين) → 6:69 ن (يتقون) → 6:70 ن (يكفرون) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:68 4:140 (emsal olarak basıldı); 6:70 10:4 (emsal olarak basıldı) ve okunmuş 2 ayet; 6:69 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:69 '_ hisâb _ şey'' süzgeç GEÇER; 6:70 '_ dûn allâh' süzgeç GEÇER, 'bi-mâ kâne kefera', 'veliyy _ şefî'' ve 'ğarra hayât dunyâ' GEÇMEZ; 6:68 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; edilgen fiilde naib-i fail — sûre 6 bölüm 2 denetimi kuralı 5; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:68 muhatap 2MS, 3MP (adsız — gönderge 'llezîne' 3. kelime), konuşan 1P, 3MS ('ğayrih' — gönderge 'hadîsin' 12. kelime; 'yunsiyenneke' 15. kelime — fail 16. kelime); "
 "6:69 3MP (adsız — gönderge 'llezîne' 3. kelime; 'hisâbihim', 'le'allehum', 'yetteqûn' — gönderge 6:68 3. kelime); "
 "6:70 muhatap 2MS, 3MP (adsız — gönderge 'llezîne' 2. kelime ve 'ulâ'ike' 32. kelime; 'ubsilû' edilgen — naib-i faili zamir), 3FS ('ve ğarrathumu' 7. kelime — fail 8. kelime, nesne zamiri 3MP 'llezîne' 2. kelimeye döner; 'tubsele' edilgen — naib-i faili 14. kelime; zamirler adsız — gönderge 'nefsun' 14. kelime), "
 "3MS ('bih' — gönderge 6:69 10. kelime; 'leyse' 17. kelime — fail 22. kelime; 'yu'xaz' edilgen — naib-i faili zamir) — betik denetimi: KHATA_ADSIZ; "
 "ileri / tartışmalı gönderge (bekleyen_ariza_6_b15 elle önerisi (10)): 6:68 'ğayrih' 3MS — 'hadîsin' (12. kelime) yakın erkek ad, anlamca 'âyetler hakkındaki söz'den başka söz (okuma); "
 "6:69 'hisâbihim' — 6:68 dalanlar (sakınanlar değil; 'hesap' dalanların hesabı) (okuma); 6:69 'le'allehum yetteqûn' — 6:68 dalanlara (hatırlatma onlara) (okuma); "
 "6:70 'bih' — ayet içinde önce erkek ad yok; 6:69 'zikrâ' (10. kelime) masdar, zamir eril — tartışmalı gönderge (hatırlatma ya da okunan söz — okuma, tam okuma sonu)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:68-70 söz yok; mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 68 70 16' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:68 've izâ' (1.) REM, 've immâ' (14.) CONJ; 6:69 've mâ' (1.), 've lâkin' (9.) REM; "
 "6:70 've zeri' (1.) REM, 've lahven' (6.), 've ğarrathumu' (7.), 've zekkir' (10.), 've lâ' (23.) CONJ, 've in' (25.) REM, 've 'azâbun' (41.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:70 ◈B حيي ('l-hayâtu' 8. kelime — B4; anlam notu: aldatan dünya hayatı, dirim verilişi yok)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 68 70 16'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:68 (4:140); 6:70 (10:4); 6:69 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş (6:69 '_ hisâb _ şey'' — 6:52; 6:70 'veliyy _ şefî'' — 6:51), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:68 şart → cevap ('izâ' 1. kelime / 'fe-a'rid' 7. kelime; 'in' 14. kelime / 'fe-lâ taq'ud' 17. kelime), şahıs geçişi yok, edim geçişi haber → emir, yasak, şart, bölüm açılışı; "
 "6:69 şahıs geçişi 2 → 3, edim geçişi emir, yasak, şart → haber; 6:70 şart → cevap ('in' 25. kelime / 'lâ yu'xaz' 29. kelime), şahıs geçişi yok, edim geçişi haber → emir, şart; "
 "şahıs beraberliği 6:68 (kişi toplamı 3. şahıs 7 / 2. şahıs 5, ölçüm baskın 2 — bölüm 23 denetimi kuralı 3, sûre 6 bölüm 1 denetimi kuralı 9); ölçüm iltifât 6:68-70 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:68 've izâ re'eyte' — zaman şartı (morph REM + T), cevap 'fe-a'rid' (morph RSLT); 've immâ yunsiyenneke' — 'mâ' zâidli şart (morph CONJ + COND + SUP), tekit nûnu (morph EMPH); 'fe-lâ taq'ud' — yasak (morph PRO); "
 "6:69 've mâ' — olumsuz isim cümlesi (morph REM + NEG); 've lâkin zikrâ' — istidrak (morph REM + AMD), mübteda takdiri; 6:70 'en tubsele' — masdar cümleciği, kerâhet takdiri (morph SUB); 'leyse lehâ' — nefy fiili; 've in ta'dil' — şart (morph REM + COND); 'ulâ'ike'llezîne' — işaret (morph DEM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:68 'hattâ yaxûdû fî hadîsin ğayrih' — 4:140 ile eş (sayım: 'say 6:68 9-13'); "
 "6:68 kök خوض ikilemesi; 6:69 'min hisâbihim min şey'' — 6:52 ile sûre içi eş (sayım: 'say 6:69 5-8'); 6:69 kök وقي ikilemesi; 6:70 'şarâbun min hamîmin ve 'azâbun alîmun bimâ kânû yekfurûn' — 10:4 ile eş (sayım: 'say 6:70 38-45'); "
 "6:70 'veliyyun ve lâ şefî'' — 6:51 ile sûre içi eş (sayım: 'say 6:70 22-24'); 6:70 kök أخذ, بسل, عدل, كسب ikilemeleri; 6:68 'z-zikrâ' / 6:69 'zikrâ' / 6:70 've zekkir' — kök ذكر 6:68, 6:69 ve 6:70'te",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 16'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'hattâ yaxûdû fî hadîsin ğayrih' 6:68 'başka bir söze dalıncaya kadar' / 4:140 'başka bir söze dalıncaya kadar' (emsal metninde) — çakışma değil; "
 "'şarâbun min hamîmin ve 'azâbun alîm' 6:70 'kaynar sudan bir içecek ve acıklı bir azap' / 10:4 'kaynar sudan bir içecek ve acıklı bir azap' (emsal metninde) — çakışma değil; 'bimâ kânû yekfurûn' 6:70 'inkâr etmekte oldukları yüzünden' / 10:4 'inkârları yüzünden' (emsal metninde) — çakışma — tam okuma sonu ('inkâr etmekte oldukları' / 'inkârları' — fiil / masdar çevirisi); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:68 're'eyte' PERF (zaman şartı) — meal 'gördüğün'; 'yaxûdûne' IMPF IND — meal 'dalanları'; 'fe-a'rid' IMPV — meal 'yüz çevir'; "
 "'yaxûdû' IMPF SUBJ — meal 'dalıncaya'; 'yunsiyenneke' IMPF IND (tekitli, şart) — meal 'unutturursa'; 'fe-lâ taq'ud' IMPF JUS (yasak) — meal 'oturma'; "
 "6:69 'yetteqûne' IMPF IND — meal 'Sakınanların'; 'yetteqûn' IMPF IND — meal 'sakınırlar'; "
 "6:70 've zeri' IMPV — meal 'bırak'; 'ttexazû' PERF — meal 'edinenleri'; 've ğarrathumu' PERF — meal 'aldattıklarını'; 've zekkir' IMPV — meal 'hatırlat'; 'tubsele' IMPF SUBJ edilgen — meal 'teslim edilmesin'; 'kesebet' PERF — meal 'kazandığı'; "
 "'leyse' PERF (nefy) — meal 'yoktur'; 'ta'dil' IMPF JUS (şart) — meal 'ödese'; 'yu'xaz' IMPF JUS edilgen — meal 'alınmaz'; 'ubsilû' PERF edilgen — meal 'edilenlerdir'; 'kesebû' PERF — meal 'kazandıkları'; 'kânû' PERF + 'yekfurûn' IMPF IND — meal 'inkâr etmekte oldukları'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 68 70 16'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:68, 6:69 ve 6:70 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:68 ('yunsiyenneke' / 'z-zikrâ'); 6:70 ('la'iben ve lahven' / 'dînehum'; 'şarâbun min hamîm' / ''azâbun alîm'); 6:69 karşıt çift yok; "
 "ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök ذكر 6:68 ('z-zikrâ'), 6:69 ('zikrâ') ve 6:70 ('ve zekkir'); kök خوض 6:68 ('yaxûdûne', 'yaxûdû'); kök كسب 6:70 ('kesebet', 'kesebû'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 8-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 16 ve 17; bu blok bölümü açıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b16/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 68 70 16'; lem_bozuk.py 16 çıktısı): lem_bozuk bayrağı 6:68 4. ve 10. kelime (خاضُ — 'yaxûdûne', 'yaxûdû'), 6:70 1. kelime (يَذَرَ — 've zeri'), 10. kelime (ذُكِّرَ — 've zekkir') ve 13. ve 34. kelime (أُبْسِلُ — 'tubsele', 'ubsilû'), meal kayıtlarında '(morph LEM ham biçim)' notu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 68 70 → AYN_SONUC; sunum/bolum4_kurallar.py 68 70 16 → KHATA_HEPSI; sunum/bolum5_kurallar.py 68 70 16 → B5_HEPSI; sunum/bolum6_kurallar.py 68 70 16 → B6_HEPSI; sunum/bolum7_kurallar.py 68 70 16 → B7_HEPSI; sunum/bolum8_kurallar.py 68 70 16 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 68 70 16 → B9_HEPSI; sunum/bolum10_kurallar.py 68 70 16 → B10_HEPSI; sunum/bolum11_kurallar.py 68 70 16 → B11_HEPSI; sunum/bolum12_kurallar.py 68 70 16 → B12_HEPSI; sunum/bolum13_kurallar.py 68 70 16 → B13_HEPSI; sunum/bolum14_kurallar.py 68 70 16 → B14_HEPSI; sunum/bolum15_kurallar.py 68 70 16 → B15_HEPSI; sunum/bolum16_kurallar.py 68 70 16 → B16_HEPSI; sunum/bolum17_kurallar.py 68 70 16 → B17_HEPSI; sunum/bolum18_kurallar.py 68 70 16 → B18_HEPSI; sunum/bolum19_kurallar.py 68 70 16 → B19_HEPSI; sunum/bolum20_kurallar.py 68 70 16 → B20_HEPSI; sunum/bolum21_kurallar.py 68 70 16 → B21_HEPSI; sunum/bolum22_kurallar.py 68 70 16 → B22_HEPSI; sunum/bolum23_kurallar.py 68 70 16 → B23_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 16 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('min', 'hisâb', 'şey'', 'mâ', 'şarâb', 'hamîm', ''azâb', 'alîm', 'dûn', 'allâh', 'kâne', 'kefera', 'veliyy', 'şefî'', 'ğarra', 'hayât', 'dunyâ'); joker '_' yalnız nakarat3 lemmasız öğede; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (68, 70): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_68_70.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b15k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '68', '70'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '68', '70', '16'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '68', '70', '16'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '68', '70', '16', '--tazelik-yok')}
    for _n in range(7, 24): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '68', '70', '16')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
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
