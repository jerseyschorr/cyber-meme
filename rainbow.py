#!/usr/bin/env python

import colorsys
import math
import time
import threading
from getch import getch
import unicornhathd

"""Unicorn HAT HD: Rainbow
OMG MY EYES.
"""

def input_thread(a_list):
    getch()
    a_list.append(True)


def woah():
    unicornhathd.rotation(0)
    unicornhathd.brightness(0.6)

    a_list = []
    threading.Thread(target=input_thread, args=(a_list,)).start()

    step = 0
    while not a_list:
        step += 1
        for x in range(0, 16):
            if a_list:
                break
            for y in range(0, 16):
                if a_list:
                    break
                dx = 7
                dy = 7

                dx = (math.sin(step / 20.0) * 15.0) + 7.0
                dy = (math.cos(step / 15.0) * 15.0) + 7.0
                sc = (math.cos(step / 10.0) * 10.0) + 16.0

                h = math.sqrt(math.pow(x - dx, 2) + math.pow(y - dy, 2)) / sc

                r, g, b = colorsys.hsv_to_rgb(h, 1, 1)

                r *= 255.0
                g *= 255.0
                b *= 255.0

                unicornhathd.set_pixel(x, y, r, g, b)

        unicornhathd.show()
        time.sleep(1.0 / 60)

    unicornhathd.off()
