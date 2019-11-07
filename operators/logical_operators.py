a = int(input("Bir sayi girin: "))
print("Sayi 0 100 arasinda mi ",(a>0 and a<100))


b = int(input("Bir sayi girin: "))
print("Sayi pozitif cift sayi mi ", (b>0 and (b%2 == 0)))


email = "iremsendur@gmail.com"
password = "abc895"

e = input("Email adresi girin: ")
p = input("Parola girin: ")
print("Girilen bilgiler dogru mu ", (e == email and p == password))


x, y, z = map(int,input("Uc sayi girin: ").split())
print("En buyuk ",x, " durumu ", (x>y and x>z))
print("En buyuk ",y, " durumu ", (y>x and y>z))
print("En buyuk ",z, " durumu ", (z>x and z>y))


vize1, vize2, final = map(int,input("Iki vize ve final notu giriniz: ").split())
ort = ((vize1+vize2)/2 * 0.6) + (final*0.4)
if((ort >= 50 and final>= 50) or final >= 70):
	print("Sinifi gectiniz.")
else:
	print("Sinifi gecemediniz.")


ad, kilo, boy = input("Ad kilo boy bilgilerinizi giriniz: ").split()
indeks = float(kilo) / float(boy)**2
print(" " ,ad," zayif mi ", (indeks>0 and indeks<18.4))
print(" " ,ad," normal mi ", (indeks>18.5 and indeks<24.9))
print(" ",ad," fazla kilolu mu ", (indeks>25.0 and indeks<29.9))
print(" ",ad," obez mi ", (indeks>30.0 and indeks<34.9))
