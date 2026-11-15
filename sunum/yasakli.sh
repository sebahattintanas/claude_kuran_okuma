# yasaklı sözcük ve Latin dışı harf taraması (bölüm 7 kuralı 11 + bölüm 8 kuralları 2 ve 8); ölçüm alıntısı 'xref üçü de boş' izinli
# kullanım: bash sunum/yasakli.sh yamalar/{metin,ariza,bag,cipa,esma_el}_4_A_B.txt
python3 - "$@" <<'PY0'
# bölüm 3 (sûre 5) denetimi kuralı 1: kelime sınırı Türkçe harf sınıfıyla (-w 'ğ' / 'ş' gibi harfleri sınır sayıyordu: 'anlamında değil' yanlış pozitifi)
import sys, re
H = "a-zçğıöşüâîûA-ZÇĞİÖŞÜ"
P = r"aynı|ilk|ikinci|tek|her ikisi|ikisi de|token|[0-9]+ ayette|[a-zçğıöşü]+ ayette|[0-9]+ ayetinde|[a-zçğıöşü]+ ayetinde|ikisinde de|kez|[a-zçğıöşü]+ü de|[a-zçğıöşü]+(?:nde|nda|sında|sinde) d[ae]|kelimede de|[a-zçğıöşü]+(?:üncü|ıncı|inci|uncu)|sûre [0-9]+ okun[a-zçğıöşü]*"
R = re.compile(r"(?<![%s])(?:%s)(?![%s])" % (H, P, H))
for f in sys.argv[1:]:
    for n, l in enumerate(open(f, encoding='utf-8'), 1):
        for m in R.finditer(l):
            if m.group(0) == 'üçü de': continue
            print('%s:%d:%s' % (f, n, m.group(0)))
PY0
# bölüm 9 kuralı 8 (sayı + iyelik, dağıtma) ve bölüm 10 kuralı 4 / 15 (metin dışı ad / terim); izinli nakarat3 kalıbı süzülür
grep -HnwoiE "ikisi|üçü|dördü|beşi|ikişer|üçer|dörder|peygamber|muhammed|ahmed|ruhsat|savaş bağlamı|korku namazı düzeni" "$@" | grep -v "üçü de" | while IFS= read -r l; do f=${l%%:*}; r=${l#*:}; n=${r%%:*}; sed -n "${n}p" "$f" | grep -qE "kalıp: (ikisi|üçü|dördü) süzgeç" && continue; [ "${r#*:}" = "üçü" ] && sed -n "${n}p" "$f" | grep -q "xref üçü de boş" && continue; echo "$l"; done
# bölüm 16 denetimi kuralı 10: 'önceki / sonraki ayet' ve çekimleri; tırnak içinde kalıp adı olarak anılması ("'sonraki ayet' kalıbı") izinli
grep -HnwoE "(önceki|sonraki) ayet[a-zçğıöşü]*" "$@" | while IFS= read -r l; do f=${l%%:*}; r=${l#*:}; n=${r%%:*}; w=${r#*:}; sed -n "${n}p" "$f" | grep -qF "'$w' kalıb" && continue; echo "$l"; done
python3 - "$@" <<'PY'
import sys, unicodedata as u
for f in sys.argv[1:]:
    t = open(f, encoding='utf-8').read()
    bad = [(i, c) for i, c in enumerate(t) if 'CYRILLIC' in u.name(c, '') or 'GREEK' in u.name(c, '')]
    if bad: print(f, 'Latin dışı harf:', bad[:5])
    import re as _re  # bölüm 1 (sûre 5) denetimi kuralı 7: wasl öncesi 've'' — 'va'' yazımı
    va = [m.group(0) for m in _re.finditer(r"(?<![a-zâîûçğışöüA-Z])va'[a-zâîûçğışöü-]+", t) if not t.startswith("' — wasl", m.end())]  # denetim bulgusunun alıntısı izinli
    if va: print(f, "wasl 'va'' yazımı:", sorted(set(va))[:8])
PY
echo "yasaklı tarama bitti"
