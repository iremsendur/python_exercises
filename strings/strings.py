#String data type
website = "http://www.udemy.com"
course = "Python kursu: Python Proglamlama (40 saat)"

print(len(course))
print(website[7:10])
print(website[-3:])
print(course[:15] + course[-15:])
print(course[::-1])

name, surname, age, job = "Irem", "Sendur", 25, "Bilgisayar Muhendisi"

print("Benim adim " + name + " " + surname + ", yasim " + str(age) + " ve meslegim " + job)

#print("Benim adim {} {}, yasim {} ve meslegim {}.".format(name,surname,age,job))
#result = f'Benim adim {name} {surname}, yasim {age} ve meslegim {job}.'
#print(result)


a = "Hello world"
print(a[:6] + "W" + a[-4:])

x = "abc"
print(x*3)
