# -*- coding: utf-8 -*-
from kavram_arac import profil
import json

# Kavramların metinden öğrenilmiş TANIMLARI (bu oturumda ölçtüğümüz haliyle)
# tanım = kavramın Kur'an'daki yapısal karakteri (meal DEĞİL)
TANIMLAR={
 'حقق':"Allah'tan gelen sabit gerçeklik; hem sıradan doğruluk hem ilâhî isim (10:32 'işte gerçek Rabbiniz Allah'). Evreni ayakta tutan (23:71). Zıttı katmanlı: inkâr eden küfür, sapan dalâlet, yok-olucu bâtıl, çiğneyen zulüm, yalanlayan tekzip.",
 'صبر':"İmtihan karşısında namazla desteklenen, karşılıklı tavsiye edilen daimî tutum (2:153, 90:17). Belirli zamana bağlı değil, her an gereken duruş. Bir kavrama değil, bir duruma (imtihan/fitne) karşı kurulur.",
 'رحم':"Her şeyi kuşatan (7:156), mağfiretle iç içe, ümit-veren ilâhî sıfat; hem isim (Rahmân/Rahîm) hem eylem (âlemlere rahmet, 21:107). Metnin açık çifti azap (25 ayet), ama simetrik değil: rahmet baskın, azap onun içinde bir seçenek.",
 'علم':"Allah'ın kuşatıcı bilgisi ve insana öğretilen (Rahmân öğretti, 55:2); kavram ağının ortak komşusu — neredeyse her kavram ilimle bağlı. Gaybın karşısında insana verilen az pay (17:85 'size az ilim verildi').",
 'وقي':"İman + amel + Allah-bilinci + sınır-koruma; azık (2:197), değer-ölçüsü (49:13 'en değerliniz en takvâlınız'). Zıttı küfür. Koruyucu bir bilinç hâli.",
 'عدل':"Tam karşılık/denge; teşrî sûrelerinde yoğun, komşusu şahitlik ve mîzan. 16:90 adl+ihsan (adalet=tam hak, ihsan=fazlası rahmet lehine). Zıttı zulüm (dengeyi bozmak).",
 'شكر':"Nimeti tanıyıp karşılık verme; zıttı küfür (nankörlük — aynı kök ailesinde inkârla buluşur). Rızık ve nimet komşulu.",
 'وحد':"Tevhid — Allah'ın birlenmesi; kök mirör şirk (ortak koşma). Metnin en sert testi: şirk bağışlanmaz çünkü kendini rahmetin dışına koyar.",
}
# zıt ve durum adayları (metne sorulacak — dayatma değil)
ZIT={
 'حقق':{'كفر','ضلل','بطل','ظلم','كذب','شرك'},
 'رحم':{'عذب','غضب','لعن','نقم','قسو','شدد','هلك'},
 'علم':{'جهل','ظنن','غفل'} if False else {'ظلم','كفر'},
 'وقي':{'كفر','فسق','ظلم','فجر'},
 'عدل':{'ظلم','بغي','جور'},
 'شكر':{'كفر','بطر'},
 'وحد':{'شرك','كفر'},
}
DURUM={
 'صبر':{'بلو','فتن','ضرر','خوف','مصب'},
}
sozluk={}
for kok,tanim in TANIMLAR.items():
    p=profil(kok,tanim.split(';')[0][:40],ZIT.get(kok),DURUM.get(kok))
    if not p:
        print("✗ BULUNAMADI: kök '%s' morfolojide yok — kök kodunu kontrol et"%kok)
        continue
    if p:
        p['tanim']=tanim  # tam tanım
        sozluk[kok]=p
        print("✓ %s (%d ayet) — ses:%s zaman-şimdi:%.2f zıt:%s"%(
            p['ad'][:20],p['ayet_sayisi'],p['ses']['imza'],
            p['zaman'].get('şimdi',0),
            ', '.join(list(p['zit'].keys())[:2]) if p['zit'] else '(durum)'))
json.dump(sozluk,open('kavram_sozlugu.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print("\n→ kavram_sozlugu.json yazıldı (%d kavram)"%len(sozluk))
