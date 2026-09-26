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
}
