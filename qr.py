# download module 'qrcode[pil]'
import qrcode

image = qrcode.make("https://127.0.0.1:8000") # General link for django project without specified url
image.save("qr.png")