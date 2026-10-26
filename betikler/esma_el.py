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
 '38:7:6': 'degil', # fi'l-milleti'l-âhira — dinin sıfatı (son/öteki)
 '38:9:6': 'ilahi', # rabbike'l-azîz — Rab'bin sıfatı
 '38:9:7': 'ilahi', # rabbike'l-vehhâb — Rab'bin sıfatı
 '38:35:10': 'degil', # lâ yenbeğî li-ehadin min ba'dî — 'kimse' (olumsuz bağlamda belirsiz zamir), ilahi gönderge yok
 '38:35:15': 'ilahi', # inneke ente'l-vehhâb — Rab'be hitap (2MS), haber
 '38:65:11': 'ilahi', # illa'llâhu'l-vâhidu'l-qahhâr — lafzın sıfatı
 '38:66:6': 'ilahi', # rabbu's-semâvâti … el-azîz — Rab'bin sıfatı
 '38:66:7': 'ilahi', # … el-ğaffâr — Rab'bin sıfatı
 '38:70:8': 'degil', # nezîrun mubîn — uyarıcının (1S) sıfatı
 '38:71:6': 'ilahi', # innî hâliqun beşeren — inne'nin haberi, 1S konuşan Rab (34:11 emsali)
    '39:1:5': 'ilahi',  # lafzın sıfatı (el-azîz)
    '39:1:6': 'ilahi',  # lafzın sıfatı (el-hakîm)
    '39:3:9': 'degil',  # evliyâ: edinilen dostlar, isim değil
    '39:4:16': 'ilahi',  # lafzın sıfatı (el-vâhidu'l-qahhâr)
    '39:5:22': 'ilahi',  # elâ huve'l-azîz — huve Allah'a döner
    '39:5:23': 'ilahi',  # elâ huve'l-ğaffâr — huve Allah'a döner
    '39:7:5': 'ilahi',  # inne'llâhe ğaniyyun — inne haberi
    '39:7:29': 'ilahi',  # innehû alîm — inne haberi, zamir Rab'a döner
    '39:9:9': 'degil',  # el-âhira: âhiret sıfatı, isim değil
    '39:12:4': 'degil',  # evvele'l-muslimîn — 'ilk', isim değil
    '39:15:19': 'degil',  # el-husrânu'l-mubîn — husrânın sıfatı
    '39:22:8': 'degil',  # alâ nûrin min rabbih — Rab'den gelen ışık, isim değil
    '39:22:20': 'degil',  # dalâlin mubîn — sapkınlığın sıfatı
    '39:23:34': 'degil',  # fe-mâ lehû min hâd — olumsuz nekre, 'yol gösteren yok'
    '39:26:8': 'degil',  # el-âhira — âhiret sıfatı
    '39:36:15': 'degil',  # fe-mâ lehû min hâd — olumsuz nekre (39:23 emsali)
    '39:37:10': 'ilahi',  # e-leyse'llâhu bi-azîzin — lafzın haberi
    '39:41:18': 'degil',  # ve mâ ente aleyhim bi-vekîl — 2MS'ye olumsuz haber
    '39:45:10': 'degil',  # el-âhira — âhiret sıfatı
    '39:46:6': 'ilahi',  # Allâhumme … âlime'l-ğayb — nidâ edilen Allah'ın sıfatı
    '39:53:19': 'ilahi',  # innehû huve'l-ğafûr — zamir Allah'a döner
    '39:53:20': 'ilahi',  # er-rahîm — aynı terkip
    '39:60:14': 'degil',  # li'l-mutekebbirîn — büyüklenen insanlar (çoğul)
    '39:62:2': 'ilahi',  # Allâhu hâliqu kulli şey' — lafzın haberi
    '39:62:9': 'ilahi',  # ve huve alâ kulli şey'in vekîl — zamir Allah'a döner
    '39:66:6': 'degil',  # mine'ş-şâkirîn — 2MS'ye emir, şükredenler (insanlar, çoğul)
    '39:69:3': 'degil',  # bi-nûri rabbihâ — Rabbin nuru (Rab'dan ışık; nûr emsali)
    '39:69:9': 'degil',  # ve'ş-şuhedâ — şahitler (insanlar, çoğul)
    '39:72:9': 'degil',  # mesve'l-mutekebbirîn — büyüklenenler (insanlar, çoğul)
    '39:73:16': 'degil',  # selâmun aleykum — bekçilerin selamlaması (esenlik dileği)
    # sûre 40 (Ğâfir) blok 1-10 (2026-10-11)
    '40:2:5': 'ilahi',  # mina'llâhi'l-azîz — lafzın sıfatı
    '40:2:6': 'ilahi',  # el-alîm — aynı terkip
    '40:8:15': 'ilahi',  # inneke ente'l-azîz — meleklerin Rabbe hitabı, zamir Rab'be döner
    '40:8:16': 'ilahi',  # el-hakîm — aynı terkip
    # sûre 40 (Ğâfir) blok 11-20 (2026-10-11)
    '40:12:14': 'ilahi',  # fe'l-hukmu li'llâhi'l-aliyy — lafzın sıfatı
    '40:12:15': 'ilahi',  # el-kebîr — aynı terkip
    '40:16:15': 'ilahi',  # li'llâhi'l-vâhidi'l-qahhâr — lafzın sıfatı
    '40:20:14': 'ilahi',  # inna'llâhe huve's-semî' — zamir lafza döner
    '40:20:15': 'ilahi',  # el-basîr — aynı terkip
    # sûre 40 (Ğâfir) blok 21-30 (2026-10-11)
    '40:22:11': 'ilahi',  # innehû qaviyyun şedîdu'l-iqâb — zamir lafza döner
    '40:23:6': 'degil',  # sultânin mubîn — Mûsâ'ya verilen delilin sıfatı
    '40:27:9': 'degil',  # min kulli mutekebbir — büyüklenen insan (nekre)
    '40:28:3': 'degil',  # racülun mu'min — inanan adam
    '40:29:5': 'degil',  # zâhirîne fi'l-ard — üstün olanlar (insanlar, çoğul)
    # sûre 40 (Ğâfir) blok 31-40 (2026-10-11)
    '40:33:16': 'degil',  # fe-mâ lehû min hâd — olumsuz nekre (39:23 emsali)
    '40:35:22': 'degil',  # kulli qalbi mutekebbir — büyüklenen kalp (insan)
    '40:35:23': 'degil',  # cebbâr — aynı terkip, kalbin sıfatı
    '40:39:8': 'degil',  # el-âhira — âhiret sıfatı
    '40:40:16': 'degil',  # ve huve mu'min — iman eden insan
    # sûre 40 (Ğâfir) blok 41-50 (2026-10-11)
    '40:42:14': 'ilahi',  # ed'ûkum ile'l-azîz — çağrılan Allah'ın sıfatı
    '40:42:15': 'ilahi',  # el-ğaffâr — aynı terkip
    '40:43:13': 'degil',  # fi'l-âhira — âhiret sıfatı
    '40:44:11': 'ilahi',  # inna'llâhe basîrun bi'l-ibâd — lafzın haberi
    # sûre 40 (Ğâfir) blok 51-60 (2026-10-11)
    '40:56:22': 'ilahi',  # innehû huve's-semî' — zamir Allah'a döner
    '40:56:23': 'ilahi',  # el-basîr — aynı terkip
    '40:58:4': 'degil',  # el-a'mâ ve'l-basîr — gören (insan), körün karşıtı
    # sûre 40 (Ğâfir) blok 61-70 (2026-10-11)
    '40:62:4': 'ilahi',  # zâlikumu'llâhu rabbukum hâliqu kulli şey' — Allah'ın sıfatı
    '40:65:2': 'ilahi',  # huve'l-hayy — zamir Allah'a döner (40:64)
    # sûre 40 (Ğâfir) blok 71-80 (2026-10-11)
    '40:76:8': 'degil',  # fe-bi'se mesve'l-mutekebbirîn — büyüklenenler (insan), çoğul
    # sûre 41 (Fussilet) blok 1-10 (2026-10-11)
    '41:2:3': 'ilahi',  # tenzîlun mine'r-rahmân — indirenin adı
    '41:2:4': 'ilahi',  # er-rahîm — aynı terkip
    '41:7:6': 'degil',  # bi'l-âhira — âhiret (son yurt), esmâ 'el-âhir' değil
    # sûre 41 (Fussilet) blok 11-20 (2026-10-11)
    '41:12:18': 'ilahi',  # zâlike taqdîru'l-azîz — takdirin sahibi
    '41:12:19': 'ilahi',  # el-alîm — aynı terkip
    '41:16:15': 'degil',  # ve le-azâbu'l-âhira — âhiret
    # sûre 41 (Fussilet) blok 21-30 (2026-10-11)
    '41:21:15': 'degil',  # halaqakum evvele merra — ilk kez (zarf), esmâ 'el-evvel' değil
    # sûre 41 (Fussilet) blok 31-40 (2026-10-11)
    '41:31:2': 'degil',  # nahnu evliyâukum — meleklerin sözü, dostlarınız (çoğul)
    '41:31:7': 'degil',  # ve fi'l-âhira — âhiret
    '41:32:3': 'ilahi',  # nuzulen min ğafûrin rahîm
    '41:32:4': 'ilahi',  # aynı terkip
    '41:34:16': 'degil',  # ke-ennehu veliyyun hamîm — sıcak dost (benzetme)
    '41:36:10': 'ilahi',  # innehu huve's-semî'u'l-alîm
    '41:36:11': 'ilahi',  # aynı terkip
    '41:39:22': 'ilahi',  # innehu alâ kulli şey'in qadîr
    '41:40:26': 'ilahi',  # innehu bi-mâ ta'melûne basîr
    # sûre 41 (Fussilet) blok 41-50 (2026-10-11)
    '41:41:9': 'degil',  # ve innehû le-kitâbun azîz — kitabın sıfatı
    '41:42:12': 'ilahi',  # tenzîlun min hakîmin hamîd
    '41:42:13': 'ilahi',  # aynı terkip
    '41:47:28': 'degil',  # mâ minnâ min şehîd — şahit (çağrılanların sözü)
    # sûre 41 (Fussilet) blok 51-54 (2026-10-11)
    '41:53:19': 'ilahi',  # e-ve lem yekfi bi-rabbike ennehû alâ kulli şey'in şehîd
    '41:54:12': 'ilahi',  # e-lâ innehû bi-kulli şey'in muhît
    # sûre 42 (Şûrâ) blok 1-10 (2026-10-11)
    '42:3:9': 'ilahi',  # allâhu'l-azîzu'l-hakîm
    '42:3:10': 'ilahi',  # aynı terkip
    '42:4:9': 'ilahi',  # ve huve'l-aliyyu'l-azîm
    '42:5:18': 'ilahi',  # inne'llâhe huve'l-ğafûru'r-rahîm
    '42:5:19': 'ilahi',  # aynı terkip
    '42:6:5': 'degil',  # min dûnihî evliyâ — edinilen dostlar (çoğul)
    '42:6:7': 'ilahi',  # allâhu hafîzun aleyhim
    '42:6:12': 'degil',  # ve mâ ente aleyhim bi-vekîl — muhatap (2MS)
    '42:8:17': 'degil',  # mâ lehum min veliyyin — olumsuz, genel
    '42:8:19': 'degil',  # ve lâ nasîr — aynı
    '42:9:5': 'degil',  # min dûnihî evliyâ — edinilen dostlar
    '42:9:8': 'ilahi',  # fe'llâhu huve'l-veliyy
    '42:9:16': 'ilahi',  # ve huve alâ kulli şey'in qadîr
    # sûre 42 (Şûrâ) blok 11-20 (2026-10-12)
    '42:11:18': 'ilahi',  # ve huve's-semî'u'l-basîr
    '42:11:19': 'ilahi',  # aynı terkip
    '42:12:13': 'ilahi',  # innehû bi-kulli şey'in alîm
    '42:17:11': 'degil',  # la'alle's-sâ'ate qarîb — saatin yakınlığı
    '42:19:2': 'ilahi',  # allâhu latîfun bi-ibâdih
    '42:19:8': 'ilahi',  # ve huve'l-qaviyyu'l-azîz
    '42:19:9': 'ilahi',  # aynı terkip
    '42:20:5': 'degil',  # harse'l-âhira — âhiret
    '42:20:20': 'degil',  # fi'l-âhira — âhiret
    # sûre 42 (Şûrâ) blok 21-30 (2026-10-12)
    '42:22:24': 'degil',  # zâlike huve'l-fadlu'l-kebîr — lütfun sıfatı
    '42:23:28': 'ilahi',  # inne'llâhe ğafûrun şekûr
    '42:23:29': 'ilahi',  # aynı terkip
    '42:24:20': 'ilahi',  # innehû alîmun bi-zâti's-sudûr
    '42:27:16': 'ilahi',  # innehû bi-ibâdihî habîrun basîr
    '42:27:17': 'ilahi',  # aynı terkip
    '42:28:12': 'ilahi',  # ve huve'l-veliyyu'l-hamîd
    '42:28:13': 'ilahi',  # aynı terkip
    '42:29:16': 'ilahi',  # ve huve alâ cem'ihim … qadîr
