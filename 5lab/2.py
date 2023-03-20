list1 = ["apple", "banana", "pear", "banana", "orange"]
set1 = set(list1)

if len(list1) != len(set1):
    for item in set1:
        if list1.count(item) > 1:
            print("Повторяющийся элемент в списке:", item)
else:
    print("В списке нет повторяющихся элементов")