# YAPILACAKLAR — programcı gözüyle (öncelik sıralı)

## ALTYAPI — OTURUM RUTİNİ (Ağustos 2026'da kuruldu)
- [x] GitHub deposu açıldı: `github.com/sebahattintanas/claude_kuran_okuma` (public) — 55 dosya, kategorik yapı, bütünlük doğrulandı (NFC ✓, morph 130030 satır ✓)
- [x] Proje alanı küçültüldü (19→3.5 MB); morph.txt + kuran_veri.json artık oturum başında kaynağından/depodan indirilir (rutin: OKUMA_SISTEMI_OZET.md sonunda)
- [x] **Kayıp dosyalar yeniden üretildi (Ağu 2026):** `kok_adlar.json` (1651/1651 kök; 430 katalog + 1221 claude-üretimi, kaynak etiketli — betikler/kok_adlar_derle.py ile yeniden üretilebilir), `bulgu_karsi_kutup_mesafe.json` (asimetri: pozitif kutuplar demirli, negatifler nötr; 3 kutup Bonferroni-sağlam), `bulgu_denge_mizan.json` (emir-mîzanı medyan 12 vs sahne-mîzanı 118, tam ayrışma, p=0.0106)
- [ ] kok_adlar.json denetimi: claude-kaynaklı 1221 adın örneklem denetimi + çok-kavramlı köklerde birincil ad seçimi (نور→'ateş' sorunu: frekans-birincil yerine bağlam-birincil?)
- [ ] Oturum sonu kuralı: güncellenen her dosya çıktı olarak verilir → kullanıcı depoya yükler (aynı adla yükleme = üstüne yazma + sürüm geçmişi)

## P0 — VERİ BÜTÜNLÜĞÜ (önce bunlar, gerisi buna bağlı)
- [ ] **بشر (beşer/müjde) ayrımını kok_anlam_tablosu'na işle** — beşer(insan-tür) vs büşrâ/beşîr/mübeşşir(müjde). Şu an SADECE analizde ayırdık, tabloda YOK. (ظلم, كذب işlendi; بشر eksik.)
- [ ] **insân/nâs ayrımını sisteme sabitle** — lemma إِنسان(birey) vs ناس(topluluk); dikey okumada kritik çıktı, kalıcı olmalı
- [ ] **kelime-akışı kurma fonksiyonunu MODÜLLEŞTİR** — "kelime=benzersiz wid, asıl N/V/ADJ/PN segmentinden lemma, el- takısı atla" mantığı 3-4 kez elle yazıldı; tek fonksiyon yap (akis_kur.py), tekrar kullan
- [ ] kok_anlam_tablosu artık 16 kök — bir doğrulama scripti yaz (her ayrım nûr/adl gibi bir kontrol-kavramıyla test edilsin, %-oran raporu)

## P1 — DİKEY OKUMA ARACINI GENELLEŞTİR
- [ ] **dikey_oku(kavram) fonksiyonu** — girdi: kök/lemma; çıktı: (A komşuluk bandı öncesi/sonrası, B Allah-mesafe medyanı, C ayet örnekleri, D eksendeki yeri). Şu an her kavram için elle kod yazıyoruz.
- [ ] **Allah-ekseni gradyan tablosunu genişlet** — şu an 8 kavram (hudûd→tuğyân). Tüm çekirdek kavramları (~30) ekle, sıralı bir "gradyan cetveli" çıkar
- [ ] Rab için de aynı komşuluk-imzası (Allah'ınki: öncesi yöneliş/sonrası nitelik; Rab'ınki rahmet/dua mı?)

## P2 — BULGULARI PROGRAMA BAĞLA (kuran_okuma.html)
- [ ] **"Mercek seç" paneli** + uyarı metni ("meal/tefsir değildir...") + 3./4. sütun
- [ ] Fizikçi(×4) + matematikçi(makro+mikro) karşılaşmalarını panele göm — karsilasmalar.json'dan oku
- [ ] Kavram kartlarına "Allah-ekseni konumu" rozeti (bu kavram Allah'a X kelime, gradyanda şurada)
- [ ] ▶Oku audio wire (everyayah CDN) — hâlâ bağlı değil

## P3 — YENİ ÖLÇÜMLER (bekleyen sorular)
- [ ] İki-Allah-arası boşluk = anlatı/kıssa modu — NİCEL doğrula (Allah-sessiz bölgelerde özel-isim/kavim yoğunluğu > Allah-yoğun bölge?)
- [ ] Allah komşuluk-imzası (öncesi yöneliş, sonrası ilim/mağfiret/rahmet) — bir bulgu dosyasına kaydet (henüz kaydedilmedi!)
- [ ] beşer/müjde ayrımı sonrası "insan" gradyanını yeniden hesapla (temiz)
- [ ] adl/zulüm ve nûr/zulmet çiftlerini dikey oku (aynalar modeline bağla)

## BEKLEYEN (eski, düşük öncelik)
- [ ] Kevser-metrik mushaf (gerçek satır verisi) → dikey/sayfa geometrisi
- [ ] Gerçek tilavet kaydı → akustik enerji
- [ ] 3-dizilim (mushaf/nüzul/rastgele) değişmezlik testleri
- [ ] kozmolog + genetikçi mercekleri

## BU OTURUMDA TAMAMLANANLAR ✓
- ظلم → zulüm/zulmet ayrımı (nûr-doğrulama %61 vs %5)
- كذب → kizb/tekzîb ayrımı (tekzîb=vahiy reddi, 242 vs 40)
- AŞMA ekseni temizlendi (440→~150, zulüm ayrı eksen)
- Allah-ekseni dikey okuma yöntemi + gradyan (bulgu_allah_ekseni_dikey.json)
- Allah↔karşı-kutup mesafe (bulgu_karsi_kutup_mesafe.json)
- Matematikçi makro+mikro karşılaşmaları (karsilasmalar.json)
- Denge/mîzan iki-katmanlı ölçü (bulgu_denge_mizan.json)
