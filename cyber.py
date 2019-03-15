#!/usr/bin/env python
import readchar
import looptest
import matrix
import showpng

def cyber():
    while True:

        # Read a key
        key = readchar.readkey()
        if(key == 'a'):
            print("Starting Matrix")
            matrix.neo()
            print("Stopping Matrix")
        elif(key == 'q'):
            print("Starting Error")
            showpng.run('/home/pi/cyber-mime/error.png')
            print("Stopping Error")
        elif(key == 'z'):
            print("Starting Heart")
            showpng.run('/home/pi/cyber-mime/heart.png')
            print("Stopping Heart")
        elif(key == '\r'):
            print("Exiting...")
            break

if __name__ == "__main__":
    cyber()