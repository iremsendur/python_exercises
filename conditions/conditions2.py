#Condition statements
a = int(input("Bir sayi girin: "))
if(a>0 and a<=100):
	print("Sayi 0'la 100 arasinda")
else:
	print("Sayi 0'la 100 arasinda degil")

#*****************************************

b = int(input("Bir sayi girin: "))
if(b>0):
	if(b%2 == 0):
		print("Sayi pozitif cift sayi")
	else:
		print("Sayi pozitif tek sayi")
else:
	print("Sayi negatif")

#******************************************

email = "iremsendur@gmail.com"
password = "abc895"

e = input("Email adresi girin: ")
p = input("Parola girin: ")

if(e == email):
	if(p == password):
		print("Giris basarili")
	else:
		print("Hatali parola")
else:
	print("Hatali mail adresi")

#******************************************

x, y, z = map(int,input("Uc sayi girin: ").split())
if(x>y and x>z):
	print("En buyuk sayi: ",x)
elif(y>x and y>z):
	print("En buyuk sayi: ",y)
elif(z>x and z>y):
	print("En buyuk sayi: ",z)

#*******************************************

vize1, vize2, final = map(int,input("Iki vize ve final notu giriniz: ").split())
ort = ((vize1+vize2)/2 * 0.6) + (final*0.4)
if(ort >= 50):
	if(final >= 50):
		print("Sinifi gectiniz")
	else:
		print("Sinifi gecemediniz, finalden en az 50 almalisiniz")
elif(final >=70):
	print("Sinifi gectiniz")
else:
	print("Sinifi gecemediniz")

#*********************************************

ad, kilo, boy = input("Ad kilo boy bilgilerinizi giriniz: ").split()
indeks = float(kilo) / float(boy)**2
if(indeks>=0 and indeks<= 18.4):
	print(" ", ad, " kilo degerlendirmen: zayif")
elif(indeks>18.4 and indeks<=24.9):
	print(" ", ad, " kilo degerlendirmen: normal")
elif(indeks>24.9 and indeks<=29.9):
	print(" ", ad, " kilo degerlendirmen: kilolu")
elif(indeks>29.9 and indeks<=34.9):
	print(" ", ad, " kilo degerlendirmen: obez")
else:
	print("Hatali bilgi girdiniz")
