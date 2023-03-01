import json
from datetime import datetime
import View


def read():
    try:
        with open('notes.json') as data:
            notes = json.loads(data.read())
        return notes
    except:
        return []


def save(notes):
    with open('notes.json', 'w') as data:
        json.dump(notes, data, indent=4)


def create_note(notes):
    title = input('Введите имя заметки: \n')
    text = input('Введите текст заметки: \n')
    note = {'title': title, 'date': datetime.now().strftime("%Y-%m-%d %H.%M"), 'text': text}
    notes.append(note)
    print('\nЗаметка создана')
    save(notes)

def update_note(notes):
    lst = sort_date(notes)
    View.note_list(lst)
    print('Введите номер заметки которую нужно изменить')
    index = input()
    if index.isdigit() and int(index) - 1 < len(notes):
        print('Введите новый текст заметки')
        notes[notes.index(lst[int(index)-1])]['text'] = input()
        notes[notes.index(lst[int(index)-1])]['date'] = datetime.now().strftime("%Y-%m-%d %H.%M")
        save(notes)
        print(f'\nЗаметка {int(index)} обновлена')
    else:
        print('Введен неверный номер заметки')

def del_note(notes):
    lst = sort_date(notes)
    View.note_list(lst)
    print('Введите номер заметки которую нужно удалить')
    index = input()
    if index.isdigit() and int(index)-1 < len(notes):
        del notes[notes.index(lst[int(index)-1])]
        save(notes)
        print(f'Заметка {int(index)} удалена')
    else:
        print('Введен неверный номер заметки')

def sort_date(notes):
    lst = []
    notes_sort = []
    for note in notes:
        lst.append([note['date'], note['title'], notes.index(note)])
    lst.sort()
    index_lst = [x[2] for x in lst]
    for index in index_lst:
        notes_sort.append(notes[index])
    return notes_sort