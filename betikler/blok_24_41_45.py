# -*- coding: utf-8 -*-
"""blok_24_41_45.py — sûre 24 blok 24:41-45 (kafiye kuşağının çekirdeği)."""
import json
DIK=json.load(open('blok_dikey_24_41_55.json',encoding='utf-8'))
veri=json.load(open('kuran_veri.json',encoding='utf-8'))
AR={}
for s in veri['sureler']:
    for a in s['ayetler']: AR[(s['no'],a['no'])]=a['ar']

MEAL={
41:"Görmedin mi, göklerde ve yerde olanlar ve kanat açmış kuşlar Allah'ı tesbih ediyor. Her biri kendi duasını ve tesbihini bilmiştir. Allah yaptıklarını bilendir.",
42:"Göklerin ve yerin mülkü Allah'ındır; varış da Allah'adır.",
43:"Görmedin mi, Allah bulutu sürüyor, sonra aralarını birleştiriyor, sonra onu üst üste yığıyor; derken yağmurun aralarından çıktığını görüyorsun. Gökten, içindeki dağlardan dolu indiriyor; dilediğine isabet ettiriyor, dilediğinden çeviriyor. Şimşeğinin parıltısı neredeyse gözleri alacak.",
44:"Allah gece ile gündüzü çevirir. Bunda görme sahipleri için bir ibret var.",
45:"Allah her canlıyı sudan yarattı. Kimi karnı üzerinde yürür, kimi iki ayak üzerinde, kimi dört ayak üzerinde. Allah dilediğini yaratır. Allah her şeye gücü yetendir.",
}

