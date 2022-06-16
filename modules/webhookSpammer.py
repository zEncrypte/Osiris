import time, requests
from pystyle import Colors, System, Cursor

def spammer():
    System.Title("Webhook Spammer :: Osiris")
    Cursor.HideCursor()

    webhook = input(f"\n {Colors.purple}[{Colors.light_blue}>{Colors.purple}] Webhook Url: {Colors.white}")
    message = input(f" {Colors.purple}[{Colors.light_blue}>{Colors.purple}] Mensaje: {Colors.white}")
    timer = input(f" {Colors.purple}[{Colors.light_blue}>{Colors.purple}] Delay: {Colors.white}")
    print("")

    timeout = time.time() + 1 * float(timer) + 2

    while time.time() < timeout:
        response = requests.post( 
            webhook,
            json = {"content" : message},
            params = {'wait' : True}
        )

        if response.status_code == 204 or response.status_code == 200:
            print(f" {Colors.purple}[{Colors.light_red}+{Colors.purple}] Mensaje enviado{Colors.white}")
        elif response.status_code == 429:
            print(f" {Colors.purple}[{Colors.yellow}-{Colors.purple}] {Colors.yellow}Rate limited {response.json()['retry_after']}{Colors.green}ms{Colors.white}")
            time.sleep(response.json()["retry_after"] / 1000)
        else:
            print(f" {Colors.purple}[{Colors.red}-{Colors.purple}] Error: {response.status_code}")

        time.sleep(.5)
