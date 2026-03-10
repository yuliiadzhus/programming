while True:
    try:
        text = input("Введіть щось: ")

        if len(text) == 0:
            raise ValueError("Ввід не може бути порожнім")
        if text.isspace():
            raise ValueError("Ввід містить тільки пробіли")

    except ValueError as e:
        print(f"Зловлено помилку: {e}")
    else:
        print("Дані прийнято")

    if input("Спробувати ще раз? (так/ні): ").lower() != 'так':
        break