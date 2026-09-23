# -*- coding: utf-8 -*-
"""32:5 'bin yıl' → hız hesabının varsayım duyarlılığı.
Metin bir SÜRE veriyor; hız hesabı metinde olmayan varsayımlar ekler. Bu betik her varsayımı ayrı ayar yapar.
Sabitler (standart astronomik değerler):"""
import math, itertools
C      = 299_792.458          # ışık hızı, km/s
A_AY   = 384_400.0            # Ay'ın ortalama uzaklığı (yarı büyük eksen), km — dairesel yörünge yaklaşımı
T_YILDIZ_AYI   = 27.321661    # gün (sidereal)
T_KAVUSUM_AYI  = 29.530589    # gün (synodic, hilâlden hilâle)
T_YILDIZ_YILI  = 365.256363   # gün (Dünya'nın Güneş etrafındaki turu)
T_GUNES_YILI   = 365.242190   # gün (tropikal yıl)
GUN_GUNES  = 86_400.0         # s
GUN_YILDIZ = 86_164.0905      # s
V_DUNYA    = 29.78            # km/s, Dünya'nın yörünge hızı (Güneş merkezli çerçeve için)

v_ay = 2*math.pi*A_AY/(T_YILDIZ_AYI*86400)   # km/s, Dünya'ya göre Ay'ın yörünge hızı
satirlar=[]
for yil, ay, duz, gun, cerceve in itertools.product(
        ['ay yılı (12 ay)','güneş yılı'], ['yıldız ayı','kavuşum ayı'], ['yok','cos α'], ['güneş günü','yıldız günü'], ['Dünya merkezli','Güneş merkezli']):
    T_ay = T_YILDIZ_AYI if ay=='yıldız ayı' else T_KAVUSUM_AYI
    sure_gun = 1000*12*T_ay if yil=='ay yılı (12 ay)' else 1000*T_GUNES_YILI
    if yil=='güneş yılı' and ay=='kavuşum ayı': continue      # güneş yılında ay türü anlamsız; tek satır yeter
    v = v_ay if cerceve=='Dünya merkezli' else math.hypot(v_ay, V_DUNYA)   # kaba: iki hızın bileşkesi
    f = math.cos(2*math.pi*T_ay/T_YILDIZ_YILI) if duz=='cos α' else 1.0
    mesafe = v*f*sure_gun*86400
    g = GUN_GUNES if gun=='güneş günü' else GUN_YILDIZ
    hiz = mesafe/g
    satirlar.append((yil, ay if yil.startswith('ay') else '—', duz, gun, cerceve, hiz, hiz/C))
satirlar.sort(key=lambda r: abs(r[6]-1))
print(f"Ay'ın Dünya'ya göre yörünge hızı: {v_ay:.4f} km/s")
print(f"{'yıl':16s} {'ay türü':11s} {'düzeltme':8s} {'gün':11s} {'çerçeve':15s} {'hız km/s':>14s} {'hız / c':>9s}")
for r in satirlar: print(f"{r[0]:16s} {r[1]:11s} {r[2]:8s} {r[3]:11s} {r[4]:15s} {r[5]:14,.0f} {r[6]:9.4f}")
print('\n70:4 (elli bin yıl), aynı akıl yürütme: her satırın hızı ×50. En yakın satır →', f"{satirlar[0][5]*50:,.0f} km/s = {satirlar[0][6]*50:.1f} c")

# ---- Mesafe karşılığı (bir günde gidilen yol = Ay'ın bin yılda kat ettiği yol)
AU = 149_597_870.7; ISIK_YILI = 9.4607304725808e12; ISIK_GUNU = C*86400
import statistics as st
def mesafe(r):
    g = GUN_GUNES if r[3]=='güneş günü' else GUN_YILDIZ
    return r[5]*g
d_all=[mesafe(r) for r in satirlar]; d_dun=[mesafe(r) for r in satirlar if r[4]=='Dünya merkezli']
def yaz(ad,d): print(f"{ad:34s} {d:>22,.0f} km = {d/AU:9,.1f} AU = {d/ISIK_GUNU:6.2f} ışık-günü = {d/ISIK_YILI:.5f} ışık yılı")
print('\n=== MESAFE ===')
yaz('en yakın (ışık hızına en yakın satır)', mesafe(satirlar[0]))
yaz('en küçük', min(d_all)); yaz('en büyük (en uzun sapma)', max(d_all))
yaz('ortalama (24 kombinasyon)', st.mean(d_all)); yaz('medyan (24 kombinasyon)', st.median(d_all))
yaz('ortalama (Dünya merkezli 12)', st.mean(d_dun)); yaz('medyan (Dünya merkezli 12)', st.median(d_dun))
yaz('70:4 aynı akıl yürütme (en yakın ×50)', mesafe(satirlar[0])*50)
print('\nKarşılaştırma: Neptün ~30 AU · Heliopoz ~120 AU · Voyager 1 (Kasım 2026) ~173,8 AU = 1 ışık-günü · Oort bulutu iç sınırı ~2.000 AU · Proxima Centauri 4,24 ışık yılı ≈ 268.000 AU')

# ---- Referans çerçevesi genişletmesi: Galaksi ve CMB
V_GUNES_GALAKSI = 230.0   # km/s, Güneş'in Galaksi merkezi etrafındaki hızı (yaklaşık, 220-240 aralığı)
V_GUNES_CMB     = 369.8   # km/s, Güneş sisteminin kozmik arka plan ışımasına göre hızı (dipol)
print('\n=== ÇERÇEVE KARŞILAŞTIRMASI (yıldız ayı, cos α yok, güneş günü) ===')
T = 1000*12*T_YILDIZ_AYI*86400
for ad,v in [('Dünya merkezli',v_ay),('Güneş merkezli',math.hypot(v_ay,V_DUNYA)),('Galaksi merkezli',V_GUNES_GALAKSI),('CMB çerçevesi',V_GUNES_CMB)]:
    d=v*T; print(f"{ad:17s} hız {v:9.3f} km/s → yol {d/AU:12,.0f} AU = {d/ISIK_YILI:8.4f} ışık yılı → 'bir günde' {d/86400/C:8.1f} c")
