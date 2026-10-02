# -*- coding: utf-8 -*-
"""sebe_kayit.py — sûre 34 (Sebe') okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır.
"""
S = 34

CIPA = {
 # blok 1-10
 1:  dict(kademe='L0', olgu=True,  cipa=False, not_='gökler ve yer adlandırılıyor; hamdın alanı, fiziksel iddia yok'),
 2:  dict(kademe='L1', olgu=True,  cipa=False, not_='yere giren/çıkan, gökten inen/yükselen: dört süreç + yön (2×2), mekanizma yok; iddia bilginin kapsamı'),
 3:  dict(kademe='L1', olgu=False, cipa=False, not_='zerre ağırlığı ölçü birimi, daha küçük/büyük ölçek; iddia bilgiye dair, olgu örnek (31:16 emsali)'),
 9:  dict(kademe='L1', olgu=True,  cipa=False, not_='yere geçirme, gökten parça düşürme: iki doğal olay koşul kipinde; tarayıcı v4 adayı, çıpa değil'),
 10: dict(kademe='L1', olgu=False, cipa=False, not_='demirin yumuşatılması: madde + nitelik değişimi, mekanizma yok; mucize anlatısı'),
 # blok 11-20
 12: dict(kademe='L4-biçim', olgu=False, cipa=False, not_="rüzgârın gidiş/dönüşü birer ay: süre birimi var, ama Süleyman'a verilen tasarruf — doğal düzenlilik değil; tanım açığı (aday 1002)"),
 14: dict(kademe='L2', olgu=True,  cipa=False, not_='yer canlısı değneği yiyor → düşme → anlama: nedensellik, mekanizma yok; tarayıcı v4 adayı, çıpa değil'),
 15: dict(kademe='L0', olgu=True,  cipa=False, not_='sağda ve solda iki bahçe adlandırılıyor'),
 16: dict(kademe='L2', olgu=True,  cipa=False, not_='sel → bahçelerin acı meyveli ağaçlara dönüşmesi: nedensellik, mekanizma yok'),
 18: dict(kademe='L1', olgu=False, cipa=False, not_='kasabalar arası ölçülü yürüyüş: yerleşim düzeni, insan eseri'),
 # blok 21-30
 22: dict(kademe='L1', olgu=False, cipa=False, not_='zerre ağırlığı ölçeği mülkün kapsamı için; olgu değil (34:3 emsali)'),
 24: dict(kademe='L0', olgu=True,  cipa=False, not_='gökten ve yerden rızık adlandırılıyor'),
 # blok 41-50
 46: dict(kademe=None, olgu=False, cipa=False, not_='tarayıcı v4 adayı: sayı kelimeleri (bir, ikişer, teker teker) tetikledi; doğal olgu yok, merdiven uygulanmadı'),
}

