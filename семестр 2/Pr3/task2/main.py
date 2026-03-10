import logic

file_name = "storage.txt"

while True:
    print("\n1 - Додати текст, 2 - Читати все, 0 - Вихід")
    vibir = input("Ваш вибір: ")

    if vibir == "1":
        text = input("Введіть текст (будь-якою мовою): ")
        logic.write_to_file(file_name, text)
    elif vibir == "2":
        print("\n--- Зміст файлу ---")
        logic.read_any_file(file_name)
    elif vibir == "0":
        break
    else:
        print("Оберіть 1, 2 або 0")