'42:31:12': 'degil',  # 'min dûni'llâhi min veliyy' — Allah'tan başka dost yok; olumsuzlanan sıfat (42:8 emsali)
'42:31:14': 'degil',  # 've lâ nasîr' — olumsuzlanan yardımcı (42:8 emsali)
'42:33:15': 'degil',  # 'li-kulli sabbârin şekûr' — insan sıfatı
'42:44:7': 'degil',  # 'fe-mâ lehû min veliyy' — olumsuzlanan dost
'42:46:5': 'degil',  # 'min evliyâe yansurûnehum' — olumsuzlanan dostlar
'42:48:6': 'degil',  # 'fe-mâ erselnâke aleyhim hafîzâ' — muhatap için, olumsuz
'42:50:10': 'ilahi',  # innehû alîmun qadîr
'42:50:11': 'ilahi',  # aynı terkip
'42:51:21': 'ilahi',  # innehû aliyyun hakîm
'42:51:22': 'ilahi',  # aynı terkip
'42:52:16': 'degil',  # 'ce'alnâhu nûran' — vahyedilen ruh/kitap için
    # sûre 43 (Zuhruf) blok 1-10 (2026-10-12)
'43:2:2': 'degil',  # ve'l-kitâbi'l-mubîn — kitabın sıfatı (34:3, 36:12 emsali)
'43:4:6': 'degil',  # innehû fî ummi'l-kitâbi ledeynâ le-aliyyun — zamir 'hû' kitap/Kur'an (43:2-3); kitabın sıfatı (41:41 emsali)
'43:4:7': 'degil',  # aynı terkip — kitabın sıfatı (36:2 'el-qur'âni'l-hakîm' emsali)
'43:6:6': 'degil',  # fi'l-evvelîn — öncekiler (insanlar)
'43:8:7': 'degil',  # meselu'l-evvelîn — öncekiler (insanlar)
'43:9:9': 'ilahi',  # halaqahunne'l-azîzu'l-alîm — yaratma fiilinin fâili; alıntı içinde (sorulanların cevabı)
'43:9:10': 'ilahi',  # aynı terkip
    # sûre 43 (Zuhruf) blok 11-20 (2026-10-12)
