import sys, requests
from time import sleep
from pystyle import Colors, Write, Cursor, System

def tortuga(_str): # slooow
    for letra in _str:
        sys.stdout.write(letra);sys.stdout.flush();sleep(0.04)

def token():
    System.Title('Token Checker :: Osiris')
    Cursor.HideCursor()
    token = input(f"\n {Colors.purple}[{Colors.light_blue}>{Colors.purple}] Token: {Colors.white}")

    tortuga(f"\n {Colors.purple}[{Colors.light_red}*{Colors.purple}] Obteniendo informacion del usuario ")

    sleep(.5)

    user = requests.get("https://discord.com/api/users/@me", headers = {'Authorization' : token})

    if user.status_code == 401:
        Write.Print(f"\n ! Token invalido", Colors.red, interval=0.05)
        return

    servers = requests.get("https://discord.com/api/users/@me/guilds", headers = {'Authorization' : token}).json()
    relations = requests.get("https://discord.com/api/v9/users/@me/relationships", headers = {'Authorization' : token}).json()

    user = user.json()
    print(f"\n {Colors.purple}[{Colors.light_red}*{Colors.purple}] Token valido{Colors.reset}")
    print(f" {Colors.purple}[{Colors.light_red}*{Colors.purple}] User: {user['username']}#{user['discriminator']} | Email: {user['email']}")
    print(f" {Colors.purple}[{Colors.light_red}*{Colors.purple}] Servidores: {len(servers)} | Amigos: {len([i for i in relations if i['type'] == 1])}{Colors.reset}")

    inp = Write.Input(f"\n ¿Quiere descargar informacion adicional? (s/n) ", Colors.purple, interval=0.04)

    if "s" in inp.lower():
        print(f"\n {Colors.purple}[{Colors.light_red}*{Colors.purple}] Este archivo lo puedes encontrar en esta carpeta")

        serversOT = ""
        for i in servers:
            serversOT += f"Nombre: {i['name']}\nID: {i['id']} Owner: {i['owner']}\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"

        relationsOT = ""
        for i in relations:
            if i['type'] == 1:
                relationsOT += f"Amigo: {i['user']['username']}#{i['user']['discriminator']} ID: {i['user']['id']}\n"
            elif i['type'] == 2:
                relationsOT += f"Bloqueados: {i['user']['username']}#{i['user']['discriminator']} ID: {i['user']['id']}\n"
            elif i['type'] == 3:
                relationsOT += f"Incomming: {i['user']['username']}#{i['user']['discriminator']} ID: {i['user']['id']}\n"
            elif i['type'] == 4:
                relationsOT += f"Outgoing: {i['user']['username']}#{i['user']['discriminator']} ID: {i['user']['id']}\n"

        if user['avatar'] is not None:
            avatar = f"https://cdn.discordapp.com/avatars/{user['id']}/{user['avatar']}.png"
        else:
            avatar = "Sin avatar"

        with open(f" {user['username']}#{user['discriminator']}.txt", "w", encoding = "utf-8") as f:
            f.write(
    f"""~~~~~~~~~~~ Informacion del Usuario ~~~~~~~~~~~
    Usuario: {user['username']}#{user['discriminator']}
    ID: {user['id']}
    Email: {user['email']}
    Telefono: {user['phone']}
    Token: {token}
    Avatar: {avatar}
    2fA: {user['mfa_enabled']}
    Lenguaje: {user['locale']}

    ~~~~~~~~~~~ Informacion de servidores ~~~~~~~~~~~
    {serversOT}
    ~~~~~~~~~~~ Informacion de amigos ~~~~~~~~~~~
    {relationsOT}""")

def webhook():

    System.Title('Webhook Checker :: Osiris')
    Cursor.HideCursor()
    webhook = input(f"\n {Colors.purple}[{Colors.light_blue}>{Colors.purple}] Webhook Url: {Colors.white}")
    print(f"\n {Colors.purple}[{Colors.light_red}*{Colors.purple}] Informacion de la webhook{Colors.white}")
    sleep(.5)

    responce = requests.get(
        webhook
    )

    if responce.status_code != 200:
        print(f" {Colors.purple}[{Colors.red}-{Colors.purple}]{Colors.red} Webhook invalido")
        return
    responce = responce.json()
    print(f" {Colors.purple}[{Colors.light_red}*{Colors.purple}] Webhook valido")
    print(f"\n {Colors.purple}[{Colors.light_red}*{Colors.purple}] Nombre: {Colors.orange}{responce['name']}\n {Colors.purple}[{Colors.light_red}*{Colors.purple}] ID:{Colors.orange} {responce['id']}{Colors.white}")
