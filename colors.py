from PIL import Image
from PIL import ImageGrab

#List all colors (rgb format) on image_name
def listColors(image_name):
    image = Image.open(image_name)
    image = image.convert('RGB')
    pixel = image.load()

    x_max, y_max = image.size

    image_colors = []

    for i in range(0, x_max):
        for j in range(0, y_max):
            if(pixel[i, j] not in image_colors):
                image_colors.append(pixel[i, j])

    return image_colors

#Turn every color_a in image_name to color_b, and every color that isn't color_a will become color_c
def changeColor(image_name, color_a, color_b, color_c):
    image = Image.open(image_name)
    image = image.convert('RGB')
    pixel = image.load()

    x_max, y_max = image.size

    for i in range(0, x_max):
        for j in range(0, y_max):
            if(pixel[i, j] == color_a):
                pixel[i, j] = color_b
            else:
                pixel[i, j] = color_c

    image.save(str(color_a) + '_' + image_name)
