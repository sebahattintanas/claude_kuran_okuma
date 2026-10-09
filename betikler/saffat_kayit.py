# -*- coding: utf-8 -*-
"""saffat_kayit.py — sûre 37 (Sâffât) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
37:1-90 2026-10-07 ortam kaybından sonra oturum dökümünden yeniden yazıldı.
"""
S = 37

CIPA = {
 # blok 1-10
 5: dict(kademe='L0', olgu=True, cipa=False, not_="gökler, yer, ikisinin arası, doğular adlanıyor; tek ilişki rubûbiyet tamlaması; 'meşâriq' çoğulluğu ad düzeyinde, sayı yok; tarayıcı vermedi"),
 6: dict(kademe='L1', olgu=True, cipa=False, not_='en yakın gök + nitelik (süs) + yıldızlar; süreç/neden yok (15:16 emsali); tarayıcı vermedi'),
 10: dict(kademe='L1', olgu=True, cipa=False, not_="alev (şihâb) + nitelik (sâqib, delip geçen) + izleme işlevi; anlatı içinde, mekanizma/ölçü yok; tarayıcı vermedi"),
 # blok 11-20
 11: dict(kademe='L1', olgu=True, cipa=False, not_="madde (tîn) + nitelik (lâzib); aşama ve nedensellik yok (32:7, 35:11 emsali); tarayıcı vermedi"),
 16: dict(kademe='L1', olgu=True, cipa=False, not_='ölüm → toprak + kemik: aşamalar adlı, itirazın içinde; nedensellik yok (36:78 L0, 35:11 L1 emsali); tarayıcı vermedi'),
 # blok 81-90
 88: dict(kademe='L0', olgu=True, cipa=False, not_='yıldızlar yalnız bakışın nesnesi; süreç/nitelik/ölçü yok; tarayıcı vermedi'),
}

