def get_balance(name, transactions) -> int:
    current_balance = 0
    for bro in transactions:
        bro_name, amount = list(bro.values())[0], list(bro.values())[1]

        if bro_name == name:
            current_balance += amount
    return current_balance


def count_debts(names, amount, transactions) -> dict:
    result = {}
    for name in names:
        balance = get_balance(name, transactions)
        if balance >= amount:
            result[name] = 0
        else:
            result[name] = amount - balance
    return result


transactions = [{"name": "Василий", "amount": 500},
                {"name": "Петя", "amount": 100},
                {"name": "Василий", "amount": -300}]

print(get_balance('Василий', transactions))
print(count_debts(["Василий", "Петя", "Вова"], 150, transactions))
