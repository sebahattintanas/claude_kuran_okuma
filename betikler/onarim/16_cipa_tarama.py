# -*- coding: utf-8 -*-
"""16_cipa_tarama.py — P0 #6, ölçütün MEKANİKLEŞTİRİLMESİ.

Çıpa şimdiye kadar okuma dikkatiyle bulunuyordu; bu, aday 899'un yasakladığı
taraflı örneklemin ta kendisi. Bu betik L2+ çıpa ADAYLARINI tarayarak bulur:

  aday = (olgu alanından en az bir kök) VE (nedensellik/karşı-olgusallık işareti)

Tarama bir KARAR vermez, okunacak listeyi daraltır. Anma/geri-çağırma (recall)
sûre 27-28'in elle kurulmuş yedi çıpasına karşı ölçülür.
"""
import json, re, collections

D = json.load(open('defter.json')); DD = {tuple(r['k']): r for r in D}
ISK = json.load(open('ayet_iskelet.json', encoding='utf-8'))
import kuran_akis
AKIS = kuran_akis.kelime_akisi()

# --- olgu alanı kökleri (gök cisimleri, su döngüsü, yer, bitki, canlı, ışık/karanlık, zaman döngüsü)
OLGU = set("""سمو أرض شمس قمر نجم كوكب ليل نهر صبح مسو فلك
موه مطر غيث سحب برق رعد صعق ثلج برد بحر عين نبع فجر
جبل رسو روس شجر نبت زرع ثمر حرث نخل عنب زتن رمن حبب
ريح عصف ذرو لقح هوي جوو طير دبب نحل نمل عنكب بعض
خلق نطف علق مضغ عظم لحم نسل ذرأ زوج موت حيي نوم رقد سبت
نور ضوأ ظلم ظلل حرر برد جري سخر قدر أجل حسب دور""".split())

# --- nedensellik / karşı-olgusallık işaretleri
# İLK SÜRÜMÜN KUSURU: edatlar ELLE, iskelet yazımıyla yazılmıştı; korpus
# yazımıyla uyuşmadıkları için anahtar_denetim.py bunları BOZUK işaretledi.
# Kayıt olarak korunuyor, eşleme morfoloji lemmasına taşındı (17_cipa_tarama2.py).
LEX_LEM = ['COND|LEM:\u0644\u064e\u0648\u0652\u0644\u0627',   # لَوْلا
           'ACC|LEM:\u0644\u064e\u0639\u064e\u0644\u0651',      # لَعَلّ
           'SUB|LEM:\u0643\u064e\u064a']                          # كَي
def isaretli(k):
    r = DD[k]
    if 'şart' in r['edim']:
        return 'edim:şart'
    if 'COND' in r['kip']:
        return 'kip:COND'
    return None   # sözlük ayağı 17_cipa_tarama2.py'ye taşındı

# ayet -> kök kümesi
AYKOK = collections.defaultdict(set)
for x in AKIS:
    if x['kok']:
        AYKOK[tuple(x['key'])].add(x['kok'])

aday = []
for r in D:
    k = tuple(r['k'])
    ort = AYKOK[k] & OLGU
    if not ort:
        continue
    im = isaretli(k)
    if im:
        aday.append((k, sorted(ort), im))

print('=== MEKANİK ÇIPA TARAMASI ===')
print('olgu alanı kök sayısı      :', len(OLGU))
print('olgu kökü taşıyan ayet     :', sum(1 for r in D if AYKOK[tuple(r['k'])] & OLGU))
print('+ nedensellik işareti      : **%d ayet aday** (korpusun %%%.1f\'i)'
      % (len(aday), 100 * len(aday) / 6236))
print()
im_dag = collections.Counter(x[2].split(':')[0] for x in aday)
print('işaret türü dağılımı       :', dict(im_dag))

# --- anma (recall): elle kurulmuş yedi çıpa taramada var mı
CIPA = [(27, 60), (27, 64), (27, 86), (27, 88), (28, 71), (28, 72), (28, 73)]
ad_set = {x[0] for x in aday}
print()
print('=== ANMA (recall) — elle kurulmuş yedi çıpaya karşı ===')
for c in CIPA:
    print('  %d:%-4d %s' % (c[0], c[1], 'YAKALANDI (%s)' % dict((x[0], x[2]) for x in aday)[c]
                            if c in ad_set else 'KAÇTI'))
tut = sum(1 for c in CIPA if c in ad_set)
print('  anma: %d/%d (%%%.0f)' % (tut, len(CIPA), 100 * tut / len(CIPA)))

# --- kesinlik (precision) tabanı: iki sûrede kaç aday var, kaçı gerçek çıpa
for s, n in ((27, 93), (28, 88)):
    sa = [x for x in aday if x[0][0] == s]
    gercek = [c for c in CIPA if c[0] == s]
    print('  sûre %d: %d aday / %d ayet (%%%.1f) · gerçek çıpa %d → kesinlik %%%.0f'
          % (s, len(sa), n, 100 * len(sa) / n, len(gercek),
             100 * len(gercek) / max(1, len(sa))))

print()
print('=== SÛRE 27-28 ADAY LİSTESİ (okunacak daraltılmış küme) ===')
for k, ort, im in aday:
    if k[0] in (27, 28):
        c = ' ★ÇIPA' if k in set(CIPA) else ''
        print('  %d:%-4d %-14s %s%s' % (k[0], k[1], im, ' '.join(ort[:6]), c))

json.dump([{'ayet': '%d:%d' % k, 'kokler': ort, 'isaret': im, 'cipa': k in set(CIPA)}
           for k, ort, im in aday],
          open('cipa_tarama_adaylari.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\ncipa_tarama_adaylari.json yazıldı (%d kayıt)' % len(aday))
