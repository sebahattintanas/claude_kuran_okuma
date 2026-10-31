# -*- coding: utf-8 -*-
"""alak_kayit.py — sûre 96 (Alak) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 96

CIPA = {
 # blok 1-8
 1: dict(kademe='L1', olgu=True, cipa=False, not_="'iqra' bi'smi rabbike'llezî xalaq' — yaratma, nesnesiz; aşama / madde yok — L1 (87:2 kaydı emsali); tarayıcı vermedi"),
 2: dict(kademe='L1', olgu=True, cipa=False, not_="'xalaqa'l-insâne min 'alaq' — yaratma + madde adı; aşama dizisi / mekanizma yok — L1 (75:38 kaydı emsali); tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'iqra' ve rabbuke'l-ekram' — emir / sıfat (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'ellezî 'alleme bi'l-qalem' — öğretme (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="''alleme'l-insâne mâ lem ya'lem' — öğretme / bilgi (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'kellâ inne'l-insâne le-yatğâ' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'en ra'âhu'steğnâ' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'inne ilâ rabbike'r-ruc'â' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 9-19
 9: dict(kademe=None, olgu=False, cipa=False, not_="'e-ra'eyte'llezî yenhâ' — engelleme (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="''abden izâ sallâ' — ibadet (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 11: dict(kademe=None, olgu=False, cipa=False, not_="'e-ra'eyte in kâne 'ala'l-hudâ' — yol / tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'ev emere bi't-taqvâ' — emir / tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'e-ra'eyte in kezzebe ve tevellâ' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="'e-lem ya'lem bi-enne'llâhe yerâ' — bilgi / görme (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'kellâ le-in lem yentehi le-nesfa'an bi'n-nâsiyeh' — tehdit (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 16: dict(kademe=None, olgu=False, cipa=False, not_="'nâsiyetin kâdhibetin xâti'eh' — nitelik (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 17: dict(kademe=None, olgu=False, cipa=False, not_="'fe'l-yed'u nâdiyeh' — çağrı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 18: dict(kademe=None, olgu=False, cipa=False, not_="'se-ned'u'z-zebâniyeh' — tehdit (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 19: dict(kademe=None, olgu=False, cipa=False, not_="'kellâ lâ tuti'hu ve'scud ve'qterib' — emir / ibadet (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 8): [
  "esmâ: e_oto 0 token; KARAR değişmedi (725); lafız yok, Rab 3 (96:1, 3, 8) — sûrenin Rab geçişlerinin üçü de bu blokta; 'ekram' esmâ listesinde değil",
  "kök tablosu: blokta yeni kök yok (1530); retroaktif yama hedefli 0, genel 0",
  "yıldız: ★★★ 96:1 rab z=3,94, 96:3 rab z=6,78, 96:8 rab z=5,01 — formül davranışı",
  "fâsıla (924): metin ق 2 (96:1-2), م 3 (96:3-5), ى 3 (96:6-8); ölçüm 96:6-8'i son harfteki medde işareti yüzünden ayrı 'ٓ' sınıfına koydu — üçü aynı sınıfta olduğu için kırık işaretlenmedi; ق → م geçişi (96:3) de işaretlenmedi",
  "biçim (924): ayet 1 harf 37 → harf3 18 (besmele ailesi); 96:6 KELLA",
  "iltifât: ölçüm 96:3 ({3} → {2}), 96:4 ({2} → {3}), 96:8 ({3} → {2}); 96:4 'ellezî' sıfat cümlesi, hitap değişmedi (924, sûre 87 dikkati)",
  "adsız gönderge (1017): hitap 2MS; 96:2 ve 96:4-5'te yaratan / öğreten 3MS (Rab'a bağlı ilgi cümleleri, okuma)",
  "KAPATILAMAZ: 96:1 'iqra'' ve 'xalaqa'nın, 96:4 'alleme'nin nesneleri yazılmamış",
  "çıpa: L1 2 (96:1 nesnesiz yaratma — 87:2 kaydı emsali; 96:2 yaratma + madde — 75:38 kaydı emsali); olgu=False 6; tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 95:8 / 96:1 sûre sınırı — lafızla soru ile kapanış / Rab adıyla okuma emri ile açılış; fâsıla ن → ق; 95 lafız 1 Rab 0, 96 bu blokta Rab 3",
  "aday 1039: ayet içi 1 (96:5 öğretti / bilmiyordu)",
  "aday 1041: sûre içi kayıt yok (lafız henüz okunmadı); sûreler arası okuma notu: lemma 'ekram' korpusun iki geçişi — 49:13 insan / 96:3 Rab",
  "bağ: kalıp / lemma eşleri okumayla (95:8, 69:52, 87:1, 87:2, 55:14, 75:38, 90:4, 95:4, 49:13, 55:4, 68:1, 79:17, 79:37, 80:5, 92:8, 53:42, 79:44); bütün emsaller bu oturumda AR + meal ile basıldı",
  "◈K / ◈B: ◈K tetik yok (سمو 'ism' S1 dışı); ◈B dolu 96:1 (خلق), 96:2 (خلق, أنس, علق), 96:5 ve 96:6 (أنس); tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 8 ayet; oturum_xy 21 sayım, 0 uyuşmaz",
  "süreç: sûre 96 dosyaları tin_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_96.py, oturum dışı; ad değişimi harf sınırıyla — 'tin' 'Latin' / 'metin' içinde değişmedi; kurulumda iki aksaklık — denetim deseninin METIN'i yakalaması, kapanış betiğinde tırnak — dosyalar kullanılmadan düzeltildi); blok sınırı sûrenin bölümlerine göre (1-8 oku emri + yaratılış + öğretme + azma + dönüş; 9-19 engelleyen, perçem, secde); taban 86953a8",
 ],
 (9, 19): [
  "esmâ: e_oto 0 token; KARAR değişmedi (725); lafız 1 (96:14 — sûrenin tek lafız geçişi), Rab 0 — sûrenin Rab geçişlerinin üçü de 96:1-8'de",
  "kök tablosu: 2 yeni kök (1530 → 1532) — سفع (96:15) ve زبن (96:18), ikisi de korpusta 1 ayet; retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı",
  "yıldız: ★ 96:9 kafiye kırığı (n z=-1,00); ★★★ 96:14 allah z=3,47, 96:15 hapaks سفع z=3,28, 96:18 hapaks زبن z=3,28 — formül davranışı",
  "fâsıla (924): 96:9 KAFİYE KIRILMASI sahte — 96:8 son harfteki medde işareti yüzünden 'ٓ' sınıfında, 96:9 A sınıfında; metinde ikisi de ى. Metin ى 6 (96:9-14), ة 3 (96:15, 16, 18), ه 1 (96:17), ب 1 (96:19); ölçüm ى → ة ve ة → ب geçişlerini kırık işaretlemedi; 96:10-13 yine 'ٓ' sınıfında",
  "biçim: 96:15 KELLA, 96:19 KELLA + NEHY; 96:16 fiilsiz (zaman yok, şahıs işareti yok)",
  "iltifât: ölçüm 96:18 ({3} → {1}), 96:19 ({1} → {2}); 96:15'te 1P ilk kez (sahset ['1', '3'], baskın 3 — iltifât sayılmadı)",
  "adsız gönderge (1017): hitap 2MS (96:9, 11, 13, 19); 'ellezî yenhâ' (96:9), ''abd' (96:10), 96:11-13 ve 96:15-17'deki 3MS, 96:19 'tuti'hu'nun 3MS'si, konuşan 1P (96:15, 18) — hiçbiri adlandırılmadı",
  "KAPATILAMAZ: 96:11-13 'e-ra'eyte in …' şartlarının cevabı yazılmamış; 96:11-12 'kâne' / 'emere'nin öznesi (engelleyen mi kul mu) metinde belirlenmemiş",
  "çıpa: olgu=False 11; merdiven uygulanmadı; tarayıcı v4 blokta aday vermedi",
  "aday 1039: ayet içi 1 (96:19 boyun eğme / secde et ve yaklaş); blok içi 2 (96:11-12 / 96:13 iki şart; 96:17 / 96:18 iki çağrı)",
  "aday 1041 (kayıt): sûre içi — lemma 'ra'â' 96:7 öznesi insan ('ra'âhu') / 96:14 öznesi Allah ('yerâ')",
  "bağ: kalıp / lemma eşleri okumayla (25:43, 79:40, 75:31, 75:32, 20:48, 92:16, 9:78, 11:56, 55:41, 68:16, 69:9, 29:29, 68:8, 84:21); bütün emsaller bu oturumda AR + meal ile basıldı",
  "◈K / ◈B: blokta tetik kökü yok — 11 ayette ikisi de '—' ('nâsiye' uzuv adı, kökü نصي tetik listesinde değil); tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 11 ayet; oturum_xy 32 sayım, 0 uyuşmaz",
  "secde: 96:19 metinde secde işareti taşıyor; bu oturumda secde işaretli ikinci basılan ayet (ilki 84:21, emsal)",
  "süreç: blok sınırı sûrenin bölümlerine göre (1-8 oku emri + insanın azması / 9-19 engelleyen, tehdit, secde emri); sûre 2 blok, ara zip yok",
 ],
}

DUZELTME = {
}
