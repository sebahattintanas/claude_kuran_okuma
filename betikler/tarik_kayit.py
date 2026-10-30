# -*- coding: utf-8 -*-
"""tarik_kayit.py — sûre 86 (Târık) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 86

CIPA = {
 # blok 1-10
 1: dict(kademe='L1', olgu=True, cipa=False, not_="'ve's-semâ'i ve't-târiq' — gök + gece gelen (86:3'te yıldız); süreç / ölçü yok — L1 (85:1 kaydı emsali); tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ edrâke me't-târiq' — soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe='L1', olgu=True, cipa=False, not_="'en-necmu's-sâqib' — gökcismi + nitelik; süreç / ölçü yok — L1; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'in kullu nefsin lemmâ 'aleyhâ hâfiz' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe='L0', olgu=True, cipa=False, not_="'fe'l-yenzuri'l-insânu mimme xuliq' — bakmaya çağrı + yaratılma adlanıyor, madde yok — L0; tarayıcı v4 adayı (bakış + خلق), çıpa değil"),
 6: dict(kademe='L1', olgu=True, cipa=False, not_="'xuliqa min mâ'in dâfiq' — madde (su) + nitelik (atılarak akan); aşama / nedensellik yok — L1 (nutfe + hâl kaydıyla aynı kademe); tarayıcı vermedi"),
 7: dict(kademe='L1', olgu=True, cipa=False, not_="'yaxruju min beyni's-sulbi ve't-terâ'ib' — çıkış yeri iki organ adıyla; mekanizma / ölçü / nedensellik yok — L1; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'innehû 'alâ rec'ihî le-qâdir' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 9: dict(kademe=None, olgu=False, cipa=False, not_="'yevme tublâ's-serâ'ir' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'fe-mâ lehû min quvvetin ve lâ nâsır' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 11-17
 11: dict(kademe='L1', olgu=True, cipa=False, not_="'ve's-semâ'i zâti'r-rec'' — gök + nitelik; süreç / ölçü yok — L1 (85:1, 51:7 kayıtları emsali); tarayıcı vermedi"),
 12: dict(kademe='L1', olgu=True, cipa=False, not_="'ve'l-ardi zâti's-sad'' — yer + nitelik; süreç / ölçü yok — L1; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'innehû le-qavlun fasl' — söz, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ huve bi'l-hezl' — söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'innehum yekîdûne keydâ' — insan davranışı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 16: dict(kademe=None, olgu=False, cipa=False, not_="'ve ekîdu keydâ' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 17: dict(kademe=None, olgu=False, cipa=False, not_="'fe-mehhili'l-kâfirîne emhilhum ruveydâ' — hitap, emir (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 0 token; KARAR değişmedi (714); lafız ve Rab yok — 86:8 'innehû' göndergesi adsız",
  "kök tablosu: kok_ekle_86 1 kök (دفق 86:6; korpusta tek ayet); 1511 → 1512; retroaktif yama hedefli 0, genel 0 (ikinci koşu da 0)",
  "harf alanı: ayet 1 ölçümünde harf 33 → harf3 14, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924)",
  "yıldız: ★★★ 86:6, 9 pas z=5,38 (86:6'da hapaks 3,28 da eşikte); ★★ 86:5 pas z=2,52 — formül davranışı",
  "biçim (924): 86:4 'in … lemmâ' hasrı kip NEG + biçim ISTISNA olarak çıkıyor (HASR değil); 86:5 emir lâmı IMPV doğru; 86:8 EMPH doğru",
  "KAPATILAMAZ: 86:4 gözetleyici; 86:8 'innehû' göndergesi (lafızsız, Rabsız; yaratan edilgenle adsız); 86:1-3 yeminin cevabı 86:4 olarak okunabilir, metin işaretlemiyor",
  "adsız gönderge (1017): 86:2 muhatap 2MS; 86:5-6 yaratan; 86:9 sınayan; konuşan adsız",
  "gloss (1021): kök صلب 'asma, salb' — 'sulb' (bel) uymuyor; kök ترب 'toprak' — 'terâ'ib' (göğüs kemikleri) uymuyor; kök بلو 'sınama; eskime' iki anlam; kök رجع 86:8 'rec'' (geri döndürme), 86:11 henüz okunmadı",
  "◈B (tetik dışı organ): 86:7 'sulb' ve 'terâ'ib' tetik listesinde değil — '—', gözlem ◇'ye",
  "çıpa: 86:5-7 yaratılış dizisi L0 / L1 / L1 — aşama sırası ve nedensellik yok; 86:5 tarayıcı v4 adayı, çıpa değil",
  "fâsıla (924): 86:1-2 ق, 86:3 ب, 86:4 ظ, 86:5-6 ق, 86:7 ب, 86:8-10 ر — geçişlerin hiçbiri kafiye kırığı işaretlenmedi",
  "esit2: 86:2 BENZER → 69:3 (basıldı)",
  "aday 1040 (kayıt): 85:22 / 86:1 sûre sınırı — nekre + edilgen ortaç / yemin; ikisi de lafızsız, Rabsız; fâsıla ظ → ق; ardışık iki sûre 've's-semâ'' yeminiyle açılıyor (85:1 / 86:1)",
  "aday 1040 ailesi (okuma): kök حفظ sınırın iki yanında — 85:22 'mahfûz' / 86:4 'hâfiz'",
  "bağ: kalıp / lemma eşleri okumayla (85:1, 51:7, 69:3, 82:17, 37:10, 53:1, 82:10, 83:33, 80:24, 77:20, 32:8, 50:3, 75:40, 72:24); 4:23, 86:11 henüz okunmadı — bağ yazılmadı",
  "◈K / ◈B: ◈K dolu 86:1 سمو, 86:3 نجم, 86:6 موه, 86:9 يوم; ◈B dolu 86:5 أنس خلق, 86:6 خلق; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 26 sayım 0 uyuşmaz",
  "süreç: sûre 86 dosyaları buruc_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_86.py, oturum dışı); kapanış / paket blok listesi BLOK_LISTESI_ELLE",
 ],
 (11, 17): [
  "esmâ: e_oto 0 token; KARAR değişmedi (714); sûre bütünü lafız 0, Rab 0 — lafızsız ve Rabsız sûre; esmâ yok",
  "kök tablosu: yeni kök yok (1512); retroaktif yama hedefli 0, genel 0",
  "yıldız: ★★★ 86:14 hapaks z=3,28 (kök هزل korpusta tek ayet) — formül davranışı",
  "iltifât: 86:16 {3} → {1} (1S konuşan) ve 86:17 {1} → {2, 3} gerçek",
  "biçim (924): 86:12 atıflı yeminde QASEM yok; 86:15 'inne' kip alanında yok; 86:11 QASEM, 86:13 EMPH, 86:14 NEG, 86:17 IMPV 2, 86:15-16 mm2 doğru",
  "KAPATILAMAZ: 86:11 'rec'' ile ne döndüğü; 86:13-14 'innehû' / 'huve' göndergesi; 86:16 konuşan 1S ile 86:17 emir verenin aynılığı",
  "adsız gönderge (1017): 86:15 3MP (86:17'de 'el-kâfirîn'); 86:16 konuşan 1S; 86:17 muhatap 2MS",
  "gloss (1021): kök مهل eşsesli (erimiş maden / mühlet) — kök sayımı verilmedi; kök طرق 'yol' 86:1-2 'târiq'e (gece gelen) uymuyor — önceki blok için kayıttan sonra görüldü, burada yazıldı, önceki kayıt değişmedi",
  "lemma 'rec'' sûre içi 2/2 iki göndergeyle: 86:8 insanın geri döndürülmesi / 86:11 göğün niteliği",
  "aday 1041 (kayıt): kök كيد 86:15 3MP (kâfirler) / 86:16 1S (konuşan adsız)",
  "aday 1040 ailesi (okuma): harekesiz 've's-semâ'i zât' 85:1 / 86:11 ardışık iki sûrede",
  "fâsıla (924): 86:11-12 ع, 86:13-14 ل, 86:15-17 ا — geçişler kafiye kırığı işaretlenmedi",
  "bağ: kalıp / lemma eşleri okumayla (51:7, 85:1, 30:43, 80:26, 69:40, 81:19, 77:13, 52:42, 68:45, 73:11)",
  "◈K / ◈B: ◈K dolu 86:11 سمو, 86:12 أرض; ◈B tetik yok; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, sûre geneli 17 / 0; oturum_xy 12 sayım 0 (sûre geneli 38 / 0)",
 ],
}

DUZELTME = {
}
