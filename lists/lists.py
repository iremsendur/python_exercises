newlist = ["Bmw", "Mercedes", "Opel", "Mazda"]

print(len(newlist))

print(newlist[0])
print(newlist[-1])
print(newlist[len(newlist)-1])

newlist[3] = "Toyota"

print(newlist.index("Mercedes"))
print("Mercedes" in newlist)

print(newlist[-2])

print(newlist[0:3])

newlist[2] = "Toyota"
newlist[3] = "Renault"
newlist[-2:] = ["Toyota", "Renault"]

newlist = newlist + ["Audi", "Nissan"]
print(newlist)

newlist.pop()
print(newlist)

print(newlist[::-1])        #print(newlist.reverse())

studentA = ["Yigit", "Bilgi", 2010, [70,60,70]]
studentB = ["Sena", "Turan", 1999, [80,70,80]]
studentC = ["Ahmet", "Turan", 1998, [80,70,90]]


print(studentA[0])
print(studentB[1])
