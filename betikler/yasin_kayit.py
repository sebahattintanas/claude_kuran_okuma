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
 # blok 21-30
 28: dict(kademe='L0', olgu=True, cipa=False, not_='gök yalnız indirmenin (olumsuz) çıkış yeri olarak adlanıyor; süreç yok; tarayıcı vermedi'),
 # blok 31-40
 33: dict(kademe='L2', olgu=True, cipa=False, not_='ölü yer → diriltme → tane çıkışı → yeme: nedensel zincir, yağmur adlanmıyor (35:9 emsali L2); tarayıcı vermedi'),
 34: dict(kademe='L1', olgu=True, cipa=False, not_='bahçe (hurma, üzüm) ve pınar yer alanında adlanıyor, aralarında ilişki yok (27:61 emsali)'),
 35: dict(kademe='L2', olgu=True, cipa=False, not_="'mâ amilethu eydîhim' nâfiye okumasıyla YETİ SINIRI (27:60 emsali); mevsûle okunursa L1 — kademe i'râb seçimine bağlı, KAPATILAMAZ; tarayıcı v4 adayı, çıpa değil"),
 36: dict(kademe='L1', olgu=True, cipa=False, not_='çift kavramı üç alana (yerin bitirdiği, enfus, bilinmeyen) dağıtılıyor, sınıflara üye eşlenmiyor (29:40 ölçütü; 30:22, 35:27 emsali); tarayıcı vermedi'),
 37: dict(kademe='L2', olgu=True, cipa=False, not_='gündüzün geceden sıyrılması → karanlık (fe-izâ sonucu): nedensel bağ; 31:29 ve 35:13 karşılıklı geçiş L1 (1010 ailesi); tarayıcı vermedi'),
 38: dict(kademe='L1', olgu=True, cipa=False, not_="güneşin akışı + varış yeri (mustaqarr); 'takdîr' ölçü adı, birim ve sayı yok (35:13 emsali); tarayıcı vermedi"),
 39: dict(kademe='L1', olgu=True, cipa=False, not_="ölçü fiili (qaddarnâ) + birim adı (menâzil), SAYI yok — L4 ölçü koluna sınırda (32:5 sayı+karşılaştırma; 30:4 emsali); teşbihte karşılaştırma var, algı/durum ayrımı yok → L3 değil; tarayıcı vermedi"),
 40: dict(kademe='L2', olgu=True, cipa=False, not_="güneş için YETİ SINIRI (lâ yenbeğî … en tudrike) + her birinin ayrı feleği; süreç işleyişi adlanmıyor → L4 değil; tarayıcı vermedi"),
 # blok 41-50
 41: dict(kademe='L1', olgu=False, cipa=False, not_='gemi adlanıyor + işlevi (taşıma); araç, doğal süreç değil (28:73 adlandırma+işlev emsali); tarayıcı vermedi'),
 # blok 61-70
 68: dict(kademe='L2', olgu=True, cipa=False, not_='ömrün uzaması → yaratılışta tersine dönüş (yaşlanmada gerileme): iki durum arasında bağımlılık; aşama ve mekanizma adsız; tarayıcı vermedi'),
 # blok 71-83
 71: dict(kademe='L1', olgu=True, cipa=False, not_='davar sınıfı (en\'âm) adlanıyor + sahiplik işlevi; tarayıcı v4 adayı, çıpa değil'),
 72: dict(kademe='L1', olgu=True, cipa=False, not_='davarların işlevi: binek ve besin'),
 73: dict(kademe='L1', olgu=True, cipa=False, not_='fayda ve içecek işlevi; madde adı yok'),
 77: dict(kademe='L1', olgu=True, cipa=False, not_='nutfe → hasım: madde ve sonuç, ara aşama yok (35:11, 32:7 emsali); tarayıcı v4 adayı, çıpa değil'),
 78: dict(kademe='L0', olgu=True, cipa=False, not_='çürümüş kemik adlanıyor (itirazın içinde), süreç yok'),
 80: dict(kademe='L1', olgu=True, cipa=False, not_='yeşil ağaç → ateş: madde, ürün ve kullanım; dönüşüm süreci yok; tarayıcı vermedi'),
 81: dict(kademe='L0', olgu=True, cipa=False, not_='gökler ve yer adlanıyor (a fortiori delil), süreç yok'),
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
 (21, 30): [
  "esmâ TANIM DIŞI: 36:23 Rahmân bağımsız ad (şart cümlesinde özne) — göndergesi Allah, 'ilahi' verildi (aday 1019, üçüncü vaka: 36:11, 36:15, 36:23)",
  "esmâ: §4.3 YANLIŞ MÜHÜR — 36:24 mübîn (sapıklığın sıfatı); sûrede mübîn yanlış mührü üçüncü (36:12, 36:17, 36:24)",
  "esmâ: 36:22 son üç içerik lemması BOŞ (yalnız fiil, zamir, ism-i mevsul) — mühür değerlendirilemiyor (kayıt)",
  "yıldız: 36:25 ★★★ tek Rab 4 kelimede (rab z=5,01) — aday 1020 ikinci vaka; 36:27 ★★ rab z=2,72 (7 kelime) aynı aile",
  "gloss: حسر 'yorgunluk, bitkinlik' — 36:30 hasret (pişmanlık); TAM SAYIM 12 token, pişmanlık lemmaları 9, yorgunluk 3 — baskın lemma yok (aday 1015 ailesi)",
  "say: 36:29 vâhide DOĞRU POZİTİF",
  "nakarat3: eş ayet satırda yok (aday 1003) — defterden: 36:23 → 36:74, 36:29 → 36:53 (7 kelime) ve 36:49 · 36:53 (3 kelime), 36:30 → 36:46",
 ],
 (31, 40): [
  "esmâ SINIR VAKASI: 36:38 'taqdîru'l-azîzi'l-alîm' — tamlama içinde ad, göndergesi Allah, 'ilahi' ×2 (aday 999, dördüncü vaka: 34:6, 35:14, 36:5, 36:38); §4.3 çift mühür geçerli",
  "gloss (aday 1021): نهر 'ırmak' — BASKIN lemma nehâr (gündüz) 57/113 yok (36:37, 36:40); حبب 'sevgi' — habb/habbe (tane) 12/95 yok (36:33); سبح 'tesbih' — yüzme lemmaları 5/92 yok (36:40)",
  "gloss: ظلم 'zulüm' — 36:37 muzlimûn karanlık anlamında (aday 1015 kaydı, zulumât 23)",
  "say: 36:36 zevc YANLIŞ POZİTİF (aday 1005 ailesi)",
  "bilanço: ★★★ 36:39 hapaks kaynaklı (عرجن, z=3,28; 983 birikimi; sûrede ikinci, 36:8)",
  "tarayıcı v4: 36:35 aday, kademe L2 (i'râba bağlı), çıpa değil (948)",
  "çıpa: 36:39 L4 ölçü koluna sınırda (birim adı var, sayı yok) — merdivende 'birimli, sayısız ölçü' basamağı yok (30:4 emsali)",
  "nakarat: 36:33 ↔ 36:37 've âyetun lehum' iki kelimelik açılış — nakarat3 (alt sınır 3) ve ikili alanı yakalamıyor (kayıt)",
  "nakarat3: eş ayet satırda yok (aday 1003) — defterden: 36:32 → 36:53",
 ],
 (41, 50): [
  "lafız: SÛREDE İLK lafız 36:47 (iki token, ikisi de alıntı içinde); 36:1-46 lafız 0 (korpus sayımı) — kayıt",
  "iltifât: 36:45 alan 1 (yön '1>23'), ayette 1. şahıs yok; 3MP → 2MP alıntı başlangıcı — YANLIŞ POZİTİF (1017 ailesi); aynı yapıdaki 36:47'de alan 0 (tutarsız)",
  "yıldız: 36:45 ★★★ pas z=3,48 (2/3 edilgen) — edilgen kaynaklı ★★★ (aday 1009 ailesi, 35:4 emsali)",
  "esmâ: §4.3 YANLIŞ MÜHÜR — 36:47 mübîn (sapıklığın sıfatı); sûrede mübîn yanlış mührü dördüncü (36:12, 17, 24, 47)",
  "say: 36:49 vâhide DOĞRU POZİTİF",
  "nakarat3 eşleri (defterden, aday 1003): 36:45 ↔ 36:47 (iżâ qîle lehum); 36:46 ↔ 36:30 DOĞRULANDI; 36:47 ↔ 36:15 DOĞRULANDI (in entum illâ); 36:49 → 36:29 · 36:53",
  "çıpa: 36:41 L1 olgu hayır (gemi, araç); 36:43 boğulma şartlı, olgu değil — kademe verilmedi",
 ],
 (51, 60): [
  "esmâ TANIM DIŞI: 36:52 Rahmân bağımsız ad (özne) — 'ilahi' (aday 1019, dördüncü vaka: 36:11, 15, 23, 52); §4.3 mühür geçerli, ölçüm satırı 'MÜHÜRSÜZ' (ayrı tanım: son kelime)",
  "esmâ: 36:58 selâm esenlik sözü (nekre) → 'degil'; rahîm Rab'bin sıfatı → 'ilahi'; mühür geçerli",
  "esmâ: §4.3 YANLIŞ MÜHÜR — 36:60 mübîn (düşmanın sıfatı); sûrede mübîn yanlış mührü beşinci (36:12, 17, 24, 47, 60)",
  "yıldız: 36:58 ★★★ tek Rab 5 kelimede (rab z=3,94) — aday 1020 üçüncü vaka (36:16, 36:25, 36:58)",
  "gloss (aday 1021 girdisi): بني 'bina, yapma' — BASKIN anlam akrabalık (benî 80, ibn 63, bint 17 = 160/184) yok (36:60)",
  "gloss: ظلل 36:56 zılâl (gölgeler) — aday 1015 kaydı (baskın lemma zıll yok)",
  "gloss: ظلم 36:37 karanlık / 36:54 zulüm — tek kök iki anlam, gloss yalnız zulüm (1015)",
  "say: 36:53 vâhide DOĞRU POZİTİF; 36:56 zevc YANLIŞ POZİTİF (1005)",
  "araç: أيي kök ipliği 36:59 'eyyuhâ' (nidâ edatı, lemma eyy) tokenini âyet ile birleştiriyor — sûrede âyet tokeni 5, iplik 6 sayıyor (aday 924: kanıt değil)",
  "iltifât: 36:59 alan 1 (yön '3>2'), ayette yalnız 2MP — tetik ayet içi mi ayetler arası mı belirsiz (517/1017 ailesi)",
  "nakarat3: 36:53 üç kalıp — 36:29 (7 kelime) ve 36:32 eşleri DOĞRULANDI; 'illâ sayhaten vâhideten' üçlüsü 29/49/53 tamamlandı",
 ],
 (61, 70): [
  "esmâ: §4.3 YANLIŞ MÜHÜR — 36:69 mübîn (Kur'an'ın sıfatı); sûrede mübîn yanlış mührü altıncı (36:12, 17, 24, 47, 60, 69)",
  "esmâ: 36:70 hayy — e_oto esmâ saydı (D2 eşlemesi), gönderge insan → e_el 'degil'; §4.3 YANLIŞ MÜHÜR. Ölçüm satırı 'esmâ yok', esmâ kaydı e_oto=1 — iki alan ayrışıyor (kayıt); okuyucu kararı ilk koşuda eksikti, esma_kayit çıktısıyla yakalandı ve eklendi",
  "yıldız: 36:63 ★★ pas z=2,52 (tek kaynak); 36:67 ★★★ hapaks مسخ z=3,28 (983 birikimi; sûrede üçüncü: 36:8, 39, 67)",
  "say: 36:62 kesîr YANLIŞ POZİTİF (belirteç; aday 1004 ailesi)",
  "gloss (1021 ailesi, baskın değil): جبل 'dağ' — cibille (topluluk) 2/41 yok (36:62); رجل 'adam; yaya' — ricl (ayak) 15/73 yok (36:65)",
  "tarayıcı v4: 36:66 ve 36:70 aday, doğal olgu yok, çıpa değil (948)",
  "nakarat3: 36:70 eşi 36:7 DOĞRULANDI ('haqqa'l-qavlu alâ')",
  "nakarat: 36:50 ↔ 36:67 aynı yapı (istitâ'a + lâ yerci'ûn) — nakarat3 yakalamıyor (kayıt)",
 ],
 (71, 83): [
  "esmâ: §4.3 YANLIŞ MÜHÜR — 36:77 mübîn (hasmın sıfatı); sûrede mübîn yanlış mührü yedinci (36:12, 17, 24, 47, 60, 69, 77) — mübîn'in sûredeki 7 e_oto tokeninin 7'si 'degil'",
  "esmâ: 36:79 evvel ('ilk kez') e_oto esmâ saydı → 'degil'; ölçüm satırı yalnız alîm'i yazıyor — 36:70 hayy ile ikinci ölçüm/esmâ kaydı ayrışması; okuyucu kararı ilk koşuda eksikti, esma_kayit eksik denetimiyle yakalandı",
  "esmâ: 36:79 alîm, 36:81 hallâq-alîm — O'na dönen zamirin haberi, 'ilahi'; mühür geçerli (81 çift)",
  "yıldız: 36:74 ★★ pas 2,52 + allah 2,33 (iki bileşen); 36:83 ★★★ pas z=5,38 tek kaynak, 8 kelimede tek edilgen fiil (aday 1009 ailesi; 36:45 ile sûrede ikinci)",
  "biçim: 'innemâ' (inne + mâ kâffe) HASR olarak işaretlenmiyor — 36:11 ve 36:82 (alan arızası, aday 924)",
  "tarayıcı v4: 36:71 (L1) ve 36:77 (L1) aday, çıpa değil (948)",
  "nakarat3: 36:74 eşi 36:23 DOĞRULANDI — sûrede bekleyen eş kalmadı",
  "nakarat: 36:22 ↔ 36:83 've ileyhi turja'ûn' ve 36:35 ↔ 36:73 'e-felâ yeşkurûn' — nakarat3 (3 kelime alt sınırı) yakalamıyor (kayıt)",
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_36.py uygular)
DUZELTME = {
 25: dict(alan='mercek', eski="Rab'bin iyelik eki: 36:22 'beni yaratan' (1S sıla) → 36:25 'sizin Rabbiniz' (2MP).",
         dogru="36:22'de Rab yok: orada Yaratıcı sılayla anılıyor ('beni yaratan', 1S nesne). Rab'bin iyelik eki ancak 36:25 'sizin Rabbiniz' (2MP) → 36:27 'Rabbim' (1S) arasında karşılaştırılabilir; 36:16 'Rabbimiz' (1P).",
         aday=None, blok='21-30'),
}
