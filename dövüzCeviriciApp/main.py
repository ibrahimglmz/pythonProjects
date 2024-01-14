import requests
import json

api_key = "9b718b9e5f169f4e1ce17ac7"
change_doviz = input("Kullanılan Döviz: ")
change_dovizBuyukHarf = change_doviz.upper()
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

alinan_Doviz = input("Alınan Döviz Türü: ")
alinan_Doviz_BuyukHarf = alinan_Doviz.upper()
miktarStr = input("Miktar Giriniz:  ")
miktar = float(miktarStr)

# Making our request
sonuc = requests.get(api_url + change_dovizBuyukHarf)
sonuc_json = json.loads(sonuc.text)

doviz_miktari = (sonuc_json["conversion_rates"][alinan_Doviz_BuyukHarf])
hesaplananDoviz = float(doviz_miktari) * miktar
print(hesaplananDoviz)
