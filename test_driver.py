from time import sleep
import RPi.GPIO as GPIO

DIR = 20       # Direction GPIO Pin
STEP = 21      # Step GPIO Pin
CW = 1         # Clockwise Rotation
CCW = 0        # Counterclockwise Rotation
SPR = 200       # Steps per Revolution (360 / 1.8)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

MODE = (14, 15, 18) # Microstep Resolution GPIO Pins
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}

GPIO.output(MODE, RESOLUTION['1/32'])

delay = .005 / 32
def clockwise(step_count):
    GPIO.output(DIR, CW)
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

sleep(.5)

def Counterclockwise(step_count):
    GPIO.output(DIR, CCW)
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)