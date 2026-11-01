# -*- coding: utf-8 -*-
"""beyyine_kayit.py — sûre 98 (Beyyine) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 98

CIPA = {
 # blok 1-8
 1: dict(kademe=None, olgu=False, cipa=False, not_="'lem yekuni'llezîne keferû … munfekkîne hattâ te'tiyehumu'l-beyyineh' — delile kadar süren tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'resûlun mine'llâhi yetlû suhufen mutahhareh' — elçinin okuması (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'fîhâ kutubun qayyimeh' — sayfaların içeriği (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ teferreqa'llezîne ûtu'l-kitâb …' — ayrılık (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ umirû illâ li-ya'budu'llâh …' — emir, ibadet (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'… fî nâri cehenneme xâlidîne fîhâ' — âhiret, cehennem (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'… ulâ'ike hum xayru'l-beriyyeh' — tutum ve değer (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'cennâtu 'adnin tecrî min tahtihe'l-enhâr' — âhiret, cennet; doğal olgu değil (olgu=False; 85:11, 58:22 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 8): [
  "esmâ: e_oto 0 token; KARAR değişmedi (726); lafız 3 (98:2, 98:5, 98:8), Rab 2 (ikisi 98:8); mühür yok",
  "kök tablosu: blokta yeni kök yok (1532); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı",
  "yıldız: ★★ 98:2 allah z=2,80; ★ 98:4 pas z=1,57; ★ 98:8 rab z=1,71 — formül davranışı",
  "fâsıla: metin ة 7 (98:1-7), ه 1 (98:8); ölçüm H sınıfı 8, kafiye kırığı 0 — ة / ه aynı sınıfta",
  "biçim (924): ayet 1 harf 75 → harf3 54 (besmele ailesi); HASR 98:4, 98:5; 98:6-7 'inne' tekidi ve 98:3 haberin önde oluşu biçim alanında görünmüyor; edilgen 98:4 'ûtû', 98:5 'umirû'",
  "iltifât: ölçüm 0; sûrenin tamamı 3. şahıs (sahset ['3'])",
  "adsız gönderge (1017): elçi (98:2, 3MS), emreden (98:5, edilgen), 'men xaşiye' (98:8) — adlandırılmadı; topluluklar metindeki adlarıyla",
  "KAPATILAMAZ: 98:1 'munfekkîn'in neden ayrıldığı yazılmamış; 98:1 'ellezîne keferû min ehli'l-kitâb' ile 98:4 'ellezîne ûtu'l-kitâb'ın aynı topluluk olup olmadığı metinde işaretli değil; 98:2 'resûlun' ile 98:1 'el-beyyinetu' i'râbca uyumlu, ilişki işaretsiz",
  "okuma düzeltmesi (kayıttan önce): 98:1 taslakta 'el-muşrikîne'nin bağlandığı ad açık bırakılmıştı — -îne yazımı NOM'u dışlıyor, 'ehli'l-kitâb'a atıflı; meal 98:1 ve 98:6 buna göre yazıldı",
  "çıpa: olgu=False 8; merdiven uygulanmadı; tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 97:5 / 98:1 sûre sınırı — fiilsiz 'hattâ' + tamlama ile kapanış / 'lem' + 'hattâ' + IMPF ile açılış; fâsıla ر → ة; sûre 97 lafızsız Rab 1, sûre 98 lafız 3 Rab 2",
  "aday 1039: ayet içi 0; blok içi 3 (98:1 / 98:4 delil gelinceye kadar / geldikten sonra; 98:6 / 98:7 'keferû' / 'âmenû' ve 'şerr' / 'xayr' 'el-beriyye' tamlamasında; 98:6 / 98:8 'nâri cehennem' / 'cennâtu 'adn')",
  "aday 1041 (kayıt): sûre içi — lemma 'radiye' 98:8 aynı ayette öznesi Allah ('radiya'llâhu 'anhum') / öznesi inananlar ('radû 'anh')",
  "korpusun tamamı sûre içi: harekesiz 'ellezîne keferû min ehli'l-kitâbi ve'l-muşrikîn' (98:1, 98:6); lemma 'beriyye' (98:6, 98:7); lemma 'qayyime' (98:3, 98:5); lemma 'munfekk' (98:1)",
  "bağ: kalıp / lemma eşleri okumayla (97:5, 59:2, 90:13, 20:133, 80:13, 80:14, 65:11, 42:14, 45:17, 40:14, 22:31, 9:68, 85:11, 20:76, 9:100, 58:22, 79:26); 97:5 bu oturumda sûre 97'de basılmıştı, yeniden basılmadı; diğerleri AR + meal ile basıldı",
  "◈K / ◈B: ◈K dolu yalnız 98:8 (نهر cennet ırmakları, أبد); ◈B tetik kökü yok — sekiz ayette '—'; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 8 ayet; oturum_xy 56 sayım, 0 uyuşmaz",
  "süreç: sûre 98 dosyaları kadr_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_98.py, oturum dışı; ad 'beyyine'; aday_ekle set değişkeni ASCII 'BEYYINE'); sûre 8 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {}
