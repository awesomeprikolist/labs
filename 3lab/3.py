while True:
    word = input("Введите слово: ")
    if word.find('ф') != -1:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово")
    answer = input("Хотите продолжить? (да/нет) ")
    if answer.lower() == 'нет':
        break
