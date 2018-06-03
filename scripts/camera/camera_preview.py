#!/usr/bin/env python

"""camera_preview.py: View a 10 second camera preview."""

# import picamera class
from picamera import PiCamera
# import static method to "sleep" for some seconds
from time import sleep

# create a camera object
camera = PiCamera()

# start a camera preview on your screen
camera.start_preview()
# sleep for 10 seconds - which does not stop the preview
sleep(10)
# stop the camera preview on your screen
camera.stop_preview()
