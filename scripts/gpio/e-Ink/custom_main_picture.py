import epd1in54
import time
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def main():
    epd = epd1in54.EPD()
    epd.init(epd.lut_full_update)

    # Open the image
    image = Image.open('./custom_picture_raspberry.png')

    # Convert image to black and white
    image = image.convert('1')
    # Resize the image
    image = image.resize((200, 200), Image.ANTIALIAS)

    # Clear frame memory and set new frame memory
    epd.clear_frame_memory(0xFF)
    epd.set_frame_memory(image, 0, 0)

    # display image
    epd.display_frame()

if __name__ == '__main__':
    main()
