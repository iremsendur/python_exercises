import requests                # Exchange program with api
import json


dovizTur = input("Bozdurmak istediginiz doviz turunu giriniz: ")
dovizTur2 = input("Cevirmek istediginiz doviz turunu giriniz: ")
miktar = input("Ne kadar {} bozdurmak istiyorsunuz?: ".format(dovizTur))

result = requests.get("https://api.exchangeratesapi.io/latest?base=",dovizTur)
dictionary = json.loads(result.text)

print("1 ",dovizTur,"=",dictionary["rates"][dovizTur2],"\n")
print(miktar," ",dovizTur,"=",dictionary["rates"][dovizTur2]*float(miktar)," ",dovizTur2)
