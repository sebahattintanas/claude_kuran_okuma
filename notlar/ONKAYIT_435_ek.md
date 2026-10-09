# ÖN-KAYIT EKİ — aday 435 yeniden testi (konum-eşli null) için ek katmanlar

Tarih: 2026-10-06 (sûre 37 oturumu; kullanıcı kararı). Bu belge `ONKAYIT_esma_katmanlari.md` §4.4'teki **kapı koşulunu** (35 kavramlık gradyanın konum-eşli null ile yeniden testi, aday 435 borcu) DEĞİŞTİRMEZ; o belge dondurulmuş kalır. Burada yalnız aynı teste EKLENECEK raporlama katmanları, test koşulmadan ve tam okuma bitmeden sabitlenir.

## 1. Değişmeyenler
- Birincil ölçü ve kapı kararı: `ONKAYIT_esma_katmanlari.md` §4.4'teki tanımla (lafza en yakın kelime mesafesi, konum-eşli null). Kapıyı yalnız bu ölçü açar ya da kapar.
- Aşağıdaki ekler İKİNCİL'dir: kapıyı açamaz, kapatamaz, bant eşiklerini (≤5 / 6–20 / >20) değiştiremez. Ayrı tablo olarak raporlanır; ikincil testlerin sayısı (aşağıda 3 ek × katman) raporda açıkça yazılır ve tek tek anlamlılık iddiası Bonferroni düzeltmeli verilir.
- Null modeli her ekte aynı: konum-eşli permütasyon (aday 435), birincil testle aynı tohum ve permütasyon sayısı.

## 2. Ek A — iki yönlü mesafe (aday 1027)
Her kavram tokeni için, sûre içinde ve sûre sınırını geçmeden:
- **geri mesafe** ("lafızdan beri"): önceki lafız tokenine kelime sayısı;
- **ileri mesafe** ("lafza kadar"): sonraki lafız tokenine kelime sayısı.
Önünde (ya da arkasında) sûre içinde lafız olmayan token o yönün hesabına girmez; dışlanan sayısı raporlanır. Kavram başına iki medyan ve iki konum-eşli p. Duyarlılık: §4.3 mühür tokenleri (e_el = ilahi olan mühür kalıbı) dışlanarak yeniden (1027 karıştırıcısı).

## 3. Ek B — taşıyıcı duyarlılık katmanları (aday 1025)
"Lafız" çapası dört iç içe katmanla genişletilir; her katman Ek A ile birlikte koşulur:
- **K0** yalnız lafız — defter lafız alanı (LEM اللَّه). Birincil testle aynı çapa.
- **K1** K0 + Rab (defter Rab alanı) + tanrısal 1P. Tanrısal 1P = konuşanı Tanrı olan ayetlerdeki 1P eki. Bu işaret tam okuma bitince, e_el turuna benzer TEK bir turda, okuma kayıtlarındaki ◈A/◇ alanlarından elle konur; işaretlenemeyen ayetler K1'den dışlanır ve sayıları raporlanır.
- **K2** K1 + edilgen fiil (defter `pas`, PASS etiketi). Aday 1037'deki morfoloji tutarsızlığı (mâte 'mit-' biçimi, 6 PASS token) onarılmadıysa bu 6 token K2'den DIŞLANIR.
- **K3** K2 + gönderge-esmâ: yalnız e_el = 'ilahi' olan esmâ tokenleri (aday 1031); e_oto tek başına yetmez.
Sen/O zamir göndergesi (1025'te adı geçen) araç olmadığı için hiçbir katmana girmez; bu eksik raporda yazılır.

## 4. Ek C — nakarat sınırlı aralık işareti (aday 1032)
Her istatistikten önce: iki sınır lafız tokeninin İKİSİ de aynı nakarat3 kalıbının içinde olan aralıklar "nakarat sınırlı" işaretlenir. nakarat3 tanımı defterdeki gibi sûre içidir. Birincil ve tüm ikincil sonuçlar iki kez verilir: (i) tüm aralıklar, (ii) nakarat sınırlılar hariç. İşaretli aralık sayısı ve kelime payı raporlanır.

## 5. Açık bağımlılık
- Aday 1030 KARARLANDI (2026-10-06, kilitten önce): vokatif Allâhümme (5 token) lafız SAYILMAZ; K0 = defter lafız alanı, değişmez. Tokenler `tablolar/lafiz_vokatif.json` bayrağıyla ayrı tutulur ve her katmanın raporunda 'vokatif lafız komşuluğu' olarak ayrıca işaretlenir; hiçbir katmana çapa olarak girmez.

## 6. Sıra
Tam okuma biter → süzgeç → geriye dönük e_el turu → süzgeç doğrulaması → tanrısal 1P işaret turu (K1 için) → aday 435 yeniden testi: birincil + Ek A/B/C → H1-H4 (H3 kapısı birincil teste bağlı).

## 7. Kilit
Bu belgenin commit hash'i depoya yüklendiğinde buraya yazılır; içerik o andan sonra değiştirilmez.

## 8. Sapmalar
(boş)
