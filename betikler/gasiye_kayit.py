# -*- coding: utf-8 -*-
"""gasiye_kayit.py — sûre 88 (Ğâşiye) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 88

CIPA = {
 # blok 1-7
 1: dict(kademe=None, olgu=False, cipa=False, not_="'hel etâke hadîthu'l-ğâşiye' — âhiret / gaybî olay (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'vucûhun yevme'izin xâşi'a' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="''âmiletun nâsıba' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'taslâ nâran hâmiye' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'tusqâ min 'aynin âniye' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'leyse lehum ta'âmun illâ min darî'' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'lâ yusminu ve lâ yuğnî min cû'' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 8-16
 8: dict(kademe=None, olgu=False, cipa=False, not_="'vucûhun yevme'izin nâ'ime' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 9: dict(kademe=None, olgu=False, cipa=False, not_="'li-sa'yihâ râdiye' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'fî cennetin 'âliye' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 11: dict(kademe=None, olgu=False, cipa=False, not_="'lâ tesme'u fîhâ lâğiye' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'fîhâ 'aynun câriye' — âhiret, cennet pınarı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'fîhâ sururun merfû'a' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="'ve ekvâbun mevdû'a' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'ve nemâriqu masfûfa' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 16: dict(kademe=None, olgu=False, cipa=False, not_="'ve zerâbiyyu mebthûtha' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 17-26
 17: dict(kademe='L0', olgu=True, cipa=False, not_="'e-fe-lâ yenzurûne ile'l-ibili keyfe xuliqat' — bakmaya çağrı + yaratılma adlanıyor (deve), madde ve aşama yok — L0 (86:5 kaydı emsali); tarayıcı v4 adayı (bakış + خلق), çıpa değil"),
 18: dict(kademe='L1', olgu=True, cipa=False, not_="'ve ile's-semâ'i keyfe rufi'at' — gök + süreç (yükseltilme), mekanizma yok — L1 (79:28 kaydı emsali); tarayıcı vermedi"),
 19: dict(kademe='L1', olgu=True, cipa=False, not_="'ve ile'l-cibâli keyfe nusibat' — dağlar + süreç (dikilme), gerekçe yok — L1 (79:32 kaydı emsali); tarayıcı vermedi"),
 20: dict(kademe='L1', olgu=True, cipa=False, not_="'ve ile'l-ardi keyfe sutihat' — yer + süreç (yayılma), mekanizma yok — L1 (79:30 kaydı emsali); tarayıcı vermedi"),
 21: dict(kademe=None, olgu=False, cipa=False, not_="'fe-zekkir innemâ ente muzekkir' — emir, hitap (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 22: dict(kademe=None, olgu=False, cipa=False, not_="'leste 'aleyhim bi-musaytir' — hitap (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 23: dict(kademe=None, olgu=False, cipa=False, not_="'illâ men tevellâ ve kefer' — insan tutumu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 24: dict(kademe=None, olgu=False, cipa=False, not_="'fe-yu'azzibuhu'llâhu'l-'azâbe'l-ekber' — âhiret / gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 25: dict(kademe=None, olgu=False, cipa=False, not_="'inne ileynâ iyâbehum' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 26: dict(kademe=None, olgu=False, cipa=False, not_="'thumme inne 'aleynâ hisâbehum' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 7): [
  "esmâ: e_oto 0 token; KARAR değişmedi (716); lafız ve Rab yok",
  "kök tablosu: yeni kök yok (1513); retroaktif yama hedefli 0, genel 0",
  "harf alanı: ayet 1 ölçümünde harf 35 → harf3 16, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924)",
  "yıldız: ★★★ 88:5 pas z=5,38 — kısa tek fiilli edilgen ayet (formül davranışı)",
  "fâsıla (924): 88:1-5 ة, 88:6-7 ع — geçiş (88:5 → 6) kafiye kırığı işaretlenmedi",
  "şahıs (924): 88:4-5 3FS (yüzler) → 88:6 3MP (yüzlerin sahipleri) ölçümde ikisi de '3' — gönderge değişimi görünmüyor",
  "biçim (924): 88:1 INTG, 88:5 EDİLGEN, 88:6 ISTISNA, 88:7 NEG 2 doğru",
  "KAPATILAMAZ: 88:1 'el-ğâşiye' — olayın ne olduğu metinde adlanmıyor (adsız ortaç)",
  "adsız gönderge (1017): 88:1 muhatap 2MS ve soran; 88:2 yüzler (nekre) ve sahipleri; 88:5 içiren",
  "gloss (1021): kök أني 'vakit, ân' — 'âniye' (kaynar) uymuyor; kök ضرع 'yalvarma' — 'darî'' (dikenli bitki) uymuyor; kök نصب üç anlam birlikte (burada yorgunluk)",
  "lemma (eşsesli): 'âniye' morph'ta 76:15 kaplar ile 88:5 kaynar'ı birleştiriyor — lemma sayısı verilmedi",
  "◈B (tetik dışı bitki): 88:6 'darî'' tetik listesinde değil — '—', gözlem ◇'ye; ◈B 88:5 عين pınar, organ anlamı değil",
  "çıpa: blokta merdiven uygulanan ayet yok (7 ayetin 7'si âhiret / gaybî, olgu=False); tarayıcı v4 blokta aday vermedi",
  "esit2 / nakarat3 / xref: blokta boş",
  "aday 1040 (kayıt): 87:19 / 88:1 sûre sınırı — adlı iki kişi (İbrâhîm, Mûsâ) ile kapanış / 2MS'ye 'hel etâke hadîthu' sorusu ile açılış; aynı soru kalıbı 79:15 ve 20:9'da Mûsâ'nın, 51:24'te İbrâhîm'in konuklarının haberini soruyor (okuma); fâsıla ى → ة",
  "bağ: kalıp / lemma eşleri okumayla (79:15, 85:17, 51:24, 20:9, 12:107, 75:22, 80:38, 79:9, 87:12, 14:16, 47:15, 76:15, 69:36, 77:31); bütün emsaller sohbette AR + meal ile basıldı",
  "◈K / ◈B: ◈K dolu 88:2 يوم; ◈B dolu 88:5 عين; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 20 sayım, 0 uyuşmaz",
  "süreç: sûre 88 dosyaları ala_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_88.py, oturum dışı); kapanış / paket blok listesi BLOK_LISTESI_ELLE ile bırakıldı; taban 75699c1 değişmedi (sûre 87 zip'i henüz yüklenmedi) — sûre 88 zip'i sûre 87'yi de taşıyacak",
 ],
 (8, 16): [
  "esmâ: e_oto 0 token; KARAR değişmedi (716); lafız ve Rab yok",
  "kök tablosu: kok_ekle_88 2 kök (نمرق 88:15, زرب 88:16; ikisi de korpusta tek ayet); 1513 → 1515; retroaktif yama hedefli 0 (daha önce okunmuş ayet 0), genel 0 (ikinci koşu da 0)",
  "yıldız: ★★★ 88:15, 16 hapaks z=3,28 — yeni eklenen kökler tek token (formül davranışı)",
  "fâsıla: blokta dokuz ayetin dokuzu ة; kafiye kırığı yok",
  "şahıs (924): 88:11 'tesme'u' morph 2MS — 3FS ('vucûh') okuması harften ayrılmaz; sahset {3} → {2, 3} kısmi örtüşme, iltifât 0",
  "KAPATILAMAZ: 88:11 işitenin 2MS mi yüzler (3FS) mi olduğu",
  "adsız gönderge (1017): 88:8 yüzler (nekre) ve sahipleri; 88:13-16 edilgen ortaçların failleri (yükselten, koyan, dizen, seren)",
  "gloss (1021): kök سرر 'sır, gizleme' — 'surur' (tahtlar) uymuyor",
  "◈B tetik (kayıttan önce): kök وضع tetik listesinde (doğurma) — 88:14 'mevdû'a' (konulmuş) satırı '—' yazılmıştı, tetik ön kuru koşusu yakaladı, satır dolduruldu ('doğurma anlamı değil' notuyla); ◈B 88:11 سمع işitme işlevi, 88:12 عين pınar",
  "esit2: 88:10 TAM → 69:22 (basıldı); 69:21-22 / 88:9-10 'râdiye' + 'fî cennetin 'âliye' sıralı iki ayet — ardışık olmayan sûre, okuma bağı",
  "çıpa: blokta merdiven uygulanan ayet yok (9 ayetin 9'u âhiret, olgu=False); tarayıcı v4 blokta aday vermedi",
  "bağ: kalıp / lemma eşleri okumayla (69:21, 69:22, 69:11, 78:35, 56:25, 52:20, 56:34, 56:18, 76:15); bütün emsaller sohbette AR + meal ile basıldı",
  "◈K / ◈B: ◈K dolu 88:8 يوم; ◈B dolu 88:11 سمع, 88:12 عين, 88:14 وضع; tetik ön kuru koşu (geçici modül, silindi) önce 1 uyuşmaz (88:14), düzeltme sonrası 0; sûre geneli 16 / 0; oturum_xy blok 19, 1-16 toplam 39 sayım, 0 uyuşmaz",
 ],
 (17, 26): [
  "esmâ: e_oto 0 token; KARAR değişmedi (716); lafız 1 (88:24) — sûrenin tek lafzı; Rab yok — sûre Rabsız",
  "kök tablosu: kok_ekle_88 2 kök (أبل 88:17, korpus 3 ayet / iki lemma; سطح 88:20, korpusta tek ayet); 1515 → 1517; retroaktif yama 'daha önce okunmuş 1 ayet' saydı — okunmamış sûrede, kayıt yok, atlandı; hedefli 0, genel 0 (ikinci koşu da 0)",
  "yıldız: ★★ 88:17 pas z=2,52; ★★★ 88:18, 19, 20 pas z=5,38 (88:20'de hapaks 3,28 da eşikte); ★★★ 88:24 allah z=4,47 — formül davranışı",
  "fâsıla (924): 88:17-20 ت, 88:21-24 ر, 88:25-26 م; 88:16 ة → 88:17 ت, ت → ر, ر → م geçişlerinin hiçbiri kafiye kırığı işaretlenmedi",
  "iltifât: 88:21 {3} → {2} gerçek; 88:25 {3} → {1, 3} kısmi örtüşme, ölçüm 0 — lafızdan (88:24) 1P konuşana geçiş görünmüyor (924)",
  "biçim (924): 88:21 'innemâ' hasrı kip / biçim alanında yok; 88:24 fiil + aynı kökten mastar — mm2 boş, kök ikilemesi veriyor; 88:17 INTG + NEG, 88:23 ISTISNA doğru",
  "KAPATILAMAZ: 88:23 istisnanın bağlandığı cümle (88:21 / 88:22); 88:25-26 konuşan 1P ile 88:24 lafzının aynılığı",
  "adsız gönderge (1017): 88:17 bakanlar (3MP); 88:17-20 yaratan, yükselten, diken, yayan (edilgen); 88:21-22 muhatap 2MS; 88:22, 25, 26 onlar (3MP); 88:23 'men'; 88:25-26 konuşan 1P",
  "gloss (1021): kök سطر 'satır, yazma; esâtîr' — 'musaytir' (hükmeden, zorlayan) uymuyor",
  "◈B (tetik dışı hayvan): 88:17 'el-ibil' tetik kök listesinde değil — satırı خلق dolduruyor, deve B1'e gözlem olarak yazıldı",
  "çıpa: 88:17 L0 (tarayıcı v4 adayı, çıpa değil); 88:18-20 L1 (gök, dağlar, yer + edilgen süreç); 88:21-26 olgu=False",
  "kayıttan önce: ◇'de basılmamış okunmuş ayeti kapsayan bir aralık basılan ayetlere indirildi (79:28, 30, 32)",
  "aday 1040 ailesi (okuma): ardışık sûreyle 'fe-zekkir' (87:9 / 88:21) ve belirli üstünlük sıfatı 'kubrâ' / 'ekber' (87:12 / 88:24)",
  "bağ: kalıp / lemma eşleri okumayla (86:5, 50:6, 79:28, 79:30, 79:32, 87:9, 50:45, 52:37, 9:74, 32:21, 87:12, 75:17); bütün emsaller sohbette AR + meal ile basıldı",
  "sûre içi tam sayım (bütün geçişler basıldı): كيف [4/4]; وجه, يوم, عين, نصب, رفع, ليس, ذكر, عذب [2/2]; lafız 1 (88:24), Rab 0",
  "◈K / ◈B: ◈K dolu 88:18 سمو, 88:19 جبل, 88:20 أرض; ◈B dolu 88:17 خلق; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, sûre geneli 26 / 0; oturum_xy blok 23, sûre 62 sayım, 0 uyuşmaz",
 ],
}

DUZELTME = {
}
