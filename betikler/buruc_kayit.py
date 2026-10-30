# -*- coding: utf-8 -*-
"""buruc_kayit.py — sûre 85 (Burûc) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 85

CIPA = {
 # blok 1-9
 1: dict(kademe='L1', olgu=True, cipa=False, not_="'ve's-semâ'i zâti'l-burûc' — gök, nitelik adlanıyor (burçlar); süreç / ölçü yok — L1 (51:7 kaydı emsali); tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'ve'l-yevmi'l-mev'ûd' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ve şâhidin ve meşhûd' — gönderge adsız; merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'qutile ashâbu'l-uxdûd' — kıssa, insan yapımı hendek (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'en-nâri zâti'l-veqûd' — insan yapımı ateş (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'iz hum 'aleyhâ qu'ûd' — insan davranışı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'ve hum 'alâ mâ yef'alûne bi'l-mu'minîne şuhûd' — insan davranışı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ neqamû minhum illâ en yu'minû bi'llâh …' — insan davranışı, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 9: dict(kademe='L0', olgu=True, cipa=False, not_="'elleżî lehû mulku's-semâvâti ve'l-ard …' — gökler ve yer mülk tamlamasında; süreç / ölçü yok — L0; tarayıcı vermedi"),
 # blok 10-16
 10: dict(kademe=None, olgu=False, cipa=False, not_="'inne'llezîne fetenu'l-mu'minîne …' — insan davranışı, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 11: dict(kademe=None, olgu=False, cipa=False, not_="'… lehum cennâtun tecrî min tahtihe'l-enhâr …' — âhiret, cennet (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'inne batşa rabbike le-şedîd' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'innehû huve yubdi'u ve yu'îd' — gaybî, nesnesiz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="'ve huve'l-ğafûru'l-vedûd' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'zu'l-'arşi'l-mecîd' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 16: dict(kademe=None, olgu=False, cipa=False, not_="'fe''âlun limâ yurîd' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 17-22
 17: dict(kademe=None, olgu=False, cipa=False, not_="'hel etâke hadîthu'l-cunûd' — kıssa, soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 18: dict(kademe=None, olgu=False, cipa=False, not_="'fir'avne ve themûd' — kıssa, yalnız adlar (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 19: dict(kademe=None, olgu=False, cipa=False, not_="'beli'llezîne keferû fî tekzîb' — insan davranışı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 20: dict(kademe=None, olgu=False, cipa=False, not_="'ve'llâhu min verâ'ihim muhît' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 21: dict(kademe=None, olgu=False, cipa=False, not_="'bel huve qur'ânun mecîd' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 22: dict(kademe=None, olgu=False, cipa=False, not_="'fî levhin mahfûz' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 9): [
  "esmâ: e_oto 4 token — 85:7 'mu'min' ('bi'l-mu'minîn', insan çoğulu) DEĞİL; 85:8 ''azîz', 'hamîd' ve 85:9 'şehîd' İLÂHÎ; KARAR 703 → 707; ölçüm mührü 3 (85:7, 8, 9), bilanço geçerli 2 (85:8, 9); 85:9 ölçüm 'MÜHÜRSÜZ' / geçerli — mühür iddiası bilançodan (1022)",
  "lafız: sûre içi 3 geçişin ikisi bu blokta (85:8, 9); Rab yok",
  "kök tablosu: yeni kök yok (1511); retroaktif yama hedefli 0, genel 0",
  "harf alanı: ayet 1 ölçümünde harf 35 → harf3 16, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924)",
  "yıldız: ★★★ 85:4 pas z=5,38; ★ 85:8 allah z=1,69 — formül davranışı, içerik iddiası değil",
  "biçim / kip (924): 85:2-3 atıflı yeminlerde QASEM yok; 85:6 'iz' kip alanında yok; 85:1 QASEM, 85:8 HASR (NEG + RES) doğru",
  "KAPATILAMAZ: 85:3 tanıklık eden / edilen; 85:1-3 yeminin cevabı — 85:4 'qutile' cevap mı beddua mı işaretli değil; 85:2 hangi gün",
  "adsız gönderge (1017): 85:2 vaat eden; 85:4 öldüren; 'ashâbu'l-uxdûd'; 85:7 'el-mu'minîn'; konuşan adsız",
  "gloss (1021): kök نور 'nûr; nâr' — burada ateş; kök خدد 'yanak; yarık' — burada hendek",
  "kök شهد sûre içi 4/4 bu blokta: 85:3 ikilemesi, 85:7 'şuhûd', 85:9 'şehîd' — tanıklık üç göndergeye (adsız / hendeğin sahipleri / Allah; okuma)",
  "fâsıla: 85:1 ج, 85:2-9 د — ج → د (85:1 → 2) gerçek geçiş, bilanço kafiye kırığı işaretlemedi (924)",
  "esit2: 85:9 BENZER → 3:189 (henüz okunmadı); xref 85:8 → 5:59 (henüz okunmadı)",
  "aday 1040 (kayıt): 84:25 / 85:1 sûre sınırı — istisna + 3MP / yemin, şahıs işareti yok; ikisi de lafızsız, Rabsız; fâsıla ن → ج",
  "bağ: kalıp / lemma eşleri okumayla (51:7, 15:16, 25:61, 11:103, 17:78, 51:10, 74:20, 80:17, 66:6, 9:83, 9:74, 58:6); 86:11, 5:59, 3:189 henüz okunmadı — bağ yazılmadı",
  "◈K / ◈B: ◈K dolu 85:1 سمو, 85:2 يوم, 85:9 سمو أرض; ◈B tetik yok; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 26 sayım 0 uyuşmaz",
  "süreç: sûre 85 dosyaları insikak_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_85.py, oturum dışı); kapanış / paket blok listesi BLOK_LISTESI_ELLE",
 ],
 (10, 16): [
  "esmâ: e_oto 5 token — 85:10 'mu'min' (insan çoğulu) ve 85:11 'kebîr' ('el-fevzu'l-kebîr') DEĞİL; 85:14 'ğafûr', 'vedûd' ve 85:15 'mecîd' İLÂHÎ; KARAR 707 → 712; ölçüm mührü 3 (85:11, 14, 15), bilanço geçerli 2 (85:14, 15); 85:15 ölçüm 'MÜHÜRSÜZ' / geçerli (1022)",
  "85:15 'el-mecîdu' merfû — 'zû'nun sıfatı (ölçüm i'râb NOM 2); karar metindeki i'râbdan",
  "Rab: 85:12 sûrenin ilk Rab'ı; 85:13-16 zamir / haber dizisi Rab'a (okuma); lafız bu blokta yok",
  "kök tablosu: yeni kök yok (1511); retroaktif yama hedefli 0, genel 0",
  "yıldız: ★★★ 85:12 rab z=5,01 (lafızsız kısa ayette Rab) — formül davranışı",
  "iltifât: 85:12 {3} → {2} ve 85:13 {2} → {3} gerçek",
  "biçim / kip (924): 85:10, 11, 13 'inne' tekidi kip alanında yok; 85:13 fasl zamiri 'huve' biçim alanında yok; 85:12 EMPH doğru",
  "KAPATILAMAZ: 85:10 fitneye uğratanların 85:4-7 hendeğin sahipleriyle aynılığı; 85:13 başlatılan / döndürülen (nesnesiz)",
  "fâsıla (924): 85:10 ق, 85:11 ر, 85:12-16 د — د → ق → ر → د geçişleri bilançoda kafiye kırığı işaretlenmedi",
  "aday 1041 (kayıt): kök فعل 85:7 'yef'alûn' (hendeğin sahipleri) / 85:16 'fe''âl' (Rab); kök شهد 85:7 'şuhûd' (hendeğin sahipleri) / 85:9 'şehîd' (Allah)",
  "aday 1040 ailesi (okuma): 84:25 / 85:11 'âmenû ve 'amilu's-sâlihâti lehum' — 'illâ' / 'inne'; 'ecrun ğayru memnûn' / 'cennât'",
  "bağ: kalıp / lemma eşleri okumayla (22:9, 22:22, 41:8, 84:25, 43:8, 50:36, 29:19, 34:49, 11:90, 40:15, 81:20, 11:73, 50:1, 11:107); 85:21 henüz okunmadı — bağ yazılmadı",
  "süreç: tetik ön kuru koşu kayıttan önce 85:11 ◈K'de tetiklenmiş satırı '—' yakaladı (نهر 'el-enhâr') — satır dolduruldu; ikinci koşu 0 uyuşmaz",
  "◈K / ◈B: ◈K dolu 85:11 نهر; ◈B tetik yok; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 25 sayım 0 uyuşmaz",
 ],
 (17, 22): [
  "esmâ: e_oto 2 token — 85:20 'muhît' İLÂHÎ; 85:21 'mecîd' ('qur'ânun mecîd') DEĞİL; KARAR 712 → 714; ölçüm mührü 2 (85:20, 21), bilanço geçerli 1 (85:20; ölçüm 'MÜHÜRSÜZ' yazıyordu — 1022)",
  "lafız: sûre içi 3/3 (85:8, 9, 20) — sûre bütünü lafız 3, Rab 1 (85:12)",
  "kök tablosu: yeni kök yok (1511); retroaktif yama hedefli 0, genel 0",
  "yıldız: ★★★ 85:20 allah z=4,47 (lafızlı kısa ayet) — formül davranışı",
  "aktör (1038 ailesi): 85:18 'fir'avn' / 'themûd' rol mecrur — bedel (okuma); 85:21 'qur'ân' rol fail — haber (okuma)",
  "biçim (924): 85:21 'bel' idrâb biçim alanında yok (85:19'da IDRAB var)",
  "KAPATILAMAZ: 85:19 yalanlanan; 85:21 'huve' zamirinin göndergesi; 85:22 levha (nekre)",
  "adsız gönderge (1017): 85:17 muhatap 2MS; 85:22 koruyan; konuşan adsız",
  "gloss (1021): kök لوح 'levha; kavurup değiştirme'",
  "fâsıla (924): 85:17-18 د, 85:19 ب, 85:20 ط, 85:21 د, 85:22 ظ — sûre sonunda dört geçiş, bilanço kafiye kırığı işaretlemedi",
  "aday 1040 (kayıt): ardışık sûrede iki ayetlik sıralı eşleşme 84:22-23 / 85:19-20 — 'beli'llezîne keferû' + yalanlama, ardından 've'llâhu' + lafız + haber (a'lem / muhît)",
  "aday 1041 (kayıt): lemma 'mecîd' 85:15 (Rab) / 85:21 (Kur'ân)",
  "bağ: kalıp / lemma eşleri okumayla (51:24, 79:15, 38:2, 84:22, 84:23, 11:92, 29:49, 50:1, 54:13, 21:32); 88:1 henüz okunmadı — bağ yazılmadı",
  "◈K / ◈B: ◈K, ◈B tetik yok; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, sûre geneli 22 / 0; oturum_xy 12 sayım 0 (sûre geneli 63 / 0)",
  "süreç: kullanıcı isteğiyle (2026-10-30) bu bloktan itibaren emsal listesinde her ayetin Türkçe meali de veriliyor — okunmuş ayetlerin meali okuma_metni kaydından alınır, elle yazılmaz",
 ],
}

DUZELTME = {
}
