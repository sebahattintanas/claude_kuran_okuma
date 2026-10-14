# -*- coding: utf-8 -*-
"""duhan_kapanis.py — sûre 44 (Duhân) TUR SONU: kapanış bilançosu, çıpa tablosu, esmâ sûre profili, ilerleme.

Her sayı kayıttan koşulur (defter.json · esma_kayit.json · duhan_kayit.py · cipa_tarama4_adaylari.json).
İlerleme eski kuralla: TAM sûreler + 2:1-20 (secde_kapanis ile aynı), elle artırma YOK.
Esmâ profili bir KAYITTIR: ön-kayıt (notlar/ONKAYIT_esma_katmanlari.md) H1-H4 testleri tam okuma
bitmeden koşulmaz; burada oran, eşik, p-değeri YOK.
"""
import json
from collections import Counter
import blok_bilanco
from duhan_kayit import CIPA
import subprocess, sys
# önkoşul: esmâ kaydı tüm bloklar için güncel (aday 1006 oturumundaki sıralama hatası dersi)
for a, b in [(1,10),(11,20),(21,30),(31,40),(41,50),(51,59)]:
    subprocess.run([sys.executable, 'esma_kayit.py', '44', str(a), str(b)], check=True, stdout=subprocess.DEVNULL)

S, N = 44, 59
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
 'etiket': 'TAM SAYIM — sûre 44, 59 ayet',
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
 'say_isareti': {k: v for a, b in [(1,10),(11,20),(21,30),(31,40),(41,50),(51,59)] for k, v in blok_bilanco.bilanco(S, a, b)['say_isareti'].items()},
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
KAP = {'_bilanco_sure': bil, '_cipa_tablosu_44': cipa, '_esma_profil_44': esma,
       '_kapanis_notu': ("SÛRE 44 TUR SONU. Blok başı kayıt on ikinci kez bir sûrenin tamamında uygulandı (6 blok; son blok 51-59, 9 ayet). "
"Ek mercekler (◈K ◈B ◈D ◈A) sûrenin 59 ayetinin tamamında; her blokta tetik taraması oturum_tetik.py ile: altı blokta da ilk koşuda 0 uyuşmaz. Her blokta [x/y] sayımları oturum_xy.py ile ölçüm satırına karşı denetlendi: 0 uyuşmaz. "
"Karşıt çift notu (aday 1039, okuma kolu) 59 ayetin hepsinde yazıldı; dolu olan 5 ayet (44:7, 8, 29, 35, 38). "
"Çıpa: L4 yok; en yüksek kademe L1 (44:10 göğün getireceği apaçık duman; 44:24 'rehv' deniz). Tarayıcı v4 adayı 44:7 çıpa değil (L0). "
"Lafız: sûrede 3 token (44:18, 44:19 elçinin sözü içinde; 44:42); Rab 9 token (44:6, 7, 8 ×2, 12, 20 ×2, 22, 57). "
"Aday 1041 alanında kayıt (test yok): 'munzir' 1P 44:3 / Peygamber 13:7, 38:65; 'bataşa' insan 26:130, 28:19 / 1P 44:16; 'el-azîz' Allah 44:42 / azaptaki insan 44:49 / Mısır yöneticisi 12:30, 12:78; 'mevlâ' Allah 22:78 / insanlar 44:41. "
"Aday 1040 alanında sınır kaydı: 43:2 → 44:2 (esit2 TAM), 43:83 → 44:9, 43:41 → 44:16, 43:49-50 → 44:12-15, 43:88 → 44:22, 43:52 · 58 → 44:37; sûre sonları 43:89 / 44:59 ('fe' + 2MS emir + 3MP hakkında cümle); 44:59 → 45:1 henüz okunmadı. Test korpus sonunda. "
"Sûrenin adı ('duhân') yalnız 44:10'da (lemma korpusta 2 ayet: 41:11, 44:10). "
"Okumada görülen sûre içi dizi ve çerçeveler (KAPATILAMAZ, sayı iddiası değil): 'fe-rtaqib' 2MS emri 44:10 ve son ayet 44:59; 1P + 'hu' 44:3 'enzelnâhu' / 44:58 'yessernâhu'; "
"Firavun anlatısı 44:17-33, Şuarâ 26:52-59 sırasıyla (44:23-28); 44:25-26 bırakılan 'cennât, uyûn, maqâm kerîm' / 44:51-52 takvâ sahiplerinin 'maqâm emîn, cennât, uyûn'; "
"'el-mevtetu'l-ûlâ' üç ağızda: 37:59 cennet ehli, 44:35 inkârcılar, 44:56 anlatı; 37:58-60 → 44:56-57 aynı sıra; 37:62-68 zakkum dörtlüsü → 44:43-48; 44:38-39 = 21:16 + 15:85; "
"cehennem 44:43-50 / cennet 44:51-57 art arda; 44:9 'yel'abûn' → 44:38 'lâ'ibîn'. "
"Kayıt düzeltmesi yok (DUZELTME boş). Okuma iddiası denetimi: kayıttan önce yazım düzeltmesi 44:2, 44:39; içerik düzeltmesi 44:45, 44:49 (ARIZA 41-50), 44:54, 55, 56, 57 (ARIZA 51-59). "
"44:41-50 taslağı yarıda kalan bir turda yazılmıştı; kayıttan önce bütün sayım ve alıntılar yeniden doğrulandı (ARIZA 41-50 oturum notu). "
"Bu sûrede kök tablosuna 4 kök eklendi (kok_ekle_44: أدي, رهو, غلي, عتل); retroaktif gloss yaması 0. "
"Tekrarlayan arıza aileleri (ayet listeleri blok ARIZA kayıtlarında): alıntı sınırları, adsız konuşan ve şahıs geçişleri ölçüm satırında iltifât 0 (1017), "
"ölçüm satırı esmâ ile esma_kayit ayrışması ve sıfat olarak geçen esmâ kelimeleri (1022: mubîn, hakîm, evvel/ûlâ, kerîm, mu'min, mevlâ; 44:49 azîz + kerîm mühür yanlış), çok anlamlı kök gloss'u (1021: ولي, أمر, جنن, عين, قوم, نظر, علو, علم, خير, مهل, حور), "
"şart / soru / hasr / tekit / benzetme biçimi ölçümde yok (517), sayı işareti yanlış pozitif (44:54 'zevvecnâ'). "
"Karar bekleyen (kullanıcı kararıyla açık): S2 ◈K tetik فلك kesinliği; مأي gloss.")}

p = REPO + 'okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
assert len([k for k in OM[str(S)] if not k.startswith('_')]) == N, 'sûre 44 kaydı eksik — DUR'
OM[str(S)].update(KAP)
I = OM['ilerleme']
I['tam'] = sorted(set(I['tam']) | {S})
I['kismi'].pop(str(S), None)
okunan = sum(1 for r in D.values() if r['k'][0] in set(I['tam']) or (r['k'][0] == 2 and r['k'][1] <= 20))
I['okunan_ayet'] = okunan
I['korpus_yuzde'] = round(100 * okunan / len(D), 1)
I['not'] = "Sûre 1, 9-43 ve **44 TAM**. Devam: sûre 45'ten ya da sûre 2'nin 21. ayetinden."
I['son_oturum'] = 'OKU_BENI_OTURUM.md (sûre 44 tur sonu)'
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
subprocess.run([sys.executable, 'duzeltme_44.py'], check=True)

E['_profil_44'] = esma
json.dump(E, open('esma_kayit.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)

print(json.dumps({'bilanco': bil, 'cipa': cipa, 'esma': esma}, ensure_ascii=False, indent=1))
print('ilerleme:', okunan, '(%', I['korpus_yuzde'], ')  tam:', I['tam'][-3:])
