# -*- coding: utf-8 -*-
"""emsal.py — emsal listesini okuma_metni.json'dan basar (Arapça + Türkçe meal). OTURUM DIŞI yardımcı.
Elle Arapça / meal yazılmaz: ikisi de kayıttaki 'ar' ve 'meal' alanından gelir.
DUR koşulları: 'S:A' kaydı yok, kayıtta 'ar' ya da 'meal' yok, ayet bu oturumda zaten basılmış (basilan.txt).
Kullanım: python3 emsal.py [--isaretle] [--cikti dosya] S:A [S:A ...]
  --isaretle : liste sohbete GÖNDERİLDİKTEN SONRA koşulur; ayetleri basilan.txt'e ekler (basmaz).
"""
import sys, json, unicodedata as ud, os

OM_YOL = '/home/claude/repo/notlar/okuma_metni.json'
BASILAN = '/home/claude/sunum/basilan.txt'
args = sys.argv[1:]
isaretle = '--isaretle' in args
cikti = None
if '--cikti' in args:
    cikti = args[args.index('--cikti') + 1]
    args = [a for a in args if a != cikti]
refs = [a for a in args if not a.startswith('--')]
assert refs, 'ayet verilmedi'
basilan = set()
if os.path.exists(BASILAN):
    basilan = {l.strip() for l in open(BASILAN, encoding='utf-8') if l.strip()}

if isaretle:
    yeni = [r for r in refs if r not in basilan]
    with open(BASILAN, 'a', encoding='utf-8') as f:
        for r in yeni:
            f.write(r + '\n')
    print('basilan.txt +%d (toplam %d)' % (len(yeni), len(basilan) + len(yeni)))
    sys.exit()

OM = json.load(open(OM_YOL, encoding='utf-8'))
out = []
for r in refs:
    s, a = r.split(':')
    assert r not in basilan, 'DUR: %s bu oturumda zaten basıldı — yeniden basılmaz' % r
    rec = OM.get(s, {}).get(r)
    assert isinstance(rec, dict), "DUR: '%s' kaydı okuma_metni'nde yok" % r
    assert rec.get('ar') and rec.get('meal'), "DUR: '%s' kaydında 'ar' / 'meal' yok" % r
    out.append('**%s**\n\n## %s\n\n%s\n' % (r, ud.normalize('NFC', rec['ar']), rec['meal']))
metin = '\n'.join(out)
if cikti:
    open(cikti, 'w', encoding='utf-8').write(metin)
print(metin)
