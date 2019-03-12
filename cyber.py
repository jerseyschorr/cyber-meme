#!/usr/bin/env python
import readchar
import looptest
import matrix

def cyber():
    while True:

        # Read a key
        key = readchar.readkey()
        if(key == 'a'):
            looptest.do_print()
            print("pressed a...")
        elif(key == 'm'):
            print("Starting Matrix")
            matrix.neo()
            print("Stopping Matrix")
        elif(key == '\r'):
            print("Exiting...")
            break

if __name__ == "__main__":
    cyber()