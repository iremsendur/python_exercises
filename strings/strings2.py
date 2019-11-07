#String data type methods
website = "http://www.google.com.tr"
course = "Python kursu: Python Proglamlama (40 saat)"

a = " Hello World "
print(a.strip())

#website.replace("http://www", "").replace(".com.tr","")
print("www.google.com".strip("w.com"))

print(course.lower())

print(website.count("a"))

print(website.startswith("www"))
print(website.endswith("com"))

print(website.find(".com"))

print(course.isalpha())

b = "Contents"
print(b.center(50,"*")) 

print(course.replace(" ","-"))

c = "Hello World"
print(c.replace("World", "There"))

print(course.split(" "))
