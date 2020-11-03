#!/usr/bin/env python

import colorsys
import time
import math
import threading
from getch import getch
from sys import exit
from datetime import datetime

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit('This script requires the pillow module\nInstall with: sudo pip install pillow')

import unicornhathd

digits = [ # 0
         [[1,1,1,0],
          [1,0,1,0],
          [1,0,1,0],
          [1,0,1,0],
          [1,1,1,0]],
         [[1,0],
          [1,0],
          [1,0],
          [1,0],
          [1,0]]
         ]


def input_thread(a_list):
    getch()
    a_list.append(True)

def clock():
    colours = [tuple([int(n * 255) for n in colorsys.hsv_to_rgb(x, 1.0, 1.0)]) for x in range(1)]


    # Use `fc-list` to show a list of installed fonts on your system,
    # or `ls /usr/share/fonts/` and explore.

    FONT = ('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 8)

    # sudo apt install fonts-droid
    # FONT = ('/usr/share/fonts/truetype/droid/DroidSans.ttf', 12)

    # sudo apt install fonts-roboto
    # FONT = ('/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf', 10)

    unicornhathd.rotation(90)
    unicornhathd.brightness(0.6)


    width, height = unicornhathd.get_shape()

    text_x = width
    text_y = 2


    font_file, font_size = FONT

    font = ImageFont.truetype(font_file, font_size)
    a_list = []
    threading.Thread(target=input_thread, args=(a_list,)).start()

    while not a_list:
        if a_list:
            break

        text_width, text_height = width, 0

        now = datetime.now()
        line = now.strftime("%H:%M")
        w, h = font.getsize(line)
        text_width += w 
        text_height = max(text_height, h)
        print(w, h, text_width, text_height, "\n")

        image = Image.new('RGB', (text_width, max(16, text_height)), (0, 0, 0))
        draw = ImageDraw.Draw(image)

        offset_left = 0

        index = 0
        draw.text((0, text_y), line, colours[index], font=font)

        offset_left += font.getsize(line)[0] + width

        for x in range(width):
            for y in range(height):
                print(x,y)
                pixel = image.getpixel((x, y))
                r, g, b = [int(n) for n in pixel]
                print(width - 1 - x,y,r,g,b)
                unicornhathd.set_pixel(width - 1 - x, y, r, g, b)

        unicornhathd.show()
        time.sleep(5)

    unicornhathd.off()

if __name__ == "__main__":
    clock()
