from logic import trigger_error

while True:
    print("\nЯку помилку викликати? (1-16)")
    try:
        choice = int(input("Ваш вибір: "))
        error_msg = trigger_error(choice)
        print(f"Отримано текст помилки: {error_msg}")
    except ValueError:
        print("Введіть число!")

    if input("Продовжуємо? (так/ні): ").lower() != 'так':
        break