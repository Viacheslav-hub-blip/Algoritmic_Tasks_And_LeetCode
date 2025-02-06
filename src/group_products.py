class Product:
    def __init__(self, name, price):
        self.name  = name
        self.price = price


class SubCategory:
    def __init__(self, name):
        self.name  = name
        self.products = [Product]

    def add_product(self, product):
        old_products = self.products
        old_products.append(product)
        sorted_products = sorted(old_products, key=lambda p: p.price)
        self.products = sorted_products


class Category:
    def __init__(self, name):
        self.name  = name
        self.subcategories = []

    def add_subcategory(self, subcategory):
        old_subcategories = self.subcategories
        old_subcategories.append(subcategory)
        sorted_subcategories = sorted(old_subcategories, key=lambda c: c.name)
        self.subcategories = sorted_subcategories

s  = input()

all_categories = [Category]
all_sub_categories  = []

while s != 'стоп':
    category, sub_category, product_name, price = s.split(' - ')

    if category not in [name in all_categories for name in all_categories]:

    current_category = Category(category)
    current_sub_category = SubCategory(sub_category)
    current_product = Product(product_name, price)

    current_sub_category.add_product(current_product)
    current_category.add_subcategory(current_sub_category)

    all_categories.append(current_category)
    all_sub_categories.append(current_sub_category)

