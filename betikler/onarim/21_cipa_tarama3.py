# -*- coding: utf-8 -*-
"""21_cipa_tarama3.py — P0 #6, taramanın morfolojiye bağlanması.

16_cipa_tarama.py'nin anması %57'de kaldı; kaçan üç çıpanın işaretleri
morfolojide ZATEN vardı ama taranmıyordu:
  27:60  مَا كَانَ لَكُمْ أَن   — YETİ SINIRI  (NEG + كون + SUB أن)
  27:86  لِيَسْكُنُوا۟         — TA'LÎL LÂMI  (PRP|PREF + MOOD:SUBJ)
  27:88  تَحْسَبُهَا ... وَهِىَ — GÖRÜNÜŞ/DURUM (sanma fiili + CIRC|PREF)

Bu sürüm beş işaret ailesi tarıyor ve her ailenin ayrı anmasını raporluyor.
Tarama KARAR vermez; okunacak listeyi daraltır.
"""
import json, re, collections

D = json.load(open('defter.json')); DD = {tuple(r['k']): r for r in D}
ISK = json.load(open('ayet_iskelet.json', encoding='utf-8'))
import kuran_akis
AKIS = kuran_akis.kelime_akisi()

OLGU = set("""سمو أرض شمس قمر نجم كوكب ليل نهر صبح مسو فلك
موه مطر غيث سحب برق رعد صعق ثلج برد بحر عين نبع فجر
جبل رسو روس شجر نبت زرع ثمر حرث نخل عنب زتن رمن حبب
ريح عصف ذرو لقح هوي جوو طير دبب نحل نمل عنكب بعض
خلق نطف علق مضغ عظم لحم نسل ذرأ زوج موت حيي نوم رقد سبت
نور ضوأ ظلم ظلل حرر برد جري سخر قدر أجل حسب دور""".split())
SANMA = {'\u062d\u0633\u0628', '\u0638\u0646\u0646', '\u062e\u064a\u0644'}  # حسب ظنن خيل
BAKIS = {'\u0631\u0623\u064a', '\u0646\u0638\u0631'}                            # رأي نظر

# --- morfolojiden ayet başına etiket toplama
TAG = collections.defaultdict(list)
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4:
        continue
    loc = p[0].split(':')
    if len(loc) == 5:
        loc = loc[1:]
    if len(loc) != 4:
        continue
    TAG[(int(loc[0]), int(loc[1]))].append(p[3])

AYKOK = collections.defaultdict(set)
for x in AKIS:
    if x['kok']:
        AYKOK[tuple(x['key'])].add(x['kok'])


def isaretler(k):
    """ayetin taşıdığı nedensellik/karşı-olgusallık işaret ailelerini döndürür"""
    r = DD[k]
    t = TAG[k]
    blob = '\n'.join(t)
    out = []
    # A — şart / karşı-olgusal
    if 'şart' in r['edim'] or 'COND' in r['kip']:
        out.append('A_şart')
    if 'COND|LEM:\u0644\u064e\u0648\u0652\u0644\u0627' in blob:   # لَوْلا — korpus lemma biçimi
        out.append('A_levlâ')
    # B — ta'lîl lâmı (amaç)
    if 'PRP|PREF' in blob:
        out.append('B_ta\u2019lîl')
    # C — recâ / amaç edatı; korpus lemma biçimleriyle (elle yazım YOK)
    if ('ACC|LEM:\u0644\u064e\u0639\u064e\u0644\u0651' in blob      # لَعَلّ
            or 'SUB|LEM:\u0643\u064e\u064a' in blob):                  # كَي
        out.append('C_recâ')
    # D — yeti sınırı: olumsuzluk + كون + أن  ya da  'başka ilâh' kalıbı
    if ('NEG' in blob and 'ROOT:\u0643\u0648\u0646' in blob            # كون
            and 'SUB|LEM:\u0623\u064e\u0646' in blob):                  # أَن
        out.append('D_yeti')
    if 'ROOT:\u0623\u0644\u0647' in blob and 'ROOT:\u063a\u064a\u0631' in blob:  # أله + غير
        out.append('D_yeti')
    # E — görünüş/durum ayrımı: sanma fiili + hâl vâvı
    if (AYKOK[k] & SANMA) and 'CIRC|PREF' in blob:
        out.append('E_görünüş')
    # F — ÖLÇÜ: iki ya da daha fazla sayı işareti (birim verilmiş nicelik)
    if len(r['say']) >= 2:
        out.append('F_ölçü')
    # G — GÖZLEME ÇAĞRI: görme/bakma kökü, soru ya da EMİR kipinde
    #     ('görmediler mi' · 'yeryüzünde gezin de bakın')
    #     `فَٱنظُرْ كَيْفَ كَانَ عَٰقِبَةُ` kalıbı DIŞARIDA: o tarihe bakış çağrısıdır,
    #     olguya değil — ayırt edici işaret عقب kökünün varlığı
    if ((AYKOK[k] & BAKIS) and (AYKOK[k] & OLGU)
            and '\u0639\u0642\u0628' not in AYKOK[k]                     # عقب
            and (('INTG' in r['kip'] and 'NEG' in r['kip']) or 'IMPV' in r['kip'])):
        out.append('G_bakış')
    return sorted(set(out))


