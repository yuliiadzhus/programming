import os

def read_any_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("Помилка: Файл не знайдено!")

def write_to_file(file_name, text):
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(text + "\n")