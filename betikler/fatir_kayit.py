# -*- coding: utf-8 -*-
"""fatir_kayit.py — sûre 35 (Fâtır) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır.
"""
S = 35

CIPA = {
 # blok 1-10
 1:  dict(kademe='L0', olgu=True,  cipa=False, not_="gökler ve yer adlandırılıyor; sayı dizisi (ikişer, üçer, dörder) meleklerin kanatlarına ait, doğal olgu değil; tarayıcı v4 adayı (F_ölçü), çıpa değil"),
 3:  dict(kademe='L0', olgu=True,  cipa=False, not_='gökten ve yerden rızık adlandırılıyor, süreç yok; tarayıcı v4 adayı (D_yeti), çıpa değil'),
 9:  dict(kademe='L2', olgu=True,  cipa=False, not_="rüzgâr → bulutun kabarması → ölü beldeye sürülme → yerin dirilmesi: nedensel zincir, ara durum yalnız bulut, yağmur ve çıkış yeri adlanmıyor (30:48 L4 / 30:24 L2 arası)"),
 # blok 11-20
 11: dict(kademe='L1', olgu=True,  cipa=False, not_='toprak → nutfe → çiftler: madde ve aşama adlandırma, ara durum yok, nedensellik yok (32:7 emsali L1)'),
 12: dict(kademe='L1', olgu=True,  cipa=False, not_='iki su sınıfı nitelikleriyle (tatlı/tuzlu) + ortak ürünler + suyu yaran gemiler; ölçütsüz ikili sınıflama, mekanizma yok (27:61 emsali L1; L4 sınıflama koluna sınırda); tarayıcı v4 adayı, çıpa değil'),
 13: dict(kademe='L1', olgu=True,  cipa=False, not_='gece-gündüz karşılıklı geçiş, güneş ve ay belirli süreye akar; 31:29 ile aynı terkip ve aynı kademe (L1); tarayıcı vermedi'),
 16: dict(kademe=None, olgu=False, cipa=False, not_='tarayıcı v4 adayı (şart): giderme / yeni halk getirme — doğal olgu yok, merdiven uygulanmadı'),
 # blok 21-30
 25: dict(kademe=None, olgu=False, cipa=False, not_='tarayıcı v4 adayı (şart): elçiler, sahifeler, kitap — doğal olgu yok, merdiven uygulanmadı'),
 27: dict(kademe='L2', olgu=True,  cipa=False, not_="gökten su → 'onunla' renkleri farklı ürünler (nedensellik, 27:60 emsali L2); dağ çizgileri beyaz/kırmızı/siyah: sınıflar ADLI ama üye eşlemesi yok (29:40 ölçütü) → sınıflama kolunda L4 değil (aday 1014); tarayıcı v4 adayı (G_bakış), çıpa değil"),
 28: dict(kademe='L1', olgu=True,  cipa=False, not_='insan, yürüyen canlı, davar: renk çeşitliliğinin varlığı, sınıf adı yok (30:22 emsali L1)'),
 # blok 31-40
 32: dict(kademe=None, olgu=False, cipa=False, not_="üç adlı sınıf + 'minhum' ×3 ile bölüntü (29:40 eşleme ölçütü dolu) ama insan sınıfları, doğal olgu değil (27:17 emsali); merdiven uygulanmadı"),
 38: dict(kademe='L0', olgu=True,  cipa=False, not_='göklerin ve yerin gaybı — gök ve yer adlanıyor, süreç yok (35:3 emsali)'),
 39: dict(kademe='L0', olgu=True,  cipa=False, not_='yeryüzünde halifeler — yer adlanıyor'),
 40: dict(kademe='L0', olgu=True,  cipa=False, not_="gök ve yer adlanıyor (ortakların yaratması sorgulanıyor); tarayıcı v4 adayı (G_bakış: 'gördünüz mü'), çıpa değil"),
 # blok 41-45
 41: dict(kademe='L2', olgu=True,  cipa=False, not_="gökler ve yer kaymasın diye tutulur; 'O'ndan sonra kimse tutamaz' — L2 yeti sınırı kolu (27:60 emsali); tarayıcı v4 adayı (şart, D_yeti), çıpa değil"),
 43: dict(kademe='L0', olgu=True,  cipa=False, not_="yeryüzü adlanıyor (büyüklenme yeri); sünnetullah olgu değil; tarayıcı v4 adayı (G_bakış), çıpa değil"),
 44: dict(kademe='L0', olgu=True,  cipa=False, not_='gök ve yer adlanıyor; tarayıcı v4 adayı (ta\'lîl), çıpa değil'),
 45: dict(kademe='L0', olgu=True,  cipa=False, not_='yeryüzünde yürüyen canlı adlanıyor (karşı-olgusal); tarayıcı v4 adayı (şart), çıpa değil'),
}

