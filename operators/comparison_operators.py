a, b = map(int,input("Iki sayi girin: ").split())
if(a>b):
	print("En buyuk sayi: ",a)
else:
	print("En buyuk sayi: ",b)

#*****************************************************

vize1, vize2, final = map(int,input("Iki vize ve final notu giriniz: ").split())
ort = ((vize1+vize2)/2 * 0.6) + (final*0.4)
if(ort >= 50):
	print("Sinifi gectiniz.")
else:
	print("Sinifi gecemediniz.")

#**********************************

c = input("Bir sayi girin: ")
if(int(c)%2 == 0):
	print("Sayi cift sayidir.")
else:
	print("Sayi tek sayidir.")

#**********************************

d = input("Bir sayi girin: ")
if(int(d)>0):
	print("Sayi pozitif.")
else:
	print("Sayi negatif.")

#*********************************

email = "iremsendur@gmail.com"
password = "abc895"

e = input("Email adresi girin: ")
if(e != email):
	print("Hatali mail adresi")
else:
	print("Girilen mail dogru")

p = input("Parola girin: ")
if(p != password):
	print("Hatali parola")
else:
	print("Girilen parola dogru")
