label laundryroom_morning:
    call resetbuttons from _call_resetbuttons_15
    call hideUI from _call_hideUI_28
    if hin_location == "laundryroom" and him_location == "laundryroom":
        scene bg laundry day with dissolve
        bo"Both are here"
        call enabletalk from _call_enabletalk_38
        if quest.is_state("bohin_1", "done"):
            call enableaction from _call_enableaction_21

    elif hin_location == "laundryroom":
        scene laundry quest1 with dissolve
        
        if quest.is_state("bohin_1", "unlocked") or quest.is_state("bohin_1", "done"):
            bot "Oh, [hin_rel] is here!"
            show screen v1_laundry_hinata
            call enableaction from _call_enableaction_22
        
    
    elif him_location == "laundryroom":
        scene bg laundry day with dissolve
        call enabletalk from _call_enabletalk_39
        bo"Himawari is here"
        
    else:
        scene bg laundry day with dissolve
        

    call showUIhouse from _call_showUIhouse_52
    $ ui.interact()

label laundryroom_evening:
    call resetbuttons from _call_resetbuttons_16
    call hideUI from _call_hideUI_29
    if hin_location == "laundryroom" and him_location == "laundryroom":
        scene bg laundry day with dissolve
        call enabletalk from _call_enabletalk_40
        

    elif hin_location == "laundryroom":
        scene bg laundry day with dissolve
        call enabletalk from _call_enabletalk_41
        if quest.is_state("bohin_1", "done"):
            call enableaction from _call_enableaction_23

    elif him_location == "laundryroom":
        scene bg laundry day with dissolve
        call enabletalk from _call_enabletalk_42
        
    else:
        scene bg laundry day with dissolve

    call showUIhouse from _call_showUIhouse_53
    $ ui.interact()

label laundryroom_night:
    call resetbuttons from _call_resetbuttons_17
    call hideUI from _call_hideUI_30
    if hin_location == "laundryroom" and him_location == "laundryroom":
        scene bg laundry night with dissolve
        call enabletalk from _call_enabletalk_43
    elif hin_location == "laundryroom":
        scene bg laundry night with dissolve
        call enabletalk from _call_enabletalk_44
    elif him_location == "laundryroom":
        scene bg laundry night with dissolve
        call enabletalk from _call_enabletalk_45
        
    else:
        scene bg laundry night with dissolve

    call showUIhouse from _call_showUIhouse_54
    $ ui.interact()

label laundryroomntalkmenu:
    call hideUI from _call_hideUI_31
    menu:
        "..."
        "Talk to [hin_name]" if hin_location == "laundryroom":
            bo"Laund"
            call showUIhouse from _call_showUIhouse_55
            $ ui.interact()
        "Talk to [him_name]" if him_location == "laundryroom":
            bo"Laund"
            call showUIhouse from _call_showUIhouse_56
            $ ui.interact()
        "Return":
            call showUIhouse from _call_showUIhouse_57
            $ ui.interact()
    call showUIhouse from _call_showUIhouse_58
    $ ui.interact()



label laundryroomactionmenu:
    call hideUI from _call_hideUI_32
    menu:
        "..."
        "Approach" if laundryquestcompleted_1 == False: #before quest is fully completed. Handles jumping to the corresponding label based on which step of the quest player is on
            hide screen v1_laundry_hinata

            if quest.is_state("bohin_1", "done"): #if left page Hinata's hospitality is done (prevents errors)
                jump bohin1_2
            else:
                if quest.is_state("bohin1_1", "in progress"):
                    jump bohin1_1
                elif quest.is_state("bohin1_2", "in progress"):
                    jump bohin1_2
                elif quest.is_state("bohin1_3", "in progress"):
                    jump bohin1_3
                elif quest.is_state("bohin1_4", "in progress"):
                    jump bohin1_4
        "Can you stop cleaning my room during mornings?" if (quest.is_state("bohin_1", "done") and wakeup_toggle1 == True and boruto_clothes!="Naked"): #dont know why red, works
            $ wakeup_toggle1 = False
            bo"Hey [hin_rel]. Can you find another time to clean my room besides mornings?"
            hin"I'll t-try..."
            jump action_taken
        "You can keep cleaning my room during mornings if you want to..." if (quest.is_state("bohin_1", "done") and wakeup_toggle1 == False and boruto_clothes!="Naked"): #dont know why red, works
            $ wakeup_toggle1 = True
            bo"Hey [hin_rel]. You can keep cleaning my room during mornings if you prefer..."
            hin"S-sure..."
            jump action_taken

        #grope after quest bohin1_3
        "Approach" if laundryquestcompleted_1 == True:
            menu laundryafterquest:
                bot"..."
                "Grope":
                    scene bg laundry day
                    show grptest
                    # show grptest with dissolve
                    "Hover over her..."
                    show screen gropetest
                    $ ui.interact() 
                "Spank":
                    bo"fill"
                
                "Locked":
                    "Progress event to unlock"
                    jump laundryafterquest
                      
                "Return":
                    label laundryreturn:
                        call showUIhouse from _call_showUIhouse_59
                        $ ui.interact()

    
