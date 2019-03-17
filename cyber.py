#!/usr/bin/env python
import readchar
import looptest
import matrix
import showpng
import demo
import os


def cyber():
    matrix.neo()

    while True:

        # Read a key
        key = readchar.readkey()
        if(key == 'a'):
            print("Starting Matrix")
            matrix.neo()
            print("Stopping Matrix")
        elif(key == 'q'):
            print("Starting Error")
            showpng.run('/home/pi/cyber-meme/error.png')
            print("Stopping Error")
        elif(key == 'z'):
            print("Starting Heart")
            showpng.run('/home/pi/cyber-meme/heart.png')
            print("Stopping Heart")
        elif(key == 'k'):
            print("Starting Cool")
            showpng.run('/home/pi/cyber-meme/cool.png')
            print("Stopping Heart")
        elif(key == 'r'):
            print("Style 0 - on")
            demo.go(0)
            print("Style 0 - off")
        elif(key == 't'):
            print("Style 1 - on")
            demo.go(1)
            print("Style 1 - off")
        elif(key == 'y'):
            print("Style 2 - on")
            demo.go(2)
            print("Style 2 - off")
        elif(key == 'u'):
            print("Style 3 - on")
            demo.go(3)
            print("Style 3 - off")
        elif(key == 'i'):
            print("Style 4 - on")
            demo.go(4)
            print("Style 4 - off")
        elif(key == 'x'):
            print("good")
            key2 = readchar.readkey()
            if (key2 == 'x'):
              print("bye")
              os.system('sudo shutdown now')
              break
        elif(key == '\r'):
            print("Exiting...")
            break

if __name__ == "__main__":
    cyber()