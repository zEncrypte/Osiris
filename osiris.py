try:
    import os, sys
    from time import sleep
    from pystyle import Colors, Colorate, System, Write, Cursor, Anime, Center
    from os import name, mkdir, system
    from os.path import isdir
    from pypresence import Presence
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
    
    System.Title("Instalando requisitos...")
    Cursor.HideCursor()
    System.Size(100, 35)
    System.Clear()

    Write.Print(f"\n * Esto tomara unos minutos...", Colors.purple, interval=0.06)
    sleep(2)
    System.Clear()

    Write.Print(f"\n * instalando psutil...\n", Colors.purple, interval=0.03)
    os.system('pip install psutil')

    Write.Print(f"\n * instalando pypiwin32...\n", Colors.purple, interval=0.03)
    os.system('pip install pypiwin32')

    Write.Print(f"\n * instalando pillow...\n", Colors.purple, interval=0.03)
    os.system('pip install pillow')

    Write.Print(f"\n * instalando colorama...\n", Colors.purple, interval=0.03)
    os.system('pip install colorama')

    Write.Print(f"\n * instalando pystyle...\n", Colors.purple, interval=0.03)
    os.system('pip install pystyle')

    Write.Print(f"\n * instalando requests...\n", Colors.purple, interval=0.03)
    os.system('pip install requests')

    Write.Print(f'\n ! Requisitos instalados, reabriendo Osiris...\n', Colors.purple, interval=0.03)
    os.system('python osiris.py')
    sleep(2)
    exit()
    System.Clear()
    

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
        
        System.Clear()
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

        System.Title("Osiris") #Menu principal
        System.Size(100, 35)
        Cursor.HideCursor()
        print(Colorate.Vertical(Colors.blue_to_purple, Center.XCenter(opts))) 
        opcion = input(f" {Colors.purple}[{Colors.light_blue}>{Colors.purple}] Opcion: {Colors.white}")
        data = self.modules[opcion]
        data["function"]()
        input(f"\n{Colors.purple}[{Colors.red}!{Colors.purple}] {Colors.white}Listo, presione enter para continuar.")
        self.main()
if __name__ == '__main__':
    client = Client()
    client.main()
