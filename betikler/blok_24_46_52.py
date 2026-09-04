# -*- coding: utf-8 -*-
"""blok_24_46_52.py — sûre 24 blok 24:46-52."""
import json
DIK=json.load(open('blok_dikey_24_46_64.json',encoding='utf-8'))
veri=json.load(open('kuran_veri.json',encoding='utf-8'))
AR={}
for s in veri['sureler']:
    for a in s['ayetler']: AR[(s['no'],a['no'])]=a['ar']

MEAL={
46:"Andolsun, açıklayıcı âyetler indirdik. Allah dilediğini dosdoğru bir yola iletir.",
47:"\"Allah'a ve Elçi'ye inandık, itaat ettik\" derler; sonra içlerinden bir bölük bunun ardından yüz çevirir. Onlar mü'min değildir.",
48:"Aralarında hüküm vermesi için Allah'a ve Elçisi'ne çağrıldıklarında, içlerinden bir bölük hemen yüz çevirir.",
49:"Ama hak kendilerinden yanaysa, boyun eğerek koşup gelirler.",
50:"Kalplerinde bir hastalık mı var, yoksa şüpheye mi düştüler, yoksa Allah'ın ve Elçisi'nin kendilerine haksızlık edeceğinden mi korkuyorlar? Hayır, onlar zalimlerin ta kendileridir.",
51:"Aralarında hüküm vermesi için Allah'a ve Elçisi'ne çağrıldıklarında mü'minlerin sözü ancak \"işittik ve itaat ettik\" demektir. İşte onlar kurtuluşa erenlerdir.",
52:"Kim Allah'a ve Elçisi'ne itaat eder, Allah'tan korkar ve O'ndan sakınırsa, işte onlar kazananlardır.",
}

