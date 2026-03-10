PRICES = {
    "UAH": 1.0,
    "USD": 43.0,
    "EUR": 51.0,
    "GBP": 59.0
}


def is_supported_currency(currency):
    return currency in PRICES


def convert(amount: float, from_currency: str, to_currency: str):
    amount_in_uah = amount * PRICES[from_currency]
    result = amount_in_uah / PRICES[to_currency]
    return result
