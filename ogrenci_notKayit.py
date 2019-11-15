def not_hesapla(satir):
	liste = satir.split(":")
	ad = liste[0]
	liste2 = liste[1].split(",")
	toplam = 0
	for i in liste2:
		toplam = toplam + int(i)
	ort = int(toplam / 3)
	if ort >= 90:
		harf = "AA"
	elif ort >= 85 and ort <= 89:
		harf = "BA"
	elif ort >= 80 and ort <= 84:
		harf = "BB"
	elif ort >= 75 and ort <= 79:
		harf = "CB"
	elif ort >= 60 and ort <= 74:
		harf = "CC"
	elif ort >= 50 and ort <= 59:
		harf = "DC"
	elif ort >= 40 and ort <= 49:
		harf = "DD"
	elif ort >= 30 and ort <= 39:
		harf = "FD"
	else:
		harf = "FF"

	return ad + ": notlarinin ortalamasi: " + str(ort) + " harf notu: " + harf + "\n"


def notlari_oku():
	with open("sinav_notlari.txt","r") as file:
		for satir in file:
			print(not_hesapla(satir))



def not_gir():
	ogrAd, ogrSoyad = input("Ogrenci ad ve soyadini giriniz: ").split()
	not1, not2, not3 = input("Ogrencinin 3 notunu giriniz: ").split()
	with open("sinav_notlari.txt","a") as file:
		file.write(ogrAd + " " + ogrSoyad + ":" + not1 + "," + not2 + "," + not3 + "\n")



def not_kayit():
	with open("sinav_notlari.txt","r") as file:
		liste = []
		for i in file:
			liste.append(not_hesapla(i))
		print(liste)

		with open("sonuclar.txt","w") as file2:
			for x in liste:
				file2.write(x)



while True:
	islem = input("Hangi islemi yapmak istiyorsunuz?\n 1-Notlari Oku\n 2-Notlari Gir\n 3-Notlari Kayit Et\n 4-Cikis\n ")

	if islem == "1":
		notlari_oku()
	elif islem == "2":
		not_gir()
	elif islem == "3":
		not_kayit()
	else:
		break
