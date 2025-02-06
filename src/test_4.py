from typing import NamedTuple


class PriceAndCount(NamedTuple):
    price: int
    count: int

s:str = input()

all_products = dict()

while s != 'конец':
    s_split: list = s.split(':')
    name  = s_split[0]
    price = int(s_split[1])

    if name not in all_products:
        all_products[name] = PriceAndCount(int(price), 1)
    else:
        all_products[name] = PriceAndCount(all_products[name].price + price, all_products[name].count + 1)

    s = input()

str_product  = ""

for product in all_products:
    str_  = "{0}: {1} ({2} шт.)\n".format(product, all_products[product].price, all_products[product].count)
    str_product += str_

su = 0
print()


str_format = (f"Чек:\n"
              f"---------------------\n"
              f"{str_product}"
              f"---------------------\n"
              f"Итого: {sum(price_and_count.price for price_and_count in all_products.values())}"
              )
print(str_format)