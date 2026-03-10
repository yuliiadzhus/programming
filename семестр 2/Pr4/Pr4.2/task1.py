def action_counter(name):
    count = 0
    def count_action():
        nonlocal count
        count += 1
        print(f"{name} виконав дію №{count}")
    return count_action

ivan = action_counter("Ivan")
petro = action_counter("Petro")

ivan()
ivan()
petro()