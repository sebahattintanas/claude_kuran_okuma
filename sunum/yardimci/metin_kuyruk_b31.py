out = ['# ── blok 6:131-135 (2026-11-22) ──', 'MEAL31 = {']
for n in range(131, 136):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M31 = {']
for n in range(131, 136):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL31); M.update(M31)']
open('/home/claude/yamalar/metin_6_131_135.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
