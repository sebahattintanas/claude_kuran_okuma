# -*- coding: utf-8 -*-
"""muhammed_kapanis.py — sûre 47 (Muhammed) TUR SONU: kapanış bilançosu, çıpa tablosu, esmâ sûre profili, ilerleme.

Her sayı kayıttan koşulur (defter.json · esma_kayit.json · muhammed_kayit.py · cipa_tarama4_adaylari.json).
İlerleme eski kuralla: TAM sûreler + 2:1-20 (secde_kapanis ile aynı), elle artırma YOK.
Esmâ profili bir KAYITTIR: ön-kayıt (notlar/ONKAYIT_esma_katmanlari.md) H1-H4 testleri tam okuma
bitmeden koşulmaz; burada oran, eşik, p-değeri YOK.
"""
import json
from collections import Counter
import blok_bilanco
from muhammed_kayit import CIPA
import subprocess, sys
# önkoşul: esmâ kaydı tüm bloklar için güncel (aday 1006 oturumundaki sıralama hatası dersi)
for a, b in [(1,10),(11,20),(21,30),(31,38)]:
    subprocess.run([sys.executable, 'esma_kayit.py', '47', str(a), str(b)], check=True, stdout=subprocess.DEVNULL)

S, N = 47, 38
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
 'etiket': 'TAM SAYIM — sûre 47, 38 ayet',
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
 'say_isareti': {k: v for a, b in [(1,10),(11,20),(21,30),(31,38)] for k, v in blok_bilanco.bilanco(S, a, b)['say_isareti'].items()},
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
KAP = {'_bilanco_sure': bil, '_cipa_tablosu_47': cipa, '_esma_profil_47': esma,
       '_kapanis_notu': ("SÛRE 47 TUR SONU. Blok başı kayıt on beşinci kez bir sûrenin tamamında uygulandı (4 blok; son blok 31-38, 8 ayet). "
"Ek mercekler (◈K ◈B ◈D ◈A) sûrenin 38 ayetinin tamamında; tetik taraması oturum_tetik.py ile: blok 1-10, 21-30, 31-38 ilk koşuda 0 uyuşmaz; blok 11-20 ilk koşuda 1 uyuşmaz (47:15 ◈B tetiksiz satır dolu yazılmıştı; organ 'em'â'' ve 'şârib' tetik listesinde yok — satır '—' yapıldı, gözlem ◇'ye taşındı), ikinci koşuda 0. "
"[x/y] sayımları oturum_xy.py ile ölçüm satırına karşı: blok 1-10 ilk koşuda 1 uyuşmaz (47:9 عمل [1/12] yazılmıştı, ölçüm [5/12]; sayım cümlesi silindi), sonra 0; öbür bloklar ilk koşuda 0. "
"Kayıttan önce düzeltilen kendi iddialarım: ثخن gloss'undaki okunmamış 8:67 anması çıkarıldı (dikey yeniden üretildi); metni okunmadan yazılmış emsaller (bâtıl 22:62 / 31:30, 'menn' 20:80, 'vizr' 16:25 / 17:15 / 35:18 / 39:7, 'erhâm' 13:8 / 22:5 / 31:34 / 33:6) ayetler okunduktan sonra yeniden yazıldı. "
"Karşıt çift notu (aday 1039, okuma kolu) 38 ayetin hepsinde yazıldı. "
"Esmâ: 4 e_oto tokeni (47:11 'mevlâ' ×2, 47:19 'mu'min', 47:38 'ğaniyy') — okuyucu kararı ilâhî 2 (47:11:4, 47:38:18), değil 2 (47:11:10 'lâ mevlâ lehum', 47:19:9 inananlar); §4.3 mühür yalnız 47:11 (geçerli; ölçüm satırı MÜHÜRSÜZ — 1022). Bilanço iddiaları karar eklendikten SONRA koşuldu. "
"Çıpa: L4 yok. 47:10 ve 47:22 L0 (yeryüzü gezilen / bozgunculuk yeri), 47:23 L1 (göz ve sağırlık — 46:26'da verilen organlar burada alınan). 47:15 cennet ırmakları âhiret sahnesi, olgu değil. Tarayıcı v4 adayları 47:22, 47:36 — çıpa değil (kesinlik 0/2). "
"Hapaks yedi kök: تعس 47:8, أسن عسل معي 47:15, شرط 47:18, قفل 47:24, لحن 47:30 — hepsi kok_ekle_47 ile eklenen köklerden. Fâsıla: 47:10 ا ve 47:24 ٓ kafiye kırılması; 47:10'un ★'ını kafiye kırığı veriyor, bilanço 'allah' etiketliyor (aday 1001). "
"Aday 1041 alanında kayıt (test yok): نصر 47:7 'in tensurû'llâha yensurkum' (aynı ayette insan → Allah, Allah → insan); 'intesara' 47:4 Allah / 26:93, 26:227, 42:39, 42:41 insan; ولي 47:11 'mevlâ' Allah / 'lâ mevlâ lehum'; علم 47:19 'fa'lem' (2MS) / 've'llâhu ya'lemu'; 'ahraca' 47:13 kasaba / 47:29 Allah; 'ebtale' 10:81 Allah / 47:33 inananlar. Sınırda: كفر 47:1-2 'keferû' / 'keffera'; 'haqq' 22:62 ve 31:30 Allah / 47:2 indirilen; عرف 47:6 ''arrafe' / 47:30 ''arafa' (farklı lemma); 'emlâ' 47:25 (özne belirsiz). "
"Aday 1040 alanında sınır kaydı: 46:34-35 → 47:1 ('ellezîne keferû'; 47 hurûf-ı mukattaa olmadan açılıyor, Hâ Mîm dizisi 46'da bitti); 46:25 'tudammiru' → 47:10 'dammera'llâhu' (aynı lemma). 47:38 → 48:1 henüz okunmadı. Test korpus sonunda. "
"Okumada görülen dizi ve çerçeveler (KAPATILAMAZ, sayı iddiası değil): 'ellezîne keferû ve saddû an sebîli'llâh' sûre içi 47:1, 32, 34 (sûre başı ve sonu); 'adalle / len yudılle / ahbata a'mâlehum' çizgisi 47:1, 4, 8, 9, 28, 32 ve 47:33 'lâ tubtılû a'mâlekum', 47:35 'len yetirakum a'mâlekum' (عمل 12/12); 'zâlike bi-enne' gerekçe kalıbı 47:3, 9, 11, 26, 28; "
"47:14 iki açılış yan yana (11:17 'alâ beyyinetin min rabbih' / 35:8 'zuyyine lehû sû'u amelih') ve 47:15 aynı 'ke-men' iskeleti; 47:15 'mâ'' bozulmayan su / kaynar su; 47:25 'irteddû alâ edbârihim' → 47:27 'yadribûne … edbârahum'; ضرب üç öznede (47:3 Allah, 47:4 inananlar, 47:27 melekler); kalp sırası 47:16 mühür, 47:20 ve 47:29 hastalık, 47:24 kilit; 9:39'un iki parçası 47:32 ve 47:38'de; 47:22 / 47:38 'in tevelleytum / in tetevellev' iki sonuç; 35:15 → 47:38 'ğaniyy / fuqarâ'' sıra ters. "
"Kayıt düzeltmesi yok (DUZELTME boş). Bu sûrede kök tablosuna 10 kök eklendi (kok_ekle_47); retroaktif gloss yaması 0 (yeni köklerin önceden okunmuş 2 ayeti vardı, ikisinde de karşılıksız anma yoktu). "
"Tekrarlayan arıza aileleri (ayet listeleri blok ARIZA kayıtlarında): adsız fiil öznesi 3MS ('adalle', 'ahbata', 'zâde', 'yu'tî', 'yuhric'), 2MS / 2MP muhatap, ayetler arası 3MP ↔ 2MP ↔ 1P geçişleri ölçümde iltifât 0 (1017); "
"ölçüm satırı esmâ ile esma_kayit ayrışması 47:11 (1022); çok anlamlı kök gloss'u (1021: دبر 'arka' 47:24 'tedebbür'ü kapsamıyor; 'menn' 20:80 / 47:4); "
"tekit 'inne', 'lev' cevap lâmı, 'lâkin', teşbih, 'em' munkatı'a, 'innemâ' hasrı, 'lev lâ' tahzîzi, cevabı düşmüş 'keyfe', masdarla beddua, tenbîh 'hâ' ölçümde yok (517); kafiye kırığında ★ kaynak etiketi (1001). "
"Karar bekleyen (kullanıcı kararıyla açık): S2 ◈K tetik فلك kesinliği; مأي gloss; oturum_* yardımcılarının depoda kalması.")}

p = REPO + 'okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
assert len([k for k in OM[str(S)] if not k.startswith('_')]) == N, 'sûre 47 kaydı eksik — DUR'
OM[str(S)].update(KAP)
I = OM['ilerleme']
I['tam'] = sorted(set(I['tam']) | {S})
I['kismi'].pop(str(S), None)
okunan = sum(1 for r in D.values() if r['k'][0] in set(I['tam']) or (r['k'][0] == 2 and r['k'][1] <= 20))
I['okunan_ayet'] = okunan
I['korpus_yuzde'] = round(100 * okunan / len(D), 1)
I['not'] = "Sûre 1, 9-46 ve **47 TAM**. Devam: sûre 48'den ya da sûre 2'nin 21. ayetinden."
I['son_oturum'] = 'OKU_BENI_OTURUM.md (sûre 47 tur sonu)'
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
subprocess.run([sys.executable, 'duzeltme_47.py'], check=True)

E['_profil_47'] = esma
json.dump(E, open('esma_kayit.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)

print(json.dumps({'bilanco': bil, 'cipa': cipa, 'esma': esma}, ensure_ascii=False, indent=1))
print('ilerleme:', okunan, '(%', I['korpus_yuzde'], ')  tam:', I['tam'][-3:])
