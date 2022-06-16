import sys, time, requests
from pystyle import Colors, System, Cursor


def fetch_data():
    System.Title("Server Lookup :: Osiris")
    Cursor.HideCursor()
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Authorization' : input(f"\n {Colors.purple}[{Colors.light_blue}>{Colors.purple}] Token: {Colors.white}")
    }

    guildId = input(f" {Colors.purple}[{Colors.light_blue}>{Colors.purple}] ID del servidor: {Colors.white}")

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
    {Colors.purple}Nombre del servidor: {Colors.orange}{response['name']} {Colors.light_blue}~{Colors.orange} {response['id']}
    {Colors.purple}Icono del servidor: {Colors.orange}https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
    {Colors.purple}Cantidad aproximada de miembros: {Colors.orange}{response['approximate_member_count']}
    {Colors.purple}Propietario: {Colors.orange}{owner['user']['username']}{Colors.light_blue}#{Colors.orange}{owner['user']['discriminator']} {Colors.light_blue}~{Colors.orange} {response['owner_id']}
    {Colors.purple}Region: {Colors.orange}{response['region']}
    {Colors.purple}Invitacion personalizada: {Colors.orange}{response['vanity_url_code']}
{Colors.white}""")

if __name__ == '__main__':
    fetch_data()
