#kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndür ve yazdı r
def tam_bolenleri_bul(sayi):
    tam_bolenler = []
    for i in range(1, sayi + 1):
        if sayi % i == 0:
            tam_bolenler.append(i)
    return tam_bolenler

sayiInputAl = int(input("Sayı Giriniz: "))
tam_bolenler_listesi = tam_bolenleri_bul(sayiInputAl)

print(f"{sayiInputAl} sayısının tam bölenleri: {tam_bolenler_listesi}")
