from PIL import Image

baseWidth = 23
img = Image.open('simpleMaze.png')
wPercent = (baseWidth / float(img.size[0]))
hSize = int((float(img.size[1]) * float(wPercent)))
img = img.resize((baseWidth, hSize), 1) # or equivalent to 1 such as ANTIALIAS
img.save('simpleMazeTiny_04.jpg')

