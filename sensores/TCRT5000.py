# importar a biblioteca de controle GPIO
import RPi.GPIO as gpio
from sensores.motores_cleaned import *

# definir o mapeamento dos pins para placa
gpio.setmode(gpio.BOARD)

# definir os pinos GPIO como input/'entrada'
leftSensor = 7
rightSensor = 10
gpio.setup(leftSensor, gpio.IN)
gpio.setup(rightSensor, gpio.IN)

# chamar a função para confirmar que os motores estão desligados
Parar()
# desligar as mensagens de perigo
gpio.setwarnings(False)

while True:  # Loop principal
    # se ambos os sensores estiverem desligados, desligar todos os motores
    if gpio.input(leftSensor) == 0 and gpio.input(rightSensor) == 0:
        Frente_Esquerda_Off()
        Frente_Direita_Off()
        Tras_Esquerda_Off()
        Tras_Direita_Off()

    # se ambos os sensores estiverem ligados, ligar ambos os motores
    if gpio.input(leftSensor) == 1 and gpio.input(rightSensor) == 1:
        Frente_Esquerda()
        Frente_Direita()
        Tras_Esquerda()
        Tras_Direita()

    # se o sensor da esquerda estiver ligado, desligar motor da direita (virar esquerda)
    if gpio.input(leftSensor) == 1 and gpio.input(rightSensor) == 0:
        Frente_Esquerda()
        Frente_Direita_Off()
        Tras_Esquerda()
        Tras_Direita_Off()
    # se o sensor da direita estiver ligado, desligar motor da esquerda (virar direita)
    if gpio.input(leftSensor) == 0 and gpio.input(rightSensor) == 1:
        Frente_Esquerda_Off()
        Frente_Direita()
        Tras_Esquerda_Off()
        Tras_Direita_Off()
# limpar os pinos para recomeçar o loop
gpio.cleanup()
