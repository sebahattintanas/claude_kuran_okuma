# blok 15 (5:42-44) ARIZA oluşturucu — bölüm 7-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b15/olcum.txt'
os.environ['SAY2'] = '/home/claude/b15/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {33: {6: "'ve rasûlehû'", 7: "'ve yes'avne'", 18: "'ve erculuhum'", 30: "'ve lehum fi'l-âxirati'"}, 34: {9: "'fa'lemû'"}, 35: {6: "'ve'bteğû'", 9: "'ve câhidû'"}, 36: {11: "'ve mislehû'", 22: "'ve lehum 'azâbun'"}}
BOL = "'Küfürde yarışanlar; Tevrat, İncil ve Kitap ile hüküm'"


def sd(key):
    return sayim.S2[key][1]


def sic(key):
    n, d = sayim.S2[key]
    return 1 + len([x for x in d['basilan'] if x.startswith('5:')]) + d['okunmus_si'] + d['henuz_si']


def taban(key, ay):
    n, d = sayim.S2[key]
    p = [ay] + [x for x in d['basilan'] if x.startswith('5:') and x != ay]
    if d['okunmus_si']: p.append('okunmus_si %d' % d['okunmus_si'])
    if d['henuz_si']: p.append('henuz_si %d' % d['henuz_si'])
    return ' + '.join(p)


R5 = [
 ("5:42", "'inne allâh ahbeb'", 2, 'say 5:42 23-25', "harekesiz 'inna'llâhe yuhibb' (23-25. kelime)", None),
 ("5:44", "'lem hakeme mâ enzele allâh zâ _'", 3, 'say 5:44 34-40', "harekesiz 'lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum' (34-40. kelime)", None),
 ("5:44", "'mâ enzele allâh'", 5, 'say 5:44 36-38', "harekesiz 'bi-mâ enzele'llâh' (36-38. kelime)", None),
]
r5 = []
for ay, kal, nk, key, ad, dz in R5:
    s = sic(key)
    h = "%s nakarat3 %s %d (tür ic) / %s sûre içi %d (%s)" % (ay, kal, nk, ad, s, taban(key, ay))
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

K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}

