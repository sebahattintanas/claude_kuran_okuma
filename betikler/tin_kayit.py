# -*- coding: utf-8 -*-
"""tin_kayit.py — sûre 95 (Tîn) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 95

CIPA = {
 # blok 1-8
 1: dict(kademe='L0', olgu=True, cipa=False, not_="'ve't-tîni ve'z-zeytûn' — yemin edilen iki bitki adı; süreç / mekanizma yok — L0; tarayıcı vermedi"),
 2: dict(kademe='L0', olgu=True, cipa=False, not_="'ve tûri sînîn' — yemin edilen adlı yer; süreç yok — L0; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ve hâze'l-beledi'l-emîn' — gönderge adsız, işaretli belde (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe='L1', olgu=True, cipa=False, not_="'le-qad xalaqne'l-insâne fî ahseni taqvîm' — yaratma + nitelik; aşama / madde / mekanizma yok — L1 (90:4 kaydı emsali); tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'thumme radednâhu esfele sâfilîn' — dönüşüm, göndergesi yazılmamış (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'ille'llezîne âmenû …' — tutum / âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'fe-mâ yukezzibuke ba'du bi'd-dîn' — soru / tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'e-leyse'llâhu bi-ahkemi'l-hâkimîn' — soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 8): [
  "esmâ: e_oto 0 token; KARAR değişmedi (725); lafız 1 (95:8), Rab yok — sûrede lafız 1, Rab 0; 'ahkem' esmâ listesinde değil",
  "kök tablosu: kok_ekle_95 1 kök (تين 95:1; korpusta tek ayet); 1529 → 1530; retroaktif yama hedefli 0, genel 0 (iki koşu); taban kayıtları om_base ile aynı",
  "yıldız: ★★★ 95:1 hapaks z=3,28 (yeni kök); ★★★ 95:8 allah z=4,47 — formül davranışı",
  "fâsıla: metin ن 7, م 1 (95:4); ölçüm hepsini N sınıfında tutuyor, kırık yok; 94:8 ب → 95:1 ن sûre sınırı",
  "biçim (924): 95:1 QASEM, ayet 1 harf 33 → harf3 14 (besmele ailesi); 95:2-3 atıflı yeminlerde QASEM yok; 95:3 DIKKAT (işaret)",
  "iltifât (924): ölçüm 0 — 95:7'de 2MS hitabın girişi {3} → {2, 3} kısmi örtüşme",
  "özel ad: 'Sînîn' (95:2) morph'ta özel ad (yer), korpusta 1; 23:20 'tûri seynâ'' aynı tamlama, ikinci ad başka biçimde",
  "adsız gönderge (1017): yemin eden; konuşan 1P (95:4-5); 95:3 belde (işaret, ad yok); hitap 2MS (95:7)",
  "KAPATILAMAZ: 95:5 'esfele sâfilîn'in göndergesi; 95:7 'ba'du'nun neyin sonrası olduğu",
  "çıpa: L1 1 (95:4 yaratma + nitelik — 90:4 kaydı emsali); L0 2 (95:1 bitki adları, 95:2 adlı yer — yemin edilen); olgu=False 5; tarayıcı v4 aday vermedi",
  "aday 1040 (kayıt): 94:8 / 95:1 sûre sınırı — Rabbe yönelme emri ile kapanış / incir ve zeytine yemin ile açılış; fâsıla ب → ن; 94 Rab 1, 95 lafız 1; ardışık olmayan sûreyle korpusun iki geçişi: 'le-qad xalaqne'l-insân' 90:4 / 95:4, ikisi de yeminin ardından",
  "aday 1039: ayetler arası 1 (95:4 / 5 en güzel biçim / aşağıların en aşağısı)",
  "aday 1041 (kayıt): 95:8 kök حكم aynı ayette lafız için ('ahkem') ve hükmedenler için ('el-hâkimîn')",
  "bağ: kalıp / lemma eşleri okumayla (94:8, 80:29, 52:1, 23:20, 90:1, 90:4, 11:82, 84:25, 41:8, 82:9, 39:36, 11:45); bütün emsaller bu oturumda AR + meal ile basıldı",
  "◈K / ◈B: ◈K tetik yok; ◈B 95:4 (خلق, أنس); bitki adları ve 'tûr' tetik listesinde değil; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 8 ayet; oturum_xy 26 sayım, 0 uyuşmaz",
  "süreç: sûre 95 dosyaları insirah_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_95.py, oturum dışı); tek blok; taban 86953a8 (sûre 92-94 zip'leri yüklenmedi) — sûre 95 zip'i 92-94'ü de taşıyacak",
 ],
}

DUZELTME = {
}
