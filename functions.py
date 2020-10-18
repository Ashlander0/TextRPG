import os
import variables as v
import charcreate

def mainmenu():
	os.system('cls')
	v.currentscreen = "main"
	print("===================================================")
	print("=============   Welcome to TextRPG   ==============")
	print("===================================================\n\n\n")
	print("Start\t\tSPACE")
	print("Continue\tC")
	print("Help\t\tH")
	print("Quit\t\tX\n")
	command = input("What would you like to do? ")
	if command == " ":
		startgame()
	elif command == "c":
		loadgame()
	elif command == "h":
		helpscreen()
	elif command == "x":
		leave()

def startgame():
	v.currentscreen = "chargen"
	charcreate.raceselect()
	charcreate.classselect()

def loadgame():
	print("Hi")

def helpscreen():
	os.system('cls')
	print("======================================")
	print("===============  Help  ===============")
	print("======================================\n\n\n")
	print("Press S to save the game. Only one save file is supported at a time.")
	print("Press H to access this help screen at any time.")
	command = input("\nPress H again to return to the main menu. ")
	if command != "h":
		command = input("That is not a valid command. Press H to return to the main menu. ")
	if command == "h":
		if v.currentscreen == "main":
			mainmenu()
		
def leave():
	print("Hi")