# -*- coding: utf-8 -*-
"""sad_kayit.py — sûre 38 (Sâd) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 38

CIPA = {
 # blok 1-10
 10: dict(kademe='L0', olgu=True, cipa=False, not_="gökler, yer, ikisinin arası adlanıyor; tek ilişki mülk (sahiplik sorusu) ve 'esbâb'a yükselme emri (meydan okuma); süreç/ölçü yok (37:5 emsali)"),
 # blok 11-20
 18: dict(kademe='L1', olgu=True, cipa=False, not_="dağlar ve günün iki ucu (akşam, doğuş) adlanıyor + davranış/yeti (tesbih); süreç/ölçü yok — blok 21-30'da L0 → L1 düzeltildi (27:16-18 emsali: canlı/nesne + yeti/davranış = L1)"),
 19: dict(kademe='L1', olgu=True, cipa=False, not_="kuşlar adlanıyor + hâl/davranış (toplanmış, 'evvâb'); süreç/ölçü yok — blok 21-30'da L0 → L1 düzeltildi (27:17-18 emsali)"),
 # blok 21-30
 23: dict(kademe='L1', olgu=True, cipa=False, not_="dişi koyunlar adlanıyor + sayı (99/1) ve sahiplik (36:71 en'âm emsali); misal anlatı içinde; tarayıcı v4 adayı (F_ölçü), çıpa değil"),
 24: dict(kademe='L1', olgu=True, cipa=False, not_="koyunlar + sahiplik/katma; süreç/ölçü yok; tarayıcı v4 adayı (F_ölçü — kesîr/qalîl), çıpa değil"),
 27: dict(kademe='L1', olgu=True, cipa=False, not_="gök, yer, ikisinin arası adlanıyor + nitelik: yaratılmışlık ve amaç ('bâtıl değil'); nedensellik/ölçü yok"),
 # blok 31-40
 31: dict(kademe='L1', olgu=True, cipa=False, not_="atlar adlanıyor + nitelik (sâfinât, ciyâd) ve vakit; süreç/ölçü yok"),
 33: dict(kademe='L1', olgu=True, cipa=False, not_="at organları (bacak, boyun) + dokunma eylemi; süreç/ölçü yok"),
 36: dict(kademe='L1', olgu=True, cipa=False, not_="rüzgâr + nitelik (yumuşak), yön ('haysu esâb'), emre bağlılık; mekanizma/ölçü yok (21:81 'âsıfa' emsali)"),
 # blok 41-50
 42: dict(kademe='L1', olgu=True, cipa=False, not_="su adlanıyor + nitelik (serin) ve işlev (yıkanma, içme); ayakla vurmayla ortaya çıkış — süreç/ölçü yok"),
 # blok 61-70
 66: dict(kademe='L0', olgu=True, cipa=False, not_="gökler, yer, ikisinin arası adlanıyor; ilişki rablık; süreç/ölçü yok (37:5, 38:10 emsali)"),
 # blok 71-80
 71: dict(kademe='L1', olgu=True, cipa=False, not_="beşer + madde (tîn); madde ve sonuç, ara aşama yok (36:77 emsali)"),
 72: dict(kademe='L1', olgu=True, cipa=False, not_="iki aşama sırayla adlanıyor (tesviye → nefh); mekanizma/ölçü yok"),
 76: dict(kademe='L1', olgu=True, cipa=False, not_="iki madde (ateş, çamur) + karşılaştırma iddiası (İblîs'in sözü); süreç/ölçü yok"),
}

ARIZA = {
 (1, 10): [
  "iltifât: 38:7 (alıntı içi 1P) — 1017 ailesi; 38:8 ayet içinde alıntı 1P (onlar) → anlatıcı 1S ('zikrî', 'azâbi') — alan ayetler arası, 0 yazıyor (kayıt)",
  "gloss: خلق 'yaratma' — 38:7 'ihtilâq' (VIII. bab, uydurma) anlamı yok (987/1015 ailesi, kayıt)",
  "esmâ: 38:7 âhir 'degil'; 38:9 azîz + vehhâb 'ilahi' — §4.3 mühür ÇİFT, geçerli",
  "bilanço: ★★★ 38:3 hapaks (لوت, نوص; z=6,79; 983); ★★ 38:8 pas (z=2,52; e-unzile); ★★ 38:9 rab (z=2,72)",
 ],
 (11, 20): [
  "kök alanı: 38:12 'Âd' (özel ad) عود 'geri dönme' olarak sayılıyor — özel ad kök alanına giriyor (924)",
  "aktör/kök: 38:13 'Eyke' (LEM eyke) ne ROOT ne PN etiketi taşıyor — kök listesinde ve aktör alanında yok (924)",
  "gloss: فوق 'üst, üstünde' — 38:15 'fevâq' (duraklama, iki sağım arası) anlamı yok (987/1015 ailesi, kayıt)",
  "1S: 38:14 'ıqâbi' iyelik yâsı yazıda düşmüş, morfoloji 1S sayıyor (38:8 'azâbi' emsali); iltifât alanı 0",
  "edilgen: 38:19 'mahşûra' ism-i meful — fiil olmadığı için edilgen alanına girmiyor (kayıt)",
  "çıpa: 38:18 dağlar + akşam/doğuş, 38:19 kuşlar — L0 (olgu evet, çıpa hayır)",
 ],
 (21, 30): [
  "tetik: ◈B listesi نعج (dişi koyun, 38:23-24 — kök korpusta yalnız bu iki ayet) içermiyor; ◈B '—' yazıldı (S1: tetik değişikliği yalnız ileriye; kayıt)",
  "gloss: فجر 'fışkırtma; fecir' — 38:28 'fuccâr' (günahkârlar) anlamı yok; دبر 'arka' — 38:29 'yeddebberû' (tedebbür) anlamı yok (987/1015 ailesi)",
  "şahıs: 38:24 'fetennâhu' (1P) Dâvûd'un zannı içinde — iltifât alanı 0 (kayıt)",
  "çıpa DÜZELTME: 38:18 ve 38:19 blok 11-20'de L0 yazılmıştı; 14_cipa_tanimi kademe tanımı (L1 = adlandırma + alan/yeti/nitelik; 27:16-18 emsali) ile L1. Mercek metni korunur, düzeltme DUZELTME alanında. 38:27 L1",
  "tarayıcı v4: 38:23 ve 38:24 (F_ölçü) aday — L1 (koyun + sayı/sahiplik), çıpa değil (948)",
  "bilanço: ★★ 38:24 n (z=2,08, 32 kelime); ★ 38:26 n (z=1,87); ★ 38:22 kafiye kırığı (ط); lafız sûrede ilk 38:26 (2 token)",
 ],
 (31, 40): [
  "gloss: سوق 'sürme; çarşı' — 38:33 'sûq' (bacaklar, sâq çoğulu) anlamı yok (987/1015 ailesi)",
  "tetik: ◈B listesi جسد (ceset, 38:34) içermiyor; ◈B '—' (S1; kayıt)",
  "belirsizlik: 38:32 'an zikri rabbî' iki okuma (ötürü / yerine); 'tevârat' öznesi adlanmıyor (atlar / güneş) — KAPATILAMAZ; çıpa değerlendirilmedi",
  "esmâ: 38:35 ehad 'degil', vehhâb 'ilahi' — §4.3 mühür geçerli",
  "bilanço: ★★★ 38:31 pas (z=5,38; hapaks صفن z=3,28 de eşik üstü; kafiye kırığı); ★★★ 38:36 hapaks رخو (z=3,28); ★ 38:32 rab (z=1,62); ★ 38:33 kafiye kırığı",
 ],
 (41, 50): [
  "aktör/kök: 38:48 'ze'l-kifl' ذو + كفل olarak ayrışmış — aktör alanında yok, كفل 'üstlenme' ipliğine (38:23 ekfilnîhâ) katılıyor (924)",
  "gloss: رجل 'adam; yaya' — 38:42 'ricl' (ayak) anlamı yok (987/1015); ◈B listesinde رجل yok → ◈B '—' (S1; kayıt)",
  "tetik: 38:45 'eydî' (güç, mecaz) ◈B'yi organ kelimesiyle tetikliyor — mercek satırında nitelik olarak yazıldı (kayıt)",
  "bilanço: ★ 38:41 rab (z=1,62); iltifât 43, 48, 50 (anlatı ↔ emir geçişleri)",
 ],
 (51, 60): [
  "gloss: ترب 'toprak' — 38:52 'etrâb' (yaşıtlar) anlamı yok (987/1015)",
  "tetik: 38:58 'ezvâc' (çeşitler) ◈B'yi زوج ile tetikliyor — canlı/eş unsuru yok, mercek satırında kayıt",
  "belirsizlik: 38:59 konuşan(lar) adlanmıyor; 2MP hitap + 3MP söz — iki ses mi tek ses mi metin ayırmıyor (KAPATILAMAZ)",
  "çıpa: blokta doğal olgu yok (cennet/cehennem tasviri) — değerlendirilmedi",
 ],
 (61, 70): [
  "sayı işareti: 38:62 'nauddu' (saymak = kabul etmek) araçta sayı işareti olarak işaretleniyor (kayıt)",
  "gloss: سخر 'boyun eğdirme' — 38:63 'sihriyy' (alay) anlamı yok (987/1015)",
  "esmâ: 38:65 qahhâr 'ilahi'; 38:66 azîz + ğaffâr 'ilahi' (ÇİFT); 38:70 mubîn 'degil' (uyarıcının sıfatı)",
  "belirsizlik: 38:67 'huve' (büyük haber) göndergesi adlanmıyor (KAPATILAMAZ)",
  "esmâ alanları: 38:35 ve 38:65'te ölçüm satırı 'MÜHÜRSÜZ', bilanço §4.3 mühür geçerli — iki alan farklı ölçüt (kayıt; araç dondurulmuş)",
  "kafiye: 38:66 ر → 38:67 م (R → N sınıfı) geçişi kafiye kırığı alanında işaretlenmiyor (kayıt)",
  "bilanço: ★ 38:61 rab (z=1,62); ★★ 38:66 rab (z=2,72); ★★★ 38:70 pas (z=5,38); lafız sûrede ikinci 38:65",
 ],
 (71, 80): [
  "kök/gloss: 'melâike' (38:71, 38:73) ملك (mülk; melik) ipliğine sayılıyor — melek anlamı gloss'ta yok (987/1015); iplik mülk ve melek geçişlerini karıştırıyor",
  "esmâ: 38:71 hâliq 'ilahi' (inne'nin haberi, 1S Rab; 34:11 emsali)",
  "bilanço: ★★ 38:71 rab (z=2,05); ★★★ 38:79 rab (z=3,23; pas 1,57 de eşik üstü); §4.3 mühür 38:71 geçerli (ölçüm satırı MÜHÜRSÜZ — 38:35/65 emsali)",
  "esit2: 38:72, 73, 77, 79, 80 → sûre 15 (29, 30, 34, 36, 37) TAM; 38:78 → 15:35 BENZER; 74-76 sûre 15'ten ayrılıp 2:34 / 7:12'ye yaslanıyor (okumada görüldü)",
  "belirsizlik: 38:75, 77, 80 'qâle' öznesi adlanmıyor; 38:77 'minhâ' göndergesi adlanmıyor (KAPATILAMAZ)",
 ],
 (81, 88): [
  "esit2: 38:81 → 15:38 ve 38:83 → 15:40 TAM; 38:87 → 81:27 TAM, 68:52 BENZER (henüz okunmadı)",
  "belirsizlik: 38:84 'qâle' öznesi; 38:87 'huve' göndergesi adlanmıyor (KAPATILAMAZ)",
  "çıpa: blokta doğal olgu yok — değerlendirilmedi",
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_38.py uygular)
DUZELTME = {
 18: dict(alan='mercek', eski="🜁 L0 — dağlar ve günün iki ucu adlanıyor; ilişki teshir + tesbih",
         dogru="🜁 L1 — dağlar ve günün iki ucu adlanıyor + davranış/yeti (tesbih); kademe tanımına göre (14_cipa_tanimi: adlandırma + alan/yeti/nitelik = L1; 27:16-18 emsali) L1. Olgu evet, çıpa hayır (değişmedi).",
         aday=None, blok='11-20'),
 19: dict(alan='mercek', eski="🜁 L0 — kuşlar adlanıyor, toplanmış hâlde",
         dogru="🜁 L1 — kuşlar adlanıyor + hâl/davranış (toplanmış, 'evvâb'); kademe tanımına göre L1 (27:17-18 emsali). Olgu evet, çıpa hayır (değişmedi).",
         aday=None, blok='11-20'),
}
