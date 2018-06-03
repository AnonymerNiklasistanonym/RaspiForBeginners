#!/usr/bin/env python

"""camera_capture.py: Take a picture."""

from picamera import PiCamera
from time import sleep

camera = PiCamera()

# set the camera resolution
camera.resolution = (2560, 1920)

camera.start_preview()
sleep(10)

# --- Important ---------------------------------------------------
# It’s important to sleep for at least 2 seconds before capturing,
# to give the sensor time to set its light levels.
# -----------------------------------------------------------------

# capture a picture
camera.capture('./test.jpg')

camera.stop_preview()