'43:15:9': 'degil',  # inne'l-insâne le-kefûrun mubîn — insanın sıfatı
'43:17:3': 'degil',  # ehaduhum — 'onlardan biri'
'43:17:6': 'ilahi',  # bi-mâ darabe li'r-rahmâni meselen — bağımsız ad, göndergesi Allah (aday 1019, 36:11 emsali)
'43:18:9': 'degil',  # ve huve fi'l-hisâmi ğayru mubîn — olumsuzlanan, insan sıfatı
'43:19:6': 'ilahi',  # ibâdu'r-rahmân — bağımsız ad, göndergesi Allah (aday 1019)
'43:20:4': 'ilahi',  # lev şâe'r-rahmânu — bağımsız ad (özne), alıntı içinde (onların sözü)
    # sûre 43 (Zuhruf) blok 21-30 (2026-10-12)
'43:29:9': 'degil',  # ve rasûlun mubîn — elçinin sıfatı
    # sûre 43 (Zuhruf) blok 31-40 (2026-10-12)
'43:33:10': 'ilahi',  # li-men yekfuru bi'r-rahmân — bağımsız ad, göndergesi Allah (aday 1019)
'43:35:9': 'degil',  # ve'l-âhiratu inde rabbike — âhiret (yurt), sıfat değil
'43:36:5': 'ilahi',  # an zikri'r-rahmân — bağımsız ad, göndergesi Allah (aday 1019)
'43:40:11': 'degil',  # fî dalâlin mubîn — sapkınlığın sıfatı
    # sûre 43 (Zuhruf) blok 41-50 (2026-10-12)
'43:42:7': 'ilahi',  # fe-innâ aleyhim muqtedirûn — 1P (azamet çoğulu) yüklemi; SINIR VAKASI (37:75:5 emsali)
'43:45:11': 'ilahi',  # min dûni'r-rahmân — bağımsız ad, göndergesi Allah (aday 1019)
    # sûre 43 (Zuhruf) blok 51-60 (2026-10-12)
'43:56:4': 'degil',  # mesel li'l-âhirîn — sonrakiler (insanlar)
    # sûre 43 (Zuhruf) blok 61-70 (2026-10-12)
'43:62:7': 'degil',  # aduwwun mubîn — şeytan sıfatı
    # sûre 43 (Zuhruf) blok 81-89 (2026-10-13)
'43:81:4': 'ilahi',  # in kâne li'r-rahmâni veled — bağımsız ad, göndergesi Allah (aday 1019)
'43:81:7': 'degil',  # fe-ene evvelu'l-âbidîn — kulluk edenlerin ilki (1S, insan)
'43:84:10': 'ilahi',  # ve huve'l-hakîmu'l-alîm — zamir 'huve' (43:84 başı 'ellezî fi's-semâi ilâh')
'43:84:11': 'ilahi',  # aynı terkip
'43:89:4': 'degil',  # ve qul selâm — selam sözü (nekre), ad olarak es-Selâm değil (36:58 kararı)
    # sûre 44 (Duhân) blok 1-10 (2026-10-13)
'44:2:2': 'degil',  # ve'l-kitâbi'l-mubîn — kitabın sıfatı (43:2 kararı)
'44:4:5': 'degil',  # kullu emrin hakîm — işin (emr) sıfatı
'44:6:6': 'ilahi',  # innehû huve's-semî'u'l-alîm — zamir 'huve' (Rab)
'44:6:7': 'ilahi',  # aynı terkip
'44:8:10': 'degil',  # âbâikumu'l-evvelîn — önceki atalar (insanlar)
'44:10:6': 'degil',  # bi-duhânin mubîn — dumanın sıfatı
    # sûre 44 (Duhân) blok 11-20 (2026-10-14)
'44:12:6': 'degil',  # innâ mu'minûn — azabın kalkmasını isteyenlerin sözü (insanlar)
'44:13:7': 'degil',  # rasûlun mubîn — elçinin sıfatı
'44:17:8': 'degil',  # rasûlun kerîm — elçinin sıfatı
'44:19:9': 'degil',  # bi-sultânin mubîn — delilin sıfatı
    # sûre 44 (Duhân) blok 21-30 (2026-10-14)
'44:26:3': 'degil',  # ve maqâmin kerîm — makamın (yerin) sıfatı
    # sûre 44 (Duhân) blok 31-40 (2026-10-14)
'44:33:7': 'degil',  # belâun mubîn — sınavın sıfatı
'44:35:5': 'degil',  # mevtetune'l-ûlâ — ilk ölüm (sıfat)
    # sûre 44 (Duhân) blok 41-50 (2026-10-14)
'44:41:4': 'degil',  # lâ yuğnî mevlen an mevlâ — dost / yakın (insan)
'44:41:6': 'degil',  # aynı terkip — ikinci 'mevlâ' (insan)
'44:42:7': 'ilahi',  # innehû huve'l-azîzu'r-rahîm — zamir 'huve', 44:42 lafız
'44:42:8': 'ilahi',  # aynı terkip
'44:49:4': 'degil',  # zuq inneke ente'l-azîzu'l-kerîm — azaptakine hitap (insan; alay işaretsiz), aday 1041 alanı
'44:49:5': 'degil',  # aynı terkip
    # sûre 44 (Duhân) blok 51-59 (2026-10-14)
'44:56:7': 'degil',  # ille'l-mevtete'l-ûlâ — 'ilk ölüm' sıfatı (ölüm), Allah değil
    # sûre 45 (Câsiye) blok 1-10 (2026-10-14)
'45:2:5': 'ilahi',  # mina'llâhi'l-azîzi'l-hakîm — lafzın sıfatı
'45:2:6': 'ilahi',  # aynı terkip
'45:3:6': 'degil',  # li'l-mu'minîn — inananlar (insan)
'45:10:16': 'degil',  # min dûni'llâhi evliyâ' — edinilen dostlar
    # sûre 45 (Câsiye) blok 11-20 (2026-10-14)
'45:19:11': 'degil',  # ba'duhum evliyâu ba'd — zâlimler birbirinin dostu (insan), aday 1041 alanı
'45:19:14': 'ilahi',  # va'llâhu veliyyu'l-muttaqîn — lafzın haberi, aday 1041 alanı
    # sûre 45 (Câsiye) blok 21-30 (2026-10-14)
'45:30:13': 'degil',  # zâlike huve'l-fevzu'l-mubîn — kurtuluşun sıfatı
    # sûre 45 (Câsiye) blok 31-37 (2026-10-14)
'45:37:7': 'ilahi',  # ve huve'l-azîzu'l-hakîm — zamir 'huve' (45:36 lafız, Rab); 45:2 ile aynı ikili
'45:37:8': 'ilahi',  # aynı terkip
    # sûre 46 (Ahkâf) blok 1-10 (2026-10-14)
'46:2:5': 'ilahi',  # mina'llâhi'l-azîzi'l-hakîm — lafzın sıfatı (45:2 ile aynı)
'46:2:6': 'ilahi',  # aynı terkip
'46:7:14': 'degil',  # sihrun mubîn — büyünün sıfatı (söyleyenlerin sözü)
'46:8:20': 'ilahi',  # kefâ bihî şehîden — 'bihî' lafız (46:8 'mina'llâh')
'46:8:24': 'ilahi',  # ve huve'l-ğafûru'r-rahîm — zamir 'huve'
'46:8:25': 'ilahi',  # aynı terkip
'46:9:24': 'degil',  # nezîrun mubîn — uyarıcının sıfatı (1S konuşan)
    # sûre 46 (Ahkâf) blok 11-20 (2026-10-14)
