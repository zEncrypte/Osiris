import requests
import time
from colorama import Fore



def spammer():
    webhook = input(Fore.BLUE + f"\n [>] Webhook Url: ")
    message = input(f" [>] Mensaje: ")
    timer = input(f" [>] Cantidad de tiempo del ataque (segundos): " + Fore.RESET)
    print("")

    timeout = time.time() + 1 * float(timer) + 2

    while time.time() < timeout:
        response = requests.post( 
            webhook,
            json = {"content" : message},
            params = {'wait' : True}
        )

        if response.status_code == 204 or response.status_code == 200:
            print(Fore.GREEN + f" [+] Mensaje enviado" + Fore.RESET)
        elif response.status_code == 429:
            print(Fore.YELLOW + f" [~] Rate limited ({response.json()['retry_after']}ms)" + Fore.RESET)
            time.sleep(response.json()["retry_after"] / 1000)
        else:
            print(Fore.RED + f" [-] Codigo de error: {response.status_code}" + Fore.RESET)

        time.sleep(.5)
