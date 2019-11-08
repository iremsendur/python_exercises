IremHesap = {
	"ad": "Irem Sendur",
	"hesapNo": "15738325",
	"bakiye": 3000,
	"ekHesap": 2000
}

AliHesap = {
	"ad": "Ali Yilmaz",
	"hesapNo": "14904623",
	"bakiye": 4000,
	"ekHesap": 1000
}

def bank(hesap, miktar):
	print("Merhaba ",hesap["ad"])
	if(miktar > hesap["bakiye"]):
		if(miktar <= hesap["bakiye"] + hesap["ekHesap"]):
			ekHspKullanim = input("Ek hesap kullanilsin mi: (e/h)")
			if(ekHspKullanim == "e"): 
				hesap["ekHesap"] = hesap["ekHesap"] - (miktar- hesap["bakiye"])
				hesap["bakiye"] = 0
				print("Para cekme islemi basarili.")
				bakiyeSorgula(hesap)
			else:
				print("Para cekme islemi basarisiz, ",hesap["hesapNo"]," nolu hesabinizda ",hesap["bakiye"]," bulunmaktadir.")
		else:
			print("Hesabinizda yeterli bakiye bulunmamaktadir.")
			bakiyeSorgula(hesap)
	else:
		hesap["bakiye"] -= miktar 
		print("Para cekme islemi basarili.")
		bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
	print(hesap["hesapNo"]," nolu hesabinizda ",hesap["bakiye"]," Tl,ek hesabinizda ",hesap["ekHesap"]," Tl bulunmaktadir.")


name = input("Hangi hesaba erismek istiyorsunuz: (IremHesap/AliHesap)")
number = int(input("Hesabinizdan ne kadar cekmek istiyorsunuz: "))
if(name == "IremHesap"):
	bank(IremHesap,number)
else:
	bank(AliHesap,number)