VF_YAZI = {42: {5: "'fe-in câ'ûke'", 12: "'ve in tu'rid'", 18: "'ve in hakemte'"}, 43: {1: "'ve keyfe'", 3: "'ve 'indehumu'", 13: "'ve mâ ulâ'ike'"}, 44: {6: "'ve nûr'", 14: "'ve'r-rabbâniyyûne'", 15: "'ve'l-ahbâru'", 21: "'ve kânû'", 24: "'fe-lâ'", 27: "'ve'xşevni'", 28: "'ve lâ teşterû'", 33: "'ve men'", 39: "'fe-ulâ'ike'"}}
M42 = ("5:42 'Onlar yalana çokça kulak verenler' ('semmâ'ûne li'l-kezib', 'onlar' takdiri (mübteda takdiri), 'çokça kulak veren' 'semmâ'' açılımı (1. kelime; mübalağa; çoğul '-ler'), 'li' 2. kelimede yönelme eki ile ('yalana' içinde; fiil yönetimi takdiri), 'yalan' 'kezib' karşılığı (2. kelime)); "
 "'haramı çokça yiyenlerdir' ('ekkâlûne li's-suht', 'çokça yiyen' 'ekkâl' açılımı (3. kelime; mübalağa; çoğul '-ler'), 'li' 4. kelimede belirtme eki ile ('haramı' içinde; fiil yönetimi takdiri), 'haram' 'suht' karşılığı (4. kelime), '-dir' takdiri ('yiyenlerdir' içinde; isim cümlesi haberi)); "
 "'Sana gelirlerse aralarında hüküm ver ya da onlardan yüz çevir' ('fe-in câ'ûke fa'hkum beynehum ev a'rid 'anhum', 'fe' 5. kelimede karşılıksız (morph REM), 'in' 5. kelimede '-se' ile ('gelirlerse' içinde; morph COND), 'gel-' 'câ'û' karşılığı (6. kelime; I. bab), 'û' 6. kelimede karşılıksız (fail eki — 'gelirlerse' içinde), 'ke' 6. kelimede yönelme eki ile ('Sana' içinde; fiil yönetimi takdiri), "
 "'fe' 7. kelimede karşılıksız (morph RSLT; şart cevabı), 'hüküm ver-' 'hkum' açılımı (7. kelime; I. bab; emir 2MS), 'ara' 'beyn' karşılığı (8. kelime; iyelik ve bulunma eki ile 'aralarında'), 'hum' 8. kelimede iyelik ile ('aralarında' içinde), 'ev' 9. kelimede 'ya da' ile (morph CONJ), 'yüz çevir-' 'a'rid' açılımı (10. kelime; IV. bab; emir 2MS), "
 "''an' 11. kelimede '-dan' ile ('onlardan' içinde), 'hum' 11. kelimede 'onlar' ile ('onlardan' içinde), sıralama: fiil sona alındı); "
 "'Onlardan yüz çevirirsen sana hiçbir şeyle zarar veremezler' ('ve in tu'rid 'anhum fe-len yedurrûke şey'â', 've' 12. kelimede karşılıksız (morph CONJ), 'in' 12. kelimede '-se' ile ('çevirirsen' içinde; morph COND), 'yüz çevir-' 'tu'rid' açılımı (13. kelime; IV. bab), ''an' 14. kelimede '-dan' ile ('Onlardan' içinde), 'hum' 14. kelimede 'onlar' ile ('Onlardan' içinde), "
 "'fe' 15. kelimede karşılıksız (morph RSLT), 'len' 15. kelimede olumsuzluk eki ile ('veremezler' içinde; morph NEG), 'zarar ver-' 'yedurrû' açılımı (16. kelime; I. bab; LEM 'yedurre' (morph LEM ham biçim)), 'û' 16. kelimede karşılıksız (fail eki — 'veremezler' içinde), 'ke' 16. kelimede yönelme eki ile ('sana' içinde; fiil yönetimi takdiri), "
 "'şey' 'şey'' karşılığı (17. kelime; nekre — 'hiçbir' takdiri; vasıta eki ile 'şeyle'), sıralama: fiil sona alındı); "
 "'Hüküm verirsen aralarında adaletle hüküm ver' ('ve in hakemte fa'hkum beynehum bi'l-qist', 've' 18. kelimede karşılıksız (morph CONJ), 'in' 18. kelimede '-se' ile ('verirsen' içinde; morph COND), 'hüküm ver-' 'hakemte' açılımı (19. kelime; I. bab), 'te' 19. kelimede 2MS ile ('verirsen' içinde), 'fe' 20. kelimede karşılıksız (morph RSLT), "
 "'hüküm ver-' 'hkum' açılımı (20. kelime; I. bab; emir 2MS), 'ara' 'beyn' karşılığı (21. kelime; iyelik ve bulunma eki ile 'aralarında'), 'hum' 21. kelimede iyelik ile ('aralarında' içinde), 'bi' 22. kelimede vasıta eki ile ('adaletle' içinde), 'adalet' 'qist' karşılığı (22. kelime), sıralama: fiil sona alındı); "
 "'Şüphesiz Allah adaletli davrananları sever' ('inna'llâhe yuhibbu'l-muqsitîn', 'inne' 23. kelimede 'şüphesiz' ile, lafız 24. kelimede 'Allah' ile, 'sev-' 'yuhibbu' karşılığı (25. kelime; IV. bab; LEM 'ahbeb' (morph LEM ham biçim)), 'adaletli davranan' 'muqsit' açılımı (26. kelime; IV. bab ortacı; çoğul '-lar'; belirtme eki ile 'davrananları'), sıralama: fiil sona alındı)")
