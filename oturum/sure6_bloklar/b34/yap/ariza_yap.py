# sûre 6 blok 34 (6:142-144) ARIZA oluşturucu — bölüm 16-3
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b34/olcum.txt'
os.environ['SAY2'] = '/home/claude/b34/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Ekinlerde ve hayvanlarda pay; sekiz eş'"


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
 ("6:143", "'isneyn qâle zeker harrame em unseyeyn emmâ iştemelet 'alâ erhâm unseyeyn'", 2, 'say 6:143 8-18', "harekesiz 'sneyn, qul e-'z-zekereyni harrame emi'l-unseyeyni emmâ'ştemelet 'aleyhi erhâmu'l-unseyeyn' (8-18. kelime)", None),
 ("6:143", "'in kâne sâdiq'", 2, 'say 6:143 21-23', "harekesiz 'in kuntum sâdiqîn' (21-23. kelime)", None),
 ("6:144", "'isneyn qâle zeker harrame em unseyeyn emmâ iştemelet 'alâ erhâm unseyeyn'", 2, 'say 6:144 6-16', "harekesiz 'sneyn, qul e-'z-zekereyni harrame emi'l-unseyeyni emmâ'ştemelet 'aleyhi erhâmu'l-unseyeyn' (6-16. kelime)", None),
 ("6:144", "'ezlem mimmen iftarâ 'alâ allâh kezib'", 3, 'say 6:144 25-30', "harekesiz 'ezlemu mimmeni'fterâ 'alâ'llâhi keziben' (25-30. kelime)", None),
 ("6:144", "'ğayr 'ilm inne'", 2, 'say 6:144 33-35', "harekesiz 'bi-ğayri 'ilm, inne' (33-35. kelime)", None),
 ("6:144", "'fe-men ezlem mimmen'", 2, 'say 6:144 24-26', "harekesiz 'fe-men ezlemu mimmeni' (24-26. kelime)", None),
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

