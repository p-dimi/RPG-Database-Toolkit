import dice
import math
import json
import os
from NPC_Maker_Database import database

# load up and initialize the RQ database
db = database()

# input which npcs to generate
chosen_race = str(input('Which race to generate?: '))
chosen_quantity = int(input('How many?: '))
# whether to generate JSON or not
json_generate = str(input('Generate JSON? (y / n): '))
json_generate = json_generate.upper()

# class definition
class NPC_Maker:
    def __init__(self, database):
        self.database = database.get("races")
    # race and difficulty can be strings or lists of strings
    def roll_stats(self, race = "BROO"):
        # initialize the dictionary of stats
        stats = {}
        # roll the stats and append to the dictionary
        stats["STR"] = dice.roll(self.database[race]['STATS']['STR']+ 't')
        stats["DEX"] = dice.roll(self.database[race]['STATS']['DEX']+ 't')
        stats["CON"] = dice.roll(self.database[race]['STATS']['CON']+ 't')
        stats["SIZ"] = dice.roll(self.database[race]['STATS']['SIZ']+ 't')
        stats["INT"] = dice.roll(self.database[race]['STATS']['INT']+ 't')
        stats["POW"] = dice.roll(self.database[race]['STATS']['POW']+ 't')
        stats["CHA"] = dice.roll(self.database[race]['STATS']['CHA']+ 't')
        return stats
    
    def calculate_hp(self, stats):
        # CALCULATES CREATURE HP BASED ON ROLLED STATS
        CON = stats['CON']
        POW = stats['POW']
        SIZ = stats['SIZ']
        # calculat POW HP modifier according to chart
        if POW >= 1 and POW <= 4:
            pow_mod = -1
        elif POW >= 5 and POW <= 16:
            pow_mod = 0
        elif POW >= 17 and POW <= 20:
            pow_mod = 1
        elif POW >= 21 and POW <= 24:
            pow_mod = 2
        elif POW >= 25 and  POW<= 28:
            pow_mod = 3
        elif POW > 28:
            # math.floor(POW / 4) rounds to the lowest nearest integer
            # making sure that every 4 additional points of POW gain exactly 1 more HP per 4 points
            pow_mod = 3 + math.floor(POW / 4)
        # calculat SIZ HP modifier according to chart
        if SIZ >= 1 and SIZ <= 4:
            siz_mod = -2
        elif SIZ >= 5 and SIZ <= 8:
            siz_mod = -1
        elif SIZ >= 9 and SIZ <= 12:
            siz_mod = 0
        elif SIZ >= 13 and SIZ <= 16:
            siz_mod = 1
        elif SIZ >= 17 and SIZ <= 20:
            siz_mod = 2
        elif SIZ >= 21 and SIZ <= 24:
            siz_mod = 3
        elif SIZ >=25 and SIZ <= 28:
            siz_mod = 4
        elif SIZ > 28:
            # math.floor(SIZ / 4) rounds to the lowest nearest integer
            # making sure that every 4 additional points of SIZ gain exactly 1 more HP per 4 points
            siz_mod = 4 + math.floor(SIZ / 4)
        
        # get final HP
        hp = {'HP' : CON + pow_mod + siz_mod}
        return hp
    
    def generate(self, race='BROO', quantity = 1):
        # generates NPCS based on the selected rase and quantity
        race = race.upper()
        chars = []
        # for the given quantity
        for i in range(quantity):
            # roll the stats of the npc
            stats = self.roll_stats(race)
            # calculate the hp of the npc
            hp = self.calculate_hp(stats)
            # calculate the mp
            # mp is equal to POW (very simple)
            mp = {'MP' : stats['POW']}
            
            # generate character sheet dictionary for the npc
            char_sheet = {}
            # adds race name and number of generated npc to the char sheet
            char_sheet['Name'] = (race + ' ' + str(i + 1))
            # updates the char sheet dictionary with stats
            char_sheet.update(stats)
            # updates the char sheet dictionary with hp
            char_sheet.update(hp)
            # updates the char sheet dictionary with mp
            char_sheet.update(mp)
            
            # appends the char sheet to the list of generated npcs
            chars.append(char_sheet)
        return chars    

# initialize NPC_Maker class       
npc_make = NPC_Maker(db)

# generate and print the generated npcs
npcs = npc_make.generate(race = chosen_race, quantity = chosen_quantity)

# create JSON
if json_generate == 'Y':
    if os.path.exists('generated_npcs.json'):
            with open('generated_npcs.json', 'w') as f:
                json.dump(npcs, f, indent=4, ensure_ascii=False)
    else:
        with open('generated_npcs.json', 'w+') as f:
                json.dump(npcs, f, indent=4, ensure_ascii=False)
        print('Created JSON file "generated_npcs.json"')
else:
    for npc in npcs:
        print(npc)
        print()
