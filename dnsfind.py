import os
from os import *
from pystyle import *

def alinea():
    print()
    print()
    print()

def exit_mode():
    alinea()
    input('                                       [+] appuyer 3 fois sur entrer pour fermer >>> ')
    input('                                       [+] appuyer 2 fois sur entrer pour fermer >>> ')
    input('                                       [+] appuyer 1 fois sur entrer pour fermer >>> ')
    exit()


banner = '''
                                            _            __ _           _  
                                           | |          / _(_)         | | 
                                         __| |_ __  ___| |_ _ _ __   __| | 
                                        / _` | '_ \/ __|  _| | '_ \ / _` | 
                                       | (_| | | | \__ \ | | | | | | (_| | 
                                        \__,_|_| |_|___/_| |_|_| |_|\__,_| 
'''

print(banner)

alinea()

word = input('                                       [?] Entrer le mot a retrouver >>> ')
alinea()
result = os.system('ipconfig /displaydns | findstr ' + word)

if (result == 1):
    print("                                       [!] Aucune recherche associé")
    exit_mode()

else:
    alinea()
    print(f"                                       [!] Le mot {word} a bien été recherché")
    exit_mode()
