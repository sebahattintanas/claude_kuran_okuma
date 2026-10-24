# -*- coding: utf-8 -*-
"""munafikun_kayit.py — sûre 63 (Münâfikûn) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 63

CIPA = {
 # blok 1-5
 4: dict(kademe=None, olgu=False, cipa=False, not_="'ke-ennehum huşubun musennede' — dayandırılmış kütük, teşbih aracı (insan yapımı / cansız); doğal süreç yok; tarayıcı vermedi"),
 # blok 6-11
 7: dict(kademe='L0', olgu=True, cipa=False, not_="'li'llâhi hazâ'inu's-semâvâti ve'l-ard' — gökler ve yer hazinelerin yeri / mülk olarak adlanıyor; süreç / ölçü yok — L0; tarayıcı vermedi"),
 10: dict(kademe='L0', olgu=True, cipa=False, not_="'min qabli en ye'tiye ehadekumu'l-mevt' — ölüm adlanıyor, süreç yok — L0; tarayıcı vermedi"),
 11: dict(kademe='L0', olgu=True, cipa=False, not_="'izâ câ'e eceluhâ' — ömrün sonu (ecel) adlanıyor, süreç / ölçü yok — L0; tarayıcı vermedi"),
}

ARIZA = {
 (1, 5): [
  "esmâ: blokta e_oto token yok; KARAR 598 (değişmedi); geçerli mühür yok",
  "harf alanı: ayet 1 ölçümünde harf 101 → harf3 78, isaret 0 (56:1-62:1 ailesi); 63:2-5'te fark = isaret — besmele harfleri olabilir; araç alanı, metin hakkında kanıt değil (aday 924); KAPATILAMAZ",
  "kök tablosu: kok_ekle_63 3 kök (جسم, خشب, سند; hepsi 63:4); 1427 → 1430; retroaktif yama hedef 1 (2:247 — sûre 2 kısmi okunduğu için hedefe giriyor, kaydı yok, henüz okunmadı), yama 0, genel geçiş 0",
  "yıldız (924): 63:4 ★★★ hapaks z=6,79 — yeni eklenen iki kökün (خشب, سند) tek token'ı; kaynak etiketi, içerik iddiası değil; 63:1 ★★ kısa ayette 3 lafız",
  "gloss (1021 ailesi): kök علو tablosu 'yücelik; böbürlenme' — 63:5 'te'âlev' (gelin) anlamı yazılmıyor",
  "tetik listesi dışı organ (ön-kayıt §4): 63:4 'ecsâm' (gövdeler), 63:5 'ru'ûs' (başlar) — ◈B satırı doldurulmadı, gözlem ◇'de",
  "edilgen (ölçüm): 63:3 'tubi'a', 63:4 'yu'fekûn', 63:5 'qîle' — fail adlanmıyor (1017)",
  "aday 1040 (kayıt): 62:11 → 63:1 sûre sınırı — 2MS'i ayakta bırakıp gidenlerle kapanış / 2MS'e gelen münafıklarla açılış; fâsıla ن → ن; test yok",
  "aday 1041 (kayıt): 63:1 kök شهد 'neşhedu' (münafıklar) / 've'llâhu yeşhedu' (Allah) aynı ayette; علم 'Allah ya'lemu'",
  "sıralı eşleşme (okuma): 58:15-16 'innehum sâ'e mâ kânû ya'melûn' + 'ittehazû eymânehum cunneh' / 63:2 tek ayette; ardışık değil, okuma bağı",
  "adsız (aday 1017): 63:1, 4, 5 muhatap 2MS (elçi, adsız); münafıklar (sınıf); 63:5 'qîle' söyleyen; 'rasûlu'llâh' adsız — ad verilmedi",
  "çıpa: 63:4 teşbihte kütük, olgu değil; L4 yok, L0 yok; tarayıcı adayı yok",
  "kendi kaydı (kayıttan önce): 63:4'te lemma 'sayha'nın bu oturumda basılmamış 12 okunmuş ayeti için 'hepsinde helâk sesi' içerik iddiası yazılmıştı — silindi",
  "karşıt çift (aday 1039, okuma): 63:1 münafıkların şahitliği / Allah'ın şahitliği; 63:3 'âmenû' / 'keferû'; 63:4 gövde / kütük, söz / düşman; 63:5 'te'âlev' / baş çevirme — kayıt, test yok",
  "okuma: 9:67, 49:7, 61:5, 62:11 → 63:1; 58:16, 58:15, 9:9 → 63:2; 9:87 → 63:3; 9:85, 48:29, 9:30 → 63:4; 33:28, 16:23 → 63:5 — KAPATILAMAZ",
  "tetik: ön kuru koşu 2 uyuşmaz (63:3 ◈B قلب, 63:4 ◈B سمع) → satırlar dolduruldu; kayıtta 0 uyuşmaz; [x/y] 0 (48 sayım)",
 ],
 (6, 11): [
  "esmâ: e_oto 4 token (63:8 'mu'minîn'; 63:10 'ehad', 'qarîb'; 63:11 'habîr'); 'habîr' İLÂHÎ, öbür üçü DEĞİL; KARAR 598 → 602; bilanço geçerli mühür 63:11; 63:8 ve 63:10 esma_kayit mühür EVET, karar sonrası geçersiz (1022)",
  "esmâ konum (1022): 63:11 'habîr' ölçümde 'SON' konum, ardından 'bimâ ta'melûn' geliyor",
  "yıldız (924): 63:11 ★★★ allah z=3,11 (11 kelimede 2 lafız), 63:6 ★ allah — içerik iddiası değil",
  "sayı işareti (924): 63:10 'ehad' — 'ehadekum' (biriniz), sayı değil",
  "biçim (517 / 924): 63:10 'rabbi' nidâsı ölçümde VOC olarak yazılmıyor (ölçüm kip yalnız IMPV); 63:10 1P (Allah) ve 1S (ölen) aynı ayette, iltifât 0",
  "aday 1040 (kayıt): 62:9 'zikri'llâh' / 63:9 'an zikri'llâh'; 62:11 'lehv', 'infaddû' / 63:7 'yenfaddû', 63:9 'lâ tulhikum'; 62:11 'hayru'r-râziqîn' / 63:10 'razaqnâkum' — ardışık sûreler; test yok",
  "aday 1041 (kayıt): 63:8 kök عزز 'el-e'azz' (münafıkların kendi iddiası) / 'li'llâhi'l-izzeh' (Allah, elçi, inananlar)",
  "kök iki anlam (okuma, D3): نفق 63:7 'lâ tunfiqû' (harcama) / 'el-munâfiqîn' (nifak) aynı ayette; gloss iki anlamı taşıyor",
  "adsız (aday 1017): 63:6 2MS muhatap; 63:7 'men inde rasûli'llâh'; 63:8 'el-e'azz' / 'el-ezell', 'el-medîne' (hangi şehir söylenmiyor, ad verilmedi); 63:10 ölen 1S — ad verilmedi",
  "çıpa: L0 63:7 (gökler ve yer), 63:10 (ölüm), 63:11 (ecel); 63:8 şehir insan yapımı, olgu değil; tarayıcı adayı yok",
  "kapanan sûre içi eşler: غفر 63:5 → 63:6 (son); فقه 63:3 → 63:7; 'lâkinne'l-munâfiqîn' 63:7 → 63:8 (nakarat3 GEÇMEZ); رسل 63:8, نفق 63:10, أخر, أجل 63:10 → 63:11 son; sûre içinde açık eş kalmadı",
  "fâsıla: sûre içi bütün ayetler ن; kafiye kırığı 0",
  "kendi kaydı (kayıttan önce): 63:6 ve 63:11'de okunmuş ama bu oturumda basılmamış iki ölçüm xref ayeti ve 63:11'de bir lemma eşi adla anılmıştı → sayıyla",
  "karşıt çift (aday 1039, okuma): 63:6 dilesen / dilemesen; 63:7 harcamayın / hazineler Allah'ın; 63:8 e'azz / ezell; 63:9 zikir / mal ve çocuklar; 63:7 / 63:10 'lâ tunfiqû' / 'enfiqû'; 63:10 / 63:11 erteleme dileği / ertelenmeme — kayıt, test yok",
  "okuma: 9:80, 47:34, 9:24, 61:5 → 63:6; 49:3, 62:11, 15:21 → 63:7; 11:92, 10:65 → 63:8; 9:85, 57:20, 62:9, 9:69 → 63:9; 62:11, 23:99, 14:44, 9:75 → 63:10; 16:61, 9:16 → 63:11 — KAPATILAMAZ",
  "tetik: ön kuru koşu 4 uyuşmaz (63:7 ◈K سمو أرض, 63:10 ◈K أجل ve ◈B موت, 63:11 ◈K أجل) → satırlar dolduruldu; kayıtta 0 uyuşmaz; [x/y] 0 (68 sayım)",
 ],
}

DUZELTME = {
}
