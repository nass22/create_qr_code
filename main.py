import qrcode

data = "It's my QRCode"

img = qrcode.make(data)

img.save('test.png')