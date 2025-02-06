class BaseWallet:
    exchange_rate: int

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, BaseWallet):
            self.amount += (other.amount * other.exchange_rate) / exchange_rate
        else:
            self.amount += other

        return self.__class__(self.name, self.amount)

class RubbleWallet(BaseWallet):
    pass


class DollarWallet(BaseWallet):
    pass


class EuroWallet(BaseWallet):
    pass

baseWallet  = BaseWallet("Rubble", 5)
baseWallet.exchange_rate = 10
baseWallet2  = baseWallet + BaseWallet("Dollar", 5)
print(baseWallet2.amount)