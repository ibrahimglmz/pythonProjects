kullaniciAdi = str(input("Kullanıcı Adı Giriniz: "))
KullaniciYas = int(input("Yaşınızı giriniz: "))
kullaniciEgitim = str(input("Egtim Durumunuzu Giriniz: "))


ehliyetOnay = "Ehliyet Alabilirsiniz"
ehliyetRed= "Ehliyet Alamadınız"

if KullaniciYas >= 18 or  kullaniciEgitim["Lise","lise","üniversite","Üniversite"]:
    print(f"Sayın {kullaniciAdi},{ehliyetOnay}")
else:
    print(ehliyetRed)




