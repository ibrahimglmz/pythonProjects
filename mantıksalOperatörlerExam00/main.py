sayiInput = int(input("Sayi Giriniz : "))
if sayiInput <= 100:
    print(f"Sayi 0-100 arasındadır " + format(sayiInput))
if sayiInput >= 0:
    print("pozitif")
if sayiInput < 0:
    print("negatif")



    #2soru
sayiInput2 = int(input("Sayi Giriniz : "))
sayiInput3 = int(input("Sayi Giriniz : "))
sayiInput4 = int(input("Sayi Giriniz : "))


enKucuk = "En Kücük Sayi:"
enBuyuk = "En Büyük Sayi"

result = int(min(sayiInput4 ,sayiInput3 , sayiInput2))
result2 = int(max(sayiInput4 ,sayiInput3 , sayiInput2))
print(f"En kücük sayi:"  + format(result))
print(f"En Buyuk Sayi:"  + format(result2))

kişiAdInput = str(input("Adınız: "))
kiloInput = float(input("Kilonuz: "))
boyInput = int(input("Boynuz :"))

sonuc = (kiloInput / (boyInput **2))
if sonuc  < 18.4:
    print("Zayıf")
if 18.5 <= sonuc <= 24.9:
    print("Normal")
if 25 <= sonuc <= 29.9:
    print("Fazla Kilolu")
if 30 <= sonuc <= 34.9:
    print("Obez")
