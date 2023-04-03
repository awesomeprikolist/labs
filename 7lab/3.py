from PIL import Image, ImageFilter
import os

# Создаем новую папку для сохранения изображений
if not os.path.exists("filtered"):
    os.makedirs("filtered")

# Открываем каждый файл и применяем к нему фильтр
for i in range(1, 6):
    # Открываем исходный файл
    image = Image.open(f"image_source/{i}.jpg")

    # Применяем фильтр и сохраняем полученную копию в новой папке
    image.filter(ImageFilter.EMBOSS).save(f"filtered/{i}.jpg")

    # Освобождаем ресурс памяти, занимаемый объектом image
    image.close()
