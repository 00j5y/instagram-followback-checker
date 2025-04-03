from colorama import Fore, init
import instaloader
import os

init() ## Initialisation de Colorama

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def login_insta(username,password):
    profile = instaloader.Instaloader()
    profile.login(username,password)

def log():
    username = input(f"\n[{Fore.GREEN}?{Fore.WHITE}] Username : ")
    password = input(f"[{Fore.GREEN}?{Fore.WHITE}] Password : ")

    try:
        login_insta(username, password)
    except:
        print(f"\n[{Fore.RED}!{Fore.WHITE}] Une erreur s'est produite, veuillez essayer a nouveau")
        log()

def main():
    clear()
    print(f"[{Fore.GREEN}!{Fore.WHITE}] Instagram Followback Checker / cred: @00j5Y\n")
    log()
    print(f"\n[{Fore.GREEN}!{Fore.WHITE}] Sucessfully connected\n")

main()