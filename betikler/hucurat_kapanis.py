# -*- coding: utf-8 -*-
"""muhammed_kapanis.py — sûre 49 (Hucurât) TUR SONU: kapanış bilançosu, çıpa tablosu, esmâ sûre profili, ilerleme.

Her sayı kayıttan koşulur (defter.json · esma_kayit.json · hucurat_kayit.py · cipa_tarama4_adaylari.json).
İlerleme eski kuralla: TAM sûreler + 2:1-20 (secde_kapanis ile aynı), elle artırma YOK.
Esmâ profili bir KAYITTIR: ön-kayıt (notlar/ONKAYIT_esma_katmanlari.md) H1-H4 testleri tam okuma
bitmeden koşulmaz; burada oran, eşik, p-değeri YOK.
"""
import json
from collections import Counter
import blok_bilanco
from hucurat_kayit import CIPA
import subprocess, sys
# önkoşul: esmâ kaydı tüm bloklar için güncel (aday 1006 oturumundaki sıralama hatası dersi)
for a, b in [(1,10),(11,18)]:
    subprocess.run([sys.executable, 'esma_kayit.py', '49', str(a), str(b)], check=True, stdout=subprocess.DEVNULL)

S, N = 49, 18
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
 'etiket': 'TAM SAYIM — sûre 49, 18 ayet',
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
 'say_isareti': {k: v for a, b in [(1,10),(11,18)] for k, v in blok_bilanco.bilanco(S, a, b)['say_isareti'].items()},
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
KAP = {'_bilanco_sure': bil, '_cipa_tablosu_49': cipa, '_esma_profil_49': esma,
       '_kapanis_notu': ("SÛRE 49 TUR SONU. Blok başı kayıt on yedinci kez bir sûrenin tamamında uygulandı (2 blok; son blok 11-18, 8 ayet). "
"Ek mercekler (◈K ◈B ◈D ◈A) sûrenin 18 ayetinin tamamında; tetik taraması oturum_tetik.py ile iki blokta da ilk koşuda 0 uyuşmaz (ön kuru koşu ile). "
"[x/y] sayımları oturum_xy.py ile ölçüm satırına karşı: iki blokta da ilk koşuda 0 (97 + 99). "
"Kayıttan önce düzeltilen kendi yazımlarım: blok 11-18'de metni bu oturumda görülmeden 'okumada görüldü' listesine girmiş emsal anmaları yedi yerde çıkarıldı (29:48; 33:20; 39:22; 10:38, 11:13, 21:38; 9:115, 24:35, 24:64, 29:62; 9:5, 9:102); yalnız metni okunan emsaller kaldı. "
"Karşıt çift notu (aday 1039, okuma kolu) 18 ayetin hepsinde yazıldı. "
"Esmâ: 18 e_oto tokeni; okuyucu kararı ilâhî 14, değil 4 (49:9, 10, 15 'mu'min'; 49:12 'ehad'). §4.3 mühür 8 ayette, hepsi geçerli (49:1, 5, 8, 12, 13, 14, 16, 18); 49:16 ve 49:18'de ölçüm satırı MÜHÜRSÜZ / esma_kayit EVET (1022). Bilanço iddiaları karar eklendikten SONRA koşuldu. "
"Çıpa: L4 yok. 49:13 L1 (erkek / dişiden yaratma + halk / kabile sınıflaması + 'li-te'ârafû' işlevi; L2'ye sınırda, sınıflama toplumsal), 49:16 ve 49:18 L0 (gökler ve yer bilginin nesnesi). 49:12 'ölü kardeş eti' temsil, olgu değil. Tarayıcı v4 adayları 49:12, 49:13 — kesinlik 0/2. "
"Hapaks üç ayette (49:11 نبز لقب, 49:12 جسس, 49:14 ليت) — hepsi kok_ekle_49 ile eklenen köklerden; üçü de ★★★ kaynak hapaks. ★★★ toplam 7 ayet: hapaks 3, allah 4 (49:1, 8, 16, 18 — kısa ayette lafız oranı). Fâsıla N 17, 49:13 ر KAFİYE KIRILMASI; 49:13'ün ★'ını kafiye kırığı veriyor, bilanço 'allah' etiketliyor (aday 1001). En uzun 49:11 (39), en kısa 49:8 (7). Rab 0; lafız 27 token / 14 ayet; edilgen 1 ayet (49:10); iltifât ölçümü 0. "
"Aday 1041 alanında kayıt (test yok): يدي 49:1 'yedeyi'llâh' (48:10 kaydına ek); سخر 9:79 'sehira'llâhu minhum' / 49:11 insanlar arası; منن 49:17 'lâ temunnû' / 'bel Allâhu yemunnu' aynı ayette; علم 49:16 'tu'allimûna'llâh' (meful Allah) / 12:37 'allemenî rabbî'. "
"Aday 1040 alanında sınır kaydı: 48:29 → 49:1 (fâsıla ا → م; hitap → 2MP nidâ; 'rasûlu'llâh' / 'yedeyi'llâhi ve rasûlih'); 48:29 → 49:3 'mağfira + ecr azîm'; 48:12 'zuyyine … fî qulûbikum' → 49:7 'zeyyenehû fî qulûbikum'; 47 'ahbata' → 49:2 'habita'; 48:6/12 'zann' → 49:12; 48:11 'se-yeqûlu … a'râb' → 49:14 'qâleti'l-a'râb'; 48:24 → 49:18 'bimâ ta'melûne basîr'. 49:18 → 50:1 henüz okunmadı. Test korpus sonunda. "
"Okumada görülen dizi ve çerçeveler (KAPATILAMAZ, sayı iddiası değil): nidâ 'yâ eyyuhe'llezîne âmenû' 49:1, 2, 6, 11, 12 → 'yâ eyyuhe'n-nâs' 49:13 (hitap genişliyor); ses 49:2 yükseltme / 49:3 kısma (31:19 'veğdud min savtik'); 'fî qulûbikum' 49:7 iman süslendi / 49:14 iman henüz girmedi; 'îmân / fusûq' 49:7 ve 49:11; 'ulâ'ike hum' + sıfat 49:7 râşidûn, 49:11 zâlimûn, 49:15 sâdiqûn; 'innema'l-mu'minûn' 49:10 ve 49:15 (24:62 açılışı); 'aslihû beyne' 49:9 ×2, 49:10; 38:22 'beğâ … alâ' / 49:9; erkek / kadın çiftleri 49:11 ve 49:13; 'menne + alâ' 26:22, 14:11 → 49:17; açılış 'semî'un alîm' / kapanış 'basîrun bimâ ta'melûn'. "
"Kayıt düzeltmesi yok (DUZELTME boş). Bu sûrede kök tablosuna 6 kök eklendi (kok_ekle_49: محن نبز لقب جسس شعب ليت); retroaktif gloss yaması 0. "
"Tekrarlayan arıza aileleri (ayet listeleri blok ARIZA kayıtlarında): nidâ ayetlerinde konuşan adlanmıyor, muhatap 2MS adsız ('qul' 49:14, 16, 17; 49:4-5), 49:13 1P → 3MS ölçümde iltifât 0, 49:17 1S 'aleyye' alıntıda (1017); ölçüm MÜHÜRSÜZ / esma_kayit EVET (1022); tekit 'inne' / 'innâ', teşbih, 'lâkinne' / 'lâkin', takdim, hasr 'innemâ', zemm 'bi'se', 'lemmâ' ölçümde yok (517); قبل gloss'u 'kabîle'yi, سخر gloss'u 'alay etme'yi kapsamıyor (1021); 49:1 harf sayımı besmeleyi katıyor olabilir (924); 49:13 kafiye kırığında ★ kaynak etiketi (1001). "
"Karar bekleyen (kullanıcı kararıyla açık): 48:29 çıpa (L4 adayı, teşbih içinde); S2 ◈K tetik فلك kesinliği; مأي gloss; oturum_* yardımcılarının depoda kalması.")}

p = REPO + 'okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
assert len([k for k in OM[str(S)] if not k.startswith('_')]) == N, 'sûre 49 kaydı eksik — DUR'
OM[str(S)].update(KAP)
I = OM['ilerleme']
I['tam'] = sorted(set(I['tam']) | {S})
I['kismi'].pop(str(S), None)
okunan = sum(1 for r in D.values() if r['k'][0] in set(I['tam']) or (r['k'][0] == 2 and r['k'][1] <= 20))
I['okunan_ayet'] = okunan
I['korpus_yuzde'] = round(100 * okunan / len(D), 1)
I['not'] = "Sûre 1, 9-48 ve **49 TAM**. Devam: sûre 50'den ya da sûre 2'nin 21. ayetinden."
I['son_oturum'] = 'OKU_BENI_OTURUM.md (sûre 49 tur sonu)'
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
subprocess.run([sys.executable, 'duzeltme_49.py'], check=True)

E['_profil_49'] = esma
json.dump(E, open('esma_kayit.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)

print(json.dumps({'bilanco': bil, 'cipa': cipa, 'esma': esma}, ensure_ascii=False, indent=1))
print('ilerleme:', okunan, '(%', I['korpus_yuzde'], ')  tam:', I['tam'][-3:])
