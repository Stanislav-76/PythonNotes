#import ctypes
#kernel32 = ctypes.windll.kernel32
#kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
#print("\033[H\033[J")


from sys import argv
c = argv
print(c)  # ['main.py', '11']

with open('filename.json', 'w') as f:
    print('1', file= f)

import keyboard

while True:
    # if keyboard.is_pressed('left'):
        # print('11111111')
    if keyboard.read_key() == ('left'):#75  97
        print('11111111111')
    if keyboard.is_pressed('right'):#77  100
        print('2222222')
    if keyboard.read_key() == ('g'):
        print('333333')
    if keyboard.read_key() == 'q': #113
        break


# from msvcrt import getwch
# import time
# from msvcrt import getch

# while True:
# n = ord(getch())
# print(n)
# m = msvcrt.getwch()
# print(m)
# print(msvcrt.getwch() == 'M')
# if n == 27:
# break
