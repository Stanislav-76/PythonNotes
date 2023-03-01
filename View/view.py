from os import system
from msvcrt import getwch
import time
# import ctypes
# kernel32 = ctypes.windll.kernel32
# kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


def view(notes):
    key = 1
    if notes == []:
        return
    while True:
        # print("\033[H\033[J") # очистка экрана
        system('clear')       # очистка экрана
        print(f'[{key}/{len(notes)}]', notes[key-1]['title'],
              notes[key-1]['date'], '\n', notes[key-1]['text'])
        print('\nНажмите для просмотра   <- ->, a или d,    для выхода в меню - q')
        key_ch = getwch()
        if key_ch in 'вdM' and key < len(notes):
            key += 1
        if key_ch in 'фaK' and key > 1:
            key -= 1
        if key_ch in 'qй':
            break


def note_list(notes):
    for item in notes:        
        print('{:} {:25} {:}'.format(notes.index(item)+1, item['title'], item['date']))


def menu():
    time.sleep(1)
    system('clear')
    move = {1: 'Создать заметку', 2: 'Прочитать заметки',
            3: 'Изменить заметку', 4: 'Удалить заметку', 5: 'Выход'}
    print('Выберите операцию', move)
    n = getwch() # input()
    if n.isdigit() and n in '12345':
        system('clear')
        return int(n)
    else:
        system('clear')
        print('Введите из предложенных вариантов')