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
 # sûre 33, blok 21-30
 '33:21:14': 'degil',                         # el-yevm el-âhir (gün)
 '33:22:3':  'degil', '33:23:2': 'degil',    # mü'minler (insan)
 '33:24:15': 'ilahi', '33:24:16': 'ilahi',   # kâne'nin haberi
 '33:25:11': 'degil',                         # mü'minler (nesne)
 '33:25:15': 'ilahi', '33:25:16': 'ilahi',   # kâne'nin haberi
 '33:27:13': 'ilahi',                         # kâne'nin haberi
 '33:29:7':  'degil',                         # ed-dâr el-âhira (yurt)
 # sûre 33, blok 31-40
 '33:31:14': 'degil',                         # rızk kerîm (rızkın sıfatı)
 '33:32:4':  'degil',                         # ke-ehadin: 'herhangi biri'
 '33:33:8':  'degil',                         # el-câhiliyyet el-ûlâ (ilk)
 '33:34:13': 'ilahi', '33:34:14': 'ilahi',   # kâne'nin haberi
 '33:35:4':  'degil', '33:36:3': 'degil',    # mü'min (insan)
 '33:36:24': 'degil',                         # dalâlen mübînen (sapmanın sıfatı)
 '33:37:36': 'degil',                         # mü'minler (insan)
 '33:39:8':  'degil',                         # lâ yahşevne ehaden: 'hiç kimse'
 '33:39:13': 'ilahi',                         # temyiz — kefâ billâhi hasîben
 '33:40:5':  'degil',                         # ebâ ehadin: 'hiçbiri'
 '33:40:17': 'ilahi',                         # kâne'nin haberi
 # sûre 33, blok 41-50
 '33:43:10': 'degil',                         # zulumâttan NÛRA (ışık, gidilen yer)
 '33:43:12': 'degil',                         # mü'minlere (insan)
 '33:43:13': 'ilahi',                         # kâne'nin haberi — özne 'huve' (lafızsız)
 '33:44:4':  'degil',                         # tahiyyetühüm selâm (selamlaşma)
 '33:44:8':  'degil',                         # ecren kerîmen (ecrin sıfatı)
 '33:47:2':  'degil', '33:47:8': 'degil',    # mü'minler · fadlan kebîran (lütfun sıfatı)
 '33:48:12': 'ilahi',                         # temyiz — kefâ billâhi vekîlen
 '33:50:43': 'degil',                         # min dûni'l-mü'minîn (insan)
 '33:50:60': 'ilahi', '33:50:61': 'ilahi',   # kâne'nin haberi
 # sûre 33, blok 51-60
 '33:51:34': 'ilahi', '33:51:35': 'ilahi',   # kâne'nin haberi
 '33:52:25': 'ilahi',                         # kâne'nin haberi
 '33:54:11': 'ilahi',                         # kâne'nin haberi
 '33:55:30': 'ilahi',                         # kâne'nin haberi
 '33:57:10': 'degil',                         # ed-dünyâ ve'l-âhira (yurt)
 '33:58:3':  'degil', '33:58:12': 'degil',   # mü'minler · ismen mübînen (günahın sıfatı)
 '33:59:7':  'degil',                         # mü'minlerin kadınları
 '33:59:20': 'ilahi', '33:59:21': 'ilahi',   # kâne'nin haberi
 # sûre 33, blok 61-70
 '33:63:15': 'degil',                         # es-sâ'ate karîben (saatin sıfatı)
 '33:65:6':  'degil', '33:65:8': 'degil',    # velî + nasîr bulamazlar (olumsuzlanan başkası; 33:17 formülü)
 '33:68:8':  'degil',                         # la'nen kebîran (lânetin sıfatı)
 # sûre 33, blok 71-73
 '33:73:10': 'degil',                         # mü'minler (insan)
 '33:73:14': 'ilahi', '33:73:15': 'ilahi',   # kâne'nin haberi
}
