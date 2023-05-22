class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f'Рейтинг: {self.rating}')

    def update_rating(self, new_rating):
        self.rating = new_rating


my_restaurant = Restaurant("Пиццуха", "Итальяно", 4)
n = Restaurant('Абв', "Ваг", 4)
n.describe_restaurant()
my_restaurant.describe_restaurant()
my_restaurant.update_rating(int(input("Новый рейтинг: ")))
my_restaurant.describe_restaurant()
