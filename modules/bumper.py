import requests
from time import sleep
from colorama import Fore


def bumper():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Authorization' : input(f"\n [>] Token: ")
    }

    id = input(f" [>] ID del canal: ")
    print(f" [+] Use ctrl + c para salir")
    sleep(.3)
    print("")

    while True:
        requests.post(
            f"https://discord.com/api/channels/{id}/messages",
            headers = headers,
            json = {"content" : "!d bump"}
        )
        print(Fore.GREEN + f" [+] Mensaje enviado" + Fore.RESET)
        sleep(121 * 60)
