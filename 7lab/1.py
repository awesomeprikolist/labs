from PIL import Image

image = Image.open('photo.jpg')

height, width = image.size
format = image.format
mode = image.mode

print(f'Размер изображения: ', image.size)
print(f'Формат изображения: ', image.format)
print(f'Цветовая модель изображения: ', image.mode)

image.show()