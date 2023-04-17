import os
from PIL import Image

processed_dir = "itog"
os.makedirs(processed_dir, exist_ok=True)

input_dir = "photo"

for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        with Image.open(os.path.join(input_dir, filename)) as img:
            img = img.rotate(90)
            output_file = os.path.join(processed_dir, filename)
            img.save(output_file)