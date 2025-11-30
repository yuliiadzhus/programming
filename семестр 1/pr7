#1
i = 1
while i <= 9:
    print(i * i)
    i += 1

#2
while True:
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    op = input("Оберіть операцію (+, -, *, /): ")
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b != 0:
            print(a / b)
        else:
            print("Ділення на 0 неможливе!")
    else:
        print("Невідома операція")
    cont = input("Продовжити? (так/ні): ")
    if cont.lower() == "ні":
        break

#3
i = 0
while i < 10:
    if i == 5 or i == 7:
        i += 1
        continue
    print(i)
    i += 1

#4
import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Вгадайте число: "))
    attempts += 1
    if secret > guess:
        print("Потрібне більше число")
    elif secret < guess:
        print("Потрібне менше число")
    else:
        print(f"Вітаю! Ви вгадали за {attempts} спроб.")
        break

#5
i = 1
while i < 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
