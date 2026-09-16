# -*- coding: utf-8 -*-
"""20_sayilari_tazele.py — anahtar_denetim.py, 17_cipa_tarama2.py'deki elle yazılmış
edatları BOZUK işaretledi; eşleme morfoloji lemmasına taşındı ve havuz 586→537'ye
daraldı. Aday 921/922/923'ün sayıları taze koşumdan güncellenir."""
import json
pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
YENI = {
 921: {"aday_ayet": 537, "korpus_oran_yuzde": 8.6,
       "isaret_ailesi": {"A_şart": 339, "B_ta’lîl": 132, "D_yeti": 93, "C_recâ": 52,
                         "A_levlâ": 14, "E_görünüş": 12},
       "kesinlik_sure_27": "4/5 (%80)", "kesinlik_sure_28": "3/12 (%25)",
       "kesinlik_toplam": "7/17 (%41)",
       "denetim_notu": "ilk yazımda edatlar ELLE, iskelet yazımıyla girilmişti "
                       "(لولا/لعل/حتا/لكيلا); anahtar_denetim.py dördünü de BOZUK "
                       "işaretledi — ikisi YAZIM, ikisi korpusta HİÇ YOK. Eşleme "
                       "morfoloji lemmasına taşındı (COND|LEM:لَوْلا · ACC|LEM:لَعَلّ · "
                       "SUB|LEM:كَي); havuz 586→537, anma 7/7 KORUNDU, kesinlik "
                       "%33→%41 YÜKSELDİ."},
 922: {"havuz_yildiz_yuzde": 50.8, "havuz_ort_n": 23.54, "uzunluk_kati": 1.9},
 923: {"yanlis_pozitif": 10, "lemma_kusurundan": 5, "oran_yuzde": 50,
       "gercek_yanlis_pozitif": 5,
       "kesinlik_simdi_yuzde": 41, "kesinlik_lemma_ile_yuzde": 58},
}
for a in AD['AJ_kasas']:
    if a['no'] in YENI:
        a['olculen'].update(YENI[a['no']])
        a.setdefault('tazeleme', []).append(
            'sayılar 20_sayilari_tazele.py ile güncellendi (anahtar_denetim düzeltmesi sonrası)')
        print('aday %d güncellendi' % a['no'])
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
