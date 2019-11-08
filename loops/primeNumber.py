#Prime numbers
sayi = int(input("Bir sayi giriniz: "))
sayac = 0
if sayi == 1:
	print("Sayi asal degildir")
	
for x in range(2,sayi):
	if(sayi % x == 0):
		sayac += 1
if(sayac >0):
	print("Sayi asal sayi degildir")
else:
	print("Sayi asal sayidir")
