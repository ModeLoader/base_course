chislo = int(input("Введите натуральное число : "))
fibonachi1 = 1
fibonachi2 = 1
for i in range(1 , chislo + 2 ):
    if i == 1:
        print(fibonachi1 , end = (" "))
    elif i == 2:
        print(fibonachi2 , end = (" "))
    elif i > 2:
        fibonachi3 = fibonachi1 + fibonachi2
        print(fibonachi3 , end = (" "))
        fibonachi2 = fibonachi1
        fibonachi1 = fibonachi3
       