try:
    value = int(input("Введіть число: "))
    print(10 / value)
except (ZeroDivisionError, ValueError) as e:
    print(f"{e}:Помилка введення")