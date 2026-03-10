def trigger_error(choice):
    result = ""
    try:
        if choice == 1:
            1 / 0
        elif choice == 2:
            int("abc")
        elif choice == 3:
            [1, 2][5]
        elif choice == 4:
            print(undefined_variable)
        elif choice == 5:
            "2" + 2
        elif choice == 6:
            {}.pop("key")
        elif choice == 7:
            import non_existent_module
        elif choice == 8:
            float("1" * 10000)
        else:
            return "Невірний вибір функції"
    except Exception as e:
        result = str(e)
    return result