OLCUM={
46:"eksen: **Allah lafzı 5. sırada** (allah z=1,29) · aktör yok · edim haber, kip EMPH 1 · CERT 1 · şahıs 1P ×2 · 3MS ×2 · n=11 mora=68 harf=50, **fâsıla مُّسْتَقِيمٍۢ *(dosdoğru)* → م, N sınıfı — KAFİYE KUŞAĞI BURADA KAPANIYOR: on ayet sonra N'ye ilk dönüş (aday 509)**; i'râb ACC 2 · NOM 1 · GEN 2; bab I ×2 · bab IV ×1; zaman PERF 1 · IMPF ×2; **dış düğüm 3** · yıldız ★ yok · kökler نزل *(inme, indirme)* · أيي *(âyet, işaret)* · بين *(arası; açıklama)* · أله *(ilâh; lafza-i celâl)* · هدي *(yol gösterme)* · شيأ *(dileme; şey)* · صرط *(yol, sırât)* · قوم *(kalkma; kavim; kıyamet)* · bağ: xref هدى *(iletti)* + شاء *(diledi)* + صراط *(yol)* → **2:142 · 2:213 · 10:25**; **24:1 · 24:18 · 24:34 · 24:46 — üçlü DÖRDÜNCÜ kez** (aday 507); **23:73 ile ortak صِرَٰط مُّسْتَقِيم** (elle, L1)",
47:"eksen: **Allah lafzı 3. sırada** (allah z=0,81) · **esmâ مُؤْمِن *(mü'min)* 15. sırada = fâsıla — ÖLÇÜM ARTEFAKTI (aday 461)**: olumsuzlanmış çoğul · **aktör: adsız ferîk *(bir bölük)* 8. sırada** · edim haber, kip NEG 1 · şahıs 3MP ×3 · 1P ×4 · 3MS 1 · n=15 mora=96 harf=75, fâsıla ٱلْمُؤْمِنِينَ → ن, N sınıfı; i'râb GEN 4 · NOM 1; bab I ×1 · bab IV ×2 · bab V ×1; zaman IMPF ×2 · PERF ×2; kök ikilemesi أمن *(güven; iman)* ×2 — biri alıntı içinde olumlu, biri dışında olumsuz; simetri [3,9,12,1] · yıldız ★ yok · kökler قول *(söz söyleme)* · أمن · أله *(ilâh; lafza-i celâl)* · رسل *(gönderme, elçi)* · طوع *(güç yetirme, itaat)* · ولي *(dost, veli; velâyet)* · فرق *(ayırma, parçalara bölme)* · بعد *(sonra; uzaklık)* · bağ: **24:48 ile ferîk çifti** (elle, L1, aday 514)",
48:"eksen: **Allah lafzı 4. sırada** (allah z=1,29) · **aktör: adsız ferîk *(bir bölük)* 9. sırada** · edim haber · şahıs 3MP ×4 · 3MS ×2 · n=11 mora=62 harf=51, fâsıla مُّعْرِضُونَ *(yüz çevirenler)* → ن, N sınıfı; i'râb GEN 2 · ACC 1 · NOM 2; bab I ×2; zaman PERF 1 · IMPF 1; **edilgen 1 — pas z=2,52**; simetri [3,1,8,1] · yıldız ★★ · kökler دعو *(çağırma, dua)* · أله *(ilâh; lafza-i celâl)* · رسل *(gönderme, elçi)* · حكم *(hüküm verme, hikmet)* · بين *(arası; açıklama)* · فرق *(ayırma, parçalara bölme)* · عرض *(sunma; yüz çevirme)* · bağ: **24:51 ile aynalı kalıp** — sekiz kelime birebir, sonuç ters (elle, L1, aday 514)",
49:"eksen yok · aktör yok · edim şart, kip COND 1 · şahıs 3MS ×2 · 3MP ×3 · **n=7 mora=35 harf=29 — bloğun en kısa ayeti**, fâsıla مُذْعِنِينَ *(boyun eğerek koşanlar)* → ن, N sınıfı; i'râb NOM 1 · ACC 1; bab I ×2; zaman IMPF ×2; **hapaks: ذعن *(boyun eğerek koşma, izʼân)* — korpusta TEK geçiş, hapaks z=3,38: yıldızın tek kaynağı**; **bloğun tek lafızsız ayeti** · yıldız ★★★ · kökler كون *(olmak)* · حقق *(hak, gerçek)* · أتي *(gelme, getirme)* · ذعن · bağ: **24:48 ile karşıtlık** — orada çağrıya yüz çevirme, burada çıkar varsa koşma (elle, L1, aday 514)",
50:"eksen: **Allah lafzı 10. sırada** (allah z=0,72) · aktör yok · edim soru, **kip INTG 1 — ayet içinde İKİ أَمْ, ikisi de muttasıla; INTG'yi أَفِى açılışı veriyor (aday 438/483 karşı kontrolü: muttasıla doğru işleniyor)** · şahıs 3MP ×7 · 3MS ×2 · n=16 mora=83 harf=70, fâsıla ٱلظَّٰلِمُونَ *(zalimler)* → ن, N sınıfı; i'râb GEN 1 · NOM 4; bab I ×2 · bab VIII ×1; zaman PERF 1 · IMPF ×2; **hapaks: حيف *(haksızlık, tarafa meyletme)* — korpusta TEK geçiş, hapaks z=3,38: yıldızın tek kaynağı; Allah medyan mesafesi 1**; biçim IDRAB; simetri [3,4,11,1] · yıldız ★★★ · kökler قلب *(çevirme; kalp)* · مرض *(hastalık)* · ريب *(şüphe, rayb)* · خوف *(korku)* · حيف · أله *(ilâh; lafza-i celâl)* · رسل *(gönderme, elçi)* · ظلم *(zulüm)* · bağ: **24:37 · 24:44 · 24:50 — قلب kökü üçüncü kez**, üç ayrı işlevde: dönen, çevrilen, hasta (elle, L1)",
51:"eksen: **Allah lafzı 8. sırada** (allah z=0,58) · **esmâ مُؤْمِن *(mü'min)* 4. sırada — ÖLÇÜM ARTEFAKTI (aday 461)** · aktör yok · edim haber · şahıs 3MS ×3 · 3MP ×6 · 1P ×4 · n=18 mora=101 harf=88, fâsıla ٱلْمُفْلِحُونَ *(kurtuluşa erenler)* → ن, N sınıfı; i'râb ACC 3 · GEN 3 · NOM 1; bab I ×5 · bab IV ×1; zaman PERF ×4 · IMPF ×2; edilgen 1 (pas z=0,62); kök ikilemesi قول *(söz söyleme)* ×2 · yıldız ★ yok · kökler كون *(olmak)* · قول · أمن *(güven; iman)* · دعو *(çağırma, dua)* · أله *(ilâh; lafza-i celâl)* · رسل *(gönderme, elçi)* · حكم *(hüküm verme, hikmet)* · بين *(arası; açıklama)* · سمع *(işitme)* · طوع *(güç yetirme, itaat)* · فلح *(kurtuluşa erme, felâh)* · bağ: **24:48 ile aynalı** — sekiz kelime birebir aynı, sonuç ters; **23:102 ile aynı fâsıla** (elle, L1, adaylar 514, 515)",
52:"eksen: **Allah lafzı 3. ve 6. sırada — n=10'da İKİ lafız, allah z=3,47: yıldızın tek kaynağı (aday 503)** · aktör yok · edim haber · şahıs 3MS ×5 · 3MP 1 · n=10 mora=57 harf=47, fâsıla ٱلْفَآئِزُونَ *(kazananlar)* → ن, N sınıfı; i'râb ACC 3 · NOM 1; bab I ×1 · bab IV ×1 · bab VIII ×1; **zaman IMPF ×3 — üç şart fiili, üç ayrı bab**; kök ikilemesi أله *(ilâh; lafza-i celâl)* ×2 · yıldız ★★★ · kökler طوع *(güç yetirme, itaat)* · أله · رسل *(gönderme, elçi)* · خشي *(haşyet, saygıyla korkma)* · وقي *(sakınma, koruma)* · فوز *(kurtuluş, fevz)* · bağ: **24:51 ↔ 24:52 = 23:102 ↔ 23:111 — aynı fâsıla çifti, aynı sırada; orada dokuz ayet ara, burada bitişik** (elle, L1, aday 515)",
}

