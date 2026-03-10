from logic import convert, is_supported_currency


def main():
    print("Конвертер валют")
    print("Доступні валюти: USD, EUR, UAH, GBP")

    amount_input = input("Введіть суму: ")
    from_currency = input("З якої валюти: ").upper()
    to_currency = input("У яку валюту: ").upper()

    if not amount_input.replace('.', '', 1).isdigit():
        print("Помилка: введіть коректне число.")

    elif not is_supported_currency(from_currency):
        print(f"Помилка: валюта {from_currency} не підтримується.")

    elif not is_supported_currency(to_currency):
        print(f"Помилка: валюта {to_currency} не підтримується.")

    else:
        amount = float(amount_input)
        result = convert(amount, from_currency, to_currency)
        print(f"\n{amount:.2f} {from_currency} = {result:.2f} {to_currency}")


if __name__ == "__main__":
    main()