M43 = ("5:43 'Yanlarında içinde Allah'ın hükmü bulunan Tevrat varken seni nasıl hakem yaparlar?' ('ve keyfe yuhakkimûneke ve 'indehumu't-tevrâtu fîhâ hukmu'llâh', 've' 1. kelimede karşılıksız (morph REM), 'keyfe' 1. kelimede 'nasıl' ile (morph INTG), 'hakem yap-' 'yuhakkimûne' açılımı (2. kelime; II. bab; LEM 'yuhakkimu' (morph LEM ham biçim)), 'ûne' 2. kelimede karşılıksız (fail eki — 'yaparlar' içinde), 'ke' 2. kelimede 'seni' ile, "
 "'ve' 3. kelimede karşılıksız (morph CIRC; 'varken' içinde), ''inde' 3. kelimede '-larında' ile ('Yanlarında' içinde), 'hum' 3. kelimede iyelik ile ('Yanlarında' içinde), 'Tevrat' 'tevrâ' karşılığı (4. kelime; özel ad), 'fî' 5. kelimede 'içinde' ile, 'hâ' 5. kelimede karşılıksız ('içinde' iyeliği), 'hüküm' 'hukm' karşılığı (6. kelime; iyelik ile 'hükmü'), "
 "lafız 7. kelimede 'Allah' ile (ilgi eki 'Allah'ın' içinde), 'bulun-' takdiri ('bulunan' içinde), 'var' takdiri ('varken' içinde), sıralama: 've' cümlesi öne alındı); "
 "'Sonra bunun ardından yüz çevirirler' ('summe yetevellevne min ba'di zâlik', 'summe' 8. kelimede 'sonra' ile (morph CONJ), 'yüz çevir-' 'yetevellevne' açılımı (9. kelime; V. bab), 'û' 9. kelimede karşılıksız (fail eki — 'çevirirler' içinde), 'min' 10. kelimede karşılıksız ('ardından' içinde), 'sonra' 'ba'd' karşılığı (11. kelime; 'ardından' açılımı), 'zâlike' 12. kelimede 'bu' ile ('bunun' içinde), sıralama: fiil sona alındı); "
 "'Onlar inananlar değildir' ('ve mâ ulâ'ike bi'l-mu'minîn', 've' 13. kelimede karşılıksız (morph REM), 'mâ' 13. kelimede 'değil' ile (morph NEG; 'kâne' ailesi), 'ulâ'ike' 14. kelimede 'onlar' ile, 'bi' 15. kelimede karşılıksız (haber 'bi'si; morph P), 'inanan' 'mu'min' karşılığı (15. kelime; ortaç; çoğul '-lar'), '-dir' takdiri ('değildir' içinde; olumsuz haber))")
