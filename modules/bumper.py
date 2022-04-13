import requests
import time
from colorama import Fore


def bumper():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Authorization' : input(f"\n [>] Token: ")
    }

    id = input(f" [>] ID del canal: ")
    print(f" [+] Use ctrl + c para salir")
    time.sleep(.3)
    print("")

    while True:
        requests.post(
            f"https://discord.com/api/channels/{id}/messages",
            headers = headers,
            json = {"content" : "!d bump"}
        )
        print(Fore.GREEN + f" [+] Mensaje enviado" + Fore.RESET)
        time.sleep(121 * 60)
