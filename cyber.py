#!/usr/bin/env python
# -*- coding: utf-8 -*-
import readchar
import looptest
import matrix
import showpng
import demo
import clockText
import scrollText
import heartbeats
import rainbow
import os

def cyber():
    matrix.neo()

    while True:

        # Read a key
        key = readchar.readkey()
        if(key == 'q'):
            print("Starting Error")
            showpng.run('/home/pi/cyber-meme/error.png')
            print("Stopping Error")
        elif(key == 'a'):
            print("Starting Cool")
            showpng.run('/home/pi/cyber-meme/cool.png')
            print("Stopping Cool")
        elif(key == 'z'):
            print("Starting Matrix")
            matrix.neo()
            print("Stopping Matrix")
        elif(key == 'w'):
            print("Starting Heart")
            heartbeats.beat()
            print("Stopping Heart")
        elif(key == 'e'):
            text = "Happy Purim!"
            clockText.clockText(text, (0,0,255))
        elif(key == 's'):
            text = ur"   חמש  םירופ  גח"
            scrollText.scrollText(text, 'he', True)
        elif(key == 'x'):
            text = ur"   ハッピープリム"
            scrollText.scrollText(text, 'jp')
        elif(key == 'f'):
            print("Style 1 - on")
            demo.go(1)
            print("Style 1 - off")
        elif(key == 'r'):
            print("Rainbow on")
            rainbow.woah()
            print("Rainbow off")
        elif(key == 'v'):
            print("Style 2 - on")
            demo.go(2)
            print("Style 2 - off")
        elif(key == 'd'):
            print("Style 3 - on")
            demo.go(3)
            print("Style 3 - off")
        elif(key == 'c'):
            print("Style 4 - on")
            demo.go(4)
            print("Style 4 - off")
        elif(key == 'm'):
            print("good")
            key2 = readchar.readkey()
            if (key2 == 'm'):
              print("bye")
              os.system('sudo shutdown now')
              break
        elif(key == '\r'):
            print("Exiting...")
            break
        else:
            print("Unknown Key %c" % key)

if __name__ == "__main__":
    cyber()
