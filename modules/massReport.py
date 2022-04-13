from colorama import Fore
import requests
import threading
import time
import random


def start():
    token = input(Fore.BLUE + f"\n [>] Token: ")
    guildId = input(f" [>] ID del servidor: ")
    channelId = input(f" [>] ID del canal: ")
    messageId = input(f" [>] ID del mensaje: ")
    reason = input(f" [>] Razon: " + Fore.RESET)

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
                print(Fore.GREEN + f" [+] Reporte enviado"+ Fore.RESET)
            elif response.status_code == 429:
                print(Fore.YELLOW + f" [~] Limitado, esperando 5 segundos"+ Fore.RESET)
                time.sleep(5)
            elif response.status_code == 401:
                print(Fore.YELLOW +f" [-] Token invalido" + Fore.RESET)
                return
            else:
                print(Fore.RED + f" [-] Error desconocido: {response.status_code}" + Fore.RESET)

    for i in range(500):
        threading.Thread(target = report).start()

if __name__ == '__main__':
    start()
