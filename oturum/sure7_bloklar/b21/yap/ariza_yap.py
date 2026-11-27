# sûre 7 blok 21 (7:73-75) ARIZA oluşturucu — bölüm 8-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b21/olcum.txt'
os.environ['SAY2'] = '/home/claude/b21/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = list(ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_7_b20.txt', encoding='utf-8').read() + ']'))
VF_YAZI_ESKI = {}
BOL = "'Sâlih ve Semûd; Lût ve kavmi'"


def sd(key):
    return sayim.S2[key][1]


def sic(key):
    n, d = sayim.S2[key]
    return 1 + len([x for x in d['basilan'] if x.startswith('7:')]) + d['okunmus_si'] + d['henuz_si']


def taban(key, ay):
    n, d = sayim.S2[key]
    p = [ay] + [x for x in d['basilan'] if x.startswith('7:') and x != ay]
    if d['okunmus_si']: p.append('okunmus_si %d' % d['okunmus_si'])
    if d['henuz_si']: p.append('henuz_si %d' % d['henuz_si'])
    return ' + '.join(p)


R5 = [
 ('7:73', "'qâle qavm 'abede allâh mâ _ min ilâh ğayr qad câ'e beyyine min rabb'", 2, 'say 7:73 5-18', "harekesiz 'qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû qad câ'etkum beyyinetun min rabbikum' (5-18. kelime)", ('dizi 7 73 5 18', "qâle qavm 'abede allâh mâ _ min ilâh ğayr qad câ'e beyyine min rabb", '5-18', 'biçim farkı (dizi 7 73 5 18): basılmamış eş yazım eş')),
 ('7:73', "'qâle qavm 'abede allâh mâ _ min ilâh ğayr'", 4, 'say 7:73 5-13', "harekesiz 'qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû' (5-13. kelime)", ('dizi 7 73 5 13', "qâle qavm 'abede allâh mâ _ min ilâh ğayr", '5-13', 'biçim farkı (dizi 7 73 5 13): 7:59 önek; 7:65 yazım eş; basılmamış eş yazım eş; öneksiz eş koşusu (dizi 7 73 5 13): 7:59 → önek kesilmiş sûre içi 1; 7:65 → önek kesilmiş sûre içi 4; basılmamış eş → önek kesilmiş sûre içi 4')),
 ('7:73', "'qad câ'e beyyine min rabb'", 3, 'say 7:73 14-18', "harekesiz 'qad câ'etkum beyyinetun min rabbikum' (14-18. kelime)", ('dizi 7 73 14 18', "qad câ'e beyyine min rabb", '14-18', "biçim farkı (dizi 7 73 14 18): basılmamış eş yazım eş; basılmamış eş fiil çekimi, i'râb, zamir eki, önek; öneksiz eş koşusu (dizi 7 73 14 18): basılmamış eş → önek kesilmiş sûre içi 2; basılmamış eş → önek kesilmiş sûre içi 1")),
 ('7:74', "'zekere iz ce'ale xalîfe min ba'd'", 2, 'say 7:74 1-6', "harekesiz 've'zkurû iz ce'alekum xulefâ'e min ba'di' (1-6. kelime)", ('dizi 7 74 1 6', "zekere iz ce'ale xalîfe min ba'd", '1-6', 'biçim farkı (dizi 7 74 1 6): 7:69 yazım eş')),
 ('7:74', "'zekere âlâ' allâh'", 2, 'say 7:74 18-20', "harekesiz 'fe'zkurû âlâ'e'llâhi' (18-20. kelime)", ('dizi 7 74 18 20', "zekere âlâ' allâh", '18-20', 'biçim farkı (dizi 7 74 18 20): 7:69 yazım eş')),
 ('7:75', "'qâle mele' ellezî istekbere min qavm'", 2, 'say 7:75 1-6', "harekesiz 'qâle'l-mele'u'llezîne'stekberû min qavmihî' (1-6. kelime)", ('dizi 7 75 1 6', "qâle mele' ellezî istekbere min qavm", '1-6', 'biçim farkı (dizi 7 75 1 6): basılmamış eş yazım eş')),
 ('7:75', "'qâle mele' ellezî'", 4, 'say 7:75 1-3', "harekesiz 'qâle'l-mele'u'llezîne' (1-3. kelime)", ('dizi 7 75 1 3', "qâle mele' ellezî", '1-3', 'biçim farkı (dizi 7 75 1 3): 7:66 yazım eş; basılmamış eş yazım eş; basılmamış eş önek; öneksiz eş koşusu (dizi 7 75 1 3): 7:66 → önek kesilmiş sûre içi 4; basılmamış eş → önek kesilmiş sûre içi 4; basılmamış eş → önek kesilmiş sûre içi 1')),
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

VF_YAZI = {73: {1: "'ve ilâ'", 6: "'yâ qavmi'", 10: "'lekum'", 22: "'lekum'", 24: "'fe-zerûhâ'", 29: "'ve lâ'", 31: "'bi-sû'in'", 32: "'fe-ye'xuzekum'"}, 74: {1: "'ve'zkurû'", 8: "'ve bevve'ekum'", 15: "'ve tenhitûne'", 18: "'fe'zkurû'", 21: "'ve lâ'"}, 75: {7: "'li'llezîne'", 9: "'li-men'", 12: "'e-ta'lemûne'", 20: "'bi-mâ'", 22: "'bihî'"}}
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
ONC = run('/home/claude/sunum/onceki_basim.py', '73', '75', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b21/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b21/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '73', '75', '21').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_73_75.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:73', '7:74', '7:75'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_73_75.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(73, 76))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:73 kök سوأ ('bi-sû'in' 31. kelime — kötülük): tetik listesinde yok; 7:74 'iz' (2. kelime — morph T, zaman); 7:74 kök بعد ('ba'di' 6. kelime — sonra): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '73', '75', '21')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b21/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 22)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(73, 76))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l.replace('**', '') for l in open('/home/claude/b21/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b21/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))
_AK2 = _esc(re.search(r'aktör: adlı .*?rol mecrur\)', _OL[1]).group(0))
_AK3 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[2]).group(0))
_HP = _esc(re.search(r'HAPAKS: .*? — hapaks z=3,28', _OL[1]).group(0))
for _k, _v in (('_AK1', _AK1), ('_AK2', _AK2), ('_AK3', _AK3), ('_HP', _HP)): _MB = _MB.replace('" + %s + "' % _k, _v)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 72), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; bölüm 7 kapanışında sunum/bolum43_kurallar.py (kural 1-5) eklendi, sunum/geriye_donuk.py ve mutasyon_sina buna göre güncellendi — önceki commit'te, kapanış mutasyon sınaması 455 / 455; yeni kök سهل karşılığı ('düzlük, ova') bu blokta kök tablosuna eklendi (yamalar/yama_kok_7_73.py); mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 486",
 "geriye dönük koşu (sûre 7 bölüm 7 kapanışı, komut 'python3 sunum/geriye_donuk.py b20k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 73 75 21'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:75 'innâ bi-mâ ursile bihî mu'minûn' (19-23. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (iman edenlerin sıfatı) (yamalar/esma_el_7_73_75.txt); 7:73 ve 7:74 esmâ yok; 7:73 lafız (8., 21. ve 28. kelime), 7:74 lafız (20. kelime); 7:75 lafız yok; 7:73 Rab (18. kelime), 7:75 Rab (17. kelime); 7:74 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 73 75 21'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 7:75 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı; muhur_el hayır): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in range(73, 76)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 73 75 21'): KALAN_P",
 "ölçüm aktör: 7:73 adlı ثَمُود (2. kelime, rol mecrur) ve صالِح (4. kelime, rol meful); 7:74 adlı عاد (7. kelime, rol mecrur); 7:75 adlı صالِح (14. kelime, rol meful)",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:73 emir, yasak, nida — CERT 1 'qad' (14.), IMPV 2 'u'budu' (7.), 'fe-zerûhâ' (24.), NEG 1 'mâ' (9.), PRO 1 've lâ' (29.), VOC 1 'yâ qavmi' (6.); "
 "7:74 emir, yasak — IMPV 2 've'zkurû' (1.), 'fe'zkurû' (18.), PRO 1 've lâ' (21.); 7:75 soru — INTG 1 'e-ta'lemûne' (12.)",
 "morph REL ('li'llezîne' 7:75 7., 'li-men' 7:75 9., 'bi-mâ' 7:75 20.), T ('iz' 7:74 2.), CAUS ('fe-ye'xuzekum' 7:73 32.), ATT ('hâzihî' 7:73 19.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:73 ★★ (kaynak n, z=2,29); 7:74 ★★★ (kaynak hapaks, z=3,28 — سهل); 7:75 yıldız yok",
 "fâsıla: 7:72 ن → 7:73 م (" + _F[0] + ") → 7:74 ن (" + _F[1] + ") → 7:75 ن (" + _F[2] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:73 11:64, 26:156 (emsal olarak basıldı), 6:157, 7:59, 7:65, 11:50, 11:61, 11:84, 23:23, 23:32, 40:66 (basılmış), okunmuş 1 ayet ve okunmamış 2 ayet (sûre içi 2); "
 "7:74 2:60, 15:82, 26:149 (emsal olarak basıldı); 7:75 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:73 'qâle qavm 'abede allâh mâ _ min ilâh ğayr qad câ'e beyyine min rabb' süzgeç GEÇER, 'qâle qavm 'abede allâh mâ _ min ilâh ğayr' süzgeç GEÇER, 'qad câ'e beyyine min rabb' süzgeç GEÇER; "
 "7:74 'zekere iz ce'ale xalîfe min ba'd' süzgeç GEÇER, 'zekere âlâ' allâh' süzgeç GEÇMEZ; 7:75 'qâle mele' ellezî istekbere min qavm' süzgeç GEÇER, 'qâle mele' ellezî' süzgeç GEÇER; sûre içi eşler — bölüm 7 bloklarındaki Nûh ve Hûd kıssası ayetleri (basılmış) ve basılmamış eşler",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:73 adlı 'semûde' (2.) ve 'sâlihan' (4.); 3MP eki ('exâhum' — gönderge 'semûde'), 3MS ('qâle' — gönderge 'sâlihan'), söz içi konuşan 1S eki ('qavmi'), söz içi muhatap 2MP ('u'budu', 'zerûhâ', 'temessûhâ'; ekler 'lekum', 'câ'etkum', 'rabbikum', 'lekum', 'ye'xuzekum'), 3FS ('câ'etkum' — fiil uyumu, fail 16. kelime; 'te'kul' ve ekler 'zerûhâ', 'temessûhâ' — gönderge 'nâqatu' 20. kelime), 3MS ('ye'xuzekum' — fiil uyumu, fail 33. kelime; ek 'ğayruhû' — gönderge 'llâhe' 8. kelime); "
 "7:74 adlı ''âdin' (7.); söz içi muhatap 2MP ('zkurû', 'tettexizûne', 'tenhitûne', 'zkurû', 'ta'sev'; ekler 'ce'alekum', 'bevve'ekum'), 3MS ('ce'ale', 'bevve'e' — gönderge 'llâhi' 20. kelime), 3FS eki ('suhûlihâ' — gönderge 'l-ardi' 10. kelime); "
 "7:75 adlı 'sâlihan' (14.); 3MS ('qâle' — fiil uyumu, fail 2. kelime; 'âmene' — gönderge 'men' 9. kelime; 'ursile' — söz içi, edilgen, gönderge 'mâ' 20. kelime; ekler 'qavmihî' — gönderge 7:73 4. kelime, 'rabbihî' — gönderge 'sâlihan' 14. kelime, 'bihî' — gönderge 'mâ' 20. kelime), 3MP ('stekberû' — gönderge 'llezîne' 3. kelime; 'stud'ifû' — edilgen, gönderge 'llezîne' 7. kelime; 'qâlû' — gönderge 'llezîne' 7. kelime; ek 'minhum' — gönderge 'men' 9. kelime), söz içi muhatap 2MP ('ta'lemûne'), söz içi konuşan 1P eki ('innâ')",
 "7:73-75 gönderge zinciri: 7:73 'qâle' göndergesi 'sâlihan' (4. kelime); 7:74 söz 7:73'ten sürüyor, 'ce'ale' ve 'bevve'e' göndergesi 'llâhi' (20. kelime); 7:75 'qavmihî' göndergesi 7:73 4. kelimedeki Sâlih; 'qâlû' göndergesi zayıf sayılanlar ('llezîne' 7. kelime) (okuma)",
 "edilgen: 7:75 'stud'ifû' (8. kelime, X. bab) ve 'ursile' (21. kelime, IV. bab) — ölçüm EDİLGEN 2/7 fiil; 7:73 ve 7:74 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:73 söz içi 6-34. kelime ('qâle' 5. kelime ardından; ayet sonunda kapanmıyor); 7:74 söz sürüyor (7:73 6. kelimeden, 1-25. kelime; 25. kelimede kapanır); "
 "7:75 söz içi 12-17. kelime ('qâle' 1. kelime ve muhatap 'li'llezîne' 7. kelime ardından) ve 19-23. kelime ('qâlû' 18. kelime ardından); "
 "REM sapması 7:73 (24. kelime) — söz içi 'fe', emir cümlesi başı; REM sapması 7:74 (18. kelime) — söz içi 'fe', emir cümlesi başı; 'fe' 18. kelime morph REM — anlamca sonuç ('Öyleyse'); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 73 75 21' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 7:73 've ilâ' (1.) CONJ, 'fe-zerûhâ' (24.) REM, 've lâ' (29.) CONJ, 'fe-ye'xuzekum' (32.) CAUS; 7:74 've'zkurû' (1.) CONJ, 've bevve'ekum' (8.) CONJ, 've tenhitûne' (15.) CONJ, 'fe'zkurû' (18.) REM, 've lâ' (21.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:73 ◈K أرض ('ardi' 27. kelime — K1), 7:74 ◈K أرض ('l-ardi' 10. kelime — K1), 7:74 ◈K جبل ('l-cibâle' 16. kelime — K1), 7:74 ◈K أرض ('l-ardi' 24. kelime — K1); 7:75 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 73 75 21'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:73 (11:64, 26:156), 7:74 (2:60, 15:82, 26:149); D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:73 أله ×4; 7:74 أرض ×2, ذكر ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:73 bölüm açılışı, söz açılır, şahıs geçişi 1 → 2, edim geçişi haber → emir, yasak, nida; 7:74 söz kapanır, şahıs geçişi yok, edim geçişi emir, yasak, nida → emir, yasak; "
 "7:75 söz açılır / kapanır (iki söz), şahıs geçişi 2 → 3, edim geçişi emir, yasak → soru; ölçüm iltifât 7:73-75 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:73 've ilâ semûde exâhum sâlihan' — atıf, yönelme ve özel adlar; fiil 7:59 2. kelimeden takdir (morph CONJ + P + PN + N + PN); 7:74 'tettexizûne min suhûlihâ qusûran' — muzâri, tümleç ve nesne (morph IMPF + P + N + N); "
 "7:75 'qâle'l-mele'u'llezîne'stekberû' — mazi, fail ve ism-i mevsûl sıla cümlesiyle (morph PERF + DET + N + REL + PERF)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:73 19-28. kelime — 11:64 ile harekesiz eş (sayım: 'say 7:73 19-28'); 7:73 29-33. kelime — 11:64 ve 26:156 ile lemma dizisi eşi (sayım: 'dizi 7 73 29 33'); "
 "7:74 21-25. kelime — 2:60 ile harekesiz eş (sayım: 'say 7:74 21-25'); 7:74 16-17. kelime — 15:82 ve 26:149 ile harekesiz eş (sayım: 'say 7:74 16-17'); 7:73 kök أله ikilemesi; 7:74 kök أرض ve ذكر ikilemesi; 7:75 kök أمن, رسل ve قول ikilemesi; geniş eşli sayımlar: 'say 7:73 5-13', 'say 7:74 21-25', 'say 7:75 1-6'",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 21'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'hâzihî nâqatu'llâhi' 7:73 'İşte Allah'ın bu devesi' / 11:64 'işte bu Allah'ın devesi' (emsal metninde) — çakışma — tam okuma sonu (daraltılmış kalıp — bag kalıbı dört satıra bölündü, meal kesimleri ve emsal metnindeki virgül — söz dizimi: 'bu' işaretinin yeri); "
 "'lekum âyeten' 7:73 'size bir âyet' / 11:64 'size bir işarettir' (emsal metninde) — çakışma — tam okuma sonu ('âyet' / 'işaret' — âye karşılığı); "
 "'fe-zerûhâ' 7:73 'Onu bırakın' / 11:64 'Bırakın onu' (emsal metninde) — çakışma — tam okuma sonu (söz dizimi — nesnenin yeri); "
 "'te'kul fî ardi'llâhi' 7:73 'Allah'ın arzında yesin' / 11:64 'Allah'ın arzında yesin' (emsal metninde) — çakışma değil; "
 "'ve lâ temessûhâ bi-sû'in' 7:73 'ona kötülükle dokunmayın' / 11:64 'ona kötülükle dokunmayın' (emsal metninde) — çakışma değil; "
 "'ve lâ temessûhâ bi-sû'in' 7:73 'ona kötülükle dokunmayın' / 26:156 'Ona bir kötülükle dokunmayın' (emsal metninde) — çakışma — tam okuma sonu (nekre 'bir' takdiri — sû' karşılığı — emsaller arası: 11:64 'ona kötülükle' / 26:156 'Ona bir kötülükle'); "
 "'l-cibâle buyûten' 7:74 'dağları evler' / 15:82 'Dağlardan güvenli evler' (emsal metninde) — çakışma — tam okuma sonu (belirtme eki / ayrılma eki — emsalde 'min'; 'güvenli' emsalde fazla); "
 "'l-cibâle buyûten' 7:74 'dağları evler' / 26:149 'Dağlardan ustalıkla evler' (emsal metninde) — çakışma — tam okuma sonu (belirtme eki / ayrılma eki — emsalde 'min'; 'ustalıkla' emsalde fazla — emsaller arası: 15:82 'güvenli' / 26:149 'ustalıkla'); "
 "'ve lâ ta'sev fi'l-ardi mufsidîn' 7:74 've yeryüzünde bozguncular olarak taşkınlık etmeyin' / 2:60 'yeryüzünde bozgunculuk yaparak taşkınlık etmeyin' (emsal metninde) — çakışma — tam okuma sonu ('bozguncular olarak' / 'bozgunculuk yaparak' — mufsid karşılığı); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:73 'qâle' PERF — meal 'Dedi'; 'u'budu' IMPV — meal 'kulluk edin'; 'câ'etkum' PERF ('qad' ile) — meal 'geldi'; 'fe-zerûhâ' IMPV — meal 'bırakın'; 'te'kul' IMPF JUS — meal 'yesin'; 'temessûhâ' IMPF JUS ('lâ' ile) — meal 'dokunmayın'; 'ye'xuzekum' IMPF SUBJ ('fe' ile) — meal 'yakalar'; "
 "7:74 've'zkurû' IMPV (1. kelime) — meal 'hatırlayın'; 'ce'alekum' PERF ('iz' ile) — meal 'kıldığı'; 'bevve'ekum' PERF — meal 'yerleştirdi'; 'tettexizûne' IMPF IND — meal 'ediniyorsunuz'; 'tenhitûne' IMPF IND — meal 'yontuyorsunuz'; 'fe'zkurû' IMPV (18. kelime) — meal 'hatırlayın'; 'ta'sev' IMPF JUS ('lâ' ile) — meal 'etmeyin'; "
 "7:75 'qâle' PERF — meal 'dedi'; 'stekberû' PERF — meal 'büyüklenen'; 'stud'ifû' PERF edilgen — meal 'sayılanlara'; 'âmene' PERF — meal 'edenlere'; 'ta'lemûne' IMPF IND ('e' ile) — meal 'biliyor musunuz'; 'qâlû' PERF — meal 'Dediler'; 'ursile' PERF edilgen — meal 'gönderilene'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 'te'kul' IMPF 7:73'te istek kipi ('-sin') ile; 'ye'xuzekum' IMPF 7:73'te geniş zaman ('-r') ile; 'ce'alekum' PERF 7:74'te sıfat-fiil ('-dığı') ile; "
 "'tettexizûne', 'tenhitûne' IMPF 7:74'te şimdiki zaman ('-iyorsunuz', '-uyorsunuz') ile; 'stekberû' PERF 7:75'te sıfat-fiil ('-en') ile; 'stud'ifû' PERF 7:75'te sıfat-fiil ('-anlara') ile; 'âmene' PERF 7:75'te sıfat-fiil ('-enlere') ile; 'ta'lemûne' IMPF 7:75'te şimdiki zaman ('-iyor') ile; 'ursile' PERF 7:75'te sıfat-fiil ('-ene') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 73 75 21'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:73 tarayıcı adayı (kök أرض; D_yeti) — çıpa değil: anlatı öğesi, doğa iddiası yok (olgu=False); 7:74 ve 7:75 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:75 ('stekberû' / 'stud'ifû'); 7:73 ve 7:74 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök أخذ 7:73 ('ye'xuzekum') ve 7:74 ('tettexizûne') ile bölüm içi; kök أرض 7:73 ('ardi') ve 7:74 ('l-ardi', 'l-ardi') ile bölüm içi; kök أله 7:73 ('llâhe', 'ilâhin', 'llâhi', 'llâhi') ve 7:74 ('llâhi') ile bölüm içi; kök ربب 7:73 ('rabbikum') ve 7:75 ('rabbihî') ile bölüm içi; kök صلح 7:73 ('sâlihan') ve 7:75 ('sâlihan') ile bölüm içi; kök قول 7:73 ('qâle') ve 7:75 ('qâle', 'qâlû') ile bölüm içi; kök قوم 7:73 ('qavmi') ve 7:75 ('qavmihî') ile bölüm içi; bölüm açılışı — bölümün önceki bloğu yok; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 8-1 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 21, 22 ve sonrakiler; bölüm açılışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b21/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 73 75 21'; lem_bozuk.py 21 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 73 75 → AYN_SONUC; sunum/bolum4_kurallar.py 73 75 21 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 73 75 21 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 44)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 21 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('qâle', 'qavm', ''abede', 'allâh', 'mâ', 'min', 'ilâh', 'ğayr', 'qad', 'câ'e', 'beyyine', 'rabb', 'zâ', 'nâqa', 'âye', 'yezere' (morph LEM ham biçim), 'ekele', 'fî', 'ard', 'lâ', 'messe', 'sû'', 'exaze', ''azâb', 'zekere', 'iz', 'ce'ale', 'xalîfe', 'ba'd', 'âlâ'', 'cebel', 'beyt', 'ta'se', 'mufsid', 'mele'', 'ellezî', 'istekbere'); joker '_' dizi lemma dizisinde boş öğe olan zamir ve önek lemmalı kelimelerde ('lekum' 7:73 10. ve 22.); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (73, 75): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_73_75.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_7_b20k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '73', '75'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '73', '75', '21'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '73', '75', '21'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '73', '75', '21', '--tazelik-yok')}
    for _n in range(7, 44): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '73', '75', '21')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42, B43 = [_R['B%d' % _n].splitlines() for _n in range(6, 44)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'), 'B40_HEPSI': (B40[-1] if B40 else '?'), 'B41_HEPSI': (B41[-1] if B41 else '?'), 'B42_HEPSI': (B42[-1] if B42 else '?'), 'B43_HEPSI': (B43[-1] if B43 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI), 'B6_ESMA': ('; '.join(l[5:] for l in B6 if 'esmâ kural' in l and l.startswith('HATA')) or 'sapma 0')}
    I_cur = list(I_HAM)
    for k, v in REP.items(): I_cur = I_cur[:len(BEK)] + [x.replace(k, v) for x in I_cur[len(BEK):]]  # bölüm 9 kuralı 9: taşınan denetim maddelerine yer tutucu değişimi uygulanmaz
    I_cur[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3, bölüm 6 kuralı 2 — komut 'python3 sunum/cakisma.py' + sûre 7'nin okunmuş bütün ARIZA dosyaları; bu bloğun karşılıklarına dokunan gruplar ve son dosyaya dokunan KÖK grupları; grup başına tam bir kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
                  + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
    if I_cur == onceki: break
    onceki = list(I_cur)
yaz(I_cur)
print('yazıldı', len(I_cur), 'tur', tur)
print('\n'.join(CAK_L))
print(GLS)
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42, B43): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
