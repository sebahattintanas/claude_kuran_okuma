# bölüm 6 kuralı 10: grep kısımları büyük / küçük harf duyarsız ((Ö|ö)nceki / (S|s)onraki + (A|a)yet); dosyaya özgü izinler eklendiği bloğun öz denetim maddesinde anılır
# yasaklı sözcük ve Latin dışı harf taraması (bölüm 7 kuralı 11 + bölüm 8 kuralları 2 ve 8); ölçüm alıntısı 'xref üçü de boş' izinli
# sınama: bash sunum/yasakli.sh sunum/yasakli_test.txt — 'OLUMLU' satırlarının hepsi isabet, 'OLUMSUZ' satırları 0 vermeli (sunum/yasakli_sina.sh)
# kullanım: bash sunum/yasakli.sh yamalar/{metin,ariza,bag,cipa,esma_el}_4_A_B.txt
python3 - "$@" <<'PY0'
# blok 33: 'beşi' sayı + iyelik dalı 'beşik' adını dışlar (yanlış pozitif; sunum/yasakli_test.txt OLUMSUZ satırı)
# bölüm 3 (sûre 5) denetimi kuralı 1: kelime sınırı Türkçe harf sınıfıyla (-w 'ğ' / 'ş' gibi harfleri sınır sayıyordu: 'anlamında değil' yanlış pozitifi)
import sys, re, os, fnmatch
H = "a-zçğıöşüâîûA-ZÇĞİÖŞÜ"
P = r"aynı|ilk|ikinci|tek|her ikisi|ikisi de|token|[0-9]+ ayette|[a-zçğıöşü]+ ayette|[0-9]+ ayetinde|[a-zçğıöşü]+ ayetinde|ikisinde de|kez|[a-zçğıöşü]+ü de|[a-zçğıöşü]+(?:nde|nda|sında|sinde) d[ae]|kelimede de|[a-zçğıöşü]+(?:üncü|ıncı|inci|uncu)|sûre [0-9]+ okun[a-zçğıöşü]*|(?:ikisin|üçün|dördün|beşin|altısın)[a-zçğıöşü]*|(?:[0-9]+|iki|üç|dört|beş|altı|yedi|sekiz|dokuz|on) ayetin[a-zçğıöşü]*"  # bölüm 4 kuralı 12
P += r"|(?:bir|iki|üç|dörd|beş|altı|yedi|sekiz|dokuz|on|son|yirmi|otuz|kırk|elli)(?:üncü|ıncı|inci|uncu)[a-zçğıöşü]+|(?:ikisi|üçü|dördü|beşi(?!k)|altısı|yedisi|sekizi|dokuzu)[a-zçğıöşü]*|bir(?:i|ini|inin|ine|inde|inden|isi|isini|isinin|isinde|isine)|birer|ikişer|üçer|dörder|altışar|yedişer|sekizer|dokuzar"  # bölüm 5 kuralı 6: 'bir'–'dokuz' + iyelik, sıra sayısı + ek, dağıtma ('beşer' insan anlamıyla eş biçimli, 'on' + iyelik 'onu' zamirle eş biçimli, taranmaz)
IZIN = (('*', "'biri' (5:27:12)"), ('*', "'birer' dağıtma"), ('*', "\\'birer\\' dağıtma"), ('*', 'üçü de'), ('*', 'kalıp: ikisi süzgeç'), ('*', 'kalıp: üçü süzgeç'), ('*', 'kalıp: dördü süzgeç'), ('*', 'xref üçü de boş'), ('*', "'bozguncu'"), ('ariza_5_*.txt', "'biri' (okunmuş 1 konum)"), ('*_5_71_74.txt', "'şüphesiz allah üçün üçüncüsüdür'"), ('ariza_5_71_74.txt', "'üçüncü' 'sâlis'"), ('ariza_5_71_74.txt', "ile 'üçüncüsü'"), ('ariza_5_71_74.txt', "('üçüncüsüdür' içinde"), ('ariza_5_71_74.txt', "ile 'üçün'"), ('ariza_5_71_74.txt', "'üçüncü' ← ثلث"), ('bekleyen_ariza_5_b24.txt', "'üçün üçüncüsüdür' tırnaksız"), ('ariza_5_78_81.txt', "'üçün üçüncüsüdür' tırnaksız"), ('ariza_5_109_110.txt', "'beşikte de olgunluk çağında da insanlarla'"), ('ariza_5_111_115.txt', "'ilk, evvel'"), ('ariza_6_12_15.txt', "'ilk, evvel'"), ('ariza_6_25_28.txt', "'ilk, evvel'"), ('ariza_6_161_165.txt', "'ilk, evvel'"), ('ariza_6_59_61.txt', "'nihayet onlardan birine ölüm geldiğinde'"), ('ariza_6_59_61.txt', "'birinize' / 'onlardan birine' zamir farkı"))  # bölüm 10 denetimi kuralı 10: (dosya deseni, metin) çifti — '*' yalnız eski izinlerde, yeni izin tırnaklı; 'bozguncu' (fâil adı, 'mufsid' karşılığı) sıra sayısı eki değil; blok 23: es_lemma numarasız çıktısındaki 'biri' karşılığı; 'sâlisu selâse' karşılığı (kök karşılığı, 'evvel' → 'ilk' emsali); blok 33: 3:46 emsal alıntısı ('de … da' bağlacı — sayma kalıbı değil); blok 34: gloss_tara çıktısındaki أول kök anlamı (araç çıktısı aynen)
R = re.compile(r"(?<![%s])(?:%s)(?![%s])" % (H, P, H))
for f in sys.argv[1:]:
    for n, l in enumerate(open(f, encoding='utf-8'), 1):
        lo = l.replace('İ', 'i').replace('I', 'ı').lower()  # bölüm 5 kuralı 6: büyük / küçük harf duyarsız (Türkçe İ / I)
        for g, z in IZIN:
            if fnmatch.fnmatch(os.path.basename(f), g): lo = lo.replace(z, '#' * len(z))
        for m in R.finditer(lo):
            if m.group(0) == 'üçü de': continue
            print('%s:%d:%s' % (f, n, m.group(0)))
