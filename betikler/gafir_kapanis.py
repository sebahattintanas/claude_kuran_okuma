# -*- coding: utf-8 -*-
"""gafir_kapanis.py — sûre 40 (Ğâfir) TUR SONU: kapanış bilançosu, çıpa tablosu, esmâ sûre profili, ilerleme.

Her sayı kayıttan koşulur (defter.json · esma_kayit.json · gafir_kayit.py · cipa_tarama4_adaylari.json).
İlerleme eski kuralla: TAM sûreler + 2:1-20 (secde_kapanis ile aynı), elle artırma YOK.
Esmâ profili bir KAYITTIR: ön-kayıt (notlar/ONKAYIT_esma_katmanlari.md) H1-H4 testleri tam okuma
bitmeden koşulmaz; burada oran, eşik, p-değeri YOK.
"""
import json
from collections import Counter
import blok_bilanco
from gafir_kayit import CIPA
import subprocess, sys
# önkoşul: esmâ kaydı tüm bloklar için güncel (aday 1006 oturumundaki sıralama hatası dersi)
for a, b in [(1,10),(11,20),(21,30),(31,40),(41,50),(51,60),(61,70),(71,80),(81,85)]:
    subprocess.run([sys.executable, 'esma_kayit.py', '40', str(a), str(b)], check=True, stdout=subprocess.DEVNULL)

S, N = 40, 85
REPO = '/home/claude/repo/notlar/'
D = {tuple(r['k']): r for r in json.load(open('defter.json', encoding='utf-8'))}
B = [D[(S, n)] for n in range(1, N + 1)]
E = json.load(open('esma_kayit.json', encoding='utf-8'))
EK = [E['%d:%d' % (S, n)] for n in range(1, N + 1)]
T = json.load(open('cipa_tarama4_adaylari.json', encoding='utf-8'))
tar = [x['ayet'] for x in T if x['ayet'].startswith('%d:' % S)]
assert len(EK) == N, 'esmâ kaydı eksik — DUR'

yk = Counter(blok_bilanco.yildiz_kaynagi(r)['kaynak'] for r in B if r['yildiz2'])
uc = Counter(blok_bilanco.yildiz_kaynagi(r)['kaynak'] for r in B if r['yildiz2'] == 3)
def _kaynak_1001(r):
    # aday 1001: kırık yalnız diğer bileşenler 1,5'i geçmezse ★ verir; toplanmaz
    z = r['z2']; diger = {k: v for k, v in z.items() if k != 'kafiye_kirik' and v >= 1.5}
    if z.get('kafiye_kirik') and not diger: return 'kafiye'
    return blok_bilanco.yildiz_kaynagi(r)['kaynak']
yk_d = Counter(_kaynak_1001(r) for r in B if r['yildiz2'])
etiket_1001 = [r['k'][1] for r in B if r['yildiz2'] and _kaynak_1001(r) != blok_bilanco.yildiz_kaynagi(r)['kaynak']]
muhur = [n for n in range(1, N + 1) if EK[n - 1]['muhur']]
gecerli = [n for n in range(1, N + 1) if blok_bilanco._muhur_gecerli('%d:%d' % (S, n), EK[n - 1])]
ton_gecerli = Counter(EK[n - 1]['ton'] for n in gecerli)
fs = Counter(r['fs'][2] for r in B)