OLCUM={
41:"eksen: **Allah lafzı 4. ve 18. sırada — iki geçiş** (allah z=1,38) · **esmâ عَلِيم *(alîm)* 19. sırada — GEÇERLİ**: doğrudan lafzın yüklemi · aktör yok · edim soru, kip INTG 1 · NEG 1 · CERT 1 · şahıs 2MS 1 · 3MS ×5 · 3MP ×2 · n=21 mora=104 harf=87 (n z=0,91), fâsıla يَفْعَلُونَ *(yaparlar)* → ن, **N sınıfı ama KAFİYE KIRIK işaretli — sûrenin iki kırığından biri (aday 509)**; i'râb ACC 4 · GEN 3 · NOM 4; bab I ×3 · bab II ×1; zaman IMPF ×3 · PERF 1; kök ikilemesi أله *(ilâh; lafza-i celâl)* ×2 · سبح *(tesbih, tenzih)* ×2 · علم *(bilme)* ×2; simetri [3,1,6,1]; dış düğüm 2 · yıldız ★ · kökler رأي *(görme)* · أله · سبح · سمو *(ad; gök)* · أرض *(yer, yeryüzü)* · طير *(kuş; uçan)* · صفف *(saf, dizi)* · كلل *(hep, bütün)* · علم · صلو *(namaz, salât)* · فعل *(yapma, işleme)* · bağ: xref سبّح *(tesbih etti)* + سماء *(gök)* + أرض *(yer)* → **59:24**; **24:36 ile ortak سبح** — orada belirli evlerde tesbih, burada gökte ve yerde olan herkes (elle, L1)",
42:"eksen: **Allah lafzı 1. ve 6. sırada — n=7'de İKİ lafız, allah z=5,18: yıldızın tek kaynağı; sûrenin en yüksek lafız yoğunluğuna EŞİT** (öteki 24:18) · aktör yok · edim haber · **şahıs kaydı YOK — ayette şahıs eki taşıyan öğe yok** · n=7 mora=42 harf=34, **fâsıla ٱلْمَصِيرُ *(varış)* → ر, R sınıfı**; i'râb GEN 4 · NOM 2; **fiil yok** · yıldız ★★★ · kökler أله *(ilâh; lafza-i celâl)* · ملك *(mülk; melik)* · سمو *(ad; gök)* · أرض *(yer, yeryüzü)* · صير *(dönüşme, varış)* · bağ: **24:18 ile aynı z, aynı n, aynı lafız sayısı; kafiye sınıfı ve esmâ durumu ayrı** (elle, L1, aday 511)",
43:"eksen: **Allah lafzı 4. sırada** (allah z=0,00) · aktör yok · edim soru, kip INTG 1 · NEG 1 · şahıs 2MS ×2 · 3MS ×17 · 3FS 1 · **n=38 mora=174 harf=150 — bloğun en uzun ayeti** (n z=2,72), **fâsıla ٱلْأَبْصَٰرِ *(gözler)* → ر, R sınıfı**; i'râb ACC 6 · GEN 7; bab I ×9 · bab II ×2 · bab IV ×2; **zaman IMPF ×13 — on üç fiilin on üçü de muzâri, tek PERF yok**; kök ikilemesi رأي *(görme)* ×2 · شيأ *(dileme; şey)* ×2; simetri [4,27,31,1]; dış düğüm 1 · yıldız ★★ · kökler رأي · أله *(ilâh; lafza-i celâl)* · زجو *(sevk etme, yavaşça sürme)* · سحب *(bulut; sürükleme)* · ألف *(bin (sayı); ülfet)* · بين *(arası; açıklama)* · جعل *(kılma, var etme)* · ركم *(üst üste yığma)* · ودق *(yağmur damlası)* · خرج *(çıkma, çıkarma)* · خلل *(ara, aralık; dostluk (hulle))* · نزل *(inme, indirme)* · سمو *(ad; gök)* · جبل *(dağ)* · برد *(soğukluk, serinlik)* · صوب *(isabet etme, doğru olma)* · شيأ · صرف *(çevirme, türlü türlü açıklama)* · كود *(neredeyse olma)* · سنو *(yıl; parıltı)* · برق *(şimşek; ibrik)* · ذهب *(gitme, götürme)* · بصر *(görme)* · bağ: xref رأى *(gördü)* + ودق *(yağmur)* + خرج *(çıktı)* → **30:48**; **24:40 ile ortak سحب** — orada karanlığın son katmanı, burada sürecin ilk öğesi (elle, L1, aday 512)",
44:"eksen: **Allah lafzı 2. sırada** (allah z=1,47) · aktör yok · edim haber, kip EMPH 1 · şahıs 3MS 1 · n=10 mora=53 harf=45, **fâsıla ٱلْأَبْصَٰرِ *(gözler)* → ر, R sınıfı — 24:43 ile aynı fâsıla kelimesi**; i'râb NOM 1 · ACC 4 · GEN 2; bab II ×1; zaman IMPF 1 · yıldız ★ yok · kökler قلب *(çevirme; kalp)* · أله *(ilâh; lafza-i celâl)* · ليل *(gece)* · نهر *(ırmak; gündüz)* · عبر *(ibret; geçme, tabir etme)* · بصر *(görme)* · bağ: **24:37 ile ortak قلب** — orada kalplerin çevrilmesi (bab V, dönüşlü, fâilsiz), burada gece-gündüzün çevrilmesi (bab II, ettirgen, fâil lafız) (elle, L1, aday 513)",
45:"eksen: **Allah lafzı 1., 23. ve 27. sırada — üç geçiş** (allah z=1,41) · **esmâ قَدِير *(kadîr)* 31. sırada = fâsıla — GEÇERLİ**: doğrudan lafzın yüklemi · aktör yok · edim haber · şahıs 3MS ×7 · 3MP ×3 · n=31 mora=144 harf=115 (n z=1,97), **fâsıla قَدِيرٌۭ → ر, R sınıfı**; i'râb NOM 3 · ACC 3 · GEN 7; **bab I ×6 — altı fiilin altısı da birinci bab**; zaman PERF 1 · IMPF ×5; **kök ikilemesi أله *(ilâh; lafza-i celâl)* ×3 · خلق *(yaratma)* ×2 · كلل *(hep, bütün)* ×2 · مشي *(yürüme)* ×3 · شيأ *(dileme; şey)* ×2**; sayı sözcüğü أَرْبَع *(dört)*; simetri [7,5,15,2]; dış düğüm 1 · yıldız ★ · kökler أله · خلق · كلل · دبب *(yeryüzünde yürüyen canlı)* · موه *(su)* · مشي · بطن *(karın, iç)* · رجل *(adam; yaya)* · ربع *(dört; dörtte bir)* · شيأ · قدر *(ölçü, güç yetirme)* · bağ: **23:12-14 ile ortak خلق** — orada tek türün aşamaları, burada bütün türlerin ortak maddesi ve üç hareket sınıfı (elle, L1, aday 512)",
}

