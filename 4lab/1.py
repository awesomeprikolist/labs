def divide(x):
    if x % 3 == 0:
        print('Число делится на 3')
        return None
    else:
        print('Число не делится на 3')
        return None

user_input= int(input('Введите число: '))
number = float(user_input)
result = divide(number)
if result is not None:
    print(result)