import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = r"""
   ███████╗███████╗ ██████╗██╗    ██╗███████╗██╗  ██╗███████╗███╗   ██╗
   ██╔════╝██╔════╝██╔════╝██║    ██║██╔════╝╚██╗██╔╝██╔════╝████╗  ██║
   ███████╗█████╗  ██║     ██║ █╗ ██║█████╗   ╚███╔╝ █████╗  ██╔██╗ ██║
   ╚════██║██╔══╝  ██║     ██║███╗██║██╔══╝   ██╔██╗ ██╔══╝  ██║╚██╗██║
   ███████║███████╗╚██████╗╚███╔███╔╝███████╗██╔╝ ██╗███████╗██║ ╚████║
   ╚══════╝╚══════╝ ╚═════╝ ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝

              {Fore.CYAN}A R S E N A L{Style.RESET_ALL}
 {Fore.CYAN}Personal cybersecurity toolkit repository{Style.RESET_ALL}
    """
    print(banner)

def main():
    clear_screen()
    print_banner()

if __name__ == "__main__":
    main()