M44 = ("5:44 'Şüphesiz Tevrat'ı biz indirdik' ('innâ enzelna't-tevrât', 'inne' 1. kelimede 'şüphesiz' ile, 'nâ' 1. kelimede 'biz' ile, 'indir-' 'enzelna' karşılığı (2. kelime; IV. bab), 'nâ' 2. kelimede 1P ile ('indirdik' içinde), 'Tevrat' 'tevrâ' karşılığı (3. kelime; özel ad; belirtme eki ile 'Tevrat'ı'), sıralama: fiil sona alındı); "
 "'onda hidayet ve nur vardır' ('fîhâ hudan ve nûr', 'fî' 4. kelimede '-da' ile ('onda' içinde), 'hâ' 4. kelimede 'o' ile ('onda' içinde), 'hidayet' 'hudâ' karşılığı (5. kelime; nekre — takdirsiz), 've' 6. kelimede 've' ile (morph CONJ), 'nur' 'nûr' karşılığı (6. kelime; nekre — takdirsiz), 'var' takdiri (isim cümlesi), '-dır' takdiri ('vardır' içinde; isim cümlesi haberi)); "
 "'Teslim olmuş nebiler Yahudi olanlara onunla hüküm verirlerdi' ('yahkumu bihe'n-nebiyyûne'llezîne eslemû li'llezîne hâdû', 'hüküm ver-' 'yahkumu' açılımı (7. kelime; I. bab; '-irlerdi' hikâye takdiri), 'bi' 8. kelimede vasıta eki ile ('onunla' içinde), 'hâ' 8. kelimede 'o' ile ('onunla' içinde), 'nebi' 'nebiyy' karşılığı (9. kelime; çoğul '-ler'), "
 "'ellezîne' 10. kelimede '-muş' ile (ism-i mevsûl; 'olmuş' içinde), 'teslim ol-' 'eslemû' açılımı (11. kelime; IV. bab), 'û' 11. kelimede karşılıksız (fail eki — 'olmuş' içinde), 'li' 12. kelimede yönelme eki ile ('olanlara' içinde), 'ellezîne' 12. kelimede '-anlar' ile (ism-i mevsûl; 'olanlara' içinde), "
 "'Yahudi ol-' 'hâdû' açılımı (13. kelime; I. bab; LEM 'hâdu' (morph LEM ham biçim)), 'û' 13. kelimede karşılıksız (fail eki — 'olanlara' içinde), sıralama: fail ve sıfat öne alındı); "
 "'rabbaniler ve âlimler de Allah'ın kitabından korumakla görevlendirildikleri şeyle hüküm verirlerdi' ('ve'r-rabbâniyyûne ve'l-ahbâru bi-me'stuhfizû min kitâbi'llâh', 've' 14. kelimede 've' ile (morph CONJ), 'rabbani' 'rabbâniyyûne' karşılığı (14. kelime; çoğul '-ler'), 've' 15. kelimede 'de' ile (morph CONJ), 'âlim' 'ahbâr' karşılığı (15. kelime; çoğul '-ler'), "
 "'bi' 16. kelimede vasıta eki ile ('şeyle' içinde), 'mâ' 16. kelimede 'şey' ile (ism-i mevsûl; 'şeyle' içinde), 'korumakla görevlendiril-' 'stuhfizû' açılımı (17. kelime; X. bab; edilgen; LEM 'ustuhfizu' (morph LEM ham biçim)), 'û' 17. kelimede karşılıksız (nâib fâil eki — 'görevlendirildikleri' içinde), "
 "'min' 18. kelimede '-dan' ile ('kitabından' içinde), 'kitap' 'kitâb' karşılığı (19. kelime; iyelik ile 'kitabından'), lafız 20. kelimede 'Allah' ile (ilgi eki 'Allah'ın' içinde), 'hüküm ver-' takdiri ('yahkumu' 7. kelimenin ortak yüklemi), sıralama: fiil sona alındı); "
 "'ve onun üzerine şahitlerdi' ('ve kânû 'aleyhi şuhedâ'', 've' 21. kelimede 've' ile (morph CIRC), 'ol-' 'kânû' karşılığı (21. kelime; I. bab; '-di' ile — 'şahitlerdi' içinde), 'û' 21. kelimede karşılıksız (fail eki — 'şahitlerdi' içinde), ''alâ' 22. kelimede '-e' ile ('üzerine' içinde), 'hî' 22. kelimede 'onun' ile, 'şahit' 'şehîd' karşılığı (23. kelime; çoğul '-ler'), sıralama: haber sona alındı); "
 "'Artık insanlardan korkmayın' ('fe-lâ taxşevu'n-nâs', 'fe' 24. kelimede 'Artık' ile (morph REM), 'lâ' 24. kelimede olumsuz emir eki ile ('korkmayın' içinde; morph PRO), 'kork-' 'taxşev' karşılığı (25. kelime; I. bab), 'û' 25. kelimede 2MP ile ('korkmayın' içinde), 'insan' 'nâs' karşılığı (26. kelime; çoğul '-lar'; ayrılma eki ile 'insanlardan'; fiil yönetimi takdiri)); "
 "'benden korkun' ('ve'xşevn', 've' 27. kelimede karşılıksız (morph REM), 'kork-' 'xşev' karşılığı (27. kelime; I. bab; emir 2MP), 'û' 27. kelimede 2MP ile ('korkun' içinde), 'nî' 27. kelimede 'ben' ile ('benden' içinde; ayrılma eki — fiil yönetimi takdiri)); "
 "'âyetlerimi az bir bedelle satmayın' ('ve lâ teşterû bi-âyâtî semenen qalîlâ', 've' 28. kelimede 've' ile (morph CONJ), 'lâ' 28. kelimede olumsuz emir eki ile ('satmayın' içinde; morph PRO), 'sat-' 'teşterû' karşılığı (29. kelime; VIII. bab), 'û' 29. kelimede 2MP ile ('satmayın' içinde), 'bi' 30. kelimede belirtme eki ile ('âyetlerimi' içinde; fiil yönetimi takdiri), "
 "'âyet' 'âye' karşılığı (30. kelime; çoğul '-ler'), 'î' 30. kelimede iyelik ile ('âyetlerimi' içinde), 'bedel' 'semen' karşılığı (31. kelime; nekre — 'bir' takdiri; vasıta eki 'bedelle' içinde), 'az' 'qalîl' karşılığı (32. kelime; nekre — takdirsiz; sıfat), sıralama: fiil sona alındı); "
 "'Kim Allah'ın indirdiğiyle hüküm vermezse' ('ve men lem yahkum bi-mâ enzele'llâh', 've' 33. kelimede karşılıksız (morph REM), 'men' 33. kelimede 'kim' ile (morph COND; şart eki '-se' 'vermezse' içinde), 'lem' 34. kelimede olumsuzluk eki ile ('vermezse' içinde; morph NEG), 'hüküm ver-' 'yahkum' açılımı (35. kelime; I. bab), "
 "'bi' 36. kelimede vasıta eki ile ('indirdiğiyle' içinde), 'mâ' 36. kelimede '-diği' ile (ism-i mevsûl; 'indirdiğiyle' içinde), 'indir-' 'enzele' karşılığı (37. kelime; IV. bab), lafız 38. kelimede 'Allah' ile (ilgi eki 'Allah'ın' içinde), sıralama: şart sona alındı); "
 "'işte onlar kâfirlerin ta kendileridir' ('fe-ulâ'ike humu'l-kâfirûn', 'fe' 39. kelimede 'işte' ile (morph RSLT; şart cevabı), 'ulâ'ike' 39. kelimede 'onlar' ile, 'hum' 40. kelimede 'ta kendileri' ile (ayırma zamiri), 'kâfir' 'kâfir' karşılığı (41. kelime; çoğul '-ler'), '-dir' takdiri ('kendileridir' içinde; isim cümlesi haberi))")
