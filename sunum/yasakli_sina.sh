# yasakli.sh sabit sınaması (bölüm 5 kuralı 6): OLUMLU satır sayısı = isabet satırı, OLUMSUZ satırlarda isabet yok
cd /home/claude
O=$(bash sunum/yasakli.sh sunum/yasakli_test.txt | grep -c '^sunum/yasakli_test.txt:')
P=$(grep -c '^OLUMLU' sunum/yasakli_test.txt)
N=$(bash sunum/yasakli.sh sunum/yasakli_test.txt | grep '^sunum/yasakli_test.txt:' | cut -d: -f2 | sort -u | while read n; do sed -n "${n}p" sunum/yasakli_test.txt; done | grep -c OLUMSUZ)
L=$(bash sunum/yasakli.sh sunum/yasakli_test.txt | grep '^sunum/yasakli_test.txt:' | cut -d: -f2 | sort -u | wc -l)
echo "yasakli sınama: olumlu satır $P, isabetli satır $L, olumsuz satırda isabet $N"
[ "$L" = "$P" ] && [ "$N" = 0 ] && echo "yasakli sınama tamam" || echo "yasakli sınama HATA"
