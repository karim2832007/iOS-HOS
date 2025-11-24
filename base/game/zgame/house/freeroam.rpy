init:
    # Global variables for tracking the day part and the current day
    $ day_part = 1  # 1 = morning, 2 = noon, 3 = night
    $ day_part_names =  ["Morning", "Evening", "Night"]
    $ day_number = 0
    $ day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    $ day_name = "Monday" #variable that stores the name of the day
    $ day_part_name = "Night" #variable that stores day state

default firstday = False

#one time events on wakeup here
label house:
    $ playmusic("audio/ost/house2.opus",0.6)
    call hidemarketUI from _call_hidemarketUI
    if hin_captured_gameover == True:
        "You have failed to rescue [hin_name]."
        "The next time you visit the Daimyo's plot, your fate will be sealed."
    if completed_intro == 4:
        $ completed_intro += 1
        jump action_taken  #hacky way to fix time/day text display

    if day_number == 14 and ch1_d14_moneyproblems_completion == False:
        jump ch1_d14_moneyproblems

    if day_number > 14 and (day_number - 14) % 7 == 0  and day_part == 1:
        jump ch1_d14_moneyproblems

    if day_number == 1 and day_part == 1 and firstday == False:  #story Day1 money probs
        scene bg bb day with dissolve
        show boruto normal with dissolve
        bo"*Yawn..."
        if introsecrethatredcummed == True:
            show boruto surprised2 with vpunch
            bo"I am ... alive!"
            show boruto sceeming with dissolve
            bo"Which must mean [hin_rel] has no idea!"
        show boruto normal with dissolve
        bo"First day of waking up with my condition..."
        show boruto smirk with dissolve
        bo"It feels... surprsingly normal."
        if introsecrethatredcummed == True:
            show boruto sceeming3 with dissolve
            bo"Besides of course the fact that i relieved myself on [hin_rel] last night."
            show boruto sceeming2 with dissolve
            bo"Maybe that's why I am not feeling as bad..."
        
        if secretscenelovehandjob == True:
            show boruto worried2 with dissolve
            bo"But maybe that's because [hin_rel] helped take care of my... problem yesterday."
            show boruto worried with dissolve
            bo"I wonder... Will I keep running into similar situations? And if [hin_rel] won't help again... what the hell do I do?"
            bo"*Sigh*"
        show boruto normal with dissolve
        bo"Well then, better get on with it."
        hide boruto with dissolve
        $ firstday = True
        scene bg day with dissolve:
            zoom 0.70
        jump ch1_d1_moneyproblems

    if day_number == 7 and day_part == 1 and ch1_dy_200paid == False and ch1_d7_hatredpath == False and ch1_dy_love_nopay == False: #day 7 money problems
        jump ch1_d7_moneyproblems_mainstory

    if day_number >=8 and day_part == 1 and tsunadeintroduction == False: #day 8 infirmary intro
        $ wakeupquestinitiated = True
        bot"ZzZz"
        show hinaq1bg 2
        show eyeclosed zorder 100
        show shina shy behind eyeclosed:
            blur 6
        with dissolve
        # show hina quest1_1t behind eyeclosed with dissolve:
        #     blur 6
        show bobedx 3:
            matrixtransform ScaleMatrix(1.0, 0.6, 1.0)*OffsetMatrix(1.0, 238.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
            alpha 1
        hin"[bo_name_stutter]!"
        call blink("...", hin_rel + "...?","Why is s-she...") from _call_blink_3
        show shina:
            blur 0
        show hinaq1bg:
            blur 0
        with dissolve
        hin"W-wake up please..."
        bo"[hin_rel]? What's wrong..."
        hin"I've arranged for you to see Lady Tsunade at the infirmary..."
        hin"I think... you've been acting a little bit too weird lately..."
        menu:
            hin"I think... you've been acting a little bit too weird lately..."
            "Act confused":
                bo"I don't know what you are talking about..."
                hin"..."
                hin"In a-any case... Please pay Lady Tsunade a visit for me, will you?"
            "...":
                bot"Shit... I must have spooked her off with my condition..."
                hin"Will you p-please pay Lady Tsunade a visit for me?"
        bo"I'll see what I can do..."
        show shina shy2 with dissolve
        hin"I'll leave you be for now... In case you have something to t-take care of!"
        hide shina with dissolve
            
        $ tsunadeintroduction = True
        $ notification ("Infirmary unlocked")
        "You can now visit the Infirmary during mornings or evenings using the map."
        bo"..."
        call hideButtons from _call_hideButtons_12
        scene black
        scene bg day with dissolve:
            zoom 0.70
        show screen topleftbuttons
        call screen housemap

    #Hinata wakes you up after quest is done
    default wakeup_toggle1 = True
    if day_number >=2 and (quest.is_state("bohin_1", "done") == False or wakeup_toggle1 == True) and day_part == 1:
        if hinata_captured == True: #skip wake up quest if hin captured
            pass
        else:
            jump bohin_1

    call hideButtons from _call_hideButtons
    $ boruto_location = "hallway"
    scene black
    scene bg day with dissolve:
        zoom 0.67
    show screen topleftbuttons
    call screen housemap



label action_taken:
    stop sfxstat fadeout 1
    stop sfx1 fadeout 1
    stop sfx2 fadeout 1
    stop sfx3 fadeout 1
    stop sfx4 fadeout 1
    stop sfx5 fadeout 1
    stop ambience fadeout 1
    stop ambience2 fadeout 1
    $ renpy.end_replay()
    scene onlayer screens
    $ config.menu_include_disabled = False
    if day_number >=2:
        call v12b_onetime from _call_v12b_onetime
    # $ playmusic("/audio/ost/house2.opus", 0.6)

    #variables to reset
    call onetime_actionstaken from _call_onetime_actionstaken
    call variablestoreset from _call_variablestoreset
    call hideEventScreens from _call_hideEventScreens
    call hideUI from _call_hideUI_37
    with dissolve

    #advance day
    $ day_part += 1


    #add lust after night
    if day_part > 4:
        if hatred >= 10 and chosen_love_path:
            scene black with dissolve
            #TODO - Fix dialogue / scene set-up for game over state
            dev"In a future update, allowing your impulse to reach 10 will result in a game-over state, along with a relevant sex-scene."
            call changeHatred(-5) from _call_changeHatred_206
            dev "Until then, enjoy your 'get out of jail free card'!"

        call increaselust(10) from _call_increaselust_21
        if day_number == 1: #one time dream kushina on day 1
            call kushinadream from _call_kushinadream
        elif day_number >= 11 and naruto_captive_seen == False: #one time Naru lore
            call naruto_held_captive from _call_naruto_held_captive
        elif day_number == 13 and kushina_plan_unlocked == False: #one time Kurama choice
            jump kuramachoice_dream

        $ day_part = 1
        $ day_part_name = "Morning"
        $ tenten_date_asked_today = False # Reset daily check for Tenten asking about a date
        $ day_number += 1
        # v0.19 Tenten Quest - Increment days since date agreed counter
        if tenten_date_agreed:
            $ tenten_days_since_agreed += 1
        $ uchihas_visited = False
        $ day_name = day_names[day_number % len(day_names)] #variable that stores the name of the day
        $ v21_hinatadate_daycounter += 1
    
    #Calendar locations - Will be overwritten by anything under this call
    call calendar from _call_calendar
    #Quests
     

    











    scene black with dissolve
    "Some time goes by..."
    if hinata_captured == True:
        default hinata_captured_eventcounter = 0
        
        $ hin_location = "captured"
        if day_part == 3:
            $ hinata_captured_eventcounter += 1
            if hinata_captured_eventcounter == 1:
                jump hinata_captured_1
            elif hinata_captured_eventcounter == 2:
                jump hinata_captured_2
            else:
                jump hinata_captured_3

        if day_part == 4:
            if hinata_captured_eventcounter == 1:
                jump hinata_captured_midnight1
            elif hinata_captured_eventcounter == 2:
                jump hinata_captured_midnight2
            else:
                jump hinata_captured_midnight3
    $ change_music_volume(1.0, 1.0)
    jump house


#used only to skip to night
label action_taken_night:

    #variables to reset
    call variablestoreset from _call_variablestoreset_1
    call hideEventScreens from _call_hideEventScreens_1
    call hideUI from _call_hideUI_38
    with dissolve
    $ day_part = 3
    $ day_part_name = "Night"    
    call calendar from _call_calendar_1
    if hinata_captured == True:
        $ hin_location = "captured"
        if day_part == 3:
            if hinata_captured_eventcounter == 1:
                jump hinata_captured_1
            elif hinata_captured_eventcounter == 2:
                jump hinata_captured_2
            else:
                jump hinata_captured_3
    jump house

label action_taken_midnight:

    #variables to reset
    call variablestoreset from _call_variablestoreset_2
    call hideEventScreens from _call_hideEventScreens_2
    call hideUI from _call_hideUI_39
    with dissolve
    $ day_part = 4
    $ day_part_name = "Midnight"    
    call calendar from _call_calendar_2   
    jump house

label calendar:
    if day_part == 1:
        $ day_part_name = "Morning"
    elif day_part == 2:
        $ day_part_name = "Evening"
    elif day_part == 3:
        $ day_part_name = "Night"
    elif day_part == 4:
        $ day_part_name = "Midnight"


    #Calendar
    if day_name == "Monday":
        if day_part == 1:
            $ hin_location = "laundryroom"
            $ him_location = "School"

        elif day_part == 2:
            $ hin_location = "kitchen"
            if himaintrotutorial2 == True:

                $ him_location = "himawaribedroom" #clothingshop after
            else:
                $ him_location = "livingroom" #clothingshop after

        elif day_part == 3:
            $ hin_location = "livingroom"
            $ him_location = "bathroom"

    elif day_name == "Tuesday":
        if day_part == 1:
            $ hin_location = "laundryroom"
            $ him_location = "School"

        elif day_part == 2:
            $ hin_location = "hinatabedroom"
            if himaintrotutorial2 == True:

                $ him_location = "himawaribedroom" #clothingshop after
            else:
                $ him_location = "livingroom" #clothingshop after

        elif day_part == 3:
            $ hin_location = "bathroom"
            $ him_location = "himawaribedroom"
    
    elif day_name == "Wednesday":
        if day_part == 1:
            $ hin_location = "laundryroom"
            $ him_location = "School"

        elif day_part == 2:
            $ hin_location = "kitchen"
            if himaintrotutorial2 == True:

                $ him_location = "himawaribedroom" #clothingshop after
            else:
                $ him_location = "livingroom" #clothingshop after


        elif day_part == 3:
            $ hin_location = "livingroom"
            $ him_location = "bathroom"

    elif day_name == "Thursday":
        if day_part == 1:
            $ hin_location = "laundryroom"
            $ him_location = "School"

        elif day_part == 2:
            $ hin_location = "hinatabedroom"
            if himaintrotutorial2 == True:

                $ him_location = "himawaribedroom" #clothingshop after
            else:
                $ him_location = "livingroom" #clothingshop after

        elif day_part == 3:
            $ hin_location = "bathroom"
            $ him_location = "himawaribedroom"

    elif day_name == "Friday":
        if day_part == 1:
            $ hin_location = "laundryroom"
            $ him_location = "School"

        elif day_part == 2:
            $ hin_location = "kitchen"
            if himaintrotutorial2 == True:

                $ him_location = "himawaribedroom" #clothingshop after
            else:
                $ him_location = "livingroom" #clothingshop after

        elif day_part == 3:
            $ hin_location = "livingroom"
            $ him_location = "bathroom"

    elif day_name == "Saturday":
        if day_part == 1:
            $ hin_location = "laundryroom"
            $ him_location = "himawaribedroom" #locked

        elif day_part == 2:
            $ hin_location = "hinatabedroom"
            $ him_location = "bathroom"

        elif day_part == 3:
            $ hin_location = "bathroom"
            $ him_location = "himawaribedroom"

    else:
        if day_part == 1: #morning
            $ hin_location = "laundryroom"
            $ him_location = "himawaribedroom" #locked

        elif day_part == 2: #evening
            $ hin_location = "kitchen"
            $ him_location = "bathroom"

        elif day_part == 3: #night
            $ hin_location = "livingroom"
            $ him_location = "himawaribedroom"
    #midnight
    if day_part == 4:
        $ hin_location = "hinatabedroom"
        $ him_location = "himawaribedroom"

    # #day1 hinata shower scene / himawari school livingroom scene
    if day_number == 1 and day_part == 2:
        $ hin_location = "kitchen"
        $ him_location = "livingroom"
    
    #himawari school intro
    if day_number >= 1 and day_part == 2 and himaintrotutorial == False:
        $ him_location = "livingroom"

    #tutorial2
    elif day_number == 1 and day_part == 3:
        $ hin_location = "livingroom"
        $ him_location = "himawaribedroom"

    return


#One time events
#---------------#---------------#---------------
#---------------#---------------#---------------
#---------------#---------------#---------------
#---------------#---------------#---------------
#---------------#---------------#---------------
#---------------#---------------#---------------
#---------------#---------------#---------------
#---------------#---------------#---------------

label kitchen:
    $ boruto_location = "kitchen"
    if completed_intro > 5:
        jump kitchenActions

    elif completed_intro == 1:
        bot"[hin_rel] is in the living room, I should probably hurry there."
        call screen housemap
        
    elif completed_intro == 2 or completed_intro == 3:
        bot"It is getting late, I should go to my bedroom..."
        call screen housemap

    elif completed_intro == 5:
        bot"I should check what the commotion is about in the living room"
        call screen housemap
    


label laundryroom:
    $ boruto_location = "laundryroom"
    if completed_intro > 5:
        jump laundryroomActions
    elif completed_intro == 1:
        bot"[hin_rel] is in the living room, I should probably hurry there."
        call screen housemap
    elif completed_intro == 2 or completed_intro == 3:
        bot"It is getting late, I should go to my bedroom..."
        call screen housemap
    elif completed_intro == 5:
        bot"I should check what the commotion is about in the living room"
        call screen housemap
        




label livingroom:
    $ boruto_location = "livingroom"
    if completed_intro > 5:
        jump livingroomActions
    elif completed_intro == 1:
        $ completed_intro += 1
        call after_asleep from _call_after_asleep
    elif completed_intro == 2 or completed_intro == 3:
        bot"It is getting late, I should go to my bedroom..."

    elif completed_intro == 5:
        jump ch1_d1_moneyproblems_mainstory
                            



label bathroom:
    $ boruto_location = "bathroom"
    if completed_intro > 5:
        jump bathroomActions
    elif completed_intro == 1:
        bot"[hin_rel] is in the living room, I should probably hurry there."
        call screen housemap
    elif completed_intro == 2 or completed_intro == 3:
        bot"It is getting late, I should go to my bedroom..."
        call screen housemap
    elif completed_intro == 5:
        bot"I should check what the commotion is about in the living room"
        call screen housemap



label borutobedroom:
    $ boruto_location = "borutobedroom"
    if completed_intro > 5:
        jump borutobedroomActions
    elif completed_intro == 1:
        bot"[hin_rel] is in the living room, I should probably hurry there."
        call screen housemap
    elif completed_intro == 2:
        $ completed_intro += 1
        jump bedroomtutorial

    elif completed_intro == 3:
        bot"It is getting late, I should get some sleep..."
        hide screen housemap
    elif completed_intro == 5:
        bot"I should check what the commotion is about in the living room"



label himawaribedroom:
    $ boruto_location = "himawaribedroom"
    if completed_intro > 5:
        jump himawaribedroomActions
    elif completed_intro == 1:
        bot"[hin_rel] is in the living room, I should probably hurry there."
        call screen housemap
    elif completed_intro == 2 or completed_intro == 3:
        #eavesdrop
        default eavesdropcountertutorial = 0
        if eavesdropcountertutorial == 0:
            if introhatredplan == True:
                show boruto bonerevil4 with dissolve
            else:
                show boruto suspicious at center with dissolve
            bot"I can hear [hin_name] and [him_name] conversing inside..."
        elif eavesdropcountertutorial == 1:
            if introhatredplan == True:
                show boruto bonerevil4 with dissolve
            else:
                show boruto surprised2 at center with dissolve
            bot"They are still at it?"
        else:
            bot"They are just girl-chatting. I am tired anyway, I should head to bed."
            jump bedroom_hallway
        bot"Should I..."
        menu :
            bot"Should I..."
            "Eavesdrop":
                if eavesdropcountertutorial == 0:
                    if introhatredplan == True:
                        show boruto bonerevil4 with dissolve
                    else:
                        show boruto smirk at center with dissolve
                    bot"No harm in it, is there?"
                    scene black with dissolve
                    "You put your ear on [him_name]'s door..."
                    hin"You can't treat your [him_rel_to_bo] like that [him_name]. Especially now that he is... troubled."
                    if secretscenelovehandjob == True:
                        hin"You saw how much pain he was in just before..."

                    him"But he keeps being annoying! Not to mention he is useless around the house, aren't you tired of pampering him!?"
                    if introhatredplan == True:
                        bot"Oh don't you worry [him_name]. [hin_rel] will definitely 'pamper' me tonight. Soon enough... you will too!"
                    hin"[him_name]... [bo_name] will come around, he just needs some time. Besides..."
                    hin"Don't you think you are also being annoying to him when you treat him like that? Maybe he just needs a little of your support..."
                    him"Only if he stops being an idiot first!"
                    bot"Same old, same old. [him_name] is still a bitch, [hin_rel] is still, well... [hin_rel]."
                    $ eavesdropcountertutorial +=1
                    jump bedroom_hallway
                else:
                    scene black with dissolve
                    him"W-what!?"
                    him"It's that serious?"
                    hin"That's what the doctor said..."
                    hin"You don't have to worry or anything, I... talked with [bo_name]"
                    hin"He will get through this. He just needs... our support, okay? Try to not be as antagonizing..."
                    hin"And if he is using the bathoom more than usual, it's because he is applying his, uh... prescribed treatment."
                    hin"So we both have to show some understanding, okay?"
                    him"Hmm..."
                    bot"My prescribed treatment? Heh. [hin_rel] is doing her best to keep [him_name] oblivious..."
                    if secretscenelovehandjob == True:
                        bot"If only she knew what [hin_rel_mother] just did... heh!"
                    if introhatredplan == True:
                        bot"But in reality, her [hin_rel_mother] is oblivious too! She has no idea what I am planning for her tonight..."
                    $ eavesdropcountertutorial +=1
                    jump bedroom_hallway


            "Don't":
                bot"I better not..."
                call screen housemap
    elif completed_intro == 5:
        bot"I should check what the commotion is about in the living room"    
        call screen housemap


label hinatabedroom:
    $ boruto_location = "hinatabedroom"
    if completed_intro > 5:
        jump hinatabedroomActions
    elif completed_intro == 1:
        bot"[hin_rel] is in the living room, I should probably hurry there."
        call screen housemap
    elif completed_intro == 2 or completed_intro == 3:
        bot"It is getting late, I should go to my bedroom..."
        call screen housemap
    elif completed_intro == 5:
        bot"I should check what the commotion is about in the living room"
        call screen housemap


