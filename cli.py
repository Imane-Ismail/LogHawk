import pyfiglet
import colorama
from colorama import Fore, Style

def main():
    colorama.init()  # Initialize colorama for Windows support

    # Generate fancy ASCII text
    ascii_art = pyfiglet.figlet_format("LogHawk")
    
    # Print colored text
    print(Fore.CYAN + ascii_art + Style.RESET_ALL)
    print(Fore.GREEN + "Your Log Analysis Tool\n" + Style.RESET_ALL)
