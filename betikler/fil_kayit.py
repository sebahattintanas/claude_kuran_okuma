# -*- coding: utf-8 -*-
"""fil_kayit.py — sûre 105 (Fil) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 105

CIPA = {
 # blok 1-5
 1: dict(kademe=None, olgu=False, cipa=False, not_="'e-lem tera keyfe fe'ale rabbuke bi-ashâbi'l-fîl' — tarihsel olay, topluluk hayvan adıyla anılıyor (olgu=False; 89:6 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'e-lem yec'al keydehum fî tadlîl' — tuzak, tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ve ersele 'aleyhim tayran ebâbîl' — anlatı içi olay, kuşların gönderilmesi; olgu tarifi değil (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'termîhim bi-hicâratin min siccîl' — anlatı içi olay, taş atma (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'fe-ce'alehum ke-'asfin me'kûl' — teşbih, olgu benzetme aracı (olgu=False; 77:32 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 5): [
  "esmâ: e_oto 0 token; KARAR değişmedi (728); lafız yok, Rab 1 (105:1, 2MS iyelikli); mühür yok",
  "kök tablosu: blokta 1 yeni kök (فيل; 1538); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı; iskelet çakışması yok",
  "gloss (1021): kök سجل 'tomar, dürülmüş sayfa' (105:4 'siccîl'), kök عصف 'fırtına, savurma' (105:5 ''asf' ekin yaprağı) — buradaki anlamları vermiyor",
  "yıldız: 105:1 ★★★ (hapaks — bu blokta eklenen kök فيل, z=3,28; rab 2,72 eşik altında) — formül davranışı; diğer 4 ayet yıldızsız",
  "biçim (924): ayet 1 harf 43 → harf3 24 (besmele ailesi); INTG + NEG 105:1-2 ölçümde var; 105:5 'ke-' teşbihi biçim alanında görünmüyor",
  "fâsıla: ölçüm ل 5 (105:1-5) — geçiş yok",
  "iltifât: ölçüm 0; sahset 105:1 ['2', '3'], 105:2-5 ['3'] — 2MS'nin çıkışı kısmi örtüşme",
  "gönderge: 105:2-5 3MS öznesi metinde yeni ad almıyor (105:1 Rab sürüyor, okuma); 105:4 3FS fiil 'tayr'a uyuyor",
  "adsız gönderge (1017): 105:1 2MS hitap adsız; konuşan / anlatıcı adsız; fil sahipleri tamlamayla anılıyor, kişi adı yok",
  "çıpa: L0 / L1 / L2 / L4 yok; olgu=False 5 (tarihsel olay, tutum, anlatı içi olay, teşbih); tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 104:9 / 105:1 sûre sınırı — fiilsiz öbekle kapanış / 'e-lem tera' sorusuyla açılış; fâsıla ة → ل; 104 lafız 1 Rab 0, 105 lafız 0 Rab 1",
  "aday 1039: ayet içi 0; blok içi 0",
  "aday 1041: kayıt yok — Rab tek geçiş, lafız yok",
  "korpusta 1 (kayıt): lemma 'tadlîl', 'ebâbîl', 'me'kûl'; kök فيل; kalıp 'ashâbi'l-fîl', 'e-lem yec'al', 'tayran ebâbîl'; korpusun iki geçişi, ikisi de basıldı: kalıp 'e-lem tera keyfe fe'ale rabbuke' (89:6, 105:1); lemma 'siccîl' korpusun tamamı 3 ayet (15:74 basıldı, okunmuş 1 ayet daha, 105:4)",
  "bağ: kalıp / lemma eşleri okumayla (89:6, 77:32, 15:74, 55:12, 21:58); hepsi AR + meal ile emsal listesinde basıldı; 104:9 bu oturumda daha önce basılmıştı, yeniden basılmadı",
  "◈K / ◈B: ◈K beş ayette '—'; ◈B dolu 105:3 (طير); 105:1 'fîl' kök فيل tetik listesinde değil — gözlem ◇'de; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 5 ayet; oturum_xy 18 sayım, 0 uyuşmaz",
  "süreç: sûre 105 dosyaları humeze_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_105.py, oturum dışı; ad 'fil'; ilerleme yüzdesi sabiti maskelendi; sûre 96 şablonuyla normalleştirilmiş aile karşılaştırması temiz — normalleştiricide 'fil' adı 'profil' içinde de eşleşti, harf sınırlı yeniden karşılaştırmada dosyalar temiz); sûre 5 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {}