'46:17:28': 'degil',  # esâtîru'l-evvelîn — öncekilerin masalları (inkârcının sözü)
    # sûre 46 (Ahkâf) blok 31-35 (2026-10-14)
'46:32:14': 'degil',  # min dûnihî evliyâ' — Allah'tan başka dostlar (yokluğu söyleniyor)
'46:32:18': 'degil',  # fî dalâlin mubîn — sapıklığın sıfatı
'46:33:22': 'ilahi',  # innehû alâ kulli şey'in qadîr — zamir 'hû' (aynı ayette lafız)
    # sûre 47 (Muhammed) blok 11-20 (2026-10-14)
'47:11:4': 'ilahi',  # enna'llâhe mevle'llezîne âmenû — lafzın haberi, aday 1041 alanı (47:11:10 ile)
'47:11:10': 'degil',  # ve enne'l-kâfirîne lâ mevlâ lehum — inkâr edenlere mevlâ yok (yokluğu söyleniyor; 46:32 emsali)
'47:19:9': 'degil',  # ve li'l-mu'minîne ve'l-mu'minât — inananlar (insan; 45:3 emsali)
    # sûre 47 (Muhammed) blok 31-38 (2026-10-15)
'47:38:18': 'ilahi',  # ve'llâhu'l-ğaniyyu ve entumu'l-fuqarâ' — lafzın haberi; karşıtı 'fuqarâ'' (insan)
    # sûre 48 (Fetih) blok 1-10 (2026-10-15)
'48:1:5': 'degil',  # fethen mubînâ — fethin sıfatı (1P konuşan)
'48:3:4': 'degil',  # nasran azîzâ — yardımın sıfatı (masdarın sıfatı; aday 1041 alanı)
'48:4:7': 'degil',  # fî qulûbi'l-mu'minîn — inananlar (insan)
'48:4:18': 'ilahi',  # ve kâna'llâhu alîmen hakîmâ — lafzın haberi
'48:4:19': 'ilahi',  # aynı terkip
'48:5:2': 'degil',  # el-mu'minîne ve'l-mu'minât — inananlar (insan)
'48:7:7': 'ilahi',  # ve kâna'llâhu azîzen hakîmâ — lafzın haberi
'48:7:8': 'ilahi',  # aynı terkip
    # sûre 48 (Fetih) blok 11-20 (2026-10-15)
'48:11:37': 'ilahi',  # bel kâna'llâhu bimâ ta'melûne habîrâ — lafzın haberi
'48:12:7': 'degil',  # er-rasûlu ve'l-mu'minûn — inananlar (insan)
'48:14:13': 'ilahi',  # ve kâna'llâhu ğafûran rahîmâ — lafzın haberi
'48:14:14': 'ilahi',  # aynı terkip
'48:18:5': 'degil',  # ani'l-mu'minîn — inananlar (insan)
'48:18:19': 'degil',  # fethan qarîbâ — fethin sıfatı
'48:19:6': 'ilahi',  # ve kâna'llâhu azîzen hakîmâ — lafzın haberi (48:7 ile aynı)
'48:19:7': 'ilahi',  # aynı terkip
'48:20:15': 'degil',  # âyeten li'l-mu'minîn — inananlar (insan)
    # sûre 48 (Fetih) blok 21-29 (2026-10-15)
'48:21:14': 'ilahi',  # ve kâna'llâhu alâ kulli şey'in qadîrâ — lafzın haberi
'48:22:10': 'degil',  # lâ yecidûne veliyyen — olumsuzlanan başkası (33:65 formülü)
'48:22:12': 'degil',  # ve lâ nasîrâ — aynı
'48:24:19': 'ilahi',  # ve kâna'llâhu bimâ ta'melûne basîrâ — lafzın haberi
'48:25:15': 'degil',  # ricâlun mu'minûn — inananlar (insan)
'48:26:16': 'degil',  # ve ale'l-mu'minîn — inananlar (insan)
'48:26:28': 'ilahi',  # ve kâna'llâhu bi-kulli şey'in alîmâ — lafzın haberi
'48:27:28': 'degil',  # fethan qarîbâ — fethin sıfatı (48:18 emsali)
'48:28:14': 'ilahi',  # ve kefâ bi'llâhi şehîdâ — lafız için temyiz
'48:29:9': 'degil',  # ruhamâ'u beynehum — beraberindekilerin sıfatı (insan)
    # sûre 49 (Hucurât) blok 1-10 (2026-10-16)
'49:1:14': 'ilahi',  # inne'llâhe semî'un alîm — lafzın haberi
'49:1:15': 'ilahi',  # aynı terkip
'49:5:11': 'ilahi',  # ve'llâhu ğafûrun rahîm — lafzın haberi
'49:5:12': 'ilahi',  # aynı terkip
'49:8:6': 'ilahi',  # ve'llâhu alîmun hakîm — lafzın haberi
'49:8:7': 'ilahi',  # aynı terkip
'49:9:4': 'degil',  # tâ'ifetâni mine'l-mu'minîn — inananlar (insan)
'49:10:2': 'degil',  # innema'l-mu'minûne ihveh — inananlar (insan)
    # sûre 49 (Hucurât) blok 11-18 (2026-10-16)
'49:12:19': 'degil',  # e-yuhibbu ehadukum — 'biriniz' (insan, sayı)
'49:12:30': 'ilahi',  # inne'llâhe tevvâbun rahîm — lafzın haberi
'49:12:31': 'ilahi',  # aynı terkip
'49:13:19': 'ilahi',  # inne'llâhe alîmun habîr — lafzın haberi
'49:13:20': 'ilahi',  # aynı terkip
'49:14:26': 'ilahi',  # inne'llâhe ğafûrun rahîm — lafzın haberi
'49:14:27': 'ilahi',  # aynı terkip
'49:15:2': 'degil',  # innema'l-mu'minûn — inananlar (insan)
'49:16:16': 'ilahi',  # ve'llâhu bi-kulli şey'in alîm — lafzın haberi
'49:18:8': 'ilahi',  # ve'llâhu basîrun bimâ ta'melûn — lafzın haberi
    # sûre 50 (Qâf) blok 1-10 (2026-10-16)
