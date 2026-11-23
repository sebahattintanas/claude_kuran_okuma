import re,sys
olc=open(sys.argv[1],encoding='utf-8').read().replace('**','')
bad=0
for f in sys.argv[2:]:
    t='\n'.join(l for l in open(f,encoding='utf-8').read().splitlines() if not re.match(r"\s*['\"](?:bölüm (?:denetimi \(|\d+ denetiminden)|araç kuralı önerileri)",l))  # bölüm 17 denetimi: BEK (bekleyen_ariza) maddeleri ölçüm alıntısı değil
    for q in re.findall(r"'([^']*)' — satır aynen",t):
        ok=q in olc; bad+= not ok
        print(('OK ' if ok else 'YOK'),f.split('/')[-1],q[:80])
print('uyuşmayan:',bad)
