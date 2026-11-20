KQ = ['bi', 'e', 'ellezîne', 'hu', 'hum', 'ke', 'kum', 'li', 'lâ', 'min', 'nâ', 've', 'î']
_EK = "çakışma değil (edat / zamir karşılığı — Türkçe ek, fiil yönetimi ve çekimle açılır)"
KM = {
 "'nahşuru' / 'yuhşerû' / 'yuhşerûn'": "çakışma değil ('topla-' etken / 'toplan-' edilgen çatı)",
 "'ted'ûn' / 'ted'ûne' / 'yed'ûne'": "çakışma — tam okuma sonu ('çağır-' / 'dua et-' bağlam karşılığı)",
 "'eqûlu' / 'neqûlu' / 'qul' / 'qâle' / 'qâlû' / 'yeqûlu' / 'yeqûlû' / 'yeqûlûn'": "çakışma değil ('de-' / 'söyle-' — bağlam)",
 "''ind' / ''inde'": "çakışma değil (ad 'ind' — bulunma eki ve iyelik çekimiyle açılır)",
 "'leyse'": "çakışma — tam okuma sonu ('yok' / 'değil' bağlam karşılığı)",
}
for _q in KQ: KM["'%s'" % _q] = _EK
