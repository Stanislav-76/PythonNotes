import Modul
import View

move = {1:'Создать заметку', 2: 'Проcмотреть заметки', 3:'Изменить заметку', 4:'Удалить заметку', 5:'Выход'}

def start():
    notes = Modul.read()
    while True:        
        n = View.menu()
        if n == 1:
            Modul.create_note(notes)
        if n == 2:
            View.view(notes)
        if n == 3:
            Modul.update_note(notes)
        if n == 4:
            Modul.del_note(notes)
        if n == 5:
            break       
        