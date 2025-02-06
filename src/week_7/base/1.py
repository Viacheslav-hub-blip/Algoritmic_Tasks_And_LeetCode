import requests


def get_exchange_rate(base_currency:str, target_currency:str):
    base_currency, target_currency = base_currency.lower(), target_currency.lower()
    url  = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{base_currency}.json"
    response = requests.get(url)
    data = response.json()
    return data[base_currency][target_currency]

def convert_currency(base_currency:str, target_currency:str, amount):
    rate  = get_exchange_rate(base_currency, target_currency)
    return round(rate * amount, 2)

print(get_exchange_rate('eur', 'rub'))
print(convert_currency('usd', 'eur', 20))

a  = [{"1":1}]
b = {"2": a}
print(b)