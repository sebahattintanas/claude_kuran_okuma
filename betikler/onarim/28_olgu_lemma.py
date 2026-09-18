# -*- coding: utf-8 -*-
"""28_olgu_lemma.py — ONARIM 18 (P0 #5'in çıpa taraması tarafındaki onarımı).

ARIZA (aday 923): çıpa tarayıcısı olgu alanını KÖK düzeyinde eşliyor. Kök olgu
alanında görünüyor ama ayetteki lemma başka anlam alanında olunca yanlış pozitif
çıkıyor. Sûre 27-29'daki 10 yanlış pozitifin 4'ü (%40) bu sebeple.

ONARIM: olgu alanı KÖK yerine (kök, lemma) çifti düzeyinde tanımlanır.
74 olgu kökünün 51'i çok lemmalı; her biri için olgu anlamındaki lemmalar
elle işaretlendi (envanter `lemma_envanteri.json`'dan koşuldu, elle taranmadı —
karar yalnız hangi lemmanın olgu alanında olduğu).

Tek lemmalı 19 olgu kökü (أرض · شمس · قمر · نجم · كوكب · مسو · رعد · ثلج · نبع ·
روس · عنب · زتن · رمن · ريح · لقح · جوو · دبب · عنكب · نطف · مضغ · لحم · ذرأ ·
سبت? ) olduğu gibi kalır: tek lemma, ayrım gereksiz.
"""
import json, unicodedata

# (kök, lemma) — yalnız OLGU anlamındaki lemmalar. Kökün öbür lemmaları düşer.
OLGU_LEMMA = {
 'أجل':  {'أَجَل', 'أَجَّلَ', 'مُؤَجَّل'},          # ecel/süre; 'أَجْل' (sebep) düşer
 'بحر':  {'بَحْر'},                                  # بَحِيرَة (adak devesi) düşer
 'برد':  {'بَرْد', 'بارِد', 'بَرَد'},
 'برق':  {'بَرْق', 'بَرِقَ'},                        # أَبارِيق (ibrik) düşer
 'بعض':  {'بَعُوضَة'},                               # بَعْض (bir kısım) düşer — canlı olan sivrisinek
 'ثمر':  {'ثَمَرَة', 'ثَمَر', 'أَثْمَرَ'},
 'جبل':  {'جَبَل'},                                  # جِبِلَّة (nesil) düşer
 'جري':  {'جَرَيْ', 'جَوار', 'جارِيَة', 'مَجْرى'},
 'حبب':  {'حَبّ', 'حَبَّة'},                         # sevgi lemmaları düşer
 'حرث':  {'حَرْث', 'تَحْرُثُ'},
 'حرر':  {'حَرّ', 'حَرُور'},                         # azat/ipek düşer
 'حسب':  {'حُسْبان'},                                # sanma/hesap düşer — yalnız gök cisimlerinin hesabı
 'حيي':  {'حَياة', 'أَحْيا', 'حَيّ', 'مَحْيا', 'مُحْى', 'حَيَوان', 'حَيَّة'},
 'خلق':  {'خَلَقَ', 'خَلْق', 'خالِق', 'خَلّاق', 'خَلاق', 'مُخَلَّقَة'},   # خُلُق (huy), اخْتِلاق düşer
 'دور':  {'تَدُورُ', 'تُدِيرُ'},                     # دار (yurt) düşer
 'ذرو':  {'تَذْرُو', 'ذارِيَة', 'ذَرْو'},
 'رسو':  {'رَواسِي', 'أَرْسَى', 'مُرْسَى'},
 'روح':  {'رِيح'},                                  # rüzgâr; رُوح (rûh), رَوْح, رَيْحان düşer
 'زيت':  {'زَيْتُون', 'زَيْتُونَة', 'زَيْت'},
 'رقد':  {'رُقُود', 'مَرْقَد'},
 'زرع':  {'زَرْع', 'تَزْرَعُ', 'زُرّاع', 'زارِع'},
 'زوج':  {'زَوْج', 'زُوِّجَتْ'},
 'سبت':  {'سُبات'},                                  # سَبْت (cumartesi) düşer
 'سحب':  {'سَحاب'},                                  # يُسْحَبُ (sürüklenme) düşer
 'سخر':  {'سَخَّرَ', 'مُسَخَّرَة', 'مُسَخَّر'},      # alay lemmaları düşer
 'سمو':  {'سَماء'},                                  # اسْم/مُسَمًّى/سَمَّى düşer
 'شجر':  {'شَجَرَة', 'شَجَر'},                       # شَجَرَ (çekişme) düşer
 'صبح':  {'صُبْح', 'مُصْبِح', 'إِصْباح', 'صَباح'},   # أَصْبَحَ (yardımcı fiil), مِصْباح düşer
 'صعق':  {'صاعِقَة', 'صَعِقَ', 'صَعِق'},
 'ضوأ':  {'أَضاءَ', 'ضِياء'},
 'طير':  {'طَيْر', 'طائِر', 'يَطِيرُ'},              # اطَّيَّرْ (uğursuzluk) düşer
 'ظلل':  {'ظِلّ', 'ظُلَّة', 'ظَلَّلْ', 'ظَلِيل'},    # ظَلَّ (sürdürme) düşer
 'ظلم':  {'ظُلُمَة', 'مُظْلِم', 'أَظْلَمَ'},         # zulüm lemmaları düşer
 'عصف':  {'عَصْف', 'عاصِف', 'عاصِفَة'},
 'عظم':  {'عِظام', 'عَظْم'},                         # عَظِيم (büyüklük) düşer
 'علق':  {'عَلَقَة', 'عَلَق'},                       # مُعَلَّقَة düşer
 'عين':  {'عَيْن', 'مَعِين'},                        # عِين (iri gözlü) düşer
 'غيث':  {'غَيْث', 'يُغاثُ'},
 'فجر':  {'فَجْر', 'فُجِّرَتْ', 'تَفْجِير', 'انفَجَرَتْ', 'يَتَفَجَّرُ', 'يَفْجُرَ'},
 'فلك':  {'فُلْك', 'فَلَك'},
 'قدر':  {'قَدَر', 'قَدْر', 'تَقْدِير', 'مِقْدار', 'قَدَّرَ'},   # kudret lemmaları düşer
 'ليل':  {'لَيْل', 'لَيْلَة'},
 'مطر':  {'مَطَر', 'أُمْطِرَتْ', 'مُمْطِر'},
 'موت':  {'مَوْت', 'ماتَ', 'مَيِّت', 'أَماتَ', 'مَيْتَة', 'مَيْت', 'مَمات', 'مَوْتَت'},
 'نبت':  {'أَنۢبَتَ', 'نَبات', 'تَنۢبُتُ'},
 'نحل':  {'نَحْل'},                                  # نِحْلَة (bağış) düşer
 'نخل':  {'نَخْل', 'نَخِيل', 'نَخْلَة'},
 'نسل':  {'نَسْل', 'يَنسِلُ'},
 'نمل':  {'نَمْل', 'نَمْلَة'},                       # أَنامِل (parmak ucu) düşer
 'نهر':  {'نَهار', 'نَهَر'},                         # تَنْهَرْ (azarlama) düşer
 'نور':  {'نار', 'نُور', 'مُنِير'},
 'نوم':  {'مَنام', 'نَوْم', 'نائِم'},
}

