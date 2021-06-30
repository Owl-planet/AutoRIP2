from Lib import Connect
from Configs import Configuration
try:
    import sys
except:
    print("Bilinmedik bir hata ile karşılaştık :/")

Connect.InformationsThenSetup() # Bağlantı için bilgi alır ve sonra bağlanır.
Configs.RipVersion2() # Gerekli yapılandırma komutlarını çalıştırır.

# Tam olarak bitmedi...