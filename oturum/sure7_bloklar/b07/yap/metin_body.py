# sûre 7 blok 7 (7:26-27) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b07/say2.txt'
os.environ['OLC'] = '/home/claude/b07/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Ey Âdemoğulları: giysi, fitne, ziynet; haram kılınanlar' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol mecrur\)', _OL[0]).group(0))
_AK2 = _esc(re.search(r'aktör: adlı .*rol fail\+meful\)', _OL[1]).group(0))
_ES2 = _esc(re.search(r'esmâ \S+ 27\. sırada, ORTA konum, MÜHÜRSÜZ', _OL[1]).group(0))
_HP = _esc(re.search(r'HAPAKS: .*? — hapaks z=3,28', _OL[0]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 26: "Ey Âdemoğulları, size çirkin yerlerinizi gizleyen bir giysi ve süs indirdik. Sakınma giysisi ise, o daha hayırlıdır. Bu, Allah'ın âyetlerindendir; umulur ki düşünürler.",
 27: "Ey Âdemoğulları, şeytan sizi sakın fitneye düşürmesin; ana babanızı bahçeden çıkardığı gibi: çirkin yerlerini onlara göstermek için giysilerini üzerlerinden çekip alıyordu. Gerçekten o ve topluluğu sizi onları görmediğiniz yerden görür. Gerçekten biz şeytanları inanmayanlara dostlar kıldık.",
}

T = {}
T[26] = ("konuşan 1P (adsız; 'enzelnâ' — 4. kelime); muhatap 2MP eki (adsız; ''aleykum', 'sev'âtikum' — 5. ve 8. kelime); 'yuvârî' 3MS (adsız; gönderge 'libâsen' 6. kelime, 7. kelime); "
         "'le'allehum' 3MP eki (adsız; tartışmalı; gönderge 'benî' 1. kelime, 18. kelime); 'yezzekkerûn' 3MP (adsız; tartışmalı; gönderge 'benî' 1. kelime, 19. kelime)")
T[27] = ("'yeftinennekumu' 3MS (fiil uyumu; 4. kelime — fail 5. kelime); muhatap 2MP eki (adsız; 'yeftinennekumu', 'ebeveykum', 'yerâkum' — 4., 8. ve 17. kelime); 'axrace', 'yenzi'u', 'yerâkum' 3MS (adsız; gönderge 'ş-şeytânu' 5. kelime — 7., 11. ve 17. kelime); "
         "''anhumâ', 'libâsehumâ', 'li-yuriyehumâ', 'sev'âtihimâ' 3D eki (adsız; gönderge 'ebeveykum' 8. kelime — 12., 13., 14. ve 15. kelime); 'li-yuriyehumâ' 3MS (adsız; edilgen, naib-i faili zamir; morph PASS etiketi, okuma etken; gönderge 'ş-şeytânu' 5. kelime, 14. kelime); "
         "'innehû', 've qabîluhû' 3MS eki (adsız; gönderge 'ş-şeytânu' 5. kelime — 16. ve 19. kelime); 'huve' 3MS (adsız; gönderge 'ş-şeytânu' 5. kelime, 18. kelime); muhatap 2MP (adsız; 'teravnehum' — 23. kelime); "
         "'teravnehum' 3MP eki (adsız; gönderge 've qabîluhû' 19. kelime, 23. kelime); konuşan 1P eki (adsız; 'innâ' — 24. kelime); konuşan 1P (adsız; 'ce'alne' — 25. kelime); 'yu'minûn' 3MP (adsız; gönderge 'lillezîne' 28. kelime, 30. kelime)")

D = {}
D[26] = ("◇ 'yâ benî âdeme qad enzelnâ 'aleykum libâsen yuvârî sev'âtikum ve rîşen ve libâsu't-taqvâ zâlike xayrun zâlike min âyâti'llâhi le'allehum yezzekkerûn' — "
 "'yâ' + çoğul 'bunayy' + özel ad 'âdem' + 'qad' + PERF 1P IV. bab + ''alâ' + 2MP + nekre 'libâs' + IMPF 3MS III. bab + çoğul 'sev'e' + 2MP + 've' + nekre 'rîş' + 've' + 'libâs' + belirli 'taqvâ' + 'zâ' + nekre 'xayr' + 'zâ' + 'min' + çoğul 'âye' + 'allâh' + 'le'alle' + 3MP + IMPF 3MP V. bab "
 "(ölçüm edim nida, kip CERT 1 · VOC 1; 1P 2 · 2MP 2 · 3MP 3 · 3MS 1; bab III. bab ×1 · IV. bab ×1 · V. bab ×1). "
 "Allah lafzı 17. sırada (ölçüm allah z=0,52); Rab yok; esmâ yok (ölçüm); ölçüm '{{1|" + _AK1 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{1|yıldız ★★★}}' — satır aynen (kaynak hapaks, z=3,28); ölçüm '{{1|" + _HP + "}}' — satır aynen (yeni kök karşılığı 'süs'); n=19 (n z=0,70); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:25 ن → 7:26 ن); "
 "ölçüm '{{1|simetri \\[3, 3, 12, 1\\]}}' — satır aynen; ölçüm '{{1|harf 87 → harf3 82, isaret 5}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (3. kelime); VOC 1: 'yâ' (1. kelime); "
 "'ve rîşen' (9.) kelimesindeki 've' CONJ; 've libâsu' (10.) kelimesindeki 've' REM; 'zâlike' (12. ve 14.) DEM + DIST + ADDR; 'le'allehum' (18.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) لبس ×2 ('libâsen' 6. / 've libâsu' 10. kelime) (okuma). "
 + T[26] + " (okuma). "
 + cumle(say('say 7:26 1-2', "yâ benî âdeme", True), say('dizi 7 26 1 2', "bunayy âdem")) + ' '
 + cumle(say('say 7:26 3-9', "qad enzelnâ 'aleykum libâsen yuvârî sev'âtikum ve rîşen", True), say('say 7:26 10-13', "ve libâsu't-taqvâ zâlike xayrun")) + ' '
 + cumle(say('say 7:26 14-17', "zâlike min âyâti'llâhi", True), say('say 7:26 18-19', "le'allehum yezzekkerûn"), say('say 7:26 1-19', "yâ benî âdeme qad enzelnâ 'aleykum libâsen yuvârî sev'âtikum ve rîşen ve libâsu't-taqvâ zâlike xayrun zâlike min âyâti'llâhi le'allehum yezzekkerûn")) + ' '
 + say('say 7:26 16-17 --on', "âyâti'llâhi", True) + " (--medde 42 ayet: 'âyâti' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). " +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'yâ' + izafet + özel ad + 'qad' + PERF + ''alâ' + nekre + IMPF + izafet + 've' + nekre + 've' + izafet + belirli + 'zâ' + nekre + 'zâ' + 'min' + izafet + lafız + 'le'alle' + IMPF; "
 "D2 nida; CERT ('qad' 3. kelime), VOC ('yâ' 1. kelime); D3 لبس ×2; D4 1P 2 · 2MP 2 · 3MP 3 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[26] + "; aktör adlı 'âdeme' (2. kelime; ölçüm rol mecrur); A2 Âdemoğullarına çirkin yerleri gizleyen giysi ve süs indirilmesi; sakınma giysisinin daha hayırlı oluşu; bunun Allah'ın âyetlerinden oluşu; "
 "A3 —; "
 "A4 " + BOLUM + "; bölüm açılışı; nidâ ('yâ benî âdeme' 1. kelime); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi haber → nida (ayetler arası).",
)

