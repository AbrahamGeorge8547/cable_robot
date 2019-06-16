
from time import sleep
import RPi.GPIO as GPIO

DIR_M1 = 5       # Direction GPIO Pin
STEP_M1 = 6      # Step GPIO Pin
DIR_M2 = 13       # Direction GPIO Pin
STEP_M2 = 19      # Step GPIO Pin
CW = 1         # Clockwise Rotation
CCW = 0        # Counterclockwise Rotation
SPR = 200       # Steps per Revolution (360 / 1.8)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_M1, GPIO.OUT)
GPIO.setup(STEP_M1, GPIO.OUT)
GPIO.setup(DIR_M2, GPIO.OUT)
GPIO.setup(STEP_M2, GPIO.OUT)
MODE_M1 = (14, 15, 18) # Microstep Resolution GPIO Pins for M1
MODE_M2 = (16, 20, 21) # Microstep Resolution GPIO pins for M2
GPIO.setup(MODE_M1, GPIO.OUT)
GPIO.setup(MODE_M2, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}

GPIO.output(MODE_M1, RESOLUTION['1/32'])
GPIO.output(MODE_M2, RESOLUTION['1/32'])
delay = .005 / 32
def clockwise(step_count, DIR, STEP, ):
    step_count = SPR * step_count
    GPIO.output(DIR, CW)
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)


def counterclockwise(step_count, DIR, STEP, ):
    step_count = SPR * step_count
    GPIO.output(DIR, CCW)
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)