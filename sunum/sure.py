# sûre parametresi (sûre 5 hazırlığı, 2026-11-15; sûre 6 hazırlığı 2026-11-18; sûre 7 hazırlığı 2026-11-24): sûreye bağlı araçlar S değerini buradan okur.
# SURE / BKOK ortam değişkenleri: önceki sûrenin blok dizinleriyle koşu (mutasyon_sina sûre 5 sınamaları: SURE=5 BKOK=/home/claude/s5/; sûre 6 sınamaları: SURE=6 BKOK=/home/claude/s6/)
import os as _os
S = int(_os.environ.get('SURE', '7'))
BK = _os.environ.get('BKOK', '/home/claude/')
