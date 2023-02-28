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
    View.note_list(notes)
    print('Введите номер заметки которую нужно изменить')
    index = input()
    if index.isdigit() and int(index) - 1 < len(notes):
        print('Введите новый текст заметки')
        notes[int(index)-1]['text'] = input()
        notes[int(index)-1]['date'] = datetime.now().strftime("%Y-%m-%d %H.%M")
        save(notes)
        print(f'\nЗаметка {int(index)} обновлена')
    else:
        print('Введен неверный номер заметки')


def del_note(notes):
    View.view(notes)
    print('Введите номер заметки которую нужно удалить')
    index = input()
    if index.isdigit() and int(index)-1 < len(notes):
        del notes[int(index)-1]
        save(notes)
        print(f'Заметка {int(index)} удалена')
    else:
        print('Введен неверный номер заметки')
