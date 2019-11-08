numbers = [1,3,5,7,9,12,19,21]

i = 0
while i<len(numbers):
	print(numbers[i])
	i = i+1

#*********************************
first, last = map(int,input("Baslangic ve bitis degeri girin: ").split())
while first<last:
	if(first%2 == 1):
		print(" ",first," tek sayidir")
	first = first+1

#**********************************************************

a = 100
while a>0:
	print(a)
	a = a - 1
#*****************************************

dizi = list(map(int,input("Bes sayi girin: ").split()))
dizi.sort()
i =0
while i<5:
	print(dizi[i])
	i +=1

#******************************************
b = int(input("Kac urun gireceksiniz: "))
c = 0
urunler = []
while c<b:
	name = input("Urun ismi girin: ")
	price = input("Urun fiyatini girin: ")
	urunler.append({
		"name": name, "price": price
		})
	c += 1

for urun in urunler:
	print(urun)
