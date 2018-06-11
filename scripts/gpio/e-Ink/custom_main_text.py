import epd1in54
import time
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def main():
    epd = epd1in54.EPD()
    epd.init(epd.lut_full_update)

    # For simplicity, the arguments are explicit numerical coordinates
    # Clear the whole frame with the code 255
    image = Image.new('1', (epd1in54.EPD_WIDTH, epd1in54.EPD_HEIGHT), 255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(
        '/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 24)

    # Header (black bg, white text)
    draw.rectangle((0, 10, 200, 34), fill=0)
    draw.text((8, 12), 'Hello World!', font=font, fill=255)

    # Text below the header
    draw.text((8, 36), 'e-Paper Demo', font=font, fill=0)

    draw.text((8, 108), datetime.now().strftime('%Y-%m-%d'), font=font, fill=0)
    draw.text((8, 132), datetime.now().strftime('%H:%M:%S'), font=font, fill=0)

    # Clear frame memory and set new frame memory
    epd.clear_frame_memory(0xFF)
    epd.set_frame_memory(image, 0, 0)

    # display frame
    epd.display_frame()

if __name__ == '__main__':
    main()
