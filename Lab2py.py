
#ввод данных(исходных)
#исходные 3 числа
a, b, c=input("Type in coefficients in format: a b c\n").split()
a=int(a)
b=int(b)
c=int(c)

sum=a+b+c #сумма трёх чисел

#нахождение минимального из чисел
#********************************

if(a<b):
    if(a<c):
        min=a
    else:
        min=c
else:
    if(b<c):
        min=b
    else:
        min=c
        
#********************************
        
sum-=min #вычитаем из суммы минимальное число
#записываем ответ
print("Answer is :")
print("sum = ", sum)
