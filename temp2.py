from threading import Thread
from time import sleep
import os


def counter():
    i = 0
    while(True):
        sleep(0.8)
        i += 1
        print(i)
        os.system('clear')

def cmd():
    while(True):
        print(f'\x1b[FCommand: {input()}')

Thread(target = counter).start()
Thread(target = cmd).start()


