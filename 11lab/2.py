class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")


restaurant1 = Restaurant("Аригато", "Японская")
restaurant2 = Restaurant("Бургер-кинг", "Американская")
restaurant3 = Restaurant("Пловчикс", "Узбекистанская")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
