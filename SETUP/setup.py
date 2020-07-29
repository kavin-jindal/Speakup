try:
    import pyfiglet
    import subprocess
    import os
    import re
except ImportError:
    os.system("pip3 install pyfiglet")

os.system("cls")
ascii_banner = pyfiglet.figlet_format("Speakup Setup")
print(ascii_banner)
input("\n[+] Press enter to start the setup >> ")

print("\n[+] Please wait, Initializing setup.py")
print("\n\n\t[+] Installing pyttsx3")
os.system("pip3 install pyttsx3")
print("\n[+] Setup was completed successfully! You can start the program.")