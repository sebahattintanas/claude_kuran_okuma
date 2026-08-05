#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dalga.py — SÛREYİ SES DALGASINA ÇEVİR
======================================
Kārîsiz iskeleti (tilavet_sentez.py) hem WAV dosyası hem görsel olarak üretir.

ÜRETİLENLER:
  dalga_cikti/<sûre>_<ayet>.wav      her ayet ayrı
  dalga_cikti/<sûre>_butun.wav       sûrenin tamamı (ayet arası duruşla)
  dalga_cikti/<sûre>_dalga.png       sûrenin bütünü — dalga, ayetler işaretli
  dalga_cikti/<sûre>_<ayet>_detay.png  bir ayetin dalgası + spektrogramı, medler etiketli

NE GÖSTERİR:
  - Medler: uzun, kararlı, yüksek genlikli bölgeler
  - Ünsüzler: kısa patlamalar / gürültü
  - Lîn (عَلَيْهِمْ'deki ye) ile Med (ٱلَّذِينَ'deki ye) yan yana görünür

DÜRÜST NOT: bu dalga METNİN değil, metnin verdiği ölçünün bir ALETTE
  gerçekleşmiş hâlidir. Perde (110 Hz düz) ve ayet arası duruş (0.55 sn)
  KEYFÎ — metin onları buyurmaz. Süre ve sesli kimliği metnin.

KULLANIM:
  python dalga.py            → Fâtiha (1)
  python dalga.py 108        → Kevser
  python dalga.py 50 1       → Kāf, ayrıca 1. ayetin detay görseli
