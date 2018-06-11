#!/usr/bin/env python3


# import packages/modules
from gpiozero import LED
from time import sleep

# "Create" a LED at GPIO pin #4
led = LED(4)

# do the following infinitely
while True:
    print("led on")
    # turn the LED on
    led.on()
    # wait 4 seconds
    sleep(4)
    print("led off")
    # turn the LED off
    led.off()
    # wait 4 seconds
    sleep(4)
