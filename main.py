import functions

def mainmenu():
#	currentscreen = "main"
	print("===================================================")
	print("=============   Welcome to TextRPG   ==============")
	print("===================================================\n\n\n")
	print("Start\t\tSPACE")
	print("Continue\tC")
	print("Help\t\tH")
	print("Quit\t\tX\n")
	command = input("What would you like to do? ")
	if command == " ":
		functions.startgame()
	elif command == "c":
		functions.loadgame()
	elif command == "h":
		functions.helpscreen()
	elif command == "x":
		functions.leave()

mainmenu()
