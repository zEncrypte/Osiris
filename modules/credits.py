import sys
from time import sleep
def tortuga(_str):
    for letra in _str:
        sys.stdout.write(letra);sys.stdout.flush();sleep(0.03)

def show_credits():
    
    tortuga(f"\nCreditos a: iFeelLucky")
    tortuga(f"\nCreditos a: zEncrypte")
    tortuga(f"\nCreditos a: billythegoat | Pyfade")

def show_help():
    pass
