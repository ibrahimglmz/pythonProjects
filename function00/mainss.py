#gönderilen iki sayı arasında kı tum asal sayıları bulup yazdır

sayıInput1 = int(input("İlk Sayıyı Giriniz: "))
sayıInput2 = int(input("İlk Sayıyı Giriniz: "))
listem = []


print(sayıInput1,sayıInput2)

while sayıInput1 <= sayıInput2:
    listem.append(sayıInput1)
    sayıInput1 += 1
    print(f"Listenin icinde ki sayılar: {listem}")

    for sayi in listem:
       if  sayi % 2 and sayi % 3:
           print(f"Listedeki Asal Sayılar : {sayi}")


