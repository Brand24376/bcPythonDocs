#Brandon Camacho
#Get blocks

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(6) == GPIO.LOW:
        pos = mc.player.getTilePos()
        blockData = mc.getBlock(pos.x, pos.y - 1, pos.z)
        print(blockData)
        if blockData == 57:
            mc.player.setTilePos(pos.x, pos.y + 20, pos.z)