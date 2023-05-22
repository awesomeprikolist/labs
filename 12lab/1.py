class Restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name)
        self.flavors = flavors

    def show_flavors(self):
        print(f"Виды мороженного: {self.flavors}")
       
        
my_ice_cream_stand = IceCreamStand('Морожка', ["Ваниль", "Шокололад", "Клубничка"])
my_ice_cream_stand.show_flavors()

