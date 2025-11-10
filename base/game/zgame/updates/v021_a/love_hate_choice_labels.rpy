# Labels where ONLY relevant variables + quests are handled after a love or hate choice is made (No visuals/sequence / silent)
# Theoretically, you can just copy the variable / quest operations away from this file and take them back to where the choice is actually being made, 
# right before jump action taken
# Otherwise, just use console to call (NOT JUMP) these labels once you finish your sequence of a player having made a choice
# No visuals take place, just variable / quest handling


default him_journal_level = 1
default hin_journal_level = 1
default him_current_view_level = 1
default hin_current_view_level = 1

label chosen_hate_path:
    # Set the global flag
    $ nochoice_made_yet = False
    $ chosen_hate_path = True
    $ chosen_love_path = False
    $ him_journal_level = 2
    $ hin_journal_level = 2
    $ him_current_view_level = 2
    $ hin_current_view_level = 2
    $ quest_hin.add(hinata2)
    $ quest_him.add(himawari2)

    # --- HINATA'S QUESTS (uses the quest_hin manager) ---
    # 1. Set the main 'Hatred' advancement quest to "in progress"
    $ quest_hin.check("hin2H_1", "in progress")
    
    # 2. **THE FIX**: Explicitly fail the main "Love Path" quest on the left page.
    $ quest_hin.check("hinata1love", "failed")
    $ quest_hin.check("hinata2love", "failed")

    # 3. Fail all the sub-quests on the right page.
    $ quest_hin.update(state="failed", category="[hin_name]'s Love path")

    # --- HIMAWARI'S QUESTS (uses the quest_him manager) ---
    # 1. Set the main 'Hatred' advancement quest to "in progress"
    $ quest_him.check("him2H_1", "in progress")

    # 2. **THE FIX**: Explicitly fail the main "Love Path" quest on the left page.
    $ quest_him.check("himawari1love", "failed")
    $ quest_him.check("himawari2love", "failed")

    # 3. Fail all the sub-quests on the right page.
    $ quest_him.update(state="failed", category="[him_name]'s Love path")

    # 4. Handle old flags (label wakeupend in bohin1_wakeup)
    $ bohin1_lovepath = False
    $ bohin1_hatredpath = True
    $ bohin1_pathchosen = True
    return


label chosen_love_path:
    # Set the global flag
    $ nochoice_made_yet = False
    $ chosen_love_path = True
    $ chosen_hate_path = False
    $ hatred.level = 1
    $ hatred.value = 0
    $ him_journal_level = 2
    $ hin_journal_level = 2
    $ him_current_view_level = 2
    $ hin_current_view_level = 2
    $ quest_hin.add(hinata2)
    $ quest_him.add(himawari2)

    # --- HINATA'S QUESTS (uses the quest_hin manager) ---
    # 1. Set the main 'Love' advancement quest to "in progress"
    $ quest_hin.check("hin2L_1", "in progress") #todo current never gets completed

    # 2. **THE FIX**: Explicitly fail the main "Hatred Path" quest on the left page.
    $ quest_hin.check("hinata1hatred", "failed")
    $ quest_hin.check("hinata2hatred", "failed")

    # 3. Fail all the sub-quests on the right page.
    $ quest_hin.update(state="failed", category="[hin_name]'s Hatred path")
    


    # --- HIMAWARI'S QUESTS (uses the quest_him manager) ---
    # 1. Set the main 'Love' advancement quest to "in progress"
    $ quest_him.check("him2L_1", "in progress")

    # 2. **THE FIX**: Explicitly fail the main "Hatred Path" quest on the left page.
    $ quest_him.check("himawari1hatred", "failed")
    $ quest_him.check("himawari2hatred", "failed")

    # 3. Fail all the sub-quests on the right page.
    $ quest_him.update(state="failed", category="[him_name]'s Hatred path")

    # 4. Handle old flags (label wakeupend in bohin1_wakeup)
    $ bohin1_lovepath = True
    $ bohin1_hatredpath = False
    $ bohin1_pathchosen = True
    
    return