D[27] = ("◇ 'yâ benî âdeme lâ yeftinennekumu'ş-şeytânu kemâ axrace ebeveykum mine'l-cenneti yenzi'u 'anhumâ libâsehumâ li-yuriyehumâ sev'âtihimâ innehû yerâkum huve ve qabîluhû min haysu lâ teravnehum innâ ce'alne'ş-şeyâtîne evliyâ'e lillezîne lâ yu'minûn' — "
 "'yâ' + çoğul 'bunayy' + özel ad 'âdem' + 'lâ' + IMPF 3MS I. bab + 'n' + 2MP + belirli 'şeytân' + 'ke' + 'mâ' + PERF 3MS IV. bab + ikil 'ebevân' + 2MP + 'min' + belirli 'cenne' + IMPF 3MS I. bab + ''an' + 3D + 'libâs' + 3D + 'li' + IMPF 3MS IV. bab edilgen + 3D + çoğul 'sev'e' + 3D + "
 "'inne' + 3MS + IMPF 3MS I. bab + 2MP + 'huve' + 've' + 'qabîl' + 3MS + 'min' + 'haysu' + 'lâ' + IMPF 2MP I. bab + 3MP + 'inne' + 1P + PERF 1P I. bab + belirli çoğul 'şeytân' + çoğul 'velî' + 'li' + 'ellezî' + 'lâ' + IMPF 3MP IV. bab "
 "(ölçüm edim nida, kip EMPH 1 · NEG 3 · VOC 1; 1P 3 · 2MP 5 · 3D 4 · 3MP 3 · 3MS 8; bab I. bab ×5 · IV. bab ×3). "
 "Allah lafzı yok; Rab yok; ölçüm '{{2|" + _ES2 + "}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'innâ ce'alne'ş-şeyâtîne evliyâ'e lillezîne lâ yu'minûn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (inanmayanların dostu kılınan şeytanlar) (okuma); ölçüm '{{2|" + _AK2 + "}}' — satır aynen. "
 "Ölçüm '{{2|yıldız ★}}' — satır aynen (kaynak n, z=1,87); n=30 (n z=1,87); ölçüm '{{2|EDİLGEN 1/8 fiil, pas z=0,38}}' — satır aynen; ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:26 ن → 7:27 ن); "
 "ölçüm '{{2|simetri \\[4, 16, 22, 1\\]}}' — satır aynen; ölçüm '{{2|harf 140 → harf3 136, isaret 4}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm EMPH 1: 'yeftinennekumu' (4. kelime; 'n'); NEG 3: 'lâ' (3. kelime), 'lâ' (22. kelime), 'lâ' (29. kelime); VOC 1: 'yâ' (1. kelime); "
 "'kemâ' (6.) P + SUB; 'li-yuriyehumâ' (14.) kelimesindeki 'li' PRP; 'innehû' (16.) ACC; 've qabîluhû' (19.) kelimesindeki 've' CONJ; 'innâ' (24.) ACC; 'lillezîne' (28.) P + REL (okuma). "
 "'li-yuriyehumâ' (14.) kelimesinin morph etiketi PASS (ölçüm EDİLGEN sayımı bu kelimeden); okuma IV. bab etken, fail şeytan, 'sev'âtihimâ' (15.) meful — etiket dizisinde ve A1'de morph etiketi korundu (okuma). "
 "Kök ikilemesi (ölçüm) رأي ×3 ('li-yuriyehumâ' 14. / 'yerâkum' 17. / 'teravnehum' 23. kelime); شطن ×2 ('ş-şeytânu' 5. / 'ş-şeyâtîne' 26. kelime) (okuma). "
 + T[27] + " (okuma). "
 + cumle(say('say 7:27 1-2', "yâ benî âdeme", True), say('dizi 7 27 1 2', "bunayy âdem"), say('say 7:27 3-5', "lâ yeftinennekumu'ş-şeytânu"), say('say 7:27 6-10', "kemâ axrace ebeveykum mine'l-cenneti"), say('say 7:27 11-15', "yenzi'u 'anhumâ libâsehumâ li-yuriyehumâ sev'âtihimâ")) + ' '
 + cumle(say('say 7:27 16-23', "innehû yerâkum huve ve qabîluhû min haysu lâ teravnehum", True), say('say 7:27 20-22', "min haysu lâ"), say('dizi 7 27 20 22', "min haysu lâ")) + ' '
 + cumle(say('say 7:27 24-30', "innâ ce'alne'ş-şeyâtîne evliyâ'e lillezîne lâ yu'minûn", True), say('say 7:27 28-30', "lillezîne lâ yu'minûn"), say('say 7:27 1-30', "yâ benî âdeme lâ yeftinennekumu'ş-şeytânu kemâ axrace ebeveykum mine'l-cenneti yenzi'u 'anhumâ libâsehumâ li-yuriyehumâ sev'âtihimâ innehû yerâkum huve ve qabîluhû min haysu lâ teravnehum innâ ce'alne'ş-şeyâtîne evliyâ'e lillezîne lâ yu'minûn")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'min haysu lâ' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'yerâkum' / 'lâ teravnehum' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'yâ' + izafet + özel ad + 'lâ' + IMPF + 'n' + belirli + 'ke' + 'mâ' + PERF + izafet + 'min' + belirli + IMPF + ''an' + izafet + 'li' + IMPF + izafet + 'inne' + IMPF + 'huve' + 've' + izafet + 'min' + 'haysu' + 'lâ' + IMPF + 'inne' + PERF + belirli + 'velî' + 'li' + 'ellezî' + 'lâ' + IMPF; "
 "D2 nida; EMPH ('yeftinennekumu' 4. kelime), NEG ('lâ' 3. kelime, 'lâ' 22. kelime, 'lâ' 29. kelime), VOC ('yâ' 1. kelime); D3 رأي ×3, شطن ×2; D4 1P 3 · 2MP 5 · 3D 4 · 3MP 3 · 3MS 8, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[27] + "; aktör adlı 'âdeme' (2. kelime; ölçüm rol mecrur), 'ş-şeytânu' (5. kelime; ölçüm rol fail+meful — 'yeftinennekumu' faili), 'l-cenneti' (10. kelime; ölçüm rol mecrur), 'ş-şeyâtîne' (26. kelime; ölçüm rol fail+meful — 'ce'alne' mefulü); "
 "A2 şeytanın fitnesine karşı uyarı; ana babanın giysileri çekilip alınarak bahçeden çıkarılışı; şeytan ve topluluğunun görülmeden görmesi; şeytanların inanmayanların dostu oluşu; "
 "A3 —; "
 "A4 " + BOLUM + "; nidâ ('yâ benî âdeme' 1. kelime); şahıs geçişi yok (ayetler arası); edim geçişi yok (ayetler arası).",
)
out = ['# ── blok 7:26-27 (2026-11-25) ──', 'MEAL7 = {']
for n in range(26, 28):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M7 = {']
for n in range(26, 28):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL7); M.update(M7)']
open('/home/claude/yamalar/metin_7_26_27.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
