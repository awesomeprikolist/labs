a = int(input())
if a % 2 == 0 and a < 50:
    print('Вы занимаете верхнюю койку купе')
elif a % 2 == 0 and a > 50:
    print('Вы занимаете нижнюю койку боковую')
elif a % 2 != 0 and a < 50:
    print('Вы занимаете нижнюю койку купе')
elif a % 2 != 0 and a > 50:
    print('Вы занимаете нижнюю койку боковую')




