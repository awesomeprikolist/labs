from PIL import Image, ImageDraw, ImageFont

img = Image.open("photo.jpg")

draw = ImageDraw.Draw(img)

font1 = ImageFont.truetype("Montserrat.ttf", 48)
font2 = ImageFont.truetype("Roboto.ttf", 48) 
color1 = (0, 0, 255) 
color2 = (255, 0, 0) 

name = input("Введите имя: ")
text = name + ", поздравляю!"

img_width, img_height = img.size
text_width1, text_height1 = draw.textsize(text, font1)
text_width2, text_height2 = draw.textsize(text, font2)

x1 = (img_width - text_width1) // 2
y1 = img_height - text_height1 - 10
x2 = (img_width - text_width2) // 2
y2 = y1 - text_height2 - 10

name_len = len(name)
half_len = name_len // 2
name1 = name[:half_len]
name2 = name[half_len:]

draw.text((x1, y1), name1, color1, font1)

name_width1 = draw.textsize(name1, font1)[0]

draw.text((x1 + name_width1, y1), name2, color2, font2)
draw.text((x1 + text_width1 - draw.textsize(", поздравляю!", font1)[0], y1), ", поздравляю!", color1, font1)

img.show()
img.save("itog.jpg")