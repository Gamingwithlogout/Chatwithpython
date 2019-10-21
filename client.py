import socket
from colorama import Fore,Style
import os
import sys
import time as t

###For CLIENT LOGO
os.system('clear')

print(Fore.RED + "\t\t\t WIRELESS MESSAGING SHELL \n\n")
print("\n\t\t CODED BY LogOut . Enforced by PYTHON!" + Style.RESET_ALL)
t.sleep(1)

print("\n\n\t\t\tCONNECTING TO THE SERVER!!!!")
t.sleep(2)


def Main():
        host = '127.0.0.1'
        port = 4444

        s = socket.socket()
        s.connect((host,port))

        message = raw_input(Fore.RED + '\n -> ' + Style.RESET_ALL)
        while message != 'q':
                s.send(message)
                data = s.recv(1024)
                print(Fore.MAGENTA + "\n    FROM SERVER : " + str(data) + Style.RESET_ALL)
                message = raw_input(Fore.RED + '\n -> ' + Style.RESET_ALL)
        s.close()

if __name__ == '__main__':
        Main()
