import sys
from functions import *
sys.dont_write_bytecode = True
from settings import *

class Main:
    def __init__(self) -> None:
        self.main()
    
    def main(self):
        clearScreen()
        printBlockLetters(APP_NAME)
        selectionScreen("", 
                        ["New game", "Continue Game", "Settings"], 
                        [self.newGame, self.continueGame, self.settings], 
                        inputText="How would you like to proceed: ", 
                        previousPage=False, 
                        color="green",
                        inputTextColor="#438525"
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
        pass

    def continueGame(self):
        pass

    def settings(self):
        clearScreen()
        selectionScreen("Settings: ", ["Change Text Speed"], [self.changeTextSpeed], self.main)

if __name__ == "__main__":
    Main()