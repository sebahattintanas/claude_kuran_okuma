# -*- coding: utf-8 -*-
"""secde_kapanis.py — sûre 32 (Secde) kapanış notları, çıpa tablosu ve ilerleme."""
import json, gloss_gecis

ATLAMA = {
 "_cipa_tablosu_32": (
  "SÛRE 32 ÇIPA KAYITLARI — **iki çıpa ve ikisi de tarayıcı tarafından yakalandı.** "
  "**32:5 (L4, ÖLÇÜ)** — 'ölçüsü sizin saydıklarınızdan bin yıl olan bir gün': açık ölçü kelimesi (مِقْدَار), "
  "sayı (أَلْف) ve karşılaştırma (مِمَّا تَعُدُّونَ). Aynı ölçü kalıbı korpusta üç ayette (22:47, 32:5, 70:4) ve "
  "'O'na yükseliş' iki ayette iki farklı süreyle veriliyor: iş 1.000 yıl (32:5), melekler ve Rûh 50.000 yıl "
  "(70:4) — süre yükselen şeye bağlı. "
  "**32:27 (L2, NEDENSELLİK)** — araç zamiriyle kurulmuş üç halkalı zincir: suyu kurak yere sürme → ONUNLA "
  "(بِهِ) ekin → hayvan ve insanın ondan yemesi. "
  "**Çıpa olmayan ama kademe taşıyanlar:** 32:7, 32:8, 32:9 (L1, insanın yaratılış maddeleri ve sırası; "
  "yaratılış sırası grafiğinin ÜÇ kenarının kaynağı) · 32:4 (L1, altı gün + istivâ)."),

 "_tarayici_32": (
  "**TARAYICI v4 SÛRE 32'DE TAM İSABET — anma 2/2, kesinlik 2/2.** Sûre 30'da 2/9 ve 0/5, sûre 31'de 0/3 ve "
  "0/7 idi. İki aday verdi (32:5 F_ölçü, 32:27 G_bakış) ve ikisi de gerçek çıpa çıktı. "
  "**Fark ölçütte değil metinde:** sûre 32'nin iki olgu ayeti ölçü kelimesi ve bakış sorusu taşıyor, yani "
  "tarayıcının aradığı söz eylemi işaretleri bu sefer gerçekten çıpanın üzerinde. "
  "**Aday 948 için birikim artık dört sûre:** 27-29 yüksek anma · 30 çöküş · 31 sıfır · 32 tam isabet. "
  "Ölçüt DEĞİŞTİRİLMEDİ."),

 "_eksen_kutuplari_32": (
  "EKSEN — **sûre 32: lafız 1 (yalnız 32:4) · Rab 10 → A/R = 0,1.** Bir önceki sûre 31'de 32 lafız / 2 Rab "
  "(A/R = 16,0) idi. **Arka arkaya iki sûre eksenin iki ucunda.** "
  "Dizi: 27→2,25 · 28→1,42 · 29→8,4 · 30→8,0 · 31→16,0 · **32→0,1.** "
  "Oranlar küçük paydalarla oynadığı için ham sayı okunur: 32 lafız/2 Rab ve 1 lafız/10 Rab."),

 "_yildiz_kaynagi_32": (
  "YILDIZ KAYNAKLARI (TAM SAYIM) — ★★★ 1 · ★★ 4 · ★ 2 · yıldızsız 23. "
  "Kaynaklar: **hapaks 1 (32:16 جفو, otomatik tetikleyici, borç #7) · edilgenlik 2 (32:11, 32:22) · rab 3 · "
  "kafiye kırığı 1 (32:23)**. İçerikten gelen yıldız yok. "
  "**32:23 sûrenin tek kafiye kırığı:** fâsıla إسرٓءيل → ل, yirmi sekiz ن'lik akışı tek başına bozuyor ve "
  "ayetin ★'ının tek kaynağı bu."),

 "_esma_arizasi_32": (
  "ESMÂ — 5 token, 3 ayette. **Mühürlü 3/3 geçerli** (hepsi 32:6: عالِم + عَزِيز + رَحِيم). "
  "**Mühürsüz 2 ve ikisi de yanlış pozitif:** 32:4 وَلِيّ ('O'ndan başka dost yok' — ilâhî değil, ORTA konum) · "
  "32:18 مُؤْمِن ('inanan kişi', P0 şüpheli lemma listesindeki vaka). "
  "Sûre 31 ile birlikte mühürsüzlerde yanlış pozitif **8/10**."),

 "_kapanis_32": (
  "SÛRE 32 KAPANIŞI — 30 ayet, 372 kelime, tamamı Mekkî. "
  "KAFİYE: N 28 · ل 1 · mukattaa 1 — sûre 31'in aksine tek akış. "
  "ADLI AKTÖR: Mûsâ ve İsrâiloğulları (32:23) · Cehennem (32:13). İltifât yalnız 32:28. "
  "BAĞ HEDEFLERİ: 10, 21, 22 (üçer) · 25, 30, 67 (ikişer) — sûre 31'in Hac'a yaslanan yapısı burada yok. "
  "YENİ KÖK **5** (جدد مهن جفو ضجع جرز) → kok_turkce **1090**. "
  "YAPI: sûre yaratılışla açılıyor (32:4-9), insana verilen yetileri sayıyor (32:9: işitme, gözler, gönüller) "
  "ve tam o yetilere yapılan iki soruyla kapanıyor: 'işitmiyorlar mı?' (32:26) · 'görmüyorlar mı?' (32:27). "
  "SÛRE İÇİ KÖK: سوي üç kez, üç ayrı anlamda — istivâ (32:4) · düzenleme (32:9) · eşitlik (32:18). "
  "أوي iki kez, iki karşıt yer — Me'vâ cenneti (32:19) · ateş (32:20). "
  "عرض iki kez, ters yönlerde — onlar yüz çeviriyor (32:22) · 'sen yüz çevir' (32:30)."),
}

ATLAMA = {k: gloss_gecis.gecir(v) for k, v in ATLAMA.items()}

D = json.load(open('defter.json', encoding='utf-8'))
TAM = set([1] + list(range(9, 33)))
okunan = sum(1 for r in D if r['k'][0] in TAM or (r['k'][0] == 2 and r['k'][1] <= 20))

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
OM['32'].setdefault('_mercek_atlama_notu', {}).update(ATLAMA)
OM['ilerleme']['tam'] = sorted(set(OM['ilerleme']['tam']) | {32})
OM['ilerleme']['not'] = "Sûre 1, 9-31 ve **32 TAM**. Devam: sûre 33'ten ya da sûre 2'nin 21. ayetinden."
OM['ilerleme']['okunan_ayet'] = okunan
OM['ilerleme']['korpus_yuzde'] = round(100 * okunan / len(D), 1)
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 32 →', len([k for k in OM['32'] if not k.startswith('_')]),
      'ayet +', len(OM['32']['_mercek_atlama_notu']), 'kapanış notu')
print('ilerleme:', OM['ilerleme']['okunan_ayet'], 'ayet (%', OM['ilerleme']['korpus_yuzde'], ')')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK['32_atlama'] = ATLAMA
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: 32_atlama →', len(MK['32_atlama']))
