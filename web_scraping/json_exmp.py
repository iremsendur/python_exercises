import json
import os

class User:
	"""docstring for ClassName"""
	def __init__(self, username, password, mail):
		self.username = username
		self.password = password
		self.mail = mail
		

class UserRepository:
	"""docstring for UserRepository"""
	def __init__(self):
		self.users = []
		self.isLoggedIn = False
		self.currentUser = {}
		self.loadUsers()
	
	def loadUsers(self):         #.json dosyasindan kullanici bilgilerini alma
		if os.path.exists("users.json"):
			with open("users.json","r") as file:
				users = json.load(file)
				for user in users:
					user = json.loads(user)
					newUser = User(username = user["username"], password = user["password"], mail = user["mail"])
					self.users.append(newUser)

	def register(self, user: User):
		self.users.append(user)
		self.savetoFile()
		print("Kullanici olusturuldu.")

	def  login(self, username, password):
		for user in self.users:
			if user.username == username and user.password == password:
				self.isLoggedIn = True
				self.currentUser = user
				print("Giris basarili.")
				break

	def savetoFile(self):
		liste = []

		for user in self.users:
			liste.append(json.dumps(user.__dict__))

		with open("users.json","w") as file:
			json.dump(liste,file)

	def logout(self):
		if self.isLoggedIn:
			self.isLoggedIn = False
			self.currentUser = {}
			print("Oturum kapatildi.")
		else:
			print("Giris yapmis kullanici bulunmamakta.")

	def identity(self):
		if self.isLoggedIn:
			print("username: ",self.currentUser.username,"kullanicisi giris yapmis durumda, kullanici maili: ",self.currentUser.mail)
		else:
			print("Giris yapmis kullanici bulunmamakta.")

repository = UserRepository()

while True:
	secim = input("Islem seciniz: 1-Kayit olma 2-Giris yapma 3-Oturumu kapatma 4-Kullanici bilgileri 5-Cikis ")
	if secim == "5":
		break
	elif secim == "1":
		mail = input("Mail adresinizi giriniz: ")
		username = input("Kullanici adinizi giriniz: ")
		password = input("Parolanizi giriniz: ")
		user = User(username, password, mail)
		repository.register(user)
	elif secim == "2":
		if repository.isLoggedIn:
			print("Giris yapmis bir kullanici bulunmakta.")
		else:
			username = input("Kullanici adinizi giriniz: ")
			password = input("Parolanizi giriniz: ")
			repository.login(username, password)
	elif secim == "3":
		repository.logout()
	elif secim == "4":
		repository.identity()
	else:
		print("Hatali secim yaptiniz.")
