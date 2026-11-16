# blok 9 (5:24-26) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b09/say2.txt'
os.environ['OLC'] = '/home/claude/b09/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Mûsâ ve kavmi: kutsal topraklar; kırk yıl' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 24: "Dediler ki: 'Ey Mûsâ! Onlar orada bulundukça biz oraya ebediyen asla girmeyeceğiz. Sen ve Rabbin gidin, savaşın; biz burada oturanlarız.'",
 25: "Dedi ki: 'Rabbim! Ben ancak kendime ve kardeşime güç yetirebilirim; artık bizimle fâsıklar kavmi arasını ayır.'",
 26: "Dedi ki: 'Öyleyse orası onlara kırk yıl haram kılınmıştır; yeryüzünde şaşkın şaşkın dolaşacaklar. Artık fâsıklar kavmi için üzülme.'",
}

T24 = ("'qâlû' faili 3MP (adsız; 1. kelime — gönderge kavim); Mûsâ (adlı kişi; nidâ, 2. kelime — ölçüm aktör); söz içi konuşan 1P (adsız; 'innâ', 'nedxulehâ', 14. kelime 'innâ'); 'nedxulehâ' ve 'fîhâ' 3FS (gönderge kutsal toprak); 'dâmû' faili 3MP (adsız; gönderge zorba kavim); "
       "muhatap 2MS (söz içi, adsız; 'zheb', 'ente' — gönderge Mûsâ); 'rabbuke' (Rab; 12. kelime — 'qâtilâ' ikil failinin bir yanı); 'qâtilâ' faili 2MD (söz içi, adsız; Mûsâ ve Rab); 'qâ'idûn' (haber; çoğul, 16. kelime)")
T25 = ("'qâle' faili 3MS (adsız; 1. kelime — gönderge Mûsâ); 'rabbi' (Rab; nidâ, 2. kelime); söz içi konuşan 1S (adsız; 'innî', 'emliku', 'nefsî', 'exî'); 'exî' (kardeş; 8. kelime); muhatap 2MS (söz içi, adsız; 'fruq' — gönderge Rab); söz içi 1P (adsız; 'beynenâ'); "
       "'l-qavmi'l-fâsiqîn' (belirli; 12-13. kelime)")
T26 = ("'qâle' faili 3MS (adsız; 1. kelime — gönderge Rab); 'innehâ' 3FS (gönderge kutsal toprak); ''aleyhim' 3MP (adsız; gönderge kavim); 'yetîhûne' faili 3MP (adsız); muhatap 2MS (söz içi, adsız; 'te'se' — gönderge Mûsâ); 'l-qavmi'l-fâsiqîn' (belirli; 13-14. kelime)")

