# -*- coding: utf-8 -*-
"""yasin_kayit.py — sûre 36 (Yâsîn) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır.
"""
S = 36

CIPA = {
}

ARIZA = {
 (1, 10): [
  "esmâ: §4.3 YANLIŞ MÜHÜR — 36:2 hakîm (Kur'an'ın sıfatı); 36:5 azîz-rahîm geçerli",
  "esmâ SINIR VAKASI: 36:5 'tenzîle'l-azîzi'r-rahîm' — tamlama içinde ad, göndergesi Allah, 'ilahi' (aday 999, üçüncü vaka: 34:6, 35:14, 36:5)",
  "say: 36:7 ekser ('çoğu') belirteç, sayı değil — yanlış pozitif (1004/1005)",
  "harf: 36:1 harf 21 → harf3 2 — mukattaa harflerinde yazım alanı harf adını saymıyor (kayıt)",
  "bilanço: ★★★ 36:8 hapaks kaynaklı (983 birikimi)",
 ],
 (11, 20): [
  "esmâ TANIM DIŞI: 36:11 ve 36:15 Rahmân bağımsız ad (nesne / özne), sıfat ya da haber değil — göndergesi Allah, 'ilahi' verildi (aday 1019, 999 emsali)",
  "esmâ: §4.3 YANLIŞ MÜHÜR — 36:11 kerîm (ödül), 36:12 mübîn (kitap), 36:17 mübîn (tebliğ); ölçüm satırı Rahmân için de MÜHÜRSÜZ (orta konum)",
  "yıldız: 36:16 ★★★ tek Rab 6 kelimede (rab z=3,23) — kısa ayet şişmesinin Rab karşılığı (aday 1020)",
  "say: 36:14 isneyn, sâlis DOĞRU POZİTİF ×2",
  "gloss: طير 'kuş; uçan' — 36:18-19 tetayyur/tâir (uğursuzluk) yok (aday 1000 ailesi)",
  "tarayıcı v4: 36:14 (F_ölçü) ve 36:19 (şart) aday, doğal olgu yok, çıpa değil (948)",
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_36.py uygular)
DUZELTME = {
}
