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
