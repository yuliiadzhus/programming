users = [
    ("Ivan", 25),
    ("Olena", 19),
    ("Petro", 30),
    ("Anna", 22)
]

sort_by_name = sorted(users, key=lambda user: user[0])
sort_by_age = sorted(users, key=lambda user: user[1])

for name, age in sort_by_name:
    print(f"{name} - {age}")

print()

for name, age in sort_by_age:
    print(f"{name} - {age}")