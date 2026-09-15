#!/bin/sh
# ONARIM BORU HATTI — düz çalışma dizininden, bu sırayla koşulur.
# Ön koşul: defter.py -> defter2 -> defter3 -> defter4 -> defter5 -> aktor2
#           -> katman6 -> graf2 tamamlanmış olmalı (defter.json hazır).
set -e
python3 onarim/01_adsiz_lemma_listesi.py    # adsiz_lemma_listesi.json (korpustan, çapa konumlarla)
python3 onarim/02_adsiz_onarim.py           # -> defter.adsiz2
python3 onarim/03_adsiz_dogrulama.py        # yanlış negatif denetimi (11/11 sınama)
python3 onarim/04_ngram_altyapi.py          # ayet_iskelet.json + ngram_indeks.json (morfoloji tabanlı)
python3 onarim/06_esit2_yaz.py              # -> defter.esit2  (tam / yakin / benzer)
python3 onarim/07_nakarat_onarim.py         # -> defter.nakarat2 + nakarat_kaliplari.json
python3 onarim/08_adli_ve_mm_onarim.py      # -> defter.adli2, defter.mm2
python3 onarim/09_dikey_kaynak.py           # dikey kaynak sınıflaması (blok_dikey.py bunu çağırır)
python3 onarim/11_harf_onarim.py            # -> defter.harf2 (besmele katkısı çıkarıldı)
python3 onarim/13_harf_kural.py             # -> defter.harf3, defter.isaret
# --- rapor betikleri (defteri değiştirmez)
python3 onarim/05_esit_onarim.py            # esit eşik taraması
python3 onarim/10_sure27_yeniden.py         # sûre 27 eski/yeni alan karşılaştırması
python3 onarim/12_nakarat_26_27.py          # aday 781 kontrollü çifti
python3 onarim/14_cipa_tanimi.py            # çıpa kademe tablosu (P0 #6)
echo "onarım boru hattı tamam"
