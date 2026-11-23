# sûre 6 blok 31 (6:131-135) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b31/say2.txt'
os.environ['OLC'] = '/home/claude/b31/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Ölüyken dirilen; cin ve insan toplulukları' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 131: "Bu, halkı gafilken Rabbinin şehirleri zulümle helâk edici olmaması dolayısıyladır.",
 132: "Herkes için yaptıklarından dereceler vardır. Rabbin, yaptıklarından gafil değildir.",
 133: "Rabbin ganîdir, rahmet sahibidir. Dilerse sizi giderir ve sizi başka bir kavmin soyundan inşâ ettiği gibi sizden sonra dilediğini halef kılar.",
 134: "Size vaat edilen şüphesiz gelecektir ve siz âciz bırakanlar değilsiniz.",
 135: "De ki: Ey kavmim, konumunuza göre yapın, şüphesiz ben de yapanım. Yurdun sonunun kimin olacağını yakında bileceksiniz. Şüphesiz zalimler kurtuluşa eremez.",
}

T = {}
T[131] = ("muhatap 2MS (adsız; 'rabbuke' eki — 5. kelime); 'yekun' 3MS (fiil uyumu; 4. kelime — fail 5. kelime); "
          "'ehluhâ' eki 3FS (adsız; gönderge 'l-qurâ' 7. kelime, 9. kelime)")
T[132] = ("''amilû', 'ya'melûn' 3MP (adsız; gönderge 'li-kullin' 1. kelime — 4. ve 9. kelime); muhatap 2MS (adsız; 'rabbuke' eki — 6. kelime)")
T[133] = ("muhatap 2MS (adsız; 'rabbuke' eki — 1. kelime); 'yuzhibkum', 've yestaxlif', 'yeşâ'u', 'enşe'ekum' 3MS (adsız; gönderge 'rabbuke' 1. kelime — 7., 8., 12. ve 14. kelime); şart fiili 3MS (adsız; gönderge 'rabbuke' 1. kelime, 6. kelime); "
          "muhatap 2MP (adsız; 'yuzhibkum', 'ba'dikum', 'enşe'ekum' ekleri — 7., 10. ve 14. kelime)")
T[134] = ("muhatap 2MP (adsız; edilgen; 'tû'adûne' — 3. kelime — naib-i faili muhatap 2MP; 'entum' — 6. kelime)")
T[135] = ("muhatap 2MS (adsız; 'qul' — 1. kelime); konuşan 1S (adsız; söz içi; 'yâ qavmi', 'innî' — 2. ve 6. kelime); "
          "muhatap 2MP (adsız; söz içi; ''melû', 'mekânetikum', 'ta'lemûne' — 3., 5. ve 9. kelime); 'tekûnu' 3FS (fiil uyumu; söz içi; 11. kelime — fail 13. kelime); "
          "'lehû' 3MS (adsız; söz içi; gönderge 'men' 10. kelime, 12. kelime); 'innehû' 3MS (adsız; söz içi; zamir-i şan, 15. kelime); 'yuflihu' 3MS (fiil uyumu; söz içi; 17. kelime — fail 18. kelime)")

D = {}
D[131] = ("◇ 'zâlike en lem yekun rabbuke muhlike'l-qurâ bi-zulmin ve ehluhâ ğâfilûn' — "
 "'zâlike' + 'en' + 'lem' + IMPF 3MS I. bab + 'rabb' + 2MS + etken ortaç 'muhlik' + belirli çoğul 'qarye' + 'bi' + nekre 'zulm' + 've' + 'ehl' + 3FS + çoğul etken ortaç 'ğâfil' "
 "(ölçüm edim haber, kip NEG 1; 2MS 1 · 3FS 1 · 3MS 1; bab I. bab ×1). "
 "Allah lafzı yok; Rab 5. sırada (ölçüm rab z=1,81); esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); "
 "ölçüm '{{1|aktör: adsız `karye` 7\\. sırada}}' — satır aynen; aktör adsız 'l-qurâ' 7. sırada — helâk edilen şehirler (okuma). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=10 (n z=-0,26); ölçüm '{{1|fâsıla غفلون → ن, N sınıfı}}' — satır aynen (6:130 ن → 6:131 ن); "
 "ölçüm '{{1|harf 38 → harf3 37, isaret 1}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen. "
 "Ölçüm NEG 1: 'lem' (3. kelime); 've ehluhâ' (9.) kelimesindeki 've' CIRC — hâl (okuma). "
 + T[131] + " (okuma). "
 + cumle(say('say 6:131 5-6', 'rabbuke muhlike', True), say('dizi 6 131 4 7', 'kâne rabb muhlik qarye')) + ' '
 + cumle(say('say 6:131 7-8', "l-qurâ bi-zulm", True)) + ' ' +
 "Ölçüm xref 28:59 (emsal olarak basıldı), 11:117 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'zâlike' + 'en' + 'lem' + IMPF + izafet + 'muhlik' + belirli + 'bi' + nekre + 've' + izafet + 'ğâfil'; "
 "D2 haber; NEG ('lem' 3. kelime); D3 28:59 eşi, 11:117 eşi; D4 2MS 1 · 3FS 1 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[131] + "; aktör adsız 'l-qurâ' (7. kelime; ölçüm); A2 Rabbin, halkı gafilken şehirleri zulümle helâk etmemesi; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi soru, nida → haber (ayetler arası).",
)