PY0
# bölüm 9 kuralı 8 (sayı + iyelik, dağıtma) ve bölüm 10 kuralı 4 / 15 (metin dışı ad / terim); izinli nakarat3 kalıbı süzülür
grep -HnwoiE "ikisi|üçü|dördü|beşi|ikişer|üçer|dörder|peygamber|muhammed|ahmed|ruhsat|savaş bağlamı|korku namazı düzeni" "$@" | grep -v "üçü de" | while IFS= read -r l; do f=${l%%:*}; r=${l#*:}; n=${r%%:*}; sed -n "${n}p" "$f" | grep -qE "kalıp: (ikisi|üçü|dördü) süzgeç" && continue; [ "${r#*:}" = "üçü" ] && sed -n "${n}p" "$f" | grep -q "xref üçü de boş" && continue; echo "$l"; done
# bölüm 16 denetimi kuralı 10: 'önceki / sonraki ayet' ve çekimleri; tırnak içinde kalıp adı olarak anılması ("'sonraki ayet' kalıbı") izinli
grep -HnwoE "([Öö]nceki|[Ss]onraki) [Aa]yet[a-zçğıöşü]*" "$@" | while IFS= read -r l; do f=${l%%:*}; r=${l#*:}; n=${r%%:*}; w=${r#*:}; sed -n "${n}p" "$f" | grep -qF "'$w' kalıb" && continue; echo "$l"; done
python3 - "$@" <<'PY'
import sys, unicodedata as u
for f in sys.argv[1:]:
    t = open(f, encoding='utf-8').read()
    bad = [(i, c) for i, c in enumerate(t) if 'CYRILLIC' in u.name(c, '') or 'GREEK' in u.name(c, '')]
    if bad: print(f, 'Latin dışı harf:', bad[:5])
    import re as _re  # bölüm 1 (sûre 5) denetimi kuralı 7: wasl öncesi 've'' — 'va'' yazımı
    va = [m.group(0) for m in _re.finditer(r"(?<![a-zâîûçğışöüA-Z])va'[a-zâîûçğışöü-]+", t) if not t.startswith("' — wasl", m.end())]  # denetim bulgusunun alıntısı izinli
    if va: print(f, "wasl 'va'' yazımı:", sorted(set(va))[:8])
    # bölüm 8 kuralı 16: art arda eş sözcük (yer tutucu + sabit metin çiftlemesi, örn. 'sapma sapma'); tırnaklı karşılık eşleri ('kâfir' 'kâfir') ve Türkçe ikilemeler izinli
    IKI = {'ayet ayet', 'grup grup', 'parça parça', 'şaşkın şaşkın', 'kalıp kalıp', 'blok blok', 'türlü türlü', 'bile bile', 'bölük bölük'}
    for m in _re.finditer(r"(?<![a-zçğıöşüâîûA-ZÇĞİÖŞÜ'])([a-zçğıöşüâîûA-ZÇĞİÖŞÜ]{2,}) \1(?![a-zçğıöşüâîûA-ZÇĞİÖŞÜ'])", t):
        _sat = t.splitlines()[t.count('\n', 0, m.start())] if t else ''
        if _re.search(r"bölüm (?:denetimi \(|\d+ denetiminden)", _sat): continue  # bekleyen denetim bulgusu aynen taşınır (alıntılanan yapıntı izinli)
        if m.group(0).lower() not in IKI: print('%s:%d:art arda eş sözcük: %s' % (f, t.count('\n', 0, m.start()) + 1, m.group(0)))
PY
echo "yasaklı tarama bitti"
