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

digits = {'0':
         [[1,1,1],
          [1,0,1],
          [1,0,1],
          [1,0,1],
          [1,1,1]],
         '1':
         [[1],
          [1],
          [1],
          [1],
          [1]]
         }


def input_thread(a_list):
    getch()
    a_list.append(True)

def clock():

    unicornhathd.rotation(90)
    unicornhathd.brightness(0.6)

    a_list = []
    threading.Thread(target=input_thread, args=(a_list,)).start()

    width = 16
    height = 5

    while not a_list:
        if a_list:
            break

        now = datetime.now()
        line = now.strftime("%H:%M")
        line = "0"

        c_offset = 0
        for c in range(0, len(line)):
            current = digits[line[c]]
	    for y in range(len(current)):
                if a_list:
                    break
                

            
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
