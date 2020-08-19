try:
    import pyfiglet
    import subprocess
    import os
    import re
    from colorama import * 
except ImportError:
    os.system("pip3 install pyfiglet", shell=True)


os.system("cls")

ascii_banner = pyfiglet.figlet_format("Welcome to Speakup")
print(ascii_banner)
init()
print(Fore.YELLOW + " [+] Speakup is a text-to-speech program")
print(Style.RESET_ALL)
input("\n[+] Press Enter to start the program >> ")
os.system("pip install pyttsx3")
os.system("pip install pillow")

os.system("python menu.py")

