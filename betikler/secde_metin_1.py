# -*- coding: utf-8 -*-
"""secde_metin_1.py — sûre 32 (Secde) meal ve matematikçi merceği, ayet 1-15."""
MEAL = {
 1: "Elif Lâm Mîm.",
 2: "Kendisinde şüphe olmayan bu Kitab'ın indirilişi âlemlerin Rabbindendir.",
 3: "Yoksa 'Onu uydurdu' mu diyorlar? Hayır, o, senden önce kendilerine bir uyarıcı gelmemiş bir kavmi uyarasın diye Rabbinden gelen gerçektir; belki doğru yolu bulurlar.",
 4: "Allah, gökleri, yeri ve ikisi arasındakileri altı günde yaratan, sonra Arş'a istivâ edendir. Sizin için O'ndan başka ne bir dost ne bir şefaatçi vardır. Hâlâ düşünüp öğüt almaz mısınız?",
 5: "İşi gökten yere doğru düzenler; sonra o, ölçüsü sizin saydıklarınızdan bin yıl olan bir günde O'na yükselir.",
 6: "İşte O, görünmeyeni de görüneni de bilendir; azîzdir, rahîmdir.",
 7: "O, yarattığı her şeyi güzel yapandır ve insanı yaratmaya çamurdan başlamıştır.",
 8: "Sonra onun neslini bayağı bir suyun özünden var etti.",
 9: "Sonra onu düzenledi ve ona ruhundan üfledi. Size kulaklar, gözler ve gönüller verdi. Ne kadar az şükrediyorsunuz!",
 10: "'Yerde kaybolup gittiğimizde mi, gerçekten yeni bir yaratılış içinde mi olacağız?' dediler. Hayır, onlar Rablerine kavuşmayı inkâr edenlerdir.",
}
M = {
 1: "◇ Altıncı ve son ALM açılışı; esit2 beş TAM bağ (2:1, 3:1, 29:1, 30:1, 31:1). Sûre 31 ile arka arkaya iki ALM sûresi.",
 2: "◇ ★★'nın tek kaynağı rab z=2,34: sekiz kelimelik ayette tek Rab — sûre 31:5'in aynısı. Sûre Rab ile açılıyor; 31 ise 32 lafız ve 2 Rab ile kapanmıştı.",
 3: "◇ نذر ×2. xref 28:46 ile dört ayrı üçlü kalıp paylaşıyor: 'uyarıcı gelmemiş kavim' kalıbı.",
 4: "◇ Sûrede lafız ilk ve şimdilik tek kez, hem de ayetin ilk kelimesi. 'Altı günde yaratma → sonra Arş'a istivâ': yaratılış sırası ölçümünde (bu oturum) ثُمَّ ile kurulan kenar, ama gök ile yer arasında değil, yaratılış ile istivâ arasında; o turda beş ayet saymıştık (7:54, 10:3, 25:59, 32:4, 57:4) — bu ayet o kümenin üyesi. Esmâ وَلِيّ burada Allah'ı göstermiyor ('O'ndan başka dost yok') → yanlış pozitif, üstelik ORTA konum.",
 5: "◇ 🜁 ÇIPA: L4 (ölçü) · olgu EVET. 'Ölçüsü sizin saydığınızdan bin yıl olan bir gün' açık bir ölçü ifadesi ve bir karşılaştırma taşıyor. TARAYICI v4 bu ayeti F_ölçü ailesiyle ADAY VERDİ — tarayıcının sûre 30 ve 31 boyunca süren sıfır anmasından sonra ilk isabeti. Aday 948'e karşı yönde ilk veri. xref 22:47 ve 70:4 (aynı ölçü kalıbının başka değerleri). Ölçülen şey bir SÜRE ORANI, mesafe değil; yükselişin hedefi bir yer değil, zamir ('O\'na'). TAM SAYIM: مِقْدار 3 ayette (13:8, 32:5, 70:4); 'O\'na yükseliş' iki ayette iki farklı süreyle: iş → 1.000 yıl (32:5), melekler ve Rûh → 50.000 yıl (70:4). Sayı yükselen şeye bağlı; sabit bir mesafe/hız okuması iki ayeti çelişkiye düşürür. Okuma, test değil.",
 6: "◇ Üç esmâ tek ayette (عالِم, عَزِيز, رَحِيم) ve üçü de geçerli; ayet sonu çifti mühürlü. esit2 → 64:18 BENZER (0,91).",
 7: "◇ Yaratılış sırası grafiğinde (bu oturum) 'çamur' düğümü: 32:7 → 32:8 kenarı ثُمَّ ile kuruluyor ve ölçümde طين → سُلالَة kenarının kaynağı tam olarak bu ayet çiftiydi. Kademe: madde adlandırma → L1, çıpa değil.",
 8: "◇ سُلالَة ve 'bayağı su' (yeni kök مهن). Grafikteki سُلالَة düğümü; 23:12-13'teki zincirin ikinci halkasıyla aynı yönde.",
 9: "◇ Grafiğin üçüncü kenarı: سَوَّى ve نَفَخَ, maddeden SONRA. Ölçümde bu sıra 15:28-29, 32:7-9 ve 38:71-72'den geliyordu; xref satırı 15:29 ve 38:72'yi zaten veriyor. İşitme, görme ve gönül burada 'verilen' olarak sayılıyor: 76:2'deki سَمِيع–بَصِير çiftiyle aynı hat (sıfatlar turundaki tek olumlu nitelik).",
 10: "◇ Yeni kök جدد. 'Rablerine kavuşmayı inkâr' kalıbı xref 30:8 ile bağlı. Rab sûrede üçüncü kez; buraya kadar A/R = 1/3, yani 31'in tam tersi bir eksen.",
}

