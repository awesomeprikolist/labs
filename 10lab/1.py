import json


# определяем функцию для вывода информации о продукте
def print_product_info(product):
    # выводим название продукта
    print(f"Название: {product['name']}")
    # выводим цену продукта
    print(f"Цена: {product['price']}")
    # выводим вес продукта
    print(f"Вес: {product['weight']}")
    # проверяем, есть ли продукт в наличии
    if product["available"]:
        # если да, то выводим соответствующее сообщение
        print("В наличии")
    else:
        # если нет, то выводим другое сообщение
        print("Нет в наличии")
    # выводим пустую строку для разделения продуктов
    print()


# открываем файл с данными о продуктах в режиме чтения
with open("products.json", "r", encoding='utf-8') as f:
    # загружаем данные из файла в переменную data
    data = json.load(f)

# получаем список продуктов из словаря data
products = data["products"]

# применяем функцию print_product_info ко всем элементам списка products с помощью функции map
list(map(print_product_info, products))
