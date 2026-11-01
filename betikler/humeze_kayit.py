# -*- coding: utf-8 -*-
"""humeze_kayit.py — sûre 104 (Humeze) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 104

CIPA = {
 # blok 1-9
 1: dict(kademe=None, olgu=False, cipa=False, not_="'veylun li-kulli humezetin lumeze' — kınama, tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'ellezî cema'a mâlen ve 'addedeh' — mal toplama, tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'yahsebu enne mâlehû axledeh' — sanı, tutum (olgu=False; 90:5 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'kellâ le-yunbezenne fi'l-hutame' — âhiret, atılma (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ edrâke me'l-hutame' — soru (olgu=False; 101:10 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'nâru'llâhi'l-mûqade' — âhiret, ateş (olgu=False; 101:11 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'elletî tettali'u 'ale'l-ef'ide' — âhiret ateşi, gönüller (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'innehâ 'aleyhim mu'sade' — âhiret, azap (olgu=False; 90:20 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 9: dict(kademe=None, olgu=False, cipa=False, not_="'fî 'amedin mumeddede' — âhiret, direkler (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 9): [
  "esmâ: e_oto 0 token; KARAR değişmedi (728); lafız 1 (104:6 'nâru'llâh', izâfet), Rab yok; mühür yok",
  "kök tablosu: blokta yeni kök yok (1537); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı",
  "gloss (1021): kök طلع 'doğma (güneş)' — 104:7 'tettali'u 'ale'l-ef'ide' (üzerine çıkma, ulaşma) anlamını vermiyor",
  "yıldız: 104:4 ★★★ (pas, edilgen 1/1, z=5,38), 104:6 ★★★ (allah, z=6,14 — kısa ayette tek lafız); diğer 7 ayet yıldızsız — formül davranışı",
  "sayı işareti (924): 104:2 ''addede' — sayı adı değil, sayma / hazırlama fiili; işaret kök kaynaklı",
  "biçim (924): ayet 1 harf 35 → harf3 14 (besmele ailesi); KELLA + EMPH 2 + edilgen 104:4, INTG 2 104:5 ölçümde var",
  "fâsıla (924): ölçüm H 9 — metinde 104:1 ve 104:4-9 ة, 104:2-3 ه (zamir); ة / ه geçişi tek H sınıfında görünmüyor",
  "iltifât: ölçüm 0; sahset 104:2-4 ['3'], 104:5 ['2', '3'] (2MS'nin girişi, kısmi örtüşme), 104:7-8 ['3'], 104:1, 104:6, 104:9 — (şahıs işareti yok)",
  "gönderge (924): 3MS ('ellezî', 104:2-4) → 3MP ('aleyhim', 104:8) ölçümde '3' / '3', görünmüyor; 3MP göndergesi metinde adlı değil; 104:9 öbeğinin bağlandığı ad KAPATILAMAZ",
  "adsız gönderge (1017): 104:1-4 nitelenen kişi adsız; 104:5 2MS hitap adsız; konuşan adsız; 104:4 atan yazılmamış (edilgen)",
  "çıpa: L0 / L1 / L2 / L4 yok; olgu=False 9 (kınama, tutum, sanı, âhiret); tarayıcı v4 blokta aday vermedi; 104:7 organ adı 'ef'ide' âhiret ateşi bağlamında",
  "aday 1040 (kayıt): 103:3 / 104:1 sûre sınırı — istisna (iman edenler) ile kapanış / 'veyl' ile açılış; fâsıla ر → ة; 103 lafızsız ve Rabsız, 104 lafız 1, Rab 0",
  "aday 1039: ayet içi 0; blok içi 0",
  "aday 1041: kayıt yok — lafız tek geçiş (104:6), Rab yok; okuma bağı kök وقد 85:5 'veqûd' / 104:6 'mûqade'",
  "korpusta 1 (kayıt): lemma 'humeze', 'lumeze', ''addede', 'mûqade', 'mumeddede'; kalıp 'ellezî cema'a mâlen', 'nâru'llâh'; korpusun tamamı sûre içi: lemma 'hutame' (104:4, 104:5); korpusun iki geçişi, ikisi de basıldı: kalıp 'veylun li-kulli' (45:7, 104:1), lemma 'mu'sade' (90:20, 104:8)",
  "bağ: kalıp / lemma eşleri okumayla (45:7, 68:11, 23:97, 90:5, 90:7, 68:49, 69:3, 101:10, 101:11, 85:5, 90:20, 31:10); hepsi AR + meal ile emsal listesinde basıldı; 103:3 bu oturumda daha önce basılmıştı, yeniden basılmadı",
  "◈K / ◈B: ikisi de dokuz ayette '—' (104:7 'ef'ide' kök فأد tetik listesinde değil — gözlem ◇'de); tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 9 ayet; oturum_xy 21 sayım, 0 uyuşmaz",
  "süreç: sûre 104 dosyaları asr_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_104.py, oturum dışı; ad 'humeze'; ilerleme yüzdesi sabiti maskelendi; sûre 96 şablonuyla normalleştirilmiş aile karşılaştırması temiz); sûre 9 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {}
