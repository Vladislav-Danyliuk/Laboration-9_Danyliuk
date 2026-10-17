import math
a = (4, 5, 10)
b = (1, 4, 3)
c = (1, 8, 8)

#довжини від 0 0 0 до точки
a1 = math.sqrt( (a[0] - 0)**2 +  (a[1] - 0)**2 + (a[2] - 0)**2)
b1 = math.sqrt( (b[0] - 0)**2 +  (b[1] - 0)**2 + (b[2] - 0)**2)
c1 = math.sqrt( (c[0] - 0)**2 +  (c[1] - 0)**2 + (c[2] - 0)**2)

spisok = [a1 , b1, c1]
print(spisok)

if a1 < b1 and a1< c1:
    print("Точка А найближча")
elif b1 < a1 and b1 < c1:
    print("Точка В найближча")
else:
    print("Точка С найближча")


if a1 > b1 and a1 > c1:
    print("Точка А найдальша")
elif b1 > a1 and b1 > c1:
    print("Точка В найдальша")
elif c1 > b1 and c1 > a1:
    print("Точка С найдальша")