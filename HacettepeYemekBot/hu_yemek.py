import requests
import xml.etree.ElementTree as ET
from datetime import date

def xml_verisi_cek():
    url = 'https://sksdb.hacettepe.edu.tr/YemekListesi.xml'  # Web sitesinin URL'si
    response = requests.get(url)

    if response.status_code == 200:
        xml_content = response.content
        return xml_content
    else:
        print('Hata:', response.status_code)
        return None

def bugunun_yemekleri():
    xml_content = xml_verisi_cek()

    if xml_content:
        root = ET.fromstring(xml_content)

        today = date.today()
        day = today.day if today.day >= 10 else str(today.day).zfill(1)
        today = '{}.{:02d}.{}'.format(day, today.month, today.year)

        # Bugünün yemeklerini bulma
        for gun in root.iter('gun'):
            tarih = gun.find('tarih').text.strip().split()[0]

            if tarih == today:
                yemekler = gun.find('yemekler')

                bugunun_yemekleri = []
                for yemek in yemekler.iter('yemek'):
                    bugunun_yemekleri.append(yemek.text.strip())

                return bugunun_yemekleri
            
    return []

bugunun_yemekler = bugunun_yemekleri()
if bugunun_yemekler:
    print("Bugünün yemekleri:")
    for yemek in bugunun_yemekler:
        print(yemek)
else:
    print("Bugün için yemek bilgisi bulunamadı.")