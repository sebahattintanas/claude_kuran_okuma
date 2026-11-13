# yasaklı sözcük ve Latin dışı harf taraması (bölüm 7 kuralı 11 + bölüm 8 kuralları 2 ve 8); ölçüm alıntısı 'xref üçü de boş' izinli
# kullanım: bash sunum/yasakli.sh yamalar/{metin,ariza,bag,cipa,esma_el}_4_A_B.txt
grep -nwoE "aynı|ilk|ikinci|tek|her ikisi|ikisi de|token|[0-9]+ ayette|[a-zçğıöşü]+ ayette|[0-9]+ ayetinde|[a-zçğıöşü]+ ayetinde|ikisinde de|kez|[a-zçğıöşü]+ü de|[a-zçğıöşü]+(nde|nda|sında|sinde) d[ae]|kelimede de|[a-zçğıöşü]+(üncü|ıncı|inci|uncu)" "$@" | grep -v "üçü de"
# bölüm 9 kuralı 8 (sayı + iyelik, dağıtma) ve bölüm 10 kuralı 4 / 15 (metin dışı ad / terim); izinli nakarat3 kalıbı süzülür
grep -nwoiE "ikisi|üçü|dördü|beşi|ikişer|üçer|dörder|peygamber|muhammed|ahmed|ruhsat|savaş bağlamı|korku namazı düzeni" "$@" | grep -v "üçü de" | while IFS= read -r l; do f=${l%%:*}; r=${l#*:}; n=${r%%:*}; sed -n "${n}p" "$f" | grep -qE "kalıp: (ikisi|üçü|dördü) süzgeç" && continue; [ "${r#*:}" = "üçü" ] && sed -n "${n}p" "$f" | grep -q "xref üçü de boş" && continue; echo "$l"; done
python3 - "$@" <<'PY'
import sys, unicodedata as u
for f in sys.argv[1:]:
    t = open(f, encoding='utf-8').read()
    bad = [(i, c) for i, c in enumerate(t) if 'CYRILLIC' in u.name(c, '') or 'GREEK' in u.name(c, '')]
    if bad: print(f, 'Latin dışı harf:', bad[:5])
PY
echo "yasaklı tarama bitti"
