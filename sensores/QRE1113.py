# importar a biblioteca de controle GPIO
import RPi.GPIO as gpio

# definir o mapeamento dos pins para placa
gpio.setmode(gpio.BOARD)

# definir os pinos GPIO como output/'saida'
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(19, gpio.OUT)
gpio.setup(21, gpio.OUT)

# definir os pinos GPIO como input/'entrada'
leftSensor = 7
rightSensor = 10
gpio.setup(leftSensor, gpio.IN)
gpio.setup(rightSensor, gpio.IN)


def leftFOn():  # ligar motor esquerdo frontal
    gpio.output(15, 1)


def leftFOff():  # desligar motor esquerdo frontal
    gpio.output(15, 0)


def leftTOn():  # ligar motor esquerdo traseiro
    gpio.output(19, 1)


def leftTOff():  # desligar motor esquerdo traseiro
    gpio.output(19, 0)


def rightFOn():  # ligar motor direito frontal
    gpio.output(13, 1)


def rightFOff():  # desligar motor direito frontal
    gpio.output(13, 0)


def rightTOn():  # ligar motor direito traseiro
    gpio.output(21, 1)


def rightTOff():  # desligar motor direito traseiro
    gpio.output(21, 0)


# desligar todos os motores
def stopAll():
    gpio.output(13, 0)
    gpio.output(15, 0)
    gpio.output(19, 0)
    gpio.output(21, 0)


# chamar a função para confirmar que os motores estão desligados
stopAll()
# desligar as mensagens de perigo
gpio.setwarnings(False)

while True:  # Loop principal
    # se ambos os sensores estiverem desligados, desligar todos os motores
    if gpio.input(leftSensor) == 0 and gpio.input(rightSensor) == 0:
        leftFOff()
        rightFOff()
        leftTOff()
        rightTOff()

    # se ambos os sensores estiverem ligados, ligar ambos os motores
    if gpio.input(leftSensor) == 1 and gpio.input(rightSensor) == 1:
        leftFOn()
        rightFOn()
        leftTOn()
        rightTOn()

    # se o sensor da esquerda estiver ligado, desligar motor da direita (virar esquerda)
    if gpio.input(leftSensor) == 1 and gpio.input(rightSensor) == 0:
        leftFOn()
        rightFOff()
        leftTOn()
        rightTOff()
    # se o sensor da direita estiver ligado, desligar motor da esquerda (virar direita)
    if gpio.input(leftSensor) == 0 and gpio.input(rightSensor) == 1:
        leftFOff()
        rightFOn()
        leftTOff()
        rightTOn()

# limpar os pinos para recomeçar o loop
gpio.cleanup()
