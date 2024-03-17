import sys
import os
import time
from functions import *
sys.dont_write_bytecode = True
from settings import *

class Main:
    def __init__(self) -> None:
        if not os.path.exists("saves"):
            os.makedirs("saves")
        self.main()
    
    def main(self):
        clearScreen()
        selectionScreen(blockLetters(APP_NAME), 
                        ["New game", "Continue Game", "Settings"], 
                        [self.newGame, self.continueGame, self.settings], 
                        inputText="How would you like to proceed: ", 
                        previousPage=False, 
                        color="green",
                        inputTextColor="yellow",
                        titleColor=TITLE_COLOR
                        )
        
    def changeTextSpeed(self):
        clearScreen()
        typeWrite("Current text speed is: " + str(TEXT_SPEED))

        with open("settings.json", "r") as f:
            self.data = json.load(f)
        
        self.textSpeed = float(input("Enter a new text speed (A lower number is a faster text speed, the default is 0.1!): "))
        self.data["textSpeed"] = self.textSpeed

        with open("settings.json", "w") as f:
            json.dump(self.data, f, indent=4)

        clearScreen()
        self.settings()

    def newGame(self):
        clearScreen()
        typeWrite("Welcome to Arvendal, a realm cloaked in mystery and danger.\nIn this text-based RPG, you'll embark on a journey through\ntreacherous landscapes, encountering allies and adversaries\nalike. Will you embrace the path of a valiant knight or wield\nthe arcane arts as a powerful sorcerer? The fate of Arvendal\nlies in your hands. Dare to embark on this enigmatic quest\nand uncover the secrets that await you.", color="cyan")
        typeWrite("\nWhat shall your character be known as: ")
        self.name = input()

    def continueGame(self):
        if not os.listdir("saves"):
            clearScreen()
            typeWrite("No save files found!", color="red")
            time.sleep(3)
            self.main()
        else:
            clearScreen()
            typeWrite("Loading Save...", color="green")

    def settings(self):
        clearScreen()
        selectionScreen("Settings: ", 
                        ["Change Text Speed"], 
                        [self.changeTextSpeed], 
                        self.main, 
                        titleColor=TITLE_COLOR,
                        color="green",
                        inputTextColor="yellow"
                        )

if __name__ == "__main__":
    Main()