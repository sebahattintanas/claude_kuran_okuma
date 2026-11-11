# ARIZA 'bağ' maddesindeki 'önceki basım' listesi (bölüm 7 kuralı 12): ◇ sayımlarındaki 'okumada görüldü' numaraları − emsal − blok ayetleri
# kullanım: python3 sunum/onceki_basim.py A B "<emsal listesi boşlukla>"
import re, sys
A, B = int(sys.argv[1]), int(sys.argv[2]); em = set(sys.argv[3].split()) | {'4:%d' % i for i in range(A, B + 1)}
t = open('/home/claude/yamalar/metin_4_%d_%d.txt' % (A, B)).read()
nums = set()
for m in re.finditer(r'ayet: ([^;.]*?) \(okumada görüldü\)', t):
    nums |= set(re.findall(r'\d+:\d+', m.group(1)))
k = lambda a: tuple(map(int, a.split(':')))
print(', '.join(sorted(nums - em, key=k)) or '—')
