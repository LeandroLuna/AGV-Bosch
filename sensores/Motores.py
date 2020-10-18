import RPi.GPIO as GPIO
import time

in1 = 14
in2 = 18
en = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(en, 1000)
p.start(25)

while True:
    print("F")
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    p.ChangeDutyCycle(60)
    time.sleep(5)

    print("F OUTRO LADO")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    p.ChangeDutyCycle(100)
    time.sleep(5)

    print("S")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    time.sleep(5)

    # elif x == 'l':
    #    print("low")
    #    p.ChangeDutyCycle(25)
    #    x = 'z'

    # elif x == 'm':
    #    print("medium")
    #    p.ChangeDutyCycle(50)
    #    x = 'z'

    # elif x == 'h':
    #    print("high")
    #    p.ChangeDutyCycle(75)
    #    x = 'z'

    # elif x == 'e':
GPIO.cleanup()