TEK_LEMMALI = ['أرض', 'شمس', 'قمر', 'نجم', 'كوكب', 'مسو', 'رعد', 'ثلج', 'نبع',
               'عنب', 'زتن', 'رمن', 'لقح', 'جوو', 'دبب', 'عنكب',
               'نطف', 'مضغ', 'لحم', 'ذرأ',
               'موه']                              # ماء — tek lemma; ilk sürümde ATLANMIŞTI

# Lemma katmanının ÇÖZEMEDİĞİ olgu kökleri: aynı lemma iki anlam alanında.
# Olgu kümesinden ÇIKARILIR (ihtiyatlı taraf): tutmak yanlış pozitif üretir.
BAGLAM_GEREKLI = {
 'هوي': 'هَواء lemması hem "hava" (14:43) hem "heva, arzu" (28:50) taşıyor; '
        'morfoloji ayırmıyor',
}

# korpusta bulunmayan, OLGU kümesine yanlışlıkla girmiş kök
# OLGU kümesine yanlış yazılmış ya da korpusta hiç bulunmayan kökler.
# `anahtar_denetim.py` yakaladı; v3'ten beri SESSİZCE hiç eşleşmiyorlardı.
KORPUSTA_YOK = {
 'روس': 'yazım hatası — doğrusu رسو, zaten kümede',
 'ريح': 'yazım hatası — korpusta rüzgâr روح kökü altında (LEM:رِيح); روح eklendi',
 'زتن': 'yazım hatası — korpusta زيت; eklendi',
 'ثلج': 'korpusta HİÇ YOK (Kur\'an\'da kar geçmiyor)',
}