ARIZA = {
 (1, 10): [
  "iltifât YANLIŞ POZİTİF: 37:5 (3D, göndergesi gökler ve yer) ve 37:8 (3MP, göndergesi şeytanlar) — zamir göndergesi değişiyor, konuşan/muhatap değişmiyor (1017 ailesi); 37:6 doğru (adla anılan → 'biz')",
  "bilanço: ★ 37:7 kaynağı kafiye kırığı; etiket 'n' (z=-0,79, eşik altı) yanlış (aday 1001)",
  "bilanço: ★★★ 37:5 rab kaynaklı (z=5,77; 7 kelimede 2 Rab) — oran temelli şişme (1020/983 ailesi)",
  "harf: 37:1 harf 29 → harf3 9 — eski alan besmeleyi sayıyor (onarım tablosu; kayıt)",
  "biçim: 37:9 haberin takdimi ('lehum azâbun') biçim alanında yok; 37:2-3 fâ atfıyla yemin devamı QASEM yazılmıyor — tek yemin okunuşuyla tutarlı (kayıt)",
  "KAYIT (nakarat3 alt sınırının altında, okumada görüldü): 37:10 ↔ 15:18 'fe-etbe'ahû şihâbun' (2 kelime); 15:16-18 ile 37:6-10 aynı sırada dört adım (süsleme, 'min kulli şeytân' koruma, 'illâ men' istisna, şihâb) — defterde yalnız 37:7→15:17 xref; KAPATILAMAZ",
 ],
 (11, 20): [
  "edilgen/morfoloji: 37:16 ★★ kaynağı pas — edilgen sayılan 'mitnâ' (mâte 'mit-' biçimi PASS etiketli; aynı biçim 19:23, 19:66'da etken) — aday 1037",
  "iltifât YANLIŞ POZİTİF (alıntı sınırı, 1017 ailesi): 37:16 (alıntı içi 'biz'), 37:18 (cevap emri, 2MS/2MP), 37:19 (cevaptan anlatıya dönüş)",
  "esmâ: 37:15 mubîn ve 37:17 evvel e_oto 1 → 'degil'; §4.3 mühür ikisinde de EVET, ikisi de geçersiz; 37:17 ölçüm satırı 'esmâ yok' yazıyor (1022 ayrışması, 36:79 evvel emsali)",
  "biçim: 37:19 'innemâ' HASR sayılmıyor (924 araç notu)",
  "bilanço: ★★★ 37:11 hapaks kaynaklı (لزب, z=3,28; 983 birikimi)",
  "KAYIT (metin sayımı, defter alanı değil): 'in hâzâ illâ sihrun mubîn' korpusta 5 ayet (5:110, 6:7, 11:7, 34:43, 37:15) — nakarat3 sûre içi, xref boş; 'yâ veylenâ' 3 ayet (21:97, 36:52, 37:20), 2 kelime, nakarat3 alt sınırının altında",
 ],
 (21, 30): [
  "say: 37:22 zevc ('ezvâcehum', eşler/benzerler) sayı değil — yanlış pozitif (1004/1005)",
  "iltifât: 37:26 (2MP → 3MP, gönderge aynı topluluk) — 37:25'in konuşanı adlanmıyor; iltifât mı alıntı sınırı mı ayırt edilemiyor (1017 ailesi, KAPATILAMAZ)",
  "esmâ: 37:29 mu'min e_oto 1 → 'degil'; §4.3 mühür EVET, geçersiz; ölçüm satırı 'MÜHÜRSÜZ' (ölçüm alanının mühür tanımı §4.3 ile aynı değil — kayıt)",
  "bilanço: ★★ 37:23 allah kaynaklı (z=2,33) — sûrenin ilk lafzı, 'min dûni'llâh' olumsuz bağlamında",
  "KAYIT (nakarat3 alt sınırının altında, okumada görüldü): 37:20 ↔ 37:21 'hâzâ yevmu …' (2 kelime; dîn → fasl)",
 ],
 (31, 40): [
  "iltifât: 37:33 (alıntı → anlatı), 37:34 (3MP inkârcılar → 1P konuşan; gönderge farklı), 37:35 (1P → 3MP) — 1017 ailesi; 37:38 GERÇEK iltifât (37:35-36 suçlular 3MP → 2MP), alan bunu 37:37'nin 3MS'iyle karşılaştırarak yakalıyor",
  "bilanço: ★★★ 37:31 rab kaynaklı (z=3,23; 6 kelimede 1 Rab, 1020 ailesi); ★★★ 37:40 allah kaynaklı (z=4,47; 4 kelime, 1012 ailesi); ★ 37:35 ve 37:39 pas — kaynak doğru (qîle, tuczevne)",
  "gloss: شرك 'ortak koşma' — 37:33 'muşterikûn' ortak olanlar (VIII. bab), tanrı-ortaklığı değil (987/1015 gloss ailesi)",
  "KAYIT (metin sayımı): 'lâ ilâhe illa'llâh' harekesiz tam dizge korpusta 2 ayet (37:35, 47:19)",
  "ölçüm: 37:40 bağ alanında esit2 37:128 ve 37:160 ikişer kez basılıyor (çift kayıt; nakarat sayımını etkilemiyor — kayıt)",
  "mercek: §8 S1 düzeltilmiş tetiklerle ilk blok — 37:31-40'ta etkilenen tetik yok (◈K yalnız يوم 37:33; ◈B tetik yok)",
 ],
 (41, 50): [
  "iltifât: 37:41 (2MP suçlular → 3MP muhlas kullar; gönderge farklı) — 1017 ailesi",
  "edilgen/morfoloji: 37:47 'yunzefûn' (fethalı, edilgen biçim) PASS etiketsiz, edilgen alanı 0; aynı lemma 56:19'da kesreli etken — aday 1037'ye ek vaka (ters yönde)",
  "bilanço: ★★★ 37:45 pas (z=5,38; tek fiil 1/1, 1009 ailesi; kaynak doğru); ★★★ 37:47 hapaks (غول, z=3,28; 983 ailesi)",
  "gloss: سرر 'sır, gizleme' — 37:44 'surur' tahtlar; طرف 'uç, kenar' — 37:48 'tarf' bakış (987/1015 gloss ailesi)",
  "biçim: 37:49 teşbih (ke-enne) biçim alanında tür olarak yok (kayıt)",
  "mercek: §8 S1 ilk etkisi — 37:43 نعم (na'îm, nimet) düzeltilmiş tetikle ◈B tetiklemiyor",
 ],
 (51, 60): [
  "biçim: 37:56 tâ-yemin (ta'llâhi) QASEM sayılmıyor — aday 443 (9/9) listesinde",
  "kip/edim: 37:56 'in' hafifletilmiş inne (in-i muhaffefe + lâm-ı fârıka), alan COND/şart yazıyor — morfoloji COND etiketi (kaba desen 'in + 3 kelime içinde lâm' korpusta 26 ayet, gerçek şartla karışık; tam sayım yapılmadı — KAYIT)",
  "şahıs: 37:56 'turdîni' 2MS, morfoloji 3FS (tu- öneki) — şahıs alanı 3FS 1 yanlış (kayıt)",
  "edilgen: 37:53 ★★ kaynağı yine 'mitnâ' PASS etiketi (aday 1037 listesi)",
  "iltifât: 37:53 (alıntı içi 1P), 37:54 (alıntıdan 2MP hitaba), 37:60 (3MS nesne göndergeli) — 1017 ailesi",
  "bilanço: ★★★ 37:56 allah (z=3,47; 5 kelime, 1012); ★★★ 37:57 rab (z=3,23; 6 kelime, 1020)",
  "esmâ: 37:59 evvel (ûlâ) e_oto 1 → 'degil'; §4.3 mühür EVET, geçersiz",
  "gloss: قرن 'nesil; bağlama' — 37:51 qarîn arkadaş; طلع 'doğma (güneş)' — 37:54-55 yukarıdan bakma (987/1015)",
 ],
 (61, 70): [
  "aktör: 37:62 'zaqqûm' (bitki adı) adlı aktör (rol yer) sayılıyor; 37:65 'şeytân' benzetme teriminde adlı aktör (gayb) — kayıt",
  "bilanço: ★★★ 37:67 hapaks (شوب, z=3,28; 983); ★★★ 37:70 pas (z=5,38; tek fiil 1/1, 1009; kaynak doğru)",
  "gloss: نزل 'inme' — 37:62 nuzul (konukluk ikramı); طلع 'doğma (güneş)' — 37:65 tal' (tomurcuk); أثر 'tercih etme' — 37:70 âsâr (izler) (987/1015)",
  "biçim: 37:65 teşbih (ke-enne) biçim alanında yok — sûrede 2. vaka (49, 65; metin sayımı)",
  "KAYIT (nakarat3 alt sınırının altında): 37:67-68 'summe inne … le-' açılışı ardışık iki ayette; 37:11 ↔ 37:62 'e-… -u + temyiz + em' karşılaştırma iskeleti",
 ],
 (71, 80): [
  "say: 37:71 'ekser' (çoğunluk) sayı değil — yanlış pozitif (981/992)",
  "esmâ: 37:71 evvel, 37:78 âhir, 37:79 selâm → 'degil'; 37:75 'mucîbûn' → 'ilahi' (övülen gizli 'biz' = Tanrı; çoğul biçim, SINIR VAKASI 999/1019); §4.3 mühür 4 ayette EVET",
  "bilanço: ★★★ 37:74 allah (z=4,47; 4 kelime, 1012) — 37:40 nakaratının ikinci geçişi",
  "biçim: 37:77 ayırma zamiri ('humu'l-bâqîn') hasr anlamı biçim alanında yok (kayıt)",
  "KAYIT (nakarat3 alt sınırının altında): 37:79 'selâmun alâ' + kişi adı — 2 kelime; 37:34 ↔ 37:80 'innâ kezâlike' + fiil + grup çerçevesi (nakarat3 dışında)",
 ],
 (81, 90): [
  "esmâ: 37:81 mu'min → 'degil'; §4.3 mühür EVET, geçersiz",
  "iltifât: 37:83 (1P → 3MS, gönderge farklı), 37:88 (alıntı içi 2MP → anlatı 3MS) — 1017 ailesi",
  "bilanço: ★★★ 37:84 rab (z=3,94; 5 kelime) ve 37:87 rab (z=5,01; 4 kelime) — 1020; ★★★ 37:86 allah (z=3,47; 5 kelime) — 1012",
  "KAYIT (okumada görüldü): 37:82 ↔ 26:66 aynı cümle iki ayrı kıssada (Nûh / Mûsâ); 37:78 'el-âhirîn' / 37:82 'el-âharîn' harekesiz yazımı aynı, hareke ayırıyor",
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_37.py uygular)
DUZELTME = {
}
