import os
import json


# generate races.db file if one does not exist already
races_db = 'races.db'
if not os.path.exists(races_db):
    with open(races_db, 'w+') as f:
        f.write('')
        
# generate spells.db file if one does not exist already
spells_db = 'spells.db'
if not os.path.exists(spells_db):
    with open(spells_db, 'w+') as f:
        f.write('')
        
# generate skills.db file if one does not exist already
skills_db = 'skills.db'
if not os.path.exists(skills_db):
    with open(skills_db, 'w+') as f:
        f.write('')
        
# generate chaos_features.db file if one does not exist already
chaos_features_db = 'chaos_features.db'
if not os.path.exists(chaos_features_db):
    with open(chaos_features_db, 'w+') as f:
        f.write('')


print('This is a non destructive script that adds data to the database files.\nYou can run this script to add new items to the database at any point.\n')
print('The requested is not case sensitive. All input gets transformed into upper case automatically.')

# Function that adds race to races.db file
def add_race_to_database(path=races_db):
    print('You can type Break at any point to reset the process')

    # init buffers for db writing
    stats_buff = []
    cs_buff = []
    ncs_buff = []
    lgs_buff = []
    psn_buff = []
    run_buff = []
    sp_spl_buff = []
    rn_spl_buff = []
    sc_spl_buff = []
    sp_sk_buff = []   
    chs_buff = []

    # get race name
    print('\n')
    rname = str(input('Input race name: '))
    rname = rname.upper()
    
    # get stats
    print('Getting Stats:')
    STR = str(input('Add STR: '))
    if STR.upper() == 'BREAK':
        print('Resetting')
        return
    stats_buff.append(('STR',STR.upper()))
    CON = str(input('Add CON: '))
    if CON.upper() == 'BREAK':
        print('Resetting')
        return
    stats_buff.append(('CON',CON.upper()))
    SIZ = str(input('Add SIZ: '))
    if SIZ.upper() == 'BREAK':
        print('Resetting')
        return
    stats_buff.append(('SIZ',SIZ.upper()))
    INT = str(input('Add INT: '))
    if INT.upper() == 'BREAK':
        print('Resetting')
        return
    stats_buff.append(('INT',INT.upper()))
    POW = str(input('Add POW: '))
    if POW.upper() == 'BREAK':
        print('Resetting')
        return
    stats_buff.append(('POW',POW.upper()))
    DEX = str(input('Add DEX: '))
    if DEX.upper() == 'BREAK':
        print('Resetting')
        return
    stats_buff.append(('DEX',DEX.upper()))
    CHA = str(input('Add CHA: '))
    if CHA.upper() == 'BREAK':
        print('Resetting')
        return
    stats_buff.append(('CHA',CHA.upper()))
    MOVE = str(input('Add MOVE: '))
    if MOVE.upper() == 'BREAK':
        print('Resetting')
        return
    stats_buff.append(('MOVE',MOVE.upper()))
    RUNEP = str(input('Add RUNE POINTS: '))
    if RUNEP.upper() == 'BREAK':
        print('Resetting')
        return
    stats_buff.append(('RUNE POINTS',RUNEP.upper()))
    BSR = str(input('Add BASE SR: '))
    if BSR.upper() == 'BREAK':
        print('Resetting')
        return
    stats_buff.append(('BASE SR',BSR.upper()))
    
    # get combat skills
    print('\n')
    print('=======================')
    print('COMBAT SKILLS:')
    print('=======================')
    print('\n')
    print('Input Combat skills. Type the skill name and the percentage, separated by a period.\nLike this: Dodge.35\nWhen finished, type Fin')
    fin_cs = False
    
    # counter
    sk_ctr = 0
    
    # recursive loop
    while fin_cs == False:
        sk_ctr = sk_ctr + 1
        cs_vb = str(input('Combat skill No.{}: '.format(sk_ctr)))
        if cs_vb.upper() == 'BREAK':
            print('Resetting')
            return
        if cs_vb.upper() == 'FIN':
            break
        else:
            # if there is no dot added, reset skill
            try:
                split_input = cs_vb.capitalize().split('.')
                cs_buff.append((split_input[0],split_input[1]+'%'))
            except:
                print('Please be sure to separate the string and digit by a dot (.). Please input again.')
    
    # reset counter
    sk_ctr = 0
    
    # get non combat skills
    print('\n')
    print('=======================')
    print('NON-COMBAT SKILLS:')
    print('=======================')
    print('\n')
    print('Input Non-Combat skills. Type the skill name and the percentage, separated by a period.\nLike this: Dance.35\nWhen finished, type Fin') 
    fin_cs = False
    # recursive loop
    while fin_cs == False:
        sk_ctr = sk_ctr + 1
        cs_vb = str(input('Non-Combat skill No.{}: '.format(sk_ctr)))
        if cs_vb.upper() == 'BREAK':
            print('Resetting')
            return
        if cs_vb.upper() == 'FIN':
            break
        else:
            # if there is no dot added, reset skill
            try:
                split_input = cs_vb.capitalize().split('.')
                ncs_buff.append((split_input[0],split_input[1]+'%'))
            except:
                print('Please be sure to separate the string and digit by a dot (.). Please input again.')
    
    # languages
    print('\n')
    print('=======================')
    print('LANGUAGES:')
    print('=======================')
    print('\n')
    print('Input Languages. Type the language name and the percentage, separated by a period.\nLike this: Speak Aldryami.90\nWhen finished, type Fin') 
    # reset counter
    sk_ctr = 0
    
    fin_cs = False
    # recursive loop
    while fin_cs == False:
        sk_ctr = sk_ctr + 1
        cs_vb = str(input('Language No.{}: '.format(sk_ctr)))
        if cs_vb.upper() == 'BREAK':
            print('Resetting')
            return
        if cs_vb.upper() == 'FIN':
            break
        else:
            # if there is no dot added, reset skill
            try:
                split_input = cs_vb.capitalize().split('.')
                lgs_buff.append((split_input[0],split_input[1]+'%'))
            except:
                print('Please be sure to separate the string and digit by a dot (.). Please input again.')
    
    # passions
    print('\n')
    print('=======================')
    print('PASSIONS:')
    print('=======================')
    print('\n')
    print('Input Passions. Type the passion name and the percentage, separated by a period.\nLike this: Honor.0\nWhen finished, type Fin') 
    # reset counter
    sk_ctr = 0
    
    fin_cs = False
    # recursive loop
    while fin_cs == False:
        sk_ctr = sk_ctr + 1
        cs_vb = str(input('Passion No.{}: '.format(sk_ctr)))
        if cs_vb.upper() == 'BREAK':
            print('Resetting')
            return
        if cs_vb.upper() == 'FIN':
            break
        else:
            # if there is no dot added, reset skill
            try:
                split_input = cs_vb.capitalize().split('.')
                psn_buff.append((split_input[0],split_input[1]+'%'))
            except:
                print('Please be sure to separate the string and digit by a dot (.). Please input again.')
    
    # runes
    print('\n')
    print('=======================')
    print('RUNES:')
    print('=======================')
    print('\n')
    print('Input Runes. Type the rune name and the percentage, separated by a period.\nLike this: Truth.60\nWhen finished, type Fin') 
    # reset counter
    sk_ctr = 0
    
    fin_cs = False
    # recursive loop
    while fin_cs == False:
        sk_ctr = sk_ctr + 1
        cs_vb = str(input('Rune No.{}: '.format(sk_ctr)))
        if cs_vb.upper() == 'BREAK':
            print('Resetting')
            return
        if cs_vb.upper() == 'FIN':
            break
        else:
            # if there is no dot added, reset skill
            try:
                split_input = cs_vb.capitalize().split('.')
                run_buff.append((split_input[0],split_input[1]+'%'))
            except:
                print('Please be sure to separate the string and digit by a dot (.). Please input again.')
    
    # spells
    print('\n')
    print('=======================')
    print('INNATE SPIRIT SPELLS:')
    print('=======================')
    print('\n')
    fin_loop = False
    # recursive loop
    while fin_loop == False:
        spls = str(input('Does the race have any Spirit Spells that it always knows? (Y/N): '))
        if spls.upper() == 'BREAK':
            print('Resetting')
            return
        if spls.upper() == 'N':
            fin_loop = True
            pass
        elif spls.upper() == 'Y':
            print('Input Spells. Type the spell name and the level, separated by a period.\nLike this: Lightwall.4\nWhen finished, type Fin') 
            # reset counter
            sk_ctr = 0
            
            fin_cs = False
            # recursive loop
            while fin_cs == False:
                sk_ctr = sk_ctr + 1
                cs_vb = str(input('Spirit Spell No.{}: '.format(sk_ctr)))
                if cs_vb.upper() == 'BREAK':
                    print('Resetting')
                    return
                if cs_vb.upper() == 'FIN':
                    fin_loop = True
                    break
                else:
                    # if there is no dot added, reset skill
                    try:
                        split_input = cs_vb.capitalize().split('.')
                        sp_spl_buff.append((split_input[0],split_input[1]))
                    except:
                        print('Please be sure to separate the string and digit by a dot (.). Please input again.')
        else:
            print('Input must be either Y or N.')
            
    print('\n')
    print('=======================')
    print('INNATE SORCERY SPELLS:')
    print('=======================')
    print('\n')
    fin_loop = False
    # recursive loop
    while fin_loop == False:
        spls = str(input('Does the race have any Sorcery Spells that it always knows? (Y/N): '))
        if spls.upper() == 'BREAK':
            print('Resetting')
            return
        if spls.upper() == 'N':
            fin_loop = True
            pass
        elif spls.upper() == 'Y':
            print('Input Spells. Type the spell name and the level, separated by a period.\nLike this: Lightwall.4\nWhen finished, type Fin') 
            # reset counter
            sk_ctr = 0
            
            fin_cs = False
            # recursive loop
            while fin_cs == False:
                sk_ctr = sk_ctr + 1
                cs_vb = str(input('Sorcery Spell No.{}: '.format(sk_ctr)))
                if cs_vb.upper() == 'BREAK':
                    print('Resetting')
                    return
                if cs_vb.upper() == 'FIN':
                    fin_loop = True
                    break
                else:
                    # if there is no dot added, reset skill
                    try:
                        split_input = cs_vb.capitalize().split('.')
                        sc_spl_buff.append((split_input[0],split_input[1]))
                    except:
                        print('Please be sure to separate the string and digit by a dot (.). Please input again.')
        else:
            print('Input must be either Y or N.')
        
        
    print('\n')
    print('=======================')
    print('INNATE RUNE SPELLS:')
    print('=======================')
    print('\n')
    fin_loop = False
    # recursive loop
    while fin_loop == False:
        spls = str(input('Does the race have any Rune Spells that it always knows? (Y/N): '))
        if spls.upper() == 'BREAK':
            print('Resetting')
            return
        if spls.upper() == 'N':
            fin_loop = True
            pass
        elif spls.upper() == 'Y':
            print('Input Spells. Type the spell name and the level, separated by a period.\nLike this: Lightwall.4\nWhen finished, type Fin') 
            # reset counter
            sk_ctr = 0
            
            fin_cs = False
            # recursive loop
            while fin_cs == False:
                sk_ctr = sk_ctr + 1
                cs_vb = str(input('Rune Spell No.{}: '.format(sk_ctr)))
                if cs_vb.upper() == 'BREAK':
                    print('Resetting')
                    return
                if cs_vb.upper() == 'FIN':
                    fin_loop = True
                    break
                else:
                    # if there is no dot added, reset skill
                    try:
                        split_input = cs_vb.capitalize().split('.')
                        rn_spl_buff.append((split_input[0],split_input[1]))
                    except:
                        print('Please be sure to separate the string and digit by a dot (.). Please input again.')
        else:
            print('Input must be either Y or N.')
    
            
    # special skills
    print('\n')
    print('=======================')
    print('SPECIAL SKILLS:')
    print('=======================')
    print('\n')
    fin_loop = False
    # recursive loop
    while fin_loop == False:
        spls = str(input('Does the race have any special skills (Y/N): '))
        if spls.upper() == 'BREAK':
            print('Resetting')
        if spls.upper() == 'N':
            fin_loop = True
            pass
        elif spls.upper() == 'Y':
            print('Input Skills. Type the skill name and the percentage, separated by a period.\nLike this: Charm Babboon.25\nWhen finished, type Fin') 
            # reset counter
            sk_ctr = 0
            
            fin_cs = False
            # recursive loop
            while fin_cs == False:
                sk_ctr = sk_ctr + 1
                cs_vb = str(input('Special Skill No.{}: '.format(sk_ctr)))
                if cs_vb.upper() == 'BREAK':
                    print('Resetting')
                if cs_vb.upper() == 'FIN':
                    fin_loop = True
                    break
                else:
                    # if there is no dot added, reset skill
                    try:
                        split_input = cs_vb.capitalize().split('.')
                        sp_sk_buff.append((split_input[0],split_input[1]+'%'))
                    except:
                        print('Please be sure to separate the string and digit by a dot (.). Please input again.')
        else:
            print('Input must be either Y or N.')
    
    
    # chaos type
    print('\n')
    print('=======================')
    print('CHAOS TYPE:')
    print('=======================')
    print('\n')
    
    fin_loop = False
    # recursive loop
    while fin_loop == False:
        spls = str(input('Is the creature inherently Chaos type? (Y/N): '))
        if spls.upper() == 'BREAK':
            print('Resetting')
        if spls.upper() == 'N':
            print('Creature is not chaos.')
            chs_buff.append('N')
            fin_loop = True
            pass
        elif spls.upper() == 'Y':
            print('Creature is Chaos.')
            chs_buff.append('Y')
            fin_loop = True
        else:
            print('Input must be either Y or N.')
    
    # generate npc sheet
    charsheet = {rname: {'STATS' : {'STR':'','CON':'','SIZ':'','INT':'','POW':'','DEX':'','CHA':'','MOVE':'','RUNE POINTS':'','BASE SR':''}, 'SKILLS':{'COMBAT SKILLS':{},'NON COMBAT SKILLS':{}},'LANGUAGES':{},'PASSIONS':{},'RUNES':{},'SPELLS':{'SPIRIT SPELLS':[], 'RUNE SPELLS':[], 'SORCERY SPELLS':[]},'SPECIAL SKILLS':[],'CHAOS':''}}
    # store stats
    for item in stats_buff:
        name = item[0]
        stat = item[1]
        charsheet[rname]['STATS'][name] = stat
    # store skills
    for item in cs_buff:
        name = item[0]
        stat = item[1]
        charsheet[rname]['SKILLS']['COMBAT SKILLS'][name] = stat
    for item in ncs_buff:
        name = item[0]
        stat = item[1]
        charsheet[rname]['SKILLS']['NON COMBAT SKILLS'][name] = stat
    # store passions
    for item in psn_buff:
        name = item[0]
        stat = item[1]
        charsheet[rname]['PASSIONS'][name]= stat
    # store languages
    for item in lgs_buff:
        name = item[0]
        stat = item[1]
        charsheet[rname]['LANGUAGES'][name]= stat
    # store runes
    for item in run_buff:
        name = item[0]
        stat = item[1]
        charsheet[rname]['RUNES'][name]= stat
    # store spells
    for item in sp_spl_buff:
        name = item[0]
        stat = item[1]
        combined = name + ' ' + '(' + stat + ')'
        lst = charsheet[rname]['SPELLS']['SPIRIT SPELLS']
        lst.append(combined)
        charsheet[rname]['SPELLS']['SPIRIT SPELLS'] = lst
    
    for item in sc_spl_buff:
        name = item[0]
        stat = item[1]
        combined = name + ' ' + '(' + stat + ')'
        lst = charsheet[rname]['SPELLS']['SORCERY SPELLS']
        lst.append(combined)
        charsheet[rname]['SPELLS']['SORCERY SPELLS'] = lst
        
    for item in rn_spl_buff:
        name = item[0]
        stat = item[1]
        combined = name + ' ' + '(' + stat + ')'
        lst = charsheet[rname]['SPELLS']['RUNE SPELLS']
        lst.append(combined)
        charsheet[rname]['SPELLS']['RUNE SPELLS'] = lst
    
    # store special skills
    for item in sp_sk_buff:
        name = item[0]
        stat = item[1]
        combined = name + ' ' + '(' + stat + ')'
        lst = charsheet[rname]['SPECIAL SKILLS']
        lst.append(combined)
        charsheet[rname]['SPECIAL SKILLS'] = lst
    # store chaos status
    if chs_buff == ['N']:
        charsheet[rname]['CHAOS'] = "NO"
    elif chs_buff == ['Y']:
        charsheet[rname]['CHAOS'] = "YES"
   
    # confirm addition
    print('\nThe race you input is this:')
    sheet = json.dumps(charsheet, indent=4)
    print(sheet)
    corr = str(input('Is this correct? (Y/N): '))
    
    inpt_fin = False
    while inpt_fin == False:
        if corr.upper() == 'Y':
            # save the json to the database
            with open(races_db, 'a') as f:
                f.write(',')
                json.dump(charsheet, f, indent=4, ensure_ascii=False)
                f.write('\n')
            inpt_fin = True
        elif corr.upper() == 'N':
            print('Resetting')
            return
        elif corr.upper() == 'BREAK':
            print('Resetting')
            return
        else:
            print('Please input either Y, N or Break')



