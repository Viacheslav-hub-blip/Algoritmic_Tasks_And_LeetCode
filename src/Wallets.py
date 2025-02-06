class BaseWallet:
    exchange_rate: int
    def __init__(self, name: str, amount):
        self.name = name
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, BaseWallet):
            self.amount += other.amount * other.exchange_rate
        else:
            self.amount += float(other)
        return self.__class__(self.name, self.amount)

    def __radd__(self, other):
        if isinstance(other, BaseWallet):
            self.amount += other.amount * other.exchange_rate
        else:
            self.amount += int(other)
        return self

    def __sub__(self, other):
        if isinstance(other, BaseWallet):
            self.amount -= other.amount * other.exchange_rate
        else:
            self.amount -= int(other)
        return self

    def __rsub__(self, other):
        if isinstance(other, BaseWallet):
            self.amount -= other.amount * other.exchange_rate
        else:
            self.amount -= int(other)
        return self

    def __mul__(self, other):
        if isinstance(other, BaseWallet):
            self.amount *= other.amount * other.exchange_rate
        else:
            self.amount *= int(other)
        return self

    def __rmul__(self, other):
        if isinstance(other, BaseWallet):
            self.amount *= other.amount * other.exchange_rate
        else:
            self.amount *= int(other)
        return self

    def __eq__(self, other):
        if isinstance(other, BaseWallet):
            if self.name == other.name and self.amount == other.amount:
                return True
            else:
                return False

    def spend_all(self):
        if self.amount >= 0:
            self.amount = 0

    def to_base(self):
        return self.amount * self.exchange_rate

    def __str__(self):
        return f"{self.__class__.__name__} {self.name} {self.amount * self.exchange_rate}"


class RubleWallet(BaseWallet):
    exchange_rate = 1
    def __init__(self, name: str, amount):
        super().__init__(name, amount)
        self.name = name
        self.amount = amount


    def __str__(self):
        return f"Rubble Wallet {self.name} {self.amount}"


class DollarWallet(BaseWallet):
    exchange_rate = 60
    def __init__(self, name: str, amount):
        super().__init__(name, amount)
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"Dollar Wallet {self.name} {self.amount}"

class EuroWallet(BaseWallet):
    exchange_rate = 70
    def __init__(self, name: str, amount):
        super().__init__(name, amount)
        self.name = name
        self.amount = amount


    def __str__(self):
        return f"Euro Wallet {self.name} {self.amount}"

ruble_wallet = RubleWallet("Первый кошелек", 10)
ruble_wallet2  = RubleWallet('Первый кошелек', 20)
result  = ruble_wallet + ruble_wallet2

r  = ruble_wallet + 2
print(type(r), r.exchange_rate) #<class '__main__.RubleWallet'>
print(DollarWallet("D", 2) + RubleWallet("X", 60))

print(type(result))  # Выводит: Ruble Wallet Первый кошелек 30
