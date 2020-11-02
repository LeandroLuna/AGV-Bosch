import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  # Para numerar os pinos fisicos
PIN_TRIGGER = 3  # Define o pino do sensor que emitira a onda sonora
PIN_ECHO = 5  # Define o pino do sensor que receberá a onda sonora
GPIO.setup(PIN_TRIGGER, GPIO.OUT)  # Enviar a onda, OUT
GPIO.setup(PIN_ECHO, GPIO.IN)  # Receber a onda, IN


while True:
    try:
        # Garante que o sensor estará desligado, para maior precisão do mensuramento da distancia do objeto
        GPIO.output(PIN_TRIGGER, False)
        print("Esperando o sensor estabilizar")
        time.sleep(2)  # Tempo para o mesmo estabilizar

    # Começo do processo para calcular a distancia, aviso para o usuario
        print("Calculando distância")

    # Liga o sensor que enviara a onda sonora
        GPIO.output(PIN_TRIGGER, True)

        time.sleep(0.00001)  # O sensor requer um de 1 nanosegundo para ativar

        GPIO.output(PIN_TRIGGER, False)  # Desligamos novamente

        while GPIO.input(PIN_ECHO) == 0:  # Checaremos se o receptor da onda está desligado (não recebeu o sinal). Caso não, enviaremos para a variavel o tempo atual até que a condição se torne falsa (ou seja, 1, HIGH)
            tempo_inicial = time.time()  # Tempo de saida da onda
        # Checaremos se o receptor da onda está ligado (recebeu o sinal). Caso sim, gravará em uma variavel o tempo atual até o pin ECHO estiver desligado novamente.
        while GPIO.input(PIN_ECHO) == 1:
            tempo_final = time.time()  # Tempo de chegada da onda

    # Calcula a diferença do tempo de chegada e envio da onda sonora
        duracao_onda = tempo_final - tempo_inicial
        distancia = round(duracao_onda * 17150, 2)  # Calcula a distancia da onda, em centimetros, e arredonda a mesma para printar ao usuario. A velocidade ultrassonica do som: 34300 cm/s. Como so queremos a distancia percorrida até o objeto, devemos dividir esse valor por 2, dando o valor de 17.150cm/s, no qual devemos multiplicar pela duraçao do impulso da onda (diferença entre saida e chegada) para obtermos o resultado da distancia em centimetros
        print(f'Distancia {distancia}')
    finally:
        GPIO.cleanup()  # Limpa as portas GPIO para não entrar em conflito com nenhum sensor
