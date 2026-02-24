import random

my_list = [random.randint(1, 100) for _ in range(random.randint(5, 15))]
print(f"Згенеровано масив (для довідки): {my_list}")

while True:
    try:
        idx = int(input("Введіть індекс елемента: "))
        print(f"Елемент під індексом {idx}: {my_list[idx]}")
    except IndexError:
        print("Помилка: Такого індексу не існує!")
    except ValueError:
        print("Помилка: Введіть ціле число.")

    if input("Бажаєте продовжити? (так/ні): ").lower() != 'так':
        break