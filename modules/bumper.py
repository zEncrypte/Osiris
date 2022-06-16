import requests
from time import sleep
from pystyle import Colors, System, Cursor


def bumper():

    System.Title("Auto Bump :: Osiris")
    Cursor.HideCursor()

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Authorization' : input(f"\n {Colors.purple}[{Colors.light_blue}>{Colors.purple}] {Colors.purple} Token: {Colors.white}")
    }

    id = input(f" {Colors.purple}[{Colors.light_blue}>{Colors.purple}] ID del canal: {Colors.white}")
    print(f" {Colors.purple}[{Colors.light_blue}*{Colors.purple}] Use ctrl + c para salir")
    sleep(.3)
    print("")

    while True:
        requests.post(
            f"https://discord.com/api/v9/channels/{id}/messages",
            headers = headers,
            json = {
                "content" : "/d bump"
                }
        )
        print(f" {Colors.purple}[{Colors.light_blue}*{Colors.purple}] Mensaje enviado {Colors.white}")
        sleep(121 * 60)
