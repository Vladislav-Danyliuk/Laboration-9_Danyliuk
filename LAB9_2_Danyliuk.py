import random
a = int(input("Введіть довжину списка: "))

b = 1
c = set()
while b <= a:
    C = random.uniform(0.7 , 150)
    b +=1
    c.add(C)

print("Початковий список: " , c)


f = 1
d = set()
while f <= a:
    D = float(input("Введіть своє число: "))
    f += 1
    d.add(D)

print("Ваша множина: " , d)

g = 0
c1 = list(c)
d1 = list(d)
while g < a:
    h = c1[0] + d1[g]
    g += 1
    print("Сума [" , g , "] елементів спискв: " , h)