# Biblioteca que da capacidade de processamento de imagem
from PIL import Image
# Biblioteca para decodificar as informaçoes do QR Code
from pyzbar.pyzbar import decode

# Nome do arquivo a ser decodificado
arquivo = input('Nome do arquivo a ser decodificado - com extensão .png: ')
# Decodificaçao do arquivo/imagem QR Code
set_dados = decode(Image.open(arquivo))
# Filtrar a informação que queremos, removendo : type, rect, polygon e coordenadas. A instrução da STR é usada para remover o caractere 'b', que significa byte, e é irrelevante na nossa decodificação.
dados = str(set_dados[0].data)[2:-1]
print(dados)  # Printa a informação armazenada no QR Code
