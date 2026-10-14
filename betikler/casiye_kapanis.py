# -*- coding: utf-8 -*-
"""casiye_kapanis.py — sûre 45 (Câsiye) TUR SONU: kapanış bilançosu, çıpa tablosu, esmâ sûre profili, ilerleme.

Her sayı kayıttan koşulur (defter.json · esma_kayit.json · casiye_kayit.py · cipa_tarama4_adaylari.json).
İlerleme eski kuralla: TAM sûreler + 2:1-20 (secde_kapanis ile aynı), elle artırma YOK.
Esmâ profili bir KAYITTIR: ön-kayıt (notlar/ONKAYIT_esma_katmanlari.md) H1-H4 testleri tam okuma
bitmeden koşulmaz; burada oran, eşik, p-değeri YOK.
"""
import json
from collections import Counter
import blok_bilanco
from casiye_kayit import CIPA
import subprocess, sys
# önkoşul: esmâ kaydı tüm bloklar için güncel (aday 1006 oturumundaki sıralama hatası dersi)
for a, b in [(1,10),(11,20),(21,30),(31,37)]:
    subprocess.run([sys.executable, 'esma_kayit.py', '45', str(a), str(b)], check=True, stdout=subprocess.DEVNULL)

S, N = 45, 37
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
 'etiket': 'TAM SAYIM — sûre 45, 37 ayet',
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
 'say_isareti': {k: v for a, b in [(1,10),(11,20),(21,30),(31,37)] for k, v in blok_bilanco.bilanco(S, a, b)['say_isareti'].items()},
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
KAP = {'_bilanco_sure': bil, '_cipa_tablosu_45': cipa, '_esma_profil_45': esma,
       '_kapanis_notu': ("SÛRE 45 TUR SONU. Blok başı kayıt on üçüncü kez bir sûrenin tamamında uygulandı (4 blok; son blok 31-37, 7 ayet). "
"Ek mercekler (◈K ◈B ◈D ◈A) sûrenin 37 ayetinin tamamında; tetik taraması oturum_tetik.py ile: dört blokta da ilk koşuda 0 uyuşmaz. Her blokta [x/y] sayımları oturum_xy.py ile ölçüm satırına karşı denetlendi: 0 uyuşmaz. "
"Karşıt çift notu (aday 1039, okuma kolu) 37 ayetin hepsinde yazıldı. "
"Çıpa: L4 yok; en yüksek kademe L2 (45:5 gökten indirilen rızıkla ölü yerin diriltilmesi; 16:65, 30:24, 35:9 emsali). Tarayıcı v4 adayları 45:12 (L1), 45:22 (L0) çıpa değil. "
"Sûrenin adı ('câsiye') korpusta yalnız 45:28'de. "
"Aday 1041 alanında kayıt (test yok): 'veliyy' 45:19 aynı ayette zâlimler ('evliyâ'') / Allah; 45:10 edinilen 'evliyâ''; 9:71 mü'minler; 'kibriyâ'' 10:78 (insanlara isnat) / 45:37 (O'nun). "
"Aday 1040 alanında sınır kaydı: 44:59 → 45:1; 44:44 → 45:7 ('esîm'); 44:32 → 45:16 ('ale'l-âlemîn'); 44:4-5 → 45:17-18 ('emr'); 44:35-36 → 45:24-25 (aynı iki adım, ''tû bi-âbâinâ' xref ölçüm); 44:57 → 45:30 ('el-fevzu'l-azîm' / '… el-mubîn'); 45:37 → 46:1 henüz okunmadı. Test korpus sonunda. "
"Okumada görülen sûre içi dizi ve çerçeveler (KAPATILAMAZ, sayı iddiası değil): 45:2 / 45:37 'el-azîz el-hakîm'; 'âyât + kavim niteliği' 45:3, 4, 5, 13 (mu'minîn / yûqinûn / ya'qilûn / yetefekkerûn) ve 45:20 (yûqinûn); "
"31:6-7 → 45:8-9 ters sıra; 10:93 → 45:16-17 (aynı dört öğe, aynı kapanış cümlesi); 2:7 → 45:23 (üç organ, mühür, perde); 23:37 + 43:20 → 45:24; 23:62 → 45:22 + 45:29; "
"45:24 'nemûtu ve nahyâ' / 45:26 'yuhyîkum summe yumîtukum summe yecma'ukum'; 45:24 'in hum illâ yezunnûn' / 45:32 'in nezunnu illâ zannâ'; 45:30-31 'emmâ' taksimi; 32:14 → 45:34 karşılıklı unutma (sıra ters); 1:2 → 45:36. "
"Kayıt düzeltmesi 1 (DUZELTME 45:37 mercek, 1022 — geçerli mühür iddiası). Okuma iddiası denetimi: kayıttan önce 45:14 ('eyyâm + Allah' → 'yevm + Allah' lemma dizisi) düzeltildi, 45:27 lemma dizisi ifadesi açık yazıldı (ayrıntı blok ARIZA kayıtlarında). "
"Bu sûrede kök tablosuna 3 kök eklendi (kok_ekle_45: صرر, جرح, دهر); retroaktif gloss yaması 0. "
"Tekrarlayan arıza aileleri (ayet listeleri blok ARIZA kayıtlarında): adsız konuşan, 'qîle' söyleyeni, alıntı sınırı ve şahıs geçişleri ölçüm satırında iltifât 0 (1017; 45:31 1S konuşan), "
"ölçüm satırı esmâ ile esma_kayit ayrışması (1022: 45:3, 10, 30 sıfat olarak geçen esmâ kelimeleri — mühür yanlış; 45:2, 19, 37 geçerli). Oturum notu: 45:2, 19, 37 için sohbet metninde okuyucu kararından ÖNCE koşulan bilançoya bakılıp 'geçerli mühür değil' yazılmıştı; kayıtlı bilanço geçerli gösteriyor; 45:37 mercek DUZELTME ile işlendi (özgün alan korunur), 45:2 ve 45:19 ARIZA metinleri özgün hâliyle duruyor, doğrusu aynı DUZELTME notunda; ders: esmâ bilanço iddiası karar eklendikten sonra yeniden koşulur, çok anlamlı kök gloss'u (1021: روح, بغي, شرع, نور), "
"şart / soru / ta'lîl / tekit / benzetme biçimi ölçümde yok (517). "
"Karar bekleyen (kullanıcı kararıyla açık): S2 ◈K tetik فلك kesinliği (45:12'de 'fulk' gemi, satır dolu yazıldı); مأي gloss.")}

p = REPO + 'okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
assert len([k for k in OM[str(S)] if not k.startswith('_')]) == N, 'sûre 45 kaydı eksik — DUR'
OM[str(S)].update(KAP)
I = OM['ilerleme']
I['tam'] = sorted(set(I['tam']) | {S})
I['kismi'].pop(str(S), None)
okunan = sum(1 for r in D.values() if r['k'][0] in set(I['tam']) or (r['k'][0] == 2 and r['k'][1] <= 20))
I['okunan_ayet'] = okunan
I['korpus_yuzde'] = round(100 * okunan / len(D), 1)
I['not'] = "Sûre 1, 9-44 ve **45 TAM**. Devam: sûre 46'dan ya da sûre 2'nin 21. ayetinden."
I['son_oturum'] = 'OKU_BENI_OTURUM.md (sûre 45 tur sonu)'
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
subprocess.run([sys.executable, 'duzeltme_45.py'], check=True)

E['_profil_45'] = esma
json.dump(E, open('esma_kayit.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)

print(json.dumps({'bilanco': bil, 'cipa': cipa, 'esma': esma}, ensure_ascii=False, indent=1))
print('ilerleme:', okunan, '(%', I['korpus_yuzde'], ')  tam:', I['tam'][-3:])
