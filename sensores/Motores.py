import RPi.GPIO as GPIO
import time


in3 = 14
in4 = 18
en = 27

GPIO.setmode(GPIO.BCM)  # https://www.google.com/search?q=raspberry+pi+zero+w+gpio&tbm=isch&ved=2ahUKEwjC7KC6-sDsAhU_BLkGHXM7D78Q2-cCegQIABAA&oq=raspberry+pi+zero+w+gpio&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADICCAAyBAgAEB4yBAgAEBgyBAgAEBgyBAgAEBgyBAgAEBgyBAgAEBg6BAgAEENQkQtY1RBgmxRoAHAAeACAAWyIAfIDkgEDMy4ymAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=uK6NX8KwJL-I5OUP8_a8-As&bih=730&biw=1517&safe=strict#imgrc=-zpdx6MHPVA5qM (GPIO dos retangulos externos)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
p = GPIO.PWM(en, 1000)
p.start(60)  # p.ChangeDutyCycle(x) == 60 < x < 100

GPIO.output(in3, GPIO.LOW)  # motores desligados
GPIO.output(in4, GPIO.LOW)


def Frente():
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    p.ChangeDutyCycle(60)
    time.sleep(5)


def Frente_Reverso():
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    p.ChangeDutyCycle(100)
    time.sleep(5)


# def Parar():
#    GPIO.output(in3, GPIO.LOW)
#    GPIO.output(in4, GPIO.LOW)
#    time.sleep(5)


while True:
    x = input('F = Frente\nFR = Lado contrario a frente\n')
    if x == 'F':
        Frente()
    elif x == 'FR':
        Frente_Reverso()
    # elif x == 'P':
    #    Parar()
    else:
        print('Valor inválido.')
        break
    GPIO.cleanup()
