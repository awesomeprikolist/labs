print('Математика для детей: ')
x = 'Решите пример: 3 + 5 = '
k = 0
user_answer = input(x)
for i in range (0,3):
    if user_answer == '8':
        print('Правильно!')
        break
    else:
        k += 1
        print('Ответ неверный')
        y = 'Решите пример: 3 + 5 = '
        user_answer = input(y)
    if k == 3:
        print("Вы проиграли =(")
