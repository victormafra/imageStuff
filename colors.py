from PIL import Image
from PIL import ImageGrab

#List all colors (rgb format) on imageName
def listColors(imageName):
    image = Image.open(imageName)
    image = image.convert('RGB')
    pixel = image.load()

    xMax, yMax = image.size

    imageColors = []

    for i in range(0, xMax):
        for j in range(0, yMax):
            if(pixel[i, j] not in imageColors):
                imageColors.append(pixel[i, j])

    return imageColors

#Turn every colorA in imageName to colorB, and every color that isn't colorA will become colorC
def changeColor(imageName, colorA, colorB, colorC):
    image = Image.open(imageName)
    image = image.convert('RGB')
    pixel = image.load()

    xMax, yMax = image.size

    for i in range(0, xMax):
        for j in range(0, yMax):
            if(pixel[i, j] == colorA):
                pixel[i, j] = colorB
            else:
                pixel[i, j] = colorC

    image.save(str(colorA) + '_' + imageName)
