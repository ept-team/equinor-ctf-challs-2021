#!/usr/bin/env python3
from PIL import Image

ct = open('flag.png.enc', 'rb').read()
data = [tuple(ct[i:i+3]) for i in range(0, len(ct), 3)]
img = Image.new('RGB', (2000, 250), (255, 255, 255))
img.putdata(data)
img.show()
