from PIL import Image

celebrity = {
    "Новый год": "hny.jpg",
    "Пасха": "pasha.jpg",
    "День рождения": "hb.jpg",
    "Масленица": "maslo.jpg"
}

x = input('Напишите праздник: ')

celebrity_path = celebrity.get(x)

if celebrity_path:
    img = Image.open(celebrity_path)
    img.show()
else:
    print('Открытка не найдена')
