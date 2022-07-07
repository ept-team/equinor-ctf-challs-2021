from PIL import Image, ImageDraw, ImageFont

flag = open('flag.txt').read()
img = Image.new('RGB', (2000, 250), (255, 255, 255))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("equinor.ttf", 108)
draw.text((40, 90), flag, (0, 0, 0), font=font)
img.show()
img.save('flag.png')
