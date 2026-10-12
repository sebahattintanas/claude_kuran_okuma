# -*- coding: utf-8 -*-
"""fussilet_kapanis.py — sûre 41 (Fussilet) TUR SONU: kapanış bilançosu, çıpa tablosu, esmâ sûre profili, ilerleme.

Her sayı kayıttan koşulur (defter.json · esma_kayit.json · fussilet_kayit.py · cipa_tarama4_adaylari.json).
İlerleme eski kuralla: TAM sûreler + 2:1-20 (secde_kapanis ile aynı), elle artırma YOK.
Esmâ profili bir KAYITTIR: ön-kayıt (notlar/ONKAYIT_esma_katmanlari.md) H1-H4 testleri tam okuma
bitmeden koşulmaz; burada oran, eşik, p-değeri YOK.
"""
import json
from collections import Counter
import blok_bilanco
from fussilet_kayit import CIPA
import subprocess, sys
# önkoşul: esmâ kaydı tüm bloklar için güncel (aday 1006 oturumundaki sıralama hatası dersi)
for a, b in [(1,10),(11,20),(21,30),(31,40),(41,50),(51,54)]:
    subprocess.run([sys.executable, 'esma_kayit.py', '41', str(a), str(b)], check=True, stdout=subprocess.DEVNULL)

S, N = 41, 54
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
 'etiket': 'TAM SAYIM — sûre 41, 54 ayet',
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
 'say_isareti': {k: v for a, b in [(1,10),(11,20),(21,30),(31,40),(41,50),(51,54)] for k, v in blok_bilanco.bilanco(S, a, b)['say_isareti'].items()},
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
KAP = {'_bilanco_sure': bil, '_cipa_tablosu_41': cipa, '_esma_profil_41': esma,
       '_kapanis_notu': ("SÛRE 41 TUR SONU. Blok başı kayıt dokuzuncu kez bir sûrenin tamamında uygulandı (6 blok; son blok 51-54, 4 ayet). "
                         "Ek mercekler (◈K ◈B ◈D ◈A) sûrenin 54 ayetinin tamamında; her blokta tetik taraması (tetik2) — altı blokta da ilk koşuda 0 uyuşmaz. "
                         "Karşıt çift notu (aday 1039, okuma kolu) 54 ayetin hepsinde yazıldı; dolu olan 28 ayet. "
                         "Çıpa: L4 yok; en yüksek kademe L2 (41:39 yer 'hâşi'a' → su → 'ihtezzet ve rabet', L3 görünüş/durum koluna sınırda, KAPATILAMAZ; 22:5 aynı terkip). Tarayıcı v4 adayları 6 (41:13, 15, 16, 24, 37, 38), isabet 0. "
                         "Aday 1040 alanında sınır kaydı: 40:2 → 41:2 (tenzîl + kaynak), 40:85 → 41:7 (kâfirûn) — test korpus sonunda; 41:54 → 42:1 sınırı sûre 42 okunmadan yazılmadı. "
                         "Sûrenin adı (fussilet) 41:3 ve 41:44'te; harekesiz kalıp 11:1 ile de eşleşiyor (12:94 'fasalat' gürültü). "
                         "Okumada görülen sûre içi dizi ve çerçeveler (KAPATILAMAZ, sayı iddiası değil): 'beyne yedeyhi … halfih' ikilisi üç kez üç özneyle (41:14 elçiler, 41:25 yakın dostlar, 41:42 bâtıl); "
                         "organların şahitliği 41:20-22 (kulak, göz, deri; 3MP → 2MP), شهد kökü 41:53 'şehîd' ile kapanıyor; 'qâle'llezîne keferû' iki alıntı (41:26 dünya, 41:29 âhiret); "
                         "'mine'l-cinni ve'l-ins' 2 kez (41:25, 29); 've min âyâtih' 2 kez (41:37, 39); 'messehu'ş-şerr' 2 kez (41:49 umutsuzluk, 41:51 geniş dua; 17:83 tek ayette birinciyi taşıyor); "
                         "41:5 inkârcıların 'fî âzâninâ vaqr' sözü 41:44'te 'fî âzânihim vaqr' olarak dönüyor; 41:45 = 11:110 kelimesi kelimesine (esit2 1,0000); 41:41 'inne'nin haberi metinde yok; 41:38 secde işareti; "
                         "fâsıla 41:1-38 ن/م, 41:39-40 ر, 41:41-54 sık değişiyor (ز د م د ب د د ص ط ظ ض د د ط); kafiye kırığı kaydı bilançoda. "
                         "Kayıt düzeltmesi yok (DUZELTME boş). Sohbet düzeltmesi 1: 41:11-20 bilançosunun sohbetteki 'edilgen' maddesi karışık yazıldı; kayıt [14, 16, 19] — 41:21-30 blok sonunda düzeltildi. "
                         "Bu sûrede kök tablosuna 7 kök eklendi (kok_ekle_41: قوت, دخن, نحس, قيض, سأم, كمم, أفق); retroaktif gloss yaması 0. "
                         "Tekrarlayan arıza aileleri (ayet listeleri blok ARIZA kayıtlarında): alıntı sınırları ve şahıs geçişleri ölçüm satırında iltifât 0 (1017), "
                         "ölçüm satırı esmâ ile esma_kayit ayrışması (1022), çok anlamlı kök gloss'u (1021), takdim / şart / soru biçimi ölçümde yok (517), kafiye kırığı ★ kaynağı (1001). "
                         "Karar bekleyen (kullanıcı kararıyla açık): S2 ◈K tetik فلك kesinliği; مأي gloss.")}

p = REPO + 'okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
assert len([k for k in OM[str(S)] if not k.startswith('_')]) == N, 'sûre 41 kaydı eksik — DUR'
OM[str(S)].update(KAP)
I = OM['ilerleme']
I['tam'] = sorted(set(I['tam']) | {S})
I['kismi'].pop(str(S), None)
okunan = sum(1 for r in D.values() if r['k'][0] in set(I['tam']) or (r['k'][0] == 2 and r['k'][1] <= 20))
I['okunan_ayet'] = okunan
I['korpus_yuzde'] = round(100 * okunan / len(D), 1)
I['not'] = "Sûre 1, 9-40 ve **41 TAM**. Devam: sûre 42'den ya da sûre 2'nin 21. ayetinden."
I['son_oturum'] = 'OKU_BENI_OTURUM.md (sûre 41 tur sonu)'
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
subprocess.run([sys.executable, 'duzeltme_41.py'], check=True)

E['_profil_41'] = esma
json.dump(E, open('esma_kayit.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)

print(json.dumps({'bilanco': bil, 'cipa': cipa, 'esma': esma}, ensure_ascii=False, indent=1))
print('ilerleme:', okunan, '(%', I['korpus_yuzde'], ')  tam:', I['tam'][-3:])
