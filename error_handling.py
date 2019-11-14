liste = ["1", "2", "5a", "10b", "abc", "10", "50"]
list2 = []

for elm in liste:
	try:
		int(elm)
	except ValueError as e:                                   #Sayisal degerleri bulma
		continue
	else:
		list2.append(elm)


print("Liste: ",liste)
print("Listedeki sayisal degerler: ",list2,"\n")
print("****************************************************\n")

#***************************************************************

num = ""
print("Cikmak icin 'q'ya basiniz")
while num != "q":
	try:
		num = input("Bir sayi giriniz: ")
		if num != "q":
			num = int(num)                                         #Girilen degerin sayisal olup olmadiginin kontrolu
			print("Girdiginiz sayi: ",num)
			break
	except ValueError as e:
		print("Hatali deger girdiniz,hata mesaji: ", e)

print("****************************************************\n")

#****************************************************************

def checkPassword(password):

	turkce_karakterler = "çşİüğıö"

	for i in password:
		if i in turkce_karakterler:
			raise TypeError("Parolaniz turkce karakter iceremez.")

	print("Gecerli parola")

password = input("Bir parola giriniz: ")                          #Girilen stringin turkce karakter icerip icermeme kontrolu

try:
	checkPassword(password)
except TypeError as e:
	print("Hatali parola, hata mesaji: ",e)

print("****************************************************\n")

#***************************************************************
import math

def faktoriyel(number):
	number = int(number)
	if number < 0:
		raise ValueError("Sayi sifirdan kucuk olamaz.")
	else:
		print("Sayinin faktoriyeli: ",math.factorial(number))    #Faktoriyel fonksiyonuna gonderilen sayinin kontrolu

sayi = input("Sayi giriniz: ")
try:
	faktoriyel(sayi)
except ValueError as e:
	print("Hatali deger, hata mesaji: ",e)