ARIZA = {
 (1, 10): [
  "esmâ: §4.3 YANLIŞ MÜHÜR bir kez — 35:7 kebîr (ödülün sıfatı); 35:3 hâlık olumsuzlanan 'Allah'tan başka' konumunda (değil, mühür değil)",
  "esmâ alanı: ölçüm satırı 35:1 qadîr ve 35:8 alîm için 'MÜHÜRSÜZ' diyor, §4.3 kaydı mühür EVET — eski token düzeyi esma_k (#9/#12, aday 908/930), §4.3 esas",
  "iltifât: 35:9 Allah (3MS) → biz (1P) geçişi, ilt=0 — lafız→zamir geçişi tagger açığı (aday 517 ailesi)",
  "bilanço: 35:8 ★ kafiye kırığından (diğer bileşenler 1,5 altı); kaynak etiketi yanlış basılırsa aday 1001",
  "say: 35:1 mesnâ, sülâs, rubâ' DOĞRU POZİTİF ×3 (981 ailesinin karşı vakası)",
  "gloss: ملك 'mülk; melik' — 35:1 melâike; melek anlamı gloss'ta yok (aday 1000 ailesi)",
  "tarayıcı v4: 35:1 (F_ölçü) ve 35:3 (D_yeti) aday, çıpa değil (948 birikimi)",
 ],
 (11, 20): [
  "esmâ: §4.3 YANLIŞ MÜHÜR üç kez — 35:17 azîz (işin sıfatı: 'güç değil'), 35:19 basîr (insan), 35:20 nûr (ışık); geçerli: 35:14 habîr, 35:15 ganî-hamîd (çift)",
  "esmâ SINIR VAKASI: 35:14 'mislu habîr' — tamlama içinde ad olarak esmâ, göndergesi Allah, 'ilahi' verildi (aday 999, ikinci vaka; ilki 34:6)",
  "say: 35:11 zevc (çiftler) sayı işareti — cins adı, sayı değil (981 yanlış pozitif)",
  "gloss: عذب 'azap' — 35:12 azb (tatlı su) anlamı yok; ظلم 'zulüm' — 35:20 zulumât (karanlık, 23 ayet) anlamı yok (aday 1000 ailesi)",
  "yıldız: ★★★ üç ayette (35:13 hapaks, 35:15 ve 35:17 allah) — 35:15 (10 kelime) ve 35:17 (5 kelime) kısa ayette tek lafız/iki lafız z'yi uca taşıyor (983)",
  "tarayıcı v4: 35:12 (ta'lîl, recâ) ve 35:16 (şart) aday, çıpa değil; 35:13 vermedi, emsali 31:29'da bakış işaretiyle vermişti (948 birikimi)",
 ],
 (21, 30): [
  "gloss: ظلل 'sürüp gitme' — baskın lemma zıll 'gölge' (14) gloss'ta YOK, 35:21'de okunan anlam eksik olan; جدد 'yenilik' — 35:27 cudad (çizgi, yol) yok (aday 1015)",
  "iltifât: 35:27 Allah (3MS) → biz (1P), ilt=0 — 517 ailesi, sûrede ikinci (35:9)",
  "şahıs: 35:24 1P → 35:26 1S (birinci şahsın sayısı değişiyor), ilt=0 — alan bu türü tanımlamıyor, arıza sayılmadı, kayıt",
  "bilanço: 35:27 ★ kafiye kırığından (n 1,02 · allah 0,38) — etiket yanlış basılırsa aday 1001",
  "esmâ: 35:22 hayy (diriler) ve 35:28 alîm ('ulemâ) değil; mühürler 35:28 azîz-ğafûr ve 35:30 ğafûr-şekûr geçerli; yanlış mühür yok",
  "çıpa tanımı: L4 sınıflama kolunun ölçütü iki emsalde farklı ifade edilmiş (30:22 'sınıf adlandırma' / 29:40 'gruplara eşleme'); 35:27'de eşleme ölçütü uygulandı (aday 1014); 35:12 gerekçesi düzeltildi",
  "tarayıcı v4: 35:25 (şart) ve 35:27 (G_bakış) aday, çıpa değil (948 birikimi)",
 ],
 (31, 40): [
  "esmâ: §4.3 YANLIŞ MÜHÜR iki kez — 35:32 kebîr (lütfun sıfatı; 35:7 'ecrun kebîr' ile aynı kalıp), 35:37 nasîr (olumsuzlanan, insan göndergeli); geçerli: 31, 34, 38",
  "esmâ alanı: 35:38 âlim ve alîm için ölçüm satırı MÜHÜRSÜZ, §4.3 mühür EVET (#9/#12)",
  "iltifât: 35:32 biz (1P) → 'Allah'ın izniyle' (lafız), ilt=0 — 517 ailesi, ters yön",
  "şahıs: 35:37 sahset 1P 7 — konuşan 'biz' hem cehennem ehli (alıntı) hem Allah; şahıs sayımı konuşmacıyı ayırmıyor (aday 1017)",
  "gloss: ذهب 'gitme, götürme' — 35:33 zeheb (altın, lemma 8) yok (aday 1015 eki)",
  "bilanço: 35:35 ★ kafiye kırığından (n 0,17) — etiket yanlış basılırsa aday 1001",
  "tarayıcı v4: 35:40 (G_bakış) aday, çıpa değil (948 birikimi)",
 ],
 (41, 45): [
  "say: 35:41 ehad ('kimse', olumsuz bağlam) sayı işareti — yanlış pozitif (981); 35:42 ihdâ ('herhangi biri') — sınırda",
  "esmâ: 35:41 ehad ve 35:43 evvel e_oto'da, e_el değil; mühürler 41, 44, 45 geçerli; yanlış mühür yok",
  "kafiye: 35:39-45 yedi ayet kesintisiz ا sınıfı fâsıla, 35:1-38'de hiç yok — kafiye_kirik alanı bu geçişi işaretlemiyor (kırık tanımı komşu-göreli; arıza değil, kayıt)",
  "tarayıcı v4: 35:41, 35:43, 35:44, 35:45 dördü de aday, hiçbiri çıpa değil (948 birikimi)",
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_35.py uygular)
DUZELTME = {
 12: dict(alan='mercek', eski="sınıflama ikili ve ölçütsüz — 27:61 emsali (L1)",
         dogru="Sınıflama ikili ve ÖLÇÜTLÜ (tat: tatlı/tuzlu), sınıflar adlı ve her birine nitelik veriliyor; 27:61'de sınıf yok, emsal zayıftı. Kademe L1 değişmiyor: sınıflara üye eşlenmiyor (29:40 ölçütü), 30:22 (L1) ile 29:40 (L4) arasında.",
         aday=1014, blok='21-30'),
}
