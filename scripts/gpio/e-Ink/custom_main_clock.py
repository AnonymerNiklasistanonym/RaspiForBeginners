import epd1in54
from time import sleep
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


def drawImage():
    epd = epd1in54.EPD()
    epd.init(epd.lut_full_update)

    # For simplicity, the arguments are explicit numerical coordinates
    # Clear the whole frame with the code 255
    image = Image.new('1', (epd1in54.EPD_WIDTH, epd1in54.EPD_HEIGHT), 255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(
        '/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 50)

    draw.rectangle((0, 0, 200, 100), fill=0)
    draw.text((15, 25), datetime.now().strftime('%d.%m.'), font=font, fill=255)
    draw.text((20, 125), datetime.now().strftime('%H:%M'), font=font, fill=0)

    # Clear frame memory and set new frame memory
    epd.clear_frame_memory(0xFF)
    epd.set_frame_memory(image, 0, 0)

    # display frame
    epd.display_frame()

    # save current display image
    image.save("current_image.png", "PNG")


def main():
    while True:
        # draw image with current time
        drawImage()
        # sleep until the next minute
        sleep(60 - datetime.now().second)


if __name__ == '__main__':
    main()
