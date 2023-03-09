def divide(x):
    try:
        return 100 / x
    except ValueError:
        print("Ошибка: Вы ввели не число.")
        return None
    except ZeroDivisionError:
        print("Ошибка: На ноль делить нельзя.")
        return None

user_input = input("Введите число: ")

try:
    number = float(user_input)
except ValueError:
    print("Ошибка: Вы ввели не число.")
else:
    result = divide(number)
    if result is not None:
        print("Результат: 100 / {} = {}".format(number, result))