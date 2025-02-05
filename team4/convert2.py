from PIL import Image
import sys
from pixel_chars import pixel_chars

importImage = sys.argv[1]

image = Image.open(importImage)

blockWidth = image.width/70
blockHeight = blockWidth

image.thumbnail((70, 70))
for y in range(0, image.height):
    for x in range(0, image.width):
        pixel = image.getpixel((x, y))
        brightness = pixel[0] * 0.2126 + pixel[1] * 0.7152 + pixel[2] * 0.0722
        char = pixel_chars[int(brightness)]
        print(char, end="")
    print()
sys.exit(0)
for x in range(0, image.width, 70):
    for y in range(0, image.height, 70):
        block = image.crop((x, y, x+blockWidth, y+blockHeight))
        block.show()
        break
    break









