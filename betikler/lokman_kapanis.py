# -*- coding: utf-8 -*-
"""lokman_kapanis.py — sûre 31 (Lokmân) kapanış notları, çıpa tablosu ve ilerleme."""
import json, gloss_gecis

ATLAMA = {
 "_cipa_tablosu_31": (
  "SÛRE 31 ÇIPA KAYITLARI — **üç çıpa, ikisi TARTIŞMALI.** "
  "**31:10 (L2, olgu EVET)** — iki nedensellik: dağlar → 'sizi sarsmasın diye' (أَن تَمِيدَ بِكُمْ), gökten su → "
  "her güzel çiftten bitki. 'Görebileceğiniz direkler olmaksızın' algı/durum ayrımına yakın ama karşılaştırma "
  "yok → L3 DEĞİL. "
  "**31:14 (L4 adayı, TARTIŞMALI)** — süreç (zayıflık üstüne zayıflıkla taşıma) + zaman birimi (sütten kesme iki "
  "yıl). Mekanizma yok, ölçü var. Sûre 27-28 kademe tablosunda L4 hiç yoktu; kademe kararı okumaya bağlı → "
  "KAPATILAMAZ. "
  "**31:34 (L2 adayı, TARTIŞMALI)** — yağmurun indirilmesi ve rahimlerdekinin bilinmesinden sonra iki kez sınır: "
  "'hiçbir nefis bilmez'. Ölçütteki 'yeti sınırı' FİİL yetisi için yazılmıştı; burada sınır BİLGİYE konuyor → "
  "KAPATILAMAZ. "
  "**Çıpa olmayan ama kademe taşıyan ayetler:** 31:16 (L1, hardal tanesi ölçü ama iddia bilgiye dair) · 31:19 "
  "(L1, seslerin karşılaştırması) · 31:20 (L1, boyun eğdirme = adlandırma + işlev) · 31:29 (L1, gece-gündüz "
  "geçişi; süreç tarifi var, nedensellik ve birim yok) · 31:31 (L1, gemilerin akışı; sebep 'Allah'ın nimeti')."),

 "_tarayici_31": (
  "**TARAYICI v4 SÛRE 31'DE İKİNCİ KEZ SIFIR ANMA — anma 0/3, kesinlik 0/7.** Sûre 30'da 2/9 idi; burada üç "
  "çıpanın üçünü de kaçırdı ve verdiği YEDİ adayın yedisi de yanlış pozitif çıktı (31:11, 31:16, 31:20, 31:25, "
  "31:27, 31:29, 31:31). "
  "**Kaçırmaların ortak özelliği:** 31:10'da amaç cümlesi ta'lîl LÂMI ile değil أَن + muzârî ile kuruluyor; 31:14 "
  "ve 31:34 düz haber cümlesi. Bu, aday 948'in söz-eylemi varsayımına sûre 30'dan sonra İKİNCİ sûre boyu "
  "olumsuz veri. "
  "**Yanlış pozitiflerin ortak özelliği:** işaret var (şart, bakış, ta'lîl) ama OLGU örnek ya da benzetme olarak "
  "kullanılıyor (hardal tanesi, ağaç-kalem, deniz-mürekkep, 'kim yarattı?' sorusu). Ölçüt DEĞİŞTİRİLMEDİ."),

 "_esma_arizasi_31": (
  "ESMÂ MÜHRÜ — **24 token, mühürlü 16 ve hepsi geçerli; mühürsüz 8'in 6'sı YANLIŞ POZİTİF.** "
  "Yanlış pozitifler ilâhî olmayan bir şeyin sıfatı: 31:2 حَكِيم (Kitab'ın) · 31:4 آخِر (âhiret) · 31:10 كَرِيم "
  "(bitki çiftinin) · 31:11 مُبِين (sapkınlığın) · 31:31 شَكُور (insanın) · 31:32 بَرّ ('KARA', ORTA konum). "
  "Geçerli ama mühürsüz iki token: 31:23 عَلِيم ve 31:29 خَبِير — gerçek ilâhî ad, ama ayet sonunda ÇİFT "
  "oluşturmuyorlar. **Borç #9/#12 bu sûrede iki ayrı hata türü üretti:** ilâhî olmayan sıfatı esmâ sayma ve "
  "gerçek esmâyı tekil olduğu için mühürsüz bırakma."),

 "_yildiz_kaynagi_31": (
  "YILDIZ KAYNAKLARI (TAM SAYIM) — ★★★ 3 · ★★ 3 · ★ 9 · yıldızsız 19. "
  "Kaynak dağılımı: **allah 6 · n 5 · hapaks 2 · rab 1 · kafiye kırığı 1.** "
  "**Üç ★★★'ın ikisi otomatik hapaks tetikleyicisinden** (31:18 صعر, 31:32 ختر) — borç #7'ye iki yeni vaka. "
  "Üçüncüsü 31:26'da allah z=3,47 (on kelimede iki lafız), yani payda etkisi (aday 909). "
  "**İçerikten gelen tek yıldız yok** — formülde içerik bileşeni zaten bulunmuyor."),

 "_kafiye_gecisi_31": (
  "KAFİYE — N 14 · R 16 · د 2 · ظ 1 · mukattaa 1. Sûre ortasında **N → R geçişi** var. "
  "Kırık bayrağı dört ayette (31:12, 31:14, 31:15, 31:26). **31:14 ve 31:15 geçişin iki yanı:** kural 'iki komşu "
  "aynı sınıf, ayet farklı' dediği için alternasyonun HER İKİ ayetini de işaretliyor ve 31:14'ün ★'ı yalnız "
  "buradan geliyor. **Geçiş bölgesinde kuralın çift işaret koyması kayda geçirildi.**"),

 "_kapanis_31": (
  "SÛRE 31 KAPANIŞI — 34 ayet, 546 kelime, tamamı Mekkî. "
  "EKSEN: lafız **32** · Rab **2** → **A/R = 16,0**; dizide 27→2,25 · 28→1,42 · 29→8,4 · 30→8,0 · **31→16,0**. "
  "Paydanın iki olması oranı oynak kılıyor; ham sayı okunmalı. "
  "ADLI AKTÖR: Lokmân (31:12, 31:13) · Şeytan (31:21). İltifât yalnız 31:28. "
  "BAĞLAR (TAM SAYIM, tekil ayet bağı): **22 (Hac) 12** · 2 (Bakara) 8 · 29 (Ankebût) 5 · 27 (Neml) 4 · 35 "
  "(Fâtır) 3. Açılış Bakara ve Neml açılışlarını taşıyor (31:4→27:3 TAM, 31:5→2:5 TAM); kapanışa yakın bölüm "
  "Hac 22:61-65 dizisiyle örtüşüyor (31:26→22:64 BENZER, 31:30→22:62 YAKIN 0,98). "
  "YENİ KÖK **16** (بثث عمد وقر حمر خدد سبغ صخر صعر فخر قصد عرو غلظ قلم وثق ختر غيث). "
  "OKUMA HATASI: 31:9 merceğine 'iki lafız' yazıldı, defter tek lafız veriyor; ölçüm satırındaki [2/32] "
  "gösterimi lafız sayısı sanıldı. Düzeltildi — hafızadan sayım kuralının bu oturumdaki ilk ihlali."),
}

