import requests
import sys

from colorama import Fore
from time import sleep


def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it) 

    def show(i, user): 
        x = int(size * i / count) 

        file.write(Fore.GREEN + f"[+] | {'#' * x}{'.' * ( size - x )}| {i} / {count} | {str(user):<30}              \r" + Fore.RESET)
        file.flush() 

    if count > 0:

        show(0, "")
        for i, item in enumerate(it):
            show(i+1, item) 
            yield item 

        show(len(it), "Listo") 

        file.write("\n") 
        file.flush()
    else:
        print(Fore.RED + f" [+] |{'#' * 60} | 0/0 | Mensajes no encontrados" + Fore.RESET)

def clear():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Authorization' : input(Fore.BLUE + f"\n [>] Token: " + Fore.RESET)
    }

    id = input(Fore.BLUE + f" [>] ID del canal: " + Fore.RESET)

    author = requests.get("https://discord.com/api/users/@me", headers = headers).json()["id"]

    allMessages = []

    messages = requests.get(
        f"https://discord.com/api/channels/{id}/messages",
        headers = headers,
        params = {"limit" : 100}
    )

    if messages.status_code != 200:
        print(Fore.RED + f" [-] Canal no encontrado" + Fore.RESET)
        return

    for x in messages.json():
        if x["author"]["id"] == author:
            allMessages.append(x["id"])

    try:
        for i in range(0, 1000, 100):
            messages = messages.json()
            messages = requests.get(
                f"https://discord.com/api/channels/{id}/messages",
                headers = headers,
                params = {"limit" : 100, "before" : messages[-1]["id"]}
            )
            if messages.status_code != 200:
                break

            for x in messages.json():
                if x["author"]["id"] == author:
                    allMessages.append(x["id"])
    except IndexError:
        pass

    for i in progressbar(allMessages, "", 60):
        responce = requests.delete(
            f"https://discord.com/api/channels/{id}/messages/{i}",
            headers = headers
        )
        time.sleep(2.5)

        while responce.status_code != 204:
            responce = requests.delete(
                f"https://discord.com/api/channels/{id}/messages/{i}",
                headers = headers
            )
            sleep(2.5)
