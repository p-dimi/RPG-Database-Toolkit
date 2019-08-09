# Database-maker-and-NPC-maker-for-RuneQuest

This project is meant to generate NPCs in bulk for the tabletop role playing game RuneQuest.

Current scripts are:
NPC_Maker_Database_Writer.py <-- Generates custom JSON like database of Races, Spells, Skills and Chaos Features

Allows you to add new elements (new races, new spells, etc) to already existing database files.

NPC_Maker_Database.py <-- Reads the database files and initializes the database

NPC_Maker.py <-- Generates NPCs in bulk based on user chosen variables, and saves the generated NPCs in JSON format


Current version only saves Races, and generates NPCs only from the race database file, and only account for stats - not for any innate special spells or abilties.


Future versions will invlude:

NPC_Maker_Database_Writer <-- will write not just races, but also spells, skills and chaos features

NPC_Maker_Database <-- will read not only races, but also spells, skills and chaos features

NPC_Maker <-- will utilize spells, skills and chaos features from the database, as well as innate creature skills, spells and abilities, in the generation of NPCs.
