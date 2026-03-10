from functools import wraps

def log_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log_name
def print_user_info(name, age, gender, city, profession, hobby):
    print(name, age, gender, city, profession, hobby)

print_user_info("Юля", 17, "Жінка", "Івано-франківськ", "Студентка", "Спорт")

print(print_user_info.__name__)