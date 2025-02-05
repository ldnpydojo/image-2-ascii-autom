from PIL import Image
import sys

importImage = sys.argv[1]

image = Image.open(importImage)

blockWidth = image.width/70
blockHeight = blockWidth

image.thumbnail((70, 70))
for y in range(0, image.height):
    for x in range(0, image.width):
        pixel = image.getpixel((x, y))
        brightness = pixel[0] * 2 + pixel[1] * 4 + pixel[2]
        if brightness > (255 * 7 / 2):
            print("X", end="")
        else:
            print(" ", end="")
    print()
sys.exit(0)
for x in range(0, image.width, 70):
    for y in range(0, image.height, 70):
        block = image.crop((x, y, x+blockWidth, y+blockHeight))
        block.show()
        break
    break









