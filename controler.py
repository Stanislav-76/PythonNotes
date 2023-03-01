import Modul
import View


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