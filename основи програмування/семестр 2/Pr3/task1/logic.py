import os

FILE_NAME = "storage.txt"

def create_file():
    if os.path.exists(FILE_NAME):
        print(f"Помилка: Файл '{FILE_NAME}' уже існує.")
    else:
        with open(FILE_NAME, 'w', encoding='utf-8') as f:
        print(f"Файл '{FILE_NAME}' успішно створено.")

def write_to_file(text):
    with open(FILE_NAME, 'a', encoding='utf-8') as f:
        f.write(text + '\n')
    print("Текст успішно додано.")

def read_file():
    if not os.path.exists(FILE_NAME):
        print("Помилка: Файл не знайдено. Спочатку створіть його.")
        return

    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if not lines:
                print("Файл порожній.")
            else:
                print("--- Вміст файлу ---")
                for line in lines:
                    print(line.strip())
                print("------------------")
    except Exception as e:
        print(f"Виникла помилка при читанні: {e}")

def get_statistics():
    if not os.path.exists(FILE_NAME):
        print("Помилка: Файл не існує.")
        return

    with open(FILE_NAME, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    non_empty_lines = len([line for line in lines if line.strip()])
    total_chars = sum(len(line.replace('\n', '')) for line in lines)

    print(f"Статистика файлу:")
    print(f" - Загальна кількість рядків: {total_lines}")
    print(f" - Кількість непорожніх рядків: {non_empty_lines}")
    print(f" - Кількість символів (без \\n): {total_chars}")

def clear_file():
    if not os.path.exists(FILE_NAME):
        print("Помилка: Файл не існує.")
        return
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        pass
    print("Вміст файлу повністю очищено.")