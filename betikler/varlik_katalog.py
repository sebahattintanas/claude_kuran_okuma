# -*- coding: utf-8 -*-
"""VARLIK KATALOĞU — genişletilmiş. Türler metin-bilgisiyle verildi."""
from varlik_makinesi import oku
import json

KATALOG=[
 # ── KAVRAMLAR (beş katman + zıt) ──
 ('hak',('kok','حقق'),'kavram',{'كفر','ضلل','بطل','ظلم','كذب','شرك'}),
 ('rahmet',('kok','رحم'),'kavram',{'عذب','غضب','لعن','نقم','قسو'}),
 ('ilim',('kok','علم'),'kavram',{'كفر','ظلم','جهل'}),
 ('takvâ',('kok','وقي'),'kavram',{'كفر','فسق','ظلم','فجر'}),
 ('sabır',('kok','صبر'),'kavram',None),
 ('adalet',('kok','عدل'),'kavram',{'ظلم','بغي'}),
 ('şükür',('kok','شكر'),'kavram',{'كفر'}),
 ('tevhid',('kok','وحد'),'kavram',{'شرك','كفر'}),
 ('iman',('lem','آمَنَ'),'kavram',{'كفر','شرك','نفق'}),
 ('hidâyet',('kok','هدي'),'kavram',{'ضلل'}),
 ('sevgi',('kok','حبب'),'kavram',{'بغض','كره'}),
 ('emanet',('kok','امن'),'kavram',{'خون'}),
 ('ihsan',('kok','حسن'),'kavram',{'سوأ'}),
 ('merhamet',('kok','رحم'),'kavram',{'قسو'}),
 # ── PEYGAMBERLER/KİŞİLER ──
 ('Mûsâ',('pn','مُوسَى'),'kişi',None),
 ('İbrâhîm',('pn','إِبْراهِيم'),'kişi',None),
 ('Nûh',('pn','نُوح'),'kişi',None),
 ('Îsâ',('pn','عِيسَى'),'kişi',None),
 ('Yûsuf',('pn','يُوسُف'),'kişi',None),
 ('Süleymân',('pn','سُلَيْمان'),'kişi',None),
 ('Dâvûd',('pn','داوُد'),'kişi',None),
 ('Hârûn',('pn','هارُون'),'kişi',None),
 ('İshâk',('pn','إِسْحاق'),'kişi',None),
 ('Yâkûb',('pn','يَعْقُوب'),'kişi',None),
 ('İsmâîl',('pn','إِسْماعِيل'),'kişi',None),
 ('Âdem',('pn','آدَم'),'kişi',None),
 ('Meryem',('pn','مَرْيَم'),'kişi',None),
 ('Lût',('pn','لُوط'),'kişi',None),
 ('Şuayb',('pn','شُعَيْب'),'kişi',None),
 ('Sâlih',('pn','صالِح'),'kişi',None),
 ('Hûd',('pn','هُود'),'kişi',None),
 ('Zekeriyyâ',('pn','زَكَرِيّا'),'kişi',None),
 ('Yahyâ',('pn','يَحْيَى'),'kişi',None),
 ('Eyyûb',('pn','أَيُّوب'),'kişi',None),
 ('Yûnus',('pn','يُونُس'),'kişi',None),
 ('Lokmân',('pn','لُقْمان'),'kişi',None),
 # ── KARŞI-FİGÜRLER ──
 ('Firavun',('pn','فِرْعَوْن'),'kişi',None),
 ('İblîs/şeytan',('pn','شَيْطان'),'kişi',None),
 ('Hâmân',('pn','هامان'),'kişi',None),
 ('Kârûn',('pn','قارُون'),'kişi',None),
 # ── KAVİMLER ──
 ('Âd',('kelime','عاد'),'kavim',None),
 ('Semûd',('kelime','ثمود'),'kavim',None),
 ('İsrâîloğulları',('pn','إِسْرائِيل'),'kavim',None),
 ('Medyen',('pn','مَدْيَن'),'kavim',None),
 ('Kureyş',('pn','قُرَيْش'),'kavim',None),
 # ── YERLER/ÂLEMLER ──
 ('Arş',('kelime','عرش'),'yer/âlem',None),
 ('cennet',('kelime','الجنة|جنة'),'yer/âlem',None),
 ('cehennem',('kelime','جهنم'),'yer/âlem',None),
 ('gök(çoğul)',('kelime','سماوات|سموت'),'yer/âlem',None),
 ('yer/arz',('kok','ارض'),'yer/âlem',None),
 ('Tûr',('pn','طُور'),'yer/âlem',None),
 # ── KİTAPLAR ──
 ('Kur\'ân',('lem','قُرْءان'),'kitap',None),
 ('Tevrât',('lem','تَوْراة'),'kitap',None),
 ('İncîl',('pn','إِنجِيل'),'kitap',None),
 # ── OLAYLAR (fiil) ──
 ('secde',('kok','سجد'),'olay',None),
 ('yaratma',('kok','خلق'),'olay',None),
 ('rükû',('kok','ركع'),'olay',None),
 ('tesbih',('kok','سبح'),'olay',None),
 ('diriliş',('kok','بعث'),'olay',None),
 # ── KOZMOS ──
 ('güneş',('kok','شمس'),'olay',None),
 ('ay',('kok','قمر'),'olay',None),
 ('yıldız',('kok','نجم'),'olay',None),
 ('gece',('kok','ليل'),'olay',None),
 # ── TEKİL SAHNELER ──
 ('karınca',('kelime','النمل|نملة'),'tekil-sahne',None),
 ('örümcek',('kelime','عنكبوت'),'tekil-sahne',None),
 ('sinek',('kelime','ذباب'),'tekil-sahne',None), # ── EKSİK DÜZELTMELER ──
 ('Tûr',('lem','طُور'),'yer/âlem',None),
 ('İdrîs',('pn','إِدْرِيس'),'kişi',None),
 ('arı',('lem','نَحْل'),'tekil-sahne',None),
 ('Hüdhüd',('lem','هُدْهُد'),'tekil-sahne',None),
 # ── TABİAT/KOZMOS (olay/yer) ──
 ('nehir',('kok','نهر'),'yer/âlem',None),
 ('deniz',('kok','بحر'),'yer/âlem',None),
 ('dağ',('kok','جبل'),'yer/âlem',None),
 ('kuş',('kok','طير'),'olay',None),
 ('ağaç',('kok','شجر'),'olay',None),
 ('meyve',('kok','ثمر'),'olay',None),
 ('yağmur',('kok','مطر'),'olay',None),
 ('rüzgâr',('kok','روح'),'olay',None),
 # ── İBADET/EYLEM ek ──
 ('namaz',('kok','صلو'),'olay',None),
 ('zekât',('kok','زكو'),'olay',None),
 ('oruç',('kok','صوم'),'olay',None),
 ('hac',('kok','حجج'),'olay',None),
 ('dua',('kok','دعو'),'olay',None),
 ('tevbe',('kok','توب'),'olay',None),
 # ── KAVRAM ek ──
 ('mağfiret',('kok','غفر'),'kavram',{'عذب'}),
 ('mîzan/ölçü',('kok','وزن'),'kavram',None),
 ('kader/ölçü',('kok','قدr'),'kavram',None),
 ('emr',('kok','امر'),'kavram',None),
 ('rızık',('kok','رزق'),'kavram',None),
 ('nimet',('kok','نعم'),'kavram',{'عذب'}),
 ('fitne',('kok','فتن'),'kavram',None),
 ('cihad',('kok','جهد'),'kavram',None),
 # ── KARŞI-FİGÜR/KAVİM ek ──
 ('Câlût',('pn','جالُوت'),'kişi',None),
 ('Tâlût',('pn','طالُوت'),'kişi',None),
 ('Ye\'cûc-Me\'cûc',('kelime','ياجوج|ماجوج'),'kavim',None),

 ('arı',('pn','نَحْل'),'tekil-sahne',None),
 ('Hüdhüd',('pn','هُدْهُد'),'tekil-sahne',None),
]

def calistir():
    katalog={}; tur_say={}
    for ad,(mod,val),tur,zit in KATALOG:
        r=oku(ad,**{mod:val,'tur':tur,'zit_adaylari':zit})
        if r.get('hata'):
            print("✗ %-14s %s"%(ad,r['hata'])); continue
        katalog[ad]=r
        tur_say[tur]=tur_say.get(tur,0)+1
    # tür tür yazdır
    for tur in ['kavram','kişi','kavim','yer/âlem','kitap','olay','tekil-sahne']:
        varliklar=[(ad,r) for ad,r in katalog.items() if r['tur']==tur]
        if not varliklar: continue
        print("\n── %s (%d) ──"%(tur.upper(),len(varliklar)))
        for ad,r in varliklar:
            extra=''
            if r.get('zit'): extra='zıt:'+list(r['zit'].keys())[0]
            print("  %-16s %3d ayet  %s"%(ad,r['ayet_sayisi'],extra))
    json.dump(katalog,open('varlik_katalog.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print("\n→ %d varlık, %d tür → varlik_katalog.json"%(len(katalog),len(tur_say)))
    return katalog

if __name__=='__main__':
    calistir()
