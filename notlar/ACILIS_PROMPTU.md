Kur'an derin okuma projesine devam ediyoruz.
Depo: github.com/sebahattintanas/claude_kuran_okuma

## İLK İŞ — sırayla

1. `git clone` (sığ klon yeter). Betikleri sırayla koştur:
   defter.py → defter2 → defter3 → defter4 → defter5 → aktor2 → katman6 → graf2
   (~3 dk; defter.json'u sıfırdan kurar — 6236 ayet, 39 alan)
2. `notlar/okuma_protokolu.json` — sekiz kilitli karar
3. `notlar/OKUMA_STANDARDI.md` — okuma düzeni ve biçim kuralları.
   **Sondaki yedi tarihli bölümü mutlaka oku**, özellikle 2026-08-24 (biçim kilidi)
   ve 2026-08-26 (dikey katman onarımı).
4. `notlar/OTURUM_2026-08-26_KAPANIS.md` — önceki oturumun durumu, düzeltilen
   hatalar, açık borçlar
5. `notlar/okuma_metni.json` — okumanın kaydı; devam noktası `ilerleme` alanında
6. `bulgular/aday_bulgular.json` — 437 açık aday

## DEVAM NOKTASI

**Sûre 21 (Enbiyâ), ayet 21.** Sûre 20 (Tâhâ) TAM okundu (135/135).
Sûre 21 makro profili ve 1–20 hazır. Blok akışı 20 ayet.

## ÇIKTI BİÇİMİ — bu oturumda iki kez ihlâl edildi, dikkat

Okumanın kendisi **sohbete** yazılır, ayet ayet. Dosyaya yazıp sohbete özet
koymak okuma sayılmaz. Her ayet için, bu sırayla:

    ### 21:NN
    > Arapça tam metin (blok alıntı, ayrı satır)
    **Türkçe meal** (Claude'un çalışma çevirisi, kalın)
    › ölçüm    — alan sırası sabit: eksen · aktör · kip ve söz edimi ·
                 şahıs ve iltifât · sözlük ve biçim · bağ
    ◇ matematikçi merceği   — her ayette
    🜁 biyolog · 🜂 uzay      — YALNIZ ★★★ ayetlerde
    ▽ dikey okuma

Kurallar:
- **Ayet numarası zorunlu.** Numarasız blok geçersiz.
- **Karşılıksız Arapça yok.** Her Arapça dizgi hemen ardından italik parantez
  içinde Türkçesini alır — kök adı, lemma, esmâ, fâsıla kelimesi, aktör adı dahil.
- **★★★ ayetlerde üç mercek de o ayetin kendi malzemesine bağlı çalışır.**
  Çıpası olmayan mercek YAZILMAZ; atlandığı belirtilir.
- **▽ satırı komşuluk zenginleşmesi olmadan yazılamaz.** `dikey_oku()` iki parça
  döndürür; (A) komşuluk zenginleşmesi birincildir, (B) Allah medyan mesafesi
  ikincil ve **etiketsiz** verilir (aday 435: düz null bozuk, etiketlerin %32.8'i
  konum artefaktı).

## KATI KURAL

Okuma sırasında **hiçbir hipotez test edilmez**. Dikkat çeken her şey
`bulgular/aday_bulgular.json`'a yazılır; test tur sonunda toplu Bonferroni ile.
Aranarak bulunan adaylar "ARANARAK BULUNDU" etiketiyle kaydedilir ve testleri
motive eden ayetler dışlanarak kurulur.

## HER BLOK SONUNDA

    python3 turkce_denetim.py                       # SIFIR olmadan blok kapanmaz
    PYTHONHASHSEED=0 python3 anahtar_denetim.py     # taban: ciktilar/anahtar_denetim_raporu_tohum0.txt

Yeni kök geçtiğinde önce `tablolar/kok_turkce.json`'a eklenir, sonra kullanılır.
Anahtarlar **korpus çıktısından kopyalanır, elle yazılmaz**.

Kayıt dosyaları: `okuma_metni.json` (ar + meal + ölçüm + mercek + dikey) ·
`mercek_kayit.json` · `okuma_baglantilari.json` · `aday_bulgular.json`

## AÇIK BORÇLAR (tur sonu, P0 sırası)

1. **435** — `dikey_oku.py`'ye konum-eşli null; 154 dikey satırı yeniden üretilecek
2. **414** — `esma_listesi.json` bağlam ayırmıyor; sûre 20'de 5 yanlış pozitif (%38)
3. **431** — `anahtar_denetim.py` öneri metni deterministik değil
4. **437** — hizalama ölçümünde donmuş kalıp ayrımı yapılacak

`nuzul.json` ve `varlik_katalog.json`'un `zaman` alanı GÜVENİLMEZ — bu alanlara
dayanan bulgu kurulamaz.

## OTURUM SONU

`YAPILACAKLAR.md` güncellenir, `OTURUM_<tarih>_KAPANIS.md` yazılır, değişen
dosyalar paketlenir. **Push yapılamıyor** (kimlik yok) — değişen dosyalar depo
yapısıyla aynı klasörlemede zip olarak verilir, kullanıcı elle kopyalar.
