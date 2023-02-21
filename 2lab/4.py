a = input()
m = input()
r = 'красный'
b = 'синий'
y = 'желтый'
p = 'фиолетовый'
o = 'оранжевый'
g = 'зеленый'
if a == r and m == b:
    print(p)
if a == r and m == y:
    print(o)
if a == b and m == y:
    print(g)
if a != r and a !=b and a !=y and m !=r and m != b and m !=y:
    print('Цвета нормальные выбирай')