# -*- coding: utf-8 -*-
"""sems_kayit.py — sûre 91 (Şems) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 91

CIPA = {
 # blok 1-10
 1: dict(kademe='L0', olgu=True, cipa=False, not_="'ve'ş-şemsi ve duhâhâ' — yemin edilen gökcismi + vakit; süreç / ölçü yok — L0 (89:1 kaydı emsali); tarayıcı vermedi"),
 2: dict(kademe='L0', olgu=True, cipa=False, not_="'ve'l-qameri izâ telâhâ' — yemin edilen gökcismi + hareket; mekanizma yok — L0 (89:4 kaydı emsali); tarayıcı vermedi"),
 3: dict(kademe='L0', olgu=True, cipa=False, not_="'ve'n-nehâri izâ cellâhâ' — yemin edilen vakit + süreç; nesne açık değil — L0; tarayıcı vermedi"),
 4: dict(kademe='L0', olgu=True, cipa=False, not_="'ve'l-leyli izâ yağşâhâ' — yemin edilen vakit + süreç — L0 (81:17, 89:4 kayıtları emsali); tarayıcı vermedi"),
 5: dict(kademe='L1', olgu=True, cipa=False, not_="'ve's-semâ'i ve mâ benâhâ' — gök + süreç (kurma); mekanizma yok — L1 (79:27 kaydı emsali); tarayıcı vermedi"),
 6: dict(kademe='L1', olgu=True, cipa=False, not_="'ve'l-ardi ve mâ tahâhâ' — yer + süreç (yayma); mekanizma yok — L1 (79:30 kaydı emsali); tarayıcı vermedi"),
 7: dict(kademe='L1', olgu=True, cipa=False, not_="'ve nefsin ve mâ sevvâhâ' — nefis + düzenleme; aşama / mekanizma yok — L1 (87:2 kaydı emsali); tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'fe-elhemehâ fucûrahâ ve taqvâhâ' — ilham (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 9: dict(kademe=None, olgu=False, cipa=False, not_="'qad efleha men zekkâhâ' — tutum ve sonuç (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'ve qad xâbe men dessâhâ' — tutum ve sonuç (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 11-15
 11: dict(kademe=None, olgu=False, cipa=False, not_="'kezzebet themûdu bi-tağvâhâ' — kavim, tarihsel olay (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'izi'nbe'athe eşqâhâ' — kişi, tarihsel olay (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'fe-qâle lehum resûlu'llâhi nâqate'llâhi ve suqyâhâ' — kıssa, söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="'fe-kezzebûhu fe-'aqarûhâ fe-demdeme 'aleyhim rabbuhum …' — kıssa, helâk (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'ve lâ yaxâfu 'uqbâhâ' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 0 token; KARAR değişmedi (720); lafız ve Rab yok",
  "kök tablosu: kok_ekle_91 3 kök (طحو 91:6, لهم 91:8, دسو 91:10; üçü korpusta tek ayet); 1523 → 1526; retroaktif yama hedefli 0",
  "retroaktif genel geçiş (1021, bekleyen karar ailesi 'gloss_gecis iskelet çakışması'): kök لهم iskeleti eski kayıtlarda harekesiz yazılmış 'lahum' (li + hum) kelimesiyle aynı; ilk koşu 24 alanda (1 mercek, 23 ölçüm; sûre 28, 35, 36, 39, 42, 47 kayıtları) 27 anmaya 'içe doğurma, ilham' gloss'unu ekledi, ikinci koşu 0; anlam yanlış (zamir, kök değil) ama türkçe denetimi bu anmaları kök sayıyor — yama bırakıldı, araç dondurulmuş; karar tam okuma sonunda",
  "yıldız: ★★★ 91:6, 8, 10 hapaks z=3,28 (bu blokta eklenen kökler) — formül davranışı",
  "fâsıla: 91:1-10 ا (her ayet 3FS 'hâ' ile bitiyor); 90:20 ة → 91:1 ا sûre sınırı",
  "biçim (924): 91:1 QASEM; 91:2-7 atıflı yeminlerde QASEM yok; 91:9 esit2 BENZER → 87:14; ayet 1 harf 31 → harf3 12 (besmele ailesi)",
  "iltifât: blokta ölçüm 0; yemin eden / konuşan şahıs işareti yok, 3FS 'hâ' on ayette",
  "adsız gönderge (1017): yemin eden; 91:5-8 kuran / yayan / düzenleyen / ilham eden ('mâ' + 3MS); 91:9-10 'men'",
  "KAPATILAMAZ: 91:3-4 'hâ' zamirinin göndergesi (açığa çıkarılan / bürünen); 91:5-7 'mâ' ilgi zamiri mi mastar edatı mı (morph REL, meal ilgi okumasını seçti)",
  "çıpa: L0 4 (91:1-4 yemin edilen gökcismi / vakit); L1 3 (91:5 gök, 91:6 yer, 91:7 nefis — 79:27, 79:30, 87:2 emsalleri); olgu=False 3; tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 90:20 / 91:1 sûre sınırı — 3MP üzerine kapatılmış ateş ile kapanış / güneşe yemin ile açılış; fâsıla ة → ا; ikisi de lafızsız ve Rabsız (91'de Rab 91:14, henüz okunmadı); ardışık sûre okuma bağları 90:3 / 91:5 'mâ' + PERF, 90:10 / 91:8 yol gösterme / ilham",
  "aday 1039: ayet içi 1 (91:8 taşkınlık / sakınma) + ayetler arası 3 (91:3 / 4 gündüz / gece; 91:5 / 6 gök / yer; 91:9 / 10 kurtuluş / hüsran)",
  "aday 1041: blokta kayıt yok — lafız ve Rab yok",
  "bağ: kalıp / lemma eşleri okumayla (79:27, 79:28, 79:29, 79:30, 87:2, 87:14, 20:111, 81:17, 89:4, 90:3, 90:10); bütün emsaller sohbette AR + meal ile basıldı",
  "◈K / ◈B: ◈K dolu 91:1 شمس, 91:2 قمر, 91:3 نهر, 91:4 ليل, 91:5 سمو, 91:6 أرض; ◈B tetik yok; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 10 / 0; oturum_xy 21 sayım, 0 uyuşmaz",
  "süreç: sûre 91 dosyaları beled_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_91.py, oturum dışı); blok sınırı sûrenin bölümlerine göre (1-10 yeminler + nefis + cevap; 11-15 Semûd); taban 75699c1 değişmedi — sûre 91 zip'i 87-90'ı da taşıyacak",
 ],
 (11, 15): [
  "esmâ: e_oto 0 token; KARAR değişmedi (720); lafız 2 (91:13 'resûlu'llâh', 'nâqatu'llâh'), Rab 1 (91:14) — sûrede lafız 2, Rab 1",
  "kök tablosu: kok_ekle_91 1 kök (دمدم 91:14; korpusta tek ayet); 1526 → 1527; retroaktif yama hedefli 0, genel 0 (ikinci koşu da 0)",
  "yıldız: ★★★ 91:13 allah z=5,18; ★★★ 91:14 hapaks z=3,28 (eşiği geçen diğer: rab 2,72); ★ 91:11 kaynak n, kafiye kırığıyla — kırık sahte (aşağıda); formül davranışı",
  "fâsıla (924): 91:11 ölçüm KAFİYE KIRILMASI — son harfte medde işareti (ٓ) harf sayıldı; metinde ا, sûre boyunca tek tip — yanlış pozitif (sûre 70 dikkati ile aynı); 91:11 ★ bu kırıktan geliyor — artefakt",
  "iltifât: blokta ölçüm 0; anlatı 3FS / 3MP / 3MS içinde",
  "alıntı: 91:13 'qâle' ile işaretli söz, ayet sonunda kapanıyor — meal tırnaklı; içerik iki ACC ad, fiil yazılmamış — meal '(gözetin)' ile tamamladı",
  "adsız gönderge (1017): 91:12 en bedbahtları; 91:13 Allah'ın elçisi (tamlama, ad yok); 91:15 'yaxâfu' öznesi",
  "KAPATILAMAZ: 91:14 son 'sevvâhâ'daki 3FS göndergesi; 91:15 'yaxâfu' öznesi ve 'uqbâhâ'daki 3FS göndergesi",
  "xref: 91:13 → 14:10 (basıldı)",
  "çıpa: blokta merdiven uygulanan ayet yok (5 ayetin 5'i olgu=False: kavim kıssası, söz, helâk, gaybî); tarayıcı v4 blokta aday vermedi",
  "aday 1041: blokta kayıt yok — lafız elçi ve deve tamlamalarında, Rab helâk fiilinin öznesi; lemma 'sevvâ' 91:7 'mâ' (adsız) / 91:14 Rab — insan değil, okuma notu",
  "aday 1039: blokta karşıt çift yok",
  "bağ: kalıp / lemma eşleri okumayla (69:4, 54:23, 87:11, 11:64, 26:155, 54:27, 54:29, 14:10, 67:11, 89:9); bütün emsaller sohbette AR + meal ile basıldı",
  "◈K / ◈B: blokta tetik yok (deve kökü نوق tetik listesinde değil); tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 1-15 toplam 15 / 0; oturum_xy blok 17, 1-15 toplam 38 sayım, 0 uyuşmaz",
 ],
}

DUZELTME = {
}
