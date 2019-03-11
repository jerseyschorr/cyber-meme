import threading
import time
from getch import *

def testThread(num):
    print(num)

def input_thread(a_list):
    getch()
    a_list.append(True)

def do_print():
    a_list = []
    threading.Thread(target=input_thread, args=(a_list,)).start()
    while not a_list:
      time.sleep(.1)
      print("Hi Mom!")

if __name__ == "__main__":
    do_print()