# sûre 6 blok 30 (6:126-130) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b30/say2.txt'
os.environ['OLC'] = '/home/claude/b30/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Ölüyken dirilen; cin ve insan toplulukları' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 126: "Bu, Rabbinin dosdoğru yoludur. Öğüt alan bir kavim için âyetleri ayrıntılı açıkladık.",
 127: "Rableri katında selam yurdu onlarındır. Yapmakta olduklarından dolayı O, onların dostudur.",
 128: "Onların hepsini toplayacağı gün, ey cin topluluğu, insanlardan çok kimseyi ele geçirdiniz. İnsanlardan onların dostları, Rabbimiz, birbirimizden faydalandık ve bize belirlediğin ecelimize ulaştık dediler. Allah'ın dilediği dışında, orada ebedî kalanlar olarak yeriniz ateştir dedi. Şüphesiz Rabbin hakîmdir, bilendir.",
 129: "Böylece kazanmakta olduklarından dolayı zalimlerin bir kısmını bir kısmına dost kılarız.",
 130: "Ey cin ve insan topluluğu, size içinizden, size âyetlerimi anlatan ve sizi bu gününüzün karşılaşmasıyla uyaran elçiler gelmedi mi? Kendi aleyhimize şahitlik ettik dediler. Dünya hayatı onları aldattı ve kâfir olduklarına kendi aleyhlerine şahitlik ettiler.",
}

T = {}
T[126] = ("muhatap 2MS (adsız; 'rabbike' eki — 3. kelime); konuşan 1P (adsız; 'fassalne' — 6. kelime); "
          "'yezzekkerûn' 3MP (adsız; gönderge 'li-qavmin' 8. kelime, 9. kelime)")
T[127] = ("'lehum', 'rabbihim', 'veliyyuhum', 'kânû', 'ya'melûn' 3MP (adsız; gönderge 6:126 8. kelime — 1., 5., 7., 9. ve 10. kelime); "
          "'huve' 3MS (adsız; gönderge 'rabbihim' 5. kelime, 6. kelime)")
T[128] = ("'yahşuruhum' 3MS (adsız; gönderge 6:127 5. kelime, 2. kelime); 'yahşuruhum' eki 3MP (adsız; gönderge 'l-cinni' 5. kelime, 2. kelime); "
          "muhatap 2MP (adsız; nidâ; 'steksertum' — 7. kelime); 'qâle' 3MS (fiil uyumu; 10. kelime — fail 11. kelime); 'evliyâ'uhum' eki 3MP (adsız; gönderge 'l-cinni' 5. kelime, 11. kelime); "
          "konuşan 1P (adsız; söz içi; 'rabbene', 'ba'dunâ', 've belağnâ', 'ecelene', 'lenâ' — 14., 16., 18., 19. ve 22. kelime); 'stemta'a' 3MS (fiil uyumu; söz içi; 15. kelime — fail 16. kelime); "
          "muhatap 2MS (adsız; söz içi; 'eccelte' — 21. kelime); 'qâle' 3MS (gizli zamir, adsız; 23. kelime — fail 23. kelime içi gizli zamir, gönderge 6:127 5. kelime; 'n-nâru' 24. kelime söz içi mübteda); muhatap 2MP (adsız; söz içi; 'mesvâkum' — 25. kelime); "
          "'fîhâ' 3FS (adsız; söz içi; gönderge 'n-nâru' 24. kelime, 27. kelime); 'şâ'e' 3MS (fiil uyumu; söz içi; 30. kelime — fail 31. kelime); muhatap 2MS (adsız; 'rabbeke' eki — 33. kelime)")
