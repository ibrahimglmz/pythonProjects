"""
# gönderilen kelımeyo  bılırtılen kez ekranda gosteren fonksıyonu yazınız
kelimeInput = str(input("Yazınız: "))
kacKere= int(input("Kaç Kere Tekrarlasın: "))

def tekrarla():
    return kelimeInput



for i in range(1,kacKere):
    print(tekrarla())


def parametreleri_listeye_cevir(*args):
    return list(args)


# Kullanıcıdan sınırsız sayıda giriş al
"""
""" def ekleme():
        global bosListe
        while True:
            sayiGiriniz = input("Sayıyı Giriniz (Çıkmak için 'q' tuşuna basın): ")
    
            if sayiGiriniz.lower() == 'q' or 'Q':
                break
    
            bosListe.extend(parametreleri_listeye_cevir(int(sayiGiriniz)))
    
    
    bosListe = []
    ekleme()
    
    print("Oluşturulan Liste:", bosListe)
    
    print(bosListe)



"""
# Gönderilen iki sayı arasında ki tüm asal sayıları bulunuz


sayi1 = int(input("Sayi Giriniz: "))
sayi2 = int(input("Sayi Giriniz: "))
listeler = []


if (sayi1 // 2 == 0 or sayi1 // 3 == 0 ) and (sayi2 // 2 == 0) or (sayi2 // 3 == 0):
    print(sayi2)
    print(sayi1)

else:
    sayi1




sayi1 = int(input("Sayi Giriniz: "))
sayi2 = int(input("Sayi Giriniz: "))

for i in range(sayi1, sayi2):
    sayi1  += 1



