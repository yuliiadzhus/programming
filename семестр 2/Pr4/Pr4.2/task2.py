def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(f"double(5) -> {double(5)}")
print(f"triple(5) -> {triple(5)}")