ARIZA = {
 (1, 10): [
  "gloss: أخر 'geciktirme, sonraya bırakma' — 34:1 ve 34:8'de âhira; kökün baskın lemması âhir (155), fiil ahhara 15 (aday 987 ailesi, kalan tarama borcu)",
  "gloss: حدد 'demir; sınır koyma' — baskın lemma hudûd (14), hadîd 6; iki anlam var ama sıra baskınlığın tersi (987 ailesi, hafif)",
  "esmâ: §4.3 YANLIŞ MÜHÜR iki kez — 34:3 mübîn (kitabın sıfatı), 34:4 kerîm (rızkın sıfatı); âhira iki kez (34:1, 34:8) ilâhî olmayan token — 34:1'de son-üç içinde ama mühür hakîm-habîr ile geçerli",
  "esmâ SINIR VAKASI: 34:6 sırâtı'l-azîzi'l-hamîd — isimler yüklem/sıfat değil muzâfun ileyh; göndergesi Allah, 'ilahi' verildi. e_suzgec kodlanırken bu konum türü (tamlama içinde ad olarak esmâ) ayrıca tanımlanmalı",
  "mm2: 34:7 mezzaktum kulle mumazzak — işlevce mef'ûl-i mutlak, kural (ACC isim w+1) yakalamıyor (982 ailesi)",
  "yıldız: 34:9 kafiye kırığı + n z=1,76; formül yalnız n'yi sayıyor (borç #15)",
  "tarayıcı v4: 34:9 aday, çıpa değil (948 birikimi)",
 ],
 (11, 20): [
  "bilanço: blok_bilanco.yildiz_kaynagi eşik altı bileşeni ★ kaynağı diye yazıyor; 34:18 ('allah -0,53') ve 34:19 ('rab 0,80') ★'ı aslında KAFİYE KIRIĞINDAN — aday 1001 (sûre 31: 1, 32: 1, 33: 0 vaka)",
  "çıpa tanımı: 34:12 L4 biçimli (birim: ay) ama olgusuz; eşik olgu koşulunu açık yazmıyor — aday 1002 (965 ailesi)",
  "esmâ: §4.3 YANLIŞ MÜHÜR üç kez — 34:13 şekûr (kullar), 34:19 şekûr (sabbâr), 34:20 mü'min; geçerli: 34:11 basîr, 34:15 gafûr (ikisi de tekil)",
  "say: qalîl iki kez sayı işareti (34:13, 34:16) — 981 ailesi; 34:12 'bir ay ... bir ay' ve 34:15-16 'iki bahçe' (ikil) sayı ifadesi YAKALANMIYOR",
  "gloss: جبي 'ictibâ' — 34:13 cevâb (havuzlar); أول 'ilk, evvel' — 34:13 âl (aile) (987 ailesi)",
  "ikili: Süleyman (34:12) köksüz ad — 21:81 ile rüzgâr bağı ikili alanında görünmüyor (borç 972)",
  "tarayıcı v4: 34:14 aday, çıpa değil (948 birikimi)",
 ],
 (21, 30): [
  "KENDİ OKUMA HATAM: 34:3 merceğinde 'nakarat3 10:61 ile 7 kelime' yazıldı; ölçüm satırındaki '2 ayet, tür ic' SÛRE İÇİ sayıdır, 7 kelimelik kalıbın eşi 34:22. 10:61'de sıra ters (yer · gök), kalıp orada yok. Ölçüm satırı eş ayeti basmıyor; xref ile karıştırıldı — aday 1003, DUZELTME ile işlendi",
  "esmâ: §4.3 YANLIŞ MÜHÜR bir kez — 34:24 mübîn (sapıklığın sıfatı); âhira üçüncü kez ilâhî olmayan token (34:21)",
  "say: ekser (34:28) sayı işareti — 981 ailesi",
  "blokta kafiye kırığı, hapaks, mm2 ve tarayıcı adayı yok",
 ],
 (31, 40): [
  "esmâ: §4.3 YANLIŞ MÜHÜR bir kez — 34:31 mü'min (insan); blokta başka e_oto tokeni yok",
  "say: ekser iki kez (34:35, 34:36) — 34:36 nicelik belirteci (981 yanlış pozitif), 34:35 GERÇEK karşılaştırmalı nicelik (mal ve evlatça daha çok) — 981 sayımında ayrı tutulmalı",
  "gloss: ملك 'mülk; melik' — 34:40 melâike; melek anlamı gloss'ta yok (987 ailesi)",
  "çıpa: blokta çıpa merdiveni ayeti yok; tarayıcı adayı yok",
 ],
 (41, 50): [
  "esmâ: §4.3 YANLIŞ MÜHÜR iki kez — 34:41 mü'min, 34:43 mübîn (sihir); geçerli: 34:47 şehîd (tekil), 34:50 semî'-karîb (çift)",
  "say: 34:45 mi'şâr DOĞRU pozitif (kesir 1/10); 34:46 vâhide, mesnâ doğru, furâdâ YAKALANMADI (yanlış negatif); 34:41 ekser belirteç (yanlış pozitif) — 981/1004",
  "tarayıcı v4: 34:46 aday — sayı kelimeleri tetikledi, olgu yok (948 birikimi)",
  "bilanço: 34:49 ★ kafiye kırığından, kaynak 'allah -0,53' diye yanlış etiket (aday 1001, sûre 34'te üçüncü vaka)",
  "yıldız: 34:48 kafiye kırığı + rab z=2,72 → ★★; kırık toplanmıyor (borç #15 sınırı)",
 ],
 (51, 54): [
  "esmâ: §4.3 YANLIŞ MÜHÜR — 34:51 karîb (mekânın sıfatı); 34:50'de aynı lemma Rab'bin sıfatıydı (geçerli)",
  "blokta çıpa ayeti, tarayıcı adayı, kafiye kırığı, say işareti yok",
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_34.py uygular)
DUZELTME = {
 3: dict(alan='mercek', eski="nakarat3 10:61 ile 7 kelime, xref de 10:61",
         dogru="nakarat3'ün 7 kelimelik kalıbı SÛRE İÇİ: yalnız 34:3 ve 34:22. 10:61 ile bağ yalnız xref (ekber · kitâb · mübîn) ve عزب kökü; 10:61'de gök/yer sırası ters, kalıp yok.",
         aday=1003, blok='21-30'),
}
