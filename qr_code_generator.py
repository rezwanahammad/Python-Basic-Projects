import qrcode

data=input("Enter the text or URL: ").strip()
filename=input("Enter FileName: ").strip()
qr=qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
image=qr.make_image(fill_color="black",back_color="white")
image.save(filename)
print(f'The QR code is saved as {filename}')
