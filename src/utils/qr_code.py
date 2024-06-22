import qrcode
from io import BytesIO

def generate_qr(code: str):
  # TODO: crear QR code
  qr = qrcode.QRCode(version=1, box_size=10, border=1)
  qr.add_data(code)
  qr.make(fit=True)

  # TODO: crear imagen del QR code
  img = qr.make_image(fill='black', back_color='white')
  
  # TODO: guardar la imagen en un buffer
  img_buffer = BytesIO()
  img.save(img_buffer, format='PNG')
  img_buffer.seek(0)

  return img_buffer