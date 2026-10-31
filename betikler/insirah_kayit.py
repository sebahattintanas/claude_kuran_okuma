# -*- coding: utf-8 -*-
"""insirah_kayit.py — sûre 94 (İnşirâh) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 94

CIPA = {
 # blok 1-8
 1: dict(kademe=None, olgu=False, cipa=False, not_="'e-lem neşrah leke sadrek' — organ adı mecazî açma (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'ve veda'nâ 'anke vizrek' — tutum / söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ellezî enqada zahrek' — organ adı mecazî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'ve rafa'nâ leke zikrek' — tutum / söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'fe-inne ma'a'l-'usri yusrâ' — genel önerme (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'inne ma'a'l-'usri yusrâ' — genel önerme (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'fe-izâ feraġte fe'nsab' — buyruk (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'ve ilâ rabbike fe'rġab' — buyruk (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 8): [
  "esmâ: e_oto 0 token; KARAR değişmedi (725); lafız yok, Rab 1 (94:8) — sûrede lafız 0, Rab 1",
  "kök tablosu: blokta yeni kök yok (1529); retroaktif yama hedefli 0, genel 0",
  "yıldız: ★★★ 94:8 rab z=6,78 — lafızsız kısa ayette tek Rab (formül davranışı); başka yıldız yok",
  "fâsıla (924): metin ك 4 (94:1-4, 2MS iyelik eki), ا 2 (94:5-6), ب 2 (94:7-8); iki gerçek geçiş (94:5 ك → ا, 94:7 ا → ب) ölçümde kafiye kırığı olarak işaretlenmedi",
  "biçim (924): ayet 1 harf 32 → harf3 13 (besmele ailesi); 94:5 / 94:6 esit2 TAM + nakarat3 — fark baştaki 'fe', harf3 14 / 13",
  "iltifât (924): ölçüm 0 — 94:3 {1, 2} → {2, 3} ve 94:5-6 şahıssız ayetler; 1P konuşan + 2MS hitap 94:1'den itibaren",
  "lemma etiketi (924): 94:7 'fe'nsab' ile 88:19 'nusibet' morph'ta aynı lemma etiketinde — dikilmek / yorulmak, iki anlam",
  "organ adı: 'sadr' (94:1), 'zahr' (94:3) ◈B tetik listesinde değil — '—', gözlem ◇'de; ◈B 94:2 kök وضع tetiği 'indirme' anlamında, doğurma değil",
  "adsız gönderge (1017): konuşan 1P; hitap 2MS",
  "KAPATILAMAZ: 94:7 'feraġte'nin neyi bitirmek olduğu; 94:1 ve 94:4 'leke'nin neden yönelttiği yazılmamış",
  "çıpa: blokta merdiven uygulanan ayet yok (8 ayetin 8'i olgu=False: organ adları mecazî, önerme, buyruk); tarayıcı v4 aday vermedi",
  "aday 1040 (kayıt): 93:11 / 94:1 sûre sınırı — Rab nimetini anlatma emri ile kapanış / 'e-lem neşrah' sorusu ile açılış; fâsıla ث → ك; 93 Rab 3, 94 Rab 1; ardışık sûre okuma bağları 93:6 / 94:1 'e-lem' + cezm IMPF + 2MS, 92:7 ve 92:10 / 94:5-6 'yusr' / ''usr' (fu'lâ / fu'l)",
  "aday 1039: ayet içi 2 (94:5 ve 94:6 zorluk / kolaylık — tekrar) + ayetler arası 1 (94:2 / 4 indirdik / yükselttik)",
  "aday 1041: sûre içi kayıt yok; sûreler arası okuma notu yok",
  "bağ: kalıp / lemma eşleri okumayla (93:11, 93:6, 20:25, 39:22, 53:38, 84:10, 65:7, 92:7, 92:10, 87:8, 74:9, 55:31, 88:19, 68:32, 9:59); bütün emsaller bu oturumda AR + meal ile basıldı",
  "◈K / ◈B: ◈K tetik yok; ◈B 94:2 وضع; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 8 ayet; oturum_xy 16 sayım, 0 uyuşmaz",
  "süreç: sûre 94 dosyaları duha_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_94.py, oturum dışı); tek blok; taban 86953a8 (sûre 92-93 zip'leri yüklenmedi) — sûre 94 zip'i 92-93'ü de taşıyacak",
 ],
}

DUZELTME = {
}
