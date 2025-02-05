from PIL import Image
import sys
from pixel_chars2 import pixel_chars

importImage = sys.argv[1]

image = Image.open(importImage)

blockWidth = image.width/70
blockHeight = blockWidth

image.thumbnail((70, 70))
for y in range(0, image.height):
    for x in range(0, image.width):
        pixel = image.getpixel((x, y))
        brightestColor = pixel.index(max(pixel))
        brightness = pixel[0] * 0.2126 + pixel[1] * 0.7152 + pixel[2] * 0.0722
        char = pixel_chars[int(brightness * (len(pixel_chars) - 1) / 255)]
        print("\x1b[38;2;%d;%d;%dm%s\x1b[0m" % (pixel[0], pixel[1], pixel[2], char), end="")

    print()

sys.exit(0)
for x in range(0, image.width, 70):
    for y in range(0, image.height, 70):
        block = image.crop((x, y, x+blockWidth, y+blockHeight))
        block.show()
        break
    break









