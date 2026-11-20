KQ = ["'indî mâ testa'cilûne bih", "'alâ", 'bi', 'ellezîne', 'enne', 'hu', 'inne', 'kum', 'min', 'mâ', 've', 'î']
_EK = "çakışma değil (edat / zamir karşılığı — Türkçe ek, fiil yönetimi ve çekimle açılır)"
KM = {
 "''indî mâ testa'cilûne bih'": "çakışma değil (6:57 / 6:58 'Acele istediğiniz şey yanımda' — eş karşılık)",
 "'yu'minû' / 'yu'minûn' / 'yu'minûne' / 'âmene'": "çakışma — tam okuma sonu ('inan-' / 'iman et-' bağlam karşılığı)",
 "'ba'd'": "çakışma değil ('ard' / 'art' — ses uyumu yazım farkı)",
 "'haqq'": "çakışma — tam okuma sonu ('hak' / 'gerçek' — bağlam karşılığı)",
 "'xayr'": "çakışma değil (isim 'hayır' / üstünlük 'daha hayırlı', 'en hayırlı' — morph ad, bağlam)",
 "'ted'ûn' / 'ted'ûne' / 'yed'ûne'": "çakışma — tam okuma sonu ('çağır-' / 'dua et-' bağlam karşılığı)",
 "'dûn'": "çakışma — tam okuma sonu ('başka' / 'bırakıp' bağlam karşılığı)",
 "'dalaltu' / 'dalle'": "çakışma — tam okuma sonu ('kaybol-' / 'sap-' bağlam karşılığı)",
 "''amile' / 'ya'melûn'": "çakışma — tam okuma sonu ('işle-' / 'yap-' bağlam karşılığı)",
 "''ind' / ''inde'": "çakışma değil (ad 'ind' — bulunma eki ve iyelik çekimiyle açılır)",
 "'eqûlu' / 'neqûlu' / 'qul' / 'qâle' / 'qâlû' / 'yeqûlu' / 'yeqûlû' / 'yeqûlûn'": "çakışma değil ('de-' / 'söyle-' — bağlam)",
 "'qadâ' / 'qudiye'": "çakışma — tam okuma sonu ('takdir et-' / 'bitiril-' bağlam karşılığı)",
 "'kezzebe' / 'kezzebtum' / 'kezzebû' / 'kuzzibet' / 'kuzzibû' / 'nukezzibe' / 'yukezzibûne'": "çakışma değil ('yalanla-' etken / 'yalanlan-' edilgen çatı)",
 "'nuhîtu' / 'nuhû' / 'yenhevne'": "çakışma — tam okuma sonu ('yasaklan-' / 'men edil-' edilgen / 'alıkoy-' etken — men etme)",
}
for _q in KQ[1:]: KM["'%s'" % _q] = _EK
