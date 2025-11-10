

default persistent.translationstring = 101218
default persistent.last_version = ""
default persistent.old_hashbase = None
label v12b_onetime:
    if persistent.last_version != config.version:
        $ persistent.old_hashbase = hashbase
        $ hashbase = 13
        

        $ print("Running version update code")
        # Update the stored version
        $ persistent.last_version = config.version
        $ renpy.block_rollback()
    return


label after_load:
    default v14_1sttime = False  #fixed hima stomach freeze
    default v14c_1sttime = False #fixed himawari panties bug
    default v14f_1sttime = False #fixed pool description in shop / polish
    default v14g_1sttime = False #onetime rollback day6
    default v14i_1sttime = False #grammar
    default v14k_1sttime = False #grammar 2
    default v17_1sttime = False
    default v17_1sttime_saradaintro = False
    default v17_1sttime_markmodelquestcomplete = False
    default v15_1sttime = False
    default v18_1sttime = False #fixed yoru's love photoshoot not advancing hima dialogue  
    
    default v18_tentenquest = False
    default v19_1sttime1 = False #Fixes tenten's quest flow
    default v19_1sttime2 = False #Fixes missing shop quests
    default v19_1sttime3 = False #Adds Hinata objectives after shower
    default v19_1sttime4 = False
    default v19_1sttime5 = False
    default v19g_1sttime_r = False
    default v20_1sttime_r = False
    default v20_1sttime_r2 = False
    default v20_1sttime_r3 = False
    default v20_1sttime_r4 = False
    default v20_1sttime_r5 = False #gallery/replay/camera fix
    default v20_1sttime_r6 = False

    #all versions
    if persistent.last_version != config.version:
        $ persistent.old_hashbase = hashbase
        $ hashbase = 14
        $ store.hashbase == 14
        $ print("Running version update code")
        # Update the stored version
        $ persistent.last_version = config.version
        
        $ renpy.block_rollback()

    if day_number >= 11:
        if v19g_1sttime_r == False:
            $ day_number = 10
            $ day_name == "Sunday"
            dev"You loaded an old save that needs to have the Day set back to 10."
            dev"After you overwrite this save, your day counter will not reset again."
            dev"Remember to train your strength, or save enough money for Day 14's quest!"
            $ v19g_1sttime_r = True

    # KEEP THIS BLOCK AT THE TOP (It runs every time). No need to keep updating quest titles/wip flag, just update from where you defined the quest.
    # AUTO QUEST SYNC (syncs quest titles and wip flags on load)
    python:
        print("--- Running post-load quest synchronization ---")
        
        # The Manager class now handles everything internally (add missing quests, update title/wip/level attributes)
        # The calls are clean and intuitive.
        quest.synchronize(boruto1)
        # Dynamically call all definitions that contain hinata or himawari to prevent need for adjustments here when new level definitions are created
        quest_hin.synchronize("hinata")
        quest_him.synchronize("himawari")

        print("--- Quest synchronization complete. ---")

        # Path validation logic remains unchanged. If a path was chosen, auto fail all opposite path quests (whether old or newly added)
        print("--- Running post-load path validation ---")
        love_path_chosen = getattr(store, 'chosen_love_path', False)
        hate_path_chosen = getattr(store, 'chosen_hate_path', False)
        
        if love_path_chosen or hate_path_chosen:
            print("  [Path Sync] Validating quest states...")
            auto_fail_quests_on_load(quest_hin, love_path_chosen, hate_path_chosen)
            auto_fail_quests_on_load(quest_him, love_path_chosen, hate_path_chosen)
        else:
            print("  [Path Sync] No Love/Hate path choice made yet. Skipping validation.")
            
        print("--- Path validation complete. ---")


    #v021i
    default v21_1sttime_i = False
    default v21_1sttime_i2 = False
    default v21_1sttime_i3 = False

    if v21_1sttime_i3 == False and chosen_hate_path == True and chosen_love_path == True: #one time 'fix' of save configs that might have been messed up with cheat engined prior to the level changes
        $ v21_1sttime_i3 = True
        if chosen_hate_path:
            $ chosen_love_path = False
        if chosen_love_path:
            $ chosen_hate_path = False

        if hatred.level >= 2:
            $ chosen_hate_path = True
            $ chosen_love_path = False
            $ hinata_love.level = 1
        if hinata_love.level >= 2:
            $ chosen_hate_path = False
            $ chosen_love_path = True
            $ hatred.level = 1



    if v21_1sttime_i == False or v21_1sttime_i2 == False:
        $ v21_1sttime_i = True
        $ v21_1sttime_i2 = True
        $ print("Overwrite_i")

        if quest.exists("bo_shower_1"):
            if quest.exists("bohim_2"):
                if quest.is_state("bohim_2", "completed"):
                    $ quest.check("bo_shower_1", "done")


        if hinata_slipped_banana == True and himawari_waitoutside == True: #complete wait outside quest
            if quest.exists("bo_shower_1"):
                if quest.is_state("bo_shower_1", "unlocked"):
                    if quest.exists("shower1_3"):
                        $ quest.check("shower1_3", "completed")
                    $ quest.check("bo_shower_1", "done") #marks left quest as complete (make sure any references now check if quest is completed to avoid errors)
                    # $ quest.remove("Just a peek!") #remove from right page

    #v021b
    # Fix stat.levels that don't match with current game progression
    default v21b_1sttime = False
    if v21b_1sttime == False:
        $ v21b_1sttime = True

        # First, reset all stat levels higher than 2 back to 2
        if himawari_obedience.level > 2:
            $ himawari_obedience.level = 2 # Is conditionally handled later
        if himawari_love.level > 1:
            $ himawari_love.level = 1 # Has to be reset to 1 since there's no himawari love advancement in the game
        if hinata_obedience.level >= 2:
            $ hinata_obedience.level = 2 # Is conditionally handled later
        if hinata_love.level > 2:
            $ hinata_love.level = 2 # Is conditionally handled later
        if dominance.level > 2:
            $ dominance.level = 2 # Is conditionally handled later
        if hatred.level > 2:
            $ hatred.level = 2 # Is conditionally handled later

        # Then, if negative or 0 level bring it back to 2

        if himawari_obedience.level <= 0:
            $ himawari_obedience.level = 2 # Is conditionally handled later
        if himawari_love.level <= 0:
            $ himawari_love.level = 1 # Has to be reset to 1 since there's no himawari love advancement in the game and isnt conditionally handled later
        if hinata_obedience.level <= 0:
            $ hinata_obedience.level = 2 # Is conditionally handled later
        if hinata_love.level <= 0:
            $ hinata_love.level = 2 # Is conditionally handled later
        if dominance.level <= 0:
            $ dominance.level = 2 # Is conditionally handled later
        if hatred.level <= 0:
            $ hatred.level = 2 # Is conditionally handled later

        # Then, conditionally reset stats that are at level 2 back to level 1, if the relevant game progression was not made.
        # hima obediece is higher than 1 but never completed swimsuit photoshoot, bring it back to 1
        if himawari_obedience.level > 1 and hima_swimsuit_first_time:
            $ himawari_obedience.level = 1
        # dominance is higher than 1 but never did the squat competition/strength training scene, bring back to 1
        if dominance.level > 1 and hima_first_time_competition:
            $ dominance.level = 1
        # hinata handjob (hatred advancement)
        if hatredlevel2_handjobcounter == 0 and hatred.level > 1:
            $ hatred.level = 1
        # hinata date (hinata_love advancement)
        if v21_hinatadate_progression == 0 and hinata_love.level > 1:
            $ hinata_love.level = 1
        # Tavern (hinata_obedience advancement)
        if v21ramenintro_progression < 2 and hinata_obedience.level > 1:
            $ hinata_obedience.level = 1

    #v021a
    # Update price of bikini, complete a plan for himawari quest category if all subquests done, take 2nd part (bohim_3) to in progress, track wrestling victory status (him1L_1/him1H_1)
    default v21_1sttime = False
    if v21_1sttime == False:
        $ v21_1sttime = True
        if day_number >= 1:
            $ inventoryShop.update_item(f"Bikini", price=100, quantity=1)
        if quest.exists("bohim_2"):
            if quest.exists("4_bohim_2") and quest.is_state("4_bohim_2", "completed"):
                $ quest.check("bohim_2", "completed")
                $ quest.check("bohim_3", "unlocked")
                $ quest.check("1_bohim_3", "in progress")
                $ inventoryShop.update_item(f"Bikini", price=100, quantity=1)
        if quest_him.is_state("him1L_1", "completed") or quest_him.is_state("him1H_1", "completed"):
            $ hima_wrestling_won = True
        

    #v020
    if v20_1sttime_r6 == False:
        $ v20_1sttime_r6 = True
        $ quest.change_quest_title("2_bohim_2","Convince [him_name] to work with you")
        $ quest.change_quest_title("3_bohim_2","Purchase necessary equipment")

    if v20_1sttime_r5 == False:
        if day_number >= 2:
            $ v20_1sttime_r5 = True
            $ inventoryShop.update_item(f"Camera", price=75, quantity=1)

    if v20_1sttime_r4 == False:
        $ v20_1sttime_r4 = True
        if tenten_extorted == True or tenten_pendant_returned == True:
            if quest.exists("shop1_3"):
                if quest.is_state("shop1_3", "in progress"):
                    $ quest.check("shop1_3", "completed")

                if quest.is_state("shop1_3", "pending"):
                    $ quest.check("shop1_3", "completed")

    if v20_1sttime_r3 == False:
        $ v20_1sttime_r3 = True
        if himawari_photoshoot_totalshots>0:
            $ himamodel_firsttime = False # Variable was set to true in old saves where people already completed a himawari model. Bring it to false (not first time)
        else:
            $ himamodel_firsttime = True # Set it to true (corrected default value) if they never reached that stage yet.
        # For those that already did photoshoot with yoru (and thus introduced her to hima) - Set the "have modeling session with hima" quest to in progress, and set the proper flags to make the menu option available
        if quest.exists("bohim_2"):
            if quest.exists("3_bohim_2") and quest.is_state("3_bohim_2", "completed") and quest.exists("4_bohim_2") and quest.is_state("4_bohim_2", "pending"):
                $ quest.check("4_bohim_2", "in progress")
                $ hima_talked_modelling = True
                $ himamodel_firsttime = True
                "You can now ask [him_name] to model for you!"
            # For those that already had the discussion with yoru about modelling, but the respective "Buy camera and do yoru photoshoot" quest was not checked in progress, put it in progress.
            elif quest.exists("3_bohim_2"):
                if quest.is_state("3_bohim_2", "pending") and yoruichi_weekdaytalk_modelling == True:
                    $ quest.check("3_bohim_2", "in progress")


    if v20_1sttime_r2 == False:
        $ v20_1sttime_r2 = True
        python:
            print("Applying patch to mark 'shop1_4' and 'shop1_5' as WIP...")
            
            # List of quest IDs to be marked as WIP in this patch
            wip_quest_ids = ["shop1_4", "shop1_5"]

            for quest_id in wip_quest_ids:
                # Find the quest object in the main quest manager
                quest_object = quest._searchID(quest_id)

                # Check if the quest actually exists in the player's save file
                if quest_object:
                    # Force its 'wip' attribute to be True.
                    quest_object.wip = True
                    print(f"  -> Success: '{quest_id}' has been set to wip=True.")
                else:
                    # This will show if the player hasn't discovered the quest yet, which is fine.
                    print(f"  -> Info: '{quest_id}' not found in this save, no patch needed.")

    #v019

    if v19_1sttime5 == False:
        $ v19_1sttime5 = True
        $ quest_hin.change_quest_title("hin1L_1","Carry [hin_name] to her bedroom after she slips")
        $ quest_hin.change_quest_title("hin1H_1","Use [hin_name]'s body after she slips")





    if v19_1sttime4 == False:
        if quest.exists("bo_shower_1"):
            $ v19_1sttime4 = True
            if quest.is_state("bo_shower_1", "done"):
                $ hinabathroom_counter = 2
                $ himabathroom_counter = 2
            if himabathroom_counter == 2:
                $ hinabathroom_counter = 2



    if v19_1sttime3 == False:
        $ v19_1sttime3 = True
        $ quest.change_quest_title("4_bohim_2",f"Have your first session with {him_name}")
        $ quest_hin.change_quest_title("hin1L_1","Carry [hin_name] to her bedroom after she slips")
        $ quest_hin.change_quest_title("hin1H_1","Use [hin_name]'s body after she slips")
        $ quest.change_quest_title("shower1_3","Wait outside...")

    if v19_1sttime2 == False:
        $ v19_1sttime2 = True
        $ quest.change_quest_title("shop1_4","Spend at least $500 (WIP)")
        if quest.exists("shop1_1"):
            $ quest.add([
                    Quest("shop1_4", ("Spend at least $500 (WIP)"), ("Shopkeeper's burden"), ("pending")),
                    Quest("shop1_5", ("Interact with the shopkeeper"), ("Shopkeeper's burden"), ("pending")),
                    
                ]) 



    if v19_1sttime1 == False:
        $ wine = Item(name="Wine", info="A bottle of exquisite wine", price=50, quantity=40)
        $ inventoryShop.add_item(wine, 49)
        $ v19_1sttime1 = True
        $ quest.change_quest_title("shop1_4","Spend at least $500 (WIP)")
        if quest.exists("shop1_1"):
            $ quest.add([
                    Quest("shop1_4", ("Spend at least $500 (WIP)"), ("Shopkeeper's burden"), ("pending")),
                    Quest("shop1_5", ("Interact with the shopkeeper"), ("Shopkeeper's burden"), ("pending")),
                    
                ]) 


            if quest.is_state("shop1_1", "completed") == True:
                $ quest.check("shop1_2", "in progress")
                $ quest.check("shop1_3", "in progress")
            if quest.is_state("shop1_2", "completed") == True:
                $ quest.check("shop1_4", "in progress")



    if v18_tentenquest == False:
        $ v18_tentenquest = True
        $ quest.change_quest_title("shop1_2","Spend at least $200")
        $ quest.change_quest_title("shop1_3","Find the shopkeeper's keepsake")

    #v18 launch
    if v18_1sttime == False:
        $ v18_1sttime = True
        if yoru_1st_photoshoot == True:
            $ yoruichi_modelling_completed = True

    #v17 fixes
    if v17_1sttime_markmodelquestcomplete == False:
        $ v17_1sttime_markmodelquestcomplete = True
        if quest.exists("bohim_2") and yoruichi_modelling_completed == True:
            if quest.is_state("3_bohim_2", "in progress"):
                $ quest.change_quest_title("job2_1",f"Save 200$ until Day 7")
                $ quest.change_quest_title("3_bohim_2",f"Purchase a camera and convince Yoru to help you")
                $ quest.change_quest_title("4_bohim_2",f"Have your first session with {him_name}")
                $ quest.check("3_bohim_2", "completed")
                $ quest.check("4_bohim_2", "in progress")

    if v17_1sttime_saradaintro == False:
        $ v17_1sttime_saradaintro = True
        $ opportunity_sakurasarada_introduction = False
    if v17_1sttime == False:
        $ v17_1sttime = True
        $ v17_update = True
        if disablentrwarning == False:
            "Would you like to disable optional NTR content?"
            $ disablentrwarning = True
            menu:
                "Would you like to disable optional NTR content?"
                "Disable optional NTR":
                    $ persistent.netorareoptional = True
                    "Optional NTR content is now disabled."
                    "Keep in mind that given the circumstances of the Shinobi world, your actions may still lead to avoidable NTR!"
                    "Act wisely..."
                    pass
                "Enable optional NTR":
                    $ persistent.netorareoptional = False
                    pass



    if v14k_1sttime == False:
        $ v14_1sttime = True
        $ v14c_1sttime = True
        $ v14f_1sttime = True
        $ v14i_1sttime = True
        $ v14k_1sttime = True
        # dev"Some code will now execute to update variables..."
        # dev"If something breaks, please report the error on Discord."
        #fixes error when loading save before himawari's introduction
        if not hasattr(store, 'snacks'): #check if variable with name 'snacks' exists
                # If it doesn't exist, create it
                $ snacks = Item(name="Snacks", info=f"{him_name}'s favorite snacks. She would appreciate it as a gift", price=10, quantity=1)
                
        # if day_number >= 6 and v14g_1sttime == False and ch1_d7_hatredpath == False and ch1_dy_200paid == False : # v14_1sttime was previous check before hotfixes. Used to avoid reseting day again
        #     $ day_number = 6
        #     $ day_name == "Sunday"
        #     $ v14g_1sttime = True
        #     "Day set to 6"


        if persistent.last_version != config.version:
            $ persistent.old_hashbase = hashbase
            $ hashbase = 14

            $ print("Running version update code")
            # Update the stored version
            $ persistent.last_version = config.version
            $ renpy.block_rollback()
        if day_number >= 1:


            if not hasattr(store, 'himawaripanties'):
                # If it doesn't exist, create it
                $ himawaripanties = Item(name=f"Panties", info=f"A pair of already worn pink underwear belonging to {him_name}", price=0, quantity=1)

            if not hasattr(store, 'himawaripantiescum'):
                # If it doesn't exist, create it
                $ himawaripantiescum = Item(name=f"Soiled Panties", info=f"A pair of cum-stained panties belonging to {him_name}", price=0, quantity=1)

            $ Inventory.update_independent_item(himawaripanties, name="Panties", info=f"A pair of already worn pink underwear belonging to {him_name}")
            $ Inventory.update_independent_item(himawaripantiescum, name="Soiled Panties", info=f"A pair of cum-stained pink underwear belonging to {him_name}")
            $ Inventory.update_independent_item(snacks, info=f"{him_name}'s favorite snacks. She would appreciate it as a gift")
            $ inventory.update_item(f"Snacks", info=f"{him_name}'s favorite snacks. She would appreciate it as a gift")
            $ inventory.update_item(f"{him_name}'s soiled panties", name="Soiled Panties", info=f"A pair of cum-stained pink underwear belonging to {him_name}")
            $ inventory.update_item(f"{him_name}'s panties", name="Panties", info=f"A pair of already worn pink underwear belonging to {him_name}")
            $ inventory.update_item(f"Soiled Panties", info=f"A pair of cum-stained pink underwear belonging to {him_name}")
            $ inventory.update_item(f"Panties", info=f"A pair of already worn pink underwear belonging to {him_name}")
            
            $ inventoryShop.update_item(f"Snacks", info=f"{him_name}'s favorite snacks. She would appreciate it as a gift")
            $ inventoryShop.update_item(f"Pills", info=f"A bottle of prescription pills. Thought to be a strong sedative", price=50)
            $ inventoryShop.update_item(f"Pool installation", info=f"Order a pool installation for your home")

            $ quest_him.change_quest_title("himawari1hatred","[him_name]'s Hatred path")


            #check hin love shower quest
            if quest_hin.exists("hin1L_5"): #check if quest exists
                if quest_hin.is_state("hin1L_5", "completed"): #check quest state
                    
                    $ quest_hin.check("hin1L_5", "done") #update hinata shower quest to strikethrough if already completed

            #check hin hatred sleep quest
            if quest_hin.exists("hin1H_5"):
                if quest_hin.is_state("hin1H_5", "completed"):
                    
                    $ quest_hin.check("hin1H_5", "done") #update hinata shower quest to strikethrough if already completed

            #quest titles fix (can try to change even if quest doesn't exist)
            $ quest.change_quest_title("bohim1_2","Perhaps her garments could enhance your nightly fantasies")
            # $ quest.change_quest_title("shop1_2","Spend at least $300 (WIP)")


            $ quest_him.change_quest_title("hin1L_4","Jerk off while [hin_name] 'helps' when waking up")
            $ quest_him.change_quest_title("hin1H_4","Expose yourself to [hin_name] in the laundry room")
            $ quest_him.change_quest_title("him1H_3","Soil her panties while fantasizing")

            $ quest.change_quest_title("2_bohim_2","Convince [him_name] to work with you")
            $ quest.change_quest_title("3_bohim_2","Purchase nescessary equipment")
    

            #check if him panties to complete quest
            $ himpantiscumininv = inventory.find_item_by_name(f"Soiled Panties")
            if himpantiscumininv!= None: #if inventory has cum panties
                #Himawari fantasize quest
                $ quest.check("bohim_1", "done") #marks left quest as complete (make sure any references now check if quest is completed to avoid errors)
                $ quest_him.check("him1H_3", "done") #mark fantasize hatred in hima's log complete

                $ quest.remove("[him_name]'s garments") # removes the quest from the right page (use when completed)
            

            $ print("Running version update code on load complete")

    return