'50:1:3': 'degil',  # ve'l-Qur'âni'l-mecîd — Kur'ân'ın sıfatı
'50:4:9': 'degil',  # kitâbun hafîz — kitabın sıfatı
'50:15:3': 'degil',  # bi'l-halqi'l-evvel — yaratmanın sıfatı (ilk yaratma)
'50:18:7': 'degil',  # ledeyhi raqîbun atîd — yanındaki gözetleyici, adsız; ilâhî ad değil
'50:21:6': 'degil',  # sâiqun ve şehîd — nefisle gelen adsız tanık
'50:32:6': 'degil',  # li-kulli evvâbin hafîz — koruyan kul, insanın sıfatı
'50:33:3': 'ilahi',  # haşiye'r-rahmâne bi'l-ğayb — ilâhî ad (meful)
'50:34:2': 'degil',  # udhulûhâ bi-selâm — esenlikle girme
'50:37:13': 'degil',  # ve huve şehîd — kulak veren kişi hazır / tanık
'50:41:7': 'degil',  # min mekânin qarîb — yerin sıfatı
'50:45:8': 'degil',  # ve mâ ente aleyhim bi-cebbâr — muhatap 2MS için olumsuzlanan
'51:25:5': 'degil',  # fe-qâlû selâmen — konukların selamı
'51:25:7': 'degil',  # qâle selâmun — İbrâhîm'in selamı
'51:28:9': 'degil',  # bi-ğulâmin alîm — müjdelenen oğlanın sıfatı
'51:30:7': 'ilahi',  # innehû huve'l-hakîm — Rab'bin sıfatı
'51:30:8': 'ilahi',  # el-alîm — Rab'bin sıfatı
'51:35:6': 'degil',  # mine'l-mu'minîn — Lût'un evindeki inananlar
'51:38:8': 'degil',  # bi-sultânin mubîn — delilin sıfatı
'51:50:8': 'degil',  # nezîrun mubîn — uyarıcının (1S) sıfatı
# sûre 51 blok 51-60
'51:51:11': 'degil',  # 'nezîrun mubîn' — uyarıcının sıfatı (51:50 ile aynı kalıp)
'51:55:5': 'degil',   # 'el-mu'minîn' — insanlar
'51:58:4': 'ilahi',   # 'inna'llâhe huve'r-razzâq' — lafzın yüklemi
'51:58:7': 'ilahi',   # 'zu'l-quvveti'l-metîn' — lafzın sıfatı
# sûre 52 blok 21-30
'52:28:8': 'ilahi',   # 'innehû huve'l-berr' — 'ned'ûhu' ile çağrılanın sıfatı; 52:27 lafız 'fe-menne'llâhu'
'52:28:9': 'ilahi',   # 'er-rahîm' — aynı göndergenin ikinci sıfatı
# sûre 52 blok 31-40
'52:35:8': 'degil',   # 'em humu'l-hâliqûn' — özne 'hum' (soru: kendileri mi yaratıcı); ilâhî ad değil
'52:38:9': 'degil',   # 'bi-sultânin mubîn' — delilin sıfatı
# sûre 53 blok 21-30
'53:25:2': 'degil',   # 'fe-li'llâhi'l-âhiratu' — âhiret (son yurt); lafzın yüklemi değil, mülk konusu
'53:25:3': 'degil',   # 've'l-ûlâ' — ilk (dünya); âhiret ile çift
'53:27:5': 'degil',   # 'lâ yu'minûne bi'l-âhira' — inanılmayan âhiret
# sûre 53 blok 31-40
'53:32:10': 'ilahi',  # 'inne rabbeke vâsi'u'l-mağfira' — Rab'bin yüklemi (izâfetle)
# sûre 53 blok 41-50
'53:50:4': 'degil',   # 'âden el-ûlâ' — Âd kavminin sıfatı (önceki)
# sûre 53 blok 51-62
'53:56:5': 'degil',   # 'mine'n-nuzuri'l-ûlâ' — önceki uyarıcıların sıfatı
# sûre 54 blok 41-50
'54:42:6': 'ilahi',   # 'ahze azîzin muqtedir' — nekre, mef'ûl-i mutlak izâfeti; yakalayan 1P ('fe-ehaznâhum') — gönderge 1P (sınır vakası, nekre)
'54:42:7': 'ilahi',   # 'muqtedir' — aynı göndergenin ikinci sıfatı
# sûre 54 blok 51-55
'54:53:3': 'degil',   # 'kullu sağîrin ve kebîr' — küçük ve büyük her şey (nekre, sayılan işler); ilâhî ad değil
'54:55:5': 'ilahi',   # ''inde melîkin muqtedir' — katında oturulan; nekre, gönderge Allah (sınır vakası, 54:42 emsali)
'54:55:6': 'ilahi',   # 'muqtedir' — aynı göndergenin ikinci sıfatı
# sûre 55 blok 1-10
'55:1:1': 'ilahi',    # 'er-rahmân' — tek kelimelik ayet; 55:2-4 fiillerinin öznesi (allema, halaqa)
# sûre 56 blok 11-20
'56:13:3': 'degil',   # 'mine'l-evvelîn' — öncekiler (insanlar; 56:14 'mine'l-âhirîn' karşılığı); ölçüm satırında görünmüyor, esma_kayit e_oto (aday 1022)
'56:14:3': 'degil',   # 'mine'l-âhirîn' — sonrakiler (insanlar; 56:13 'mine'l-evvelîn' karşılığı), 37:78:4 emsali
# sûre 56 blok 21-30
'56:26:3': 'degil',   # 'illâ qîlen selâmen' — işitilen söz: selam (nekre), ad olarak es-Selâm değil (36:58 kararı)
'56:26:4': 'degil',   # 'selâmen' tekrarı — aynı söz (56:26:3 kararı)
# sûre 56 blok 31-40
'56:39:3': 'degil',   # 'sulletun mine'l-evvelîn' — öncekiler (insanlar; 56:13:3 kararı)
'56:40:3': 'degil',   # 've sulletun mine'l-âhirîn' — sonrakiler (insanlar; 56:14:3 kararı)
# sûre 56 blok 41-50
'56:44:4': 'degil',   # 'lâ bâridin ve lâ kerîm' — 'yahmûm' gölgesinin olumsuzlanan sıfatı; ilâhî ad değil
'56:48:2': 'degil',   # 'âbâ'unâ'l-evvelûn' — ilk atalar, insanın sıfatı (37:17:2 kararı; ölçüm satırında 'esmâ yok' — 1022)
'56:49:3': 'degil',   # 'inne'l-evvelîne' — öncekiler (insanlar; 56:13:3 kararı)
'56:49:4': 'degil',   # 've'l-âhirîn' — sonrakiler (insanlar; 56:14:3 kararı)
# sûre 56 blok 51-60
'56:59:5': 'ilahi',   # 'em nahnu'l-hâliqûn' — 1P (azamet çoğulu) yüklemi, 'e-entum tahluqûnehû' sorusunun karşıtı; SINIR VAKASI (43:42:7 emsali; 52:35:8 'em humu'l-hâliqûn' değil kararının karşıtı)
# sûre 56 blok 61-70
'56:62:4': 'degil',   # 'en-neş'ete'l-ûlâ' — ilk yaratılış, 'neş'e'nin sıfatı (36:79:5 'evvele merra' emsali); ölçüm satırında 'esmâ yok' (1022)
# sûre 56 blok 71-80
'56:77:3': 'degil',   # 'innehû le-qur'ânun kerîm' — Kur'ân'ın sıfatı (nekre); ilâhî ad değil (56:44:4 'kerîm' sıfat kararı)
# sûre 56 blok 91-96
'56:91:1': 'degil',   # 'fe-selâmun leke min ashâbi'l-yemîn' — nekre selâm / esenlik sözü (selamlama); ilâhî ad değil (56:26:3, 37:79:1 kararları)
# sûre 57 blok 1-6
'57:1:8': 'ilahi',    # 've huve'l-azîzu'l-hakîm' — 'huve' göndergesi aynı ayette lafız 'lillâhi'
'57:1:9': 'ilahi',    # 'el-hakîm' — aynı göndergenin ikinci sıfatı (57:1:8 kararı)
'57:2:11': 'ilahi',   # 've huve alâ kulli şey'in qadîr' — 'huve' 57:2 'lehû mulku's-semâvât' sahibi (57:1 lafız)
'57:3:2': 'ilahi',    # 'huve'l-evvel' — 'huve' 57:1-2 göndergesi; insan 'evvelîn' kararlarından (56:13:3) ayrı
'57:3:3': 'ilahi',    # 've'l-âhir' — aynı gönderge (57:3:2 kararı); insan 'âhirîn' (56:14:3) ayrı
'57:3:4': 'ilahi',    # 've'z-zâhir' — aynı gönderge
'57:3:5': 'ilahi',    # 've'l-bâtın' — aynı gönderge
'57:3:9': 'ilahi',    # 've huve bi-kulli şey'in alîm' — aynı gönderge
'57:4:36': 'ilahi',   # 'va'llâhu bimâ ta'melûne basîr' — lafzın haberi
'57:6:10': 'ilahi',   # 've huve alîmun bi-zâti's-sudûr' — 'huve' 57:5 lafız 've ile'llâhi'
# sûre 57 blok 7-10
'57:7:15': 'degil',   # 'lehum ecrun kebîr' — ecrin sıfatı (35:7:13 kararı)
'57:8:15': 'degil',   # 'in kuntum mu'minîn' — muhatap 2MP insanların sıfatı (37:29:5 kararı)
'57:9:12': 'degil',   # 'mine'z-zulumâti ile'n-nûr' — ışık, karanlıkların karşıtı; isim değil (35:20:4 kararı)
'57:9:16': 'ilahi',   # 'inne'llâhe bikum le-ra'ûfun' — lafzın haberi
'57:9:17': 'ilahi',   # 'rahîm' — aynı göndergenin ikinci sıfatı
'57:10:37': 'ilahi',  # 've'llâhu bimâ ta'melûne habîr' — lafzın haberi
# sûre 57 blok 11-15
'57:11:12': 'degil',  # 've lehû ecrun kerîm' — ecrin sıfatı (57:7:15 kararı)
'57:12:3': 'degil',   # 'terâ'l-mu'minîne ve'l-mu'minât' — insanlar (57:8:15 kararı)
'57:12:6': 'degil',   # 'yes'â nûruhum' — inananların ışığı (57:9:12 kararı)
'57:13:10': 'degil',  # 'naqtebis min nûrikum' — inananların ışığı (57:12:6 kararı)
'57:13:15': 'degil',  # 'fe'ltemisû nûrâ' — ışık, nekre (57:12:6 kararı)
'57:13:21': 'degil',  # 'bâtınuhû fîhi'r-rahme' — surun içi; 57:3 'el-bâtın' İLÂHÎ kararının karşıtı (aday 1041)
'57:13:24': 'degil',  # 've zâhiruhû min qibelihi'l-azâb' — surun dışı; 57:3 'ez-zâhir' İLÂHÎ kararının karşıtı (aday 1041)
'57:15:13': 'degil',  # 'hiye mevlâkum' — gönderge 'en-nâr' (ateş); ilâhî ad değil
# sûre 57 blok 16-19
'57:18:12': 'degil',  # 've lehum ecrun kerîm' — ecrin sıfatı (57:11:12 kararı)
'57:19:8': 'degil',   # 've'ş-şuhedâ'u inde rabbihim' — insanlar (çoğul); ilâhî ad değil
'57:19:13': 'degil',  # 'lehum ecruhum ve nûruhum' — inananların ışığı (57:12:6 kararı)
# sûre 57 blok 20-22
'57:20:27': 'degil',  # 've fi'l-âhirati azâbun şedîd' — âhiret (yurt); 57:3:3 'el-âhir' İLÂHÎ kararından ayrı
# sûre 57 blok 23-26
'57:24:11': 'ilahi',  # 'fe-inne'llâhe huve'l-ğaniyyu'l-hamîd' — lafzın haberi
'57:24:12': 'ilahi',  # 'el-hamîd' — aynı göndergenin ikinci sıfatı
'57:25:27': 'ilahi',  # 'inne'llâhe qaviyyun azîz' — lafzın haberi
'57:25:28': 'ilahi',  # 'azîz' — aynı göndergenin ikinci sıfatı
# sûre 57 blok 27-29
'57:28:14': 'degil',  # 'yec'al lekum nûran temşûne bih' — inananlara verilen ışık (57:12:6 kararı)
'57:28:20': 'ilahi',  # 've'llâhu ğafûrun rahîm' — lafzın haberi
'57:28:21': 'ilahi',  # 'rahîm' — aynı göndergenin ikinci sıfatı
# sûre 58 blok 1-4 (2026-10-21)
'58:1:17': 'ilahi',  # semî' — lafzın haberi (inne'llâhe semî'un basîr)
'58:1:18': 'ilahi',  # basîr — aynı haber, çift
'58:2:22': 'ilahi',  # afuvv — ve inne'llâhe le-afuvvun ğafûr
'58:2:23': 'ilahi',  # ğafûr — aynı haber, çift
'58:3:21': 'ilahi',  # habîr — va'llâhu bimâ ta'melûne habîr
# sûre 58 blok 5-7 (2026-10-21)
'58:6:15': 'ilahi',  # şehîd — va'llâhu alâ kulli şey'in şehîd, lafzın haberi
'58:7:47': 'ilahi',  # alîm — inne'llâhe bi-kulli şey'in alîm, lafzın haberi
# sûre 58 blok 8-10 (2026-10-21)
'58:10:17': 'degil',  # 'el-mu'minûn' — çoğul, inananlar ('fe-l-yetevekkeli'l-mu'minûn'); Allah adı değil
# sûre 58 blok 11-13 (2026-10-21)
'58:11:30': 'ilahi',  # habîr — va'llâhu bimâ ta'melûne habîr, lafzın haberi
'58:12:21': 'ilahi',  # ğafûr — fe-inna'llâhe ğafûrun rahîm
'58:12:22': 'ilahi',  # rahîm — aynı haber, çift
'58:13:22': 'ilahi',  # habîr — va'llâhu habîrun bimâ ta'melûn
# sûre 58 blok 19-22 (2026-10-22)
'58:21:8': 'ilahi',  # qavî — inne'llâhe qaviyyun azîz, lafzın haberi
'58:21:9': 'ilahi',  # azîz — aynı haber, çift
'58:22:7': 'degil',  # 'el-yevmi'l-âhir' — günün sıfatı (son gün); 57:3 'el-âhir' İLÂHÎ kararının karşıtı
# sûre 59 blok 1-5
'59:1:10': 'ilahi',  # azîz — ve huve'l-azîzu'l-hakîm, zamir (Allah) haberi
'59:1:11': 'ilahi',  # hakîm — aynı haber, çift
'59:2:11': 'degil',  # 'evvel' — li-evveli'l-haşr, sürgünün ilki; Allah adı değil
'59:2:37': 'degil',  # 'el-mu'minîn' — çoğul, inananların elleri; Allah adı değil
'59:3:12': 'degil',  # 'el-âhira' — âhiret yurdu; Allah adı değil
# sûre 59 blok 6-10
'59:6:25': 'ilahi',  # qadîr — va'llâhu alâ kulli şey'in qadîr, lafzın haberi
'59:7:22': 'degil',  # 'el-ağniyâ'' — çoğul zenginler (beyne'l-ağniyâ'i minkum); Allah adı değil
'59:10:22': 'ilahi',  # ra'ûf — rabbenâ innake ra'ûfun rahîm, Rab hitabının haberi
'59:10:23': 'ilahi',  # rahîm — aynı haber, çift
# sûre 59 blok 11-17
'59:11:20': 'degil',  # 'ehaden' — 'lâ nutî'u fîkum ehaden ebedâ', hiç kimse; Allah adı değil
'59:15:5': 'degil',  # 'qarîben' — 'mine'llezîne min qablihim qarîbâ', yakın zamanda; Allah adı değil
# sûre 59 blok 18-24
'59:18:15': 'ilahi',  # habîr — inna'llâhe habîrun bimâ ta'melûn, lafzın haberi
'59:22:8': 'ilahi',  # âlim — âlimu'l-ğaybi ve'ş-şehâde, 'huve'llâh' haberi
'59:22:12': 'ilahi',  # rahmân — huve'r-rahmânu'r-rahîm
'59:22:13': 'ilahi',  # rahîm — aynı haber, çift
'59:23:8': 'ilahi',  # melik — huve'llâhu … el-melik
'59:23:9': 'ilahi',  # quddûs — aynı dizi
'59:23:10': 'ilahi',  # selâm — aynı dizi
'59:23:11': 'ilahi',  # mu'min — aynı dizi (59:2 çoğul 'mu'minîn' DEĞİL kararının karşıtı)
'59:23:12': 'ilahi',  # muheymin — aynı dizi
'59:23:13': 'ilahi',  # azîz — aynı dizi
'59:23:14': 'ilahi',  # cebbâr — aynı dizi
'59:23:15': 'ilahi',  # mutekebbir — aynı dizi
'59:24:3': 'ilahi',  # hâlik — huve'llâhu'l-hâlik
'59:24:4': 'ilahi',  # bâri' — aynı dizi
'59:24:5': 'ilahi',  # musavvir — aynı dizi
'59:24:16': 'ilahi',  # azîz — ve huve'l-azîzu'l-hakîm
'59:24:17': 'ilahi',  # hakîm — aynı haber, çift
# sûre 60 blok 1-3
'60:1:8': 'degil',  # 'evliyâ'' — çoğul dostlar ('lâ tettehizû aduvvî ve aduvvekum evliyâ''); Allah adı değil
'60:3:13': 'ilahi',  # basîr — va'llâhu bimâ ta'melûne basîr, lafzın haberi
# sûre 60 blok 4-7
'60:5:12': 'ilahi',  # azîz — innake ente'l-azîzu'l-hakîm, Rab hitabının haberi
'60:5:13': 'ilahi',  # hakîm — aynı haber, çift
'60:6:12': 'degil',  # 'el-yevme'l-âhir' — günün sıfatı; Allah adı değil (58:22 emsali)
'60:6:18': 'ilahi',  # ğanî — fe-inna'llâhe huve'l-ğaniyyu'l-hamîd
'60:6:19': 'ilahi',  # hamîd — aynı haber, çift
'60:7:12': 'ilahi',  # qadîr — va'llâhu qadîr, lafzın haberi
'60:7:14': 'ilahi',  # ğafûr — va'llâhu ğafûrun rahîm
'60:7:15': 'ilahi',  # rahîm — aynı haber, çift
# sûre 60 blok 8-10
'60:10:54': 'ilahi',  # alîm — va'llâhu alîmun hakîm, lafzın haberi
'60:10:55': 'ilahi',  # hakîm — aynı haber, çift
# sûre 60 blok 11-13
'60:11:21': 'degil',  # mu'minûn — 'entum bihî mu'minûn', inananların sıfatı
'60:12:37': 'ilahi',  # ğafûr — inna'llâhe ğafûrun rahîm, lafzın haberi
'60:12:38': 'ilahi',  # rahîm — aynı haber, çift
'60:13:13': 'degil',  # âhir — 'el-âhire' (âhiret), sıfat ismi değil
# sûre 61 blok 1-7
'61:1:10': 'ilahi',  # azîz — ve huve'l-azîzu'l-hakîm, zamir (Allah) haberi
'61:1:11': 'ilahi',  # hakîm — aynı haber, çift
'61:6:31': 'degil',  # mubîn — 'sihrun mubîn', sihrin sıfatı
# sûre 61 blok 8-14
'61:8:3': 'degil',   # 'nûra'llâh' — Allah'ın nuru, izâfet (39:69:3 emsali); isim değil
'61:8:8': 'degil',   # 'mutimmu nûrihî' — aynı nur, zamirle izâfet
'61:13:7': 'degil',  # 'fethun qarîb' — fethin sıfatı (48:18:19 emsali)
'61:13:9': 'degil',  # 'beşşiri'l-mu'minîn' — inananlar, çoğul
'61:14:5': 'degil',  # 'kûnû ensâra'llâh' — yardımcılar, inananlar (çoğul)
'61:14:14': 'degil', # 'men ensârî' — Îsâ'nın yardımcıları, çoğul
'61:14:20': 'degil', # 'nahnu ensâru'llâh' — havariler, çoğul
'61:14:35': 'degil', # 'fe-asbahû zâhirîn' — üstün gelenler, inananlar (40:29:5 emsali)
# sûre 62 blok 1-5
'62:1:9': 'ilahi',   # melik — li'llâhi ... el-meliki, lafzın sıfatı (ad dizisi)
'62:1:10': 'ilahi',  # quddûs — aynı dizi (ölçüm satırında görünmüyor, esma_kayit konumu)
'62:1:11': 'ilahi',  # azîz — aynı dizi
'62:1:12': 'ilahi',  # hakîm — aynı dizi, son kelime
'62:2:21': 'degil',  # mubîn — 'dalâlin mubîn', sapkınlığın sıfatı
'62:3:7': 'ilahi',   # azîz — 've huve'l-azîzu'l-hakîm', zamir 62:2 'huve'llezî ba'ase' (Allah)
'62:3:8': 'ilahi',   # hakîm — aynı haber, çift
# sûre 62 blok 6-11
'62:6:8': 'degil',   # evliyâ' — 'ennekum evliyâ'u li'llâh', iddia edenler, çoğul
'62:7:8': 'ilahi',   # alîm — 've'llâhu alîmun bi'z-zâlimîn', lafzın haberi
'62:8:12': 'ilahi',  # âlim — 'ilâ âlimi'l-ğaybi ve'ş-şehâdeh', dönüş yeri Allah (lafız yok)
# sûre 63 blok 6-11
'63:8:13': 'degil',  # mu'minîn — 've li'l-mu'minîn', inananlar (çoğul)
'63:10:9': 'degil',  # ehad — 'ehadekumu'l-mevt', biriniz (zamirli), sayı / kimse
'63:10:17': 'degil', # qarîb — 'ecelin qarîb', ecelin sıfatı (fethun qarîb emsali)
'63:11:9': 'ilahi',  # habîr — 've'llâhu habîrun bimâ ta'melûn', lafzın haberi
# sûre 64 blok 1-6
'64:1:17': 'ilahi',  # qadîr — 've huve alâ kulli şey'in qadîr', zamir 'lehu' lafız (64:1)
'64:2:7': 'degil',   # mu'min — 've minkum mu'min', sizden inanan (insan, tekil sınıf)
'64:2:11': 'ilahi',  # basîr — 've'llâhu bimâ ta'melûne basîr', lafzın haberi
'64:4:12': 'ilahi',  # alîm — 've'llâhu alîmun bi-zâti's-sudûr', lafzın haberi
'64:6:15': 'ilahi',  # ğaniyy — 've'llâhu ğaniyyun hamîd', lafzın haberi
'64:6:16': 'ilahi',  # hamîd — aynı haber, çift
# sûre 64 blok 7-12
'64:8:4': 'degil',    # nûr — 've'n-nûri'llezî enzelnâ', indirilen nur (izâfetsiz ama mevsûlle nitelenen indirilen şey)
'64:8:10': 'ilahi',  # habîr — 've'llâhu bimâ ta'melûne habîr', lafzın haberi
'64:11:16': 'ilahi', # alîm — 've'llâhu bi-kulli şey'in alîm', lafzın haberi
'64:12:11': 'degil', # mubîn — 'el-belâğu'l-mubîn', tebliğin sıfatı
# sûre 64 blok 13-18
'64:13:9': 'degil',  # mu'minûn — 've ale'llâhi fe'l-yetevekkeli'l-mu'minûn', inananlar (çoğul)
'64:14:17': 'ilahi', # ğafûr — 'fe-inna'llâhe ğafûrun rahîm', lafzın haberi
'64:14:18': 'ilahi', # rahîm — aynı haber, çift
'64:17:11': 'ilahi', # şekûr — 've'llâhu şekûrun halîm', lafzın haberi
'64:17:12': 'ilahi', # halîm — aynı haber, çift
'64:18:1': 'ilahi',  # âlim — 'âlimu'l-ğaybi ve'ş-şehâdeh', 64:17 lafzının devamı (lafız yok; 62:8:12 emsali)
'64:18:4': 'ilahi',  # azîz — 'el-azîzu'l-hakîm', aynı ad dizisi
'64:18:5': 'ilahi',  # hakîm — aynı dizi, son kelime
# sûre 65 blok 1-3
'65:2:24': 'degil',  # âhir — 've'l-yevmi'l-âhir', günün sıfatı
# sûre 65 blok 8-12
'65:11:15': 'degil', # nûr — 'mine'z-zulumâti ile'n-nûr', karanlıklardan aydınlığa (mecaz, gidilen yer)
'65:12:18': 'ilahi', # qadîr — 'enna'llâhe alâ kulli şey'in qadîr', lafzın haberi
# sûre 66 blok 1-4
'66:1:13': 'ilahi', # ğafûr — 've'llâhu ğafûrun rahîm', lafzın haberi
'66:1:14': 'ilahi', # rahîm — aynı haber, çift
'66:2:8': 'ilahi',  # mevlâ — 've'llâhu mevlâkum', lafzın haberi
'66:2:10': 'ilahi', # alîm — 've huve'l-alîmu'l-hakîm', zamir lafız
'66:2:11': 'ilahi', # hakîm — aynı haber, çift
'66:3:28': 'ilahi', # alîm — 'nebbe'eniye'l-alîmu'l-habîr', Peygamberin sözünde haber veren (Allah)
'66:3:29': 'ilahi', # habîr — aynı fail, çift
'66:4:14': 'ilahi', # mevlâ — 'fe-inna'llâhe huve mevlâhu', lafzın haberi (Cibrîl ve sâlih mü'minler atıfla)
'66:4:17': 'degil', # mu'minîn — 've sâlihu'l-mu'minîn', inananlar (çoğul)
# sûre 66 blok 5-8
'66:8:29': 'degil', # nûr — 'nûruhum yes'â beyne eydîhim', inananların nuru (âhiret sahnesi)
'66:8:38': 'degil', # nûr — 'etmim lenâ nûranâ', inananların duasında kendi nurları
'66:8:45': 'ilahi', # qadîr — 'inneke alâ kulli şey'in qadîr', 'rabbenâ' hitabının haberi
# sûre 67 blok 1-10
'67:1:9': 'ilahi',  # qadîr — 've huve alâ kulli şey'in qadîr', 'ellezî biyedihi'l-mulk' mevsûlünün zamiri
'67:2:10': 'ilahi', # azîz — 've huve'l-azîzu'l-ğafûr', zamir ölümü ve hayatı yaratan
'67:2:11': 'ilahi', # ğafûr — aynı haber, çift
'67:3:10': 'ilahi', # rahmân — 'fî halqi'r-rahmân', yaratanın adı (izâfet)
'67:9:18': 'degil', # kebîr — 'in entum illâ fî dalâlin kebîr', sapıklığın sıfatı (cehennemliklerin sözü içinde)
# sûre 67 blok 11-20
'67:12:9': 'degil',  # kebîr — 'lehum mağfiretun ve ecrun kebîr', ecrin sıfatı
'67:13:7': 'ilahi',  # alîm — 'innehû alîmun bi-zâti's-sudûr', zamir (söz gizlenen / açıklanan)
'67:14:6': 'ilahi',  # latîf — 've huve'l-latîfu'l-habîr', zamir
'67:14:7': 'ilahi',  # habîr — aynı haber, çift
'67:19:11': 'ilahi', # rahmân — 'mâ yumsikuhunne ille'r-rahmân', hasr içinde fail
'67:19:15': 'ilahi', # basîr — 'innehû bi-kulli şey'in basîr', zamir rahmân
'67:20:10': 'ilahi', # rahmân — 'min dûni'r-rahmân'
# sûre 67 blok 21-30
'67:26:9': 'degil',  # mubîn — 'innemâ ene nezîrun mubîn', 1S konuşan uyarıcının sıfatı
'67:29:3': 'ilahi',  # rahmân — 'qul huve'r-rahmân', zamirin haberi
'67:29:13': 'degil', # mubîn — 'men huve fî dalâlin mubîn', sapıklığın sıfatı
# sûre 68 blok 11-20
'68:15:7': 'degil',  # evvel — 'esâtîru'l-evvelîn', öncekiler (insanlar), inkârcının sözü içinde
# sûre 68 blok 31-41
'68:33:4': 'degil',  # el-âhira — 've le-azâbu'l-âhira', âhiret (son yurt), esmâ 'el-âhir' değil
# sûre 68 blok 42-52
'68:45:5': 'degil',  # metîn — 'inne keydî metîn', 1S konuşanın 'keyd'inin sıfatı, isim değil
# sûre 69 blok 31-41
'69:40:4': 'degil',  # kerîm — 'innehû le-qavlu rasûlin kerîm', elçinin sıfatı
# sûre 69 blok 42-52
'69:47:4': 'degil',  # ehad — 'fe-mâ minkum min ehadin anhu hâcizîn', hiç kimse (nefy)
# sûre 70 blok 1-10
'70:7:2': 'degil',  # qarîb — 've nerâhu qarîbâ', 70:6 'yeravnehû ba'îdâ' karşıtı; göndergesi 70:1 azap / 70:4 gün, ilâhî sıfat değil
# sûre 71 blok 1-10
'71:2:6': 'degil',  # mubîn — 'innî lekum nezîrun mubîn', Nûh'un kendini nitelemesi (insan)
'71:10:6': 'ilahi',  # ğaffâr — 'istağfirû rabbekum innehû kâne ğaffârâ', göndergesi Rab
# sûre 71 blok 11-20
'71:16:4': 'degil',  # nûr — 've ce'ale'l-qamera fîhinne nûran', ayın nitelemesi (ışık), ilâhî ad değil
# sûre 71 blok 21-28
'71:25:12': 'degil',  # nasîr — 'fe-lem yecidû lehum min dûni'llâhi ensârâ', 'ensâr' insan / yardımcı çoğulu, ilâhî ad değil
'71:28:8': 'degil',  # mu'min — 'li-men dehale beytiye mu'minen', eve giren insanın hâli
'71:28:9': 'degil',  # mu'min — 've li'l-mu'minîne', inananlar (insan çoğulu)
# sûre 72 blok 1-10
'72:2:9': 'degil',  # ehad — 've len nuşrike bi-rabbinâ ehadâ', hiç kimse (nefy; 69:47 emsali)
'72:7:9': 'degil',  # ehad — 'en len yeb'asa'llâhu ehadâ', hiç kimse (nefy)
# sûre 72 blok 11-20
'72:18:8': 'degil',  # ehad — 'fe-lâ ted'û ma'a'llâhi ehadâ', hiç kimse (nehy)
'72:20:8': 'degil',  # ehad — 've lâ uşriku bihî ehadâ', hiç kimse (nefy)
# sûre 72 blok 21-28
'72:22:7': 'degil',  # ehad — 'len yucîranî mine'llâhi ehad', hiç kimse (nefy)
'72:25:4': 'degil',  # qarîb — 'e-qarîbun mâ tû'adûn', vaat edilenin yakınlığı (70:7 'qarîb' kuralı), ilâhî sıfat değil
'72:26:1': 'ilahi',  # âlim — 'âlimu'l-ğaybi', göndergesi 72:25 'rabbî' (lafızsız 'âlim' İLÂHÎ, sınıf E kuralı)
'72:26:7': 'degil',  # ehad — 'fe-lâ yuzhiru alâ ğaybihî ehadâ', hiç kimse (nefy)
# sûre 73 blok 1-10
'73:9:9': 'ilahi',  # vekîl — 'fe'ttehizhu vekîlâ', zamir 73:8-9 Rab'a döner (39:62 kuralı)
# sûre 73 blok 20-20
'73:20:77': 'ilahi', '73:20:78': 'ilahi',  # inna'llâha ğafûrun rahîm — inne'nin haberi, göndergesi lafız
}