T[129] = ("konuşan 1P (adsız; 'nuvellî' — 2. kelime); 'kânû', 'yeksibûn' 3MP (adsız; gönderge 'z-zâlimîne' 4. kelime — 7. ve 8. kelime)")
T[130] = ("muhatap 2MP (adsız; 'ye'tikum', 'minkum', ''aleykum', 've yunzirûnekum', 'yevmikum' ekleri — 5., 7., 9., 11. ve 13. kelime); 'ye'tikum' 3MS (fiil uyumu; 5. kelime — fail 6. kelime); "
          "'yaqussûne', 've yunzirûnekum' 3MP (adsız; gönderge 'rusulun' 6. kelime — 8. ve 11. kelime); konuşan 1S (adsız; 'âyâtî' eki — 10. kelime); "
          "'qâlû' 3MP (adsız; gönderge 'ma'şera'l-cinni' 1. kelime, 15. kelime); konuşan 1P (adsız; söz içi; 'şehidnâ', 'enfusinâ' — 16. ve 18. kelime); "
          "'ğarrat' 3FS (fiil uyumu; 19. kelime — fail 20. kelime); 'ğarrathumu', 've şehidû', 'enfusihim', 'ennehum', 'kânû' 3MP (adsız; gönderge 'ma'şera'l-cinni' 1. kelime — 19., 22., 24., 25. ve 26. kelime)")

D = {}
D[126] = ("◇ 've hâzâ sırâtu rabbike mustaqîmen qad fassalne'l-âyâti li-qavmin yezzekkerûn' — "
 "'ve' + 'hâ' + 'zâ' + 'sırât' + 'rabb' + 2MS + nekre etken ortaç 'mustaqîm' + 'qad' + PERF 1P II. bab + 1P + belirli çoğul 'âye' + 'li' + nekre 'qavm' + IMPF 3MP V. bab + 3MP "
 "(ölçüm edim haber, kip CERT 1, biçim DIKKAT; 1P 2 · 2MS 1 · 3MP 2; bab II. bab ×1 · V. bab ×1). "
 "Allah lafzı yok; Rab 3. sırada (ölçüm rab z=2,05); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=9 (n z=-0,36); ölçüm '{{1|biçim DIKKAT}}' — satır aynen; ölçüm '{{1|fâsıla يذكرون → ن, N sınıfı}}' — satır aynen (6:125 ن → 6:126 ن); "
 "ölçüm '{{1|harf 43 → harf3 40, isaret 3}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (5. kelime); 've hâzâ' (1.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) قوم ×2 ('mustaqîmen' 4. / 'li-qavmin' 8. kelime) (okuma). "
 + T[126] + " (okuma). "
 + cumle(say('say 6:126 5-8', "qad fassalne'l-âyâti li-qavmin", True), say('dizi 6 126 5 8', 'qad fassale âye qavm')) + ' '
 + cumle(say('say 6:126 8-9', 'li-qavmin yezzekkerûn', True), say('dizi 6 126 7 9', 'âye qavm tezekkera')) + ' '
 + cumle(say('say 6:126 2-3', 'sırâtu rabbike', True)) + ' ' +
 "Ölçüm xref 16:13 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı: 'qad fassale âye qavm' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'hâ' + 'zâ' + 'sırât' + izafet + nekre + 'qad' + PERF + belirli + 'li' + nekre + IMPF; "
 "D2 haber; CERT ('qad' 5. kelime); D3 قوم ×2; 16:13 eşi; D4 1P 2 · 2MS 1 · 3MP 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[126] + "; aktör yok (ölçüm); A2 Rabbin yolunun dosdoğru oluşu; öğüt alan bir kavim için âyetlerin ayrıntılı açıklanması; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs sayısında beraberlik (1. şahıs 2 · 3. şahıs 2 — ölçüm baskın 1); şahıs geçişi 3 → 1 (ayetler arası); edim geçişi şart → haber (ayetler arası).",
)

