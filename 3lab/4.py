print('Математика для детей: ')
print('Решите пример: 3 + 5 = ? ')
k = 0
x = int(input())
for i in range (0,3):
    if x == 8:
        print('Правильно!')
        break
    else:
        k += 1
        print('Ответ неверный')
        print('Решите пример: 3 + 5 = ? ')
        x = int(input())
    if k == 3:
        print("Вы проиграли =(")
