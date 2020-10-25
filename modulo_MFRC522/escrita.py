# pinagens
import RPi.GPIO as GPIO
# funções do modulo simplificadas, também possivel usar a biblioteca MFRC522
from mfrc522 import SimpleMFRC522

# cria uma copia da biblioteca SimpleMFRC522 como um objeto. É a onde ira armazenar todas as configuraçoes escritas na TAG.
leia = SimpleMFRC522()

try:
    texto = input('Dado a ser escrito na TAG: ')
    print("Posicione sua TAG para escrita")
    leia.write(texto)
    print("Escrita!")
finally:
    GPIO.cleanup()  # Limpar saida para não confundir demais scripts
