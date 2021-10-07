#Brandon Camacho
#Places a randomly colored wool block

import RPi.GPIO as GPIO
import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter = 0
woolColors = [6, 5, 10]

def placeNext(direction):
    global counter
    counter += direction
    if counter > 2:
        counter = 0
    elif counter < 0:
        counter = 2
    mc.setBlock(8, 7, -73, 35, woolColors[counter])

while True:
    time.sleep(0.1)
    if GPIO.input(6) == GPIO.LOW:
        placeNext(1)
    elif GPIO.input(13) == GPIO.LOW:
        placeNext(-1)