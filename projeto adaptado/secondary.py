import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  # https://www.google.com/search?q=raspberry+pi+zero+w+gpio&tbm=isch&ved=2ahUKEwjC7KC6-sDsAhU_BLkGHXM7D78Q2-cCegQIABAA&oq=raspberry+pi+zero+w+gpio&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADICCAAyBAgAEB4yBAgAEBgyBAgAEBgyBAgAEBgyBAgAEBgyBAgAEBg6BAgAEENQkQtY1RBgmxRoAHAAeACAAWyIAfIDkgEDMy4ymAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=uK6NX8KwJL-I5OUP8_a8-As&bih=730&biw=1517&safe=strict#imgrc=-zpdx6MHPVA5qM (GPIO dos retangulos externos)

i1 = 7
i2 = 11
ea = 16
GPIO.setup(i1, GPIO.OUT)
GPIO.setup(i2, GPIO.OUT)
GPIO.setup(ea, GPIO.OUT)
a = GPIO.PWM(ea, 1000)
a.start(100)

i3 = 13
i4 = 15
eb = 21
GPIO.setup(i3, GPIO.OUT)
GPIO.setup(i4, GPIO.OUT)
GPIO.setup(eb, GPIO.OUT)
b = GPIO.PWM(eb, 1000)
b.start(100)

i5 = 24
i6 = 26
ec = 29
GPIO.setup(i5, GPIO.OUT)
GPIO.setup(i6, GPIO.OUT)
GPIO.setup(ec, GPIO.OUT)
c = GPIO.PWM(ec, 1000)
c.start(100)

i7 = 33
i8 = 35
ed = 36
GPIO.setup(i7, GPIO.OUT)
GPIO.setup(i8, GPIO.OUT)
GPIO.setup(ed, GPIO.OUT)
d = GPIO.PWM(ed, 1000)
d.start(100)

PIN_TRIGGER = 7
PIN_ECHO = 11
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)


def Parar():
    GPIO.output(i1, GPIO.LOW)
    GPIO.output(i2, GPIO.LOW)
    GPIO.output(i3, GPIO.LOW)
    GPIO.output(i4, GPIO.LOW)
    GPIO.output(i5, GPIO.LOW)
    GPIO.output(i6, GPIO.LOW)
    GPIO.output(i7, GPIO.LOW)
    GPIO.output(i8, GPIO.LOW)


def Frente_Esquerda():
    GPIO.output(i1, GPIO.HIGH)
    a.ChangeDutyCycle(100)


def Frente_Esquerda_Off():
    GPIO.output(i1, GPIO.LOW)
    a.ChangeDutyCycle(0)


def Frente_Esquerda_Reverso():
    GPIO.output(i2, GPIO.HIGH)
    a.ChangeDutyCycle(100)


def Frente_Esquerda_Reverso_Off():
    GPIO.output(i2, GPIO.LOW)
    a.ChangeDutyCycle(0)


def Frente_Direita():
    GPIO.output(i3, GPIO.HIGH)
    b.ChangeDutyCycle(100)


def Frente_Direita_Off():
    GPIO.output(i3, GPIO.LOW)
    b.ChangeDutyCycle(0)


def Frente_Direita_Reverso():
    GPIO.output(i4, GPIO.HIGH)
    b.ChangeDutyCycle(100)


def Frente_Direita_Reverso_Off():
    GPIO.output(i4, GPIO.LOW)
    b.ChangeDutyCycle(0)


def Tras_Esquerda():
    GPIO.output(i5, GPIO.HIGH)
    c.ChangeDutyCycle(100)


def Tras_Esquerda_Off():
    GPIO.output(i5, GPIO.LOW)
    c.ChangeDutyCycle(0)


def Tras_Esquerda_Reverso():
    GPIO.output(i6, GPIO.HIGH)
    c.ChangeDutyCycle(100)


def Tras_Esquerda_Reverso_Off():
    GPIO.output(i6, GPIO.LOW)
    c.ChangeDutyCycle(0)


def Tras_Direita():
    GPIO.output(i7, GPIO.HIGH)
    d.ChangeDutyCycle(100)


def Tras_Direita_Off():
    GPIO.output(i7, GPIO.LOW)
    d.ChangeDutyCycle(0)


def Tras_Direita_Reverso():
    GPIO.output(i8, GPIO.HIGH)
    d.ChangeDutyCycle(100)


def Tras_Direita_Reverso_Off():
    GPIO.output(i8, GPIO.LOW)
    d.ChangeDutyCycle(0)


def distance(PIN_TRIGGER, PIN_ECHO):
    try:
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        print("Esperando o sensor estabilizar")
        time.sleep(2)
        print("Calculando distância")

        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO) == 0:
            tempo_inicial = time.time()
        while GPIO.input(PIN_ECHO) == 1:
            tempo_final = time.time()

        duracao_onda = tempo_final - tempo_inicial
        distancia = round(duracao_onda * 17150, 2)
    finally:
        GPIO.cleanup()
    return distancia
