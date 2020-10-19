import os
import variables as v

# races
races = {}
races[0] = {"race": "Human",
				"Str": 15,
				"End": 16,
				"Dex": 15,
				"Int": 15} 
races[1] = {"race": "Elf",
				"Str": 14,
				"End": 14,
				"Dex": 17,
				"Int": 17}
races[2] = {"race": "Orc",
				"Str": 17,
				"End": 16,
				"Dex": 14,
				"Int": 12}

# classes
classes = {}
classes[0] = {"title": "Warrior",
				"Str": 2,
				"End": 2,
				"Dex": -1,
				"Int": -2}
classes[1] = {"title": "Mage",
				"Str": -2,
				"End": 0,
				"Dex": 1,
				"Int": 2}
classes[2] = {"title": "Rogue",
				"Str": -1,
				"End": -1,
				"Dex": 2,
				"Int": 1}

# player stats
playerstats = {
	"Race": "",
	"Class": "",
	"Str": 0, 
	"End": 0, 
	"Dex": 0, 
	"Int": 0}

# race selection function
def raceselect():
	os.system('cls')
	print("===============================")
	print("=====  Create  Charactor  =====")
	print("===============================\n")

	# display
	racecount = 0
	for x in races:
		racecount = racecount + 1
		print(f"[{racecount}] {races[x].get("race")}")

	# adjust raceinput		
	raceinput = input("\nSelect your race. ")
	raceinput = int(raceinput) - 1

	# set variables
	if races.get(str(raceinput)):
		playerstats["Race"] = races[raceinput]['race']
		playerstats["Str"] = int(races[str(raceinput)]['Str'])
		playerstats["End"] = races[(raceinput)]['End']
		playerstats["Dex"] = races[str(raceinput)]['Dex']
		playerstats["Int"] = races[str(raceinput)]['Int']
	
# class selection function
def classselect():
	os.system('cls')
	print("===============================")
	print("=====  Create  Charactor  =====")
	print(f"================{playerstats}===============\n")

	# display
	classcount = 0
	for clas in classes:
		classcount = classcount + 1
		print(f'[{classcount}] {clas}')

	# adjust classinput
	classinput = input("\nSelect your class. ")
	classinput = int(classinput) - 1

	# set variables
	if classes.get(str(classinput)):
		playerstats["Class"] = classes[str(classinput)]["title"]
		playerstats["Str"] = playerstats["Str"] + int(races[str(classinput)]['Str'])
		playerstats["End"] = playerstats["End"] + races[(classinput)]['End']
		playerstats["Dex"] = playerstats["Dex"] + races[str(classinput)]['Dex']
		playerstats["Int"] = playerstats["Int"] + races[str(classinput)]['Int']

	print(f"\nYou are a , with: \nStrength:  \nEndurance:  \nDexterity:  \nIntelligence: ")
	print(playerstats["Str"])
