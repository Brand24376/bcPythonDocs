#Brandon Camacho

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
coordinates = mc.player.getTilePos()
#Use a module for requesting data onlie
import requests

#Use a module to control time
import time

#Setup for buttons and leds
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering

#Set up each pin number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Start an infinite loop
while True:
    #Wait for one second
    time.sleep(1)
    #Check the first button
    if GPIO.input(6) == GPIO.LOW:
        mc.postToChat("Button 6 was pressed(Thumbs Up)")
        requests.get("http://192.168.10.53:5000/tutd?thumb=up")
    elif GPIO.input(13) == GPIO.LOW:
        mc.postToChat("Button 13 was pressed(You have been teleported)")
        mc.player.setTilePos(+0,+100,+0)
    elif GPIO.input(19) == GPIO.LOW:
        mc.postToChat(coordinates)
    elif GPIO.input(26) == GPIO.LOW:
        mc.postToChat("Button 26 was pressed(Oops)")
        requests.get("http://192.168.10.53:5000/tutd?thumb=oops")