# -*- coding: utf-8 -*-
"""kadr_kayit.py — sûre 97 (Kadr) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 97

CIPA = {
 # blok 1-5
 1: dict(kademe=None, olgu=False, cipa=False, not_="'innâ enzelnâhu fî leyleti'l-qadr' — indirme zamanı olarak adlı gece; doğal olgu anlatımı değil (olgu=False; 44:3 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ edrâke mâ leyletu'l-qadr' — soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'leyletu'l-qadri xayrun min elfi şehr' — değer karşılaştırması (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'tenezzelu'l-melâ'iketu ve'r-rûhu fîhâ' — melekler ve rûhun inişi gaybî (olgu=False; 70:4, 78:38 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe='L0', olgu=True, cipa=False, not_="'selâmun hiye hattâ matla'i'l-fecr' — fecrin doğuşu, zaman sınırı olarak adlı vakit; süreç / ölçü yok — L0 (89:1 kaydı emsali); tarayıcı vermedi"),
}

ARIZA = {
 (1, 5): [
  "esmâ: e_oto 1 token — 97:5 'selâm' (nekre, gecenin haberi) 'degil' kararı (esma_el_ekle; KARAR 725 → 726); e_el=? kalmadı; ölçüm mührü 1 (97:5), geçerli 0; lafız yok, Rab 1 (97:4) — sûrenin tek Rab geçişi",
  "kök tablosu: blokta yeni kök yok (1532); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı",
  "yıldız: ★★ 97:4 rab z=2,05 — lafızsız kısa sûrede tek Rab, formül davranışı",
  "fâsıla: metin ر 5 (97:1-5); ölçüm R sınıfı 5, kafiye kırığı 0 — medde artefaktı yok",
  "biçim (924): ayet 1 harf 39 → harf3 20 (besmele ailesi); 97:1 'inne' tekidi ve 97:5 haberin önde oluşu biçim alanında görünmüyor; 97:3 sayı işareti 'elf' gerçek sayı",
  "iltifât: ölçüm 0; 97:1 {1, 3} → 97:2 {2, 3} kısmi örtüşme; 97:3 şahıs işareti yok; 97:4-5 {3}",
  "özne sayısı (924): 97:4 iki özne bir fiile bağlı ('el-melâ'iketu ve'r-rûhu') — fiil 3FS, öndeki ada uyuyor; ölçüm özne sayısını göstermiyor (78:38 dikkati)",
  "adsız gönderge (1017): konuşan 1P (97:1), indirilen 3MS 'hu' (97:1), hitap 2MS (97:2) — hiçbiri adlandırılmadı; meal 'onu' ile açık bırakır",
  "KAPATILAMAZ: 97:1 'enzelnâhu' zamirinin göndergesi metinde yazılmamış",
  "çıpa: L0 1 (97:5 fecrin doğuşu — 89:1 kaydı emsali); olgu=False 4 (97:1-3 adlı gece — 44:3 kaydı emsali; 97:4 gaybî iniş — 70:4, 78:38 kaydı emsali); tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 96:19 / 97:1 sûre sınırı — 2MS'ye yasak ve secde emri ile kapanış / 1P haber ile açılış; fâsıla ب → ر; sûre 96 lafız 1 Rab 3, sûre 97 lafızsız, Rab 1",
  "aday 1039: ayet içi 0; blok içi 1 ('leyle' 97:1-3 / 'fecr' 97:5 — gece ve onu sınırlayan fecir)",
  "aday 1041: sûre içi kayıt yok — lafız yok, Rab 1; 'selâm' bu sûrede yalnız gecenin haberi",
  "bağ: kalıp / lemma eşleri okumayla (96:19, 12:2, 44:3, 44:4, 69:3, 86:2, 70:4, 78:38, 16:2, 41:30, 14:1, 89:1); bütün emsaller bu oturumda AR + meal ile basıldı",
  "◈K / ◈B: ◈K dolu 97:1-3 (ليل); 97:4 'rûh' S1 kısıtı, 97:5 فجر tetik listesinde değil — '—'; ◈B tetik kökü yok — beş ayette '—'; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 5 ayet; oturum_xy 21 sayım, 0 uyuşmaz",
  "süreç: sûre 97 dosyaları alak_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_97.py, oturum dışı; ad değişimi harf sınırıyla, açık satırlar genel numara değişiminden sonra; kapanışta 2, pakette 1 yer tutucu); sûre 5 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {}
