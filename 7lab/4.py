from PIL import Image, ImageDraw, ImageFont
import os

if not os.path.exists("image_watermark"):
    os.makedirs("image_watermark")
        
img = Image.open("photo.jpg")
draw = ImageDraw.Draw(img)

font = ImageFont.truetype("Montserrat.ttf", 30)
text = "7laba"

text_width, text_height = draw.textsize(text, font)
x = img.width - text_width - 10
y = img.height - text_height - 10
draw.text((x, y), text, font=font)

img.save(f"image_watermark/watermarked_image.jpg")