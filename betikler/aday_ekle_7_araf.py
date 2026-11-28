# -*- coding: utf-8 -*-
"""aday_ekle_7_araf.py — sûre 7 (A'râf) adayları (AX_araf) ve okuma bağları (AS_araf).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1043'ten); betik sıranın kopmadığını doğrular.
"""
import json

ARAF = [
]

BAGLAR = {"AS_araf": [
 # blok 1-5
 {'bag': '21:14 → 7:5', 'kural': "okuma — harekesiz 'innâ kunnâ zâlimîn'; sayım 'say 7:5 10-12'; en uzun ortak lemma dizisi 'inne kâne zâlim' (dizi 7 5 10 12)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '21:46 → 7:5', 'kural': "okuma — harekesiz 'innâ kunnâ zâlimîn'; sayım 'say 7:5 10-12'; en uzun ortak lemma dizisi 'inne kâne zâlim' (dizi 7 5 10 12)", 'not': 'kalıp eşi (sayım).'},
 # blok 6-10
 {'bag': '23:102 → 7:8', 'kural': "okuma — harekesiz 'fe-men sequlet mevâzînuhû fe-ulâ'ike humu'l-muflihûn'; sayım 'say 7:8 4-9'; en uzun ortak lemma dizisi 'men sequlet mîzân zâ _ muflih' (dizi 7 8 4 9)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '23:103 → 7:9', 'kural': "okuma — harekesiz 've men xaffet mevâzînuhû fe-ulâ'ike'llezîne xasirû enfusehum'; sayım 'say 7:9 1-7'; en uzun ortak lemma dizisi 'men xaffet mîzân zâ ellezî xasira nefs' (dizi 7 9 1 7)", 'not': 'kalıp eşi (sayım).'},
 # blok 11-13
 {'bag': '18:50 → 7:11', 'kural': "okuma — harekesiz 'qulnâ li'l-melâ'iketi'scudû li-âdeme fe-secedû illâ iblîs'; sayım 'say 7:11 6-12'; en uzun ortak lemma dizisi 'qâle melek secede âdem secede illâ iblîs' (dizi 7 11 6 12)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '38:75 → 7:12', 'kural': "okuma — harekesiz 'mâ mene'ake'; sayım 'say 7:12 2-3'; en uzun ortak lemma dizisi 'mâ mene'a' (dizi 7 12 2 3)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '38:76 → 7:12', 'kural': "okuma — harekesiz 'qâle ene xayrun minhu xalaqtenî min nârin ve xalaqtehû min tîn'; sayım 'say 7:12 8-17'; en uzun ortak lemma dizisi 'qâle _ xayr min xalaqa min nâr xalaqa min tîn' (dizi 7 12 8 17)", 'not': 'kalıp eşi (sayım).'},
 # blok 14-18
 {'bag': '15:36 → 7:14', 'kural': "okuma — harekesiz 'ilâ yevmi yub'asûn'; sayım 'say 7:14 3-5'; en uzun ortak lemma dizisi 'yunzaru ilâ yevm be'ase' (dizi 7 14 2 5)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '38:79 → 7:14', 'kural': "okuma — harekesiz 'ilâ yevmi yub'asûn'; sayım 'say 7:14 3-5'; en uzun ortak lemma dizisi 'yunzaru ilâ yevm be'ase' (dizi 7 14 2 5)", 'not': 'kalıp eşi (sayım).'},
 # blok 19-21
 {'bag': '2:35 → 7:19', 'kural': "okuma — harekesiz 'haysu şi'tumâ ve lâ taqrabâ hâzihi'ş-şecerate fe-tekûnâ mine'z-zâlimîn'; sayım 'say 7:19 8-16'; en uzun ortak lemma dizisi 'haysu şâ'e lâ yaqrabu zâ şecera kâne min zâlim' (dizi 7 19 8 16)", 'not': 'kalıp eşi (sayım).'},
 # blok 22-25
 {'bag': '20:121 → 7:22', 'kural': "okuma — harekesiz 'sev'âtuhumâ ve tafiqâ yaxsifâni 'aleyhimâ min varaqi'l-cenneti'; sayım 'say 7:22 8-14'; en uzun ortak lemma dizisi 'bedâ _ sev'e tafiqa yaxsife 'alâ min varaq cenne' (dizi 7 22 6 14)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '2:36 → 7:24', 'kural': "okuma — harekesiz 'hbitû ba'dukum li-ba'din 'aduvvun ve lekum fi'l-ardi musteqarrun ve metâ'un ilâ hîn'; sayım 'say 7:24 2-12'; en uzun ortak lemma dizisi 'qâle yehbitu ba'd ba'd 'aduvv _ fî ard musteqarr metâ' ilâ hîn' (dizi 7 24 1 12)", 'not': 'kalıp eşi (sayım).'},
 # blok 26-27
 # blok 28-30
 {'bag': '2:169 → 7:28', 'kural': "okuma — harekesiz ''ale'llâhi mâ lâ ta'lemûn'; sayım 'say 7:28 18-22'; en uzun ortak lemma dizisi 'qâle 'alâ allâh mâ lâ 'alime' (dizi 7 28 17 22)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '40:65 → 7:29', 'kural': "okuma — harekesiz 'muxlisîne lehu'd-dîne'; sayım 'say 7:29 11-13'; en uzun ortak lemma dizisi 'de'â muxlis _ dîn' (dizi 7 29 10 13)", 'not': 'kalıp eşi (sayım).'},
 # blok 31-34
 {'bag': '40:51 → 7:32', 'kural': "okuma — harekesiz 'âmenû fi'l-hayâti'd-dunyâ'; sayım 'say 7:32 15-18'; en uzun ortak lemma dizisi 'ellezî âmene fî hayâ dunyâ' (dizi 7 32 14 18)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '10:68 → 7:33', 'kural': "okuma — harekesiz ''ale'llâhi mâ lâ ta'lemûn'; sayım 'say 7:33 25-29'; en uzun ortak lemma dizisi 'qâle 'alâ allâh mâ lâ 'alime' (dizi 7 33 24 29)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '10:49 → 7:34', 'kural': "okuma — harekesiz 'câ'e eceluhum'; sayım 'say 7:34 5-6'; en uzun ortak lemma dizisi 'kull umme ecel izâ câ'e ecel lâ yeste'xiru sâ'a lâ yestaqdimu' (dizi 7 34 1 11)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '16:61 → 7:34', 'kural': "okuma — harekesiz 'fe-izâ câ'e eceluhum'; sayım 'say 7:34 4-6'; en uzun ortak lemma dizisi 'izâ câ'e ecel lâ yeste'xiru sâ'a lâ yestaqdimu' (dizi 7 34 4 11)", 'not': 'kalıp eşi (sayım).'},
 # blok 35-37
 {'bag': '40:74 → 7:37', 'kural': "okuma — harekesiz 'dallû 'annâ'; sayım 'say 7:37 30-31'; en uzun ortak lemma dizisi 'min dûn allâh qâle dalle 'an' (dizi 7 37 26 31)", 'not': 'kalıp eşi (sayım).'},
 # blok 38-41
 {'bag': '41:25 → 7:38', 'kural': "okuma — harekesiz 'mine'l-cinni ve'l-insi'; sayım 'say 7:38 9-11'; en uzun ortak lemma dizisi 'fî umme qad xalâ min qabl min cinn ins' (dizi 7 38 3 11)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '46:18 → 7:38', 'kural': "okuma — harekesiz 'mine'l-cinni ve'l-insi'; sayım 'say 7:38 9-11'; en uzun ortak lemma dizisi 'fî umme qad xalâ min qabl min cinn ins' (dizi 7 38 3 11)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '38:61 → 7:38', 'kural': "okuma — harekesiz ''azâben dı'fen'; sayım 'say 7:38 31-32'; en uzun ortak lemma dizisi ''azâb dı'f' (dizi 7 38 31 32)", 'not': 'kalıp eşi (sayım).'},
 # blok 42-43
 {'bag': '15:47 → 7:43', 'kural': "okuma — harekesiz 've neza'nâ mâ fî sudûrihim min ğıllin'; sayım 'say 7:43 1-6'; en uzun ortak lemma dizisi 'neza'a mâ fî sadr min ğıll' (dizi 7 43 1 6)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '43:72 → 7:43', 'kural': "okuma — harekesiz 'ûristumûhâ bimâ kuntum ta'melûn'; sayım 'say 7:43 33-36'; en uzun ortak lemma dizisi 'evrase mâ kâne 'amile' (dizi 7 43 33 36)", 'not': 'kalıp eşi (sayım).'},
 # blok 44-47
 {'bag': '11:18 → 7:44', 'kural': "okuma — harekesiz 'la'netu'llâhi 'ale'z-zâlimîn'; sayım 'say 7:44 25-28'; en uzun ortak lemma dizisi 'la'ne allâh 'alâ zâlim' (dizi 7 44 25 28)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '11:19 → 7:45', 'kural': "okuma — harekesiz 'llezîne yasuddûne 'an sebîli'llâhi ve yebğûnehâ 'ivecen'; sayım 'say 7:45 1-7'; en uzun ortak lemma dizisi 'ellezî sadde 'an sebîl allâh beğâ 'iveç' (dizi 7 45 1 7)", 'not': 'kalıp eşi (sayım); ölçüm esit2 YAKIN.'},
 {'bag': '14:3 → 7:45', 'kural': "okuma — harekesiz 'sebîli'llâhi ve yebğûnehâ 'ivecen'; sayım 'say 7:45 4-7'; en uzun ortak lemma dizisi 'sadde 'an sebîl allâh beğâ 'iveç' (dizi 7 45 2 7)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '23:94 → 7:47', 'kural': "okuma — harekesiz 'l-qavmi'z-zâlimîn'; sayım 'say 7:47 12-13'; en uzun ortak lemma dizisi 'rabb lâ ce'ale' (dizi 7 47 8 10)", 'not': 'kalıp eşi (sayım).'},
 # blok 48-51
 {'bag': '36:47 → 7:50', 'kural': "okuma — harekesiz 'mimmâ razaqakumu'llâhu'; sayım 'say 7:50 12-14'; en uzun ortak lemma dizisi 'min-mâ razaqa allâh qâle' (dizi 7 50 12 15)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '41:28 → 7:51', 'kural': "okuma — harekesiz 'kânû bi-âyâtinâ yechadûn'; sayım 'say 7:51 17-19'; en uzun ortak lemma dizisi 'mâ kâne âye cehadu' (dizi 7 51 16 19)", 'not': 'kalıp eşi (sayım).'},
 # blok 52-53
 {'bag': '16:64 → 7:52', 'kural': "okuma — harekesiz 'rahmeten li-qavmin yu'minûn'; sayım 'say 7:52 8-10'; en uzun ortak lemma dizisi 'hudâ rahme qavm âmene' (dizi 7 52 7 10)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '35:37 → 7:53', 'kural': "okuma — harekesiz 'ğayra'llezî kunnâ na'mel'; sayım 'say 7:53 27-30'; en uzun ortak lemma dizisi 'ğayr ellezî kâne 'amile' (dizi 7 53 27 30)", 'not': 'kalıp eşi (sayım).'},
 # blok 54-56
 {'bag': '10:3 → 7:54', 'kural': "okuma — harekesiz 'inne rabbekumu'llâhu'llezî xalaqa's-semâvâti ve'l-arda fî sitteti eyyâmin summe'stevâ 'ale'l-'arşi'; sayım 'say 7:54 1-14'; en uzun ortak lemma dizisi 'inne rabb allâh ellezî xalaqa semâ' ard fî sitte yevm summe istevâ 'alâ 'arş' (dizi 7 54 1 14)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '13:3 → 7:54', 'kural': "okuma — harekesiz 'yuğşi'l-leyle'n-nehâra'; sayım 'say 7:54 15-17'; en uzun ortak lemma dizisi 'uğşiyet leyl nehâr' (dizi 7 54 15 17)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '16:12 → 7:54', 'kural': "okuma — harekesiz 've'ş-şemse ve'l-qamera ve'n-nucûme musaxxarâtin bi-emrihî'; sayım 'say 7:54 20-24'; en uzun ortak lemma dizisi 'şems qamer necm musaxxare emr' (dizi 7 54 20 24)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '22:18 → 7:54', 'kural': "okuma — harekesiz 've'ş-şemse ve'l-qamera ve'n-nucûme'; sayım 'say 7:54 20-22'; en uzun ortak lemma dizisi 'şems qamer necm' (dizi 7 54 20 22)", 'not': 'kalıp eşi (sayım).'},
 # blok 57-58
 {'bag': '25:48 → 7:57', 'kural': "okuma — harekesiz 'r-riyâha buşran beyne yedey rahmetihî'; sayım 'say 7:57 4-8'; en uzun ortak lemma dizisi 'ellezî ersele rîh buşr beyn yed rahme' (dizi 7 57 2 8)", 'not': 'kalıp eşi (sayım).'},
 # blok 59-64
 {'bag': '23:23 → 7:59', 'kural': "okuma — harekesiz 'erselnâ nûhan ilâ qavmihî'; sayım 'say 7:59 2-5'; en uzun ortak lemma dizisi 'qad ersele nûh ilâ qavm qâle qavm 'abede allâh mâ _ min ilâh ğayr' (dizi 7 59 1 14)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '11:50 → 7:59', 'kural': "okuma — harekesiz 'yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû'; sayım 'say 7:59 7-14'; en uzun ortak lemma dizisi 'qâle qavm 'abede allâh mâ _ min ilâh ğayr' (dizi 7 59 6 14)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '11:61 → 7:59', 'kural': "okuma — harekesiz 'yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû'; sayım 'say 7:59 7-14'; en uzun ortak lemma dizisi 'qâle qavm 'abede allâh mâ _ min ilâh ğayr' (dizi 7 59 6 14)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '11:84 → 7:59', 'kural': "okuma — harekesiz 'yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû'; sayım 'say 7:59 7-14'; en uzun ortak lemma dizisi 'qâle qavm 'abede allâh mâ _ min ilâh ğayr' (dizi 7 59 6 14)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '23:32 → 7:59', 'kural': "okuma — harekesiz 'u'budu'llâhe mâ lekum min ilâhin ğayruhû'; sayım 'say 7:59 8-14'; en uzun ortak lemma dizisi ''abede allâh mâ _ min ilâh ğayr' (dizi 7 59 8 14)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '12:30 → 7:60', 'kural': "okuma — harekesiz 'fî dalâlin mubîn'; sayım 'say 7:60 7-9'; en uzun ortak lemma dizisi 'inne ra'â fî dalâl mubîn' (dizi 7 60 5 9)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '23:33 → 7:60', 'kural': "okuma — harekesiz 'l-mele'u min qavmihî'; sayım 'say 7:60 2-4'; en uzun ortak lemma dizisi 'qâle mele' min qavm' (dizi 7 60 1 4)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '26:16 → 7:61', 'kural': "okuma — harekesiz 'rabbi'l-'âlemîn'; sayım 'say 7:61 9-10'; en uzun ortak lemma dizisi 'rabb 'âlem' (dizi 7 61 9 10)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '43:46 → 7:61', 'kural': "okuma — harekesiz 'rabbi'l-'âlemîn'; sayım 'say 7:61 9-10'; en uzun ortak lemma dizisi 'rabb 'âlem' (dizi 7 61 9 10)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '10:73 → 7:64', 'kural': "okuma — harekesiz 'me'ahû fi'l-fulki'; sayım 'say 7:64 4-6'; en uzun ortak lemma dizisi 'uğriqu ellezî kezzebe âye' (dizi 7 64 7 10)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '21:77 → 7:64', 'kural': "okuma — harekesiz 'llezîne kezzebû bi-âyâtinâ'; sayım 'say 7:64 8-10'; en uzun ortak lemma dizisi 'ellezî kezzebe âye inne kâne qavm' (dizi 7 64 8 13)", 'not': 'kalıp eşi (sayım).'},
 # blok 65-69
 {'bag': '11:27 → 7:66', 'kural': "okuma — harekesiz 'l-mele'u'llezîne kefarû min'; sayım 'say 7:66 2-5'; en uzun ortak lemma dizisi 'qâle mele' ellezî kefere min qavm' (dizi 7 66 1 6)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '23:24 → 7:66', 'kural': "okuma — harekesiz 'llezîne kefarû min qavmihî'; sayım 'say 7:66 3-6'; en uzun ortak lemma dizisi 'qâle mele' ellezî kefere min qavm' (dizi 7 66 1 6)", 'not': 'kalıp eşi (sayım).'},
 # blok 70-72
 {'bag': '11:32 → 7:70', 'kural': "okuma — harekesiz 'fe'tinâ bi-mâ te'idunâ'; sayım 'say 7:70 11-13'; en uzun ortak lemma dizisi 'etâ mâ ve'ade in kâne min sâdiq' (dizi 7 70 11 17)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '46:22 → 7:70', 'kural': "okuma — harekesiz 'fe'tinâ bi-mâ te'idunâ'; sayım 'say 7:70 11-13'; en uzun ortak lemma dizisi 'etâ mâ ve'ade in kâne min sâdiq' (dizi 7 70 11 17)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '14:10 → 7:70', 'kural': "okuma — ölçüm xref 14:10; lemma dizisi eşi 'dizi 7 70 8 11'; en uzun ortak lemma dizisi 'kâne 'abede âbâ' etâ' (dizi 7 70 8 11)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '12:40 → 7:71', 'kural': "okuma — harekesiz 'esmâ'in semmeytumûhâ entum ve âbâ'ukum'; sayım 'say 7:71 11-14'; en uzun ortak lemma dizisi 'ism semmâ _ âbâ'' (dizi 7 71 11 14)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '53:23 → 7:71', 'kural': "okuma — harekesiz 'esmâ'in semmeytumûhâ entum ve âbâ'ukum'; sayım 'say 7:71 11-14'; en uzun ortak lemma dizisi 'ism semmâ _ âbâ'' (dizi 7 71 11 14)", 'not': 'kalıp eşi (sayım).'},
 # blok 73-75
 {'bag': '11:64 → 7:73', 'kural': "okuma — harekesiz 'hâzihî nâqatu'llâhi lekum âyeten fe-zerûhâ te'kul fî ardi'llâhi'; sayım 'say 7:73 19-28'; en uzun ortak lemma dizisi 'zâ nâqa allâh _ âye yezere ekele fî ard allâh lâ messe sû' exaze 'azâb' (dizi 7 73 19 33)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '26:156 → 7:73', 'kural': "okuma — ölçüm xref 26:156; lemma dizisi eşi 'dizi 7 73 29 33'; en uzun ortak lemma dizisi 'lâ messe sû' exaze 'azâb' (dizi 7 73 29 33)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '2:60 → 7:74', 'kural': "okuma — harekesiz 've lâ ta'sev fi'l-ardi mufsidîn'; sayım 'say 7:74 21-25'; en uzun ortak lemma dizisi 'allâh lâ ta'se fî ard mufsid' (dizi 7 74 20 25)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '15:82 → 7:74', 'kural': "okuma — harekesiz 'l-cibâle buyûten'; sayım 'say 7:74 16-17'; en uzun ortak lemma dizisi 'cebel beyt' (dizi 7 74 16 17)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '26:149 → 7:74', 'kural': "okuma — harekesiz 'l-cibâle buyûten'; sayım 'say 7:74 16-17'; en uzun ortak lemma dizisi 'cebel beyt' (dizi 7 74 16 17)", 'not': 'kalıp eşi (sayım).'},
 # blok 76-79
 {'bag': '51:44 → 7:77', 'kural': "okuma — harekesiz ''an emri rabbihim'; sayım 'say 7:77 4-6'; en uzun ortak lemma dizisi ''ate 'an emr rabb' (dizi 7 77 3 6)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '29:37 → 7:78', 'kural': "okuma — harekesiz 'fe-exazethumu'r-racfetu fe-esbahû fî dârihim câsimîn'; sayım 'say 7:78 1-6'; en uzun ortak lemma dizisi 'exaze racfe esbaha fî dâr câsim' (dizi 7 78 1 6)", 'not': 'kalıp eşi (sayım).'},
 # blok 80-84
 {'bag': '27:54 → 7:80', 'kural': "okuma — harekesiz 'e-te'tûne'l-fâhişete'; sayım 'say 7:80 5-6'; en uzun ortak lemma dizisi 'lût iz qâle qavm etâ fâhişe' (dizi 7 80 1 6)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '29:28 → 7:80', 'kural': "okuma — harekesiz 'mâ sebeqakum bihâ min ehadin mine'l-'âlemîn'; sayım 'say 7:80 7-13'; en uzun ortak lemma dizisi 'fâhişe mâ sebeqa _ min ehad min 'âlem' (dizi 7 80 6 13)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '27:55 → 7:81', 'kural': "okuma — harekesiz 'r-ricâle şehveten min dûni'n-nisâ'i'; sayım 'say 7:81 3-7'; en uzun ortak lemma dizisi 'inne etâ ricâl şehve min dûn nisâ' bel' (dizi 7 81 1 8)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '29:28 → 7:81', 'kural': "okuma — harekesiz 'innekum le-te'tûne'; sayım 'say 7:81 1-2'; en uzun ortak lemma dizisi 'inne etâ' (dizi 7 81 1 2)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '29:29 → 7:81', 'kural': "okuma — harekesiz 'le-te'tûne'r-ricâle'; sayım 'say 7:81 2-3'; en uzun ortak lemma dizisi 'inne etâ ricâl' (dizi 7 81 1 3)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '27:56 → 7:82', 'kural': "okuma — harekesiz 'innehum unâsun yetetahharûn'; sayım 'say 7:82 11-13'; en uzun ortak lemma dizisi 'mâ kâne cevâb qavm illâ en qâle exrece' (dizi 7 82 1 8)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '29:24 → 7:82', 'kural': "okuma — harekesiz 'cevâbe qavmihî'; sayım 'say 7:82 3-4'; en uzun ortak lemma dizisi 'mâ kâne cevâb qavm illâ en qâle' (dizi 7 82 1 7)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '29:29 → 7:82', 'kural': "okuma — harekesiz 'cevâbe qavmihî'; sayım 'say 7:82 3-4'; en uzun ortak lemma dizisi 'mâ kâne cevâb qavm illâ en qâle' (dizi 7 82 1 7)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '27:57 → 7:83', 'kural': "okuma — harekesiz 'fe-enceynâhu ve ehlehû'; sayım 'say 7:83 1-2'; en uzun ortak lemma dizisi 'encâ ehl illâ imrae' (dizi 7 83 1 4)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '29:32 → 7:83', 'kural': "okuma — harekesiz 'kânet mine'l-ğâbirîn'; sayım 'say 7:83 5-7'; en uzun ortak lemma dizisi 'ehl illâ imrae kâne min ğâbir' (dizi 7 83 2 7)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '29:33 → 7:83', 'kural': "okuma — harekesiz 'kânet mine'l-ğâbirîn'; sayım 'say 7:83 5-7'; en uzun ortak lemma dizisi 'ehl illâ imrae kâne min ğâbir' (dizi 7 83 2 7)", 'not': 'kalıp eşi (sayım).'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_araf', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in ARAF]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_araf'] = ARAF
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_araf', len(ARAF), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_araf', len(BAGLAR['AS_araf']))
