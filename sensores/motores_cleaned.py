import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  # https://www.google.com/search?q=raspberry+pi+zero+w+gpio&tbm=isch&ved=2ahUKEwjC7KC6-sDsAhU_BLkGHXM7D78Q2-cCegQIABAA&oq=raspberry+pi+zero+w+gpio&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADICCAAyBAgAEB4yBAgAEBgyBAgAEBgyBAgAEBgyBAgAEBgyBAgAEBg6BAgAEENQkQtY1RBgmxRoAHAAeACAAWyIAfIDkgEDMy4ymAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=uK6NX8KwJL-I5OUP8_a8-As&bih=730&biw=1517&safe=strict#imgrc=-zpdx6MHPVA5qM (GPIO dos retangulos externos)
GPIO.cleanup()
# Shield1
# Frontal Esquerdo
in1 = 7
in2 = 16
ena = 11
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)
a = GPIO.PWM(ena, 1000)
a.start(100)
# Frontal Direito
in3 = 13
in4 = 15
enb = 21
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)
b = GPIO.PWM(enb, 1000)
b.start(100)
# Shield2
# Traseiro Esquerdo
in11 = 24
in22 = 26
enaa = 29
GPIO.setup(in11, GPIO.OUT)
GPIO.setup(in22, GPIO.OUT)
GPIO.setup(enaa, GPIO.OUT)
c = GPIO.PWM(enaa, 1000)
c.start(100)
# Traseiro Direito
in33 = 35
in44 = 36
enbb = 37
GPIO.setup(in33, GPIO.OUT)
GPIO.setup(in44, GPIO.OUT)
GPIO.setup(enbb, GPIO.OUT)
d = GPIO.PWM(enbb, 1000)
d.start(100)

# p.ChangeDutyCycle(x) == 60 < x < 100


def stop(x):  # motores desligados
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(in11, GPIO.LOW)
    GPIO.output(in22, GPIO.LOW)
    GPIO.output(in33, GPIO.LOW)
    GPIO.output(in44, GPIO.LOW)
    time.sleep(x)


def FrontalEsquerdaFrente(x):
    GPIO.output(in1, GPIO.HIGH)
    a.ChangeDutyCycle(100)
    time.sleep(x)
    GPIO.output(in1, GPIO.LOW)


def FrontalEsquerdaReverso(x):
    GPIO.output(in2, GPIO.HIGH)
    a.ChangeDutyCycle(100)
    time.sleep(x)
    GPIO.output(in2, GPIO.LOW)


while True:
    stop(1)
    FrontalEsquerdaFrente(5)
    FrontalEsquerdaReverso(5)
    GPIO.cleanup()
