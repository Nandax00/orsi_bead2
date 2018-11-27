from random import randrange

classes = ["Mage", "Priest", "Warlock", "Demon Hunter", "Druid", "Monk", "Rogue","Hunter", "Shaman","Death Knight", "Paladin", "Warrior"]
races = ["Human", "Dwarf", "Night Elf", "Gnome", "Draenei", "Worgen",
    "Void Elf", "Lightforged Draenei", "Dark Iron Dwarf",
    "Orc", "Undead", "Tauren", "Troll", "Blood Elf", "Goblin",
    "Nightborne", "Highmountain Tauren", "Mag'har Orc",
    "Pandaren (Alliance)", "Pandaren (Horde)"
    ]

genders = ["Female", "Male"]

professions = ["Herbalism", "Skinning", "Mining", "Blacksmithing", "Engineering", "Jewelcrafting", "Tailoring", "Enchanting", "Alchemy", "Inscription", "Leatherworking"]

towns = ["Orgrimmar", "Thunder Bluff", "Silvermoon", "Undercity", "Stormwind", "Ironforge", "Exodar", "Darnassus",
    "Dalaran", "Shattrath", "Zuldazar", "Boralus", "Shrine of Two Moons", "Shrine of Seven Stars"]

realms = ["Aerie Peak",
    "Aggramar",
    "Al'Akir",
    "Alonsus",
    "Antonidas",
    "Arathor",
    "Argent Dawn",
    "Auchindoun",
    "Azjol-Nerub",
    "Blackhand",
    "Blackmoore",
    "Blackrock",
    "Bloodhoof",
    "Burning Legion",
    "Chamber of Aspects",
    "Darksorrow",
    "Darkspear",
    "Defias Brotherhood",
    "Destromath",
    "Doomhammer",
    "Draenor",
    "Dragonblight",
    "Drak'thul",
    "Earthen Ring",
    "Emerald Dream",
    "Eonar",
    "Eredar",
    "Frostmane",
    "Frostwhisper",
    "Frostwolf",
    "Grim Batol",
    "Kazzak",
    "Kilrogg",
    "Lightbringer",
    "Lordaeron",
    "Magtheridon",
    "Molten Core",
    "Moonglade",
    "Nordrassil",
    "Onyxia",
    "Outland",
    "Ragnaros",
    "Ravencrest",
    "Shadowmoon",
    "Shadowsong",
    "Shattered Hand",
    "Silvermoon",
    "Stonemaul",
    "Stormrage",
    "Stormreaver",
    "Stormscale",
    "Sunstrider",
    "Sylvanas",
    "Tarren Mill",
    "The Maelstrom",
    "Thrall",
    "Thunderhorn",
    "Twilight's Hammer",
    "Twisting Nether",
    "Warsong"]

titles = ["<name> the Patient",
    "Starcaller <name>",
    "<name> the Astral Walker",
    "<name>, Destroyer's End",
    "<name>, Liberator of Orgrimmar",
    "<name> of the Ashen Verdict",
    "<name>, Champion of the Frozen Wastes",
    "Ambassador <name>",
    "<name>, Blackwing's Bane",
    "<name> of the Four Winds",
    "Dragonslayer <name>",
    "<name> the Kingslayer",
    "<name>, Savior of Azeroth",
    "<name> the Explorer",
    "<name> the Hallowed",
    "Brewmaster <name>",
    "<name>, Conqueror of Orgrimmar",
    "Associate Professor <name>",
    "<name> Jenkins",
    "Assistant Professor <name>",
    "Twilight Vanquisher <name>",
    "<name> of the Nightfall",
    "<name> the Seeker",
    "<name> the Light of Dawn",
    "Firelord <name>"]



num_of_samples = randrange(1,101)
f = open("input.txt", "wt")
f.write(str(num_of_samples) + "\n")
for i in range(0,num_of_samples):
    class_id = randrange(0,len(classes))
    race_id = randrange(0,len(races))
    title_id = randrange(0,len(titles))
    realm_id = randrange(0,len(realms))
    town_id = randrange(0,len(towns))
    profession_id = randrange(0,len(professions))

    f.write(classes[class_id] + ";") #class
    f.write(races[race_id] + ";")    #race
    f.write(str(randrange(1,121)) + ";")  #level
    f.write(genders[randrange(0,2)] + ";") #gender
    f.write(titles[title_id] + ";")  #title
    f.write(realms[realm_id] + ";") #realm
    f.write(towns[town_id] + ";") #town
    f.write(professions[profession_id] + "\n") #prof

f.close()
