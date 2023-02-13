import qrcode
import urllib.request

input_data = input("QR kodunu yapmak istediğiniz link: ")
qr = qrcode.QRCode(version=5, box_size=10, border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode001.png')
img.show('qrcode001.png')
url = "https://replit.com/@erencanakkus/qr#qrcode001.png"
urllib.request.urlretrieve(url, "qr.png")