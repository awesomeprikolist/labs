class Restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name


class IceCream(Restaurant):
    def __init__(self, restaurant_name, flavors, location, hours):
        super().__init__(restaurant_name)
        self.flavors = flavors
        self.location = location
        self.hours = hours

    def show_flavors(self):
        print(f"Сорта мороженого в {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"Сорт {flavor} добавлен в список.")
        else:
            print(f"Сорт {flavor} уже есть в списке.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт {flavor} удален из списка.")
        else:
            print(f"Сорт {flavor} не найден в списке.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Сорт {flavor} есть в наличии.")
        else:
            print(f"Сорт {flavor} отсутствует.")

    def describe_restaurant(self):
        print(f"Локация: {self.location}")
        print(f"Время работы: {self.hours}")


class Stick(IceCream):
    def __init__(self, restaurant_name, flavors, location, hours, stick_material):
        super().__init__(restaurant_name, flavors, location, hours)
        self.stick_material = stick_material

    def show_stick_material(self):
        print(f"Материал палочки: {self.stick_material}")

class SoftIce(IceCream):
    def __init__(self, restaurant_name, flavors, location, hours, shape):
        super().__init__(restaurant_name, flavors, location, hours)
        self.shape = shape

    def show_shape(self):
        print(f"Форма мягкого мороженого: {self.shape}")
            


popsicle = Stick("Мороженное нахрен", ["Вишневое", "Лимонное", "Апельсиновое"], "ТЦ Галерея",
                    "10:00 - 22:00", "Дуб")
soft_serve = SoftIce("Мороженное нахрен", ["Ванильное", "Шоколадное", "Карамельное"], "ТЦ Галерея",
                     "10:00 - 22:00", "Банан")

popsicle.describe_restaurant()
popsicle.show_flavors()
popsicle.show_stick_material()

soft_serve.describe_restaurant()
soft_serve.show_flavors()
soft_serve.show_shape()
