import sys
import os
import time
from art import text2art

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

def typeWrite(text, color="white", speed=0.1):
    for char in text:
        if color.casefold() == "red":
            sys.stdout.write(colors.RED + char + colors.RESET)
        elif color.casefold() == "green":
            sys.stdout.write(colors.GREEN + char + colors.RESET)
        elif color.casefold() == "yellow":
            sys.stdout.write(colors.YELLOW + char + colors.RESET)
        elif color.casefold() == "blue":
            sys.stdout.write(colors.BLUE + char + colors.RESET)
        elif color.casefold() == "magenta":
            sys.stdout.write(colors.MAGENTA + char + colors.RESET)
        elif color.casefold() == "cyan":
            sys.stdout.write(colors.CYAN + char + colors.RESET)
        else:
            sys.stdout.write(colors.WHITE + char + colors.RESET)

        sys.stdout.flush()
        time.sleep(speed)
    print()

def printBlockLetters(text):
    print(text2art(text=text))

def blockLetters(text):
    return text2art(text=text)

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def selectionScreen(title, selections, functions):
    print(title)
    for i, option in enumerate(selections):
        print(f"{i+1}. {option}")
    while True:
        try:
            choice = int(input("Enter your choice: ")) - 1
            if 0 <= choice < len(selections):
                functions[choice]()
                break
            else:
                print("Invalid choice. Please enter a number corresponding to the options.")
        except ValueError:
            print("Invalid input. Please enter a number.")