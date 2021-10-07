#Brandon Camacho
#Build a house with a button press

import RPi.GPIO as GPIO
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buildHouse():
    pos = mc.player.getPos()
    mc.setBlocks(pos.x + 3, pos.y, pos.z + 3, pos.x + 7, pos.y + 4, pos.z + 7, 43, 5)
    mc.setBlocks(pos.x + 4, pos.y + 1, pos.z + 4, pos.x + 6, pos.y + 3, pos.z + 6, 0)
    mc.setBlocks(pos.x + 5, pos.y + 1, pos.z + 7, pos.x + 5, pos.y + 2, pos.z + 7, 107)

while True:
    if GPIO.input(6) == GPIO.LOW:
        buildHouse()