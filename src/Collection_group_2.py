from array import array
from typing import NamedTuple


class Product(NamedTuple):
    name: str
    price: int


class ProductType(NamedTuple):
    type: str
    products: array


categories_with_products = {}

s_input = input()

while s_input != 'стоп':
    category = s_input.split(' - ')[0]
    product_type = s_input.split(' - ')[1]
    name = s_input.split(' - ')[2]
    price = int(s_input.split(' - ')[3])

    if category not in categories_with_products:
        categories_with_products[category] = [ProductType(product_type, [Product(name, price)])]
    else:
        type_exist = True
        for product_type_in_category in categories_with_products[category]:

            if product_type_in_category.type == product_type:
                product_type_in_category.products.append(Product(name, price))
                type_exist = False

        if type_exist:
            print('Добавление новой категории', product_type, name)
            categories_with_products[category].append(ProductType(product_type, [Product(name, price)]))

    s_input = input()

sorted_dict_by_categories = dict(sorted(categories_with_products.items()))

for category, products_types in sorted_dict_by_categories.items():
    sorted_products_types = sorted(products_types, key=lambda p: p.type)
    sorted_dict_by_categories[category] = sorted_products_types

print()
print(sorted_dict_by_categories)

sorted_dict = {}

for category, syb_categories in sorted_dict_by_categories.items():
    print(category, syb_categories)
    for sub_category in syb_categories:
        print(sub_category)
        sorted_products = sorted(sub_category.products, key=lambda p: p.price)
        sorted_dict[category] = ProductType(sub_category.type, sorted_products)

print()

print(sorted_dict)