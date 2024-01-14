vizeNotu = float(input("Vize Notunuzu Giriniz: "))
finalNotu = float(input("Final Notunuzu giriniz: "))

dönemNotu = (vizeNotu * 40 / 100) + (finalNotu * 60 / 100)

if dönemNotu <= 24:
    print("0")
elif 25 <= dönemNotu <= 44:
    print("1")
elif 45 <= dönemNotu <= 54:
    print("2")
elif 55 <= dönemNotu <= 69:
    print("3")
elif 70<= dönemNotu <= 84:
    print("4")
elif 85 <=dönemNotu <= 100:
    print("5")
