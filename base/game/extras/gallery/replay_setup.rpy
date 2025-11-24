## Replay Gallery screen ######################################
##
default persistent.replay_unlocker = False
init python:
    replay_page = 0
    current_replay_category = "Everything"  # For replay gallery categories

    class ReplayItem:
        def __init__(self, thumbs, replay, name, categories="Miscellaneous", tooltip="", thumbnail=False, condition=None):
            self.thumbs = thumbs
            self.replay = replay
            self.name = name
            # Handle categories same way as gallery
            if isinstance(categories, str):
                self.categories = [categories]
            elif isinstance(categories, list):
                self.categories = categories
            else:
                self.categories = ["Miscellaneous"]
            self.tooltip = tooltip if tooltip else name
            self.thumbnail = thumbnail  # Added thumbnail flag like GalleryItem
            self.condition = condition

        def get_tooltip(self):
            
            if persistent.translationstring != 101218:
                return self.tooltip
            return self.name  

    def supb(): #edit active condition

        return name  

    def get_replay_category_thumbnail(category):
        # Find first image marked as thumbnail for this category
        for item in Replay_items:
            if category in item.categories and item.thumbnail:
                return item.thumbs[0]  # Return the first thumbnail of items marked as thumbnail
        return None

    def get_unique_replay_categories():
        category_order = ["Everything", "Miscellaneous", "Endings", "Secret Scenes", "Hinata", "Himawari", "Ino", "Tsunade", "Yoruichi", "Tenten", "Kushina", "Sakura", "Sarada", "Madame", "v019", "v020", "v021"]  
        categories = set()
        for item in Replay_items:
            categories.update(item.categories)
            if "Miscellaneous" in item.categories:
                categories.add("Miscellaneous")  # Ensure Miscellaneous is added if there are items with that category
        categories.add("Everything")  # Always add Everything category
        
        def custom_sort(x):
            try:
                return category_order.index(x)
            except ValueError:
                return len(category_order)
        return sorted(list(categories), key=custom_sort)

    def initialize_replay_defaults():
        if _in_replay:
            reconcile_stats_on_start()
            store.hin_rel_to_bo = "son"
            store.bo_name = "Boruto"
            store.bo_age = "18"
            store.bo_name_stutter = "B-boruto"
            store.hin_rel_stutter = "M-mom"
            store.na_rel_default = "Dad"
            store.na_name = "Naruto"
            store.na_rel = "Dad"
            store.na_rel_to_bo_default = "son"
            store.hin_rel_default = "Mom"
            store.hin_name = "Hinata"
            store.hin_rel = "Mom"
            store.hin_rel_mother = "Mother"
            store.hin_rel_to_bo = "son"
            store.hin_age = "36"
            store.him_name = "Himawari"
            store.him_rel = "sister"
            store.him_rel_default = "sister"
            store.him_rel_to_bo = "brother"
            store.him_age = "18"
            store.inventory = Inventory()
            store.inventoryShop = Inventory()
            store.himawaripanties = None
            if has_tier_or_higher("Jonin"):
                store.hinata_respect = 10
                store.hinata_obedience.value = 100
                store.hinata_obedience.level = 5
                store.hinata_love.value = 100
                store.hinata_love.level = 5
                store.himawari_respect = 10
                store.himawari_obedience.value = 100
                store.himawari_obedience.level = 5
                store.himawari_love.value = 100
                store.himawari_love.level = 5
                store.hatred.value = 100
                store.hatred.level = 5
                store.dominance.value = 100
                store.dominance.level = 5
                store.percentage = 100
                store.strength = 10

            if 'initialize_replay_defaults_2' in globals() and callable(initialize_replay_defaults_2):
                initialize_replay_defaults_2()
        
        else:
            return



    #add replay items here format below
    Replay_items = []
    #v21_r
    Replay_items.append(ReplayItem(["images/v21_r/hinata_end/new/v21_hin_end.webp"], "v21_rageending_hinata_replay", "Hinata's Capture - Bad Ending", categories=["Hinata","v021","Endings"], tooltip="TIP: Keep your eyes open during the third midnight after Hinata's capture! 'Hatred(30+)'", condition=None)) 
    Replay_items.append(ReplayItem(["images/v21_r/kushina/hate/toy_vibrator1_3cum.webp"], "replayjump_kushinatieherup", "Kushina's Resistance - Shibari", categories=["Kushina","v021"], tooltip="After choosing to side with Kurama, repeatedly visit Kushina and break down her resistances.", condition=None)) 

    #v21_p
    #Hinata
    Replay_items.append(ReplayItem(["images/v21_p/hinata_love/v21_sakura_endingphoto1.webp"], "hinata_blackdress_firstdatenight_reveal", "Dinner date with Hinata and Sakura (Love)", categories=["v021", "Hinata", "Sakura"], tooltip="TIP: {p}>Be on the love path {p}>Surprise Hinata with a romantic gesture in the living room during the evening", condition=None,thumbnail=True))
    Replay_items.append(ReplayItem(["images/v21_p/hinata_hatred/v21_hinatahate_hand grab 3a.webp"], "hatredlevel2_intro", "Using Hinata to jerk you off (Hate) (Part 1)", categories=["v021", "Hinata"], tooltip="TIP: {p}>Be on the hatred path {p}>Complete Hinata's hospitality quest {p}>Manipulate her into providing stress relief when she wakes you up", condition=None,thumbnail=True))
    Replay_items.append(ReplayItem(["images/v21_p/hinata_hatred/v21_hinatahate_finish_surprised_cum2.webp"], "hatredlevel2_handjob_repeatable", "Using Hinata to jerk you off (Hate) (Part 2)", categories=["v021", "Hinata"], tooltip="TIP: {p}>Be on the hatred path {p}>Manipulate Hinata twice to provide stress relief when she wakes you up", condition=None,thumbnail=True))
    Replay_items.append(ReplayItem(["images/v21_p/hinata_hatred/v21_hinatahate_povonbed2_bc.webp"], "hatredlevel2_intro_chosenlove", "Hinata lends a helping hand (Love) (Part 1)", categories=["v021", "Hinata"], tooltip="TIP: {p}>Be on the love path {p}>Complete Hinata's hospitality quest {p}>Ask her for more help when she wakes you up", condition=None,thumbnail=True))
    Replay_items.append(ReplayItem(["images/v21_p/hinata_hatred/v21_hinatahate_onbed2.webp"], "hatredlevel2_handjob_chosenlove_repeatable", "Hinata lends a helping hand (Love) (Part 2)", categories=["v021", "Hinata"], tooltip="TIP: {p}>Be on the love path {p}>Ask Hinata for more help a second time when she wakes you up", condition=None,thumbnail=True))
    Replay_items.append(ReplayItem(["images/v21_p/hinata_hatred/v20hin_handy 1_1_asleep.webp"], "v21_hinatawakeup_handjob", "Hinata lends a helping hand (Love) (Part 3)", categories=["v021", "Hinata"], tooltip="TIP: {p}>Be on the love path {p}>Previously cuddled with Hinata in bed {p}>50% chance to receive a special wakeup if you have 50 lust in the morning", condition=None,thumbnail=True))
    Replay_items.append(ReplayItem(["images/v21_p/ramenstuff/use/used/scene_intro/v21_hinata_ramenintro_customer_slap.webp"], "v21_initial_ramenintro_start", "Hinata's first shift", categories=["v021", "Hinata"], tooltip="TIP: {p}>Be on the love or hatred path {p}>Have a ramen high score above 4200 {p}>Pay your weekly debts and help Hinata get a job!", condition=None,thumbnail=True))

    #v21_a
    #Himawari
    Replay_items.append(ReplayItem(["images/v21_a/himawari_photoshoot_swimsuit/all fours 2_a.webp"], "hima_swimsuit_modelling_hatred_begin", "Himawari's Swimsuit Photoshoot (Hatred)", categories=["v021", "Himawari"], tooltip="TIP: While on the hatred path, buy the bikini from the shop and increase obedience to 35!", condition=None,thumbnail=True))
    Replay_items.append(ReplayItem(["images/v21_a/himawari_bedroom_strength_training/himawari_scared_cg.webp"], "hima_training_proper_start", "Himawari's Training Sessions (Hatred)", categories=["v021", "Himawari"], tooltip="TIP: Beat himawari at wrestling and then while on the hatred path challenge her to a squat face-off!", condition=None,thumbnail=True))
    Replay_items.append(ReplayItem(["images/v21_a/himawari_photoshoot_swimsuit/v021_hima_swimsuit_hug.webp"], "hima_swimsuit_modelling_love_begin", "Himawari's Swimsuit Photoshoot (Love)", categories=["v021", "Himawari"], tooltip="TIP: While on the love path, buy the bikini from the shop and increase obedience to 35!", condition=None,thumbnail=True))
    Replay_items.append(ReplayItem(["images/v21_a/himawari_bedroom_strength_training/hima_changing_buruma.webp"], "hima_training_proper_start_love", "Himawari's Training Sessions (Love)", categories=["v021", "Himawari"], tooltip="TIP: Beat himawari at wrestling and then while on the love path challenge her to a squat face-off!", condition=None,thumbnail=True))

    #v20

    Replay_items.append(ReplayItem(["images/v20_r/kushina/kushina_dream intro1.webp"], "naruto_held_captive", "Raikage's Plans", categories=["v020"], tooltip="TIP: Automatically unlocked on Day 13", condition=None,thumbnail=True))

    #Hinata HJ
    Replay_items.append(ReplayItem(["images/v20_r/day14/fight/hin_afterfight.webp"], "replay_hinhj_afterfight", "Hinata attempts to 'help'", categories=["Hinata","v020"], tooltip="TIP: Defeat Toji in a fight.", condition=None))
    #Kushina
    Replay_items.append(ReplayItem(["images/v20_r/kushina/kushina_dream intro1.webp"], "kuramachoice_dream", "Mind's Construct", categories=["Kushina","v020"], tooltip="TIP: Automatically unlocked on Day 12", condition=None))
    #Sarada SparringWinLose / Room Masturbation
    Replay_items.append(ReplayItem(["images/v20/sarada/Selected For Use/req_assets/sarada_masturbating2.webp"], "sarada_reintro_bargein_masturbating", "You catch Sarada masturbating", categories=["Sarada","v020"], tooltip="TIP: Increase your relationship with Sarada, then when barging into Sarada's room, you have a chance of encountering this scene!", condition=None))
    Replay_items.append(ReplayItem(["images/v20/sarada/Selected For Use/v20_sarada_spar_win_02.webp"], "sarada_sparring_win", "Sarada Sparring Victory", categories=["Sarada","v020"], tooltip="TIP: Defeat Sarada while sparring!", condition=None))
    Replay_items.append(ReplayItem(["images/v20/sarada/Selected For Use/v20_sarada_spar3.webp"], "sarada_sparring_lose", "Sarada Sparring Loss", categories=["Sarada","v020"], tooltip="TIP: Let Sarada beat you while sparring!", condition=None))
    #Succubus
    Replay_items.append(ReplayItem(["images/v20/tenten_succubus/p5_1.webp"], "lake_succubus", "The legend of the Lake Succubus", categories=["Tenten","v020"], tooltip="TIP: Find the shopkeeper's keepsake and dream during the night!", condition=None))
    #Madame/Hinata rescue mission
    Replay_items.append(ReplayItem(["images/v20/madame/onsen_intro 4_0.webp"], "madame_reward_scene", "Madame helps you rescue Hinata (Part 2)", categories=["Madame","Hinata","v020"], tooltip="TIP: After Hinata is captured, attempt to rescue her, but jump into the pool with the girls!", condition=None))
    Replay_items.append(ReplayItem(["images/v20/madame/req_assets/pool/jumponsen_intro1.webp"], "madame_pool_replay", "Madame's servants (Part 2 - Pool Fun)", categories=["Madame","v020"], tooltip="TIP: After Hinata is captured, attempt to rescue her, but jump into the pool with the girls!", condition=None))    
    Replay_items.append(ReplayItem(["images/v20/madame/rangi_secret_pathway.webp"], "ch1_d14_onsen_replay", "Madame helps you rescue Hinata", categories=["Madame","v020"], tooltip="TIP: After Hinata is captured, go and rescue her!", condition=None,thumbnail=True))
    #HinataCaptureScenes
    Replay_items.append(ReplayItem(["images/v20_r/hinata_captured/v20_hin_captured 0_2.webp"], "hinata_captured_1_replay", "Hinata's Capture Evening (Part 1)", categories=["Hinata","v020"], tooltip="TIP: Keep your eyes open during the first evening after Hinata's capture!", condition=None))
    Replay_items.append(ReplayItem(["images/v20_r/hinata_captured/v20_hin_captured 2.webp"], "hinata_captured_2_replay", "Hinata's Capture Evening (Part 2)", categories=["Hinata","v020"], tooltip="TIP: Keep your eyes open during the second evening after Hinata's capture!", condition=None))
    Replay_items.append(ReplayItem(["images/v20_r/hinata_captured/gameover/lvl2/daimyo/use/v20_daimyoend_0.webp"], "hinata_captured_3_replay", "Hinata's Capture Evening (Part 3)", categories=["Hinata","v020"], tooltip="TIP: Keep your eyes open during the third evening after Hinata's capture!", condition=None))
    Replay_items.append(ReplayItem(["images/v20_r/hinata_captured/captives/dungeon_victim 2.webp"], "hinata_captured_midnight1_replay", "Hinata's Capture Midnight (Part 1)", categories=["Hinata","v020"], tooltip="TIP: Keep your eyes open during the first midnight after Hinata's capture!", condition=None))
    Replay_items.append(ReplayItem(["images/v20_r/hinata_captured/gameover/lvl1/groped_koji/v20z_1.webp"], "hinata_captured_midnight2_replay", "Hinata's Capture Midnight (Part 2)", categories=["Hinata","v020"], tooltip="TIP: Keep your eyes open during the second midnight after Hinata's capture!", condition=None))
    Replay_items.append(ReplayItem(["images/v20_r/hinata_captured/gameover/lvl2/daimyo/use/v20_daimyoend_0test1.webp"], "hinata_captured_midnight3_replay", "Hinata's Capture Midnight (Part 3)", categories=["Hinata","v020","Endings"], tooltip="TIP: Keep your eyes open during the third midnight after Hinata's capture!", condition=None))

    #v19

    #Tenten blowjob repeatable and date hate scene
    Replay_items.append(ReplayItem(["images/v019/tenten_pendant_continuation/tenten_lake_bj_3.webp"], "tenten_lake_date_blowjob_scene_repeatable", "Tenten's Lake Date 2", categories=["Tenten","v019"], tooltip="TIP: After returning Tenten's pendant, agree to multiple dates. Ask her to help with her mouth.", condition=None))
    Replay_items.append(ReplayItem(["images/v019/tenten_pendant_continuation/tenten_lake_bj_hate6_1.webp"], "thebeastgrowls", "Tenten's Lake Date (Hate)", categories=["Tenten","v019"], tooltip="TIP: After returning Tenten's pendant, agree to multiple dates. Ask her to help with her mouth. (Hate 30)", condition=None))


    #Hinata shower interruptoin
    Replay_items.append(ReplayItem(["images/v19_r/barthroom/hinata_inside/bh_hin 3_1.webp"], "hinata_knocks_bathroom", "Hinata Shower Interruption", categories=["Hinata","v019"], tooltip="TIP: Take a shower when the bathroom is unoccupied. There's a random chance an event may occur!", condition=None))

    #Himawari shower interruptoin
    Replay_items.append(ReplayItem(["images/v19_r/barthroom/himawari/aftershower_boner 0.webp"], "himawari_outside_bathroom", "Himawari Shower Interruption", categories=["Himawari","v019"], tooltip="TIP: Take a shower when the bathroom is unoccupied. There's a random chance an event may occur!", condition=None))

    #Himawari shower knock
    Replay_items.append(ReplayItem(["images/v19_r/barthroom/himawari/fight/him_aftershower fight1.webp"], "hima_bathroom_event1_replay", "Himawari Shower Wait", categories=["Himawari","v019"], tooltip="TIP: Spy on Himawari enough times while she is showering. Then tell her you need to use the bathroom.", condition=None))

    #Hinata shower knock
    Replay_items.append(ReplayItem(["images/v19_r/barthroom/hinata_banana/slipped/carry/hin_slip carry3.webp"], "eatsomethingwhileyouwait", "Hinata Shower Wait", categories=["Hinata","v019"], tooltip="TIP: Spy on Hinata enough times while she is showering. Wait outside the bathroom for her", condition=None))

    #Hinata shower knock2 
    Replay_items.append(ReplayItem(["images/v19_r/barthroom/hinata_inside/bh_hin barge1.webp"], "replay_hinatashowerletinobedience15", "Hinata Shower Barge", categories=["Hinata","v019"], tooltip="TIP: Spy on Hinata enough times while she is showering. Convince her to let you go inside.", condition=None))

    #Hinata kitchen sneak
    Replay_items.append(ReplayItem(["images/v19_r/kitchen/approach/hinkitchen approach1.webp"], "kitchen_events_gethandsy", "Hinata Cooking Sneak", categories=["Hinata","v019"], tooltip="TIP: Sneak behind Hinata while she is cooking in the Kitchen.", condition=None))

    #Hinata kitchen motorboat
    Replay_items.append(ReplayItem(["images/v19_r/kitchen/approach/motorboat/approach_motorboat 2.webp"], "cryonherchest_motro_replay", "Hinata Cooking Sneak (Love)", categories=["Hinata","v019"], tooltip="TIP: Sneak behind Hinata while she is cooking in the Kitchen. 'Cry' on her chest.", condition=None))
    #Kitchen eat evening
    Replay_items.append(ReplayItem(["images/v19_r/kitchen/food/eattogether1 peek0.webp"], "kitchen_events_eatafternoon", "Kitchen Lunch", categories=["Hinata","Himawari","v019"], tooltip="TIP: Ask Hinata to cook something while she is in the kitchen. Drop your fork a few times...", condition=None))


    #Sakura Winedate1
    Replay_items.append(ReplayItem(["images/v19_r/sakura_midnight/sakurwine intro1_1.webp"], "sakura_wine_date", "Sakura Midnight Visit", categories=["Sakura","v019"], tooltip="TIP: Improve your relationship with Sakura. Have her ask you to purchase wine. Purchase win and visit her during midnight.", condition=None))
    #Sakura Winedate2
    Replay_items.append(ReplayItem(["images/v19_r/sakura_midnight/sakurwine intro1.webp"], "sakura_wine_date2", "Sakura Midnight Visit 2", categories=["Sakura","v019"], tooltip="TIP: Improve your relationship with Sakura. Have her ask you to purchase wine. Purchase win and visit her during midnight.", condition=None))




    #clown ending
    Replay_items.append(ReplayItem(["images/v19_r/barthroom/hinata_banana/boruto_banana 0.webp"], "clownending_boruto", "Boruto is Cancelled", categories=["Endings","v019"], tooltip="Spy on Hinata enough times while she is showering. Wait outside the bathroom for her. Joke about bananas...", condition=None))




    #Tenten Lake Date
    Replay_items.append(ReplayItem(["images/v019/tenten_pendant_continuation/tenten_lookaway_1.webp"], "tenten_lake_date_start_repeatable", "Tenten's Lake Date", categories=["Tenten","v019"], tooltip="TIP: After returning Tenten's pendant, agree to a date. This is the main lake date event.", condition=None))
    #Tenten extort hatred
    Replay_items.append(ReplayItem(["images/v019/tenten_pendant_continuation/new/tenten_pendantdangle1_3angry.webp"], "tenten_pendant_extort_start", "Tenten's Pendant - Extortion (Hatred)", categories=["Tenten","v019"], tooltip="TIP: After finding Tenten's pendant, choose to extort her down the hatred path.", condition=None))
    #Tenten extort dom
    Replay_items.append(ReplayItem(["images/v019/tenten_pendant_continuation/new/tenten_pendantdangle1_3.webp"], "tenten_pendant_dom", "Tenten's Pendant - Extortion (Dominance)", categories=["Tenten","v019"], tooltip="TIP: After finding Tenten's pendant, choose to extort her down the dominance path.", condition=None))
    #Tsunades_discovery_femdom
    Replay_items.append(ReplayItem(["images/v019/tsunade_discovery/sub/tsunadiscsub_7_cum.webp"], "tsunade_discovery_treatment_sub_repeat", "Tsunade's Discovery - Submissive Treatment", categories=["Tsunade","v019"], tooltip="TIP: Triggered when semen quantity reaches 30. Tsunade explains her findings and provides 'treatment' while she is dominant.", condition=None))
    #Tsunades_discovery_maledom
    Replay_items.append(ReplayItem(["images/v019/tsunade_discovery/dom/tsunadiscdom_9.webp"], "tsunade_discovery_treatment_dom_repeat", "Tsunade's Discovery - Dominant Treatment", categories=["Tsunade","v019"], tooltip="TIP: Triggered when semen quantity reaches 30. Tsunade explains her findings, but Boruto takes control.", condition=None))

    #v18
    Replay_items.append(ReplayItem(["images/v5/Himawari/Working/sexy/hima_model_sexy feet2_look.webp"], "himawari_repeatable_menu_photo", "Himawari's Photoshoot", categories=["Himawari"], tooltip="TIP: TIP: Keep visiting Himawari in her bedroom until you complete all trust objectives{p}>Requires you to purchase Blindfold, Camera{p}>Requires Yoruichi's relationship set to at least Obedient",condition=None))
    Replay_items.append(ReplayItem(["images/v5/SAKURA/final/sakura_lr 1.webp"], "sakura_lesson1", "Visiting Auntie Sakura", categories=["Sakura"], tooltip="TIP: Train until you reach level 1{p}>Visit the Uchiha household and choose to spend time with Sakura{p}>Improve your relation ship with her by visiting her again",condition=None))
    Replay_items.append(ReplayItem(["images/v5/SAKURA/final/sakura_lr 4_3.webp"], "sakura_lesson2", "Sakura's Teachings", categories=["Sakura"], tooltip="TIP: Train until you reach level 1{p}>Visit the Uchiha household and choose to spend time with Sakura{p}>Have your lust maxed out during her final lesson",condition=None))
    Replay_items.append(ReplayItem(["images/v5/SAKURA/final/sarada/sarada_barge 1_2.webp"], "visit_sarada", "Sarada's Feelings", categories=["Sarada"], tooltip="TIP: Train until you reach level 1{p}>Visit the Uchiha household and choose to spend time with Sarada{p}>Barge in",condition=None))
    Replay_items.append(ReplayItem(["images/v5/tenten/final/tenten stuck0.webp"], "tenten_qauest_menu_start_replay", "Tenten's Troubles", categories=["Tenten"], tooltip="TIP: Keep tapping on the shopkeeper until she is annoyed with you{p}>Visit the shopkeeper after a few days",condition=None,thumbnail=True))


    #testing
    # Replay_items.append(ReplayItem(["images/intro storyboard/day1/intro/ninjawar/war/war3.webp"], "introwartestt", "War Intro", categories=["Miscellaneous"], tooltip="TIP: Automatically unlocked by progressing through the story",thumbnail=True,condition=None))

    
    #misc
    Replay_items.append(ReplayItem(["images/intro storyboard/day1/intro/ninjawar/war/war3.webp"], "introwartest", "War Intro", categories=["Miscellaneous"], tooltip="TIP: Automatically unlocked by progressing through the story",thumbnail=True,condition=None))

    #secret
    #ending
    Replay_items.append(ReplayItem(["images/v4/hima_gameover/himapregnant1.webp"], "hima_gameover_wrestling", "Himawari's Bad Ending 1", categories=["Endings", "Himawari", "Secret Scenes"], tooltip="TIP:{p}>Increase your Strength to a certain threshold{p}>When she interrupts your training, select 'Hatred(20+)' related options{p}>A unique option will be present when your 'Lust(80+)' is high enough",condition=None))

    #hima scenes 
    


    Replay_items.append(ReplayItem(["images/intro storyboard/day1/intro/himawari/hima intro3_1.webp"], "himaintroreplay", "Himawari's Introduction", categories=["Himawari"], tooltip="TIP: Automatically unlocked by progressing through the story{p}",thumbnail=True,condition=None))
    Replay_items.append(ReplayItem(["images/characters/hima/livingroom/workin/himaintro stand2.webp"], "v1_secret_himawarisecretscene", "Return from Ninja Academy", categories=["Himawari"], tooltip="TIP: Automatically unlocked by progressing through the story",condition=None))
    Replay_items.append(ReplayItem(["images/characters/hima/livingroom/workin/himaintro_s 1.webp"], "replay_testing", "Himawari - Secret Scene 1", categories=["Secret Scenes","Himawari"], tooltip="TIP:{p}>Ponder Idly during the intro{p}>Be respectful when Himawari stops you before you leave the house{p}>Purchase Himawari's favorite snacks{p}>Be respectful when Himawari returns home from the Ninja Academy{p}>Give her the snacks",condition=None))
    
    Replay_items.append(ReplayItem(["images/characters/hima/bathroom/lvl1/himabathroomstart.webp"], "himabathroompeakfirst", "Shower Scene 1", categories=["Himawari"], tooltip="TIP: Spy on Himawari while she is showering",condition=None))
    Replay_items.append(ReplayItem(["images/characters/hima/bathroom/lvl1/himabathroom2.webp"], "replay_himabathroompeakfirst", "Shower Scene 2", categories=["Himawari"], tooltip="TIP: Keep spying on Himawari while she is showering",condition=None))
    Replay_items.append(ReplayItem(["images/fantasize/himawari/schl/hinafantasize_schl 6.webp"], "replay_littlecocktease", "Fantasize - Little cocktease", categories=["Himawari"], tooltip="TIP: Fantasize during nights",condition=None))
    Replay_items.append(ReplayItem(["images/fantasize/himawari/beach/himafantasize_f2_1.webp"], "replay_himasecretpanties", "Himawari - Secret Scene 1", categories=["Himawari"], tooltip="TIP: Steal an item from Himawari's bedroom and use it to fantasize during nights",condition=None))

    Replay_items.append(ReplayItem(["images/v2/clothe_store/hima_storewalk3.webp"], "replay_visitclothingstore", "Clothing Store Visit", categories=["Himawari"], tooltip="TIP:{p}>Achieve a score of 4200 or higher during a work shift{p}>Redeem Obo's Story 1 from the 'Rewards' section in Work Menu{p}>Talk to Himawari when she is in the living room",condition=None))
    Replay_items.append(ReplayItem(["images/v2/hima_store/dress_tryout/clothdress peekt.webp"], "trydress_love", "Clothing Store Visit (Love)", categories=["Himawari"], tooltip="TIP: Choose 'Love(3)' related options during the clothing store event",condition=None))
    Replay_items.append(ReplayItem(["images/v2/hima_store/dress_tryout/clothdress intro.webp"], "replay_trydress_hatred", "Clothing Store Visit (Hatred)", categories=["Himawari"], tooltip="TIP: Choose 'Hatred(0)' related options during the clothing store event",condition=None))

    Replay_items.append(ReplayItem(["images/v3/hima_bedroom/blindfold/himablindfold 1_1.webp"], "replay_blindfoldtaste1", "Blindfold Taste Test 1", categories=["Himawari"], tooltip="TIP:{p}>Earn Himawari's trust by interacting wit her when she is in her bedroom{p}>Purchase a blindfold{p}>Convince Himawari to help you with your recipe",condition=None))
    Replay_items.append(ReplayItem(["images/v3/hima_bedroom/blindfold/himablindfold 1.webp"], "replay_blindfoldtaste2", "Blindfold Taste Test 2", categories=["Himawari"], tooltip="TIP:{p}>Keep asking Himawari for help with your recipe...",condition=None))
    Replay_items.append(ReplayItem(["images/v3/hima_bedroom/blindfold/working/hima_crawl1.webp"], "replay_blindfoldtaste3", "Blindfold Taste Test 3", categories=["Himawari"], tooltip="TIP:{p}>Keep asking Himawari for help with your recipe...",condition=None))
    Replay_items.append(ReplayItem(["images/v3/hima_bedroom/blindfold/working/hima_force1.webp"], "replay_blindfoldtaste_hate", "Blindfold Taste Test (Hatred)", categories=["Himawari", "Secret Scenes"], tooltip="TIP:{p}>Ask Himawari to help you with your recipe once more{p}>You'll be presented with a special option when your 'Hatred(30+)' and 'Lust(80+)' are high enough.",condition=None))
    Replay_items.append(ReplayItem(["images/v3/hima_bedroom/blindfold/working/hima_suck1.webp"], "replay_blindfoldtaste_love", "Blindfold Taste Test (Love)", categories=["Himawari", "Secret Scenes"], tooltip="TIP:{p}>Ask Himawari to help you with your recipe once more{p}>You'll be presented with a special option when your 'Love(3+)' and 'Lust(80+)' are high enough.",condition=None))

    Replay_items.append(ReplayItem(["images/v3/hima_bedroom/kiss/kiss_force1.webp"], "replay_himakiss", "Kissing 'Prank'", categories=["Himawari"], tooltip="TIP:{p}>Give some money to Himawari when interacting wit her in her bedroom{p}>Pull a 'prank' on her when she tries to kiss your cheek{p}>Choose 'Dominance(3+)' related options",condition=None))

    Replay_items.append(ReplayItem(["images/v3/strength/hima_interrupts/dom/wrestle1_tickle1.webp"], "replay_wrestlingdom", "Tame Wrestling", categories=["Himawari"], tooltip="TIP:{p}>Train in your Bedroom when Himawari while Himawari is home and awake{p}>Build enough 'Strength' to wrestle her off{p}>Pin her against the wall",condition=None))
    Replay_items.append(ReplayItem(["images/v3/strength/hima_interrupts/int4.webp"], "replay_wrestlinghate", "Aggressive Wrestling", categories=["Himawari"], tooltip="TIP:{p}>Train in your Bedroom when Himawari while Himawari is home and awake{p}>Build enough 'Strength' to wrestle her off{p}>Be antagonistic when she comes to complain and choose 'Hatred(20+) related options",condition=None))


    #Hinata
    Replay_items.append(ReplayItem(["images/intro storyboard/day1/intro/dream/working/dream hinaleash1.webp"], "nap", "Nightmare", categories=["Hinata"], tooltip="TIP: Automatically unlocked by progressing through the story",condition=None))
    Replay_items.append(ReplayItem(["images/intro storyboard/day1/intro/hinata/hina intro00.webp"], "intro_hinataintroduction", "Hinata's Introduction", categories=["Hinata"], tooltip="TIP: Automatically unlocked by progressing through the story",thumbnail=True,condition=None))
    Replay_items.append(ReplayItem(["images/intro storyboard/secretscenes/introlove/secretbath1.jpg"], "secretscenelove", "Hinata - Secret Scene 1(Love)", categories=["Secret Scenes", "Hinata"], tooltip="TIP:{p}>Have at least 'Love(4)' with Hinata{p}>Select 'love' related options after returning home from the infirmary during Day 1",condition=None))
    Replay_items.append(ReplayItem(["images/intro storyboard/secretscenes/introhatred/sleep/ass/afinal ass1.webp"], "replay_secretscenehate", "Hinata - Secret Scene 1(Hatred)", categories=["Secret Scenes","Hinata"], tooltip="TIP:{p}>Have at least 'Hatred(12)'{p}>Select 'hatred' related options after returning home from the infirmary during Day 1",condition=None))
    Replay_items.append(ReplayItem(["images/intro storyboard/day1/intro/moneyproblems/hina opendoor1.webp"], "replay_ch1_d1_moneyproblems_mainstory", "First encounter with thugs", categories=["Hinata"], tooltip="TIP: Automatically unlocked by progressing through the story",condition=None))
    Replay_items.append(ReplayItem(["images/characters/hina/bathroom/lvl1/bathroom hinapeak1.webp"], "hinabathroompeakfirst", "Shower Scene 1", categories=["Hinata"], tooltip="TIP: Spy on Hinata while she is showering",condition=None))
    Replay_items.append(ReplayItem(["images/v4/hina_fantasize/hinata_ndream_end1.webp"], "narutoisback_nonntr", "Naruto is back!", categories=["Hinata"], tooltip="TIP: Dream during nights (NTR Disabled)",condition=None))
    Replay_items.append(ReplayItem(["images/v4/hina_fantasize/hinata_ndream_end1_2.webp"], "replay_narutoisback", "Naruto... is back?", categories=["Hinata"], tooltip="TIP: Dream during nights (NTR Enabled)",condition=None))
    Replay_items.append(ReplayItem(["images/fantasize/hinata/hinafantasize 2.webp"], "replay_anightout", "Fantasize - A night out", categories=["Hinata"], tooltip="TIP: Fantasize during nights",condition=None))
    
    Replay_items.append(ReplayItem(["images/v2/day7/working/mp_v1_1.webp"], "replay_ch1_day7_konohaoutskirts", "Second encounter with thugs", categories=["Hinata"], tooltip="TIP: Triggers on Day 7",condition=None))
    Replay_items.append(ReplayItem(["images/v2/day7/bh c4.webp"], "replay_rangikuintro", "The Daimyo's concubine", categories=["Hinata"], tooltip="TIP: Triggers on Day 7 (Accept the Madame's advances)",condition=None))
    Replay_items.append(ReplayItem(["images/v2/day7/audience/daimyo 3.png"], "replay_daimyointroduction", "Hinata meets the Daimyo", categories=["Hinata"], tooltip="TIP:{p}>Paying off the debt will prevent the Daimyo from disrespecting Hinata{p}Answering his questions gracefully will prevent the Daimyo from humiliating Hinata",condition=None))
    Replay_items.append(ReplayItem(["images/v2/day7/audience/daimyo apologize final1.png"], "daimyo_cruelapology", "Hinata's Humiliation (Debts Unpaid)", categories=["Hinata"], tooltip="TIP:{p}>Leave the debt unpaid{p}>Anger the Daimyo by answering his questions disrespectfully",condition=None))


    Replay_items.append(ReplayItem(["images/v2/hina_massage/fm2_start2_3.webp"], "usenewfoundknowledge", "Helping Hinata Relax", categories=["Hinata"], tooltip="TIP:{p}>Prove to Hinata you are a competent masseur{p}>Purchase a Massage Guide from the shop and read it to increase your knowledge{p}>Convince Hinata to allow you to massage her",condition=None))
    Replay_items.append(ReplayItem(["images/v2/hina_massage/01footjob_cum4.webp"], "replay_hinatafootjobpills", "Helping Hinata 'Relax'(Sedate)", categories=["Hinata"], tooltip="TIP:{p}>Prove to Hinata you are a competent masseur{p}>Purchase a Massage Guide from the shop and read it to increase your knowledge{p}>Convince Hinata to allow you to massage her{p}>Purchase Pills from the shop and use them to sedate Hinata",condition=None))

    Replay_items.append(ReplayItem(["images/v4/hinata/minigame/squatform3.webp"], "hinata_squat_label", "Squat Form Tips", categories=["Hinata"], tooltip="TIP:{p}>Increase your strength to a certain threshold{p}>Out-squat Hinata when training together in her bedroom{p}>Offer to help with her squat form",condition=None))
    Replay_items.append(ReplayItem(["images/v4/hinata/watch/watch3.webp"], "hinata_stretch_label", "Stretching Tips", categories=["Hinata"], tooltip="TIP:{p}>Increase your strength to a certain threshold{p}>Out-squat Hinata when training together in her bedroom{p}>Offer to help with stretching",condition=None))
    Replay_items.append(ReplayItem(["images/v4/hinata/watch/watch5.webp"], "hinatawatchnormal", "Watching Hinata's Routine", categories=["Hinata"], tooltip="TIP:{p}>Ask Hinata to train with you while she is in her bedroom{p}>Hinata will decline your offer if her 'Respect(-1) is low enough{p}>Choose to watch her train instead{p}>Can also chose to watch her after out-squatting her",condition=None))
    Replay_items.append(ReplayItem(["images/v4/hinata/watch/watch4.webp"], "hinatawatchhate", "Watching Hinata's Routine (Hate)", categories=["Hinata"], tooltip="TIP:{p}>Ask Hinata to train with you while she is in her bedroom{p}>Hinata will decline your offer if her 'Respect(-1) is low enough{p}>Pick 'Hatred' related options(25)",condition=None))


    #Yoruichi
    Replay_items.append(ReplayItem(["images/characters/headshots/npcs/yoruichi/nightscenes/1/ramen_nightscene1_7.webp"], "yoru_replay_nightscene1", "Yoruichi's Secret 1", categories=["Yoruichi"], tooltip="TIP:{p}>Improve your relationship with Yoruichi to at least 'Formal'{p}>Interact with her until she shares critical information{p}>Uncover her secret by visiting her workplace during nights",thumbnail=True,condition=None))
    Replay_items.append(ReplayItem(["images/characters/headshots/npcs/yoruichi/nightscenes/2/ramen_nightscene2_7.webp"], "yoru_replay_nightscene2", "Yoruichi's Secret 2", categories=["Yoruichi"], tooltip="TIP:{p}>Improve your relationship with Yoruichi to at least 'Formal'{p}>Interact with her until she shares critical information{p}>Keep visiting her workplace during nights until you discover her secret",condition=None))
    Replay_items.append(ReplayItem(["images/characters/headshots/npcs/yoruichi/oboquest/shout.webp"], "score_3", "Three Commandments", categories=["Yoruichi"], tooltip="TIP:{p}>Reach a high-score of at least 3800 in the ramen shop{p}>Unlock 'Yoruichi's Story 2' from the rewards panel",condition=None))
    Replay_items.append(ReplayItem(["images/characters/headshots/npcs/yoruichi/oboquest/TITS/secret/yorusecretabove0.webp"], "yoruintro_kneel", "Abuse the Rules", categories=["Yoruichi", "Secret Scenes"], tooltip="TIP:{p}>During the events of 'Yoruichi's Story 2', take advantage of Obo's idea{p}>Command Yoruichi to show you her bare chest{p}>Command Yoruichi to get on her knees{p}>A secret option will be available if your 'Lust(100)' is maxed out",condition=None))

    Replay_items.append(ReplayItem(["images/v4/yoruichi/model1/yorum_intro0.webp"], "yoru_first_photoshoot", "Yoruichi's Photoshoot (Unwilling)", categories=["Yoruichi"], tooltip="TIP:{p}>Have your relationship with Yoruichi set to 'Unwillingly Obedient'{p}>Purchase a camera and talk with Yoruichi about your idea",thumbnail=True,condition=None))
    Replay_items.append(ReplayItem(["images/v4/yoruichi/model1/bed/front/yoru_bed_frontstart.webp"], "yoru_first_photoshoot_love", "Yoruichi's Photoshoot (Love)", categories=["Yoruichi"], tooltip="TIP:{p}>Have your relationship with Yoruichi set to 'Obedient'{p}>Purchase a camera and talk with Yoruichi about your idea",condition=None))
    Replay_items.append(ReplayItem(["images/v4/yoruichi/model1/fj/yoru_p1_footjob1.webp"], "replay_yoru_firstphotoshoot_footjob", "Yoruichi's Photoshoot Footjob (Love)", categories=["Yoruichi"], tooltip="TIP:{p}>Have your relationship with Yoruichi set to 'Obedient'{p}>Have at least 'Lust(80)' before Yoruichi's photoshoot comes to an end",condition=None))

    Replay_items.append(ReplayItem(["images/v4/yoruichi/model1/tj/yoru_photo_behind1_1.webp"], "replay_yoru_firstphotoshoot_blackmail", "Yoruichi's Photoshoot (Blackmail)", categories=["Yoruichi"], tooltip="TIP:{p}>Have your relationship with Yoruichi set to 'Unwillingly Obedient'{p}>Choose to blackmail 'Hatred(30)' Yoruichi when the photoshoot comes to an end{p}>Have at least 'Strength(1)' and 80/100 points to be able to overpower Yoruichi{p}>Choose 'Dominance' related options",condition=None))
    Replay_items.append(ReplayItem(["images/v4/yoruichi/model1/tj/yoru_photo_h_end3.webp"], "replay_yoru_firstphotoshoot_dominance", "Yoruichi's Photoshoot (Dominate)", categories=["Yoruichi"], tooltip="TIP:{p}>Have your relationship with Yoruichi set to 'Unwillingly Obedient'{p}>Choose 'Dominance(25)' related options",condition=None))


    #Ino
    Replay_items.append(ReplayItem(["images/intro storyboard/day1/intro/ino/ino sitting.webp"], "inointroscene", "Encounter with Ino", categories=["Ino"], tooltip="TIP: Automatically unlocked by progressing through the story",thumbnail=True,condition=None))

    #Tsunade
    Replay_items.append(ReplayItem(["images/intro storyboard/day1/intro/tsunade/n7.webp"], "replaytsunadenaruto", "Tsunade's past with Naruto", categories=["Tsunade"], tooltip="TIP: Automatically unlocked by progressing through the story",condition=None))
    Replay_items.append(ReplayItem(["images/intro storyboard/day1/intro/tsunade/boruto waking2.webp"], "replaytsunadeboruto1", "First Infirmary Visit", categories=["Tsunade"], tooltip="TIP: Automatically unlocked by progressing through the story",thumbnail=True,condition=None))
    Replay_items.append(ReplayItem(["images/intro storyboard/day1/intro/tsunade/working/pretend1.webp"], "replaytsunade_pretendasleep", "Tsunade - Pretend to be asleep", categories=["Tsunade"], tooltip="TIP: Pretend you are still asleep after you wake up in the infirmary",condition=None))
    Replay_items.append(ReplayItem(["images/intro storyboard/day1/intro/tsunade/tsunade ending choice.webp"], "tsunadereplay_pullher", "Tsunade - Pull her towards you", categories=["Tsunade"], tooltip="TIP: Pull Tsunade towards you after you wake up in the infirmary",condition=None))
    #Tsunade Dom
    Replay_items.append(ReplayItem(["images/v2/tsunade_revisit/intro/ts_intro5.webp"], "replay_visittsunade2", "Second Infirmary Visit", categories=["Tsunade"], tooltip="TIP: Automatically unlocked by progressing through the story",condition=None))
    Replay_items.append(ReplayItem(["images/v2/tsunade_revisit/dom/lvl1/infirmary_dom_lvl1_6.webp"], "replay_infirmary_domstart1", "Tsunade's extraction 1 (Sub)", categories=["Tsunade"], tooltip="TIP:{p}>Select 'Dominance(10)' related options during your visits to Tsunade{p}>Have Tsunade's demeanor below -20 (Submissive)",condition=None))
    Replay_items.append(ReplayItem(["images/v2/tsunade_revisit/dom/lvl2/tsuna_dom2_anim3.webp"], "replay_infirmary_domstart2", "Tsunade's extraction 2 (Sub)", categories=["Tsunade"], tooltip="TIP:{p}>Select 'Dominance(18)' related options during your visits to Tsunade{p}>Have Tsunade's demeanor below -30 (Submissive)",condition=None))
    #Tsunade Sub
    Replay_items.append(ReplayItem(["images/v2/tsunade_revisit/sub/start3.webp"], "replay_infirmary_substart1", "Tsunade's extraction 1 (Dom)", categories=["Tsunade"], tooltip="TIP:{p}>Select non-dominance related options during your visits to Tsunade",condition=None))
    Replay_items.append(ReplayItem(["images/v2/tsunade_revisit/sub/lvl1/repeat4.webp"], "replay_infirmary_substart2", "Tsunade's extraction 2 (Dom)", categories=["Tsunade"], tooltip="TIP:{p}>Select non-dominance related options during your visits to Tsunade{p}>Have Tsunade's demeanor above 25 (Dominant)",condition=None))


    #kushina
    Replay_items.append(ReplayItem(["images/intro storyboard/day2/dreamsequence/kushina/dreamkushina1.webp"], "kushinadream", "Jinchūriki's Curse", categories=["Kushina"], tooltip="TIP: Triggers after going to sleep before Day 2",thumbnail=True,condition=None))

    #Sakura
    Replay_items.append(ReplayItem(["images/v4/saradaintro/sakuraintro1_2.webp"], "saradasakuraintroduction", "Sakura's Introduction", categories=["Sakura"], tooltip="TIP: Triggers the next time you train after leveling 'Strength(1) and acquiring more than 20/100 points",thumbnail=True,condition=None))
    Replay_items.append(ReplayItem(["images/intro storyboard/day2/dreamsequence/kushina/sakura2.webp"], "kushinadream", "Jinchūriki's Curse", categories=["Sakura"], tooltip="TIP: Triggers after going to sleep before Day 2",condition=None))

    #Sarada
    Replay_items.append(ReplayItem(["images/v4/saradaintro/saradaintro1.webp"], "saradasakuraintroduction", "Sarada's Introduction", categories=["Sarada"], tooltip="TIP: Triggers the next time you train after leveling 'Strength(1)' and acquiring more than 20/100 points",thumbnail=True,condition=None))
    Replay_items.append(ReplayItem(["images/intro storyboard/day2/dreamsequence/kushina/dreamsarada1.webp"], "kushinadream", "Jinchūriki's Curse", categories=["Sarada"], tooltip="TIP: Triggers after going to sleep before Day 2",condition=None))

