import requests                   #github api usage
import json


class Github():
	"""docstring for Github"""
	def __init__(self):
		self.url = "https://api.github.com"

	def findUSer(self, username):
		result = requests.get(self.url + "/users/" + username)
		value = json.loads(result.text)               #return result.json()
		return value

	def showRepo(self, username):
		result = requests.get(self.url + "/users/" + username + "/repos")
		return result.json()                         #value = json.loads(result.text) #return value

	def createRepo(self, repoName, token):
		result = requests.post(self.url + "/user/repos?access_token=" + token, json={"name": repoName,
  "description": "This is your first repository",
  "private": False,
  "has_issues": True,
  "has_projects": True,
  "has_wiki": True})
		return result.json()


github = Github()
	
while True:
	secim = input("1-Kullanici bul 2-Kullanicinin repositorylerini goster 3-Repository olustur 4-Cikis \n Seciminizi girin: ")
	if secim == "4":
		break
	elif secim == "1":
		kullaniciAdi = input("Bulmak istediginiz kullanicinin kullanici adini girin: ")
		result = github.findUSer(kullaniciAdi)
		print("Kullanicinin adi: ",result["name"],",public repository sayisi: ",result["public_repos"],",takipci sayisi: ",result["followers"])
	elif secim == "2":
		kullaniciAdi = input("Repositorylerini gormek istediginiz kullanicinin kullanici adini girin: ")
		result = github.showRepo(kullaniciAdi)
		for repo in result:
			print("Repository ismi: ",repo["name"])
	elif secim == "3":
		token = input("Hesabinizdaki token bilgisini giriniz: ")
		repoName = input("Olusturmak istediginiz repositorynin ismini giriniz: ")
		result = github.createRepo(repoName,token)
		print(result)
	else:
		print("Yanlis bir secim yaptiniz.")
