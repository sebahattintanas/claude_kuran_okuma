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
 # sûre 34, blok 1-10
 '34:1:14':  'degil',                         # el-âhira (yurt)
 '34:1:16':  'ilahi', '34:1:17': 'ilahi',    # 'huve'nin haberi (Allah'a dönen zamir)
 '34:2:17':  'ilahi', '34:2:18': 'ilahi',    # 'huve'nin haberi
 '34:3:11':  'ilahi',                         # Rabbî'nin sıfatı — âlimi'l-gayb
 '34:3:32':  'degil',                         # kitâbin mübîn (kitabın sıfatı)
 '34:4:10':  'degil',                         # rızkun kerîm (rızkın sıfatı)
 '34:6:15':  'ilahi', '34:6:16': 'ilahi',    # sırâtı'l-azîzi'l-hamîd — isim olarak Allah (muzâfun ileyh; sınır vakası)
 '34:8:12':  'degil',                         # bi'l-âhira (yurt)
 # sûre 34, blok 11-20
 '34:11:12': 'ilahi',                         # inne'nin haberi — innî (Allah, 1S) ... basîr
 '34:13:19': 'degil',                         # ibâdiye'ş-şekûr (insan)
 '34:15:20': 'ilahi',                         # ve Rabbun gafûr — Rab'bin sıfatı
 '34:19:19': 'degil',                         # sabbârin şekûr (insan)
 '34:20:10': 'degil',                         # mü'minler (insan)
 # sûre 34, blok 21-30
 '34:21:11': 'degil',                         # bi'l-âhira (yurt)
 '34:21:21': 'ilahi',                         # ve Rabbüke ... hafîz — Rab'bin haberi
 '34:23:21': 'ilahi', '34:23:22': 'ilahi',   # 'huve'nin haberi
 '34:24:17': 'degil',                         # dalâlin mübîn (sapıklığın sıfatı)
 '34:26:10': 'ilahi', '34:26:11': 'ilahi',   # 'huve'nin haberi
 '34:27:11': 'ilahi', '34:27:12': 'ilahi',   # huve'llâhu'l-azîzu'l-hakîm — lafzın sıfatı
 # sûre 34, blok 31-40
 '34:31:32': 'degil',                         # lekünnâ mü'minîn (insan)
 # sûre 34, blok 41-50
 '34:41:4':  'ilahi',                         # ente veliyyunâ — meleklerin Allah'a hitabı (sübhâneke)
 '34:41:13': 'degil',                         # mü'minûn (insan)
 '34:43:34': 'degil',                         # sihrun mübîn (sihrin sıfatı)
 '34:47:17': 'ilahi',                         # ve huve ... şehîd — Allah'a dönen zamirin haberi
 '34:50:15': 'ilahi', '34:50:16': 'ilahi',   # innehû semî'un karîb
 # sûre 34, blok 51-54
 '34:51:10': 'degil',                         # mekânin karîb (mekânın sıfatı)
}