MEALS = (M42, M43, M44)





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
open('/home/claude/b15/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '15')
BLOKLAR = [str(i) for i in range(1, 16)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR).replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '15').replace('\n', '; ')
EMS = open('/home/claude/b15/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '42', '44', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b15/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'
GLS = run('/home/claude/sunum/gloss_tara.py', '42', '44', '15').splitlines()

I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11): bu blokta araç değişmedi; sunum/sinifla.py (SON 44); bölüm 6 kurallarının araçları (bolum4 / bolum5 / bolum6_kurallar, mutasyon_sina — MUT_SONUC) koşuldu",
 "kök tablosu: ölçümde '???' 5:42-44 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 42 44 15'): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:43:15 مُؤْمِن 'degil' — 've mâ ulâ'ike bi'l-mu'minîn', kural 'çoğul insan göndergeli → degil' (inananlar); 5:44:6 نُور 'degil' — 'hudan ve nûr', kural 'esmâ adı esmâ dışı göndergeyle → degil' (Tevrat'taki nur); 5:44:23 شَهِيد 'degil' — 've kânû 'aleyhi şuhedâ'', kural 'çoğul insan göndergeli → degil' (şahitler) (esma_el_ekle → esma_kayit; "
 "bölüm 6 kuralı 14: eş yapılı önceki kayıtların kural adı — betikle, sapma B6_ESMA); lafız 5:42, 5:43, 5:44; Rab ölçümde 5:44 14. sırada — 'r-rabbâniyyûne' kök ربب, Rab adı değil",
 "esma_kayit: 5:42 'mühür hayır' (uyuşuyor), 5:43 'mühür EVET ton cemâl' (ölçüm MÜHÜRSÜZ — uyuşmuyor; esmâ göndergesi inananlar, 'degil'), 5:44 'mühür hayır' (ölçüm MÜHÜRSÜZ — uyuşuyor)",
 "ölçüm: 5:42 '{{1|fâsıla ٱلمقسطين → ن, N sınıfı}}', '{{1|simetri \\[4, 5, 18, 1\\]}}', '{{1|harf 116 → harf3 111, isaret 5}}' ve '{{1|dış düğüm 2}}'; 5:43 '{{2|aktör: adlı تَوْراة 4\\. sırada \\(kitab, rol fail\\)}}', '{{2|fâsıla بٱلمؤمنين → ن, N sınıfı}}', '{{2|simetri \\[3, 4, 12, 1\\]}}', '{{2|harf 71 → harf3 68, isaret 3}}' ve '{{2|dış düğüm 0}}'; "
 "5:44 '{{3|aktör: adlı تَوْراة 3\\. sırada \\(kitab, rol meful\\)}}', '{{3|biçim NEHY}}', '{{3|EDİLGEN 1/11 fiil, pas z=0,19}}', '{{3|sayı işareti ثَمَن, قَلِيل}}', '{{3|fâsıla ٱلكفرون → ن, N sınıfı}}', '{{3|simetri \\[4, 1, 36, 1\\]}}', '{{3|harf 206 → harf3 192, isaret 14}}' ve '{{3|dış düğüm 2}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 42 44 15'): KALAN_P",
 "ölçüm aktör: 5:42 aktör yok; 5:43 adlı Tevrat (kitap, rol fail); 5:44 adlı Tevrat (kitap, rol meful) — A1'de 'adlı aktör' etiketiyle",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:42 emir, şart — COND 3 'in' (5., 12., 18.), IMPV 3 'fa'hkum' (7., 20.), 'a'rid' (10.), NEG 1 'len' (15.); 5:43 soru — INTG 1 'keyfe' (1.), NEG 1 'mâ' (13.); 5:44 emir, yasak, şart — PRO 2 'lâ' (24., 28.), IMPV 1 've'xşevni' (27.), COND 1 'men' (33.), NEG 1 'lem' (34.); biçim NEHY; EDİLGEN 1 'stuhfizû' (17.)",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:44 ★★★ (kaynak n, z=3,04); 5:42 ve 5:43 yıldız yok",
 "fâsıla: 5:41 م (عظيم) → 5:42 ن (المقسطين) → 5:43 ن (بالمؤمنين) → 5:44 ن (الكافرون); hepsi N sınıfı; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:42 49:9 (emsal olarak basıldı) ve okunmuş başka bir ayet; 5:43 xref yok; 5:44 2:41 (emsal olarak basıldı) ve okunmuş başka bir ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' ile; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:42 'inne allâh ahbeb' süzgeç GEÇMEZ; 5:43 kalıp yok; 5:44 'lem hakeme mâ enzele allâh zâ _' ve 'mâ enzele allâh' süzgeç GEÇER",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15 — ölçüt: 1P / 1S / 2MS / 2FS / 2MP / 2FP / 2D / 3MS / 3FS / 3D / 3MD / 3FD / 3MP / 3FP zamirlerin hepsi 'adsız', etiketin kendi parantezinde; adlı aktör ölçümün 'aktör: adlı' alanından): "
 "5:42 muhatap 2MS (adsız), 3MP (adsız — 'câ'ûke', 'yedurrûke' failleri; 'beynehum', ''anhum'), 3MS (adsız — 'yuhibbu' faili), Allah (lafız), 'semmâ'ûne', 'ekkâlûne', 'şey'â', 'l-muqsitîn'; 5:43 muhatap 2MS (adsız), 3MP (adsız), 3FS (adsız — 'fîhâ'), 't-tevrâtu' (adlı aktör), Allah (lafız), 'ulâ'ike'; "
 "5:44 konuşan 1P (adsız), 't-tevrâte' (adlı aktör), 3FS (adsız), 3MS (adsız), 3MP (adsız), muhatap 2MP (adsız), konuşan 1S (adsız), Allah (lafız), 'n-nebiyyûne', 'r-rabbâniyyûne', 'l-ahbâru', 'n-nâse', 'men' — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): blokta 'qâle' yok, söz aralığı yok (A3 —); 5:44 konuşan 1P / 1S doğrudan anlatım (söz değil); REM sapması (komut 'python3 sunum/bolum4_kurallar.py 42 44 15' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:42 'fe-in' (5.) REM, 'fa'hkum' (7., 20.) ve 'fe-len' (15.) RSLT, 've in' (12., 18.) CONJ; 5:43 've keyfe' (1.), 've mâ' (13.) REM, 've 'indehumu' (3.) CIRC; 5:44 've nûr' (6.), 've'r-rabbâniyyûne' (14.), 've'l-ahbâru' (15.), 've lâ' (28.) CONJ, 've kânû' (21.) CIRC, 've'xşevni' (27.), 've men' (33.) REM, 'fe-lâ' (24.) REM, 'fe-ulâ'ike' (39.) RSLT",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:42 ◈B سمع ('semmâ'ûne' 1. kelime — B3; anlam notu: yalana kulak verme); 5:44 ◈B أنس ('n-nâse' 26. kelime — B1; anlam notu: insanlardan korkma yasağı); 5:43 tetik yok; oturum_tetik kuru koşusu 5:42 سمع'yu yakaladı (önceki yazımda ◈B boştu) — blok 14'te 5:41 'semmâ'ûne' (20. ve 22. kelime, سمع B3) ◈B'de anılmamıştı: geriye dönük, tam okuma sonu",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 42 44 15'): TETIKDISI; anılış: 5:42 kök أكل ('ekkâlûne' 3. kelime — yeme, beden); 5:42 kök عرض ('a'rid' 10. kelime, 'tu'rid' 13. kelime — yüz çevirme, mecaz; beden değil); 5:43 kök ولي ('yetevellevne' 9. kelime — yüz çevirme, mecaz); 5:43 kök بعد ('ba'di' 11. kelime — 'sonra', zaman); 5:44 kök نور ('nûr' 6. kelime — ışık; K alanına yakın, tetik dışı); 5:44 kök ثمن ('semenen' 31. kelime — bedel; gloss 'sekiz', sayı işareti); oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:42 (49:9), 5:43 (24:47), 5:44 (2:41, 3:79) (kontrol.py ile); blok geçişi 5:41 → 5:42: ayetler arası kalıp 'semmâ'ûne li'l-kezib' (5:41, 5:42) — sayım 'say 5:42 1-2' (sûre içi 5:41 ve 5:42; korpusta başka eş yok) — ardışık bağ yerine sayımla kayıt (bölüm içi tekrar); "
 "D3 dışı bırakılan basılmış sayım eşleri: 5:42 'inna'llâhe yuhibb' 2:195, 5:13; 5:43 'hukmu'llâh' 60:10; 5:44 'semenen qalîlâ' 3:187, 3:199; 'kitâbi'llâh' 4:24, 5:21, 59:3; 've'xşevn' 5:3 — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:42 edim geçişi emir, yasak, nida, şart → emir, şart; şahıs geçişi yok; şart → cevap (ayet içi; COND 'in' 5. kelime: 'fe-in câ'ûke' / 'fa'hkum beynehum ev a'rid 'anhum' (7. kelime)); şart → cevap (ayet içi; COND 'in' 12. kelime: 've in tu'rid 'anhum' / 'fe-len yedurrûke şey'â' (15. kelime)); "
 "şart → cevap (ayet içi; COND 'in' 18. kelime: 've in hakemte' / 'fa'hkum beynehum bi'l-qist' (20. kelime)); 5:43 edim geçişi emir, şart → soru; şahıs geçişi yok; 5:44 edim geçişi soru → emir, yasak, şart; şahıs geçişi yok; şart → cevap (ayet içi; COND 'men' 33. kelime: 've men lem yahkum bi-mâ enzele'llâh' / 'fe-ulâ'ike humu'l-kâfirûn' (39. kelime))",
 "sözdizimi (okuma; morph etiketiyle): 5:42 'semmâ'ûne … ekkâlûne' — mübtedası takdirli haber (morph etiketi yok, okuma); 'fe-in câ'ûke' — istînâf (morph REM) + şart (COND); 'fa'hkum … ev a'rid' — şart cevabı, iki emir 'ev' ile (morph RSLT, CONJ); 'inna'llâhe yuhibbu'l-muqsitîn' — gerekçe ('inne' morph ACC); "
 "5:43 've keyfe' — istînâf (morph REM) + soru (INTG); 've 'indehumu't-tevrâtu' — morph CIRC; 've mâ ulâ'ike bi'l-mu'minîn' — istînâf (morph REM); 'mâ' 'kâne' ailesi olumsuz (morph NEG, haberi 'bi' ile); 5:44 'innâ enzelna't-tevrâte' — 'inne' + 1P; 'yahkumu bihe'n-nebiyyûne' — 't-tevrâte'nin sıfatı (morph etiketi yok, okuma); 've kânû 'aleyhi şuhedâ'' — morph CIRC; 'fe-lâ taxşevu' — istînâf (morph REM) + yasak (morph PRO); 've men lem yahkum … fe-ulâ'ike' — şart / cevap (COND / RSLT)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:42 'semmâ'ûne li'l-kezib' ile açılıyor (1-2. kelime) — ayetler arası kalıp 'semmâ'ûne li'l-kezib' (5:41, 5:42); 5:42 kök حكم üç geçiş (7., 19., 20. kelime), kök قسط iki geçiş ('l-qist' 22. / 'l-muqsitîn' 26. kelime); "
 "5:43 kök حكم iki geçiş — 'yuhakkimûneke' (II. bab, hakem yapma) / 'hukmu'llâh'; 5:44 kök خشي iki geçiş — 'taxşevu'n-nâse' (yasak) / 've'xşevni' (emir): insanlardan / benden karşıtlığı; 5:44 kök نزل iki geçiş — 'enzelna' (1P) / 'enzele'llâh' (lafız); bölümün 'Tevrat ile hüküm' kısmı 5:43-44'te ('t-tevrâtu', 't-tevrâte'; ölçüm aktör adlı Tevrat)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 15'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + "'; çıktı aynen): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle): 'llâhe yuhibbu'l-muqsitîn' 5:42 'adaletli davrananları sever' / 49:9 (emsal metninde 'muqsit' karşılığı) — tam okuma sonu; 've mâ ulâ'ike bi'l-mu'minîn' 5:43 'Onlar inananlar değildir' / 24:47 — tam okuma sonu; "
 "'ve lâ teşterû bi-âyâtî semenen qalîlâ' 5:44 'âyetlerimi az bir bedelle satmayın' / 2:41 — tam okuma sonu; 'rabbâniyyîn' 5:44 'rabbani' / 3:79 — tam okuma sonu",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 42 44 15'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:44 tarayıcı adayı (kök نور; A_şart, F_ölçü) — çıpa değil: 'fîhâ hudan ve nûr' kitabın nitelemesi (olgu=False); 5:42 ve 5:43 tarayıcı adayı yok; L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:42 ('fa'hkum beynehum' / 'ev a'rid 'anhum'), 5:44 ('fe-lâ taxşevu'n-nâse' / 've'xşevni') — okuma; ayetler arası yok; eşleme betikle: ADAY_P",
 "aday 1041: kök حكم 5:42 'fa'hkum' (muhatap 2MS), 5:43 'yuhakkimûneke' (3MP hakem yapma) / 'hukmu'llâh' (Allah'ın hükmü), 5:44 'yahkumu' (nebiler, rabbaniler, âlimler) / 'lem yahkum bi-mâ enzele'llâh' — hükmün kaynağı lafız, hükmedenler insan; kök حبب 5:42 'yuhibbu' (fail Allah) — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 7-2 — bölüm dört blok (14, 15, 16, 17); başlıktaki 'Tevrat ile hüküm' 5:43-44 ('t-tevrâtu', 't-tevrâte', 'yahkumu', 'lem yahkum'); 'İncil ve Kitap ile hüküm' sonraki bloklarda; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b15/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3 — betikle: komut 'python3 sunum/bolum5_kurallar.py 42 44 15'; lem_bozuk.py 15 çıktısı): 5:42:16 'yedurre', 5:42:25 'ahbeb', 5:43:2 'yuhakkimu', 5:44:13 'hâdu', 5:44:17 'ustuhfizu' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 42 44 → AYN_SONUC; sunum/bolum4_kurallar.py 42 44 15 → KHATA_HEPSI; sunum/bolum5_kurallar.py 42 44 15 → B5_HEPSI; sunum/bolum6_kurallar.py 42 44 15 → B6_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (sunum/sonradan.py --plan 15): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('semmâ'', 'kezib', 'ekkâl', 'suht', 'câ'e', 'hakeme', 'beyn', 'a'rada', 'yedurre' (morph LEM ham biçim), 'şey'', 'qist', 'ahbeb' (morph LEM ham biçim), 'muqsit', 'keyfe', 'yuhakkimu' (morph LEM ham biçim), 'tevrâ', 'hukm', 'tevellâ', 'ba'd', 'mu'min', 'enzele', 'hudâ', 'nûr', 'nebiyy', 'eslema', 'hâdu' (morph LEM ham biçim), "
 "'rabbâniyyîn', 'ahbâr', 'ustuhfizu' (morph LEM ham biçim), 'kitâb', 'kâne', 'şehîd', 'xaşiye', 'nâs', 'işterâ', 'âye', 'semen', 'qalîl', 'kâfir'); transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]


def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (42, 44): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_42_44.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '15'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b13.txt', encoding='utf-8').read().splitlines()[:2]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '42', '44').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '42', '44', '15').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '42', '44', '15').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '42', '44', '15', '--tazelik-yok').splitlines()
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'),
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI), 'B6_ESMA': ('; '.join(l[5:] for l in B6 if 'esmâ kural' in l and l.startswith('HATA')) or 'sapma 0')}
    I_cur = list(I_HAM)
    for k, v in REP.items(): I_cur = [x.replace(k, v) for x in I_cur]
    I_cur[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3, bölüm 6 kuralı 2 — komut 'python3 sunum/cakisma.py' + sûre 5'in okunmuş bütün ARIZA dosyaları; bu bloğun karşılıklarına dokunan gruplar ve son dosyaya dokunan KÖK grupları; grup başına tam bir kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
                  + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
    if I_cur == onceki: break
    onceki = list(I_cur)
yaz(I_cur)
print('yazıldı', len(I_cur), 'tur', tur)
print('\n'.join(CAK_L))
print(GLS); print(KUR); print(B5); print(B6)
