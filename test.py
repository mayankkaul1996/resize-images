from PIL import Image
import os

def resize(im, new_width):
    width, height = im.size
    ratio = height/width
    new_height = int(ratio * new_width)
    resized_image = im.resize((new_width, new_height))
    return resized_image

files = os.listdir('images')
extensions = ['jpg', 'jpeg', 'png', 'webp']
widths = [1500, 2400, 3300, 4800, 6000]
for file in files:
    ext = file.split('.')[-1]
    if ext in extensions:
        im = Image.open('images/' + file)
        for width in widths:
            im_resized = resize(im, width)
            file_path = f"resized_images/{file}-{width}.jpg"
            im_resized.save(file_path)
