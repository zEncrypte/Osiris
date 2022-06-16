import random, time, threading, requests
from pystyle import Colors, System, Cursor

def start():

    System.Title("Mass Report :: Osiris")
    Cursor.HideCursor()

    token = input(Fore.BLUE + f"\n {Colors.purple}[{Colors.light_blue}>{Colors.purple}] Token: {Colors.white}")
    guildId = input(f" {Colors.purple}[{Colors.light_blue}>{Colors.purple}] ID del servidor: {Colors.white}")
    channelId = input(f" {Colors.purple}[{Colors.light_blue}>{Colors.purple}] ID del canal: {Colors.white}")
    messageId = input(f" {Colors.purple}[{Colors.light_blue}>{Colors.purple}] ID del mensaje: {Colors.white}")
    reason = input(f" {Colors.purple}[{Colors.light_blue}>{Colors.purple}] Razon: {Colors.white}")

    headers = {
        "Content-Type" : "application/json",
        "Authorization" : token,
        "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"
    }

    payload = {"guild_id" : guildId, "channel_id" : channelId, "message_id" : messageId, "reason" : reason}

    def report():
        while True:
            response = requests.post(
                'https://discord.com/api/v9/report',
                headers = headers,
                json = payload
            )
            if response.status_code == 201:
                print(f" {Colors.purple}[{Colors.light_red}*{Colors.purple}] {Colors.red}Reporte enviado{Colors.white}")
            elif response.status_code == 429:
                print(f" {Colors.purple}[{Colors.yellow}~{Colors.purple}] {Colors.yellow}Limitado, esperando 5 segundos{Colors.white}")
                time.sleep(5)
            elif response.status_code == 401:
                print(Fore.YELLOW +f" {Colors.purple}[{Colors.red}-{Colors.purple}]{Colors.red} Token invalido{Colors.white}")
                return
            else:
                print(Fore.RED + f" {Colors.purple}[{Colors.red}-{Colors.purple}]{Colors.red} Error: {response.status_code}{Colors.white}")

    for i in range(500):
        threading.Thread(target = report).start()

if __name__ == '__main__':
    start()
