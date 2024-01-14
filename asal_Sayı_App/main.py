sayi = int(input("Sayı: "))
asalSayi = True

if sayi == 1:
    print("1 sayısı asal degildir.")

for i in range(2,sayi):
    if sayi % i == 0:
        asalSayi = False
        break

if asalSayi:
    print("sayı asaldır")
else:
    print("Sayı Asal Degildir")