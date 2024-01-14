kelimeInput = str(input("Kelime Yazınız: "))
kacKereYazdır = int(input("Kelime Kac kere yazdırılsın: "))


def kelimeFunc(kelimeInput,kacKereYazdır):
        while kacKereYazdır > 0:

            print(f" {kelimeInput} {kacKereYazdır}")
            kacKereYazdır -= 1






kelimeFunc()




