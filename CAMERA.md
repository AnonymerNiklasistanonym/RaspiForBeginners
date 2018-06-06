# RaspiForBeginners > Camera

Disclaimer: Not everything tested right now, because I do not want to disassemble my infrared camera and therefore will test everything in here not before one week from now (04.05.18)

## 0. Sources with better explanation

- https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

## 1. Get a camera

- Get a compatible camera with the special connection for the Raspberry Pi
- I got the following one (contains also an infrared camera): [Kuman IR camera model (30 Euro)](https://www.amazon.de/gp/product/B01ICNT3HC/ref=oh_aui_detailpage_o02_s00?ie=UTF8&psc=1)

### Infrared camera / Power supply

**If you want to use the IR camera feed you need to assemble the lights and probably get a new or a better power supply!**

For the normal camera a normal USB power supply (for me the power supply of a Kindle Fire HD 8  with **5V 1A**) was enough, but to use the infrared camera not - so I bought a [5V 3A power supply from Aukru (9 Euro)](https://www.amazon.de/gp/product/B01566WOAG/ref=oh_aui_detailpage_o00_s01?ie=UTF8&psc=1) with which I could easily power the IR camera.

## 2. Connect the camera

**Attention: Do not assemble the (infrared) camera, use only the camera, no additional lights that suck too much voltage if you only have a phone "1A" power supply.**

- Simply connect the one end of the wide cable to the camera module so that the cable pins touch the connector pins
- and do the same with the cable and the camera connector on the Raspberry Pi 3
- If not already activated either
  - Open the *Raspberry Pi Configuration Tool* from the main menu (under *Preferences*)
  - Or go into `sudo raspi-config`, `Interfacing Options` and `P1 Camera`
  and activate it

## 3. Test the camera

Just run some very simple python scripts (taken from the first link in this document):

### [camera_preview.py](scripts/camera/camera_preview.py)

```python
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
```

#### [camera_capture.py](scripts/camera/camera_capture.py)

```python
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
```

## 3. Play with the camera

### Take a picture every 5 seconds

```python
camera.start_preview()

# do the following 5 times with i being 1,2,3,4,5
for i in range(5):
    sleep(5)
    camera.capture('./5_second_image_%s.jpg' % i)

camera.stop_preview()
```

### Rotate camera

```python
# rotate camera to a certain degree (default = 0)
camera.rotation = 180

camera.start_preview()
sleep(10)
camera.capture('./test_rotated.jpg')
camera.stop_preview()
```

### Hide camera preview

```python
# set alpha to 'hide' preview - alpha can be 0 to 255
camera.start_preview(alpha=255)
sleep(10)
camera.stop_preview()
```

### Record a video

```python
# set the video framerate
camera.framerate = 15

camera.start_preview()
sleep(10)

# make a 10 second recording
camera.start_recording('./test.mp4')
sleep(10)
camera.stop_recording()

camera.stop_preview()
```

### Add an annotation

```python
camera.start_preview()

# set annotated text size - value should be and between 6 and 160, 32 is default
camera.annotate_text_size = 32

# set text that should be annotated
camera.annotate_text = "Hello world!"

sleep(5)
camera.capture('./text_annotated.jpg')
camera.stop_preview()
```

```python
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.annotate_text = "image #%s" % i
    camera.capture('./5_second_image_%s.jpg' % i)
camera.stop_preview()
```

```python
# --- Important ----------------------------------------
# change header from "from picamera import PiCamera" to
# "from picamera import PiCamera, Color"
# ------------------------------------------------------

camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('red')
camera.annotate_text = " Hello world "
sleep(5)
camera.stop_preview()
```

### Change brightness and contrast

```python
camera.start_preview()
for i in range(100):
    camera.annotate_text = "Brightness: %s" % i
    camera.brightness = i
    sleep(0.1)
camera.stop_preview()
```

```python
camera.start_preview()
for i in range(100):
    camera.annotate_text = "Contrast: %s" % i
    camera.contrast = i
    sleep(0.1)
camera.stop_preview()
```

### Add camera effects

```python
# --- Important -----------------------------------------------------
# You can use camera.image_effect to apply a particular image effect
# Default option: none
# Options: none, negative, solarize, sketch, denoise, emboss,
# oilpaint, hatch, gpen, pastel, watercolor, film, blur, saturation,
# colorswap, washedout, posterise, colorpoint, colorbalance,
# cartoon, deinterlace1, deinterlace2
# -----------------------------------------------------

camera.start_preview()

# apply camera effect
camera.image_effect = 'colorswap'

sleep(5)
camera.capture('/home/pi/Desktop/colorswap.jpg')
camera.stop_preview()
```

```python
camera.start_preview()

# loop over all image effects and view each effect for 5 seconds
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    sleep(5)

camera.stop_preview()
```

### Force exposure/white-balance mode

```python
# --- Important --------------------------------------------------------
# You can use camera.exposure_mode to set the exposure to a preset mode
# Default option: auto
# Options: auto, off, night, nightpreview, backlight, spotlight,
# sports, snow, beach, verylong, fixedfps, antishake, fireworks
# ----------------------------------------------------------------------

camera.start_preview()

# loop over all exposure modes and view each mode for 5 seconds
for exposure in camera.EXPOSURE_MODES:
    camera.exposure_mode = exposure
    camera.annotate_text = "Exposure mode: %s" % exposure
    sleep(5)

camera.stop_preview()
```

```python
# --- Important -------------------------------------------------------------
# You can use camera.awb_mode to set the auto white balance to a preset mode
# Default option: auto
# Options: auto, off, night, nightpreview, backlight, spotlight, sports,
# snow, beach, verylong, fixedfps, antishake, fireworks
# ---------------------------------------------------------------------------

camera.start_preview()

# loop over all white balance modes and view each mode for 5 seconds
for white_balance in camera.AWB_MODES:
    camera.awb_mode  = white_balance
    camera.annotate_text = "Auto white balance mode: %s" % white_balance
    sleep(5)

camera.stop_preview()
```
