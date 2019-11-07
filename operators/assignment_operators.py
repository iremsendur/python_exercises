x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

a, b = input("Iki sayi girin: ").split()
print((int(a)*int(b)) - (x+y+z))

print(y//x)

print((x+y+z) % 3)

print(y**x)

x, *y, z = numbers
print(z**3)

print(y[0] + y[1] + y[2])
