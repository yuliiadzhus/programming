#1
number = int(input("Введіть число:"))
if number > 0:
    print("Додатнє!")
name = input("Введіть ваше ім'я:")
if name == "Yulia":
    print("Успіх!")
    
#2
number = int(input("Введіть число:"))
if  number % 2 == 0:
     print("Парне!")
else:
    print("Не парне!")
    
#3
password = "12345UKD"
your_password = input("Введіть пароль:")І
if password == your_password:
    print("Доступ дозволено!")
else:
    print("Доступ відхилено")

#4
text = input("Введіть слово:")
if "а" in text:
    print("Пропускаю!")
else:
    print("Не пропускаю")

#5
week_day = input("Введіть день тижня:")
if week_day in ("Понеділок", "Четвер", "Субота"):
    print("Гарного дня!")
elif week_day in ("Вівторок", "П'ятниця"):
    print("Гарного настрою!")
else:
    print("Гарно попрацювати!")

#6
password = input("Введіть пароль:")
if len(password) < 4:
    print("Закороткий")
elif len(password) > 10:
    print("Задовгий")
else:
    print("Прийнято")
   
#7
number = int(input("Введіть число:"))
if  number % 2 == 0:
     print("Парне!")
else:
    print("Не парне!")
 
#8
age = int(input("Введіть свій вік:"))
print("Дитина" if age < 18 else "Дорослий")

#9
mounth = int(input("Введіть число:"))
match mounth:
    case 1:
        print("Січень")
    case 2:
        print("Лютий")
    case 3:
        print("Березень")
    case 4:
        print("Квітень")
    case 5:
        print("Травень")
    case 6:
        print("Червень")
    case 7:
        print("Липень")
    case 8:
        print("Серпень")
    case 9:
        print("Вересень")
    case 10:
        print("Жовтень")
    case 11:
        print("Листопад")
    case 12:
        print("Грудень")
    case _:
        print("Такого місяця немає!")

#10
grade = input("Введіть оцінку від A до F:")
match grade:
    case "A":
        print("5")
    case "B":
        print("4")
    case "C":
        print("3")
    case "D":
        print("2")
    case "F":
        print("1")
    case _:
        print("Не правильна оцінка")

#11
number1 = int(input("Введіть перше число:"))
number2= int(input("Введіть друге число:"))
calculation = input("Оберіть дію: (+, -, *, /, **)")
match calculation:
    case "+":
        print(number1 + number2)
    case "-":
        print(number1 - number2)
    case "*":
        print(number1 * number2)
    case "/":
        print(number1 / number2)
    case "**":
        print(number1 ** number2)
    case _:
        print("Неправильна дія")

#12
password = input("Введіть пароль:")
if len(password) > 8:
    if any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        print("Надійний пароль!")
    else:
        print("Додай цифру!")
else:
    print("Закороткий пароль!")