VF_YAZI = {142: {1: "'ve mine'", 4: "'ve ferşâ'", 9: "'ve lâ'"}, 143: {6: "'ve mine'"}, 144: {1: "'ve mine'", 4: "'ve mine'"}}
sys.path.insert(0, '/home/claude/b34/yap')
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
open('/home/claude/b34/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '34')
BLOKLAR = [str(i) for i in range(1, 35)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '34', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b34/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '142', '144', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b34/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b34/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '142', '144', '34').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_142_144.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:142', '6:143', '6:144'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_142_144.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(142, 145))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:142 kök شطن ('ş-şeytân' 12. kelime — şeytan); 6:143 kök ضأن ('d-da'ni' 4. kelime — koyun), kök معز ('l-ma'zi' 7. kelime — keçi), kök رحم ('erhâmu' 17. kelime — rahim, organ); 6:144 kök أبل ('l-ibili' 2. kelime — deve), kök بقر ('l-baqari' 5. kelime — sığır), kök رحم ('erhâmu' 15. kelime — rahim, organ), 'iz' (20. kelime — zaman zarfı, morph T, kök yok): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '142', '144', '34')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b34/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 35)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(142, 145))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 15 kapanışında sunum/bolum31_kurallar.py eklendi (kural 1-5), sunum/bolum19_kurallar.py KURAL_ATIF bölüm 15, sunum/geriye_donuk.py bolum31 satırı, sunum/mutasyon_sina.py b31 sınamaları; bu blokta araç değişikliği yok; yeni kök: yamalar/yama_kok_6_142.py (ضأن, معز) → kok_ekle_6.py, ölçüm yeniden koşuldu; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 311",
 "geriye dönük koşu (bölüm 15 kapanışı, komut 'python3 sunum/geriye_donuk.py b31k yamalar/geriye_donuk_6_b28k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 142 144 34'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "kök tablosu: 6:143 ضأن (koyun (da'n)) ve معز (keçi (ma'z)) yeni kök — yamalar/yama_kok_6_142.py; ölçüm HAPAKS alanı yeni karşılıklarla yeniden koşuldu; kok_envanteri ضأن 1 ayet, معز 1 ayet",
 "esmâ: 6:142 ''aduvvun mubîn' (15-16. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (düşmanın sıfatı) (yamalar/esma_el_6_142_144.txt); 6:144 'em kuntum şuhedâ'e' (17-19. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (muhatap topluluk); شَهِيد lemmasında 6:144:19 'degil' kaydıyla 6:19:8 'ilahi' kaydı (lafzın haberi) ayrık — esmâ dışı gönderge / çerçeve ayrılığı; "
 "مُبِين lemmasında sûre 6'daki önceki 'degil' kayıtlarıyla karar eş; 6:143 esmâ yok; 6:142 lafız (8. kelime), 6:144 lafız (22., 29. ve 36. kelime); 6:143 lafız yok; blokta Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 142 144 34'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 6:142 esma_kayit 'mühür EVET' — ölçüm MÜHÜRSÜZ ile uyuşmuyor, araç tanımı farkı; muhur_el hayır, ölçümle uyuşuyor): " + EMH,
 "ölçüm: 6:142 '{{1|aktör: adlı شَيْطان 12\\. sırada \\(gayb, rol mecrur\\)}}', '{{1|esmâ مُبِين 16\\. sırada, SON konum, MÜHÜRSÜZ}}', '{{1|fâsıla مبين → ن, N sınıfı}}', '{{1|harf 76 → harf3 67, isaret 9}}' ve '{{1|dış düğüm 5}}'; "
 "6:143 '{{2|fâsıla صدقين → ن, N sınıfı}}', '{{2|simetri \\[3, 3, 6, 1\\]}}', '{{2|harf 108 → harf3 104, isaret 4}}' ve '{{2|dış düğüm 1}}'; "
 "6:144 '{{3|esmâ شَهِيد 19\\. sırada, ORTA konum, MÜHÜRSÜZ}}', '{{3|fâsıla ٱلظلمين → ن, N sınıfı}}', '{{3|simetri \\[3, 1, 4, 1\\]}}', '{{3|harf 172 → harf3 167, isaret 5}}' ve '{{3|dış düğüm 0}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 142 144 34'): KALAN_P",
 "ölçüm aktör: 6:142 adlı شَيْطان 12. sırada ('ş-şeytân'; gayb, rol mecrur); 6:143 ve 6:144 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:142 emir, yasak — IMPV 1 'kulû' (5.), PRO 1 'lâ' (9.); ölçüm biçim NEHY (D2'de yazılmadı); "
 "6:143 soru, emir, şart — COND 1 'in' (21.), IMPV 2 'qul' (9.), 'nebbi'ûnî' (19.), INTG 1 'e-'z-zekereyni' (10.); 6:144 soru, emir — IMPV 1 'qul' (7.), INTG 2 'e-'z-zekereyni' (8.), 'men' (24.), NEG 1 'lâ' (37.); ölçüm biçim DIKKAT (D2'de yazılmadı); "
 "morph REM ('fe-men' 6:144 24.), PRP ('li-yudille' 6:144 31.), ACC ('innehû' 6:142 13., 'inne'llâhe' 6:144 35.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:143 ★★★ (kaynak hapaks, z=6,79); 6:144 ★★ (kaynak n, z=2,93); 6:142 yıldız yok",
 "fâsıla: 6:141 ن → 6:142 ن (مبين) → 6:143 ن (صدقين) → 6:144 ن (ٱلظلمين) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:142 2:168 (emsal olarak basıldı), 2:208 (emsal olarak basıldı), 24:21 (emsal olarak basıldı), 5:88 (basılmış), 16:114 (basılmış); 6:143 okunmuş 1 ayet; 6:144 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:143 'isneyn qâle zeker harrame em unseyeyn emmâ iştemelet 'alâ erhâm unseyeyn' süzgeç GEÇER, 'in kâne sâdiq' süzgeç GEÇMEZ; 6:144 'isneyn qâle zeker harrame em unseyeyn emmâ iştemelet 'alâ erhâm unseyeyn' süzgeç GEÇER, 'ezlem mimmen iftarâ 'alâ allâh kezib' süzgeç GEÇER, 'ğayr 'ilm inne' süzgeç GEÇMEZ, 'fe-men ezlem mimmen' süzgeç GEÇMEZ; 6:142 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8): "
 "6:142 muhatap 2MP ('kulû', 'razaqakumu', 'tettebi'û', 'lekum'), 3MS ('razaqakumu' — fiil uyumu, fail 8. kelime; 'innehû' eki — gönderge 'ş-şeytân' 12. kelime), aktör adlı 'ş-şeytân' (ölçüm); "
 "6:143 muhatap 2MS ('qul'), 3MS ('harrame' — söz içi, tartışmalı, gönderge 6:142 8. kelime; ''aleyhi' — söz içi, gönderge 'emmâ' 14. kelime), 3FS ('ştemelet' — söz içi, fiil uyumu, fail 17. kelime), muhatap 2MP ('nebbi'ûnî', 'kuntum' — söz içi), konuşan 1S ('nebbi'ûnî' — söz içi); "
 "6:144 muhatap 2MS ('qul'), 3MS ('harrame' — söz içi, tartışmalı, gönderge 6:142 8. kelime; ''aleyhi' — söz içi, gönderge 'emmâ' 12. kelime; 'vassâkumu' — söz içi, fiil uyumu, fail 22. kelime; 'fterâ', 'li-yudille' — gönderge 'mimmeni' 26. kelime; 'yehdi' — gönderge 'llâhe' 36. kelime), 3FS ('ştemelet' — söz içi, fiil uyumu, fail 15. kelime), muhatap 2MP ('kuntum', 'vassâkumu' — söz içi)",
 "6:142-144 gönderge zinciri: 6:142 1-4. kelime 6:141 3. kelimedeki fiile bağlı nesne atfı; 6:143 'semâniyete ezvâc' 6:142 'hamûleten ve ferşâ' bedeli; 6:144 1-6. kelime 6:143 sayımının devamı (okuma)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:143 'qul' (9.) ardından söz 10-23. kelime — ayet sonuna kadar; 6:144 'qul' (7.) ardından söz 8-23. kelime — 'bi-hâzâ' (23.) ile kapanır, 'fe-men' (24.) morph REM ile anlatı; 6:142 söz yok — söz fiili yok (okuma); mealde 'De ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 142 144 34' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:142 've mine' (1.), 've ferşâ' (4.), 've lâ' (9.) CONJ; 6:143 've mine' (6.) CONJ; 6:144 've mine' (1.), 've mine' (4.) CONJ; 'fe' konumları: 6:144 'fe-men' (24.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:142 ◈B نعم ('l-en'âmi' 2. kelime — B1); 6:142 ◈B حمل ('hamûleten' 3. kelime — B2; yük taşıyan anlamında, üreme anlamı yok (okuma)); 6:143 ◈B زوج ('ezvâc' 2. kelime — B2); 6:143 ◈B أنث ('l-unseyeyni' 13. kelime — B2); 6:143 ◈B أنث ('l-unseyeyn' 18. kelime — B2); "
 "6:144 ◈B أنس ('n-nâse' 32. kelime — B1); 6:144 ◈B أنث ('l-unseyeyni' 11. kelime — B2); 6:144 ◈B أنث ('l-unseyeyn' 16. kelime — B2); 6:142-144 ◈K tetik yok; tetik listesinde olmayan organ adı 'erhâmu' (6:143 17., 6:144 15. kelime — rahim)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 142 144 34'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:142 (2:168, 2:208, 24:21); 6:143 ve 6:144 bağ yok; ayetler arası kalıp 'qul e-'z-zekereyni harrame emi'l-unseyeyni emmâ'ştemelet 'aleyhi erhâmu'l-unseyeyn' (6:143, 6:144) — sayım 'dizi 6 143 8 18', 'dizi 6 144 6 16'; blok içi tekrar (bölüm 9 kuralı 6), ardışık bağ yerine sayımla kayıt; ◈D D3 satırına yazılmadı (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:142 şahıs geçişi 3 → 2, edim geçişi yok; 6:143 söz açılır (10. kelime), söz kapanır (23. kelime, ayet içi), şart → cevap (ayet içi; COND 'in' 21. kelime), şahıs geçişi yok, edim geçişi emir, yasak → soru, emir, şart; "
 "6:144 söz açılır (8. kelime), söz kapanır (23. kelime, ayet içi), şahıs geçişi 2 → 3, edim geçişi soru, emir, şart → soru, emir; bölüm kapanışı; "
 "ölçüm iltifât 6:142-144 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:142 've mine'l-en'âmi hamûleten' — takdir edilen inşâ fiiline bağlı nesne atfı (morph CONJ); 6:143 'semâniyete ezvâc' — bedel (okuma); 6:143 'e-'z-zekereyni harrame emi'l-unseyeyni' — soru hemzesi ve 'em' ile denk seçenek (morph INTG + CONJ); "
 "6:144 'men ezlemu mimmeni'fterâ' — soru ve ism-i tafdîl (morph INTG); 6:144 'li-yudille'n-nâse' — amaç (morph PRP)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:142 9-16. kelime — 2:168 ve 2:208 ile harekesiz eş (sayım: 'say 6:142 9-16'); 6:142 10-12. kelime — 24:21 ile harekesiz eş (sayım: 'say 6:142 10-12'); "
 "6:143 8-18. kelime ile 6:144 6-16. kelime harekesiz eş (sayım: 'say 6:143 8-18'); 6:143 kök أنث, ثني ikilemeleri; 6:144 kök أله, أنث, ثني, ظلم ikilemeleri",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 34'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'ve lâ tettebi'û xutuvâti'ş-şeytân, innehû lekum 'aduvvun mubîn' 6:142 'şeytanın adımlarına uymayın. Şüphesiz o sizin için apaçık bir düşmandır' / 2:168 'şeytanın adımlarına uymayın. Şüphesiz o sizin için apaçık bir düşmandır' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve lâ tettebi'û xutuvâti'ş-şeytân, innehû lekum 'aduvvun mubîn' 6:142 'şeytanın adımlarına uymayın. Şüphesiz o sizin için apaçık bir düşmandır' / 2:208 'şeytanın adımlarına uymayın. Şüphesiz o sizin için apaçık bir düşmandır' (emsal metninde) — çakışma değil (bayt eşit); "
 "'tettebi'û xutuvâti'ş-şeytân' 6:142 'şeytanın adımlarına uymayın' / 24:21 'şeytanın adımlarına uymayın' (emsal metninde) — çakışma değil (bayt eşit); 'tettebi'û xutuvâti'ş-şeytân' 6:142 'şeytanın adımlarına uymayın' / 2:168 'şeytanın adımlarına uymayın' (emsal metninde) — çakışma değil (bayt eşit); 'tettebi'û xutuvâti'ş-şeytân' 6:142 'şeytanın adımlarına uymayın' / 2:208 'şeytanın adımlarına uymayın' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:142 'kulû' IMPV — meal 'yiyin'; 'razaqa' PERF — meal 'verdiğinden'; 'tettebi'û' IMPF JUS ('lâ' ile) — meal 'uymayın'; "
 "6:143 'qul' IMPV — meal 'De'; 'harrame' PERF — meal 'kıldı'; 'ştemelet' PERF — meal 'içerdiğini'; 'nebbi'ûnî' IMPV — meal 'haber verin'; 'kuntum' PERF (şart) — meal 'söyleyenlerseniz'; "
 "6:144 'qul' IMPV — meal 'De'; 'harrame' PERF — meal 'kıldı'; 'ştemelet' PERF — meal 'içerdiğini'; 'kuntum' PERF — meal 'miydiniz'; 'vassâ' PERF ('iz' ile) — meal 'tavsiye ettiğinde'; 'fterâ' PERF — meal 'uydurandan'; 'yudille' IMPF SUBJ ('li' ile) — meal 'saptırmak'; 'yehdi' IMPF IND ('lâ' ile) — meal 'iletmez'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'kuntum' PERF 6:143'te şart ('-seniz'), 6:144'te soru ('miydiniz') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 142 144 34'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:142, 6:143 ve 6:144 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:143 ('e-'z-zekereyni' / 'emi'l-unseyeyni'); 6:144 ('e-'z-zekereyni' / 'emi'l-unseyeyni'); 6:142 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök نعم 6:142 ('l-en'âmi') — 6:136, 6:138 ve 6:139 ile bölüm içi; kök زوج 6:143 ('ezvâc') — 6:139 ile bölüm içi; kök ثني 6:143 ('sneyni', 'sneyn') ve 6:144 ('sneyni', 'sneyn'); kök ذكر 6:143 ('e-'z-zekereyni') ve 6:144 ('e-'z-zekereyni'); kök حرم 6:143 ('harrame') ve 6:144 ('harrame'); kök أنث 6:143 ve 6:144; kök رحم 6:143 ('erhâmu') ve 6:144 ('erhâmu'); kök شمل 6:143 ('ştemelet') ve 6:144 ('ştemelet'); kök قول 6:143 ('qul') ve 6:144 ('qul'); kök علم 6:143 ('bi-'ilmin') ve 6:144 (''ilm'); kök كون 6:143 ('kuntum') ve 6:144 ('kuntum'); kök أله 6:142 ('llâhu') ve 6:144 ('llâhu', 'llâhi', 'llâhe'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 16-3 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 32, 33 ve 34; bölüm kapanışı bu blokta; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b34/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 142 144 34'; lem_bozuk.py 34 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 142 144 → AYN_SONUC; sunum/bolum4_kurallar.py 142 144 34 → KHATA_HEPSI; sunum/bolum5_kurallar.py 142 144 34 → B5_HEPSI; sunum/bolum6_kurallar.py 142 144 34 → B6_HEPSI; sunum/bolum7_kurallar.py 142 144 34 → B7_HEPSI; sunum/bolum8_kurallar.py 142 144 34 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 142 144 34 → B9_HEPSI; sunum/bolum10_kurallar.py 142 144 34 → B10_HEPSI; sunum/bolum11_kurallar.py 142 144 34 → B11_HEPSI; sunum/bolum12_kurallar.py 142 144 34 → B12_HEPSI; sunum/bolum13_kurallar.py 142 144 34 → B13_HEPSI; sunum/bolum14_kurallar.py 142 144 34 → B14_HEPSI; sunum/bolum15_kurallar.py 142 144 34 → B15_HEPSI; sunum/bolum16_kurallar.py 142 144 34 → B16_HEPSI; sunum/bolum17_kurallar.py 142 144 34 → B17_HEPSI; sunum/bolum18_kurallar.py 142 144 34 → B18_HEPSI; sunum/bolum19_kurallar.py 142 144 34 → B19_HEPSI; sunum/bolum20_kurallar.py 142 144 34 → B20_HEPSI; sunum/bolum21_kurallar.py 142 144 34 → B21_HEPSI; sunum/bolum22_kurallar.py 142 144 34 → B22_HEPSI; sunum/bolum23_kurallar.py 142 144 34 → B23_HEPSI; sunum/bolum24_kurallar.py 142 144 34 → B24_HEPSI; sunum/bolum25_kurallar.py 142 144 34 → B25_HEPSI; sunum/bolum26_kurallar.py 142 144 34 → B26_HEPSI; sunum/bolum27_kurallar.py 142 144 34 → B27_HEPSI; sunum/bolum28_kurallar.py 142 144 34 → B28_HEPSI; sunum/bolum29_kurallar.py 142 144 34 → B29_HEPSI; sunum/bolum30_kurallar.py 142 144 34 → B30_HEPSI; sunum/bolum31_kurallar.py 142 144 34 → B31_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 34 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; 6:143 xref adayı (okunmuş 1 ayet) yalnız geniş kalıpla ('in kuntum sâdiqîn') bulunduğu için emsal alınmadı; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('fe-men', 'isneyn', 'qâle', 'zeker', 'harrame', 'em', 'unseyeyn', 'emmâ', 'iştemelet' (morph LEM ham biçim), ''alâ', 'erhâm', 'in', 'kâne', 'sâdiq', 'ezlem', 'mimmen', 'iftarâ', 'allâh', 'kezib', 'ğayr', ''ilm', 'inne', 'men', 'lâ', 'ittebe', 'xutuve', 'şeytân', ''aduvv', 'mubîn'); joker '_' yalnız lemmasız 'lekum' öğesinde; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme ve şedde ikilemesi ('emmâ') yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (142, 144): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_142_144.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b31k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '142', '144'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '142', '144', '34'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '142', '144', '34'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '142', '144', '34', '--tazelik-yok')}
    for _n in range(7, 32): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '142', '144', '34')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31 = [_R['B%d' % _n].splitlines() for _n in range(6, 32)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
