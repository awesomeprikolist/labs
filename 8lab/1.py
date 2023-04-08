from PIL import Image

img = Image.open('photo.jpg')

place = (100,200,500,600)
cropped_image = img.crop(place)
cropped_image.save('image_crop.jpg')
