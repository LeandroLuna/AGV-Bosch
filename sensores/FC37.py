import RPi.GPIO as GPIO


def itsrainingmen():
    try:
        GPIO.setmode(GPIO.BOARD)  # Para numerar os pinos fisicos
        chuva = 7  # Define o pino onde estará o sensor de chuva

        # Define o pino 7 como INPUT (receber informações)
        GPIO.setup(chuva, GPIO.IN)

        # Se estiver chovendo, o sensor analogico completara o seu circuito (mais informações no README.md sobre os sensores**), ficando com sinal 1.
        if chuva == 1:
            print('Está chovendo!')
        # Caso o circuito não esteja completo (0), é sinal de que não está chovendo.
        else:
            print('Não está chovendo!')

    GPIO.cleanup()  # Limpa as portas GPIO para não entrar em conflito com nenhum sensor
    finally:
