from colorama import Fore
import requests
import time
import sys


def fetch_data():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Authorization' : input(Fore.BLUE + f"\n [>] Token: " + Fore.RESET)
    }

    guildId = input(Fore.BLUE + f" [>] ID del servidor: "+ Fore.RESET)

    response = requests.get(
        f"https://discord.com/api/guilds/{guildId}",
        headers = headers,
        params = {"with_counts" : True}
    ).json()

    owner = requests.get(
        f"https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}",
        headers = headers,
        params = {"with_counts" : True}
    ).json()

    print(f"""
    Nombre del servidor: {response['name']} ~ {response['id']}
    URL del icono: https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
    Cantidad aproximada de miembros: {response['approximate_member_count']}
    Owner: {owner['user']['username']}#{owner['user']['discriminator']} ~ {response['owner_id']}
    Region: {response['region']}
    Invitacion personalizada: {response['vanity_url_code']}
""")

if __name__ == '__main__':
    fetch_data()
