import socket
from colorama import Fore,Style
import os
import sys
import time as t

### For SERVER LOGO
os.system('clear')

print(Fore.RED + "\t\t\t WIRELESS MESSAGING SHELL \n\n")
print("\n\t\t CODED BY LogOut . Enforced by PYTHON!" + Style.RESET_ALL)


def Main():
        host = '127.0.0.1'
        port = 4444

        s = socket.socket()
        s.bind((host,port))

        s.listen(1)
        c, addr = s.accept()
        print("\n\n\t\t CONNECTION FROM : " + str(addr))
        while True:
                data = c.recv(1024)
                if not data:
                        break

                print(Fore.YELLOW + "\n    FROM CLIENT : " + str(data) + Style.RESET_ALL)
                data = raw_input(Fore.RED + '\n -> ' + Style.RESET_ALL)
                c.send(data)

        c.close()

if __name__ == '__main__':
        Main()
