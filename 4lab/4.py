def lucky(number):
    half = len(number) // 2
    first_half = number[:half]
    second_half = number[half:]
    return sum(map(int, first_half)) == sum(map(int, second_half))

number = input("Введите номер билета: ")

if len(number) % 2 == 0:
    if lucky(number):
        print("Поздравляем! У вас счастливый билет!")
    else:
        print("К сожалению у вас несчатливый билет =(")
else:
    print("Номер должен быть четной длины")