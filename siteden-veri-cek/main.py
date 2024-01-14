import requests
from bs4 import BeautifulSoup


def haberleri_kaydet(url, anahtar_kelimeler, dosya_adı):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        haber_basliklari = soup.find_all('h2')
        haber_icerikleri = soup.find_all('p')

        with open(dosya_adı, 'w', encoding='utf-8') as dosya:
            for baslik, icerik in zip(haber_basliklari, haber_icerikleri):
                baslik_metni = baslik.get_text().strip()
                icerik_metni = icerik.get_text().strip()

                if any(kelime.lower() in baslik_metni.lower() or kelime.lower() in icerik_metni.lower() for kelime in
                       anahtar_kelimeler):
                    dosya.write(f"{baslik_metni}\n{icerik_metni}\n\n")

        print(f"Haberler {dosya_adı} dosyasına kaydedildi.")
    else:
        print(f"Hata: {response.status_code} - Sayfa çekilemedi.")


# Kullanıcıdan URL al
web_sitesi_url = input("Lütfen bir web sitesi URL'si girin: ")

# Kullanıcıdan anahtar kelimeleri al
anahtar_kelimeler_str = input("Lütfen arama yapmak istediğiniz anahtar kelimeleri virgülle ayırarak girin: ")
anahtar_kelimeler = [kelime.strip() for kelime in anahtar_kelimeler_str.split(',')]

# Dosya adını belirle
dosya_adi = 'haber.txt'

# Haberleri kaydet
haberleri_kaydet(web_sitesi_url, anahtar_kelimeler, dosya_adi)