# a black background screen for the selection
image black = "#000000"












screen replay_category_select():
    tag menu
    
    default categories = get_unique_replay_categories()
    
    add "black"
    text "Scene Gallery" size 40 xalign 0.5 color "#fff"
    



    frame:
        background "#0008"
        margin (50, 50)
        xfill True
        yfill True
        
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            xfill True
            yfill True
            
            vbox:
                spacing 20
                xfill True
                
                
                $ rows = (len(categories) + 2) // 3  # Changed to divide by 3 for 3 columns
                grid 3 rows:  # Changed to 3 columns
                    spacing 20
                    xsize 1150  # Increased width to accommodate 3 columns
                    xalign 0.5
                    
                    for category in categories:
                        $ unlocked, total = get_replay_category_counts(category)
                        frame:
                            background "#fff"
                            padding (2, 2)
                            margin (5, 5)
                            
                            fixed:
                                xysize (350, 180)  # Kept same thumbnail size
                                if category == "Everything":
                                    imagebutton:
                                        idle Transform("images/characters/kurama/kurama2.webp", size=(350, 180), alpha=1.0)
                                        hover Transform("images/characters/kurama/kurama2.webp", size=(350, 180), alpha=0.8)
                                        action [SetVariable("replay_page", 0),
                                                SetVariable("current_replay_category", category),
                                                Show("replay_gallery")]
                                        style "gallery_button"
                                        xalign 0.5
                                        yalign 0.5
                                        hover_sound "audio/soun_fx/select2.opus"
                                        activate_sound "audio/soun_fx/select4.opus"
                                if category == "Endings":
                                    imagebutton:
                                        idle Transform("images/intro storyboard/disclaimers/disclameimerintro.jpg", size=(350, 180), alpha=1.0)
                                        hover Transform("images/intro storyboard/disclaimers/disclameimerintro.jpg", size=(350, 180), alpha=0.8)
                                        action [SetVariable("replay_page", 0),
                                                SetVariable("current_replay_category", category),
                                                Show("replay_gallery")]
                                        style "gallery_button"
                                        xalign 0.5
                                        yalign 0.5
                                        hover_sound "audio/soun_fx/select2.opus"
                                        activate_sound "audio/soun_fx/select4.opus"

                                if category == "Secret Scenes":
                                    imagebutton:
                                        idle Transform("images/intro storyboard/secretscenes/introhatred/sleep/ass/afinal ass1.webp", size=(350, 180), alpha=1.0)
                                        hover Transform("images/intro storyboard/secretscenes/introhatred/sleep/ass/afinal ass1.webp", size=(350, 180), alpha=0.8)
                                        action [SetVariable("replay_page", 0),
                                                SetVariable("current_replay_category", category),
                                                Show("replay_gallery")]
                                        style "gallery_button"
                                        xalign 0.5
                                        yalign 0.5
                                        hover_sound "audio/soun_fx/select2.opus"
                                        activate_sound "audio/soun_fx/select4.opus"
                                
                                if category == "v019":
                                    imagebutton:
                                        idle Transform("images/v19_r/barthroom/hinata_banana/slipped/carry/hin_slip carry2.webp", size=(350, 180), alpha=1.0)
                                        hover Transform("images/v19_r/barthroom/hinata_banana/slipped/carry/hin_slip carry2.webp", size=(350, 180), alpha=0.8)
                                        action [SetVariable("replay_page", 0),
                                                SetVariable("current_replay_category", category),
                                                Show("replay_gallery")]
                                        style "gallery_button"
                                        xalign 0.5
                                        yalign 0.5
                                        hover_sound "audio/soun_fx/select2.opus"
                                        activate_sound "audio/soun_fx/select4.opus"

                                if category == "v020":
                                    imagebutton:
                                        idle Transform("images/v20_r/kushina/kushina_dream intro1.webp", size=(350, 180), alpha=1.0)
                                        hover Transform("images/v20_r/kushina/kushina_dream intro1.webp", size=(350, 180), alpha=0.8)
                                        action [SetVariable("replay_page", 0),
                                                SetVariable("current_replay_category", category),
                                                Show("replay_gallery")]
                                        style "gallery_button"
                                        xalign 0.5
                                        yalign 0.5
                                        hover_sound "audio/soun_fx/select2.opus"
                                        activate_sound "audio/soun_fx/select4.opus"

                                else:
                                    $ thumbnail = get_replay_category_thumbnail(category)
                                    if thumbnail:
                                        imagebutton:
                                            if unlocked == 0:
                                                idle Transform(thumbnail, 
                                                    size=(350, 180), 
                                                    alpha=1.0,
                                                    matrixcolor=Matrix([0.5, 0.0, 0.0, 0.0,
                                                                    0.0, 0.5, 0.0, 0.0,
                                                                    0.0, 0.0, 0.5, 0.0,
                                                                    0.0, 0.0, 0.0, 1.0]))
                                                hover Transform(thumbnail, 
                                                    size=(350, 180), 
                                                    alpha=0.8,
                                                    matrixcolor=Matrix([0.5, 0.0, 0.0, 0.0,
                                                                    0.0, 0.5, 0.0, 0.0,
                                                                    0.0, 0.0, 0.5, 0.0,
                                                                    0.0, 0.0, 0.0, 1.0]))
                                                action [SetVariable("replay_page", 0),
                                                    SetVariable("current_replay_category", category),
                                                    Show("replay_gallery")]
                                            else:
                                                idle Transform(thumbnail, size=(350, 180), alpha=1.0)
                                                hover Transform(thumbnail, size=(350, 180), alpha=0.8)
                                                action [SetVariable("replay_page", 0),
                                                    SetVariable("current_replay_category", category),
                                                    Show("replay_gallery")]
                                            hover_sound "audio/soun_fx/select2.opus"
                                            activate_sound "audio/soun_fx/select4.opus"
                                
                                text category:
                                    xalign 0.5
                                    yalign 0.5
                                    size 24
                                    color "#fff"
                                    outlines [(2, "#000", 0, 0)]
                                
                                text f"({unlocked}/{total})":
                                    xalign 0.5
                                    yalign 0.9
                                    size 20
                                    color "#fff"
                                    outlines [(2, "#000", 0, 0)]

                    # Fill remaining grid slots with null if needed
                    for i in range(len(categories), rows * 3):
                        null

    textbutton "{color=#000}Return{/color}" style "powerup_button":
        action Return()
        xalign 0.5
        yalign 0.98
        background "#fff8"
        hover_background "#fffa"
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"