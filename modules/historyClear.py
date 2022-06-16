import sys, requests
from pystyle import Colors, System, Cursor
from time import sleep


def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it) 

    def show(i, user): 
        x = int(size * i / count) 

        file.write(f"{Colors.purple}[{Colors.light_blue}*{Colors.purple}] {Colors.light_green}| {'#' * x}{'.' * ( size - x )}| {i} / {count} | {str(user):<30}              \r{Colors.white}")
        file.flush() 

    if count > 0:

        show(0, "")
        for i, item in enumerate(it):
            show(i+1, item) 
            yield item 

        show(len(it), f"{Colors.light_red} Listo") 

        file.write("\n") 
        file.flush()
    else:
        print(f" {Colors.purple}[{Colors.light_blue}*{Colors.purple}] |{'#' * 60} | {Colors.light_green}0/0 | {Colors.red}Mensajes no encontrados{Colors.white}")

def clear():
    
    System.Title("History Clear :: Osiris")
    Cursor.HideCursor()

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Authorization' : input(f"\n {Colors.purple}[{Colors.light_blue}>{Colors.purple}] Token: {Colors.white}")
    }

    id = input(f" {Colors.purple}[{Colors.light_blue}>{Colors.purple}] ID del canal: {Colors.white}")

    author = requests.get("https://discord.com/api/v9/users/@me", headers = headers).json()["id"]

    allMessages = []

    messages = requests.get(
        f"https://discord.com/api/v9/channels/{id}/messages",
        headers = headers,
        params = {"limit" : 100}
    )

    if messages.status_code != 200:
        print(f" {Colors.purple}[{Colors.red}-{Colors.purple}] {Colors.red}Canal no encontrado {Colors.white}")
        return

    for x in messages.json():
        if x["author"]["id"] == author:
            allMessages.append(x["id"])

    try:
        for i in range(0, 1000, 100):
            messages = messages.json()
            messages = requests.get(
                f"https://discord.com/api/v9/channels/{id}/messages",
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
            f"https://discord.com/api/v9/channels/{id}/messages/{i}",
            headers = headers
        )
        time.sleep(2.5)

        while responce.status_code != 204:
            responce = requests.delete(
                f"https://discord.com/api/v9/channels/{id}/messages/{i}",
                headers = headers
            )
            sleep(2.5)
