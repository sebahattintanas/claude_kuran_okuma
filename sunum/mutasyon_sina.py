# bölüm 6 kuralları 4 / 6 / 15 ve 1, 2, 3, 5, 12 sınamaları: denetim araçları bozulmuş kopyada isabet vermeli, sağlam kayıtta vermemeli
# kullanım (/home/claude'dan): python3 sunum/mutasyon_sina.py — dosyalar sınamadan sonra geri yüklenir
import subprocess, shutil, sys
Y = '/home/claude/yamalar/'
def run(*a): return subprocess.run(['python3'] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout
SON = []
def mut(dosya, eski, yeni, arac, arg, aranan, ad):
    p = Y + dosya; s = open(p, encoding='utf-8').read(); shutil.copy(p, '/tmp/mut_yedek')
    assert eski in s, (ad, 'mutasyon kaynağı yok')
    open(p, 'w', encoding='utf-8').write(s.replace(eski, yeni))
    try: o = run('sunum/' + arac, *arg)
    finally: shutil.copy('/tmp/mut_yedek', p)
    SON.append((ad, aranan in o))
def var(arac, arg, aranan, ad):
    SON.append((ad, aranan in run('sunum/' + arac, *arg)))
mut('metin_5_37_40.txt', "'lehû' 3MS (adsız; gönderge lafız)", "'lehû' 3MS (gönderge lafız)", 'bolum4_kurallar.py', ['37', '40', '13'], "adsız etiketi yok 5:40 'lehû'", 'kural 15: adsız silinmiş 5:40 lehû')
mut('ariza_5_37_40.txt', "ayetler arası 5:38 / 5:39 ('fa'qta'û eydiyehumâ'", "ayetler arası 5:38 / 5:39 ('fa'qta'û eydiyehum'", 'bolum5_kurallar.py', ['37', '40', '13'], 'aday 1039 ayetler arası', 'kural 6: ayetler arası çift bozuk')
var('bolum4_kurallar.py', ['37', '40', '13'], 'A1 kapsamı 5:39 şahıs etiketli kelime A1 dışında: 9.', "kural 1: 5:39 'yetûbu'")
var('bolum5_kurallar.py', ['33', '36', '12'], "normalleştirilmiş lemma adı 'melek'", "kural 3: 'melek'")
var('bolum5_kurallar.py', ['33', '36', '12'], '5:34 5. kelime قبل', 'kural 4: 5:34 قبل aday')
var('bolum5_kurallar.py', ['37', '40', '13'], "ayetler arası ortak kalıp sayımsız 've lehum 'azâbun'", "kural 5: 've lehum 'azâb'")
var('bolum6_kurallar.py', ['37', '40', '13', '--tazelik-yok'], "çakışma grubu ARIZA'da yok: 'ceza' ←", "kural 2: 'ceza' grubu")
var('bolum6_kurallar.py', ['37', '40', '13', '--tazelik-yok'], "karar sayısı 2 (tam bir kapalı karar olmalı): KÖK 'yetir-'", "kural 2: KÖK 'yetir-' çift karar")
var('bolum6_kurallar.py', ['33', '36', '12', '--tazelik-yok'], "Türkçe alıntı MEAL dışı 5:34 'bilin'", "kural 12: 5:34 'bilin'")
var('bolum6_kurallar.py', ['37', '40', '13', '--tazelik-yok'], "Türkçe alıntı MEAL dışı 5:40 'dilediğine'", "kural 12: 5:40 'dilediğine'")
var('bolum6_kurallar.py', ['33', '36', '12', '--tazelik-yok'], 'esmâ kural sapması 5:33:32', 'kural 14: 5:33:32')
var('bolum6_kurallar.py', ['33', '36', '12', '--tazelik-yok'], "lemma dizisi adı 'fî dunyâ fî âxir 'azâb'", 'kural 16: joker')
var('bolum6_kurallar.py', ['33', '36', '12'], 'bayat araç çıktısı: ham LEM: ad', 'kural 7: blok 12 bayat ham LEM')
for ad, ok in SON: print(('tamam ' if ok else 'BAŞARISIZ ') + ad)
print('mutasyon sınaması: %d / %d' % (sum(ok for _, ok in SON), len(SON)))