D[132] = ("◇ 've li-kullin derecâtun mimmâ 'amilû, ve mâ rabbuke bi-ğâfilin 'ammâ ya'melûn' — "
 "'ve' + 'li' + nekre 'kull' + nekre çoğul 'derece' + 'min' + 'mâ' + PERF 3MP I. bab + 3MP + 've' + 'mâ' + 'rabb' + 2MS + 'bi' + nekre etken ortaç 'ğâfil' + ''an' + 'mâ' + IMPF 3MP I. bab + 3MP "
 "(ölçüm edim haber, kip NEG 1; 2MS 1 · 3MP 4; bab I. bab ×2). "
 "Allah lafzı yok; Rab 6. sırada (ölçüm rab z=2,05); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=9 (n z=-0,36); ölçüm '{{2|fâsıla يعملون → ن, N sınıfı}}' — satır aynen (6:131 ن → 6:132 ن); "
 "ölçüm '{{2|harf 39 → harf3 35, isaret 4}}' — satır aynen; ölçüm '{{2|dış düğüm 3}}' — satır aynen. "
 "Ölçüm NEG 1: 'mâ' (5. kelime); 've li-kullin' (1.) kelimesindeki 've' REM, 've mâ' (5.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) عمل ×2 (''amilû' 4. / 'ya'melûn' 9. kelime) (okuma). "
 + T[132] + " (okuma). "
 + cumle(say('say 6:132 1-2', 've li-kullin derecât', True)) + ' '
 + cumle(say('say 6:132 6-7', 'rabbuke bi-ğâfil', True)) + ' ' +
 "Ölçüm xref 46:19 (emsal olarak basıldı), 11:123 (emsal olarak basıldı), 27:93 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'li' + nekre + nekre + 'min' + 'mâ' + PERF + 've' + 'mâ' + izafet + 'bi' + nekre + ''an' + 'mâ' + IMPF; "
 "D2 haber; NEG ('mâ' 5. kelime); D3 عمل ×2; 46:19 eşi, 11:123 eşi, 27:93 eşi; D4 2MS 1 · 3MP 4, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[132] + "; aktör yok (ölçüm); A2 herkes için yaptıklarından dereceler; Rabbin yaptıklarından gafil olmaması; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[133] = ("◇ 've rabbuke'l-ğaniyyu zu'r-rahmeh, in yeşe' yuzhibkum ve yestaxlif min ba'dikum mâ yeşâ'u kemâ enşe'ekum min zurriyyeti qavmin âxarîn' — "
 "'ve' + 'rabb' + 2MS + belirli 'ğaniyy' + 'zû' + belirli 'rahme' + 'in' + IMPF 3MS I. bab + IMPF 3MS IV. bab + 2MP + 've' + IMPF 3MS X. bab + 'min' + 'ba'd' + 2MP + 'mâ' + IMPF 3MS I. bab + 'ke' + 'mâ' + PERF 3MS IV. bab + 2MP + 'min' + 'zurriyye' + nekre 'qavm' + çoğul 'âxar' "
 "(ölçüm edim şart, kip COND 1; 2MP 3 · 2MS 1 · 3MS 5; bab I. bab ×2 · IV. bab ×2 · X. bab ×1). "
 "Allah lafzı yok; Rab 1. sırada (ölçüm rab z=0,86); ölçüm '{{3|esmâ غَنِيّ 2\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' — ölçüm MÜHÜRSÜZ ile uyuşuyor (muhur_el hayır); "
 "esma_el kaydı 'ilahi' — 've rabbuke'l-ğaniyyu', kural ''ve'llâhu X' kuralı → ilahi' (Rab; 've rabbuke X' kalıbı) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=18 (n z=0,59); ölçüm '{{3|fâsıla ءاخرين → ن, N sınıfı}}' — satır aynen (6:132 ن → 6:133 ن); "
 "ölçüm '{{3|simetri \\[4, 3, 9, 1\\]}}' — satır aynen; ölçüm '{{3|harf 74 → harf3 72, isaret 2}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm COND 1: 'in' (5. kelime); 've rabbuke' (1.) ve 've yestaxlif' (8.) kelimelerindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) شيأ ×2 ('yeşe'' 6. / 'yeşâ'u' 12. kelime) (okuma). "
 + T[133] + " (okuma). "
 + cumle(say('say 6:133 5-6', "in yeşe'", True)) + ' '
 + cumle(say('say 6:133 11-12', "mâ yeşâ'u", True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + izafet + belirli + 'zû' + belirli + 'in' + IMPF + IMPF + 've' + IMPF + 'min' + izafet + 'mâ' + IMPF + 'ke' + 'mâ' + PERF + 'min' + 'zurriyye' + nekre + 'âxar'; "
 "D2 şart; COND ('in' 5. kelime); D3 شيأ ×2; D4 2MP 3 · 2MS 1 · 3MS 5, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[133] + "; aktör yok (ölçüm); A2 Rabbin ganî ve rahmet sahibi oluşu; dilerse muhatapları giderip yerlerine dilediğini halef kılması; başka bir kavmin soyundan inşâ edilişleri; "
 "A3 —; "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'in' 5. kelime: 'in' / 'yuzhibkum' (7. kelime)); şahıs geçişi yok (ayetler arası); edim geçişi haber → şart (ayetler arası).",
)

D[134] = ("◇ 'inne mâ tû'adûne le-ât, ve mâ entum bi-mu'cizîn' — "
 "'inne' + 'mâ' + edilgen IMPF 2MP I. bab + 2MP + 'le' + nekre etken ortaç 'âtî' + 've' + 'mâ' + 'entum' + 'bi' + çoğul etken ortaç 'mu'ciz' "
 "(ölçüm edim haber, kip EMPH 1 · NEG 1; 2MP 3; bab I. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=7 (n z=-0,58); ölçüm '{{4|EDİLGEN 1/1 fiil, pas z=5,38}}' — satır aynen; ölçüm '{{4|fâsıla بمعجزين → ن, N sınıfı}}' — satır aynen (6:133 ن → 6:134 ن); "
 "ölçüm '{{4|simetri \\[3, 1, 5, 1\\]}}' — satır aynen; ölçüm '{{4|harf 30 → harf3 28, isaret 2}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm EMPH 1: 'le-ât' (4. kelime); NEG 1: 'mâ' (5. kelime); 've mâ' (5.) kelimesindeki 've' REM; 'inne' (1.) ACC (okuma). "
 + T[134] + " (okuma). "
 + cumle(say('say 6:134 1-3', "inne mâ tû'adûne", True)) + ' '
 + cumle(say('say 6:134 5-7', "ve mâ entum bi-mu'cizîn", True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'inne' + 'mâ' + IMPF + 'le' + nekre + 've' + 'mâ' + 'entum' + 'bi' + 'mu'ciz'; "
 "D2 haber; EMPH ('le-ât' 4. kelime), NEG ('mâ' 5. kelime); D3 —; D4 2MP 3, sahset ['2'], iltifât 0.",
 "◈A — A1 " + T[134] + "; aktör yok (ölçüm); A2 vaat edilenin mutlaka gelişi; muhatapların âciz bırakamayışı; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 2 (ayetler arası); edim geçişi şart → haber (ayetler arası).",
)

D[135] = ("◇ 'qul yâ qavmi 'melû 'alâ mekânetikum innî 'âmil, fe-sevfe ta'lemûne men tekûnu lehû 'âqibetu'd-dâr, innehû lâ yuflihu'z-zâlimûn' — "
 "IMPV 2MS I. bab + 'yâ' + 'qavm' + 1S + IMPV 2MP I. bab + 2MP + ''alâ' + 'mekâne' + 2MP + 'inne' + 1S + nekre etken ortaç ''âmil' + 'fe' + 'sevfe' + IMPF 2MP I. bab + 2MP + 'men' + IMPF 3FS I. bab + 'li' + 3MS + ''âqibe' + belirli 'dâr' + 'inne' + 3MS + 'lâ' + IMPF 3MS IV. bab + belirli çoğul etken ortaç 'zâlim' "
 "(ölçüm edim emir, nida, kip FUT 1 · IMPV 2 · NEG 1 · VOC 1; 1S 2 · 2MP 5 · 2MS 1 · 3FS 1 · 3MS 3; bab I. bab ×4 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=18 (n z=0,59); ölçüm '{{5|fâsıla ٱلظلمون → ن, N sınıfı}}' — satır aynen (6:134 ن → 6:135 ن); "
 "ölçüm '{{5|simetri \\[3, 4, 8, 1\\]}}' — satır aynen; ölçüm '{{5|harf 78 → harf3 72, isaret 6}}' — satır aynen; ölçüm '{{5|dış düğüm 4}}' — satır aynen. "
 "Ölçüm IMPV 2: 'qul' (1. kelime), ''melû' (3. kelime); VOC 1: 'yâ qavmi' (2. kelime); FUT 1: 'fe-sevfe' (8. kelime); NEG 1: 'lâ' (16. kelime); 'fe-sevfe' (8.) kelimesindeki 'fe' REM; 'innî' (6.) ve 'innehû' (15.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) عمل ×2 (''melû' 3. / ''âmil' 7. kelime), كون ×2 ('mekânetikum' 5. / 'tekûnu' 11. kelime) (okuma). "
 + T[135] + " (okuma). "
 + cumle(say('say 6:135 4-5', "'alâ mekânetikum", True), say('dizi 6 135 3 7', "'amile 'alâ mekânet inne 'âmil"), say('dizi 6 135 2 10', "qavm 'amile 'alâ mekânet inne 'âmil sevfe 'alime men"), say('dizi 6 135 1 9', "qâle qavm 'amile 'alâ mekânet inne 'âmil sevfe 'alime")) + ' '
 + cumle(say('say 6:135 13-14', "'âqibetu'd-dâr", True)) + ' '
 + cumle(say('say 6:135 15-18', "innehû lâ yuflihu'z-zâlimûn", True), say('dizi 6 135 15 18', 'inne lâ eflaha zâlim')) + ' ' +
 "Ölçüm xref 39:39 (emsal olarak basıldı), 11:93 (emsal olarak basıldı), 11:121 (emsal olarak basıldı), 28:37 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı: 'inne lâ eflaha zâlim' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'yâ' + izafet + IMPV + ''alâ' + izafet + 'inne' + nekre + 'fe' + 'sevfe' + IMPF + 'men' + IMPF + 'li' + ''âqibe' + belirli + 'inne' + 'lâ' + IMPF + belirli; "
 "D2 emir, nida; IMPV ('qul' 1. kelime, ''melû' 3. kelime), VOC ('yâ qavmi' 2. kelime), FUT ('fe-sevfe' 8. kelime), NEG ('lâ' 16. kelime); D3 عمل ×2, كون ×2; 39:39 eşi, 11:93 eşi, 11:121 eşi, 28:37 eşi; D4 1S 2 · 2MP 5 · 2MS 1 · 3FS 1 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[135] + "; aktör yok (ölçüm); A2 kavme konumlarına göre yapmaları emri; yurdun sonunun kimin olacağının bilinecek oluşu; zalimlerin kurtuluşa eremeyişi; "
 "A3 'yâ qavmi 'melû 'alâ mekânetikum innî 'âmil, fe-sevfe ta'lemûne men tekûnu lehû 'âqibetu'd-dâr, innehû lâ yuflihu'z-zâlimûn' (söz içi, 2-18. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (18. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi haber → emir, nida (ayetler arası); bölüm kapanışı.",
)
