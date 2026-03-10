import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} виконалась за {end - start:.7f} секунд")
        return result
    return wrapper

numbers = [4, 45, -3, 12, 23, 34, 54, 90, 23, 34, 100, 45, -78, 23, 1]

@measure_time
def power_for(nums):
    result = []
    for num in nums:
        result.append(num ** 10)
    return result

@measure_time
def power_while(nums):
    result = []
    i = 0
    while i < len(nums):
        result.append(nums[i] ** 10)
        i += 1
    return result

@measure_time
def power_lambda(nums):
    return list(map(lambda x: x ** 10, nums))

power_for(numbers)
power_while(numbers)
power_lambda(numbers)