bil = {
 'etiket': 'TAM SAYIM — sûre 40, 85 ayet',
 'kelime_toplam': sum(r['n'] for r in B),
 'lafiz_token': sum(len(r['A']) for r in B), 'lafiz_ayet': sum(1 for r in B if r['A']),
 'rab_token': sum(len(r['R']) for r in B), 'rab_ayet': [r['k'][1] for r in B if r['R']],
 'A_R_orani': round(sum(len(r['A']) for r in B) / max(1, sum(len(r['R']) for r in B)), 2),
 'yildiz': {str(k): v for k, v in sorted(Counter(r['yildiz2'] for r in B).items())},
 'yildiz_kaynak_tum': dict(yk), 'yildiz_kaynak_duzeltilmis': dict(yk_d), 'etiket_1001_ayet': etiket_1001, 'ucyildiz_kaynak': dict(uc),
 'edilgen_ayet': sum(1 for r in B if r['pas']),
 'iltifat_ayet': [r['k'][1] for r in B if r['ilt']],
 'hapaks_ayet': [r['k'][1] for r in B if r['hapaks2']],
 'mm2_ayet': [r['k'][1] for r in B if r['mm2']],
 'fasila_sinif': dict(fs), 'kafiye_kirik': [r['k'][1] for r in B if r['z2'].get('kafiye_kirik')],
 'en_uzun': max(((r['n'], r['k'][1]) for r in B)),
 'en_uzun_esit': [r['k'][1] for r in B if r['n'] == max(x['n'] for x in B)],
 'en_kisa_esit': [r['k'][1] for r in B if r['n'] == min(x['n'] for x in B)],
 'say_isareti': {k: v for a, b in [(1,10),(11,20),(21,30),(31,40),(41,50),(51,60),(61,70),(71,80),(81,85)] for k, v in blok_bilanco.bilanco(S, a, b)['say_isareti'].items()},
}
cipa = {
 'isaretli': {str(k): v for k, v in sorted(CIPA.items())},
 'L4': [n for n, v in CIPA.items() if v.get('cipa')],
 'tarayici_v4_aday': tar,
 'anma': '%d/%d' % (sum(1 for n, v in CIPA.items() if v.get('cipa') and '%d:%d' % (S, n) in tar),
                    sum(1 for v in CIPA.values() if v.get('cipa'))),
 'kesinlik': '%d/%d' % (sum(1 for a in tar if CIPA.get(int(a.split(':')[1]), {}).get('cipa')), len(tar)),
}
esma = {
 'uyari': 'KAYIT — ölçüm değil. H1-H4 tam okuma bitince, global Bonferroni ile.',
 'sinif_oto': dict(Counter(x['sinif_oto'] for x in EK)),
 'sinif_el': dict(Counter(x['sinif_el'] for x in EK)),
 'esma_token_oto': sum(len(x['esma']) for x in EK),
 'esma_token_ilahi': sum(1 for x in EK for v in x['esma_el'].values() if v == 'ilahi'),
 'muhur_43': len(muhur), 'muhur_43_gecerli': len(gecerli), 'muhur_43_yanlis': sorted(set(muhur) - set(gecerli)),
 'ton_gecerli_muhur': dict(ton_gecerli),
 'bant': 'KAPI_KAPALI (§4.4, aday 435)',
}
KAP = {'_bilanco_sure': bil, '_cipa_tablosu_40': cipa, '_esma_profil_40': esma,
       '_kapanis_notu': ("SÛRE 40 TUR SONU. Blok başı kayıt sekizinci kez bir sûrenin tamamında uygulandı (9 blok; son blok 81-85, 5 ayet). "
                         "Ek mercekler (◈K ◈B ◈D ◈A) sûrenin 85 ayetinin tamamında; her blokta tetik taraması (tetik2) — iki blokta ilk koşuda uyuşmaz (31-40: 40:34; 51-60: 40:55, 40:59), kayıttan önce düzeltildi; kayıtta 0. "
                         "Kayıt sayımı denetimi: mercek metinlerindeki [x/y] kök sayımları ölçüm satırıyla karşılaştırıldı (549 sayım, 0 uyuşmaz). "
                         "Karşıt çift notu (aday 1039, okuma kolu) 85 ayetin hepsinde yazıldı; dolu olan 33 ayet. "
                         "Çıpa: L4 yok; en yüksek kademe L2 (40:61 gece/gündüz işlevi — 27:86 emsali; 40:67 toprak → nutfe → alaka → bebek → güçlü çağ → yaşlılık, L4 süreç koluna sınırda, KAPATILAMAZ). Tarayıcı v4 adayları 5, isabet 0. "
                         "Yeni aday 1040 (blok 1-10, okuma gözlemi): ardışık sûre sınırında süreklilik (39:1 → 40:2 tenzîl; 39:75 → 40:7 Arş/tesbih) — test korpus sonunda, önceden yazıldı; 40:85 → 41:1 sınırı sûre 41 okunmadan yazılmadı. "
                         "Sûrenin adı (ğâfir) lemma olarak korpusta 2 ayette: 7:155 (çoğul), 40:3. "
                         "Okumada görülen sûre içi dizi ve çerçeveler (KAPATILAMAZ, sayı iddiası değil): 'ellezîne yucâdilûne fî âyâti'llâh' 3 ayet (40:35, 56, 69) üç yüklemle; 'allâhu'llezî ce'ale lekum' 3 ayet (40:61, 64, 79); 'lâkinne ekserâ'n-nâsi lâ …' 3 ayet (40:57, 59, 61) üç fiille; 'fasbir inne va'da'llâhi haqq' 2 ayet (40:55, 77); 40:21 ↔ 40:82 yeryüzünde gezme kalıbı (nakarat3 8 kelime); 40:12 ↔ 40:84 aynı dört kök (وحد, كفر, شرك, أمن) ters dizilişte; edilgen 'çevrilme' üç kez (40:62, 63, 69). "
                         "Düzeltme kaydı 1: 40:30 meali tırnağı erken kapattı (alıntı 40:31-33'te sürüyor) — özgün alan korunur. "
                         "Araç açıkları ARIZA alanlarında: gloss eksikleri (حول çevre, بني oğul, قوم üç anlam, سمو ad, شدد eşudd, حمم yakın dost, نور hep nâr, أيي eyye, أثر âsâr), "
                         "takdim ve ayırma zamiri biçimde işaretsiz (517), alıntı sınırları işaretsiz (1017: 40:7-9, 40:28-44 konuşmaları, 40:66, 40:73-76), "
                         "ölçüm satırı esmâ ile esma_kayit ayrışması (1022: 40:44, 40:65, 40:76), tek fiilli ayette edilgen oranından ★★★ (924: 40:62, 40:71, 40:72), kafiye kırığı ★ kaynağı (1001: 40:23, 29, 30), 40:1 besmele ayet metnine bitişik (n=1, en kısa). "
                         "Karar bekleyen (kullanıcı kararıyla açık): S2 ◈K tetik فلك kesinliği (40:80 fulk — gemi); مأي gloss.")}

p = REPO + 'okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
assert len([k for k in OM[str(S)] if not k.startswith('_')]) == N, 'sûre 40 kaydı eksik — DUR'
OM[str(S)].update(KAP)
I = OM['ilerleme']
I['tam'] = sorted(set(I['tam']) | {S})
I['kismi'].pop(str(S), None)
okunan = sum(1 for r in D.values() if r['k'][0] in set(I['tam']) or (r['k'][0] == 2 and r['k'][1] <= 20))
I['okunan_ayet'] = okunan
I['korpus_yuzde'] = round(100 * okunan / len(D), 1)
I['not'] = "Sûre 1, 9-39 ve **40 TAM**. Devam: sûre 41'den ya da sûre 2'nin 21. ayetinden."
I['son_oturum'] = 'OKU_BENI_OTURUM.md (sûre 40 tur sonu)'
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
subprocess.run([sys.executable, 'duzeltme_40.py'], check=True)

E['_profil_40'] = esma
json.dump(E, open('esma_kayit.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)

print(json.dumps({'bilanco': bil, 'cipa': cipa, 'esma': esma}, ensure_ascii=False, indent=1))
print('ilerleme:', okunan, '(%', I['korpus_yuzde'], ')  tam:', I['tam'][-3:])
