try:
    import pyfiglet
    import subprocess
    import os
    import re
    import sys
    from colorama import * 
    import platform
except ImportError:
    os.system("pip3 install pyfiglet", shell=True)


os.system("cls")

ascii_banner = pyfiglet.figlet_format("Speakup")
print(ascii_banner)
init()
print(Fore.CYAN + " [+] ©Instant Devs Corp. 2020")
print(Fore.CYAN + " [+] Speakup is a text-to-speech program created by Kavin Jindal")
print(Fore.RED + "-----------------------------------------------------")
print(Fore.WHITE + "App Version : 1.1.2")
print(Fore.WHITE + "Detected OS: " + platform.system())
print(Fore.WHITE + "OS Release: " + platform.release())
print(Fore.RED + "-----------------------------------------------------")
print(Fore.CYAN + "Developer : Kavin Jindal from Instant Devs Corp.")

input('\n [=] Press Enter to get Developer Contact')
print("Please wait")
print("Developer : Kavin Jindal from Instant Devs Corp.")
print("Email : kavinsjindal@gmail.com")
print("Github : github.com/kavinjindal")

#print(Style.RESET_ALL)


