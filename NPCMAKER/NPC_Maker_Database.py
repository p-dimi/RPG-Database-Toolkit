import json
import os

# check all necessary files to start
races_db = 'races.db'
spells_db = 'spells.db'
skills_db = 'skills.db'
chaos_features_db = 'chaos_features.db'
if not os.path.exists(races_db) or not os.path.exists(spells_db) or not os.path.exists(skills_db) or not os.path.exists(chaos_features_db):
    print('DATABASE FILE NOT EXIST. PLEASE RUN "NPC_Maker_Database_Writer.py" SCRIPT FIRST TO GENERATE DATABASE FILE')

# database class definition
class database:
    def __init__(self):
        self.races = {}
        self.spells = {}
        self.skills = {}
        self.chaos_features = {}
        # read the database files
        self.races_db = 'races.db'
        self.spells_db = 'spells.db'
        self.skills_db = 'skills.db'
        self.chaos_features_db = 'chaos_features.db'
        # build database
        self.build_database()
        
    def get(self, item):
        if item == 'skills':
            return self.skills
        elif item == 'races':
            return self.races
        elif item == 'spells':
            return self.spells
        elif item == 'chaos features':
            return self.chaos_features
        elif item == 'all':
            return self.races, self.skills, self.spells, self.chaos_features
    
    def load_database(self, db_file):
        # load database file into single dictionary
        with open(db_file, 'r') as file:
            # read db
            data = file.read()
            # remove constant first comma in file
            data = data[1:]
            # add square brackets to string
            data = '[' + data + ']'
            # alter single quotes to double quotes (JSON requirement)
            data.replace("\'","\"")
            # parse db string into list of dicionaries
            loaded_db = json.loads(data)
        # assemble list of dicionaries into single dictionary
        full_dic = {}
        for dic in loaded_db:
            full_dic.update(dic)
        return(full_dic)
    
    def initialize_races(self):
        self.races = self.load_database(self.races_db)
    
    def build_database(self):
        self.initialize_races()