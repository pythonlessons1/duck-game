# MADE BY  MG#1583
# OPOIOS PEI OTI EINAI DIKO TOU EINAI CLOWN ;)
# https://github.com/pythonlessons1

from time import sleep
import os
import colorama
from colorama import Back, Fore, Style
os.system('title Duck Game')
colorama.init()
list = []
def Menu():
    print(Fore.CYAN + '''
██████╗ ██╗   ██╗ ██████╗██╗  ██╗     ██████╗  █████╗ ███╗   ███╗███████╗
██╔══██╗██║   ██║██╔════╝██║ ██╔╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ██║██║   ██║██║     █████╔╝     ██║  ███╗███████║██╔████╔██║█████╗  
██║  ██║██║   ██║██║     ██╔═██╗     ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
██████╔╝╚██████╔╝╚██████╗██║  ██╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝                                                             


[1] Pick up the duck       [2] Fuck the duck       [3] Unpick the duck


''')
    ans=input('what are u gonna do? ')
    if ans == '1':
        if 's' not in list:
            print('Picking up...')
            sleep(2)
            print('Picked up the duck!')
            list.append('s')
            sleep(2)
            os.system('cls')
            Menu()
    elif ans == '2':
        if 's' not in list:
            print('You are not holding the duck!')
            sleep(1.5)
            os.system('cls')
            Menu()
        else:
            print('Fucking.')
            os.system('cls')
            sleep(0.10)
            print('Fucking..')
            os.system('cls')
            sleep(0.10)
            print('Fucking...')
            os.system('cls')
            sleep(0.10)
            print('Fucking.')
            os.system('cls')
            sleep(0.10)
            print('Fucking..')
            os.system('cls')
            sleep(0.10)
            print('Fucking...')
            os.system('cls')
            sleep(0.10)
            print('Fucking.')
            os.system('cls')
            sleep(0.10)
            print('Fucking..')
            os.system('cls')
            sleep(0.10)
            print('Fucking...')
            os.system('cls')
            sleep(0.10)
            print('Fucking.')
            os.system('cls')
            sleep(0.10)
            print('Fucking..')
            os.system('cls')
            sleep(0.10)
            print('Fucking...')
            os.system('cls')
            sleep(0.15)
            print('AHH.. Duck got fucked, finally..')
            sleep(2)
            os.system('cls')
            Menu()
    elif ans == '3':
        if 's' not in list:
            print('You are not holding the duck!')
            sleep(1.5)
            os.system('cls')
            Menu()
        else:
            list.remove('s')
            print('Nice! You let the duck down!')
            sleep(2)
            os.system('cls')
            Menu()
    else:
        print('Invalid option!')
        sleep(1.5)
        os.system('cls')
        Menu()
Menu()