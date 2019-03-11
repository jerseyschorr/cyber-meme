#!/usr/bin/env python
import readchar
import looptest

def cyber():
	while True:

		# Read a key
		key = readchar.readkey()
		if(key == 'a'):
			looptest.do_print()
			print("pressed a...")
		elif(key == 'z'):
			print("pressed z...")
		elif(key == '\r'):
			print("Exiting...")
			break

if __name__ == "__main__":
	cyber()