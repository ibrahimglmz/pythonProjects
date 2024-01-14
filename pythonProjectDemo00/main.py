a = int(input("Sayı giriniz"))
b = int(input("sayi giriniz"))

if a > b:
    print("A büyüktür")
elif b < a :
    print("B büyüktür")
elif a == b :
    print("Sayılar Eşit")

    # 2.soru


vize1 = int(input("vize notunuzu giriniz: "))
vize2 = int(input("vize notunuzu giriniz"))
final = int(input("final notunuzu giriniz: "))
resultt = ((vize1  + vize2 )/2 * 60 /100 )+ (final * 40 / 100)
if resultt > 50:
    print(f"Dönemi Geçti " + format(resultt))
else:
    print(f"Dönemi Geçemediniz " + format(resultt))



 # soru 3



sayi1 = int(input("Sayi Giriniz: "))
if sayi1 & 2:
    print(f"Sayi Cift " + format(sayi1))
else:
    print(f"Sayi Tek" + format(sayi1))



 # 4. soru

sayi1 = int(input("Sayi Giriniz: "))
if sayi1 < 0:
     print(f"sayi negatif " + format(sayi1))
else:
    print(f"sayi positif " + format(sayi1))




parolaInput = str(input("parola giriniz: "))
emailInput = str(input("email giriniz: "))
if parolaInput  == "deneme":
    print( " Email ve Parola Doğru")
elif emailInput == "deneme@gmail.com":
    print("Email ve Parola yanlış")

