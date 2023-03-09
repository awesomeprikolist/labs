def magic():
    day = int(input('Введите день: '))
    month = int(input('Введите месяц: '))
    year = int(input('Введите год: '))
    last_digits = year % 100
    return day * month == last_digits

result = magic()
print(result)
