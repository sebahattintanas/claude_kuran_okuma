# -*- coding: utf-8 -*-
"""esma_ton_kur.py — ön-kayıt §4.3.1 (D3, ölçüt kullanıcı onaylı 2026-09-28) → tablolar/esma_ton.json

Ölçüt: birim lemma (bağlam değil) · cemâl = kula yönelen iyilik (rahmet, bağış, lütuf, koruma, yakınlık, kabul)
· celâl = güç ve üstünlük (kudret, üstün gelme, zorlama, azamet, büyüklük, hesaba çekme, egemenlik)
· denge = iyilik ya da güç merkezde değil (bilgi, algı, yaratma, varlık/zât, zaman, kapsama)
· BELİRSİZ = iki bileşen eşit ya da ana bileşen belirsiz (kullanıcı değişikliği: eşitlikte 'denge' değil)
· kaynak sırası: kök anlamı, sonra Kur'an'daki baskın kullanım; ayet sayımı yok; katalogla karşılaştırma yok.
Anahtarlar esma_listesi.json'dan SIRAYLA alınır (Arapça elle yazılmaz); Latin adlar yalnız okunabilirlik
ve hizalama denetimi içindir.
"""
import json, hashlib, unicodedata
L = json.load(open('esma_listesi.json', encoding='utf-8'))['lemmalar']
T = [
 ('rahmân','cemâl','rahmet'), ('rahîm','cemâl','rahmet'), ('gafûr','cemâl','bağış'), ('gaffâr','cemâl','bağış'),
 ('alîm','denge','bilgi'), ('azîz','celâl','üstün gelme, güç'), ('hakîm','belirsiz','hüküm (celâl) ile hikmet (bilgi) eşit'), ('semî','denge','algı'),
 ('basîr','denge','algı'), ('habîr','denge','bilgi'), ('latîf','belirsiz','lütuf (cemâl) ile incelik/ince bilgi (denge) eşit'), ('kadîr','celâl','kudret'),
 ('halîm','cemâl','yumuşaklık, cezayı ertelemek'), ('şekûr','cemâl','iyiliğin karşılığını vermek'), ('tevvâb','cemâl','tevbeyi kabul'), ('vedûd','cemâl','sevgi'),
 ('mecîd','celâl','şan, azamet'), ('velî','cemâl','dostluk, koruma'), ('hamîd','denge','övülmeye layık: zât niteliği'), ('vâsi','denge','kapsama'),
 ('kavî','celâl','güç'), ('metîn','celâl','sarsılmaz güç'), ('şehîd','denge','tanıklık: algı/bilgi'), ('rakîb','denge','gözetme: algı'),
 ('hasîb','celâl','hesaba çekme'), ('kerîm','cemâl','cömertlik'), ('hafîz','cemâl','koruma'), ('mücîb','cemâl','duaya icabet, kabul'),
 ('vekîl','cemâl','işi üstlenip koruma'), ('ganî','denge','muhtaç olmama: zât'), ('mevlâ','belirsiz','koruyucu (cemâl) ile efendi (celâl) eşit'), ('nasîr','cemâl','yardım'),
 ('afüv','cemâl','af'), ('raûf','cemâl','şefkat'), ('melik','celâl','egemenlik'), ('melîk','celâl','egemenlik'),
 ('kuddûs','denge','arınmışlık: zât'), ('selâm','belirsiz','esenlik veren (cemâl) ile kusursuz (zât) eşit'), ('mü\'min','cemâl','güven veren'), ('müheymin','belirsiz','gözetim (denge) ile hâkimiyet (celâl) eşit'),
 ('cebbâr','celâl','zorlama, üstünlük'), ('mütekebbir','celâl','büyüklük'), ('hâlık','denge','yaratma'), ('hallâk','denge','yaratma'),
 ('bâri','denge','yaratma'), ('musavvir','denge','biçim verme'), ('ehad','denge','zât'), ('samed','denge','zât'),
 ('fettâh','belirsiz','açma (cemâl) ile hükmetme (celâl) eşit'), ('rezzâk','cemâl','rızık verme'), ('aliyy','celâl','yücelik, azamet'), ('kebîr','celâl','büyüklük'),
 ('kahhâr','celâl','kahır'), ('vehhâb','cemâl','bağışlama (hibe)'), ('bedî','denge','eşsiz yaratma'), ('hâdî','cemâl','yol gösterme'),
 ('mukît','belirsiz','azık veren (cemâl) ile güç yetiren (celâl) eşit'), ('muktedir','celâl','kudret'), ('karîb','cemâl','yakınlık'), ('muhît','denge','kuşatma: kapsama'),
 ('şâkir','cemâl','iyiliğin karşılığını vermek'), ('âlim','denge','bilgi'), ('hayy','denge','varlık'), ('kayyûm','denge','varlığı sürdürme: zât'),
 ('zâhir','denge','zât'), ('bâtın','denge','zât'), ('evvel','denge','zaman'), ('âhir','denge','zaman'),
 ('nûr','denge','aydınlık: zât, iyilik/güç merkezde değil'), ('berr','cemâl','iyilik'), ('vâris','denge','sonunda kalan: zaman/varlık'), ('mübîn','denge','açıklık: bilgi'),
]
assert len(T) == len(L) == 72, 'hizalama bozuk — DUR'
TAB = {unicodedata.normalize('NFC', l): {'ad': a, 'ton': t, 'gerekce': g} for l, (a, t, g) in zip(L, T)}
from collections import Counter
C = Counter(v['ton'] for v in TAB.values())
out = {'_meta': {'olcut': 'ONKAYIT §4.3.1 (D3)', 'onay': 'kullanıcı 2026-09-28, eşitlikte belirsiz', 'dagilim': dict(C)}, 'tablo': TAB}
p = '/home/claude/repo/tablolar/esma_ton.json'
json.dump(out, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)
json.dump(out, open('esma_ton.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)
print('dağılım:', dict(C), '| SHA-256:', hashlib.sha256(open(p, 'rb').read()).hexdigest())
for a, t, g in T: print('%-11s %-8s %s' % (a, t, g))