D[127] = ("◇ 'lehum dâru's-selâmi 'inde rabbihim, ve huve veliyyuhum bi-mâ kânû ya'melûn' — "
 "'li' + 3MP + 'dâr' + belirli 'selâm' + ''ind' + 'rabb' + 3MP + 've' + 'huve' + 'veliyy' + 3MP + 'bi' + 'mâ' + PERF 3MP I. bab + 3MP + IMPF 3MP I. bab + 3MP "
 "(ölçüm edim haber, kip yok; 3MP 7 · 3MS 1; bab I. bab ×2). "
 "Allah lafzı yok; Rab 5. sırada (ölçüm rab z=1,81); ölçüm '{{2|esmâ سَلام 3\\. sırada, ORTA konum, MÜHÜRSÜZ \\| وَلِيّ 7\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET (ÇİFT) ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor, araç tanımı farkı (muhur_el EVET, ölçümle uyuşmuyor — tam okuma sonu); "
 "esma_el kaydı 'degil' — 'lehum dâru's-selâmi', kural 'esmâ adı esmâ dışı göndergeyle → degil' (cennet adı tamlaması; onaya açık) (okuma); "
 "esma_el kaydı 'ilahi' — 've huve veliyyuhum', kural 'zamirin haberi → ilahi' (Rab) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=10 (n z=-0,26); ölçüm '{{2|fâsıla يعملون → ن, N sınıfı}}' — satır aynen (6:126 ن → 6:127 ن); "
 "ölçüm '{{2|harf 43 → harf3 40, isaret 3}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; 've huve' (6.) kelimesindeki 've' CONJ; ''inde' (4.) LOC (okuma). "
 + T[127] + " (okuma). "
 + cumle(say('say 6:127 8-10', "bi-mâ kânû ya'melûn", True), say('dizi 6 127 8 10', "mâ kâne 'amile")) + ' '
 + cumle(say('say 6:127 2-3', "dâru's-selâm", True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'bi-mâ kâne 'amile' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'li' + 'dâr' + belirli + ''ind' + izafet + 've' + 'huve' + izafet + 'bi' + 'mâ' + PERF + IMPF; "
 "D2 haber; D3 —; D4 3MP 7 · 3MS 1, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[127] + "; aktör yok (ölçüm); A2 selam yurdunun Rableri katında onların oluşu; Rablerinin yaptıkları dolayısıyla onların dostu oluşu; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 1 → 3 (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[128] = ("◇ 've yevme yahşuruhum cemî'an yâ ma'şera'l-cinni qadi'steksertum mine'l-insi ve qâle evliyâ'uhum mine'l-insi rabbene'stemta'a ba'dunâ bi-ba'din ve belağnâ ecelene'llezî eccelte lenâ qâle'n-nâru mesvâkum xâlidîne fîhâ illâ mâ şâ'e'llâh, inne rabbeke hakîmun 'alîm' — "
 "'ve' + 'yevm' + IMPF 3MS I. bab + 3MP + nekre 'cemî'' + 'yâ' + 'ma'şer' + belirli 'cinn' + 'qad' + PERF 2MP X. bab + 2MP + 'min' + belirli 'ins' + 've' + PERF 3MS I. bab + çoğul 'veliyy' + 3MP + 'min' + belirli 'ins' + "
 "'rabb' + 1P + PERF 3MS X. bab + 'ba'd' + 1P + 'bi' + nekre 'ba'd' + 've' + PERF 1P I. bab + 1P + 'ecel' + 1P + 'ellezî' + PERF 2MS II. bab + 2MS + 'li' + 1P + PERF 3MS I. bab + belirli 'nâr' + 'mesvâ' + 2MP + "
 "çoğul etken ortaç 'xâlid' + 'fî' + 3FS + 'illâ' + 'mâ' + PERF 3MS I. bab + lafız + 'inne' + 'rabb' + 2MS + nekre 'hakîm' + nekre ''alîm' "
 "(ölçüm edim nida, kip CERT 1 · VOC 1, biçim ISTISNA; 1P 6 · 2MP 3 · 2MS 3 · 3FS 1 · 3MP 2 · 3MS 5; bab I. bab ×5 · II. bab ×1 · X. bab ×2). "
 "Allah lafzı 31. sırada (ölçüm allah z=0,04); Rab 14. ve 33. sırada (ölçüm rab z=0,90); ölçüm '{{3|esmâ وَلِيّ 11\\. sırada, ORTA konum, MÜHÜR \\| حَكِيم 34\\. sırada, SON konum, MÜHÜR \\| عَلِيم 35\\. sırada, SON konum, MÜHÜR}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET (ÇİFT) ton denge' — ölçüm MÜHÜR ile uyuşuyor (muhur_el EVET); "
 "esma_el kaydı 'degil' — 've qâle evliyâ'uhum', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); "
 "esma_el kaydı 'ilahi' — 'inne rabbeke hakîmun 'alîm', kural ''inne/enne' haberi → ilahi' (Rab) ve ''alîm' için kural ''inne/enne' haberi → ilahi' (Rab; 'hakîm'in sıfatı) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=35 (n z=2,40); ölçüm '{{3|sayı işareti مَعْشَر, اسْتَكْثَرْ}}' — satır aynen; ölçüm '{{3|fâsıla عليم → م, N sınıfı}}' — satır aynen (6:127 ن → 6:128 م); "
 "ölçüm '{{3|simetri \\[3, 6, 20, 1\\]}}' — satır aynen; ölçüm '{{3|harf 155 → harf3 149, isaret 6}}' — satır aynen; ölçüm '{{3|dış düğüm 5}}' — satır aynen; ölçüm '{{3|İÇ düğüm 2}}' — satır aynen. "
 "Ölçüm CERT 1: 'qadi' (6. kelime); VOC 1: 'yâ ma'şera' (4. kelime); biçim ISTISNA: 'illâ' (28. kelime); 've yevme' (1.), 've qâle' (10.) ve 've belağnâ' (18.) kelimelerindeki 've' CONJ; 'inne' (32.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) أجل ×2 ('ecelene' 19. / 'eccelte' 21. kelime), أنس ×2 ('l-insi' 9. / 'l-insi' 13. kelime), بعض ×2 ('ba'dunâ' 16. / 'bi-ba'din' 17. kelime), ربب ×2 ('rabbene' 14. / 'rabbeke' 33. kelime), قول ×2 ('qâle' 10. / 'qâle' 23. kelime) (okuma). "
 + T[128] + " (okuma). "
 + cumle(say('say 6:128 32-35', "inne rabbeke hakîmun 'alîm", True), say('dizi 6 128 32 35', "inne rabb hakîm 'alîm")) + ' '
 + cumle(say('say 6:128 1-3', "ve yevme yahşuruhum cemî'an", True), say('dizi 6 128 1 3', "yevm haşera cemî'")) + ' '
 + cumle(say('say 6:128 4-5', "yâ ma'şera'l-cinn", True)) + ' '
 + cumle(say('say 6:128 26-27', "xâlidîne fîhâ", True)) + " (--medde 40 ayet: 'xâlidîne' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). "
 "Ölçüm xref 6:22 (basılmış), 10:28 (basılmış), 34:40 (emsal olarak basıldı), 6:83 (basılmış) ve okunmuş 2 ayet ve okunmamış 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'inne rabb hakîm 'alîm' süzgeç GEÇER, 'yevm haşera cemî'' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 'yevme' (1. kelime), 'ecelene' (19. kelime), 'eccelte' (21. kelime).",
 "◈B — B1 'l-insi' (9. kelime), 'l-insi' (13. kelime); B2 —; B3 —; B4 —.",
 "◈D — D1 've' + 'yevm' + IMPF + nekre + 'yâ' + 'ma'şer' + belirli + 'qad' + PERF + 'min' + belirli + 've' + PERF + izafet + 'min' + belirli + izafet + PERF + izafet + 'bi' + nekre + 've' + PERF + izafet + 'ellezî' + PERF + 'li' + PERF + belirli + izafet + 'xâlid' + 'fî' + 'illâ' + 'mâ' + PERF + lafız + 'inne' + izafet + nekre + nekre; "
 "D2 nida; CERT ('qadi' 6. kelime), VOC ('yâ ma'şera' 4. kelime); D3 أجل ×2, أنس ×2, بعض ×2, ربب ×2, قول ×2; 34:40 eşi; D4 1P 6 · 2MP 3 · 2MS 3 · 3FS 1 · 3MP 2 · 3MS 5, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[128] + "; aktör yok (ölçüm); A2 cin topluluğuna insanlardan çok kimseyi ele geçirdiklerinin söylenmesi; insanlardan dostlarının birbirinden faydalanma ve belirlenen ecele ulaşma itirafı; ateşin onların yeri oluşu; Rabbin hakîm ve bilen oluşu; "
 "A3 'rabbene'stemta'a ba'dunâ bi-ba'din ve belağnâ ecelene'llezî eccelte lenâ' (söz içi, 14-22. kelime); 'n-nâru mesvâkum xâlidîne fîhâ illâ mâ şâ'e'llâh' (söz içi, 24-31. kelime); "
 "A4 " + BOLUM + "; söz açılır (14. kelime); söz kapanır (22. kelime, ayet içi); söz açılır (24. kelime); söz kapanır (31. kelime, ayet içi); şahıs sayısında beraberlik (1. şahıs 6 · 2. şahıs 6 · 3. şahıs 8 — ölçüm baskın 1); şahıs geçişi 3 → 1 (ayetler arası); edim geçişi haber → nida (ayetler arası).",
)

D[129] = ("◇ 've kezâlike nuvellî ba'da'z-zâlimîne ba'dan bi-mâ kânû yeksibûn' — "
 "'ve' + 'ke' + 'zâlike' + IMPF 1P II. bab + 'ba'd' + belirli çoğul etken ortaç 'zâlim' + nekre 'ba'd' + 'bi' + 'mâ' + PERF 3MP I. bab + 3MP + IMPF 3MP I. bab + 3MP "
 "(ölçüm edim haber, kip yok; 1P 1 · 3MP 4; bab I. bab ×2 · II. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=8 (n z=-0,47); ölçüm '{{4|fâsıla يكسبون → ن, N sınıfı}}' — satır aynen (6:128 م → 6:129 ن); "
 "ölçüm '{{4|harf 39 → harf3 37, isaret 2}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; 've kezâlike' (1.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) بعض ×2 ('ba'da' 3. / 'ba'dan' 5. kelime) (okuma). "
 + T[129] + " (okuma). "
 + cumle(say('say 6:129 6-8', 'bi-mâ kânû yeksibûn', True)) + ' '
 + cumle(say('say 6:129 1-2', 've kezâlike nuvellî', True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'ke' + 'zâlike' + IMPF + 'ba'd' + belirli + nekre + 'bi' + 'mâ' + PERF + IMPF; "
 "D2 haber; D3 بعض ×2; D4 1P 1 · 3MP 4, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[129] + "; aktör yok (ölçüm); A2 zalimlerin bir kısmının kazandıkları dolayısıyla bir kısmına dost kılınması; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 1 → 3 (ayetler arası); edim geçişi nida → haber (ayetler arası).",
)

D[130] = ("◇ 'yâ ma'şera'l-cinni ve'l-insi e-lem ye'tikum rusulun minkum yaqussûne 'aleykum âyâtî ve yunzirûnekum liqâ'e yevmikum hâzâ, qâlû şehidnâ 'alâ enfusinâ, ve ğarrathumu'l-hayâtu'd-dunyâ ve şehidû 'alâ enfusihim ennehum kânû kâfirîn' — "
 "'yâ' + 'ma'şer' + belirli 'cinn' + 've' + belirli 'ins' + 'e' + 'lem' + IMPF 3MS I. bab + 2MP + nekre çoğul 'resûl' + 'min' + 2MP + IMPF 3MP I. bab + 3MP + ''alâ' + 2MP + çoğul 'âye' + 1S + 've' + IMPF 3MP IV. bab + 3MP + 2MP + "
 "mastar 'liqâ'' + 'yevm' + 2MP + 'hâ' + 'zâ' + PERF 3MP I. bab + 3MP + PERF 1P I. bab + 1P + ''alâ' + çoğul 'nefs' + 1P + 've' + PERF 3FS I. bab + 3MP + belirli 'hayât' + belirli 'dunyâ' + "
 "'ve' + PERF 3MP I. bab + 3MP + ''alâ' + çoğul 'nefs' + 3MP + 'enne' + 3MP + PERF 3MP I. bab + 3MP + çoğul etken ortaç 'kâfir' "
 "(ölçüm edim soru, nida, kip INTG 1 · NEG 1 · VOC 1, biçim DIKKAT; 1P 3 · 1S 1 · 2MP 5 · 3FS 1 · 3MP 13 · 3MS 1; bab I. bab ×7 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=27 (n z=1,55); ölçüm '{{5|biçim DIKKAT}}' — satır aynen; ölçüm '{{5|sayı işareti مَعْشَر}}' — satır aynen; ölçüm '{{5|fâsıla كفرين → ن, N sınıfı}}' — satır aynen (6:129 ن → 6:130 ن); "
 "ölçüm '{{5|simetri \\[4, 16, 22, 1\\]}}' — satır aynen; ölçüm '{{5|harf 138 → harf3 132, isaret 6}}' — satır aynen; ölçüm '{{5|dış düğüm 4}}' — satır aynen. "
 "Ölçüm INTG 1: 'e-lem' (4. kelime; soru hemzesi); NEG 1: 'e-lem' (4. kelime); VOC 1: 'yâ ma'şera' (1. kelime); 've'l-insi' (3.), 've yunzirûnekum' (11.), 've ğarrathumu' (19.) ve 've şehidû' (22.) kelimelerindeki 've' CONJ; 'ennehum' (25.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) شهد ×2 ('şehidnâ' 16. / 've şehidû' 22. kelime), نفس ×2 ('enfusinâ' 18. / 'enfusihim' 24. kelime) (okuma). "
 + T[130] + " (okuma). "
 + cumle(say('say 6:130 1-3', "yâ ma'şera'l-cinni ve'l-ins", True)) + ' '
 + cumle(say('say 6:130 11-13', "ve yunzirûnekum liqâ'e yevmikum", True), say('dizi 6 130 11 15', "enzere liqâ' yevm zâ qâle")) + ' '
 + cumle(say('say 6:130 19-21', "ve ğarrathumu'l-hayâtu'd-dunyâ", True), say('dizi 6 130 19 21', 'ğarra hayât dunyâ')) + ' ' +
 "Ölçüm xref 55:33 (emsal olarak basıldı), 39:71 (emsal olarak basıldı) ve okunmamış 2 ayet. "
 "Ölçüm nakarat3 kalıbı: 'ğarra hayât dunyâ' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 'yevmikum' (13. kelime).",
 "◈B — B1 'l-insi' (3. kelime); B2 —; B3 —; B4 'l-hayâtu' (20. kelime).",
 "◈D — D1 'yâ' + 'ma'şer' + belirli + 've' + belirli + 'e' + 'lem' + IMPF + nekre + 'min' + IMPF + ''alâ' + izafet + 've' + IMPF + 'liqâ'' + izafet + 'hâ' + 'zâ' + PERF + PERF + ''alâ' + izafet + 've' + PERF + belirli + belirli + 've' + PERF + ''alâ' + izafet + 'enne' + PERF + 'kâfir'; "
 "D2 soru, nida; INTG ('e-lem' 4. kelime), NEG ('e-lem' 4. kelime), VOC ('yâ ma'şera' 1. kelime); D3 شهد ×2, نفس ×2; 55:33 eşi, 39:71 eşi; D4 1P 3 · 1S 1 · 2MP 5 · 3FS 1 · 3MP 13 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[130] + "; aktör yok (ölçüm); A2 cin ve insan topluluğuna içlerinden elçilerin gelip gelmediğinin sorulması; kendi aleyhlerine şahitlikleri; dünya hayatının onları aldatması ve kâfir olduklarına şahitlik etmeleri; "
 "A3 'şehidnâ 'alâ enfusinâ' (söz içi, 16-18. kelime); "
 "A4 " + BOLUM + "; söz açılır (16. kelime); söz kapanır (18. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi haber → soru (ayetler arası).",
)