def coz(E):
    """Tabloda ELLE yazılmış lemmaları korpus biçimine çözer.

    Elle yazarken şedde ile hareke sırası korpustan farklı olabiliyor
    (0x64e+0x651 yerine 0x651+0x64e); NFC'de ikisi aynı. Proje kuralı gereği
    tabloya giren dizge KORPUSTAN kopyalanmış olmalı, bu yüzden her girdi
    NFC üzerinden korpus biçimine çevrilir ve çözülemeyen varsa DURULUR."""
    nfc = {}
    for k, v in E.items():
        for l in v:
            nfc[(k, unicodedata.normalize('NFC', l))] = l
    cozulmus, coz_yok = {}, []
    for k, ls in OLGU_LEMMA.items():
        yeni = set()
        for l in ls:
            g = nfc.get((k, unicodedata.normalize('NFC', l)))
            if g is None:
                coz_yok.append((k, l))
            else:
                yeni.add(g)
        cozulmus[k] = yeni
    return cozulmus, coz_yok


if __name__ == '__main__':
    E = json.load(open('lemma_envanteri.json', encoding='utf-8'))
    OLGU_LEMMA, coz_yok = coz(E)
    print('NFC ile korpus biçimine çözülemeyen girdi: %d  <- sıfır olmalı' % len(coz_yok))
    for k, l in coz_yok:
        print('   %s / %s  — korpustaki lemmalar: %s' % (k, l, list(E.get(k, {}))))
    assert not coz_yok, 'tablo korpusla tutarsız'
    print('=== ONARIM 18 — OLGU LEMMA TABLOSU ===')
    print('çok lemmalı olgu kökü : %d' % len(OLGU_LEMMA))
    print('tek lemmalı olgu kökü : %d (ayrım gereksiz)' % len(TEK_LEMMALI))
    tut = dus = 0
    hata = []
    for k, ls in OLGU_LEMMA.items():
        if k not in E:
            hata.append('%s korpusta yok' % k); continue
        yok = ls - set(E[k])
        if yok:
            hata.append('%s: tabloda olup korpusta olmayan lemma %s' % (k, yok))
        tut += sum(E[k][l] for l in ls if l in E[k])
        dus += sum(E[k][l] for l in E[k] if l not in ls)
    print('\ntablodaki lemmaların korpus token toplamı : %d' % tut)
    print('DÜŞEN token (olgu alanı dışındaki lemmalar): **%d** (%%%.1f)'
          % (dus, 100 * dus / (tut + dus)))
    print('tablo/korpus tutarsızlığı: %s' % (hata or 'YOK'))

    # KAPSAM DENETİMİ — OLGU kümesinin her kökü bir listede olmalı
    OLGU_KUME = set("""سمو أرض شمس قمر نجم كوكب ليل نهر صبح مسو فلك
موه مطر غيث سحب برق رعد صعق ثلج برد بحر عين نبع فجر
جبل رسو روس شجر نبت زرع ثمر حرث نخل عنب زتن رمن حبب
ريح عصف ذرو لقح هوي جوو طير دبب نحل نمل عنكب بعض
خلق نطف علق مضغ عظم لحم نسل ذرأ زوج موت حيي نوم رقد سبت
نور ضوأ ظلم ظلل حرر برد جري سخر قدر أجل حسب دور""".split())
    kapsanan = set(OLGU_LEMMA) | set(TEK_LEMMALI) | set(BAGLAM_GEREKLI) | set(KORPUSTA_YOK)
    acik = sorted(OLGU_KUME - kapsanan)
    print('KAPSAM AÇIĞI (hiçbir listede olmayan olgu kökü): %d  <- sıfır olmalı' % len(acik))
    for k in acik:
        print('   %s — korpusta: %s' % (k, list(E.get(k, {})) or 'YOK'))
    assert not acik, 'kapsam açığı: kök sessizce düşer'
    print('bağlam gerektirdiği için ÇIKARILAN kök: %d %s'
          % (len(BAGLAM_GEREKLI), list(BAGLAM_GEREKLI)))
    print('yazım hatası / korpusta yok: %d %s' % (len(KORPUSTA_YOK), list(KORPUSTA_YOK)))
    for k in KORPUSTA_YOK:
        if k in E:
            print('   UYARI: %s korpusta VAR, listeden çıkarılmalı' % k)
    json.dump({'cok_lemmali': {k: sorted(v) for k, v in OLGU_LEMMA.items()},
               'tek_lemmali': TEK_LEMMALI},
              open('olgu_lemma.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('olgu_lemma.json yazıldı')
