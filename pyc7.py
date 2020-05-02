#!/bin/python
from PIL import Image
import re

image = Image.open("index.png")

width, ht = image.size

pixls = [image.getpixel((x,ht/2)) for x in range(0, width, 7)]

info = ''
for i in pixls:
    info = info + chr(i[0])

data = re.findall('\d+', info)
print(data)
print(''.join(chr(int(i)) for i in data))