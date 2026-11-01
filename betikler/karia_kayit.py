# -*- coding: utf-8 -*-
"""karia_kayit.py — sûre 101 (Karia) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 101

CIPA = {
 # blok 1-11
 1: dict(kademe=None, olgu=False, cipa=False, not_="'el-qâri'ah' — âhiret, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'me'l-qâri'ah' — soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ edrâke me'l-qâri'ah' — soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'yekûnu'n-nâsu ke'l-ferâşi'l-mebsûs' — insanların hâli, teşbih; 'ke'l-ferâş' teşbih aracı (olgu=False; 70:8 kaydı emsali — orada özne gök, L1); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe='L1', olgu=True, cipa=False, not_="'ve tekûnu'l-cibâlu ke'l-'ihni'l-menfûş' — dağlar + hâl; mekanizma / ölçü yok — L1 (70:9 kaydı emsali); 'ke'l-'ihn' teşbih aracı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'fe-emmâ men saqulet mevâzînuh' — tartı, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'fe-huve fî 'îşetin râdiyeh' — âhiret (olgu=False; 69:21 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'ve emmâ men xaffet mevâzînuh' — tartı, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 9: dict(kademe=None, olgu=False, cipa=False, not_="'fe-ummuhû hâviyeh' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ edrâke mâ hiyeh' — soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 11: dict(kademe=None, olgu=False, cipa=False, not_="'nârun hâmiyeh' — âhiret, ateş (olgu=False; 88:4 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 11): [
  "esmâ: e_oto 0 token; KARAR değişmedi (728); lafız yok, Rab yok — lafızsız ve Rabsız sûre (77, 80, 83, 86, 90 gibi); mühür yok",
  "kök tablosu: blokta yeni kök yok (1537); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı",
  "gloss (1021): kök فرش 'yayma; döşek' (101:4 'ferâş' pervane), kök نفش 'geceleyin ekine yayılma' (101:5 'menfûş' atılmış), kök أمم 'ümmet, topluluk' (101:9 'umm' ana) — buradaki anlamları vermiyor",
  "yıldız: sûrenin hiçbir ayetinde yıldız yok (yıldız 0: 11) — lafız / Rab / edilgen / hapaks yok",
  "fâsıla (924): metin ة 6 (101:1-3, 7, 9, 11), ث 1 (101:4), ش 1 (101:5), ه 3 (101:6, 8 zamir; 101:10 'hiyeh'); ölçüm H 9, ث 1, ش 1 — ة → ث → ش → ه geçişleri kafiye kırığı işaretlenmedi",
  "biçim (924): ayet 1 harf 26 → harf3 7 (besmele ailesi; tek kelimelik ayet); 101:4-5 teşbih 'ke' biçim alanında yok; 101:7 ve 101:9 şart cevabı, 101:11 soru cevabı biçim alanında görünmüyor; 101:6, 101:8 AMMA ölçümde var",
  "morph (924): 101:10 'hiyeh' sonundaki 'h'ye lemma verilmiyor; lemma dizisinde boş öğe",
  "iltifât: ölçüm 0; 101:3 ve 101:10 2MS hitap — {—} → {2, 3} ve {3} → {2, 3} kısmi örtüşme",
  "adsız gönderge (1017): hitap 2MS (101:3, 101:10), 'men' (101:6, 101:8) — adlandırılmadı",
  "çıpa: L1 1 (101:5 dağlar — 70:9 kaydı emsali); olgu=False 10 (101:4 insanların hâli, teşbih — 70:8 ile özne farkı); tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 100:11 / 101:1 sûre sınırı — Rab + tekitli haberle kapanış / tek kelimeyle açılış; fâsıla ر → ة; sûre 100 Rab 2, sûre 101 lafızsız ve Rabsız",
  "aday 1039: ayet içi 0; blok içi 1 (101:6 / 101:8 'saqulet' / 'xaffet' — ağır / hafif)",
  "aday 1041: kayıt yok — lafız / Rab yok",
  "esit2 TAM (kayıt): 101:7 = 69:21 — aynı ayet iki ayrı 'fe-emmâ men' şartına cevap (69:19 kitabı sağdan verilen / 101:6 tartısı ağır gelen); ölçüm eşi iki kez yazıyor (araç tekrarı)",
  "korpusun iki geçişi, ikisi de basıldı: harekesiz 've tekûnu'l-cibâlu ke'l-'ihn' (70:9, 101:5); lemma ''îşe' (69:21, 101:7); lemma 'hâmiye' (88:4, 101:11); korpusun tamamı sûre içi: harekesiz 'me'l-qâri'a' (101:2, 101:3); korpusta 1: 'ferâş', 'mebsûs', 'menfûş', 'hâviye'",
  "bağ: kalıp / lemma eşleri okumayla (100:11, 69:1, 69:2, 69:3, 69:4, 13:31, 86:2, 97:2, 70:8, 70:9, 23:102, 23:103, 69:19, 69:21, 88:4); 69:3, 86:2, 97:2, 100:11 bu oturumda daha önce basılmıştı, yeniden basılmadı; diğerleri AR + meal ile basıldı",
  "◈K / ◈B: ◈K dolu 101:4 (يوم), 101:5 (جبل); ◈B dolu 101:4 (أنس); tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 11 ayet; oturum_xy 25 sayım, 0 uyuşmaz",
  "süreç: sûre 101 dosyaları adiyat_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_101.py, oturum dışı; ad 'karia'; set değişkeni ASCII 'KARIA'; kok_ekle ISTEK boşaltıldı); sûre 11 ayet — tek blok, ara zip yok",
  "süreç (kayıttan sonra, ek satır): iskele_101 genel numara değişimi (100 → 101) yüzde formülündeki sabiti de değiştirdi — uret_blok_101 ve karia_kapanis'te round(101 * okunan / len(D)); ilk blok koşusu ilerleme yüzdesini %80,3 yazdı (doğrusu %79,5). Sabit 100'e döndürüldü, blok betiği yalnız ilerleme / bilanço için yeniden koşuldu, ayet kayıtları önce / sonra karşılaştırmasıyla aynı. Assert eski numaranın KALMADIĞINI denetliyordu; sayısal sabitin numarayla çakışmasını denetlemiyordu. Sûre 97-100 iskeleleri sûre 96 şablonuyla normalleştirilmiş karşılaştırmada temiz",
 ],
}

DUZELTME = {}