# BLOCK TO ADD DATA TO DB
add_to_db = str(input('Add data to database? (Y/N): '))
add_to_db = add_to_db.upper()

if add_to_db == 'Y':
    # recursive loop to add data until done
    finished_adding_all = False
    while finished_adding_all == False:
        # what type of data to add to database. 'Break' in order to break out of the loop
        add_type = str(input('What to add? (Race, Spell, Skill, Chaos feature, Break): '))
        add_type = add_type.upper()
        
        # adding specific type of data to relevant database
        if add_type == 'RACE':
            # recursive loop to keep adding races until finished
            finished_adding = False
            while finished_adding == False:
                add_race_to_database()
                fin = str(input('Input more races? (Y, N, Break): '))
                fin = fin.upper()
                if fin == 'Y':
                    pass
                elif fin == 'N':
                    finished_adding = True
                elif fin == 'BREAK':
                    break
                else:
                    print('Input must be one of these three arguments: Y, N, Break')
                
        elif add_type == 'SPELL':
            pass
        elif add_type == 'SKILL':
            pass
        elif add_type == 'CHAOS FEATURE':
            pass
        elif add_type == 'BREAK':
            break
        else:
            print('Input must be one of these four arguments: Race, Spell, Skill, Chaos feature')
        
        fin_all = str(input('Finished adding data to database? (Y/N): '))
        fin_all = fin_all.upper()
        if fin_all == 'Y':
            finished_adding_all = True
        elif fin_all == 'N':
            pass
        else:
            print('Input must be one of these two arguments: Y, N')
else:
    pass
