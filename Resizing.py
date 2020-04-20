from PIL import Image

baseWidth = 204
img = Image.open('binary03.jpg')
wPercent = (baseWidth / float(img.size[0]))
hSize = int((float(img.size[1]) * float(wPercent)))
img = img.resize((baseWidth, hSize), Image.ANTIALIAS)
img.save('tinyImage_204.jpg')