MERCEK={
46:"Kuşak kapanıyor ve kapanış ayeti sûrenin açılış üçlüsünü dördüncü kez getiriyor — bu kez 24:34'ün biçimiyle birebir: أَنزَلْنَآ ءَايَٰتٍ مُّبَيِّنَٰتٍ *(açıklayıcı âyetler indirdik)*. Üçlünün son iki geçişi aynı sıfatı taşıyor, ilk ikisi ayrı. Ölçülebilir bir bağ: kuşağın açılışı (24:36) ile kapanışı (24:46) arasında on ayet, ve kuşağın hemen öncesinde de aynı üçlü vardı (24:34). Kuşak iki ucundan aynı formülle çevreleniyor.",
47:"Ayet bir alıntıyla açılıyor ve alıntının içeriğiyle kapanışını aynı kökle karşıtlıyor: ءَامَنَّا *(inandık)* — بِٱلْمُؤْمِنِينَ *(mü'minler … değil)*; birincisi kendi ağızlarından, ikincisi anlatıcının hükmü. İddia ile hüküm aynı sözcük üzerinden çarpışıyor. Dönüş bir zaman belirteciyle işaretleniyor: مِّنۢ بَعْدِ ذَٰلِكَ *(bunun ardından)*. فَرِيق *(bir bölük)* sûrede ilk kez ve hemen bir sonraki ayette ikinci kez.",
48:"İki ayet üst üste aynı adsız aktörle ve aynı hareketle bitiyor: يَتَوَلَّىٰ *(yüz çevirir)* — مُّعْرِضُونَ *(yüz çevirenler)*, iki ayrı kök, aynı hareket. Ölçülebilir olan çağrının çatısı: دُعُوٓا۟ *(çağrıldılar)* edilgen, çağıran adlandırılmıyor, ama çağrının hedefi iki kez adlandırılıyor. Bu sekiz kelimelik çağrı kalıbı üç ayet sonra harfi harfine geri gelecek, tek fark sonuçta.",
49:"Sûrenin dört hapaksından ikincisi ve fâsılanın kendisi: مُذْعِنِينَ *(boyun eğerek koşanlar)*, ism-i fâil çoğulu. Kök korpusta tek geçişli, dikey komşuluğu boş. Ölçülebilir bir yapı: şart cümlesi yedi kelimede kuruluyor ve 24:48'in tersini veriyor — orada hüküm için çağrılınca yüz çevrilmişti, burada hüküm kendi lehlerineyse koşuluyor. Bloğun tek lafızsız ayeti.",
50:"Üç seçenekli bir soru ve üçü de reddediliyor — بَلْ *(hayır)* ile, IDRAB. Ölçülebilir bir dizilim: hastalık (durum), şüphe (fiil, PERF), korku (fiil, IMPF); seçenekler hâlden eyleme, geçmişten şimdiye gidiyor. İki hapaks arka arkaya iki ayette (ذعن *(boyun eğerek koşma)* 24:49, حيف *(haksızlık)* 24:50) ve ikisi de aynı z ile ★★★. Dikey ölçüm مرض *(hastalık)* ▸önce kalp ×31,5 · nifak ×26,0 veriyor — kalp-hastalık çifti korpusta zaten sabit ve nifakla bağlı.",
51:"24:48'in sekiz kelimelik çağrı kalıbı harfi harfine geri geliyor ve yalnız cevap değişiyor: orada bir bölük yüz çevirmişti, burada mü'minler سَمِعْنَا وَأَطَعْنَا *(işittik ve itaat ettik)* diyor. Ölçülebilir bir HASR: إِنَّمَا … أَن يَقُولُوا۟ *(ancak … demektir)* — mü'minlerin sözü tek bir formüle indirgeniyor. 24:47'nin alıntısıyla karşıtlık: orada ءَامَنَّا … وَأَطَعْنَا *(inandık … itaat ettik)* denmiş ama yüz çevrilmişti; burada aynı itaat sözü, ama önüne işitme konmuş. Fâsıla 23:102'nin fâsılasıyla aynı.",
52:"Sûre 23'ün kurtuluş çifti burada bitişik iki ayette dönüyor. 23:102 ٱلْمُفْلِحُونَ *(kurtuluşa erenler)* ve 23:111 ٱلْفَآئِزُونَ *(kazananlar)* ile bitiyordu; 24:51 ve 24:52 aynı iki kelimeyle, aynı sırada. Ölçülebilir fark: orada dokuz ayet ara, burada sıfır. Bu ayette üç şart fiili üç ayrı bab: طوع *(güç yetirme, itaat)* bab IV, خشي *(haşyet, saygıyla korkma)* bab I, وقي *(sakınma, koruma)* bab VIII. 23:57-61 zincirinde haşyet ile takvâ Rab'be bağlıydı; burada ikisi de lafza bağlı — sûrenin Rab-sızlığı bu ayette de görünüyor.",
}

