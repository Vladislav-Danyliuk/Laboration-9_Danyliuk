auto = {1:"BMW" , 2:"Ford" , 3:"Tesla" , 4:"Gigul" , 5:"Hyundai" , 6:"Lexus" , 7:"AUDI"}

a = int(input("Введіть індекс. номер автомобіля (від 1 до 7): "))
print( auto[a] )

b = 1
g = 8
c = int(input("Скільки автівок ви ще хочете додати? -> "))
while b <= c:
    auto[g] = str(input("Назва автівки: "))
    g += 1
    b += 1

print(auto)

otua = {"BMW":"10,000$" , "Ford":"9,000" , "Tesla":"21,000$" , "Gigul":"125$" , "Hyundai":"5,000$" , "Lexus":"4,500$" , "AUDI":"7,000$"}

d = str(input("Введіть нзву автомобіля (не вкл. написані вами): "))
print( otua[d] )