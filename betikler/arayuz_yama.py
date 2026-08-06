# -*- coding: utf-8 -*-
"""
arayuz_yama.py — kuran_okuma.html'e P2 bağlarını ekler (idempotent).

Eklenenler (v1):
  1. ▶Oku audio: everyayah CDN (varsayılan kārî: Alafasy_128kbps).
     Ayet değişince durur; hata durumunda buton eski hâline döner.
  2. Allah-ekseni rozeti: bulgu_gradyan_cetveli.json'daki 40 ölçüm,
     yan paneldeki varlık satırlarına ve tanım-kartı modalına rozet olarak işlenir.
     Renk: yakın+Bonferroni yeşil, uzak+Bonferroni turuncu, nominal soluk, nötr gri.

Gövdeye (DATA/render) dokunulmaz; yama </body> öncesine tek <script> bloğu
olarak eklenir ve mevcut render/openCard sarmalanır. Tekrar çalıştırılırsa
eski yama bloğu değiştirilir (marker: ARAYUZ-YAMA).

Kullanım: python betikler/arayuz_yama.py  (depo kökünden)
"""
import json, re, sys, os

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(KOK, 'ciktilar', 'kuran_okuma.html')
GRADYAN_BULGU = os.path.join(KOK, 'bulgular', 'bulgu_gradyan_cetveli.json')
MARKER_BAS = '<!-- ARAYUZ-YAMA v1 BAS -->'
MARKER_SON = '<!-- ARAYUZ-YAMA v1 SON -->'

def gradyan_verisi():
    g = json.load(open(GRADYAN_BULGU, encoding='utf-8'))
    cikti = {}
    for o in g['tum_olcumler']:
        cikti[o['ad']] = {
            'medyan': o['allah_medyan'], 'p': o['p'], 'yon': o['yon'],
            'anlamli': bool(o.get('anlamli')), 'bonferroni': bool(o.get('bonferroni')),
            'gecis': o['gecis']
        }
    return cikti