"""
import os, sys, json, importlib.util
import numpy as np

CIKTI='dalga_cikti'
ARA=0.55          # ayet arası duruş — KEYFÎ

def yukle():
    if not os.path.exists('tilavet_sentez.py'): sys.exit("[!] tilavet_sentez.py gerekli")
    if not os.path.exists('kuran_veri.json'): sys.exit("[!] kuran_veri.json gerekli")
    spec=importlib.util.spec_from_file_location('ts','tilavet_sentez.py')
    ts=importlib.util.module_from_spec(spec); spec.loader.exec_module(ts)
    return ts, json.load(open('kuran_veri.json',encoding='utf-8'))

def wav_yaz(yol, y, sr):
    from scipy.io import wavfile
    wavfile.write(yol, sr, (np.clip(y,-1,1)*32767).astype(np.int16))

def main():
    sn = int(sys.argv[1]) if len(sys.argv)>1 else 1
    detay_ay = int(sys.argv[2]) if len(sys.argv)>2 else None
    ts, veri = yukle()
    s = next(x for x in veri['sureler'] if x['no']==sn)
    ad = s.get('ad_latin', str(sn))
    os.makedirs(CIKTI, exist_ok=True)
    print("═"*64)
    print("  %d. %s — %d ayet"%(sn, ad, len(s['ayetler'])))
    print("═"*64)

    # ---- her ayet + bütün ----
    parcalar=[]; sinir=[]; t=0.0; kayit=[]
    if s.get('besmele'):
        y,seg = ts.sentezle_iz(s['besmele'], 0)
        wav_yaz(os.path.join(CIKTI,"%03d_000_besmele.wav"%sn), y, ts.SR)
        parcalar.append(y); sinir.append((t, t+len(y)/ts.SR, 'besmele', seg))
        t += len(y)/ts.SR
        parcalar.append(np.zeros(int(ARA*ts.SR))); t += ARA
        kayit.append(('besmele', len(y)/ts.SR))
    for a in s['ayetler']:
        y,seg = ts.sentezle_iz(a['ar_saf'], a.get('mukattaa',0))
        wav_yaz(os.path.join(CIKTI,"%03d_%03d.wav"%(sn,a['no'])), y, ts.SR)
        parcalar.append(y); sinir.append((t, t+len(y)/ts.SR, str(a['no']), seg))
        t += len(y)/ts.SR
        parcalar.append(np.zeros(int(ARA*ts.SR))); t += ARA
        kayit.append((str(a['no']), len(y)/ts.SR))
    butun = np.concatenate(parcalar)
    wav_yaz(os.path.join(CIKTI,"%03d_butun.wav"%sn), butun, ts.SR)
    print("\n  WAV: %d ayet + bütün (%.1f sn)"%(len(s['ayetler']), len(butun)/ts.SR))
    for k,v in kayit[:4]: print("     %-9s %5.2f sn"%(k,v))
    if len(kayit)>4: print("     … (+%d)"%(len(kayit)-4))

    # ---- görsel: sûrenin bütünü ----
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    TAS='#EDE9E1'; CIVIT='#2E4374'; GUL='#A63D40'; ADA='#7D8471'; SONUK='#6B6558'
    sr=ts.SR
    fig,ax=plt.subplots(figsize=(15, 3.4), facecolor=TAS)
    ax.set_facecolor(TAS)
    zaman=np.arange(len(butun))/sr
    adim=max(1,len(butun)//9000)
    ax.plot(zaman[::adim], butun[::adim], lw=.45, color=CIVIT, alpha=.85)
    for b,e,et,seg in sinir:
        ax.axvspan(b,e, color=ADA, alpha=.07)
        ax.text((b+e)/2, 1.06, et, ha='center', va='bottom', fontsize=7.5, color=SONUK)
        for sb,se,set_,tip,li in seg:
            if tip=='med':
                ax.axvspan(b+sb, b+se, color=GUL, alpha=.30, lw=0)
    ax.set_xlim(0, len(butun)/sr); ax.set_ylim(-1.15,1.25)
    ax.set_xlabel('saniye', fontsize=8.5, color=SONUK)
    ax.set_yticks([])
    for sp in ('top','right','left'): ax.spines[sp].set_visible(False)
    ax.spines['bottom'].set_color('#D8D2C4')
    ax.tick_params(colors=SONUK, labelsize=8)
    ax.set_title('%d. %s — kārîsiz iskelet, sûrenin bütünü   (kırmızı: medler)'%(sn,ad),
                 fontsize=10.5, color=CIVIT, pad=12, loc='left')
    plt.tight_layout()
    p1=os.path.join(CIKTI,"%03d_dalga.png"%sn)
    plt.savefig(p1, dpi=150, facecolor=TAS); plt.close()
    print("  görsel: %s"%p1)

    # ---- görsel: bir ayetin detayı (dalga + spektrogram) ----
    if detay_ay is None: detay_ay = s['ayetler'][-1]['no']
    a = next((x for x in s['ayetler'] if x['no']==detay_ay), None)
    if a:
        y,seg = ts.sentezle_iz(a['ar_saf'], a.get('mukattaa',0))
        fig,(ax1,ax2)=plt.subplots(2,1, figsize=(15,6.4), facecolor=TAS,
                                   gridspec_kw={'height_ratios':[1,1.5]}, sharex=True)
        zt=np.arange(len(y))/sr
        ax1.set_facecolor(TAS)
        ax1.plot(zt, y, lw=.5, color=CIVIT, alpha=.85)
        for sb,se,et,tip,li in seg:
            if tip=='med':
                ax1.axvspan(sb,se, color=GUL, alpha=.25, lw=0)
                ax1.text((sb+se)/2, 1.02, et, ha='center', va='bottom',
                         fontsize=9, color=GUL, fontweight='bold')
            elif tip=='sesli':
                ax1.axvspan(sb,se, color=ADA, alpha=.16, lw=0)
            elif et in ('ي','و'):        # LÎN — med DEĞİL, metin sükûnla işaretliyor
                ax1.axvspan(sb,se, color=CIVIT, alpha=.35, lw=0)
                ax1.text((sb+se)/2, -1.02, 'lîn', ha='center', va='top',
                         fontsize=7.5, color=CIVIT, style='italic')
                ax2.axvspan(sb,se, color=CIVIT, alpha=.18, lw=0)
        ax1.set_ylim(-1.1,1.32); ax1.set_yticks([])
        for sp in ('top','right','left','bottom'): ax1.spines[sp].set_visible(False)
        ax1.set_title('%d:%d — dalga   kırmızı: MED (uzar) · lacivert: LÎN (uzamaz) · yeşil: kısa sesli'%(sn,detay_ay),
                      fontsize=10.5, color=CIVIT, pad=14, loc='left')
        # spektrogram
        ax2.set_facecolor(TAS)
        ax2.specgram(y+1e-9, NFFT=1024, Fs=sr, noverlap=896, cmap='bone_r', vmin=-95, vmax=-25)
        ax2.set_ylim(0,3200)
        ax2.set_ylabel('Hz', fontsize=8.5, color=SONUK)
        ax2.set_xlabel('saniye', fontsize=8.5, color=SONUK)
        ax2.tick_params(colors=SONUK, labelsize=8)
        for sp in ('top','right'): ax2.spines[sp].set_visible(False)
        for sp in ('left','bottom'): ax2.spines[sp].set_color('#D8D2C4')
        for sb,se,et,tip,li in seg:
            if tip=='med':
                ax2.axvline(sb, color=GUL, lw=.7, alpha=.5, ls='--')
                ax2.axvline(se, color=GUL, lw=.7, alpha=.5, ls='--')
        ax2.set_title('spektrogram — yatay bantlar formantlar. Medde uzun ve kararlı; lînde kısa geçiş.',
                      fontsize=9, color=SONUK, pad=8, loc='left')
        plt.tight_layout()
        p2=os.path.join(CIKTI,"%03d_%03d_detay.png"%(sn,detay_ay))
        plt.savefig(p2, dpi=150, facecolor=TAS); plt.close()
        print("  görsel: %s"%p2)
        print("\n  %d:%d medleri: %s"%(sn,detay_ay,
              [e[2] for e in seg if e[3]=='med']))
    print("\n  → hepsi %s/ klasöründe"%CIKTI)
    print("\n  DÜRÜST NOT: perde (110 Hz düz) ve ayet arası duruş (%.2f sn) KEYFÎ."%ARA)
    print("  Metin onları buyurmaz. Süre ve sesli kimliği metnin.")

if __name__=='__main__':
    main()
