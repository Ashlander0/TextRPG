import os
#     races -----------------
races = {}
races["Human"] = {"index": "0",
				"race": "Human",
				"Str": 15,
				"End": 16,
				"Dex": 15,
				"Int": 15} 

races["Elf"] = {"index": "1",
				"race": "Elf",
				"Str": 14,
				"End": 14,
				"Dex": 17,
				"Int": 17}
 
races["Orc"] = {"index": "2",
				"race": "Orc",
				"Str": 17,
				"End": 16,
				"Dex": 14,
				"Int": 12}
#     classes ---------------
classes = {}
classes["Warrior"] = {"Str": 2,
					"End": 2,
					"Dex": -1,
					"Int": -2}

classes["Mage"] = {"Str": -2,
					"End": 0,
					"Dex": 1,
					"Int": 2}

classes["Rogue"] = {"Str": -1,
					"End": -1,
					"Dex": 2,
					"Int": 1}


stats = {
	"Strength", 
	"Endurance", 
	"Dexterity", 
	"Intelligence"
}

def raceselect():

	global playerRace
	global playerStr
	global playerEnd
	global playerDex
	global playerInt
	
	os.system('cls')
	print("===============================")
	print("=====  Create  Charactor  =====")
	print("===============================\n")

# display
	racecount = 0
	for x in races:
		racecount = racecount + 1
		print(f"[{racecount}] {x}")

# adjust raceinput		
	raceinput = input("\nSelect your race. ")
	raceinput = int(raceinput) - 1

# set variables
	if races.get(str(raceinput)):
		playerRace = races[str(raceinput)]['race']
		playerStr = races[str(raceinput)]['Str']
		playerEnd = races[str(raceinput)]['End']
		playerDex = races[str(raceinput)]['Dex']
		playerInt = races[str(raceinput)]['Int']
		print(f"You are a {playerRace}, with \n{playerStr} Strength \n{playerEnd} Endurance \n{playerDex} Dexterity, and \n{playerInt} Intelligence")

""" 	if raceinput == "1":
		playerRace = races['Human']['race']
		playerStr = races['Human']['Str']
		playerEnd = races['Human']['End']
		playerDex = races['Human']['Dex']
		playerInt = races['Human']['Int']
		print(f"You are a {playerRace}, with {playerStr} Str, {playerEnd} End, {playerDex} Dex, and {playerInt} Int.")
 """
def classselect():
	global playerRace
	global playerStr
	global playerEnd
	global playerDex
	global playerInt
	global playerClass

	os.system('cls')
	print("===============================")
	print("=====  Create  Charactor  =====")
	print("===============================\n")

# display
	classcount = 0
	for clas in classes:
		classcount = classcount + 1
		print(f'[{classcount}] {clas}')
		#print(f"You are a {playerRace}, with \n{playerStr} Strength \n{playerEnd} Endurance \n{playerDex} Dexterity, and \n{playerInt} Intelligence")

# adjust classinput
	classinput = input("\nSelect your class. ")
	classinput = int(classinput) - 1

# set variables
	if classes.get(str(classinput)):
		playerClass = classes[str(classinput)]
		playerStr = playerStr + classes[classinput]["Str"]
		playerEnd = playerEnd + classes[classinput]["End"]
		playerDex = playerDex + classes[classinput]["Dex"]
		playerInt = playerInt + classes[classinput]["Int"]

print(f"You are a {playerRace} {playerClass}, with: \nStrength: {playerStr} \nEndurance: {playerEnd} \nDexterity: {playerDex} \nIntelligence: {playerInt}")
