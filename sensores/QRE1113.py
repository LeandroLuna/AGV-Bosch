# importar a biblioteca de controle GPIO
import RPi.GPIO as gpio

# definir o mapeamento dos pins para placa
gpio.setmode(gpio.BOARD)

# definir os pinos GPIO como output/'saida'
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)


# definir os pinos GPIO como input/'entrada'
leftSensor = 7
rightSensor = 10
gpio.setup(leftSensor, gpio.IN)
gpio.setup(rightSensor, gpio.IN)


def leftOn():  # ligar motor esquerdo
    gpio.output(15, 1)


def leftOff():  # desligar motor esquerdo
    gpio.output(15, 0)


# ligar motor direito
def rightOn():
    gpio.output(13, 1)


# desligar motor direito
def rightOff():
    gpio.output(13, 0)


# desligar todos os motores
def stopAll():
    gpio.output(13, 0)
    gpio.output(15, 0)


# chamar a função para confirmar que os motores estão desligados
stopAll()
# desligar as mensagens de perigo
gpio.setwarnings(False)

while True:  # Loop principal
    # se ambos os sensores estiverem desligados, desligar ambos os motores
    if gpio.input(leftSensor) == 0 and gpio.input(rightSensor) == 0:
        leftOff()
        rightOff()

    # se ambos os sensores estiverem ligados, ligar ambos os motores
    if gpio.input(leftSensor) == 1 and gpio.input(rightSensor) == 1:
        leftOn()
        rightOn()

    # se o sensor da esquerda estiver ligado, desligar motor da direita (virar esquerda)
    if gpio.input(leftSensor) == 1 and gpio.input(rightSensor) == 0:
        leftOn()
        rightOff()

    # se o sensor da direita estiver ligado, desligar motor da esquerda (virar direita)
    if gpio.input(leftSensor) == 0 and gpio.input(rightSensor) == 1:
        leftOff()
        rightOn()

# limpar os pinos para recomeçar o loop
gpio.cleanup()
