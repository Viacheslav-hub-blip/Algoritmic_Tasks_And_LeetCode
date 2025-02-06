from typing import NamedTuple


class Product(NamedTuple):
    name: str
    price: int


categories_with_products = {}

s = input()

while s != 'стоп':
    s_split = s.split(' - ')

    product_name = s_split[0]
    product_category = s_split[1]
    product_price = int(s_split[2])

    if product_category not in categories_with_products:
        categories_with_products[product_category] = [Product(product_name, product_price)]
    else:
        categories_with_products[product_category].append(Product(product_name, product_price))
    s = input()

sorted_dict = dict(sorted(categories_with_products.items()))

for category, value in sorted_dict.items():
    sorted_value = sorted(value, key=lambda item: item.price)
    sorted_dict[category] = sorted_value

result_str = f""

for category, value in sorted_dict.items():
    result_str += f"{category}:\n"
    for product in value:
        result_str += f"  - {product.name} ({product.price} руб.)\n"

print(result_str)
