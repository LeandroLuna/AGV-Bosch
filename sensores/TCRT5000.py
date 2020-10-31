# importar a biblioteca de controle GPIO
import RPi.GPIO as GPIO
import motores_f
import HCSR04
import time
# definir o mapeamento dos pins para placa
GPIO.setmode(GPIO.BOARD)

# definir os pinos GPIO como input/'entrada'
leftSensor = 7
rightSensor = 10
GPIO.setup(leftSensor, GPIO.IN)
GPIO.setup(rightSensor, GPIO.IN)

# chamar a função para confirmar que os motores estão desligados
motores_f.Parar()
# desligar as mensagens de erro
GPIO.setwarnings(False)

while True:  # Loop principal
    if HCSR04.distance() < 15.0:
        motores_f.Parar()
        for x in range(x, 5, 1):
            print(
                'Objeto detectado em uma distância menor que 15cm. Por favor retirar da trajetoria.')
        time.sleep(10)
    else:
        # se ambos os sensores estiverem desligados, desligar todos os motores
        if GPIO.input(leftSensor) == 0 and GPIO.input(rightSensor) == 0:
            motores_f.Frente_Esquerda_Off()
            motores_f.Frente_Direita_Off()
            motores_f.Tras_Esquerda_Off()
            motores_f.Tras_Direita_Off()
        # se ambos os sensores estiverem ligados, ligar ambos os motores
        if GPIO.input(leftSensor) == 1 and GPIO.input(rightSensor) == 1:
            motores_f.Frente_Esquerda()
            motores_f.Frente_Direita()
            motores_f.Tras_Esquerda()
            motores_f.Tras_Direita()

        # se o sensor da esquerda estiver ligado, desligar motor da direita (virar esquerda)
        if GPIO.input(leftSensor) == 1 and GPIO.input(rightSensor) == 0:
            motores_f.Frente_Esquerda()
            motores_f.Frente_Direita_Off()
            motores_f.Tras_Esquerda()
            motores_f.Tras_Direita_Off()
        # se o sensor da direita estiver ligado, desligar motor da esquerda (virar direita)
        if GPIO.input(leftSensor) == 0 and GPIO.input(rightSensor) == 1:
            motores_f.Frente_Esquerda_Off()
            motores_f.Frente_Direita()
            motores_f.Tras_Esquerda_Off()
            motores_f.Tras_Direita_Off()
    # limpar os pinos para recomeçar o loop
    GPIO.cleanup()
