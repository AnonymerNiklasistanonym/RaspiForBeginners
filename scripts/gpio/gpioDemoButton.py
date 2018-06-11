#!/usr/bin/env python3


# import packages/modules
from gpiozero import Button

# "Create" a button at GPIO pin #4
button = Button(4)

# do the following infinitely
while True:
    print("Wait for button to be pressed")
    # wait until the button is pressed
    button.wait_for_press()
    print("Button was pressed")
    button.wait_for_release()
    # wait until the button is released