aday = []
for r in D:
    k = tuple(r['k'])
    ort = AYKOK[k] & OLGU
    im = isaretler(k)
    # F_ölçü ve G_bakış aileleri kendi başına yeter: ölçü verilmiş nicelik ve
    # gözleme çağrı kalıbı, olgu kökü listesinden bağımsız olarak çıpa işareti
    if not im:
        continue
    if not ort and not ({'F_ölçü', 'G_bakış'} & set(im)):
        continue
    aday.append((k, sorted(ort), im))

print('=== MEKANİK ÇIPA TARAMASI — sürüm 2 (morfoloji bağlı) ===')
print('olgu kökü taşıyan ayet : %d' % sum(1 for r in D if AYKOK[tuple(r['k'])] & OLGU))
print('+ işaret taşıyan       : **%d ayet aday** (korpusun %%%.1f\'i)'
      % (len(aday), 100 * len(aday) / 6236))
c = collections.Counter(i for _, _, im in aday for i in im)
print('işaret ailesi dağılımı :', dict(c))
print()

# KURULUM KÜMESİ (tarayıcı bunları yakalamak için yazıldı — anma ölçümü DÖNGÜSEL)
KURULUM = [(27, 60), (27, 64), (27, 86), (27, 88), (28, 71), (28, 72), (28, 73)]
# TUTULAN KÜME (sûre 29 okumasından, tarayıcı yazıldıktan SONRA bulundu — BAĞIMSIZ sınama)
TUTULAN = [(29, 14), (29, 19), (29, 20)]
CIPA = KURULUM + TUTULAN
ad = {x[0]: x[2] for x in aday}
print('=== ANMA — KURULUM kümesi (döngüsel, bilgi değeri sınırlı) ===')
for k in CIPA:
    print('  %d:%-4d %s' % (k[0], k[1], ', '.join(ad[k]) if k in ad else '*** KAÇTI ***'))
tut = sum(1 for k in KURULUM if k in ad)
print('  anma: %d/%d (%%%.0f)' % (tut, len(KURULUM), 100 * tut / len(KURULUM)))
print()
print('=== ANMA — TUTULAN küme (BAĞIMSIZ sınama, sûre 29) ===')
for k in TUTULAN:
    print('  %d:%-4d %s' % (k[0], k[1], ', '.join(ad[k]) if k in ad else '*** KAÇTI ***'))
t2 = sum(1 for k in TUTULAN if k in ad)
print('  anma: **%d/%d (%%%.0f)**' % (t2, len(TUTULAN), 100 * t2 / len(TUTULAN)))
print()

print('=== İŞARET AİLESİ BAŞINA KATKI (hangi aile hangi çıpayı yakalıyor) ===')
for aile in ('A_şart', 'A_levlâ', 'B_ta\u2019lîl', 'C_recâ', 'D_yeti', 'E_görünüş', 'F_ölçü', 'G_bakış'):
    y = [('%d:%d' % k) for k in CIPA if k in ad and aile in ad[k]]
    n = sum(1 for _, _, im in aday if aile in im)
    print('  %-12s korpus aday %4d · yakaladığı çıpa: %s' % (aile, n, ', '.join(y) or '—'))
print()

for s, n in ((27, 93), (28, 88), (29, 69)):
    sa = [x for x in aday if x[0][0] == s]
    g = [k for k in CIPA if k[0] == s]
    print('  sûre %d: %2d aday / %d ayet (%%%.1f) · gerçek çıpa %d → kesinlik %%%.0f'
          % (s, len(sa), n, 100 * len(sa) / n, len(g), 100 * len(g) / max(1, len(sa))))

json.dump([{'ayet': '%d:%d' % k, 'kokler': ort, 'isaretler': im, 'cipa': k in set(CIPA)}
           for k, ort, im in aday],
          open('cipa_tarama3_adaylari.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\ncipa_tarama3_adaylari.json yazıldı (%d kayıt)' % len(aday))
