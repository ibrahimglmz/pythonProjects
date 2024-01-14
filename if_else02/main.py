from datetime import datetime

tarih_str = input("Lütfen tarihi 'YYYY-MM-DD' formatında girin: ")

try:
    tarih = datetime.strptime(tarih_str, '%Y-%m-%d')
    print("Girilen tarih:", tarih)
except ValueError:
    print("Geçersiz tarih formatı. 'YYYY-MM-DD' formatında giriniz.")
