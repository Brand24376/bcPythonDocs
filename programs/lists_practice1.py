#Brandon Camacho
#Lists Practice 1

#A variable that holds more than one value is a list
groceries = ['bread', 'milk', 'eggs', 'cheese']
#You can get items from their list by their index
print(groceries[0])

#Start an empty list
cart = []

#For every item in my grocery list:
#Add that item to the cart
for item in groceries:
    cart.append(item)
print(cart)

#Random Funny Quotes

#Make a list of "funny" quotes
funnyQuote = ['Among Us', 'Falcon Punch', '$19 Fortnite Card', 'When the imposter is Sus', 'SANS', 'E']
#Generate a random integer
#Make sure to assign random.randint a variable
import random
randomInteger = random.randint(0, 5)
#Use the integer to select one random "funny" quote and print it.
print(funnyQuote[randomInteger])
#Generate a new random quote with button 1
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    if GPIO.input(6) == GPIO.LOW:
        print(funnyQuote[randomInteger])