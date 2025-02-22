# loghawk/cli.py
import pyfiglet

def main():

    # Generate the ASCII art text for 'LogHawk'
    ascii_art = pyfiglet.figlet_format("LogHawk")

    # Print the fancy text to the console
    print(ascii_art)
    print("Your Log Analysis Tool")