D = {}
D[24] = ("◇ 'qâlû yâ mûsâ innâ len nedxulehâ ebeden mâ dâmû fîhâ fe'zheb ente ve rabbuke fe-qâtilâ innâ hâhunâ qâ'idûn' — "
 "PERF 3MP I. bab + 'yâ' + özel ad 'mûsâ' + 'inne' + 1P + 'len' + IMPF 1P I. bab + 3FS + zarf 'ebeden' + 'mâ' + PERF 3MP I. bab + 'fî' + 3FS + 'fe' + IMPV 2MS I. bab + 'ente' + 've' + 'rabb' + 2MS + 'fe' + IMPV 2MD III. bab + 'inne' + 1P + 'hâ' + 'hunâ' + çoğul etken ortaç 'qâ'id' "
 "(ölçüm edim emir, nida, kip IMPV 2 · NEG 1 · VOC 1, biçim DIKKAT; 1P 3 · 2D 1 · 2MD 1 · 2MS 3 · 3FS 2 · 3MP 4; bab I. bab ×4 · III. bab ×1). "
 "Lafız yok; ölçüm '{{1|رَبّ 12\\. sırada \\(rab z=1,01\\)}}' — satır aynen; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor; sınıf R/R); ölçüm '{{1|aktör: adlı مُوسَى 2\\. sırada \\(kisi, rol fail\\+muhatap\\)}}' — satır aynen. "
 "Ölçüm '{{1|yıldız yok}}' — satır aynen; n=16 (n z=0,38); ölçüm '{{1|biçim DIKKAT}}' — satır aynen; ölçüm '{{1|fâsıla قعدون → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|simetri \\[3, 2, 7, 1\\]}}' — satır aynen; ölçüm '{{1|harf 69 → harf3 65, isaret 4}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 2: 'zheb' (10. kelime), 'qâtilâ' (13. kelime); NEG 1: 'len' (4. kelime); VOC 1: 'yâ' (2. kelime) (okuma); ölçüm biçim DIKKAT — 'yâ mûsâ' nidâsı ve 'hâhunâ' (15. kelime, morph ATT); D2'de yazılmadı (okuma); 'mâ' (7. kelime) morph SUB — süre (okuma). "
 "'fe'zheb' (10.)'deki 'fe' morph REM; 've rabbuke' (12.)'deki 've' CONJ; 'fe-qâtilâ' (13.)'daki 'fe' CONJ (okuma). "
 + T24 + " (okuma). "
 + cumle(say('say 5:24 1-2', "qâlû yâ mûsâ", True), say('say 5:24 3-5', "innâ len nedxulehâ"), say('dizi 5 24 3 5', "inne len dexale"), say('say 5:24 3-6', "innâ len nedxulehâ ebeden"), say('say 5:24 7-9', "mâ dâmû fîhâ")) + ' '
 + cumle(say('say 5:24 10-13 --on', "fe'zheb ente ve rabbuke fe-qâtilâ", True), say('say 5:24 10-12 --on', "fe'zheb ente ve rabbuke"), say('say 5:24 14-16', "innâ hâhunâ qâ'idûn"), say('lem 5:24:16', "qâ'id")) + ' '
 "Ölçüm xref yok. Ölçüm nakarat3 bir kalıp: süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'fe'zheb ente ve rabbuke fe-qâtilâ' / 'innâ hâhunâ qâ'idûn' — ayetler arası: 5:23 / 5:24 (5:23 9. kelimedeki giriş emri / 'len nedxulehâ ebeden').",
 "◈K — K2 'ebeden' (6. kelime).",
 "◈B — —",
 "◈D — D1 PERF + 'yâ' + özel ad + 'inne' + 'len' + IMPF + zarf + 'mâ' + PERF + 'fî' + 'fe' + IMPV + 'ente' + 've' + izafet + 'fe' + IMPV + 'inne' + 'hâ' + 'hunâ' + çoğul; "
 "D2 emir, nida, IMPV ('zheb' 10. kelime, 'qâtilâ' 13. kelime), NEG ('len' 4. kelime), VOC ('yâ' 2. kelime); D3 kök ikilemesi yok; 9:86 eşi; 5:22 sûre içi eşi; D4 1P 3 · 2D 1 · 2MD 1 · 2MS 3 · 3FS 2 · 3MP 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T24 + "; A2 girmeme; süreklilik; gitme; savaşma; oturma; A3 'yâ mûsâ' ile açılan söz (2-16. kelime); A4 " + BOLUM + "; edim geçişi emir, şart → emir, nida (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası); söz açılır (2. kelime); söz kapanır (16. kelime, ayet içi).",
)

D[25] = ("◇ 'qâle rabbi innî lâ emliku illâ nefsî ve exî fe'fruq beynenâ ve beyne'l-qavmi'l-fâsiqîn' — "
 "PERF 3MS I. bab + 'rabb' + 1S + 'inne' + 1S + 'lâ' + IMPF 1S I. bab + 'illâ' + 'nefs' + 1S + 've' + 'ex' + 1S + 'fe' + IMPV 2MS I. bab + 'beyn' + 1P + 've' + 'beyn' + belirli 'qavm' + belirli çoğul etken ortaç 'fâsiq' "
 "(ölçüm edim emir, kip IMPV 1 · NEG 1, biçim ISTISNA; 1P 1 · 1S 5 · 2MS 1 · 3MS 1; bab I. bab ×3). "
 "Lafız yok; ölçüm '{{2|رَبّ 2\\. sırada \\(rab z=1,32\\)}}' — satır aynen; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor; sınıf R/R). "
 "Ölçüm '{{2|yıldız yok}}' — satır aynen; n=13 (n z=0,06); ölçüm '{{2|biçim ISTISNA}}' — satır aynen; ölçüm '{{2|fâsıla ٱلفسقين → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|harf 52 → harf3 51, isaret 1}}' — satır aynen; ölçüm '{{2|dış düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 1: 'fruq' (9. kelime); NEG 1: 'lâ' (4. kelime) (okuma); ölçüm biçim ISTISNA — 'illâ' (6. kelime, morph EXP); D2'de yazılmadı (okuma). "
 "Kök ikilemeleri (ölçüm) بين ×2: 'beynenâ' (10. kelime) / 've beyne' (11. kelime) (okuma). "
 "'ve exî' (8.) ve 've beyne' (11.)'deki 've' morph CONJ; 'fe'fruq' (9.)'taki 'fe' SUP (okuma). "
 + T25 + " (okuma). "
 + cumle(say('say 5:25 1-2', "qâle rabbi", True), say('say 5:25 3-7', "innî lâ emliku illâ nefsî"), say('say 5:25 4-5', "lâ emliku"), say('say 5:25 8-8 --on', "ve exî")) + ' '
 + cumle(say('say 5:25 9-13 --on', "fe'fruq beynenâ ve beyne'l-qavmi'l-fâsiqîn", True), say('say 5:25 10-13', "beynenâ ve beyne'l-qavmi'l-fâsiqîn"), say('say 5:25 12-13', "l-qavmi'l-fâsiqîn")) + ' '
 "Ölçüm xref okunmamış bir ayet. Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'nefsî ve exî' / 'l-qavmi'l-fâsiqîn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + izafet + 'inne' + 'lâ' + IMPF + 'illâ' + izafet + 've' + izafet + 'fe' + IMPV + izafet + 've' + 'beyn' + belirli + belirli; "
 "D2 emir, IMPV ('fruq' 9. kelime), NEG ('lâ' 4. kelime); D3 بين ×2; 10:49, 28:34 ve 61:5 eşleri; 5:26 blok içi eşi; D4 1P 1 · 1S 5 · 2MS 1 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T25 + "; aktör yok (ölçüm); A2 güç yetirme; kendisi; kardeş; ayırma; fâsıklık; A3 'rabbi' ile açılan söz (2-13. kelime; dua); A4 " + BOLUM + "; edim geçişi emir, nida → emir (ayetler arası); şahıs geçişi 3 → 1 (ayetler arası); söz açılır (2. kelime); söz kapanır (13. kelime, ayet içi).",
)