ATLAMA={
 "24:49":"★★★ ayet. 🜁 biyolog ve 🜂 uzay YAZILMADI — dört kökün (كون *(olmak)* · حقق *(hak)* · أتي *(gelme)* · ذعن *(boyun eğerek koşma)*) hiçbiri canlıya, organa, sürece ya da gök öğesine bağlanmıyor.",
 "24:50":"★★★ ayet. 🜁 biyolog YAZILMADI — مرض *(hastalık)* bir tıp terimi ama فِى قُلُوبِهِم *(kalplerinde)* tamlamasıyla ve dikey komşuluğu nifak ×26,0; gönderge zihinsel-ahlâkî bir durum. Patolojik okumayı seçmek yasaklı 'bilimsel izdüşüm' olurdu — 23:104'teki gerekçe sınıfı. 🜂 uzay YAZILMADI — gök öğesi yok.",
 "24:52":"★★★ ayet. 🜁 biyolog ve 🜂 uzay YAZILMADI — altı kökün hiçbiri çıpa vermiyor.",
 "_blok_notu_24_46_52":"Blok 24:46-52'de üç ★★★ ayet (49, 50, 52) ve üçünde de iki mercek atlandı. Kaynaklar: iki hapaks (z=3,38) ve bir allah z (3,47). Sûre 24 toplamı: on beş ★★★'ın on dördünde mercek atlandı, yalnız 24:35'te yazıldı.",
}

