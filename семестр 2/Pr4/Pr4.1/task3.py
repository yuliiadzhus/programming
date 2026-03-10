def safe_divide(x, y):
    if y == 0:
        return "Помилка: ділення на нуль!"
    return x / y


def calculate_root(x, y):
    if y == 0:
        return "Помилка: корінь нульового степеня!"
    if x < 0 and y % 2 == 0:
        return "Помилка: парний корінь з від'ємного числа!"
    return x ** (1 / y)


operations = {
    "add": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
    "mul": lambda x, y: x * y,
    "div": safe_divide,
    "pow": lambda x, y: x ** y,
    "root": calculate_root
}

while True:
    operation = input("Введіть операцію (add, sub, mul, div, pow, root) або 'exit' для виходу: ")

    if operation == "exit":
        break

    if operation not in operations:
        print("Помилка: такої операції не існує. Спробуйте ще раз.\n")
        continue

    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
    except ValueError:
        print("Помилка: потрібно вводити саме числа. Спробуйте ще раз.\n")
        continue

    result = operations[operation](num1, num2)
    print(f"Результат: {result}\n")