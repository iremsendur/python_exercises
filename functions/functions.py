def prnt(word, number):
	for x in range(1,number+1):
		print(word)

prnt("irem",5)

#******************************
def turnToList(*params):
	list1 = params
	print(list1)

	#for param in params:
	#   list1.append(param)

turnToList(10,20,30,40,50)
#*****************************

def findPrimes(sayi1,sayi2):
	list2 = []
	for sayi in range(sayi1,sayi2+1):
		sayac = 0
		
		for x in range(2,sayi):
			if(sayi % x == 0):
				sayac += 1
		if(sayac == 0):
			list2.append(sayi)
	print(sayi1," ve ",sayi2," arasindaki asal sayilar: ",list2)

findPrimes(5,15)
#*********************************************************************

def bolen(sayi):
	list1 =[]
	for x in range(1,sayi):
		if(sayi % x == 0):
			list1.append(x)
	print(sayi,"sayisinin tam bolenleri: ",list1)

bolen(10)
