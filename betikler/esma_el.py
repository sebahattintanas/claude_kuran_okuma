# -*- coding: utf-8 -*-
"""esma_el.py — esmâ tokenleri için OKUYUCU KARARI (ön-kayıt §4.2 son cümlesi).
Anahtar 'S:A:kelime' (kelime sırası morph.txt'ten); Arapça yazılmaz.
Değer: 'ilahi' (Allah'ı niteleyen yüklem/sıfat/temyiz) | 'degil' (ilâhî olmayan gönderge).
Karar okumada, blok bilançosunda gerekçesiyle verilir; burada yalnız sonuç tutulur."""
KARAR = {
 # sûre 33, blok 1-10
 '33:1:12': 'ilahi', '33:1:13': 'ilahi',     # kâne'nin haberi
 '33:2:12': 'ilahi',                          # kâne'nin haberi
 '33:3:6':  'ilahi',                          # temyiz — kefâ bi-llâhi vekîlen
 '33:5:27': 'ilahi', '33:5:28': 'ilahi',     # kâne'nin haberi
 '33:6:3':  'degil', '33:6:17': 'degil',     # mü'minler (insan)
 '33:6:23': 'degil',                          # evliyâ (insan dostlar)
 '33:9:21': 'ilahi',                          # kâne'nin haberi
 # sûre 33, blok 11-20
 '33:11:3':  'degil',                         # mü'minler (imtihan edilenler)
 '33:17:22': 'degil', '33:17:24': 'degil',   # 'Allah'tan başka dost ve yardımcı' — olumsuzlanan başkası
}