D[26] = ("◇ 'qâle fe-innehâ muharrametun 'aleyhim erba'îne seneten yetîhûne fi'l-ard fe-lâ te'se 'ale'l-qavmi'l-fâsiqîn' — "
 "PERF 3MS I. bab + 'fe' + 'inne' + 3FS + nekre edilgen ortaç 'muharrame' + ''alâ' + 3MP + sayı 'erba'' + nekre 'sene' + IMPF 3MP I. bab + 'fî' + belirli 'ard' + 'fe' + 'lâ' + IMPF 2MS I. bab + ''alâ' + belirli 'qavm' + belirli çoğul etken ortaç 'fâsiq' "
 "(ölçüm edim haber, kip NEG 1; 2MS 1 · 3FS 1 · 3MP 3 · 3MS 1; bab I. bab ×3). "
 "Ölçüm '{{3|lafız YOK · Rab YOK}}' — satır aynen; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=14 (n z=0,17); ölçüm '{{3|HAPAKS: تيه}}' — satır aynen (kök bu blokta tabloya eklendi); ölçüm '{{3|hapaks z=3,28}}' — satır aynen; ölçüm '{{3|sayı işareti أَرْبَع}}' — satır aynen; ölçüm '{{3|fâsıla ٱلفسقين → ن, N sınıfı}}' — satır aynen; "
 "ölçüm '{{3|simetri \\[3, 2, 8, 1\\]}}' — satır aynen; ölçüm '{{3|harf 65 → harf3 61, isaret 4}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 1: 'lâ' (10. kelime; yasak anlamlı, cezm) (okuma); 'erba'îne' (5. kelime) morph T — süre (okuma). "
 "'fe-innehâ' (2.) ve 'fe-lâ' (10.)'daki 'fe' morph SUP (okuma). "
 + T26 + " (okuma). "
 + cumle(say('say 5:26 1-4', "qâle fe-innehâ muharrametun 'aleyhim", True), say('say 5:26 2-4 --on', "fe-innehâ muharrametun 'aleyhim"), say('say 5:26 5-6', "erba'îne sene"), say('say 5:26 7-9', "yetîhûne fi'l-ard"), say('lem 5:26:7', "yetîhu")) + ' '
 + cumle(say('say 5:26 10-13 --on', "fe-lâ te'se 'ale'l-qavm", True), say('dizi 5 26 10 13', "lâ te'se 'alâ qavm"), say('say 5:26 10-14 --on', "fe-lâ te'se 'ale'l-qavmi'l-fâsiqîn"), say('say 5:26 12-14', "'ale'l-qavmi'l-fâsiqîn")) + ' '
 "Ölçüm xref yok. Ölçüm nakarat3 bir kalıp: süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: 5:25 / 5:26 ('fe'fruq beynenâ' / 'fe-lâ te'se').",
 "◈K — K1 'l-ard' (9. kelime); K2 'seneten' (6. kelime).",
 "◈B — —",
 "◈D — D1 PERF + 'fe' + 'inne' + nekre + ''alâ' + sayı + nekre + IMPF + 'fî' + belirli + 'fe' + 'lâ' + IMPF + ''alâ' + belirli + belirli; "
 "D2 haber, NEG ('lâ' 10. kelime); D3 kök ikilemesi yok; 46:15 eşi; 5:25 blok içi eşi; D4 2MS 1 · 3FS 1 · 3MP 3 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T26 + "; aktör yok (ölçüm); A2 haram kılma; kırk yıl; şaşkın dolaşma; üzülme; fâsıklık; A3 'fe-innehâ' ile açılan söz (2-14. kelime); A4 " + BOLUM + "; edim geçişi emir → haber (ayetler arası); şahıs geçişi 1 → 3 (ayetler arası); söz açılır (2. kelime); söz kapanır (14. kelime, ayet içi); bölüm kapanışı.",
)

out = ['# ── blok 5:24-26 (2026-11-15) ──', 'MEAL9 = {']
for n in range(24, 27):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M9 = {']
for n in range(24, 27):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL9); M.update(M9)']
open('/home/claude/yamalar/metin_5_24_26.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
