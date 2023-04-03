from PIL import Image
        
image = Image.open("photo.jpg")

resized_image = image.resize((int(image.width/3), int(image.height/3)))

horizontal_image = image.transpose(Image.FLIP_LEFT_RIGHT)

vertical_image = image.transpose(Image.FLIP_TOP_BOTTOM)


resized_image.save(f"image_changed/resize.jpg")
horizontal_image.save(f"image_changed/horizontal.jpg")
vertical_image.save(f"image_changed/vertical.jpg")