p='/home/claude/repo/notlar/okuma_metni.json'
OM=json.load(open(p,encoding='utf-8'))
for n in range(46,53):
    OM['24']["24:%d"%n]={"ar":AR[(24,n)],"meal":MEAL[n],"olcum":OLCUM[n],
                         "mercek":MERCEK[n],"dikey":DIK["24:%d"%n]}
OM['24']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not']=("Sûre 23 TAM (118/118). Sûre 24 (Nûr) makro profil + 24:1-52 okundu. "
                       "Devam: 24:53. Kafiye kuşağı 24:46'da KAPANDI (doğrulandı). Sûrede 12 ayet kaldı.")
OM['ilerleme']['kismi']={"2":"1-20 ayet düzeyinde","24":"1-52 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet']=1633
json.dump(OM,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('okuma_metni: sûre 24 →',len([k for k in OM['24'] if not k.startswith('_')]),'ayet')

pm='/home/claude/repo/notlar/mercek_kayit.json'
MK=json.load(open(pm,encoding='utf-8'))
for n in range(46,53): MK['24']["24:%d"%n]=MERCEK[n]
MK['24_atlama'].update(ATLAMA)
json.dump(MK,open(pm,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('mercek_kayit: sûre 24 →',len(MK['24']),'mercek')

pb='/home/claude/repo/notlar/okuma_baglantilari.json'
d=json.load(open(pb,encoding='utf-8'))
d['AD_nur'] += [
 {"bag":"24:34 ↔ 24:46","kural":"L1","not":"Aynı biçim: أَنزَلْنَآ ءَايَٰتٍ مُّبَيِّنَٰتٍ *(açıklayıcı âyetler indirdik)*. Kafiye kuşağı (24:36-45) iki ucundan bu üçlüyle çevreleniyor — 24:34 hemen önce, 24:46 kapanışta (adaylar 507, 509)."},
 {"bag":"24:47 ↔ 24:48","kural":"L1","not":"Ferîk çifti: aynı adsız aktör, aynı hareket (yüz çevirme) iki ayrı kökle — ولي *(velâyet)* bab V / عرض *(yüz çevirme)* (aday 514)."},
 {"bag":"24:48 ↔ 24:51","kural":"L1","not":"Aynalı çağrı kalıbı: إِذَا دُعُوٓا۟ إِلَى ٱللَّهِ وَرَسُولِهِۦ لِيَحْكُمَ بَيْنَهُمْ sekiz kelime birebir; sonuç ters — مُّعْرِضُونَ *(yüz çevirenler)* / سَمِعْنَا وَأَطَعْنَا *(işittik ve itaat ettik)* (aday 514)."},
 {"bag":"24:47 ↔ 24:51 (alıntı)","kural":"L1","not":"İki alıntı aynı fiili paylaşıyor: ءَامَنَّا … وَأَطَعْنَا *(inandık … itaat ettik)* reddediliyor, سَمِعْنَا وَأَطَعْنَا *(işittik ve itaat ettik)* onaylanıyor. Fark birinci fiilde: iman → işitme."},
 {"bag":"24:49 ↔ 24:50 (hapaks)","kural":"L1","not":"Ardışık iki hapaks: ذعن *(boyun eğerek koşma)* ve حيف *(haksızlık)*; ikisi de z=3,38 ile ★★★; حيف'in Allah medyan mesafesi 1."},
 {"bag":"23:102/23:111 ↔ 24:51/24:52","kural":"L1","not":"Kurtuluş çifti iki sûrede aynı sırada: ٱلْمُفْلِحُونَ *(kurtuluşa erenler)* sonra ٱلْفَآئِزُونَ *(kazananlar)*, ikisi de فَأُو۟لَٰٓئِكَ هُمُ kalıbıyla. Ara 9 → 0 (aday 515)."},
 {"bag":"23:57-61 ↔ 24:52","kural":"L2","not":"خشي *(haşyet)* ve وقي *(takvâ)* çifti: sûre 23'ün ikinci sıfat zincirinde Rab'be bağlı, 24:52'de lafza bağlı — sûre 24'ün Rab-sızlığı (aday 498) bu çiftte de görünüyor."},
]
json.dump(d,open(pb,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('AD_nur',len(d['AD_nur']),'bağ')
