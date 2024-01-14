kullaniciGiris = str(input("Kullanici Adı veya Hesap Numarası Giriniz: "))
adInput = str(input("Adınızı Yazınız: "))

ibrahimHesap = {
    'ad': 'ibrahim gülmez',
    'hesapNo': '1234',
    'bakiye': 3000,
    'ekHesap': 2000
}

aliHesap = {
    'ad': 'ali gülmez',
    'hesapNo': '987',
    'bakiye': 2000,
    'ekHesap': 1000
}

if kullaniciGiris == ibrahimHesap['ad'] or kullaniciGiris == ibrahimHesap['hesapNo']:
    paraCek = int(input("Ne Kadar Para Cekilecek:"))
    if ibrahimHesap['bakiye'] < paraCek:
        tumKalan = ibrahimHesap['bakiye'] + ibrahimHesap['ekHesap']
        sonKalan = tumKalan - paraCek
        print(f"Kalan Bakiyeniz: {sonKalan}")
    else:
        kalanPara = ibrahimHesap['bakiye'] - paraCek
        print(f"Kalan Bakiyeniz: {kalanPara} \nEk Hesabinizda Kalan Bakiyeniz: {ibrahimHesap['ekHesap']}")
else:
    print(f"Hoş Geldiniz {adInput}")

if kullaniciGiris == aliHesap['ad'] or kullaniciGiris == aliHesap['hesapNo']:
    paraCek = int(input("Ne Kadar Para Cekilecek: "))
    if aliHesap['bakiye'] >= paraCek:
        kalanPara = aliHesap['bakiye'] - paraCek
        print(f"Kalan Bakiyeniz: {kalanPara} \nEk Hesabinizda Kalan Bakiyeniz: {aliHesap['ekHesap']}")
    else:
        tumKalan = aliHesap['bakiye'] + aliHesap['ekHesap']
        sonKalan = tumKalan - paraCek
        print(f"Kalan Bakiyeniz: {sonKalan}")
else:
    print("")
