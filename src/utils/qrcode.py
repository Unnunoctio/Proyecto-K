import qrcode

def generate_qr(text: str, path='qr_code.png'):
  # TODO: crear QR code
  qr = qrcode.QRCode(version=1, box_size=10, border=5)
  qr.add_data(text)
  qr.make(fit=True)

  # TODO: crear imagen del QR code
  img = qr.make_image(fill='black', back_color='white')
  img.save(path)