MERCEK={
41:"Kafiye kuşağının açılış ayeti ve fâsılası kırık işaretli: ن ile bitiyor ama sûrenin N deseninden sapıyor. Ölçülebilir bir kapsam genişlemesi: 24:36'da tesbih edenler belirli evlerdeki adamlardı, burada göklerde ve yerde olan herkes ve kuşlar. Ve كُلٌّ قَدْ عَلِمَ *(her biri bilmiştir)* cümlesi bilgiyi özneye dağıtıyor — bilen tek merci değil, her varlık kendi tesbihini biliyor. صفف *(saf, dizi)* kökü korpusta on dört geçişli ve komşuluğunda melek ×15,3; burada kuşun kanat açmış hâli.",
42:"Yedi kelime, iki lafız, hiç fiil ve hiç şahıs eki yok. Ayet iki isim cümlesini yan yana koyuyor ve ikisini de aynı sözcükle bağlıyor: لِلَّهِ *(Allah'ındır)* ve إِلَى ٱللَّهِ *(Allah'adır)* — biri mülkiyet, öteki yön; ikisi de harf-i cerle. Ölçülebilir simetri: iki tamlama, ikisi de mecrur, ve ayetin altı isminden dördü mecrur. 24:18 ile aynı yıldız kaynağını ve aynı z değerini paylaşıyor ama fâsıla sınıfı ayrı — biri sûrenin N koşusunda, öteki R kuşağında.",
43:"On üç fiilin on üçü de muzâri — ayet baştan sona sürüyor olan bir işlemi anlatıyor ve hiçbir yerde tamamlanmış zamana geçmiyor. Ölçülebilir bir adım dizisi: sürme → birleştirme → yığma → çıkma → indirme → isabet ettirme → çevirme, ve ilk üçü ثُمَّ *(sonra)* ile ayrılmış. Üç seyrek kök yan yana: زجو *(sevk etme, yavaşça sürme)* üç, ركم *(üst üste yığma)* üç, ودق *(yağmur damlası)* iki geçişli; üçünün de dikey komşuluğu boş. Ve 24:40'ın son öğesi (سحب *(bulut; sürükleme)*) burada ilk öğe oluyor: karanlık meselinin bittiği yerden bu ayet başlıyor.",
44:"Aynı kök yedi ayet arayla iki ölçekte: 24:37'de قُلُوب *(kalpler)* dönüyordu (bab V, dönüşlü), burada gece ve gündüz çevriliyor (bab II, ettirgen) ve fâil adlandırılmış. Ölçülebilir bir bağ: iki ayet aynı fâsıla kelimesini de paylaşıyor — ٱلْأَبْصَٰرُ / ٱلْأَبْصَٰرِ, biri merfû biri mecrur. Ve 24:43 de aynı kelimeyle bitiyordu: üç ayette üç kez بصر *(görme)*, üçü de fâsılada ya da fâsılaya bitişik.",
45:"Ayet bir sınıflandırma kuruyor ve sınıflandırmayı tek bir ölçütle yapıyor: yürüme biçimi. مشي *(yürüme)* kökü üç kez, üçünde de aynı kalıpla ve yalnız dayanak değişiyor — karın, iki ayak, dört ayak. Ölçülebilir bir sayı dizisi: sıfır (karın), iki, dört; tek sayı yok ve dörtten sonrası da yok. Ortak madde tek kelimeyle veriliyor: مِّن مَّآءٍ *(sudan)*, nekre. دبب *(yeryüzünde yürüyen canlı)* korpusta on sekiz geçişli ve dikey komşuluğunda رزق *(rızık)* ×10,0 · أرض *(yer, yeryüzü)* ×3,5 — kök korpusta zaten yeryüzü ve beslenmeyle bağlı.",
}

