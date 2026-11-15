# bölüm 3 (sûre 5) denetimi kuralı 8: meal karşılığı ↔ ölçüm kök glossu — ortak Türkçe kökü (ilk 4 harf) olmayanlar listelenir
# bölüm 5 kuralı 4: kök taşıyan edat / zarf biçimli kayıtlar da taranır; taranmayan kök taşıyan kelime sayısı basılır (MK'da kelime numarası hiç geçmeyen)
# kullanım (/home/claude'dan): python3 sunum/gloss_tara.py A B NN   (bNN/yap/veri.py MK + bNN/morph.txt + bNN/olcum.txt)
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
sys.path.insert(0, '/home/claude/b%s/yap' % NN); import veri
olc = open('/home/claude/b%s/olcum.txt' % NN, encoding='utf-8').read().replace('**', '')
GL = dict(re.findall(r"(\S+) \*\((.*?)\)\*", olc))
ROOT = {}
for l in open('/home/claude/b%s/morph.txt' % NN, encoding='utf-8'):
    k, w, f = l.rstrip('\n').split('\t'); _, a, n = k.split(':')
    m = re.search(r'ROOT:([^|]+)', f)
    if m: ROOT[(int(a), int(n))] = m.group(1)
def kok(t):
    return re.sub(r'[^a-zçğıöşüâîû ]', '', t.lower().replace('â', 'a').replace('î', 'i').replace('û', 'u'))
ZAM = set("'hâ' 'hu' 'hû' 'hî' 'hi' 'hum' 'him' 'humâ' 'himâ' 'hunne' 'hinne' 'kum' 'ke' 'ki' 'nâ' 'î' 'nî' 'ye' 'te' 'tu' 'tum' 'û' 'â' 'ûne' 'ne' 'tunne' 'tumâ'".split())
ONEK = set("'ve' 'fe' 'li' 'le' 'bi' 'ke' 'e' 'sin' 'yâ' 'eyy'".split())  # önek / nida edatları — kökü taşıyan sözcük değil
yok, var, ATLA, TAR = [], [], [], set()
for a in range(A, B + 1):
    for tr, q, items in veri.MK.get(a, []):
        for it in items:
            m = re.match(r"'([^']+)' '(.+?)' (?:karşılığı|açılımı) \((\d+)\. kelime", it)  # bölüm 4 kuralı 7: hemze / ayn ile biten lemma
            if not m:  # bölüm 5 kuralı 4: kök taşıyan edat / zarf biçimli kayıt "'X' N. kelimede 'Y' ile"
                m2 = re.match(r"('(?:[^']|'(?=[a-zâîûçğışöü]))+') (\d+)\. kelimede '([^']+)'(?: [a-zçğıöşü]+)? ile", it)
                if m2 and (a, int(m2.group(2))) in ROOT and m2.group(1) not in ZAM and m2.group(1) not in ONEK:
                    m = m2; t, lat, n = m2.group(3), m2.group(1), int(m2.group(2))
            if m and m.re.pattern.startswith("'([^']+)' '"):
                t, lat, n = m.group(1), m.group(2), int(m.group(3))
            if not m:
                if re.search(r"(?:karşılığı|açılımı) \(\d+\. kelime", it): ATLA.append(it[:40])
                continue
            TAR.add((a, n)); r = ROOT.get((a, n))
            if not r or r not in GL: continue
            g = kok(GL[r]); stem = kok(t).split()[0].rstrip('-')[:4]
            (var if stem and stem in g else yok).append("%d:%d:%d '%s' ← %s '%s'" % (S, a, n, t, r, GL[r]))
print('KAPSAMAYAN %d: ' % len(yok) + '; '.join(yok))
print('KAPSAYAN %d' % len(var))
MKS = {a: ' '.join(' '.join(x[2]) for x in veri.MK.get(a, [])) for a in range(A, B + 1)}
tar_yok = ['%d:%d:%d' % (S, a, n) for (a, n) in sorted(ROOT) if A <= a <= B and (a, n) not in TAR and not re.search(r'(?<!\d)%d\. kelime' % n, MKS[a])]
print('TARANMAYAN kök taşıyan kelime %d' % len(tar_yok) + ((' — ' + ', '.join(tar_yok)) if tar_yok else ''))
print('ATLANAN %d' % len(ATLA) + ((' — ' + ' | '.join(ATLA)) if ATLA else ''))
