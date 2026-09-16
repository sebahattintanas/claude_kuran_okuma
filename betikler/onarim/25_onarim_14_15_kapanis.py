# -*- coding: utf-8 -*-
"""25_onarim_14_15_kapanis.py — ONARIM 14 ve 15'in aday kayıtları (937-939)."""
import json

ADAYLAR = [
{"no": 937,
 "aday": "★ ONARIM 14 KAPANDI — `hapaks2`: ölçüt TOKEN'dan AYET'e taşındı. Eski `hapaks` alanı bir kökün nadirliğini ölçmek istiyor ama korpusta tek AYETTE geçen 420 kökten yalnız **399'unu** sayıyordu; kalan **21'i** o ayette birden çok token taşıdığı için düşüyordu. Yeni alan `hapaks2` ölçütü 'korpusta tek AYETTE geçen kök' olarak yazıyor. **Eski alan korundu** (protokol: hiçbir eski alan silinmez); `yildiz2` ve `z2` ayrıca yazıldı.",
 "olculen": {"eski_olcut": "tek ayet VE tek token", "yeni_olcut": "tek ayet",
             "eski_kok": 399, "yeni_kok": 420, "eklenen_kok": 21, "kaybedilen": 0,
             "eklenen_listesi": {"4_token": ["سلح"], "3_token": ["فسح", "نفذ", "زبد"],
                                 "2_token": ["رفد", "هور", "صنو", "عنكب", "بسس", "كدح", "نشط",
                                             "لهث", "رجج", "بسل", "بتل", "برم", "وطر", "زود",
                                             "ذبب", "زجج", "أزز"]},
             "hapaks_ayet": {"eski": 358, "yeni": 375},
             "yildiz_degisen_ayet": 10,
             "degisenler": {"2:197": "★1→★3", "7:176": "★1→★3", "11:99": "★2→★3",
                            "13:4": "★1→★3", "19:83": "★0→★3", "29:41": "★0→★3",
                            "43:79": "★0→★3", "55:33": "★0→★3", "79:2": "★0→★3",
                            "84:6": "★2→★3"},
             "yildiz_dagilimi": {"eski": {"0": 4029, "1": 748, "2": 579, "3": 880},
                                 "yeni": {"0": 4024, "1": 745, "2": 577, "3": 890}},
             "sinama_kumesi": "12/12", "sinama_kaynagi": "sûre 28-29 okuma kayıtlarındaki hapaks vakaları"},
 "durum": "KAPALI", "oncelik": "P0", "kaynak": "onarım turu, aday 926",
 "etiket": "onarım (P0 #10 kapandı)",
 "test_notu": "**kaybedilen == 0 savı doğrulandı: hapaks2 ⊇ hapaks, eski hapaks dolu ama hapaks2 boş olan ayet SIFIR.** Sınama kümesi okuma kayıtlarından kuruldu (onarım yazılırken değil): sûre 28-29'un sekiz belgelenmiş hapaks ayeti korunmalı, 29:41 (okumada 'sayılmıyor' diye kaydedilen vaka) artık sayılmalı, 28:12 ve 29:40 (okumada 'nadirlik yığılması ile hapaks ayrı şeyler' diye kaydedilen vakalar) boş kalmalı — **12/12.** **En çarpıcı düzeltme 29:41: sûrenin adını taşıyan kök (عنكب) korpusta yalnız o ayette geçiyor ve ayet yıldızsızdı, artık ★★★.**"},

{"no": 938,
 "aday": "★ ONARIM 15 KAPANDI — `fig2`: KELLA etiketi yüzey biçiminden morfoloji lemmasına taşındı. Eski `fig` alanı `كَلَّا` edatını yüzey biçimiyle arıyor ve `كُلّ` (her) ile karıştırıyordu: KELLA etiketli 48 ayetin **15'inde (%31)** morfolojide `LEM:كَلّا` yok ve 14'ünde `كلل` kökü var. Yeni alan `fig2`, `fig`in tamamını taşıyor ama KELLA ölçütünü `LEM:كَلّا` varlığına bağlıyor. **Eski alan korundu.**",
 "olculen": {"eski_kella_ayet": 48, "morfolojide_gercek": 33,
             "yanlis_pozitif": 15, "oran_yuzde": 31, "yanlis_negatif": 0,
             "dusen_ayetler": ["4:95", "4:130", "6:84", "6:86", "7:46", "11:111", "11:120",
                               "17:20", "17:23", "19:49", "21:72", "21:79", "25:39", "29:40", "57:10"],
             "kella_disi_etiketlerde_kaybedilen": 0,
             "etiket_dagilimi_degismeyen": {"HASR": 510, "DIKKAT": 487, "NEHY": 289,
                                            "IDRAB": 116, "ISTISNA": 100, "QASEM": 71,
                                            "AMMA": 52, "MM": 3},
             "sinama_kumesi": "8/8",
             "sinama_icerigi": "29:40 KELLA düşmeli · beş gerçek كَلَّا (74:16, 74:32, 80:11, 96:6, 102:3) korunmalı · 4:95 ve 21:79 düşmeli"},
 "durum": "KAPALI", "oncelik": "P1", "kaynak": "onarım turu, aday 927",
 "etiket": "onarım (P0 #11 kapandı)",
 "test_notu": "**kaybedilen == 0 iki yönden doğrulandı: gerçek KELLA'ların hiçbiri düşmedi (yanlış negatif SIFIR) ve KELLA dışındaki sekiz etiketin hiçbiri değişmedi.** Yanlış pozitif listesine okuma sırasında bilinmeyen iki ayet daha eklendi (25:39, 57:10) — aday 927'nin listesi on üç vakayla yazılmıştı, tam sayım on beş verdi. **Bu onarım, aday 927'nin 'seyrek etiketlerin denetlenme fırsatı çok az' kaydını da doğruluyor: 48 ayetlik bir etiket üç sûrelik okumada bir kez çıktı ve o bir kez yanlıştı.** TUR SONU: `fig`in öbür seyrek etiketleri (QASEM 71, AMMA 52, MM 3) aynı yöntemle — yüzey mi lemma mı — denetlenmeli."},

{"no": 939,
 "aday": "★ ADAY 903'ÜN KORPUS SAYILARI YENİLENDİ — VE ADAY 926'NIN İKİ ALT-KAYDI DÜŞTÜ. Yıldız formülünün iki otomatik ★★★ tetikleyicisi `hapaks2` ile yeniden hesaplandı: **hapaks2 içeren 375 ayetin 375'i ★★★** (istisnasız) · **bütün fiilleri edilgen olan 124 ayetin 124'ü ★★★** (istisnasız) · kesişim 13, birleşim **486** = `yildiz2` ile ★★★ olan **890** ayetin **%54,6'sı** (eskiden %53,5).",
 "olculen": {"hapaks2_ayet": 375, "hepsi_yildiz3": True,
             "tam_edilgen": 124, "hepsi_yildiz3_2": True,
             "kesisim": 13, "birlesim": 486, "yildiz3_toplam": 890, "kapsanan_oran": 54.6,
             "eski_oran": 53.5,
             "tek_hapaks_z": {"eski": 3.38, "yeni": 3.28},
             "hapaks2_z_dagilimi": {"3.28": 338, "6.79": 32, "10.3": 3, "13.81": 1, "17.32": 1},
             "kalan_404_kaynagi": {"rab": 179, "allah": 123, "n": 82, "pas": 23},
             "dusen_alt_kayitlar": {
               "ongoru_1": {"aday": 926, "iddia": "hapaks ayeti 358 → 379", "gercek": "358 → 375",
                            "sebep": "eklenen 21 kökün dördü, zaten hapaks taşıyan ayetlere düşüyor"},
               "ongoru_2": {"aday": 926, "iddia": "beş yeni ★★★", "gercek": "10 ayet yıldız değiştirdi, beşi yıldızsızdan ★★★'a",
                            "sebep": "21 ayetin 11'i zaten başka ölçütten ★★★ idi; kalan 10'u değişti, beşi ★ ya da ★★ iken ★★★ oldu"}}},
 "durum": "KAPALI", "oncelik": "P0", "kaynak": "onarım turu",
 "etiket": "aday 903 tazelemesi + düşen kayıt",
 "test_notu": "**Kural onarımdan sonra da geçerli ve biraz güçlendi:** tek hapaks kökün z'si 3,38'den 3,28'e indi (dağılım değişti) ama hâlâ ★★★ eşiğinin (>3) üstünde, yani **hapaks tek başına yeter şart olmayı sürdürüyor.** İki tetikleyicinin kapsadığı pay %53,5'ten %54,6'ya çıktı. **DÜŞEN İKİ ALT-KAYIT, aday 926'nın kendi öngörüleriydi ve ikisi de onarım koşulunca yanlış çıktı** — sessizce düzeltilmedi, düşürüldüğü belgelendi. Ortak sebep: **kaçan 21 kökün ayet dağılımı hesaplanmadan, kök sayısından ayet sayısına doğrudan geçilmişti.** Aday 843'ün ('sayım defterden koşulur, hafızadan değil') üçüncü tekrarı — bu kez hafızadan değil, **koşulmamış bir aritmetikten.**"},
]

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.setdefault('AL_onarim2', []).extend(ADAYLAR)
AD['son_guncelleme'] = 'onarım 14-15 (hapaks2, fig2) — adaylar 937-939'
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('aday_bulgular: AL_onarim2 →', len(AD['AL_onarim2']),
      '|', AD['AL_onarim2'][0]['no'], '-', AD['AL_onarim2'][-1]['no'])