ATLAMA={
 "24:42":"★★★ ayet. 🜁 biyolog YAZILMADI — beş kökün hiçbiri canlıya, organa ya da sürece bağlanmıyor. 🜂 uzay YAZILMADI — سَمَٰوَٰت *(gökler)* geçiyor ama ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ *(gökler ve yer)* bir BÜTÜNLÜK FORMÜLÜ; mülkün kapsamını veriyor, gök cismi/hareket/ölçü değil. Formülü astronomik okumak yasaklı 'bilimsel izdüşüm' olurdu.",
 "24:43":"★★ ayet — **mercek eşiği ★★★, TUTMUYOR.** Oysa çıpa VAR: sûrenin meteorolojik olarak en yoğun ayeti (سحب *(bulut)* · ودق *(yağmur damlası)* · برد *(dolu)* · برق *(şimşek)* · جبل *(dağ)* · سمو *(gök)*; üç seyrek kök: زجو n=3 · ركم n=3 · ودق n=2). Protokol gereği mercek YAZILAMADI. Aday 512 — 468'in en temiz vakalarından biri. NOT: çıpa olsaydı bile uzay merceği yazılmazdı; ayet meteorolojik bir dizi veriyor, gök cismi/yörünge/ölçü değil.",
 "24:45":"★ ayet — **mercek eşiği ★★★, TUTMUYOR.** Çıpa VAR ve güçlü: sûrenin biyolojik olarak en yoğun ayeti (دبب *(yeryüzünde yürüyen canlı)* · موه *(su)* · مشي *(yürüme)* ×3 · بطن *(karın)* · رجل *(ayak)*), üç hareket sınıfı ve bir ortak madde. Protokol gereği mercek YAZILAMADI. **Aday 512 — 468 için EN TEMİZ vaka.** 🜂 uzay zaten çıpasız.",
 "_blok_notu_24_41_45":"Blok 24:41-45'te tek ★★★ ayet (24:42) ve iki mercek de atlandı (bütünlük formülü çıpa sayılmadı). Buna karşılık bloğun İKİ çıpalı ayeti (24:43 meteoroloji ★★, 24:45 biyoloji ★) yıldız eşiğinin ALTINDA kaldı. Sûre 24'te uzman merceği yalnız 24:35'te yazılabildi. Aday 512: çıpa ile yıldız birbirinden bağımsız ölçüler ve bu blokta TERS yönde ayrışıyorlar — 468'in en temiz vakası.",
}

p='/home/claude/repo/notlar/okuma_metni.json'
OM=json.load(open(p,encoding='utf-8'))
for n in range(41,46):
    OM['24']["24:%d"%n]={"ar":AR[(24,n)],"meal":MEAL[n],"olcum":OLCUM[n],
                         "mercek":MERCEK[n],"dikey":DIK["24:%d"%n]}
OM['24']['_mercek_atlama_notu'].update(ATLAMA)
OM['24']['_blok_bolme_notu'] += (" İKİNCİ BÖLME: 24:41-55 yerine 24:41-45 okundu; gerekçe, bu beş ayetin "
  "kafiye kuşağının çekirdeği olması (24:41 kırık, 42-45 R) ve içlerinde sûrenin iki mercek-çıpalı "
  "ayetinin (24:43 meteoroloji, 24:45 canlı sınıfları) bulunması.")
OM['ilerleme']['not']=("Sûre 23 TAM (118/118). Sûre 24 (Nûr) makro profil + 24:1-45 okundu. "
                       "Devam: 24:46. Kafiye kuşağı 24:46'da kapanıyor (N'ye dönüş).")
OM['ilerleme']['kismi']={"2":"1-20 ayet düzeyinde","24":"1-45 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet']=1626
json.dump(OM,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('okuma_metni: sûre 24 →',len([k for k in OM['24'] if not k.startswith('_')]),'ayet')

pm='/home/claude/repo/notlar/mercek_kayit.json'
MK=json.load(open(pm,encoding='utf-8'))
for n in range(41,46): MK['24']["24:%d"%n]=MERCEK[n]
MK['24_atlama'].update(ATLAMA)
json.dump(MK,open(pm,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('mercek_kayit: sûre 24 →',len(MK['24']),'mercek')
