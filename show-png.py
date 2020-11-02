#!/usr/bin/env python

import time
import threading
from getch import getch
from sys import exit

try:
    from PIL import Image
except ImportError:
    exit('This script requires the pillow module\nInstall with: sudo pip install pillow')

import unicornhathd


"""Unicorn HAT HD: Show a PNG image!

This basic example shows use of the Python Pillow library.

The tiny 16x16 bosses in lofi.png are from Oddball:
http://forums.tigsource.com/index.php?topic=8834.0

Licensed under Creative Commons Attribution-Noncommercial-Share Alike 3.0
Unported License.


"""

def input_thread(a_list):
    getch()
    a_list.append(True)

def run(imgFile='lofi.png')

    unicornhathd.rotation(0)
    unicornhathd.brightness(0.6)

    width, height = unicornhathd.get_shape()

    img = Image.open(imgFile)

    a_list = []
    threading.Thread(target=input_thread, args=(a_list,)).start()

    while not a_list:
        for o_x in range(int(img.size[0] / width)):
            for o_y in range(int(img.size[1] / height)):

                valid = False
                for x in range(width):
                    for y in range(height):
                        pixel = img.getpixel(((o_x * width) + y, (o_y * height) + x))
                        r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
                        if r or g or b:
                            valid = True
                        unicornhathd.set_pixel(x, y, r, g, b)

                if valid:
                    unicornhathd.show()
                    time.sleep(0.5)

    unicornhathd.off()
