chislo1 = int(input("Введите 1-ое целое число: "))
chislo2 = int(input("Введите 2-ое целое число: "))

if chislo2 == 0 :
    print("Деление на ноль невозможно")
elif chislo1 % chislo2 == 0:
    print(f"Деление числа {chislo1} на {chislo2} возможно и вот результат:{chislo1//chislo2} " )
else:
    print(f"Деление числа {chislo1} на {chislo2} невозможно и вот остаток:{chislo1%chislo2} " )