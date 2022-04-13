from colorama import Fore
import requests
import time


def token():
    token = input(Fore. BLUE + f"\n[>] Token: ")

    print(f" [+] Obteniendo informacion del usuario" + Fore.RESET)
    time.sleep(.5)

    user = requests.get("https://discord.com/api/users/@me", headers = {'Authorization' : token})

    if user.status_code == 401:
        print(Fore.YELLOW + f" [-] Token invalido" + Fore.RESET)
        return

    servers = requests.get("https://discord.com/api/users/@me/guilds", headers = {'Authorization' : token}).json()
    relations = requests.get("https://discord.com/api/v9/users/@me/relationships", headers = {'Authorization' : token}).json()

    user = user.json()

    print(Fore.GREEN + f"\n [+] Token valido")
    print(f" [+] User: {user['username']}#{user['discriminator']} | Email: {user['email']}")
    print(f" [+] Servidores: {len(servers)} | Amigos: {len([i for i in relations if i['type'] == 1])}" + Fore.RESET)

    inp = input(f"\n ¿Quiere descargar informacion adicional? (s/n)")

    if "s" in inp.lower():
        print(f" [+] Este archivo lo puedes encontrar en la carpeta *output*")

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

        with open(f"./output/TokenData {user['username']}#{user['discriminator']}.txt", "w", encoding = "utf-8") as file:
            file.write(
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
    webhook = input(Fore.BLUE + f"\n [>] Webhook Url: " + Fore.RESET)

    print(Fore.GREEN + f" [+] informacion de un webhook" + Fore.RESET)
    time.sleep(.5)

    responce = requests.get(
        webhook
    )

    if responce.status_code != 200:
        print(Fore.YELLOW + f" [!] Webhook invalido" + Fore.RESET)
        return

    responce = responce.json()

    print(Fore.GREEN + f"\n [+] Webhook valido" + Fore.RESET)
    print(f" [+] Nombre: {responce['name']} ID: {responce['id']}")
