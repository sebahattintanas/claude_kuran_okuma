# -*- coding: utf-8 -*-
"""19_aday_910_duzelt.py — aday 910'un düşen ölçümlerini DÜZELTMEZ, düşürüldüğünü
kaydeder. Protokol: 'Kendi kaydım düştüğünde sessizce değiştirilmez, düşürüldüğü
belgelenir.' Özgün `olculen` olduğu gibi bırakılır; yanına `dusuruldu` eklenir."""
import json
pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
for a in AD['AJ_kasas']:
    if a['no'] != 910:
        continue
    a['durum'] = 'KAPALI'
    a['dusuruldu'] = {
      "ne_zaman": "P0 #6 kapatılırken (aday 920-923)",
      "duseni_bulan": "14_cipa_tanimi.py'nin kendi sûre 27 tablosu",
      "yanlis_1": "olculen.sure_27.L3 = 0 → DOĞRUSU 1 (27:88, görünüş/durum ayrımı)",
      "yanlis_2": "olculen.sure_27.L2 = 'birkaç, hepsi olgu-dışı' → DOĞRUSU 4 kayıt, "
                  "İKİSİ gerçek doğa olgusu (27:60 yeti sınırı, 27:86 işlevsel nedensellik)",
      "yanlis_3": "test_notu'ndaki 'sûre 28'de ilk kez L2 gerçek bir doğa olgusuna "
                  "uygulanıyor' — korpus düzeyinde YANLIŞ; 27:60 ve 27:86 zaten yapmıştı. "
                  "Doğrusu: sûre 28'de ilk kez.",
      "yanlis_4": "olculen.sure_28.L1 içinde 28:73 → DOĞRUSU L2 (27:86'nın emsali, "
                  "işlevsel nedensellik)",
      "ortak_sebep": "dört kayıt da sûre 27'nin tablosuna BAKILMADAN, okuma anındaki "
                     "hatıradan kuruldu — aday 843'ün ('sayım defterden koşulur, "
                     "hafızadan değil') çıpa tarafındaki eşi",
      "alinan_onlem": "15_cipa_kademe_28.py'nin her satırı sûre 27'den hangi ayetle aynı "
                      "kademeye konduğunu (emsal) taşımak zorunda",
      "duzeltilmis_tablo": "cipa_kademe_27_28.json"}
    print('aday 910: dusuruldu alanı eklendi, özgün olculen korundu')
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
