import os
from os import *
from pystyle import *

System.Size(150, 40)

def alinea():
    print()
    print()
    print()

def exit_mode():
    alinea()
    input(Colorate.Horizontal(Colors.blue_to_red, '                                       [+] appuyer 3 fois sur entrer pour fermer >>> ', 1))
    input(Colorate.Horizontal(Colors.blue_to_red, '                                       [+] appuyer 2 fois sur entrer pour fermer >>> ', 1))
    input(Colorate.Horizontal(Colors.blue_to_red, '                                       [+] appuyer 1 fois sur entrer pour fermer >>> ', 1))
    exit()


banner = '''
                                            _            __ _           _  
                                           | |          / _(_)         | | 
                                         __| |_ __  ___| |_ _ _ __   __| | 
                                        / _` | '_ \/ __|  _| | '_ \ / _` | 
                                       | (_| | | | \__ \ | | | | | | (_| | 
                                        \__,_|_| |_|___/_| |_|_| |_|\__,_| 
'''

print(Colorate.Horizontal(Colors.blue_to_red, banner, 1))

alinea()

word = input(Colorate.Horizontal(Colors.blue_to_red, '                                       [?] Entrer le mot a retrouver >>> ', 1))
alinea()
result = os.system('ipconfig /displaydns | findstr ' + word)

if (result == 1):
    print(Colorate.Horizontal(Colors.blue_to_red, "                                       [!] Aucune recherche associé", 1))
    exit_mode()

else:
    alinea()
    print(Colorate.Horizontal(Colors.green_to_red, f"                                       [!] Le mot {word} a bien été recherché", 1))
    exit_mode()