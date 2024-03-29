import sys
sys.dont_write_bytecode = True
import os
import time
from art import text2art
from settings import *

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

def typeWrite(text, color="white", speed=TEXT_SPEED):
    if color.startswith("#") and len(color) == 7:
        color_code = f"\033[38;2;{int(color[1:3], 16)};{int(color[3:5], 16)};{int(color[5:], 16)}m"
    else:
        color_code = getattr(Color, color.upper(), Color.WHITE)
    
    for char in text:
        sys.stdout.write(color_code + char + Color.RESET)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def printBlockLetters(text):
    print(text2art(text=text))

def blockLetters(text):
    return text2art(text=text)

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def selectionScreen(title, selections, functions, previousPageFunction=None, inputText="Enter your choice: ", 
                    previousPage=True, color="white", inputTextColor="white", titleColor="white", previousTextColor="white",
                    functionInput=None):
    if titleColor.startswith("#") and len(titleColor) == 7:
        title_color_code = f"\033[38;2;{int(titleColor[1:3], 16)};{int(titleColor[3:5], 16)};{int(titleColor[5:], 16)}m"
    else:
        title_color_code = getattr(Color, titleColor.upper(), Color.WHITE)

    print(title_color_code + title + Color.RESET)

    for i, option in enumerate(selections):
        typeWrite(f"{str(i + 1)}. {option}", color=color)
    if previousPage:
        typeWrite("B. Previous Page", color=previousTextColor)
    while True:
        try:
            typeWrite("\n" + inputText, inputTextColor)
            choice = input()
            if choice == "b".casefold():
                previousPageFunction()
                break
            elif 0 <= int(choice) - 1 < len(selections):
                if functionInput != None:
                    functions[int(choice) - 1](functionInput)
                else:
                    functions[int(choice) - 1]()
                break
            else:
                typeWrite("Invalid choice. Please enter a number corresponding to the options.")
        except ValueError:
            typeWrite("Invalid input. Please enter a number.")

def saveData(saveFile, saveData, key):
    with open(saveFile, "r") as f:
        data = json.load(f)

    data[key] = saveData

    with open(saveFile, "w") as f:
        json.dump(data, f, indent=4)