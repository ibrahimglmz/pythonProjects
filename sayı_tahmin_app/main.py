# ödev 1-100 arasında rasgele üretilecek bir sayıyı tahmin ettirmr
# random modülünü ögren ve kullan
# kalan can sayısını yazdır
# 100 üzerinden puanlama yapılsın ve her soru 20  puan olsun


import random

hakBilgisi = 5
puan = 0

for  a in range(hakBilgisi):
    kullaniciSayGir = int(input("Sayi Giriniz: "))
    randomNumber = random.randint(0, 1)

    print(f"Girilen Sayi: {kullaniciSayGir}  Tahmin Edilen Sayi: {randomNumber}  Hak Bilgisi: {hakBilgisi}")

    if kullaniciSayGir == randomNumber:
        puan += 20
        print(f" Tebrikler Sayı Tahminin Doğru. Puan: {puan}")

    hakBilgisi -= 1

    if hakBilgisi == 0:
        print("Hakkınız kalmadı. Oyunu kaybettiniz.")
        break
