from PIL import Image
import os

formats = [
    ".jpg",
    ".png",
    ".jpeg"
]

save_format = ".png"

current_dir = os.getcwd()
save_dir = os.path.join(current_dir, "Converted")

for file in os.listdir(current_dir):
    
    if not os.path.isfile(file):
        continue

    name, ext = os.path.splitext(file)

    if ext in formats:
        with Image.open(file, 'r') as image:
            os.makedirs(save_dir, exist_ok=True)
            image.save(os.path.join(save_dir, name+save_format), format=save_format[1:])