def yama_blogu():
    G = json.dumps(gradyan_verisi(), ensure_ascii=False)
    return MARKER_BAS + """
<style>
.rozet{display:inline-flex;align-items:center;gap:4px;font-size:10.5px;font-weight:600;
  padding:1px 7px;border-radius:10px;margin-left:6px;white-space:nowrap;cursor:default}
.rozet.yakin{background:#e1f0eb;color:#0f6e56}
.rozet.uzak{background:#fdeee0;color:#b05c1a}
.rozet.nominal{opacity:.65}
.rozet.notr{background:#f0ede6;color:#8a8172}
</style>
<script>
/* ---- 1) AUDIO: everyayah CDN ---- */
(function(){
  var KARI='Alafasy_128kbps';
  var pb=document.getElementById('playBtn'); if(!pb) return;
  var audio=null;
  function sifirla(){ pb.classList.remove('playing'); pb.textContent='\\u25b6 Oku'; }
  function dur(){ if(audio){audio.pause(); audio=null;} sifirla(); }
  function pad3(n){ return String(n).padStart(3,'0'); }
  pb.onclick=function(){
    if(audio){ dur(); return; }
    var url='https://everyayah.com/data/'+KARI+'/'+pad3(cur.s)+pad3(cur.a)+'.mp3';
    audio=new Audio(url);
    pb.classList.add('playing'); pb.textContent='\\u23f8 Duraklat';
    audio.onended=dur;
    audio.onerror=function(){ dur(); pb.textContent='\\u26a0 ses yok'; setTimeout(sifirla,1600); };
    audio.play().catch(function(){ dur(); });
  };
  /* ayet değişince sesi durdur */
  if(typeof window.render==='function'){
    var _r=window.render;
    window.render=function(){ dur(); _r.apply(this,arguments); };
  }
})();

/* ---- 2) ALLAH-EKSENİ ROZETİ (bulgu_gradyan_cetveli.json) ---- */
var GRADYAN=""" + G + """;
(function(){
  var KOPRU={'merhamet':'rahmet','sab\\u0131r':'sabr','\\u015f\\u00fck\\u00fcr':'\\u015f\\u00fckr',
    'tevbe':'t\\u00f6vbe','adalet':'adl','k\\u00fcf\\u00fcr':'k\\u00fcfr'};
  function bul(ad){
    if(GRADYAN[ad]) return GRADYAN[ad];
    var parcalar=String(ad).split('/');
    for(var i=0;i<parcalar.length;i++){
      var p=parcalar[i].trim();
      if(GRADYAN[p]) return GRADYAN[p];
      if(KOPRU[p] && GRADYAN[KOPRU[p]]) return GRADYAN[KOPRU[p]];
    }
    return null;
  }
  function rozetHTML(g){
    var sinif = !g.anlamli ? 'notr' : (g.yon==='yakin'?'yakin':'uzak') + (g.bonferroni?'':' nominal');
    var ok = g.yon==='yakin' ? '\\u2192A' : 'A\\u2192';
    var etiket = !g.anlamli ? 'n\\u00f6tr' : ok+' '+g.medyan;
    var baslik = 'Allah-ekseni: medyan '+g.medyan+' kelime \\u00b7 p='+g.p+
      ' \\u00b7 n='+g.gecis+(g.bonferroni?' \\u00b7 Bonferroni-sa\\u011flam':(g.anlamli?' \\u00b7 nominal p<0.05':' \\u00b7 anlams\\u0131z'));
    return '<span class="rozet '+sinif+'" title="'+baslik+'">'+etiket+'</span>';
  }
  function satirlaraEkle(){
    document.querySelectorAll('#varliklar .varlik').forEach(function(row){
      if(row.querySelector('.rozet')) return;
      var adEl=row.querySelector('.v-ad'); if(!adEl) return;
      var g=bul(adEl.textContent.trim()); if(!g) return;
      adEl.insertAdjacentHTML('beforeend', rozetHTML(g));
    });
  }
  if(typeof window.render==='function'){
    var _r2=window.render;
    window.render=function(){ _r2.apply(this,arguments); satirlaraEkle(); };
  }
  /* modal: tanım-kartına hücre olarak ekle */
  if(typeof window.openCard==='function'){
    var _oc=window.openCard;
    window.openCard=function(){
      _oc.apply(this,arguments);
      var adEl=document.getElementById('mAd'); var grid=document.getElementById('mGrid');
      if(!adEl||!grid) return;
      if(grid.querySelector('.rozet-mcell')) return;
      var g=bul(adEl.textContent.trim()); if(!g) return;
      var deger = (g.anlamli? (g.yon==='yakin'?'yak\\u0131n':'uzak') : 'n\\u00f6tr')+
        ' \\u00b7 medyan '+g.medyan+' kelime \\u00b7 p='+g.p+(g.bonferroni?' \\u2713B':'');
      grid.insertAdjacentHTML('beforeend',
        '<div class="mcell rozet-mcell"><div class="mk">Allah-ekseni</div><div class="mv">'+deger+'</div></div>');
    };
  }
  satirlaraEkle();
})();
</script>
""" + MARKER_SON

def uygula():
    h = open(HTML, encoding='utf-8').read()
    blok = yama_blogu()
    if MARKER_BAS in h:
        h = re.sub(re.escape(MARKER_BAS)+r'.*?'+re.escape(MARKER_SON), lambda _m: blok, h, flags=re.S)
        durum = 'değiştirildi'
    else:
        i = h.rfind('</body>')
        if i < 0: sys.exit('HATA: </body> bulunamadı')
        h = h[:i] + blok + '\n' + h[i:]
        durum = 'eklendi'
    open(HTML, 'w', encoding='utf-8').write(h)
    print('yama %s — %s (%.2f MB)' % (durum, HTML, len(h)/1e6))
    print('gradyan girdisi: %d kavram' % len(gradyan_verisi()))

if __name__ == '__main__':
    uygula()
