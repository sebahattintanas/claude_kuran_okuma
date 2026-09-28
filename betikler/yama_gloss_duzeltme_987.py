# -*- coding: utf-8 -*-
"""yama_gloss_duzeltme_987.py — aday 987: kök glossu kökün baskın / kullanılan anlamını taşımıyor.

Kullanıcı kararı (2026-09-28, dondurma öncesi 5/5): sûre 33'te bulunan 6 kökün glossu ŞİMDİ
çok anlamlı hâle getirilir; eski gloss SİLİNMEZ (tablolar/kok_gloss_duzeltme.json), yamalanan
her kayda `_gloss_duzeltildi` damgası konur. 1112 kökün sistematik taraması YAPILMAZ (araç
dondurması) — borç olarak kalır.

Ölçüm etkisi YOK: defter.json gloss taşımaz. Yalnız görüntü metni (okuma_metni, mercek_kayit,
blok_dikey JSON'ları) ve kok_turkce.json değişir.
İdempotent: eski dizge bulunmazsa hiçbir şey yazılmaz; ikinci koşu 0 yama verir.
"""
import json, glob, os, unicodedata, datetime

nfc = lambda s: unicodedata.normalize('NFC', s)
DUZELT = {   # kök: yeni gloss — kök anahtarı kok_turkce.json'da bulunmazsa koşu DURUR
    'نور': "nûr, ışık; nâr, ateş",
    'بلو': "sınama, imtihan (belâ); eskiyip yıpranma",
    'ولي': "dost, veli; velâyet; yüz ya da arka çevirme (tevellî)",
    'حيي': "diri olma, hayat; utanma (istihyâ); selamlama (tahiyye)",
    'دور': "yurt, ev; dönme, devir",
    'سدد': "set, engel; doğru, isabetli (sedîd)",
}
KP = ['kok_turkce.json', '/home/claude/repo/tablolar/kok_turkce.json']
K = json.load(open(KP[0], encoding='utf-8'))
DUZELT = {nfc(k): v for k, v in DUZELT.items()}
for k in DUZELT:
    assert k in K, 'kök kok_turkce.json\'da yok — NFC eşleşmesi tutmadı, DUR: %r' % k

kayit_p = '/home/claude/repo/tablolar/kok_gloss_duzeltme.json'
KAYIT = json.load(open(kayit_p, encoding='utf-8')) if os.path.exists(kayit_p) else {}
ESKI = {}
for k, yeni in DUZELT.items():
    eski = KAYIT.get(k, {}).get('eski', K[k])      # ikinci koşuda özgün eski gloss korunur
    ESKI[k] = eski
    KAYIT[k] = {'eski': eski, 'yeni': yeni, 'aday': 987,
                'karar': 'kullanıcı, dondurma öncesi 5/5', 'tarih': str(datetime.date.today())}

CIFT = [(k + ' *(' + ESKI[k] + ')*', k + ' *(' + DUZELT[k] + ')*') for k in DUZELT if ESKI[k] != DUZELT[k]]
say = {k: 0 for k in DUZELT}

def yama(s):
    if not isinstance(s, str):
        return s, set()
    deg = set()
    for (e, y), k in zip(CIFT, [c[0].split(' ')[0] for c in CIFT]):
        n = s.count(e)
        if n:
            s = s.replace(e, y); say[k] += n; deg.add(k)
    return s, deg

# okuma_metni — ayet kayıtlarına damga
om_p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(om_p, encoding='utf-8'))
ayet_say = 0
def gez(x):
    global ayet_say
    if isinstance(x, dict):
        deg_top = set()
        for key in list(x):
            v = x[key]
            if isinstance(v, str):
                x[key], d = yama(v); deg_top |= d
            else:
                gez(v)
        if deg_top and 'ar' in x:
            x['_gloss_duzeltildi'] = sorted(set(x.get('_gloss_duzeltildi', [])) | deg_top)
            ayet_say += 1
    elif isinstance(x, list):
        for i, v in enumerate(x):
            if isinstance(v, str):
                x[i], _ = yama(v)
            else:
                gez(v)
gez(OM)
json.dump(OM, open(om_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

mk_p = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(mk_p, encoding='utf-8')); gez(MK)
json.dump(MK, open(mk_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

dosya = 0
for p in sorted(set(glob.glob('blok_dikey_*.json') + glob.glob('/home/claude/repo/ciktilar/blok_dikey_*.json'))):
    J = json.load(open(p, encoding='utf-8')); once = json.dumps(J, ensure_ascii=False); gez(J)
    if json.dumps(J, ensure_ascii=False) != once:
        json.dump(J, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1); dosya += 1

for p in KP:
    T = json.load(open(p, encoding='utf-8'))
    T.update(DUZELT)
    json.dump(T, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
KAYIT['_ozet'] = {'yama_sayisi': {k: v for k, v in say.items()}, 'damgali_ayet': ayet_say,
                  'dikey_dosya': dosya, 'not': 'ikinci koşuda yama 0 olmalı (idempotent)'} \
    if sum(say.values()) else KAYIT.get('_ozet', {})
json.dump(KAYIT, open(kayit_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('yama (kök → anma):', say, '| damgalı ayet kaydı:', ayet_say, '| dikey dosya:', dosya)
