/* kuran_ses.js — KÂRÎSİZ TİLÂVET İSKELETİ (tarayıcı sentezi)
   ============================================================
   tilavet_sentez.py'nin birebir çevirisi. Aynı DSP, aynı çıktı.
     SÜRE  ← tecvîd (metnin)
     SESLİ ← formant fiziği (metnin belirlediği kimlik)
     PERDE ← DÜZ 110 Hz — KEYFÎ. Metin perde buyurmaz; makam kārînindir.
   Hiçbir insan kaydından öğrenilmedi. Robotik olması dürüstlüğün kendisi.
*/
(function(){
'use strict';
var SR=22050, F0=110, HAREKE=0.20, UNS=0.070;
/* TEMPO — ÖLÇEK İCRACININ, METNİN DEĞİL.
   Ölçüldü: 3 kārî × 7 sûre → 0.197–0.382 sn/hareke.
   Tek kārî içinde sûreye göre 1.7 kat, aynı sûrede kārîler arası 1.7 kat.
   Metin ORAN buyurur (2/4/6 hareke), mutlak değer değil. Bu yüzden serbest. */
function tempoAyarla(sn){ HAREKE = Math.max(0.10, Math.min(0.60, sn)); }

/* ---------- DSP ---------- */
function rez(x,f,bw){
  var r=Math.exp(-Math.PI*bw/SR), th=2*Math.PI*f/SR;
  var a1=-2*r*Math.cos(th), a2=r*r, g=1+a1+a2;
  var y=new Float32Array(x.length), y1=0, y2=0;
  for(var i=0;i<x.length;i++){ var v=g*x[i]-a1*y1-a2*y2; y[i]=v; y2=y1; y1=v; }
  return y;
}
function glottal(n){
  var y=new Float32Array(n), s=0;
  for(var i=0;i<n;i++){ var ph=(F0*i/SR)%1;
    y[i]= ph<0.4 ? 0.5*(1-Math.cos(Math.PI*ph/0.4)) : (ph<0.6 ? Math.cos(Math.PI*(ph-0.4)/0.4) : 0);
    s+=y[i]; }
  var m=s/n; for(i=0;i<n;i++) y[i]-=m;
  return y;
}
function kaskad(src,F,BW){ var y=src; for(var i=0;i<F.length;i++) y=rez(y,F[i],BW[i]); return y; }
function zarf(y,ar,de){
  ar=ar||0.012; de=de||0.012;
  var n=y.length, a=Math.floor(ar*SR), d=Math.floor(de*SR), i;
  for(i=0;i<a&&i<n;i++) y[i]*=i/a;
  for(i=0;i<d&&i<n;i++) y[n-1-i]*=i/d;
  return y;
}
function randn(){                       // Box-Muller — numpy.randn ile aynı dağılım
  var u=0,v=0;
  while(u===0) u=Math.random();
  while(v===0) v=Math.random();
  return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);
}
function gurultu(n,merkez,bw,kaz){
  var x=new Float32Array(n);
  for(var i=0;i<n;i++) x[i]=randn();
  var y=rez(x,merkez,bw);
  for(i=0;i<n;i++) y[i]*=kaz;
  return zarf(y,0.005,0.005);
}

/* ---------- sesliler ---------- */
var SESLI={
  a:[[700,1200,2500],[90,100,140]], i:[[300,2300,3000],[70,110,150]], u:[[350,800,2400],[70,100,140]],
  A:[[750,1150,2500],[90,100,140]], I:[[280,2400,3050],[70,110,150]], U:[[320,750,2400],[70,100,140]]
};
function sesli(v,sure,emf){
  var d=SESLI[v], F=d[0].slice(), BW=d[1];
  if(emf){ F[1]=Math.max(700,F[1]-350); F[0]=F[0]+60; }   // tefhîm — gerçek fizik
  var n=Math.max(1,Math.round(sure*SR));
  return zarf(kaskad(glottal(n),F,BW));
}
function nazal(sure,F2){
  var n=Math.round(sure*SR), y=kaskad(glottal(n),[250,F2||1700,2600],[80,150,200]);
  for(var i=0;i<n;i++) y[i]*=0.6;
  return zarf(y);
}
function yanal(sure){
  var n=Math.round(sure*SR), y=kaskad(glottal(n),[350,1200,2600],[70,110,150]);
  for(var i=0;i<n;i++) y[i]*=0.8;
  return zarf(y);
}
function carpma(sure){
  var n=Math.round(sure*SR), y=kaskad(glottal(n),[500,1400,2500],[80,120,160]);
  for(var i=0;i<n;i++) y[i]*=(0.5+0.5*Math.sin(2*Math.PI*26*i/SR))*0.85;
  return zarf(y);
}
function bogaz(sure,otumlu){
  var n=Math.round(sure*SR);
  if(otumlu){ var y=kaskad(glottal(n),[700,1100,2400],[110,130,180]);
    for(var i=0;i<n;i++) y[i]*=0.75; return zarf(y); }
  return gurultu(n,1200,700,0.35);
}
function patlama(kapanma,merkez,otumlu){
  var nk=Math.round(kapanma*SR), y0=new Float32Array(nk);
  if(otumlu){ var m=kaskad(glottal(nk),[250],[120]); for(var i=0;i<nk;i++) y0[i]=0.05*m[i]; }
  var nb=Math.round(0.012*SR), b=gurultu(nb,merkez,900,0.9);
  var out=new Float32Array(nk+nb);
  out.set(y0,0); out.set(b,nk);
  return out;
}

/* ---------- ünsüz tablosu ---------- */
var EMFATIK='صضطظ';
var UNSUZ={
 'ء':['p',0.035,700,0],  'ب':['p',0.045,600,1],  'ت':['p',0.045,3200,0],
 'ث':['g',5500,2200,0.22],'ج':['p',0.040,2200,1], 'ح':['b',0],
 'خ':['g',1600,900,0.30], 'د':['p',0.040,2600,1], 'ذ':['g',4800,2000,0.20],
 'ر':['c'],               'ز':['g',5200,1800,0.28],'س':['g',6200,1800,0.35],
 'ش':['g',3300,1400,0.35],'ص':['g',5000,1600,0.35],'ض':['p',0.045,1800,1],
 'ط':['p',0.045,1900,0],  'ظ':['g',4200,1600,0.22],'ع':['b',1],
 'غ':['g',1400,800,0.26], 'ف':['g',7000,2500,0.22],'ق':['p',0.050,1100,0],
 'ك':['p',0.045,2100,0],  'ل':['y'],               'م':['n',1000],
 'ن':['n',1700],          'ه':['g',1000,1600,0.14],'و':['k','U'],
 'ي':['k','I'],           'ٱ':['0'], 'ا':['0']
};
function unsuzSes(c,emf){
  var d=UNSUZ[c];
  if(!d) return new Float32Array(Math.round(UNS*SR));
  switch(d[0]){
    case 'p': return patlama(d[1],d[2],d[3]);
    case 'g': return gurultu(Math.round(UNS*SR),d[1],d[2],d[3]);
    case 'n': return nazal(UNS,d[1]);
    case 'y': return yanal(UNS);
    case 'c': return carpma(UNS);
    case 'b': return bogaz(UNS,d[1]);
    case 'k': var y=sesli(d[1],UNS); for(var i=0;i<y.length;i++) y[i]*=0.7; return y;
  }
  return new Float32Array(Math.round(UNS*SR));
}

/* ---------- metin çözümleme ---------- */
var FATHA=0x64E,DAMMA=0x64F,KASRA=0x650,SUKUN=0x652,SHADDA=0x651;
var FATHATAN=0x64B,DAMMATAN=0x64C,KASRATAN=0x64D;
var DAGGER=0x670,MADDA=0x653,WASLA=0x671,MAKSURA=0x649;
var TANWIN={}; TANWIN[FATHATAN]='a'; TANWIN[DAMMATAN]='u'; TANWIN[KASRATAN]='i';
var HRK={}; HRK[FATHA]='a'; HRK[DAMMA]='u'; HRK[KASRA]='i';
var HARAKAT=[FATHA,DAMMA,KASRA,SUKUN,SHADDA,FATHATAN,DAMMATAN,KASRATAN];
function isHar(cp){ return HARAKAT.indexOf(cp)>=0; }
function isL(cp){ return (cp>=0x621&&cp<=0x64A&&!isHar(cp))||cp===WASLA||(cp>=0x66E&&cp<=0x6D3); }
function coz(ar){
  var L=[],cur=null,sp=false;
  for(var i=0;i<ar.length;i++){
    var ch=ar[i], cp=ar.charCodeAt(i);
    if(cp===0x20){ sp=true; continue; }
    if(cp===0x6DF||cp===0x6E0){ if(cur) cur.sessiz=true; continue; }
    if((cp>=0x6D6&&cp<=0x6ED)||cp===0x640||cp===0xFEFF||(cp>=0x610&&cp<=0x61A)) continue;
    if(isHar(cp)||cp===DAGGER||cp===MADDA){ if(cur) cur.h.push(cp); continue; }
    if(isL(cp)){ cur={c:ch,h:[],sp:sp,sessiz:false}; L.push(cur); sp=false; }
  }
  return L.filter(function(x){ return !x.sessiz; });
}
function has(h,x){ return h.indexOf(x)>=0; }

/* mukattaa harf isimleri: [ünsüz, sesli, hareke, kapanış] */
var MUK_ISIM={
 'ل':['ل','A',6,'م'], 'م':['م','I',6,'م'], 'ص':['ص','A',6,'د'], 'ر':['ر','A',2,null],
 'ك':['ك','A',6,'ف'], 'ه':['ه','A',2,null], 'ي':['ي','A',2,null], 'ع':['ع','a',6,'ن'],
 'ط':['ط','A',2,null], 'س':['س','I',6,'ن'], 'ح':['ح','A',2,null], 'ق':['ق','A',6,'ف'],
 'ن':['ن','U',6,'ن']
};
var ALEF=['ا','ٱ','آ','أ','إ'];

/* ---------- sentez (Python ile hizalı: _sentez_govde) ---------- */
var ARID_MORA=4;
function uzunluk(L,k){
  if(k+1<L.length){
    var nc=L[k+1].c, nh=L[k+1].h;
    if(['ء','أ','إ','ؤ','ئ'].indexOf(nc)>=0) return 4;
    if(has(nh,SHADDA)||has(nh,SUKUN)) return 6;
  }
  return 2;
}
function safMed(L,k){
  /* SADECE önceki sesliyi uzatan taşıyıcı mı?
     ÖNEMLİ: üst-elif (ٰ) buraya GİRMEZ — o ünsüzün üstünde durur, ünsüzü yutmaz. */
  var ch=L[k].c, h=L[k].h;
  if(ch==='آ') return 'A';
  if(ch==='ا'||ch==='ى'||ch.charCodeAt(0)===MAKSURA){
    if(has(h,MADDA)) return 'A';
    var hrk=false; for(var j=0;j<h.length;j++) if(HRK[h[j]]) hrk=true;
    if(!hrk && k>0 && (has(L[k-1].h,FATHA)||has(L[k-1].h,FATHATAN))) return 'A';
    return null;
  }
  if(ch==='و' && h.length===0 && k>0 && has(L[k-1].h,DAMMA)) return 'U';
  if(ch==='ي' && h.length===0 && k>0 && has(L[k-1].h,KASRA)) return 'I';
  return null;
}
function aridIndeksi(L,muk){
  if(!L.length) return -1;
  var last=L.length-1;
  if(last<muk) return -1;
  if(has(L[last].h,FATHATAN)) return -1;                       // ıvaz
  if(safMed(L,last)||has(L[last].h,DAGGER)) return -1;         // açık
  for(var d=1;d<=2;d++){
    var j=last-d;
    if(j>=muk && j>=0 && (safMed(L,j)||has(L[j].h,DAGGER))) return j;
  }
  return -1;
}
function sentezle(ar,muk){
  muk=muk||0;
  var L=coz(ar), parca=[], seg=[], t=0, li=0;
  var arid=aridIndeksi(L,muk);
  function ekle(y,et,tip){
    if(!y||!y.length) return;
    seg.push({b:t,e:t+y.length/SR,et:et,tip:tip,li:li}); parca.push(y); t+=y.length/SR;
  }
  for(var k=0;k<L.length;k++){
    li=k;
    var ch=L[k].c, h=L[k].h;
    /* --- mukattaa: harf ADIYLA --- */
    if(k<muk){
      if(ch==='ا'){
        ekle(unsuzSes('ء'),'ء','unsuz'); ekle(sesli('a',HAREKE),'a','sesli');
        ekle(unsuzSes('ل'),'ل','unsuz'); ekle(sesli('i',HAREKE),'i','sesli');
        ekle(unsuzSes('ف'),'ف','unsuz');
      } else {
        var ad=MUK_ISIM[ch];
        if(ad){
          var e0=EMFATIK.indexOf(ad[0])>=0;
          ekle(unsuzSes(ad[0],e0),ad[0],'unsuz');
          if(ad[1]) ekle(sesli(ad[1],ad[2]*HAREKE,e0),ad[1]+'('+ad[2]+')','med');
          if(ad[3]) ekle(unsuzSes(ad[3]),ad[3],'unsuz');
        }
      }
      ekle(new Float32Array(Math.round(0.05*SR)),'','bosluk');
      continue;
    }
    var emf = EMFATIK.indexOf(ch)>=0 || (k>0 && EMFATIK.indexOf(L[k-1].c)>=0);
    /* --- 1) saf med taşıyıcısı --- */
    var sm=safMed(L,k);
    if(sm){
      var u=uzunluk(L,k);
      if(arid===k && u<ARID_MORA) u=ARID_MORA;
      if(parca.length){ parca.pop(); var sx=seg.pop(); t=sx.b; }
      li=k;
      ekle(sesli(sm,u*HAREKE,emf),sm+'('+u+')','med');
      continue;
    }
    /* --- sessiz taşıyıcı --- */
    if((ch==='ا'||ch==='ٱ'||ch==='آ') && h.length===0){
      if(k===0) ekle(sesli('i',HAREKE),'i','sesli');   // vasla, söz başında
      continue;
    }
    /* --- 2) ÜNSÜZ --- */
    ekle(unsuzSes(ch,emf),ch,'unsuz');
    if(has(h,SHADDA)) ekle(unsuzSes(ch,emf),ch,'unsuz');
    /* --- 3) ünsüzün seslisi --- */
    if(has(h,DAGGER)){                     // üst-elif: ünsüz KORUNUR + uzun â
      var u2=uzunluk(L,k);
      if(arid===k && u2<ARID_MORA) u2=ARID_MORA;
      ekle(sesli('A',u2*HAREKE,emf),'A('+u2+')','med');
    } else if(has(h,MADDA)){
      ekle(sesli('A',2*HAREKE,emf),'A(2)','med');
    } else {
      var v=null; for(var j2=0;j2<h.length;j2++) if(HRK[h[j2]]) v=HRK[h[j2]];
      if(v) ekle(sesli(v,HAREKE,emf),v,'sesli');
      var tw=null; for(j2=0;j2<h.length;j2++) if(TANWIN[h[j2]]) tw=TANWIN[h[j2]];
      if(tw){ ekle(sesli(tw,HAREKE,emf),tw,'sesli'); ekle(nazal(UNS),'n','unsuz'); }
    }
  }
  var n=0,i2; for(i2=0;i2<parca.length;i2++) n+=parca[i2].length;
  var y=new Float32Array(n), o=0, mx=0;
  for(i2=0;i2<parca.length;i2++){ y.set(parca[i2],o); o+=parca[i2].length; }
  for(i2=0;i2<n;i2++) if(Math.abs(y[i2])>mx) mx=Math.abs(y[i2]);
  if(mx>0) for(i2=0;i2<n;i2++) y[i2]=y[i2]/mx*0.85;
  return {wave:y, seg:seg, sr:SR, sure:n/SR};
}

window.KuranSes={ sentezle:sentezle, sesli:sesli, SR:SR, F0:F0, SESLI:SESLI,
  tempoAyarla:tempoAyarla, tempo:function(){ return HAREKE; } };
})();
