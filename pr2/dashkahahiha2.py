d = int(input("Введите день "))
m = int(input("Введите месяц "))
c = int(input("Введите год ")) 
 

y = c * 100
a = d + ((13*m - 1) // 5 ) + y + (y //4 + c // 4 - 2*c + 777)
a %= 7
print(a)
