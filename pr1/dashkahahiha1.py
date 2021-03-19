print ("введи число")
a = int(input("a = " ))
b = int(input("b = " ))
print ("меняем местоположение")
a, b = b, a
print (a, b)



print ("напиши любое число")
a = int(input())
suma = 0
while a > 0:
    suma = suma + a % 10
    a = a // 10
print (suma)



print ("напиши число а")
a = int(input())
print ("напиши число b")
b = int(input())
print ("напиши число c")
c = int(input())
D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)
    print (x1, x2)
elif D == 0:
    x1 = (-b) / (2 * a)
    print (x1)
else:
    print ("корней нет")