# aday 926 ve 927'ye düşürüldü/kapandı kaydı — özgün olculen KORUNUR
for a in AD['AK_ankebut']:
    if a['no'] == 926:
        a['durum'] = 'KAPALI'
        a['dusuruldu'] = {
          "ne_zaman": "onarım 14 koşulurken (aday 937/939)",
          "yanlis_1": "olculen.onarim_etkisi.hapaks_ayet '358 → 379' → DOĞRUSU 358 → 375",
          "yanlis_2": "olculen.onarim_etkisi.yeni_yildiz3 = 5 → DOĞRUSU 10 ayet yıldız "
                      "değiştirdi, beşi yıldızsızdan ★★★'a",
          "ortak_sebep": "kaçan 21 kökün AYET dağılımı hesaplanmadan kök sayısından ayet "
                         "sayısına doğrudan geçilmişti — aday 843'ün üçüncü tekrarı, bu kez "
                         "hafızadan değil koşulmamış bir aritmetikten",
          "onarim": "22_hapaks_onarim.py · sınama 24_onarim_sinama.py 12/12"}
        print('aday 926: KAPALI + dusuruldu')
    if a['no'] == 927:
        a['durum'] = 'KAPALI'
        a['tazeleme'] = ['yanlış pozitif listesi 13 → 15 vakaya tamamlandı '
                         '(25:39 ve 57:10 eklendi); onarım 23_fig_kella_onarim.py, sınama 8/8']
        print('aday 927: KAPALI + tazeleme')
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
