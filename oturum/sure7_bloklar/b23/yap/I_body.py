_OL = [l.replace('**', '') for l in open('/home/claude/b23/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b23/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))
_AK2 = _esc(re.search(r'aktör: adsız `racül` 3\. sırada', _OL[1]).group(0))
_AK3 = _esc(re.search(r'aktör: adsız `karye` 10\. sırada', _OL[2]).group(0))
_AK4 = _esc(re.search(r'aktör: adsız `imrae` 4\. sırada', _OL[3]).group(0))
for _k, _v in (('_AK1', _AK1), ('_AK2', _AK2), ('_AK3', _AK3), ('_AK4', _AK4)): _MB = _MB.replace('" + %s + "' % _k, _v)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 79), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 506",
 "geriye dönük koşu (sûre 7 bölüm 7 kapanışı, komut 'python3 sunum/geriye_donuk.py b20k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 80 84 23'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:80 'min ehadin mine'l-'âlemîn' (10-13. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (hiç kimse — olumsuz sayı) (yamalar/esma_el_7_80_84.txt); 7:81, 7:82, 7:83 ve 7:84 esmâ yok; lafız yok; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 80 84 23'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 7:80 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı; muhur_el hayır): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in range(80, 85)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 80 84 23'): KALAN_P",
 "ölçüm aktör: 7:80 adlı لُوط (1. kelime, rol meful); 7:81 adsız racül (3. kelime); 7:82 adsız karye (10. kelime); 7:83 adsız imrae (4. kelime); 7:84 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:80 soru — INTG 1 'e-te'tûne' (5.), NEG 1 'mâ' (7.); 7:81 haber — EMPH 1 'le-te'tûne' (2.); "
 "7:82 emir — IMPV 1 'exricûhum' (8.), NEG 1 've mâ' (1.), RES 1 'illâ' (5.); 7:83 haber — kip yok; 7:84 emir — IMPV 1 'fe'nzur' (4.)",
 "morph T ('iz' 7:80 2.), RET ('bel' 7:81 8.), SUB ('en' 7:82 6.), EXP ('illâ' 7:83 3.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:80, 7:81, 7:82, 7:83 ve 7:84 yıldız yok",
 "fâsıla: 7:79 ن → 7:80 ن (" + _F[0] + ") → 7:81 ن (" + _F[1] + ") → 7:82 ن (" + _F[2] + ") → 7:83 ن (" + _F[3] + ") → 7:84 ن (" + _F[4] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:80 27:54, 29:28 (emsal olarak basıldı); 7:81 27:55 (emsal olarak basıldı); 7:82 27:56, 29:24, 29:29 (emsal olarak basıldı); "
 "7:83 27:57, 29:32, 29:33 (emsal olarak basıldı); 7:84 27:69 (basılmış)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:82 'illâ en qâle' süzgeç GEÇMEZ; 7:84 'nazara keyfe kâne 'âqibe' süzgeç GEÇER; 7:80, 7:81 ve 7:83 nakarat3 kalıbı yok; sûre içi eşler — 7:5 (basılmış) ve basılmamış eşler",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:80 adlı 'lûtan' (1.); 3MS ('qâle' ve ek 'qavmihî' — gönderge 'lûtan'; 'sebeqakum' — söz içi, fiil uyumu, fail 11. kelime), söz içi muhatap 2MP ('te'tûne'; ek 'sebeqakum'), 3FS eki ('bihâ' — gönderge 'l-fâhişete' 6. kelime); "
 "7:81 adsız 'r-ricâle' (3.); söz içi muhatap 2MP ('te'tûne'; zamir 'entum'; ek 'innekum'); "
 "7:82 adsız 'qaryetikum' (10.); 3MS ('kâne' — fiil uyumu, fail 6. kelime; ek 'qavmihî' — gönderge 7:80 1. kelime), 3MP ('qâlû' — gönderge 'qavmihî' 4. kelime; 'yetetahharûn' — söz içi, gönderge 'unâsun' 12. kelime; ekler 'exricûhum', 'innehum' — söz içi, gönderge 7:80 1. kelime), söz içi muhatap 2MP ('exricû'; ek 'qaryetikum'); "
 "7:83 adsız 'mra'etehû' (4.); konuşan 1P ('enceynâhu'), 3MS eki ('enceynâhu', 'ehlehû', 'mra'etehû' — gönderge 7:80 1. kelime), 3FS ('kânet' — gönderge 'mra'etehû' 4. kelime); "
 "7:84 konuşan 1P ('emtarnâ'), 3MP eki (''aleyhim' — gönderge 7:80 4. kelime), muhatap 2MS ('nzur'), 3MS ('kâne' — fiil uyumu, fail 7. kelime)",
 "7:80-84 gönderge zinciri: 7:80 'qâle' göndergesi 'lûtan' (1. kelime); 7:81 söz 7:80'den sürüyor; 7:82 'qâlû' göndergesi kavmi ('qavmihî' 4. kelime); 7:83 'enceynâhu' göndergesi 7:80 1. kelimedeki Lût; 7:84 ''aleyhim' göndergesi 7:80 4. kelimedeki kavmi (okuma)",
 "edilgen: 7:80, 7:81, 7:82, 7:83 ve 7:84 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:80 söz içi 5-13. kelime ('qâle' 3. kelime ardından; ayet sonunda kapanmıyor); 7:81 söz sürüyor (7:80 5. kelimeden, 1-11. kelime; 11. kelimede kapanır); "
 "7:82 söz içi 8-13. kelime ('qâlû' 7. kelime ardından); 7:83 ve 7:84 söz yok; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 80 84 23' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 7:80 've lûtan' (1.) CONJ; 7:82 've mâ' (1.) REM; 7:83 'fe-enceynâhu' (1.) REM, 've ehlehû' (2.) CONJ; 7:84 've emtarnâ' (1.) CONJ, 'fe'nzur' (4.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:82 ◈B أنس ('unâsun' 12. kelime — B1); 7:80, 7:81, 7:83 ve 7:84 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 80 84 23'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:80 (27:54, 29:28), 7:81 (27:55, 29:28, 29:29), 7:82 (27:56, 29:24, 29:29), 7:83 (27:57, 29:32, 29:33); D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:84 مطر ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:80 söz açılır, şahıs geçişi 1 → 3, edim geçişi nida → soru; 7:81 söz kapanır, şahıs geçişi 3 → 2, edim geçişi soru → haber; 7:82 söz açılır / kapanır, şahıs geçişi 2 → 3, edim geçişi haber → emir; "
 "7:83 şahıs geçişi yok, edim geçişi emir → haber; 7:84 bölüm kapanışı, şahıs sayısında beraberlik (1P 2 · 3. şahıs 2 — ölçüm baskın 1), şahıs geçişi 3 → 1, edim geçişi haber → emir; ölçüm iltifât 7:80-84 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:80 've lûtan iz qâle' — bağlaç, özel ad ve zaman zarfı ile mazi (morph CONJ + PN + T + PERF); 7:81 'innekum le-te'tûne'r-ricâle' — tekit edatı, lâm ile muzâri ve belirli nesne (morph ACC + EMPH + IMPF + DET + N); "
 "7:83 'fe-enceynâhu ve ehlehû' — istînâf, mazi ve bağlaçla nesne (morph REM + PERF + CONJ + N)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:80 5-6. kelime — 27:54 ile harekesiz eş (sayım: 'say 7:80 5-6'); 7:80 7-13. kelime — 29:28 ile harekesiz eş (sayım: 'say 7:80 7-13'); "
 "7:81 3-7. kelime — 27:55 ile harekesiz eş (sayım: 'say 7:81 3-7'); 7:82 2-5. kelime — 27:56, 29:24 ve 29:29 ile harekesiz eş (sayım: 'say 7:82 2-5'); 7:83 3-7. kelime — 29:32 ile harekesiz eş (sayım: 'say 7:83 3-7'); 7:84 kök مطر ikilemesi; geniş eşli sayımlar: 'say 7:80 1-6', 'say 7:80 7-13', 'say 7:80 6-13', 'say 7:82 9-13'",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 23'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'iz qâle li-qavmihî' 7:80 'hani kavmine demişti' / 27:54 'kavmine demişti' (emsal metninde) — çakışma — tam okuma sonu ('hani' — emsalde 'iz' karşılıksız — emsaller arası: 27:54 'kavmine demişti' / 29:28 'Kavmine şöyle demişti'); "
 "'iz qâle li-qavmihî' 7:80 'hani kavmine demişti' / 29:28 'Kavmine şöyle demişti' (emsal metninde) — çakışma — tam okuma sonu (daraltılmış kalıp — araç 29:28 bag kalıplarını kesmede bölüyor — 'hani' / 'şöyle': 'iz' karşılığı ve söz açılışı); "
 "'e-te'tûne'l-fâhişete' 7:80 'hayâsızlığı mı yapıyorsunuz' / 27:54 'bu hayâsızlığı mı yapıyorsunuz' (emsal metninde) — çakışma — tam okuma sonu ('bu' emsalde fazla); "
 "'mâ sebeqakum bihâ min ehadin mine'l-'âlemîn' 7:80 'Âlemlerden hiç kimsenin sizden önce yapmadığı' / 29:28 'âlemlerden hiç kimsenin sizden önce yapmadığı' (emsal metninde) — çakışma değil; "
 "'r-ricâle şehveten min dûni'n-nisâ'i' 7:81 'kadınları bırakıp şehvetle erkeklere' / 27:55 'kadınları bırakıp şehvetle erkeklere' (emsal metninde) — çakışma değil ('say 7:81 1-7' korpusta 1, 'dizi 7 81 1 7' 27:55 ile eş — soru 'e' önek farkı); 'innekum' 7:81 'Gerçekten siz' / 27:55 'Siz' (emsal metninde) — çakışma — tam okuma sonu ('Gerçekten' — emsalde soru); 'innekum' 7:81 'Gerçekten siz' / 29:28 'Siz gerçekten' (emsal metninde) — çakışma — tam okuma sonu (söz dizimi); 'le-te'tûne'r-ricâle' 7:81 'erkeklere yöneliyorsunuz' / 29:29 'erkeklere yönelip' (emsal metninde) — çakışma — tam okuma sonu (çekim — emsalde ulaç); 'le-te'tûne' 7:81 'yöneliyorsunuz' / 29:29 'yönelip' (emsal metninde) — çakışma — tam okuma sonu (çekim — emsalde ulaç); "
 "'kâne cevâbe qavmihî illâ' 7:82 'Kavminin cevabı ancak şu oldu' / 27:56 'Kavminin cevabı ancak şu olmuştu' (emsal metninde) — çakışma — tam okuma sonu ('-du' / '-muştu' — kip; 'say 7:82 1-5' korpusta 1, 'dizi 7 82 1 7' 27:56, 29:24 ve 29:29 ile eş — önek farkı 've' / 'fe'); 'en qâlû' 7:82 'dediler' / 29:24 'demekten' (emsal metninde) — çakışma — tam okuma sonu (masdar 'en' — emsalde isim-fiil); 'en qâlû' 7:82 'dediler' / 29:29 'demekten' (emsal metninde) — çakışma — tam okuma sonu (masdar 'en' — emsalde isim-fiil); "
 "'cevâbe qavmihî' 7:82 'Kavminin cevabı' / 29:24 'Kavminin cevabı' (emsal metninde) — çakışma değil; "
 "'cevâbe qavmihî' 7:82 'Kavminin cevabı' / 29:29 'Kavminin cevabı' (emsal metninde) — çakışma değil; "
 "'innehum unâsun yetetahharûn' 7:82 'çünkü onlar temizlenmeye çalışan insanlardır' / 27:56 'onlar temiz kalmak isteyen kimselermiş' (emsal metninde) — çakışma — tam okuma sonu ('temizlenmeye çalışan' / 'temiz kalmak isteyen' — tetahhar karşılığı; 'insan' / 'kimse' — unâs karşılığı); "
 "'fe-enceynâhu ve ehlehû' 7:83 'Bunun üzerine onu ve ailesini kurtardık' / 27:57 'Onu ve ailesini kurtardık' (emsal metninde) — çakışma — tam okuma sonu ('Bunun üzerine' — emsalde 'fe' karşılıksız); "
 "'ille'mra'etehû' 7:83 'karısı hariç' / 27:57 'karısı hariç' (emsal metninde) — çakışma değil; "
 "'ille'mra'etehû' 7:83 'karısı hariç' / 29:32 'karısı hariç' (emsal metninde) — çakışma değil; "
 "'kânet mine'l-ğâbirîn' 7:83 'o geride kalanlardandı' / 29:32 'o geride kalanlardan olacak' (emsal metninde) — çakışma — tam okuma sonu (zaman — emsalde 'kânet' gelecek bildiren cümlede); "
 "'kânet mine'l-ğâbirîn' 7:83 'o geride kalanlardandı' / 29:33 'o geride kalanlardan olacak' (emsal metninde) — çakışma — tam okuma sonu (zaman — emsalde 'kânet' gelecek bildiren cümlede); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:80 'qâle' PERF ('iz' ile) — meal 'demişti'; 'te'tûne' IMPF IND ('e' ile) — meal 'yapıyorsunuz'; 'sebeqakum' PERF ('mâ' ile) — meal 'yapmadığı'; "
 "7:81 'te'tûne' IMPF IND ('le' ile) — meal 'yöneliyorsunuz'; 7:82 'kâne' PERF (2. kelime; 'mâ' ile) — meal 'oldu'; 'qâlû' PERF ('en' ile) — meal 'dediler'; 'exricûhum' IMPV — meal 'çıkarın'; 'yetetahharûn' IMPF IND — meal 'çalışan'; "
 "7:83 'enceynâhu' PERF — meal 'kurtardık'; 'kânet' PERF — meal 'kalanlardandı'; 7:84 'emtarnâ' PERF — meal 'yağdırdık'; 'nzur' IMPV — meal 'Bak'; 'kâne' PERF (6. kelime) — meal 'oldu'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 'qâle' PERF 7:80'de miş'li geçmiş ('-mişti') ile; 'te'tûne' IMPF 7:80'de şimdiki zaman ('-ıyorsunuz') ile; 'sebeqakum' PERF 7:80'de sıfat-fiil ('-madığı') ile; "
 "'te'tûne' IMPF 7:81'de şimdiki zaman ('-iyorsunuz') ile; 'yetetahharûn' IMPF 7:82'de sıfat-fiil ('-an') ile; 'kânet' PERF 7:83'te ek fiil ('-dı') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'e' (INTG: 'mı' / 'mu') — çakışma değil (ünlü uyumu); 'inne' (ACC: 'Gerçekten' / 'çünkü' / 'gerçekten') — çakışma değil (tekit / gerekçe); 'iz' (T: 'hani' / 'zamanı') — çakışma değil (anlatı açılışı / 'hatırla-' nesnesi); 'le' (EMPH: karşılıksız / 'andolsun') — çakışma değil ('inne' ile pekiştirmede karşılıksız / yemin lâmı); 'mâ' (NEG: 'ancak' / olumsuzluk eki / 'yok') — çakışma değil ('illâ' ile hasr / fiil olumsuzluğu / varlık olumsuzluğu); 've' (CONJ: 'da' / 've' / karşılıksız) — çakışma değil (özel ada atıfta 'da' / atıf / cümle başı); 'bi' (karşılıksız / '-la' / '-le' / belirtme eki / yönelme eki) — çakışma değil (fiil yönetimi); 'hum' ('onlar' / 'onları' / 'onlardan' / iyelik eki) — çakışma değil (çekim ve tamlama); 'hâ' (karşılıksız / 'ona' / 'onu' / 'onun') — çakışma değil (hayâsızlığa dönen zamir, çekim); 'hû' (iyelik eki / 'O'ndan') — çakışma değil (tamlama, çekim); 'kum' ('siz' / 'sizden' / 'size' / 'sizi' / 'sizin' / iyelik eki) — çakışma değil (çekim ve tamlama); 'min' (ayrılma eki / karşılıksız) — çakışma değil (ayrılma / zâid 'min' ve 'min dûni' kalıbı)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 80 84 23'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:80, 7:81, 7:82, 7:83 ve 7:84 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:81 ('r-ricâle' / 'n-nisâ'i'); 7:80, 7:82, 7:83 ve 7:84 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök أتي 7:80 ('te'tûne') ve 7:81 ('te'tûne') ile bölüm içi; kök قول 7:80 ('qâle') ve 7:82 ('qâlû') ile bölüm içi; kök قوم 7:80 ('qavmihî'), 7:81 ('qavmun') ve 7:82 ('qavmihî') ile bölüm içi; kök كون 7:82 ('kâne'), 7:83 ('kânet') ve 7:84 ('kâne') ile bölüm içi; bölümün önceki bloklarıyla ortak kökler: أتي (7:77 / 7:80, 7:81), علم (7:75 / 7:80), قول (7:73, 7:75, 7:76, 7:77, 7:79 / 7:80, 7:82), قوم (7:73, 7:75, 7:79 / 7:80, 7:81, 7:82), كون (7:77 / 7:82, 7:83, 7:84); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 8-3 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 21, 22 ve 23; bölüm kapanışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b23/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 80 84 23'; lem_bozuk.py 23 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 80 84 → AYN_SONUC; sunum/bolum4_kurallar.py 80 84 23 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 80 84 23 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 44)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 23 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('lût', 'iz', 'bel', 'exrece', 'qâle', 'qavm', 'etâ', 'fâhişe', 'mâ', 'sebeqa', 'min', 'ehad', ''âlem', 'inne', 'ricâl', 'şehve', 'dûn', 'nisâ'', 'kâne', 'cevâb', 'illâ', 'en', 'qarye', 'insân', 'tetahhar' (morph LEM ham biçim), 'encâ', 'ehl', 'imrae', 'ğâbir', 'nazara', 'keyfe', ''âqibe'); joker '_' dizi lemma dizisinde boş öğe olan zamir ve önek lemmalı kelimelerde ('bihâ' 7:80 9.); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]
