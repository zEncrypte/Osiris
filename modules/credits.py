import sys
from time import sleep
from pystyle import Colors, Colorate, System, Cursor
def tortuga(_str):
    for letra in _str:
        sys.stdout.write(letra);sys.stdout.flush();sleep(0.03)

def show_credits():
    System.Clear()
    System.Title("End")
    Cursor.HideCursor()
    tortuga(Colorate.Vertical(Colors.purple_to_red, f"""\n Agradecimientos especiales a
    \n :: iFeeLucky ::
    \n :: zEncrypte :: 
    \n :: Y a ti ::
    \n :: Por usar esta herramienta :: 
    \n :: Nos alegra haberte ayudado ::
    \n :: Gracias por usar Osiris :: 
    \n"""))
    exit()
