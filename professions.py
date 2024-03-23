from functions import *
sys.dont_write_bytecode = True

def knight(saveName):
    if saveName == None:
        raise Exception("No save name provided")
    saveData("saves/" + saveName +".json", "Knight", "Profession")

def archer(saveName):
    if saveName == None:
        raise Exception("No save name provided")
    saveData("saves/" + saveName +".json", "Archer", "Profession")