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
 # sûre 35, blok 1-10
 '35:1:24':  'ilahi',                         # inne'llâhe ... qadîr — inne'nin haberi
 '35:2:18':  'ilahi', '35:2:19': 'ilahi',     # ve huve'l-azîzu'l-hakîm — Allah'a dönen zamirin haberi
 '35:3:9':   'degil',                         # hel min hâlıkın ğayru'llâh — olumsuzlanan 'Allah'tan başka'
 '35:7:13':  'degil',                         # ecrun kebîr (ecrin sıfatı)
 '35:8:23':  'ilahi',                         # inne'llâhe alîmun — inne'nin haberi
 # sûre 35, blok 11-20
 '35:14:18': 'ilahi',                         # mislu habîr — tamlama içinde ad, göndergesi Allah (aday 999 sınır vakası, 34:6 emsali)
 '35:15:9':  'ilahi', '35:15:10': 'ilahi',   # ve'llâhu huve'l-ğaniyyu'l-hamîd — huve'nin haberi
 '35:17:5':  'degil',                         # ve mâ zâlike ... bi-azîz — 'güç, zor' işin sıfatı
 '35:19:4':  'degil',                         # el-a'mâ ve'l-basîr (gören insan)
 '35:20:4':  'degil',                         # ve le'n-nûr (ışık)
 # sûre 35, blok 21-30
 '35:22:3':  'degil',                         # el-ahyâ' (diriler, insan)
 '35:28:13': 'degil',                         # el-'ulemâ' (âlimler, insan)
 '35:28:16': 'ilahi', '35:28:17': 'ilahi',   # inna'llâha azîzun ğafûr — inne'nin haberi
 '35:30:7':  'ilahi', '35:30:8':  'ilahi',   # innehû ğafûrun şekûr — O'na dönen zamir, inne'nin haberi
 # sûre 35, blok 31-40
 '35:31:15': 'ilahi', '35:31:16': 'ilahi',   # inna'llâhe bi-ibâdihî le-habîrun basîr — inne'nin haberi
 '35:32:21': 'degil',                         # el-fadlu'l-kebîr (fadlın sıfatı)
 '35:34:10': 'ilahi', '35:34:11': 'ilahi',   # inne rabbenâ le-ğafûrun şekûr — inne'nin haberi
 '35:37:25': 'degil',                         # fe-mâ li'z-zâlimîne min nasîr — olumsuzlanan, insan göndergeli
 '35:38:3':  'ilahi', '35:38:8':  'ilahi',   # inna'llâhe âlimu ğayb... / innehû alîmun — inne'nin haberi
 # sûre 35, blok 41-45
 '35:41:13': 'degil',                         # min ehadin min ba'dih — 'kimse', olumsuzlanan
 '35:41:18': 'ilahi', '35:41:19': 'ilahi',   # innehû kâne halîmen ğafûrâ — kâne haberi
 '35:43:16': 'degil',                         # sünnete'l-evvelîn (öncekiler, insan)
 '35:44:29': 'ilahi', '35:44:30': 'ilahi',   # innehû kâne alîmen qadîrâ — kâne haberi
 '35:45:25': 'ilahi',                         # kâne bi-ibâdihî basîrâ — kâne haberi
 # sûre 36, blok 1-10
 '36:2:2':   'degil',                         # ve'l-qur'âni'l-hakîm — Kur'an'ın sıfatı
 '36:5:2':   'ilahi', '36:5:3':   'ilahi',   # tenzîle'l-azîzi'r-rahîm — tamlama içinde ad, göndergesi Allah (aday 999, üçüncü vaka)
 # sûre 36, blok 11-20
 '36:11:7':  'ilahi',                         # haşiye'r-rahmâne — bağımsız ad (nesne), göndergesi Allah; tanım dışı (aday 1019, 999 emsali)
 '36:11:12': 'degil',                         # ecrin kerîm (ödülün sıfatı)
 '36:12:14': 'degil',                         # fî imâmin mübîn (kitabın sıfatı)
 '36:15:9':  'ilahi',                         # ve mâ enzele'r-rahmânu — bağımsız ad (özne), göndergesi Allah (aday 1019)
 '36:17:5':  'degil',                         # el-belâğu'l-mübîn (tebliğin sıfatı)
 # sûre 36, blok 21-30
 '36:23:7':  'ilahi',                         # in yuridni'r-rahmânu — bağımsız ad (şart cümlesinde özne), göndergesi Allah; tanım dışı (aday 1019, üçüncü vaka)
 '36:24:5':  'degil',                         # fî dalâlin mübîn (sapıklığın sıfatı)
 # sûre 36, blok 31-40
 '36:38:7':  'ilahi', '36:38:8':  'ilahi',   # zâlike taqdîru'l-azîzi'l-alîm — tamlama içinde ad, göndergesi Allah (aday 999, dördüncü vaka)
 # sûre 36, blok 41-50
 '36:47:24': 'degil',                         # in entum illâ fî dalâlin mübîn (sapıklığın sıfatı; inkârcıların sözü)
 # sûre 36, blok 51-60
 '36:52:10': 'ilahi',                         # hâzâ mâ va'ade'r-rahmânu — bağımsız ad (özne), göndergesi Allah; tanım dışı (aday 1019, dördüncü vaka)
 '36:58:1':  'degil',                         # selâmun qavlen — esenlik sözü (nekre), ad olarak es-Selâm değil
 '36:58:5':  'ilahi',                         # min rabbin rahîm — Rab'bin sıfatı
 '36:60:13': 'degil',                         # aduvvun mübîn (düşmanın sıfatı, şeytan)
 # sûre 36, blok 61-70
 '36:69:12': 'degil',                         # zikrun ve qur'ânun mübîn (Kur'an'ın sıfatı)
 # sûre 36, blok 61-70 (ek)
 '36:70:4':  'degil',                         # men kâne hayyen — diri olan (insan; kâne haberi ama gönderge insan)
 # sûre 36, blok 71-83
 '36:77:11': 'degil',                         # hasîmun mübîn (insanın sıfatı)
 '36:79:10': 'ilahi',                         # ve huve bi-kulli halqin alîm — O'na dönen zamirin haberi
 '36:81:13': 'ilahi', '36:81:14': 'ilahi',   # ve huve'l-hallâqu'l-alîm — O'na dönen zamirin haberi
 # sûre 36, blok 71-83 (ek)
 '36:79:5':  'degil',                         # enşeehâ evvele merratin — 'ilk kez' (zaman, sıfat değil)
 # sûre 37, blok 11-20
 '37:15:6':  'degil',                         # sihrun mübîn — sihrin sıfatı (inkârcıların sözü)
 '37:17:2':  'degil',                         # âbâunâ'l-evvelûn — 'ilk atalar', insanın sıfatı (ölçüm satırı 'esmâ yok', 1022)
 # sûre 37, blok 21-30
 '37:29:5':  'degil',                         # lem tekûnû mu'minîn — insanların sıfatı (kâne haberi, gönderge insan)
 # sûre 37, blok 51-60
 '37:59:3':  'degil',                         # mevtetene'l-ûlâ — 'ilk ölümümüz' (ölümün sıfatı, zaman sırası)
 # sûre 37, blok 71-80
 '37:71:5':  'degil',                         # ekseru'l-evvelîn — 'öncekiler' (insanlar, zaman sırası)
 '37:75:5':  'ilahi',                         # fe-le-ni'me'l-mucîbûn — övülen 'biz' (Tanrı); çoğul biçim (azamet çoğulu), SINIR VAKASI (999/1019 ailesi)
 '37:78:4':  'degil',                         # fi'l-âhirîn — 'sonrakiler' (insanlar)
 '37:79:1':  'degil',                         # selâmun alâ Nûh — selam/esenlik dileği, ad değil
 # sûre 37, blok 81-90
 '37:81:4':  'degil',                         # min ibâdine'l-mu'minîn — kulların sıfatı (insan)
 '37:101:3': 'degil', # halîm gulâmın sıfatı (bi-ğulâmin halîm)
 '37:106:5': 'degil', # el-belâu'l-mubîn — belânın sıfatı
 '37:108:4': 'degil', # fi'l-âhirîn — sonrakiler (nakarat, 37:78:4 ile aynı karar)
 '37:109:1': 'degil', # selâmun alâ İbrâhîm — selam cümlesi (37:79:1 ile aynı karar)
 '37:111:4': 'degil', # mu'minîn — kulların sıfatı (37:81 nakaratı)
 '37:113:10': 'degil', # zâlimun li-nefsihî mubîn — sıfat
 '37:119:4': 'degil', # fi'l-âhirîn — sonrakiler (37:78:4 kararı)
 '37:120:1': 'degil', # selâmun alâ Mûsâ ve Hârûn — selam cümlesi (37:79:1 kararı)
 '37:122:4': 'degil', # mu'minîn — kulların sıfatı (37:111 kararı)
 '37:125:5': 'ilahi', # ahsene'l-hâlikîn — gönderge Allah (37:126 'Allâhe' bedel); çoğul sıfat tamlaması, sınır vakası (37:75:5 emsali)
 '37:126:5': 'degil', # âbâikumu'l-evvelîn — ataların sıfatı (37:17 emsali)
 '37:129:4': 'degil', # fi'l-âhirîn (37:78:4 kararı)
 '37:130:1': 'degil', # selâmun alâ il yâsîn (37:79:1 kararı)
 '37:132:4': 'degil', # mu'minîn — kulların sıfatı (37:111 kararı)
 '37:156:4': 'degil', # sultânun mubîn — delilin sıfatı
 '37:168:6': 'degil', # mine'l-evvelîn — öncekiler (37:17 emsali)
 '37:181:1': 'degil', # selâmun ale'l-murselîn — selam cümlesi (37:79:1 kararı)
}
