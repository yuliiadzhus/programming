while True:
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        print(f"Результат: {a / b}")
    except ZeroDivisionError:
        print("Помилка: Не можна ділити на нуль!")
    except ValueError:
        print("Помилка: Введіть, будь ласка, число, а не літери.")

    if input("Продовжити? (так/ні): ").lower() != 'так':
        break