# todas funçoes necessarias para interagir com os  PINS
import RPi.GPIO as GPIO
# funções do modulo simplificadas, também possivel usar a biblioteca MFRC522
from mfrc522 import SimpleMFRC522

# cria uma copia da biblioteca SimpleMFRC522 como um objeto. É a onde ira armazenar todas as configuraçoes escritas na TAG que chamare-mos posteriomente.
leia = SimpleMFRC522()

try:
    # Chama o nosso objeto de leitura; envia para o circuito uma ordem para começar uma leitura de qualquer TAG posicionado sobre o leitor RC522.
    id, texto = leia.read()
    print(id)
    print(texto)
finally:
    # Limpar saida para não confundir demais scripts
    GPIO.cleanup()
