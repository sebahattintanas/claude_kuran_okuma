# -*- coding: utf-8 -*-
"""ahkaf_kapanis.py — sûre 46 (Ahkâf) TUR SONU: kapanış bilançosu, çıpa tablosu, esmâ sûre profili, ilerleme.

Her sayı kayıttan koşulur (defter.json · esma_kayit.json · ahkaf_kayit.py · cipa_tarama4_adaylari.json).
İlerleme eski kuralla: TAM sûreler + 2:1-20 (secde_kapanis ile aynı), elle artırma YOK.
Esmâ profili bir KAYITTIR: ön-kayıt (notlar/ONKAYIT_esma_katmanlari.md) H1-H4 testleri tam okuma
bitmeden koşulmaz; burada oran, eşik, p-değeri YOK.
"""
import json
from collections import Counter
import blok_bilanco
from ahkaf_kayit import CIPA
import subprocess, sys
# önkoşul: esmâ kaydı tüm bloklar için güncel (aday 1006 oturumundaki sıralama hatası dersi)
for a, b in [(1,10),(11,20),(21,30),(31,35)]:
    subprocess.run([sys.executable, 'esma_kayit.py', '46', str(a), str(b)], check=True, stdout=subprocess.DEVNULL)

S, N = 46, 35
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
 'etiket': 'TAM SAYIM — sûre 46, 35 ayet',
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
 'say_isareti': {k: v for a, b in [(1,10),(11,20),(21,30),(31,35)] for k, v in blok_bilanco.bilanco(S, a, b)['say_isareti'].items()},
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
KAP = {'_bilanco_sure': bil, '_cipa_tablosu_46': cipa, '_esma_profil_46': esma,
       '_kapanis_notu': ("SÛRE 46 TUR SONU. Blok başı kayıt on dördüncü kez bir sûrenin tamamında uygulandı (4 blok; son blok 31-35, 5 ayet). "
"Ek mercekler (◈K ◈B ◈D ◈A) sûrenin 35 ayetinin tamamında; tetik taraması oturum_tetik.py ile: dört blokta da ilk koşuda 0 uyuşmaz. Her blokta [x/y] sayımları oturum_xy.py ile ölçüm satırına karşı denetlendi: 0 uyuşmaz. "
"Karşıt çift notu (aday 1039, okuma kolu) 35 ayetin hepsinde yazıldı. "
"Esmâ bilanço iddiaları her blokta okuyucu kararı eklendikten SONRA koşulan bilançodan yazıldı (sûre 45 dersi); geçerli mühür 46:2, 8, 33; mühür yanlış 46:7, 9, 17, 32. "
"Çıpa: 46:15 L4 adayı, TARTIŞMALI — ölçü kolu tek başına ('selâsûne şehrâ', 'erba'îne sene'; mekanizma yok), 31:14 emsali; tarayıcı v4 isabet. 46:24 ('âridun mumtırunâ' / 'bel huve … rîhun') ve 46:35 ('ke-ennehum … sâ'aten min nehâr') L3 koluna sınırda, karşılaştırma ya da durum söylenmiyor — L1, KAPATILAMAZ. Tarayıcı v4 adayları 46:4 (L0), 46:33 (L1), 46:35 (L1) çıpa değil. "
"Sûrenin adı ('ahqâf') korpusta yalnız 46:21'de (hapaks, ★★★). Fâsıla: 46:33 ر kafiye kırılması; öbür 34 ayetin son harfi ن 26, م 8. "
"Aday 1041 alanında kayıt (test yok): شهد 46:8 'şehîd' (Allah) / 46:10 'şâhid'; وعد 46:16-17 Allah'ın vaadi / anne babanın vaadi (aynı kök, farklı kalıp; sınırda); 'velî' 42:9 (Allah) / 46:32 'evliyâ'' (Allah'tan başkası). "
"Aday 1040 alanında sınır kaydı: 45:37 → 46:1-2 ('el-azîz el-hakîm'; 46:1-2 = 45:1-2 esit2 TAM; Hâ Mîm dizisinin son sûresi); 46:35 → 47:1 henüz okunmadı. Test korpus sonunda. "
"Okumada görülen dizi ve çerçeveler (KAPATILAMAZ, sayı iddiası değil): 46:3 / 46:33 gökler-yer yaratması (1P / 3MS lafız); 46:20 / 46:34 aynı açılıştan iki alıntı; 46:12 / 46:30 Mûsâ'nın kitabı 'önce' / 'sonra'; 41:52'nin iki parçası 46:5 ve 46:10'da; 11:17 sırası (şahit, Mûsâ'nın kitabı) 46:10 → 46:12; "
"29:8 + 31:14 + 27:19 + 41:33 → 46:15 (31:14 'iki yıl' / 46:15 'otuz ay', hesap metinde yok); 17:23 → 46:17 ('uff'); 41:14 + 26:135 → 46:21 (Âd; kardeş adsız, 11:50 ve 26:124'te adlı); 11:29, 11:32 (Nûh anlatısı) → 46:22-23; 16:78, 23:78, 32:9 → 46:26 (üç organ, şükür yerine 'yarar sağlamadı'); 17:99 → 46:33; 10:45 → 46:35. "
"Kayıt düzeltmesi yok (DUZELTME boş). Okuma iddiası denetimi: ölçümün esmâ satırı ile esma_kayit ayrışması her blokta ayrı yazıldı (46:17 'evvel' ölçümde yok; 46:32-33 ölçümde MÜHÜRSÜZ). "
"Bu sûrede kök tablosuna 3 kök eklendi (kok_ekle_46: بدع, حقف, عيي); retroaktif gloss yaması 0. "
"Tekrarlayan arıza aileleri (ayet listeleri blok ARIZA kayıtlarında): adsız konuşan ve muhatap ('qul' muhatabı, alıntı içi 1S, 46:17 'ellezî', 46:21 Âd'ın kardeşi, 46:24 ve 46:34 söyleyen) ve şahıs geçişleri ölçüm satırında iltifât 0 (1017), "
"ölçüm satırı esmâ ile esma_kayit ayrışması (1022), çok anlamlı kök gloss'u (1021: أثر 46:4 'esâre'), "
"şart / soru / tekit / tahzîz / yemin / teşbih / şart cevabı hazfi biçimi ölçümde yok (517). "
"Karar bekleyen (kullanıcı kararıyla açık): S2 ◈K tetik فلك kesinliği; مأي gloss.")}

p = REPO + 'okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
assert len([k for k in OM[str(S)] if not k.startswith('_')]) == N, 'sûre 46 kaydı eksik — DUR'
OM[str(S)].update(KAP)
I = OM['ilerleme']
I['tam'] = sorted(set(I['tam']) | {S})
I['kismi'].pop(str(S), None)
okunan = sum(1 for r in D.values() if r['k'][0] in set(I['tam']) or (r['k'][0] == 2 and r['k'][1] <= 20))
I['okunan_ayet'] = okunan
I['korpus_yuzde'] = round(100 * okunan / len(D), 1)
I['not'] = "Sûre 1, 9-45 ve **46 TAM**. Devam: sûre 47'den ya da sûre 2'nin 21. ayetinden."
I['son_oturum'] = 'OKU_BENI_OTURUM.md (sûre 46 tur sonu)'
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
subprocess.run([sys.executable, 'duzeltme_46.py'], check=True)

E['_profil_46'] = esma
json.dump(E, open('esma_kayit.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)

print(json.dumps({'bilanco': bil, 'cipa': cipa, 'esma': esma}, ensure_ascii=False, indent=1))
print('ilerleme:', okunan, '(%', I['korpus_yuzde'], ')  tam:', I['tam'][-3:])
