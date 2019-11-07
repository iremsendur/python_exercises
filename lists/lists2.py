#Lists methods examples
names = ["Ali", "Yagmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]

names.append("Cenk")
print(names)

names.insert(0, "Sena")
print(names)

print(names.index("Deniz"))

names.remove("Deniz")
print(names)

print(names.count("Ali"))
print("Ali" in names)

names.reverse()
print(names)

names.sort()
print(names)

years.sort()
print(years)

strng = "Chevrolet,Dacia"
print(strng.split(","))

print(min(years))
print(max(years))

print(years.count(1998))

years.clear()
print(years)

a, b, c = input("Uc marka bilgisi giriniz: ").split()
brands = [a, b, c]
print(brands)
