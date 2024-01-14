sayilar = [1, 3, 4, 7, 9, 12, 19, 21]
toplam = 0

for sayi in sayilar:
    toplam += sayi
    print(f"toplam: {format(sayi)}")




for a in sayilar:
    if a % 2 == 1:
        print(a **2)





sehirler = ['Kocaeli','İstanbul','Ankara','izmir','rize']

for i in  sehirler:
    print(f" {i}: {len(i)}")




toplam_fiyat = 0
urunler = [
    {'name': 'Samgung s6', 'price': '3000'},
    {'name': 'Samgung s7', 'price': '4000'},
    {'name': 'Samgung s8', 'price': '5000'},
    {'name': 'Samgung s9', 'price': '6000'},
    {'name': 'Samgung s10', 'price': '7000'},

]
for i in urunler:
    fıyat = int(i['price'])
    toplam_fiyat += fıyat
print(f"Toplam Fiyat: "+format(toplam_fiyat))


for i in urunler:
    fiyat = int(i['price'])
    if fiyat <= 5000:
        print(f"{fiyat}")



