import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    data = []
    total = 0
    for row in reader:
        data.append(row)
        total += int(row[1]) * int(row[2])


print("Нужно купить:")
for row in data:
    print(f"{row[0]} - {row[1]} шт. за {row[2]} руб.")
print(f"Итоговая сумма: {total} руб.")