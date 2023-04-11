from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('test.png')

result = decode(img)

print(result[0])