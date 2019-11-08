#Condition statements
name, age, edct = input("Isim, yas ve egitim bilgilerinizi giriniz: ").split()
if(int(age) >= 18 and (edct == "lise" or edct == "universite")):
	print(" ", name, " ehliyet alabilir\n")
else:
	print(" ", name, " ehliyet alamaz\n")

#*****************************************************************

yazili1, yazili2, sozlu = map(int,input("Iki yazili ve sozlu notunuzu girin: ").split())
ort = (yazili1 + yazili2 + sozlu)/3
if(ort >= 0 and ort <= 24):
	print("Not bilgisi: 0")
elif(ort >= 25 and ort <= 44):
	print("Not bilgisi: 1")
elif(ort >= 45 and ort <= 54):
	print("Not bilgisi: 2")
elif(ort >= 55 and ort <= 69):
	print("Not bilgisi: 3")
elif(ort >= 70 and ort <= 84):
	print("Not bilgisi: 4")
elif(ort >= 85 and ort <= 100):
	print("Not bilgisi: 5")
else:
	print("Yanlis bilgi girdiniz")


#**************************************

import datetime

date = input("Aracinizin trafige cikis tarihini giriniz: (y/m/d)").split("/")
dateN = datetime.datetime.now()

date2 = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
result = dateN - date2
day = result.days

if(day <= 365):
	print("1.servis araligi")
elif(day > 365 and day <= 365*2):
	print("2.servis araligi")
elif(day > 365*2 and day <= 365*3):
	print("3.servis araligi")
else:
	print("Hatali sure bilgisi")