MEAL.update({
 11: "De ki: Size vekil kılınan ölüm meleği canınızı alacak; sonra Rabbinize döndürüleceksiniz.",
 12: "Suçluları Rablerinin huzurunda başlarını önlerine eğmiş hâlde bir görsen: 'Rabbimiz, gördük ve işittik; bizi geri döndür de sâlih amel işleyelim; artık kesin olarak inanıyoruz.'",
 13: "Dileseydik her nefse hidayetini verirdik; fakat benden şu söz hak oldu: Andolsun cehennemi cinlerden ve insanlardan hep birlikte dolduracağım.",
 14: "Bu gününüze kavuşmayı unutmanızın karşılığını tadın; biz de sizi unuttuk. Yaptıklarınızın karşılığı olarak ebedî azabı tadın.",
 15: "Âyetlerimize ancak, onlarla öğüt verildiğinde secdeye kapanan, Rablerini hamd ile tesbih eden ve büyüklenmeyenler inanır.",
 16: "Yanları yataklardan uzaklaşır; Rablerine korku ve umutla dua ederler ve kendilerine verdiğimiz rızıktan harcarlar.",
 17: "Yaptıklarına karşılık olarak onlar için gizlenmiş göz aydınlığını hiçbir nefis bilmez.",
 18: "İnanan kişi, yoldan çıkmış kişi gibi olur mu? Bunlar eşit olmazlar.",
 19: "İman edip sâlih ameller işleyenler için, yaptıklarına karşılık bir ağırlama olarak Me'vâ cennetleri vardır.",
 20: "Yoldan çıkanlara gelince, onların barınağı ateştir. Oradan her çıkmak istediklerinde oraya geri döndürülürler ve onlara 'Yalanlamakta olduğunuz ateşin azabını tadın' denir.",
})
M.update({
 11: "◇ ★★'nın kaynağı pas z=2,52 (edilgen 2/4); rab z=1,62 ikinci. Bağ yok.",
 12: "◇ ★★ kaynağı rab z=2,34 (16 kelimede 2 Rab). 'Gördük ve işittik': 32:9'da verilen işitme ve gözler burada, iş işten geçtikten sonra dile geliyor (رأي, بصر, سمع sûre içinde ikinci kez).",
 13: "◇ Cehennem adlı aktör (yer). 'Cinlerden ve insanlardan dolduracağım' xref 11:119 ile aynı cümle.",
 14: "◇ Simetrik ceza: 'unuttunuz → biz de unuttuk' (نسي ×2). nakarat3 'بِمَا كُنتُمْ تَعْمَلُونَ' GEÇİYOR: 32:14, 32:17, 32:19'da sûre içi tekrar.",
 15: "◇ Sûreye adını veren secde ayeti. TAM SAYIM: kapanmak (خرر) + secde korpusta 4 ayette: 12:100, 17:107, 19:58, 32:15. خرر, Dâvûd merceğinde Dâvûd'u ayıran köklerden biriydi (38:24, 'rükûa kapandı').",
 16: "◇ ★★★'ın tek kaynağı hapaks جفو (hapaks z=3,28): sûre 31-32'de üçüncü otomatik hapaks ★★★ (borç #7). İki yeni kök burada: جفو, ضجع. TAM SAYIM: 'korku ve umutla dua' (دعو + خوف + طمع) korpusta yalnız iki ayette: 7:56 ve 32:16. 7:56 'Allah'ın rahmeti muhsinlere yakındır' ile sürüyor — dua taramasındaki yakınlık hattı.",
 17: "◇ 'Hiçbir nefis bilmez': 31:34'teki 'hiçbir nefis bilmez' ile ardışık iki sûrede bilgi sınırı (orada دري, burada علم). Edilgen 1/4 (أُخْفِىَ). nakarat3 GEÇİYOR.",
 18: "◇ Esmâ مُؤْمِن 'inanan kişi' anlamında → yanlış pozitif (P0 şüpheli lemma listesindeki vaka). 'Eşit olmazlar' (لَا يَسْتَوُۥنَ): سوي kökü sûrede üç kez ve üç ayrı anlamda — istivâ (32:4), düzenleme (32:9), eşitlik (32:18).",
 19: "◇ Sâlihât köprüsü ölçümünde 32:19 bir köprü çapası. TAM SAYIM: me'vâ + cennet 4 ayette: 5:72, 32:19, 53:15, 79:41. Necm dökümündeki 'sidrenin yanındaki Me'vâ cenneti' (53:15) burada iman ve sâlih amelin karşılığı olarak geçiyor.",
 20: "◇ 32:19 ile simetrik: me'vâ cennet (19) / me'vâ ateş (20); أوي sûrede iki kez, iki karşıt yer. xref 22:22 ('her çıkmak istediklerinde geri döndürülürler'), 34:42.",
})
