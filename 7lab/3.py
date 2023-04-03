from PIL import Image, ImageFilter
import os

if not os.path.exists("image_filtered"):
    os.makedirs("image_filtered")

for i in range(1, 6):
    image = Image.open(f"image_source/{i}.jpg")
    image.filter(ImageFilter.EMBOSS).save(f"image_filtered/{i}.jpg")
    image.close()