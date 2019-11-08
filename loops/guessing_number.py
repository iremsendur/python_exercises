#Guess the number game
import random
sayi = random.randint(1,100)
hak = 5
puan = 100
sayac = 0

print("Sayi tahmin oyunu\n")


while hak>0:
	sayac += 1
	tahmin = int(input("Tahmininiz nedir?: "))
	if(tahmin == sayi):
		print(sayac,". seferde dogru tahmin ettiniz oyunu kazandiniz, puaniniz: ",puan)
		break
	else:
		if(tahmin>sayi):
			print("Sayi tahmininizden daha kucuk")
		else:
			print("Sayi tahmininizden daha buyuk")
	hak -=1
	puan -= 20
	if(hak == 0):
		print("Sayiyi bilemediniz oyunu kaybettiniz, sayi ", sayi)

#*******************************************************************
print("Sayi tahmin oyunu\n")
hak2 = int(input("Hak sayisini girin: "))
puan2 = 100
num = puan2//hak2
sayac2 = 0

while hak2>0:
	sayac2 += 1
	tahmin = int(input("Tahmininiz nedir?: "))
	if(tahmin == sayi):
		print(sayac2,". seferde dogru tahmin ettiniz oyunu kazandiniz, puaniniz: ",puan2)
		break
	else:
		if(tahmin>sayi):
			print("Sayi tahmininizden daha kucuk")
		else:
			print("Sayi tahmininizden daha buyuk")
	hak2 -=1
	puan2 = puan2 - num
	if(hak2 == 0):
		print("Sayiyi bilemediniz oyunu kaybettiniz, sayi ",sayi)
