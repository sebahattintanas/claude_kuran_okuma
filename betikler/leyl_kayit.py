# -*- coding: utf-8 -*-
"""leyl_kayit.py — sûre 92 (Leyl) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 92

CIPA = {
 # blok 1-11
 1: dict(kademe='L0', olgu=True, cipa=False, not_="'ve'l-leyli izâ yağşâ' — yemin edilen vakit + süreç; mekanizma yok — L0 (91:4 kaydı emsali); tarayıcı vermedi"),
 2: dict(kademe='L0', olgu=True, cipa=False, not_="'ve'n-nehâri izâ tecellâ' — yemin edilen vakit + süreç — L0 (91:3 kaydı emsali); tarayıcı vermedi"),
 3: dict(kademe='L1', olgu=True, cipa=False, not_="'ve mâ xalaqa'z-zekera ve'l-unthâ' — yaratma + iki cins adı; aşama / madde / mekanizma yok — L1 (49:13 kaydı emsali); tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'inne sa'yekum le-şettâ' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'fe-emmâ men a'tâ ve'ttaqâ' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'ve saddaqa bi'l-husnâ' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'fe-se-nuyessiruhû li'l-yusrâ' — âhiret / sonuç (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'ve emmâ men bexile ve'steğnâ' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 9: dict(kademe=None, olgu=False, cipa=False, not_="'ve kezzebe bi'l-husnâ' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'fe-se-nuyessiruhû li'l-'usrâ' — âhiret / sonuç (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 11: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ yuğnî 'anhu mâluhû izâ teraddâ' — tutum / âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 12-21
 12: dict(kademe=None, olgu=False, cipa=False, not_="'inne 'aleynâ le'l-hudâ' — söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'ve inne lenâ le'l-âxirate ve'l-ûlâ' — âhiret / söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="'fe-enzertukum nâran telezzâ' — âhiret, uyarı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'lâ yaslâhâ ille'l-eşqâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 16: dict(kademe=None, olgu=False, cipa=False, not_="'ellezî kezzebe ve tevellâ' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 17: dict(kademe=None, olgu=False, cipa=False, not_="'ve se-yujennebuhe'l-etqâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 18: dict(kademe=None, olgu=False, cipa=False, not_="'ellezî yu'tî mâlehû yetezekkâ' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 19: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ li-ehadin 'indehû min ni'metin tujzâ' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 20: dict(kademe=None, olgu=False, cipa=False, not_="'ille'btiğâ'e vechi rabbihi'l-a'lâ' — tutum / Rab (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 21: dict(kademe=None, olgu=False, cipa=False, not_="'ve le-sevfe yerdâ' — âhiret / tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 11): [
  "esmâ: e_oto 0 token; KARAR değişmedi (720); lafız ve Rab yok",
  "kök tablosu: blokta yeni kök yok (1527); retroaktif yama hedefli 0, genel 0",
  "yıldız (1001): ★ 92:3 ve 92:11 kaynak 'n' etiketli, ikisi de kafiye kırığıyla — kırıklar sahte (aşağıda); ★ artefakt",
  "fâsıla (924): 92:3 ve 92:11 ölçüm KAFİYE KIRILMASI — son harfte medde işareti harf sayıldı; metinde ى, blok boyunca tek tip — yanlış pozitif (sûre 70 dikkati ile aynı)",
  "biçim (924): 92:1 QASEM; 92:2-3 atıflı yeminlerde QASEM yok; 92:2 'tecellâ' V. bab, ölçüm bab alanı 'I. bab' (morph VF:1 etiketi); ayet 1 harf 31 → harf3 12 (besmele ailesi)",
  "iltifât: 92:4 {3} → {2} 2MP hitabın girişi; 92:5 {2} → {3} hitaptan 'men' anlatımına; 92:7 ve 92:10 {3} → {1, 3} kısmi örtüşme, ölçüm 0 — 1P konuşanın girişi ölçümde görünmüyor (924)",
  "adsız gönderge (1017): yemin eden; 92:3 yaratan ('mâ'); 92:4 hitap 2MP; 92:5-11 'men'; 92:7 ve 92:10 konuşan 1P",
  "KAPATILAMAZ: 92:3 'mâ' ilgi zamiri mi mastar edatı mı (morph REL, meal ilgi okumasını seçti); 92:6 ve 92:9 'el-husnâ'nın neyin en güzeli olduğu",
  "kök gloss (1021): ذكر 'anma, zikir' — 92:3 'zeker' (erkek) anlamına uymuyor",
  "çıpa: L0 2 (92:1-2 yemin edilen vakit); L1 1 (92:3 yaratma + iki cins — 49:13 kaydı emsali); olgu=False 8; tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 91:15 / 92:1 sûre sınırı — öznesi açık olmayan 'korkmaz' ile kapanış / geceye yemin ile açılış; fâsıla ا → ى; 91 lafızlı ve Rablı, 92 bu blokta lafızsız ve Rabsız; ardışık sûre okuma bağları 91:4 / 92:1 aynı lemma dizisi ('leyl' + 'izâ' + 'ğaşiye'; 3FS nesne / nesnesiz), 91:3 / 92:2 've'n-nehâri izâ' + kök جلو (II. bab nesneli / V. bab nesnesiz)",
  "aday 1039: ayet içi 1 (92:3 erkek / dişi) + ayetler arası 4 (92:1 / 2 gece / gündüz ve bürüme / açığa çıkma; 92:5 / 8 verdi / cimrilik etti; 92:6 / 9 doğruladı / yalanladı; 92:7 / 10 en kolay / en zor)",
  "aday 1041: blokta kayıt yok — lafız ve Rab yok; sûreler arası okuma notu: kök غني 47:38 ve 57:24'te lafız için ('el-ğaniyy') / 92:8'de insan için ('istağnâ'); kök بخل üçünde de insan",
  "bağ: kalıp / lemma eşleri okumayla (91:3, 91:4, 10:6, 49:13, 76:22, 53:40, 20:53, 79:37, 53:34, 87:8, 79:40, 80:5, 80:8, 57:24, 47:38, 74:9, 69:28); bütün emsaller sohbette AR + meal ile basıldı",
  "◈K / ◈B: ◈K dolu 92:1 ليل, 92:2 نهر; ◈B dolu 92:3 (tetik خلق, أنث; ذكر tetik listesinde değil); tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 11 ayet; oturum_xy 26 sayım, 0 uyuşmaz",
  "süreç: sûre 92 dosyaları sems_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_92.py, oturum dışı); blok sınırı sûrenin bölümlerine göre (1-11 yeminler + cevap + iki yol; 12-21 hidayet + ateş uyarısı + en bedbaht / en sakınan); taban 86953a8",
 ],
 (12, 21): [
  "esmâ: e_oto 3 token (92:13 'âxir', 'evvel'; 92:19 'ehad') — üçü 'degil' (yamalar/esma_el_92_12_21.txt); KARAR 720 → 723; ölçüm mührü 92:13, 92:19 → bilanço geçerli 0 (1022); lafız yok, Rab 1 (92:20) — sûrede lafız 0, Rab 1",
  "kök tablosu: kok_ekle_92 1 kök (لظي 92:14; korpusta tek ayet); 1527 → 1528; retroaktif yama hedefli 0, genel 0 (ikinci koşu da 0); taban kayıtları om_base ile aynı",
  "özel ad / kök (924): 70:15 'lezâ' aynı harflerle morph'ta özel ad, kök etiketi yok — لظي kök sayısı (1 ayet) ona dahil değil",
  "yıldız: ★★★ 92:14 hapaks z=3,28 (yeni kök); ★★★ 92:17 ve 92:19 pas z=5,38; ★★★ 92:20 rab z=3,94 — formül davranışı; 92:19 ★★★ kaynağı 'pas', kırık bayrağı da açık (1001)",
  "fâsıla (924): 92:19 ölçüm KAFİYE KIRILMASI — son harfte medde işareti harf sayıldı; metinde ى — yanlış pozitif; sûre boyunca fâsıla tek tip ى, ölçüm kırıklarının üçü de (92:3, 11, 19) bu artefakt",
  "biçim (924): 92:14 'telezzâ' V. bab, ölçüm bab alanı 'I. bab' (morph VF:1); 92:19 sayı işareti 'ehad' yanlış pozitif",
  "iltifât (924): 92:12 {3} → {1} ölçüm 1; 92:14 1P → 1S geçişi {1} → {1, 2, 3} kısmi örtüşme, ölçüm 0 — konuşan katman değişimi görünmüyor",
  "adsız gönderge (1017): konuşan 1P (92:12-13) ve 1S (92:14); hitap 2MP; 92:15-16 en bedbaht; 92:17-20 en sakınan; 92:17 ve 92:19 edilgen fiillerin faili; 92:21 'yerdâ' öznesi",
  "KAPATILAMAZ: 92:20 'el-a'lâ'nın bağlandığı ad ('vech' / 'rabb', ikisi GEN); 92:21 'yerdâ' öznesi (en sakınan / Rab); 92:18 'yetezekkâ' hâl mi amaç mı",
  "kök gloss (1021): بغي 'iffetsizlik; azgınlık; yakışma' — 92:20 'ibtiğâ'' (arama) anlamına uymuyor",
  "çıpa: blokta merdiven uygulanan ayet yok (10 ayetin 10'u olgu=False: söz, âhiret, tutum); tarayıcı v4 blokta aday vermedi",
  "aday 1041: sûre içi kayıt yok — lafız yok, Rab 1 (92:20); sûreler arası okuma notu: lemma 'a'lâ' + 'rabb' 87:1 ve 92:20 Rab tamlaması / 79:24 konuşanın kendisi için iddiası",
  "aday 1039: ayet içi 1 (92:13 âhiret / ilk) + ayetler arası 1 (92:15 / 17 en bedbaht / en sakınan; ona girer / ondan uzak tutulur)",
  "aday 1040 (okuma bağı): ardışık sûre 91:12 / 92:15 lemma 'eşqâ' — korpusun üç geçişi (87:11, 91:12, 92:15) okundu",
  "bağ: kalıp / lemma eşleri okumayla (75:17, 75:19, 88:26, 22:67, 53:25, 79:25, 70:15, 87:11, 87:12, 91:12, 20:48, 75:32, 49:13, 87:14, 79:18, 13:22, 87:1, 79:24); bütün emsaller sohbette AR + meal ile basıldı",
  "◈K / ◈B: blokta tetik yok (نور 'nâr' ve نعم 'ni'meh' tetiklemiyor); tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 1-21 toplam 21 / 0; oturum_xy blok 24, 1-21 toplam 50 sayım, 0 uyuşmaz",
  "süreç: 1-11 bloğundan sonra ortam korundu (okuma_metni['92'] 11 anahtar, ilerleme 4861 ile doğrulandı); taban 86953a8 değişmedi",
 ],
}

DUZELTME = {
 11: {'alan': 'mercek', 'eski': "Lemma 'ağnâ' 28 ayet: 69:28 ('mâ ağnâ 'annî mâliyeh') (okumada görüldü), okunmuş 22 ayet daha, 92:11, henüz okunmamış 4", 'dogru': "28 ayetlik sayım 92:11'in kendi lemma etiketidir ('ağnet') ve 69:28'i içermiyor: lemma 28 ayet — okunmuş 23, 92:11, henüz okunmamış 4. 69:28 'mâ ağnâ 'annî mâliyeh' morph'ta ayrı lemma etiketinde ('ağnâ', 15 ayet) — aynı fiil iki lemma etiketine bölünmüş (924); 69:28 ile eşlik lemma 'mâl' ve kök غني üzerinden doğru. Basılan metinler değişmedi; yalnız lemma sayım cümlesi. Sûre 93 okunurken (93:8 'ağnâ' lemma listesi karşılaştırılınca) kayıttan sonra yakalandı.", 'aday': None, 'blok': '1-11'},
}
