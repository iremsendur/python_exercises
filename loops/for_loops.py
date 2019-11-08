numbers = [1,3,5,7,9,12,19,21]

for num in numbers:
	if(num % 3 == 0):
		print(num, " 3un katıdır")


summon = 0
for num in numbers:
	summon = summon + num
print("Dizideki sayilarin toplami: ", summon)


for num in numbers:
	if(num % 2 == 1):
		print(num, "tek sayisinin karesi: ",num**2)

#*******************************************************

cities = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]

for city in cities:
	if(len(city) <= 5):
		print(city," karakter sayisi: ", len(city))

#********************************************************

products =  [
	{"name":"samsung s6", "price": "3000"},
	{"name":"samsung s7", "price": "4000"},
	{"name":"samsung s8", "price": "5000"},
	{"name":"samsung s9", "price": "6000"},
	{"name":"samsung s10", "price": "7000"},
]

sum2 = 0
for product in products:
	sum2 = sum2 + int(product["price"])
print("Urunlerin toplam fiyati: ",sum2)


for product in products:
	if(int(product["price"]) <= 5000):
		print(" ",product["name"]," urununun fiyati: ", product["price"])
