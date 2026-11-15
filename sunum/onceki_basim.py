# ARIZA 'bağ' maddesindeki 'önceki basım' listesi (bölüm 7 kuralı 12): ◇ sayımlarındaki 'okumada görüldü' numaraları − emsal − blok ayetleri
# kullanım: python3 sunum/onceki_basim.py A B "<emsal listesi boşlukla>"
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys
A, B = int(sys.argv[1]), int(sys.argv[2]); em = set(sys.argv[3].split()) | {'%d:%d' % (S, i) for i in range(A, B + 1)}
t = open('/home/claude/yamalar/metin_%d_%d_%d.txt' % (S, A, B)).read()
nums = set()
for m in re.finditer(r'ayet: ([^;.]*?) \(okumada görüldü\)', t):
    nums |= set(re.findall(r'\d+:\d+', m.group(1)))
k = lambda a: tuple(map(int, a.split(':')))
print(', '.join(sorted(nums - em, key=k)) or '—')