ATLAMA = {k: gloss_gecis.gecir(v) for k, v in ATLAMA.items()}

# ilerleme DEFTERDEN koşulur (elle artırma, −2 kaymasının sebebiydi)
D = json.load(open('defter.json', encoding='utf-8'))
TAM = set([1] + list(range(9, 32)))
okunan = sum(1 for r in D if r['k'][0] in TAM or (r['k'][0] == 2 and r['k'][1] <= 20))

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
OM['31'].setdefault('_mercek_atlama_notu', {}).update(ATLAMA)
OM['ilerleme']['tam'] = sorted(set(OM['ilerleme']['tam']) | {31})
OM['ilerleme']['not'] = "Sûre 1, 9-30 ve **31 TAM**. Devam: sûre 32'den ya da sûre 2'nin 21. ayetinden."
OM['ilerleme']['okunan_ayet'] = okunan
OM['ilerleme']['korpus_yuzde'] = round(100 * okunan / len(D), 1)
OM['ilerleme']['sayim_notu'] = "okunan_ayet defter.json'dan koşulur; elle artırılmaz (eski sayaç −2 kaymıştı)."
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 31 →', len([k for k in OM['31'] if not k.startswith('_')]),
      'ayet +', len(OM['31']['_mercek_atlama_notu']), 'kapanış notu')
print('ilerleme:', OM['ilerleme']['okunan_ayet'], 'ayet (%', OM['ilerleme']['korpus_yuzde'], ')')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK['31_atlama'] = ATLAMA
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: 31_atlama →', len(MK['31_atlama']))
