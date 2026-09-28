# -*- coding: utf-8 -*-
"""ahzab_kayit.py — sûre 33 okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır.
"""
S = 33

CIPA = {
 72: dict(kademe='L0', olgu=True,  cipa=False, not_='gökler, yer, dağlar adlandırılıyor; emanet sahnesi, fiziksel iddia yok'),
 4:  dict(kademe='L1', olgu=True,  cipa=False, not_='bir göğüste iki kalp: sayı + organ + yer, mekanizma yok; ayette analojinin tabanı'),
 9:  dict(kademe='L0', olgu=True,  cipa=False, not_='rüzgâr adlandırılıyor, başka iddia yok'),
 10: dict(kademe='L0', olgu=False, cipa=False, not_='gözlerin kayması, yüreklerin gırtlağa dayanması: korku betimi (mecaz)'),
 13: dict(kademe='L3-benzeri', olgu=False, cipa=False, not_='beyan / durum ayrımı (evler korunmasız değil) — konu niyet, olgu değil'),
 19: dict(kademe='L1', olgu=False, cipa=False, not_='korkudan göz dönmesi, ölüm baygınlığına benzetme — davranış betimi'),
}

ARIZA = {
 (1, 10): [
  "blok_goster.py besmele ayıklaması 33:1'de besmeleyi bırakıyordu (eski kural 26/112) — okumayı bloke ettiği için ONARILDI (112/112, 1:1'deki BOM ayrıca)",
  "say: zevc 'eş' anlamında iki kez (33:4, 33:6) ve a'adde 'hazırladı' (33:8) sayı işareti sayılıyor — yanlış pozitif (borç #13)",
  "mm2: 33:10 zann fiili + ez-zunûn (ACC, aynı kök) araya lafız girdiği için yakalanmadı — bitişiklik koşulu (27:58 ile ikinci vaka)",
  "yıldız: 33:4 hapaks + n + kafiye kırığı, formül yalnız birini sayıyor (borç #15)",
  "esmâ: 33:6 mü'min ×2 + velî insan göndergeli; e_oto sınıfı etkilemedi (lafız var) ama §4.2 sınama kümesine girer",
  "ton: vekîl (33:3) varlik_katalog'da tonsuz — katalog 72 lemmanın 26'sını kapsıyor",
 ],
 (11, 20): [
  "gloss: belâ kökü 'eskiyip yıpranma' (33:11'de ve kökün baskın lemmalarında anlam SINAMA); devr kökü 'yurt, ev' (33:19 tedûru = dönmek); velî kökü 'dost, veli' (33:15 yüvellûne = arka çevirmek)",
  "say: qalîl üç kez (33:16, 33:18, 33:20) sayı işareti — miktar sözcüğü, tartışmalı",
  "mm2: 33:11 zülzilû zilzâlen YAKALANDI (bitişik) — 33:10 ile karşıt çift",
  "yıldız: 33:19 hapaks z=3,28 + n z=2,40, formül yalnız birini sayıyor (borç #15)",
  "esmâ: 33:11 mü'min (insan) sınıfı E yapıyor (e_oto) ve §4.3 son-üç tanımıyla MÜHÜR; 33:17 velî + nasîr ('Allah'tan başka') ÇİFT MÜHÜR — ikisi de yanlış",
  "ikili: Yesrib (33:13) köksüz özel ad, ikili alanında görünmüyor (borç 972)",
 ],
 (21, 30): [
  "esmâ: âhir iki kez ilâhî olmayan sıfat (33:21 âhiret günü, 33:29 âhiret yurdu); 33:21'de son-üç içinde olduğu için §4.3 YANLIŞ MÜHÜR (sûrede üçüncü)",
  "esmâ: mü'min üç kez insan göndergeli (33:22, 33:23, 33:25)",
  "ton: 33:25 'karma' — kavî katalog-dışı, azîz katalogda cemâl; 'karma' etiketi eksik tonu gerçek ton farkından ayırmıyor",
  "say: kesîr (33:21), zevc 'eş' (33:28), a'adde 'hazırladı' (33:29) yanlış pozitif; 33:30 di'fayn (iki kat) gerçek sayı ifadesi YAKALANMIYOR — yanlış negatif",
  "yıldız: ★★★ ikisi hapaks (33:23 nahb, 33:26 sayâsî), biri allah yoğunluğu (33:25, 3 lafız / 16 kelime) — içerikten ★★★ yok",
 ],
 (31, 40): [
  "say: 33:31 merrateyn (iki kere) gerçek sayı ifadesi YAKALANMIYOR (33:30 di'fayn ile ardışık ikinci yanlış negatif); a'adde yakalanıyor, aynı anlamdaki a'tednâ (عتد) yakalanmıyor",
  "say: zevc 'eş' anlamında üç kez (33:37); ehad 'hiç kimse' üç kez (33:32, 33:39, 33:40) — tartışmalı",
  "esmâ: §4.3 YANLIŞ MÜHÜR iki kez — 33:31 kerîm (rızkın sıfatı), 33:36 mübîn (sapıklığın sıfatı); ehad (33:32) lafızsız ayeti E sınıfına sokuyor",
  "yıldız: 33:37 n z=3,78 + hapaks 3,28 + allah 1,56 — üç ölçüt, biri sayılıyor (borç #15); 33:39 ★★★ allah yoğunluğu (3 lafız / 13 kelime)",
  "iltifât: 33:33 aynı ayette 2FP → 2MP geçişi (ehl-el-beyt) iltifât alanında görünmüyor",
  "dikey: komşulukta karşılıksız kök (hame') çıktı — glossu eklendi",
 ],
 (41, 50): [
  "mm2: 33:41 üzkürullâhe zikran — araya lafız giriyor, YAKALANMIYOR (33:10'dan sonra sûrede ikinci bitişik-olmayan vaka)",
  "esmâ: 33:43 tek gerçek esmâ (rahîm) ama son-üçte nûr ve mü'min de var → §4.3 'ÇİFT' ve ton 'karma' yanlış tokenlerden; 33:44 selâm + kerîm tamamen yanlış ÇİFT MÜHÜR; 33:47 kebîr (lütfun sıfatı) YANLIŞ MÜHÜR",
  "esmâ: 33:43 okuyucu kararıyla sûrenin ilk gerçek E sınıfı (lafız/Rab yok, özne zamir)",
  "say: a'adde dördüncü yanlış pozitif (33:44); 'idde ta'teddûnehâ (33:49) aynı kökten ilk açık DOĞRU pozitif; zevc ×2 (33:50)",
  "yıldız: 33:50 ★★★ tek kaynak n z=5,16 (sûrenin en uzun ayeti)",
 ],
 (51, 60): [
  "gloss: حيي 'diri olma, hayat' — 33:53 istihyâ (utanmak) ×2 ve 33:44 tahiyye (selamlama) bu glossta yok (aday 987 ailesi)",
  "esmâ: §4.3 YANLIŞ MÜHÜR iki kez — 33:57 âhir (âhiret), 33:58 mübîn (günahın sıfatı; lafızsız ayet, e_oto E → e_el 0)",
  "say: zevc 'eş' üç kez (33:52, 33:53, 33:59), a'adde beşinci kez (33:57), qalîl (33:60)",
  "yıldız: 33:53 ★★★ tek kaynak n z=6,01 (sûrenin en uzun ayeti)",
 ],
 (61, 70): [
  "gloss: نور 'nûr, ışık' — 33:66 nâr (ateş); envanterde nâr 145, nûr 43: gloss baskın lemmanın tersini gösteriyor (aday 987)",
  "gloss: سدد 'set' — 33:70 kavlen sedîdâ (doğru söz) bu glossta yok (aday 987)",
  "say: 33:68 di'fayn (azabın iki katı) YAKALANMIYOR — sûrede üç gerçek ikil sayı ifadesinin (33:30, 33:31, 33:68) üçü de işaretsiz; a'adde altıncı yanlış pozitif (33:64)",
  "esmâ: §4.3 YANLIŞ MÜHÜR üç kez — 33:63 karîb (saatin sıfatı), 33:65 velî + nasîr ÇİFT (olumsuzlanan başkası; lafızsız, e_oto E → e_el 0), 33:68 kebîr (lânetin sıfatı); blokta geçerli mühür YOK",
  "yıldız: 33:61 ★★★ tek kaynak pas z=5,38 (üç fiil, üçü edilgen)",
 ],
 (71, 73): [
  "esmâ: 33:73 mü'min (insan) son-üç dışında; mühür gafûr-rahîm geçerli — blokta yanlış mühür yok",
  "yıldız: 33:73 ★★★ tek kaynak allah z=3,47 (3 lafız / 15 kelime)",
  "azîm (33:71) varlik_katalog'da ilâhî isim (denge), esmâ listesinde yok — aday 986",
 ],
}
