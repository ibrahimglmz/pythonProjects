# SORU ÖDEV
#liste kullan
# fonksiyon kullan
# while veya for kullan

listeler = []
sayi = 0

def tekrarla():
    while sayi == 0:
        parametreInput = int(input("Parametre Giriniz: "))
        listeler.append(parametreInput)
        print(listeler)
        parametreInput2 = int(input("Parametre2 Giriniz: "))
        listeler.append(parametreInput2)
        print(listeler)


tekrarla()