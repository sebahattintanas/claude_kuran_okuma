# -*- coding: utf-8 -*-
"""shura_kapanis.py — sûre 42 (Şûrâ) TUR SONU: kapanış bilançosu, çıpa tablosu, esmâ sûre profili, ilerleme.

Her sayı kayıttan koşulur (defter.json · esma_kayit.json · shura_kayit.py · cipa_tarama4_adaylari.json).
İlerleme eski kuralla: TAM sûreler + 2:1-20 (secde_kapanis ile aynı), elle artırma YOK.
Esmâ profili bir KAYITTIR: ön-kayıt (notlar/ONKAYIT_esma_katmanlari.md) H1-H4 testleri tam okuma
bitmeden koşulmaz; burada oran, eşik, p-değeri YOK.
"""
import json
from collections import Counter
import blok_bilanco
from shura_kayit import CIPA
import subprocess, sys
# önkoşul: esmâ kaydı tüm bloklar için güncel (aday 1006 oturumundaki sıralama hatası dersi)
for a, b in [(1,10),(11,20),(21,30),(31,40),(41,50),(51,53)]:
    subprocess.run([sys.executable, 'esma_kayit.py', '42', str(a), str(b)], check=True, stdout=subprocess.DEVNULL)

S, N = 42, 53
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
 'etiket': 'TAM SAYIM — sûre 42, 53 ayet',
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
 'say_isareti': {k: v for a, b in [(1,10),(11,20),(21,30),(31,40),(41,50),(51,53)] for k, v in blok_bilanco.bilanco(S, a, b)['say_isareti'].items()},
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
KAP = {'_bilanco_sure': bil, '_cipa_tablosu_42': cipa, '_esma_profil_42': esma,
       '_kapanis_notu': ("SÛRE 42 TUR SONU. Blok başı kayıt onuncu kez bir sûrenin tamamında uygulandı (6 blok; son blok 51-53, 3 ayet). "
"Ek mercekler (◈K ◈B ◈D ◈A) sûrenin 53 ayetinin tamamında; her blokta tetik taraması (tetik2). 42:21-30'da 42:27 ◈K أرض satırı ilk yazışta '—' idi, tetik2 1 uyuşmaz verdi, kayıttan önce dolduruldu; 42:11-20'de 42:11 ◈B سمع/بصر satırı kayıttan önce eklendi; öbür dört blokta ilk koşuda 0 uyuşmaz. "
"Karşıt çift notu (aday 1039, okuma kolu) 53 ayetin hepsinde yazıldı; dolu olan 33 ayet. "
"Çıpa: L4 yok; en yüksek kademe L2 (42:33 rüzgârın durdurulması → 'revâkid', şartlı). 42:49-50 dörtlü sonuç kümesi (dişi / erkek / ikisi / kısır) L1, L4 sınıflama koluna sınırda (aday 1014 ölçütü: üye eşlemesi yok). Tarayıcı v4 adayları 4 (42:11, 14, 27, 33), isabet 0. "
"Aday 1041 açıldı (blok 31-40): aynı kelimenin önce Allah, sonra insan için kullanılması — şekûr 42:23 → 33, ğafr 42:5/23 → 37/43, afv 42:25/30/34 → 40, istecâbe 42:26 → 38/47; insan grupları arasında şera'a 42:13 → 21, işfâk 42:18 → 22. Kayıt; test korpus sonunda. "
"Aday 1040 alanında sınır kaydı: 41:43 → 42:3, 41:3 → 42:7, 39:75 → 40:7 → 42:5 (tesbih kalıbı); 42:51 'aliyyun hakîm' → 43:4 (henüz okunmadı). Test korpus sonunda. "
"Sûrenin adı ('şûrâ') yalnız 42:38'de; lemma korpusta 1; شور kökü 4 ayet. "
"Okumada görülen sûre içi dizi ve çerçeveler (KAPATILAMAZ, sayı iddiası değil): vahiy çerçevesi 42:3 'kezâlike yûhî ileyk' → 42:7 've kezâlike evhaynâ ileyk' → 42:13 → 42:51-52 (42:7 ve 42:52 aynı açılış); "
"'lehû mâ fi's-semâvâti ve mâ fi'l-ard' 42:4 ve 42:53 (sûrenin 4. ve son ayeti); 'min veliyyin ve lâ nasîr' 42:8, 42:31; 'tera'z-zâlimîn' 42:22, 42:44; 'men yudlili'llâh' 42:44 ('min veliyy') / 42:46 ('min sebîl'); "
"iman edenlerin sıfat zinciri 42:36 'lillezîne' → 37-39 've'llezîne'; 'izâ … hum + IMPF' yapısı 42:37 (bağışlarlar) / 42:39 (karşı koyarlar); 'sebîl' 42:41, 42, 44, 46; "
"9:91/93 'mâ … min sebîl' / 'innema's-sebîl' ikilisi 42:41-42'de aynı sırayla; 28:60'ın üç parçası 42:36'da aynı sırayla; 30:36 dizisi 42:48'de farklı sonla; "
"'gemi' kelimesi 42:32-34'te yok ('el-cevâr' adsız); 42:49-50'de dişi/erkek sırası değişiyor; 42:52 'ce'alnâhu' zamiri (rûh / kitap) açık değil. "
"Kayıt düzeltmesi yok (DUZELTME boş). Render öncesi metin düzeltmeleri blok ARIZA kayıtlarında. "
"Bu sûrede kök tablosuna 2 kök eklendi (kok_ekle_42: شرع, ركد); retroaktif gloss yaması 0. "
"Tekrarlayan arıza aileleri (ayet listeleri blok ARIZA kayıtlarında): alıntı sınırları ve şahıs geçişleri ölçüm satırında iltifât 0 (1017), "
"ölçüm satırı esmâ ile esma_kayit ayrışması (1022), çok anlamlı kök gloss'u (1021: عرض, روح, بشر, ملك, ذكر, علم), şart / soru / hasr biçimi ölçümde yok (517), kafiye kırığı ★ kaynağı (1001), "
"araç açıkları (924: 42:50 sayı işareti 'zuwwijat', 42:51 1S etiketi). "
"Karar bekleyen (kullanıcı kararıyla açık): S2 ◈K tetik فلك kesinliği; مأي gloss.")}

p = REPO + 'okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
assert len([k for k in OM[str(S)] if not k.startswith('_')]) == N, 'sûre 42 kaydı eksik — DUR'
OM[str(S)].update(KAP)
I = OM['ilerleme']
I['tam'] = sorted(set(I['tam']) | {S})
I['kismi'].pop(str(S), None)
okunan = sum(1 for r in D.values() if r['k'][0] in set(I['tam']) or (r['k'][0] == 2 and r['k'][1] <= 20))
I['okunan_ayet'] = okunan
I['korpus_yuzde'] = round(100 * okunan / len(D), 1)
I['not'] = "Sûre 1, 9-41 ve **42 TAM**. Devam: sûre 43'ten ya da sûre 2'nin 21. ayetinden."
I['son_oturum'] = 'OKU_BENI_OTURUM.md (sûre 42 tur sonu)'
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
subprocess.run([sys.executable, 'duzeltme_42.py'], check=True)

E['_profil_42'] = esma
json.dump(E, open('esma_kayit.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)

print(json.dumps({'bilanco': bil, 'cipa': cipa, 'esma': esma}, ensure_ascii=False, indent=1))
print('ilerleme:', okunan, '(%', I['korpus_yuzde'], ')  tam:', I['tam'][-3:])
