# -*- coding: utf-8 -*-
"""muhammed_kapanis.py — sûre 48 (Fetih) TUR SONU: kapanış bilançosu, çıpa tablosu, esmâ sûre profili, ilerleme.

Her sayı kayıttan koşulur (defter.json · esma_kayit.json · fetih_kayit.py · cipa_tarama4_adaylari.json).
İlerleme eski kuralla: TAM sûreler + 2:1-20 (secde_kapanis ile aynı), elle artırma YOK.
Esmâ profili bir KAYITTIR: ön-kayıt (notlar/ONKAYIT_esma_katmanlari.md) H1-H4 testleri tam okuma
bitmeden koşulmaz; burada oran, eşik, p-değeri YOK.
"""
import json
from collections import Counter
import blok_bilanco
from fetih_kayit import CIPA
import subprocess, sys
# önkoşul: esmâ kaydı tüm bloklar için güncel (aday 1006 oturumundaki sıralama hatası dersi)
for a, b in [(1,10),(11,20),(21,29)]:
    subprocess.run([sys.executable, 'esma_kayit.py', '48', str(a), str(b)], check=True, stdout=subprocess.DEVNULL)

S, N = 48, 29
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
 'etiket': 'TAM SAYIM — sûre 48, 29 ayet',
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
 'say_isareti': {k: v for a, b in [(1,10),(11,20),(21,29)] for k, v in blok_bilanco.bilanco(S, a, b)['say_isareti'].items()},
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
KAP = {'_bilanco_sure': bil, '_cipa_tablosu_48': cipa, '_esma_profil_48': esma,
       '_kapanis_notu': ("SÛRE 48 TUR SONU. Blok başı kayıt on altıncı kez bir sûrenin tamamında uygulandı (3 blok; son blok 21-29, 9 ayet). "
"Ek mercekler (◈K ◈B ◈D ◈A) sûrenin 29 ayetinin tamamında; tetik taraması oturum_tetik.py ile üç blokta da ilk koşuda 0 uyuşmaz (ön kuru koşuda tetikler önceden alındı). "
"[x/y] sayımları oturum_xy.py ile ölçüm satırına karşı: blok 1-10 ve 11-20 ilk koşuda 0; blok 21-29 ilk koşuda 1 uyuşmaz (48:28 شهد [1/2] yazılmıştı, ölçüm [2/2] — ilk geçiş 48:8), düzeltildi, sonra 0. "
"Kayıttan önce düzeltilen kendi yazımlarım: 48:8 ◇'de boş kalmış bir not cümlesi silindi; 48:10 ◇ 9:111 metni okunduktan sonra genişletildi ('evfâ', ''ahd', 'bâya'a' 9:111'de bir arada). "
"Karşıt çift notu (aday 1039, okuma kolu) 29 ayetin hepsinde yazıldı. "
"Esmâ: 27 e_oto tokeni; okuyucu kararı ilâhî 13 token. §4.3 mühür 15 ayette; karar sonrası geçerli 9 (48:4, 7, 11, 14, 19, 21, 24, 26, 28); mühür yanlış 6 (48:1 'mubîn', 48:3 'azîz' — fethin / yardımın sıfatı; 48:18, 48:27 'qarîb' — fethin sıfatı; 48:20 'mu'min'; 48:22 'veliyy' + 'nasîr' olumsuzlanan başkası). Ölçüm satırı MÜHÜRSÜZ / esma_kayit EVET ayrışması birçok ayette (1022). Bilanço iddiaları karar eklendikten SONRA koşuldu. "
"Çıpa: L4 kesin yok. 48:4, 48:7, 48:14 L0 (gökler ve yer yalnız 'cunûd' / 'mulk' tamlamasında), 48:18 L0 (ağaç biatin yeri); 48:5, 48:17 cennet ırmakları âhiret sahnesi, olgu değil. 48:29 ekin büyümesi dört aşama ('fe' dizisi, şat' / sûq adlı) — 39:21 emsaline göre L4 mekanizma kolu adayı, ANCAK teşbih içinde (İncil'deki mesel): L4 adayı, TARTIŞMALI, cipa kararı açık (kullanıcı kararına bırakıldı). Tarayıcı v4 adayları 48:4, 48:5, 48:29 — kesinlik 0/3 (48:29 kısmi). "
"Hapaks yok (kok_ekle_48 ile eklenen ظفر ve حلق korpusta 1'den fazla token). Fâsıla 29/29 ا — kafiye kırığı yok. En uzun ayet 48:29 (54 kelime), en kısa 48:3. ★★★ 48:3, 48:7 (kaynak allah, kısa ayet) ve 48:29 (kaynak n, uzun ayet) — yıldız formülü davranışı, içerik iddiası değil. İltifât ölçümü yalnız 48:8. Rab sûrede 0, lafız 39 token / 25 ayet. "
"Aday 1041 alanında kayıt (test yok): يدي 48:10 'yedu'llâhi fevqa eydîhim' (aynı ayette Allah ve insan), 48:20, 48:24 insan elleri; 'azîz' 48:3 yardımın sıfatı / 48:7, 48:19 Allah; ملك 48:11 'yemliku' / 48:14 'mulk'; غفر 48:11 'istağfir' / 48:14 'yağfiru'; قدر 48:21 'lem taqdirû' / 'qadîr' (aynı ayet, kök); شهد 48:8 'şâhid' (elçi) / 48:28 'şehîd' (Allah, kök); رحم 48:14 'rahîm' (Allah) / 48:29 'ruhamâ'' (insanlar). "
"Aday 1040 alanında sınır kaydı: 47:38 → 48:1 (hitap 2MP → 2MS, fâsıla م → ا); 47:19 → 48:2 'istağfir li-zenbik' / 'li-yağfira leke … zenbik'; 47:7 → 48:3 'yensurkum' / 'yensurake'; 47:38 'in tetevellev' → 48:16 'in tetevellev'; 9:39'un iki parçası 47:38 ('yestebdil') ve 48:16 ('yu'azzibkum'); 47:2 / 48:29 'Muhammed'; 47:30 / 48:29 'sîmâ'; 47:28 'ridvân' → 48:18, 48:29. 48:29 → 49:1 henüz okunmadı. Test korpus sonunda. "
"Okumada görülen dizi ve çerçeveler (KAPATILAMAZ, sayı iddiası değil): sekîne sûre içi üç ayet (48:4 'fî qulûb', 48:18 'aleyhim', 48:26 'alâ rasûlihî ve ale'l-mu'minîn') ve 48:26 inkâr edenlerin kalbine 'hamiyye'; 'feth' 48:1 'mubîn', 48:18 ve 48:27 'qarîb'; biat 48:10 ve 48:18; geri bırakılan bedevîler bölümü 48:11-17 ('se-yeqûlu' ×2, 'qul' ×3); 48:11 'mâ leyse fî qulûbihim' / 48:18 'alime mâ fî qulûbihim'; ganimet dizisi 48:15, 19, 20, 21; eller 48:10, 20, 24 (tek yön → ayna); 'kâna'llâhu … ' kapanışları (alîm hakîm, azîz hakîm, habîr, ğafûr rahîm, qadîr, basîr, alîm); 'sunneta'llâh' 48:23 / 33:62 / 35:43; 9:33 = 48:28 cümlesi, farklı kapanış; 24:61 üçlüsü 48:17'de savaş bağlamında; 12:99 'girme + in şâ'a'llâh + âminîn' 48:27'de; 39:21 ekin büyüme → çöküş / 48:29 yalnız büyüme. "
"Kayıt düzeltmesi yok (DUZELTME boş). Bu sûrede kök tablosuna 2 kök eklendi (kok_ekle_48: ظفر, حلق); retroaktif gloss yaması 0. "
"Tekrarlayan arıza aileleri (ayet listeleri blok ARIZA kayıtlarında): muhatap 2MS adsız (48:1-3, 8, 10, 11, 15, 23, 29), süsleyen adsız (48:12), 'qavmin ulî be'sin şedîd' adsız, 48:25 1P 'le-azzebnâ' ölçümde iltifât 0 ve cevabı düşmüş 'lev lâ', 48:9 zamir göndergesi ayrılmıyor (1017); ölçüm satırı esmâ ile esma_kayit ayrışması (1022); tekit 'innâ' / 'fe-innâ', takdim 'li'llâhi …', zemm, hasr 'innemâ', soru, teşbih ('kemâ', 'ke-'), üçlü tekrar ölçümde yok (517); 48:25 ölçüm IMPV 1 — metinde emir yok; ◈B tetik listesinde olmayan beden / bitki sözcükleri (a'mâ, a'rec, merîd, ru'ûs, vucûh, zer', sûq) — araç açığı (924). "
"Karar bekleyen (kullanıcı kararıyla açık): 48:29 çıpa (L4 adayı, teşbih içinde — TARTIŞMALI); S2 ◈K tetik فلك kesinliği; مأي gloss; oturum_* yardımcılarının depoda kalması.")}

p = REPO + 'okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
assert len([k for k in OM[str(S)] if not k.startswith('_')]) == N, 'sûre 48 kaydı eksik — DUR'
OM[str(S)].update(KAP)
I = OM['ilerleme']
I['tam'] = sorted(set(I['tam']) | {S})
I['kismi'].pop(str(S), None)
okunan = sum(1 for r in D.values() if r['k'][0] in set(I['tam']) or (r['k'][0] == 2 and r['k'][1] <= 20))
I['okunan_ayet'] = okunan
I['korpus_yuzde'] = round(100 * okunan / len(D), 1)
I['not'] = "Sûre 1, 9-47 ve **48 TAM**. Devam: sûre 49'dan ya da sûre 2'nin 21. ayetinden."
I['son_oturum'] = 'OKU_BENI_OTURUM.md (sûre 48 tur sonu)'
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
subprocess.run([sys.executable, 'duzeltme_48.py'], check=True)

E['_profil_48'] = esma
json.dump(E, open('esma_kayit.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)

print(json.dumps({'bilanco': bil, 'cipa': cipa, 'esma': esma}, ensure_ascii=False, indent=1))
print('ilerleme:', okunan, '(%', I['korpus_yuzde'], ')  tam:', I['tam'][-3:])
