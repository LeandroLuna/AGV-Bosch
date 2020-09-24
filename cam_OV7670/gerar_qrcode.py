import pyqrcode  # Biblioteca que ajudara a escrever o QRCode
import png

# Informação digitada pelo usuario a ser armazenada no QRCode
texto = (input('Identificação do produto: '))
img = texto + '.png'
# Armazena a informação do usuario em formato do QRCode
imagem = pyqrcode.create(texto)
# Cria a imagem do QR Code em formato .PNG
imagem.png(img, scale=5)
