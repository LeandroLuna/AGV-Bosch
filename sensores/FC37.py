import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)  # Para numerar os pinos fisicos
chuva = 7  # Define o pino onde estará o sensor de chuva
GPIO.setup(chuva, GPIO.IN)  # Define o pino 7 como INPUT (receber informações)


def itsrainingmen(chuva):
    try:
        # Caso o circuito não esteja completo (0), é sinal de que está chovendo.
        if chuva == 0:
            GPIO.cleanup()  # Limpa as portas GPIO para não entrar em conflito com nenhum sensor
            return 'Está chovendo'
        # Se estiver chovendo o sensor analogico completara o seu circuito (mais informações no README.md sobre os sensores**), ficando com sinal 1, indicando que não está chovendo.
        else:
            GPIO.cleanup()
            return 'Não está chovendo!'
    finally:
        GPIO.cleanup()


print(itsrainingmen(chuva))
