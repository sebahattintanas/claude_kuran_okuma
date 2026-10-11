# -*- coding: utf-8 -*-
"""zumer_kayit.py — sûre 39 (Zümer) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 39

CIPA = {
 # blok 1-10
 4: dict(kademe=None, olgu=False, cipa=False, not_='tarayıcı v4 adayı (A_şart; خلق): çocuk edinme varsayımı — doğal olgu yok, merdiven uygulanmadı'),
 5: dict(kademe='L1', olgu=True, cipa=False, not_="gece/gündüz karşılıklı tekvîr + güneş/ay boyun eğdirme + adı konmuş süreye akış; süreç fiili adlanıyor (sarma), ara durum/birim/nedensellik yok; 31:29 ve 35:13 aynı terkip L1 ('yûlicu' → 'yukevviru')"),
 6: dict(kademe='L1', olgu=True, cipa=False, not_="tek nefis → eş; davarlardan sekiz çift; karında aşama ardışıklığı + yer (üç karanlık); ara aşama adsız, nedensellik yok; 'sekiz çift' sınıf sayısı ama üye eşlemesi yok (1014; eşleme 6:143-144'te); 'üç karanlık' sayı + nesne, birim yok — L4 ölçü/sınıf koluna sınırda (36:39 emsalinin tersi), KAPATILAMAZ; tarayıcı v4 adayı (F_ölçü), çıpa değil"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="tarayıcı v4 adayı (B_ta'lîl; نور — burada nâr): doğal olgu yok, merdiven uygulanmadı"),
 9: dict(kademe='L0', olgu=True, cipa=False, not_="gece saatleri yalnız ibadet vakti olarak adlanıyor; nitelik/süreç/ölçü yok"),
 10: dict(kademe='L1', olgu=True, cipa=False, not_="yer + nitelik (geniş); süreç/ölçü yok; bağlam ahlâkî (4:97 hicret emsali) — doğal olgu iddiası sınırda, KAPATILAMAZ; tarayıcı v4 adayı (D_yeti), çıpa değil"),
 # blok 21-30
 21: dict(kademe='L4', olgu=True, cipa=True, not_="MEKANİZMA kolu: su → yerde kaynaklar → ekin (renkleri farklı) → kabarıp kuruma → sararma → çer çöp; beş aşama 'fe'/'summe' ile türetiliyor, ara durumlar adlı (yenâbî', zer', musfarr, hutâm), suyun yolu adlanıyor — 30:48 emsali; 35:27 aynı açılış tek aşama L2; 'fe-terâhu' görme ama algı/durum ayrımı yok (L3 değil); tarayıcı v4 adayı (G_bakış) — isabet"),
 26: dict(kademe=None, olgu=False, cipa=False, not_="tarayıcı v4 adayı (A_şart; حيي — 'el-hayâtu'd-dunyâ'): doğal olgu yok, merdiven uygulanmadı"),
 # blok 31-40
 38: dict(kademe='L0', olgu=True, cipa=False, not_="gökler ve yer yalnız yaratılan olarak adlanıyor (soru içinde); süreç/ölçü yok (38:10, 38:66 emsali); tarayıcı v4 adayı (A_şart, G_bakış), çıpa değil"),
 # blok 41-50
 42: dict(kademe='L4-biçim', olgu=True, cipa=False, not_="sınıflama biçimi: ölüm/uyku aynı süreçle (teveffî), sonra ölçütle iki sınıf + akıbet eşlemesi (imsâk / adı konmuş süreye irsâl) — 29:40 eşleme ölçütü biçimce karşılanıyor; ama sınıflanan 'nefs' ve süreç gözlenebilir değil: olgu koşulu sınırda (aday 1002 ailesi, 34:12 emsali); tarayıcı vermedi"),
 44: dict(kademe='L0', olgu=True, cipa=False, not_="gökler ve yer yalnız mülk olarak adlanıyor; süreç/ölçü yok (38:10 emsali)"),
 46: dict(kademe='L0', olgu=True, cipa=False, not_="gökler ve yer yaratılan olarak ('fâtır') adlanıyor; süreç/ölçü yok (39:38 emsali)"),
 47: dict(kademe=None, olgu=False, cipa=False, not_="tarayıcı v4 adayı (A_şart; أرض — 'mâ fi'l-ardı cemî'an'): varsayım içinde mülk; doğal olgu yok, merdiven uygulanmadı"),
 63: dict(kademe='L0', olgu=True, cipa=False, not_="gökler ve yer yalnız 'anahtarları O'nun' olarak adlanıyor; süreç/ölçü yok (39:44 emsali)"),
 67: dict(kademe='L0', olgu=True, cipa=False, not_="yer 'avucu', gökler 'sağında dürülmüş' — kıyamet tasviri; doğal süreç/ölçü iddiası yok (39:63 emsali); tarayıcı aday vermedi"),
 68: dict(kademe='L0', olgu=True, cipa=False, not_="göklerdekiler ve yerdekiler adlanıyor (sûr sahnesi); süreç/ölçü yok (27:87 emsali)"),
 69: dict(kademe='L1', olgu=True, cipa=False, not_="yer + nitelik (Rabbinin nuruyla aydınlanma) — kıyamet sahnesi; mekanizma/ölçü yok (39:10 emsali L1); doğal olgu iddiası KAPATILAMAZ"),
 74: dict(kademe='L0', olgu=True, cipa=False, not_="yer yalnız miras olarak adlanıyor ('evrasena'l-ard') — cennet sahnesi; süreç/ölçü yok (39:63 emsali)"),
}

ARIZA = {
 (1, 10): [
  "veri: 39:1 Arapça satırında besmele ayet metnine bitişik (harf 47 → harf3 28; n=6 besmelesiz) — veri biçimi, 38:1 ile aynı",
  "gloss: نهر 'ırmak' — 39:5 nehâr (gündüz) (1021); ظلم 'zulüm' — 39:6 zulumât (karanlık) (1015); أخر 'geciktirme' — 39:7 uhrâ, 39:9 âhira (1000 ailesi)",
  "gloss (1021 ailesi, baskın olmayan): أمم 'ümmet, topluluk' — 39:6 ummehât (anneler); morph lemma umm 35 segment, ümmet 64 — 'anne' anlamı gloss'ta yok",
  "biçim: 39:9 ve 39:10 'innemâ' hasrı biçim alanında yok (517 ailesi); 39:3 takdimli 'li'llâhi'd-dîn' işaretlenmiyor (RES 1 alıntı içi 'mâ … illâ')",
  "alıntı sınırı: 39:3 giriş fiilsiz alıntı (1P 2) — 1017 ailesi; 39:10 'qul' içinde 1S hitap ('yâ ibâdi')",
  "sayı işareti: 39:6 zevc/ezvâc (eş/çift, sınıf adı) ve 39:8 qalîl (azlık sıfatı) yanlış pozitif; 39:4 vâhid, 39:6 vâhide/semâniye/selâs doğru",
  "esmâ: 39:3 veliyy (evliyâ) ve 39:9 âhir (âhira) 'degil'; 39:1 azîz+hakîm, 39:4 qahhâr, 39:5 azîz+ğaffâr, 39:7 ğaniyy+alîm 'ilahi'",
 ],
 (11, 20): [
  "esit2: 39:13 ölçüm satırında 6:15 iki kez listeleniyor (aynı ayet, aynı oran) — araç tekrarı",
  "gloss (987 ailesi): ظلل 'sürüp gitme' — 39:16 zulel (gölgelik); morph lemma zıll 14 + zulle 6, zalle 9; نور 39:16, 39:19 nâr",
  "gloss (1021 ailesi): جنب 'yan, taraf' — 39:17 ictinâb (kaçınma); lemma ictenebe 9, cânib 9, cenb 8",
  "biçim: 39:14 takdimli nesne (lafız) hasrı biçim alanında yok (517); 39:15 tehdit emri ayrı işaretlenmiyor",
  "alıntı/şahıs: 39:16 aynı ayette 3 ('ibâdehû') → 1S ('yâ ibâdi fe'ttaqûn'), iltifât 0 (1017 ailesi); 39:17 'ibâdi' 1S",
  "esmâ: 39:12 evvel ve 39:15 mubîn 'degil'",
  "çıpa: blokta değerlendirilen ayet yok — 39:16 ve 39:20 âhiret tasviri (ateş gölgelikleri, gurfeler/ırmaklar), tarayıcı v4 aday vermedi",
 ],
 (21, 30): [
  "çıpa: 39:21 L4 (mekanizma kolu, 30:48 emsali) — tarayıcı v4 isabeti; sûre 33-38'de L4 yoktu",
  "gloss (987): نور 39:22 nûr — sûrede ilk ışık anlamı (39:8, 39:16, 39:19 nâr); gloss iki anlamı da taşıyor, baskın nâr",
  "sayı işareti: 39:23 mesânî (ikişer/tekrarlanan) sınırda, 39:29 ekser (çokluk) yanlış pozitif",
  "◈B tetik listesi: 39:29 'racul' ×3 (رجل listede yok — 38:42 kaydı); 39:24 'vech' (وجه listede yok)",
  "hazfli karşılaştırma sorusu: 39:9, 39:19, 39:22, 39:24 — biçim alanı yalnız INTG yazıyor, hazf işaretlenmiyor (517 ailesi)",
  "esmâ: 39:22 nûr ve mubîn, 39:23 hâd, 39:26 âhir 'degil'",
  "hapaks: 39:23 قشعر ve 39:29 شكس — iki kök de bu sûre için kok_ekle_39'da tabloya eklendi (★★★ kaynağı)",
 ],
 (31, 40): [
  "iltifât alanı: 39:32 ve 39:40 iltifât 1 — ayet içinde tek şahıs (3MS); alan ayetler arası geçişi (2MP → 3MS) sayıyor (1017 ailesi)",
  "gloss (1021 ailesi): كفر 'inkâr, nankörlük' — 39:35 tekfîr (II. bab: örtme, silme) yok",
  "biçim: 39:33 'ulâike humu'l-muttaqûn' zamir-i fasl hasrı ve 39:38 takdimli 'aleyhi' hasrı biçim alanında yok (517)",
  "esmâ: 39:36 hâd 'degil' (39:23 emsali); 39:37 azîz 'ilahi'",
  "aday 1039 için karşıt çift kayıtları (okuma): 39:32↔39:33 kezzebe/saddeqa bi's-sıdq; 39:35 esve'/ahsen; 39:36↔39:37 yudlil-hâd / yehdi-mudill; 39:38 durr/rahmet, kâşifât/mumsikât",
 ],
 (41, 50): [
  "lafız ekseni: 39:46 'Allâhumme' lafız sayılmıyor ('lafız YOK') ama أله kök sayımına giriyor [45/61]; aktör alanı 'Allâhumme'yi adlı aktör, rol 'konuşan+meful' yazıyor — nidâ edilen muhatap",
  "çıpa: 39:42 'L4-biçim' (sınıflama biçimi, olgu sınırda) — aday 1002 ailesi; tarayıcı vermedi",
  "biçim: 39:41 ve 39:49 'innemâ', 39:44 takdimli 'li'llâhi' hasrı biçim alanında yok (517)",
  "sayı işareti: 39:45 vahd (teklik) doğru; 39:49 ekser yanlış pozitif",
  "esmâ: 39:41 vekîl ve 39:45 âhir 'degil'; 39:46 âlim 'ilahi'",
  "aday 1039 karşıt çiftleri (okuma): 39:41 ihtidâ/dalâl; 39:42 ölüm/uyku, imsâk/irsâl; 39:45 Allah tek anılınca tiksinme / başkaları anılınca sevinme; 39:46 gayb/şehâde; 39:8↔39:49 aynı sahne 3. şahıs / 1P",
 ],
 (51, 60): [
  "gloss (1021 ailesi): سخر 'boyun eğdirme' — 39:56 sâhirîn (alay edenler) yok; حسر 'yorgunluk, bitkinlik' — 39:56 hasret (pişmanlık) yok",
  "biçim: 39:51 DIKKAT 'hâulâi' işaret isminden (ölçüm); 39:56 'en teqûle' olumsuz amaç (li-ellâ) okuması biçimde yok",
  "şahıs: 39:56-58 'nefs' 3FS + alıntı içi 1S → 39:59 hitap 2MS (eril); iltifât alanı 0 — alıntı sınırı (1017 ailesi)",
  "esmâ: 39:53 ğafûr + rahîm 'ilahi' (mühür ÇİFT); 39:60 mutekebbir 'degil'",
  "çıpa: blokta değerlendirilen ayet yok; tarayıcı v4 aday vermedi",
  "aday 1039 karşıt çiftleri (okuma): 39:51 öncekiler PERF / bunlar FUT; 39:52 yebsutu / yaqdiru; 39:52 esit2 30:37 YAKIN — 'yerav' / 'ya'lemû' (görme / bilme)",
 ],
 (61, 70): [
  "gloss: نور 'nûr, ışık; nâr, ateş' — kök ipliği 39:8-19 nâr ile 39:22-69 nûr'u birleştiriyor (okuma ayırıyor); وفي 'tam verme; vefat ettirme' iki anlam — 39:42 / 39:70 ayrımı okumada",
  "biçim: 39:66 'beli'llâhe fa'bud' takdim hasrı biçim alanında yok (517 ailesi; IDRAB yalnız 'bel'den); 39:64 'e-fe-ğayra'llâhi' takdimi de işaretsiz (DIKKAT ölçüm)",
  "zaman: 39:68-70 kıyamet sahnesi PERF ile anlatılıyor (zaman alanı PERF sayar; geleceğe gönderme okumada)",
  "iltifât: 39:64 1S/2MP alıntı içi, 39:67 3MP→3MS — iltifât alanı 1 (1017 ailesi: alıntı / ayet içi zamir değişimi ayrımı yok)",
  "esmâ: 39:62 hâliq + vekîl 'ilahi' (ölçüm MÜHÜRSÜZ, bilanço geçerli — 1022 ailesi); 39:66 şâkir, 39:69 nûr + şehîd 'degil'",
  "çıpa: 39:63, 39:67, 39:68 L0; 39:69 L1; tarayıcı v4 aday vermedi; L4 yok",
  "aday 1039 karşıt çiftleri (okuma): 39:61 sakınanlar kurtulur / 39:63 inkâr edenler kaybeder; 39:11-12 'umirtu' / 39:64 'te'murûnnî'; 39:64 soru / 39:66 emir; 39:67 yer avuçta / gökler sağda dürülü; 39:68 birinci üfleniş bayılma / ikinci üfleniş kalkış",
 ],
 (71, 75): [
  "gloss: ملك 'mülk; melik' — 39:75 melâike (melekler) yok; حول 'çevirme, değiştirme' — 39:75 'min havli'l-arş' (çevre) yok; علم 'bilme' — 39:75 'âlemîn' (âlemler) yok (1021 ailesi)",
  "biçim: 39:71 DIKKAT 'hâzâ' işaret isminden (ölçüm); 39:73 'hattâ izâ … ve futihat' — izâ'nın cevabının söylenmemesi biçim alanında yok",
  "alıntı sınırı: 39:71 've lâkin haqqat kelimetu'l-azâb' cevabın parçası mı anlatıcı mı — alan ayırmıyor, metin de işaretlemiyor (KAPATILAMAZ)",
  "nakarat3: 39:71 ↔ 39:73 9 kelimelik ortak gövde GEÇER — karşıt ayetlerin ortak iskeleti; ayrışan öğeler (keferû/ittekav, cehennem/cennet, futihat/ve futihat, soru/selâm) alanda kayıtlı değil, okumada",
  "esmâ: 39:72 mutekebbir, 39:73 selâm 'degil'; bilanço geçerli mühür yok",
  "çıpa: 39:74 L0 (yer mirası); tarayıcı v4 aday vermedi; L4 yok",
  "aday 1039 karşıt çiftleri (ölçüm + okuma): 39:71 / 39:73 ('zumeran' korpusta yalnız bu 2 ayet); 39:72 'udhulû … hâlidîne fîhâ' / 39:73 'fedhulûhâ hâlidîn'; 39:59 'belâ' (1S) / 39:71 'qâlû belâ'; 39:60 / 39:75 'terâ' (kararmış yüzler / Arş'ı kuşatan melekler)",
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_39.py uygular)
DUZELTME = {
}
