import sys
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

def blockLetters(text):
    print(text2art(text=text))
