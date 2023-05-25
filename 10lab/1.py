import json


def print_product_info(product):
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии")
    print()


with open("products.json", "r", encoding='utf-8') as f:
    data = json.load(f)

products = data["products"]

list(map(print_product_info, products))
