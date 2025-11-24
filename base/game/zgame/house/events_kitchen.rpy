label kitchen_morning:
    call resetbuttons from _call_resetbuttons_12
    call hideUI from _call_hideUI_23
    if hin_location == "kitchen" and him_location == "kitchen":
        scene kitchen day with dissolve
        call enabletalk from _call_enabletalk_29
    elif hin_location == "kitchen":
        scene kitchen day hinata
        show screen kitchen_hinata_day
        with dissolve
        call enabletalk from _call_enabletalk_30
        call showUIhouse from _call_showUIhouse_42
    elif him_location == "kitchen":
        scene kitchen day with dissolve
        call enabletalk from _call_enabletalk_31
        
    else:
        scene kitchen day with dissolve

    call showUIhouse from _call_showUIhouse_43
    $ ui.interact()

label kitchen_evening:
    call resetbuttons from _call_resetbuttons_13
    call hideUI from _call_hideUI_24
    if hin_location == "kitchen" and him_location == "kitchen":
        scene kitchen day with dissolve
        call enabletalk from _call_enabletalk_32
    elif hin_location == "kitchen":
        scene kitchen day hinata
        show screen kitchen_hinata_day
        with dissolve
        call enabletalk from _call_enabletalk_33
        call showUIhouse from _call_showUIhouse_44
    elif him_location == "kitchen":
        scene kitchen day with dissolve
        call enabletalk from _call_enabletalk_34
        
    else:
        scene kitchen day with dissolve

    call showUIhouse from _call_showUIhouse_45
    $ ui.interact()

label kitchen_night:
    call resetbuttons from _call_resetbuttons_14
    call hideUI from _call_hideUI_25
    if hin_location == "kitchen" and him_location == "kitchen":
        scene kitchen night with dissolve
        call enabletalk from _call_enabletalk_35
    elif hin_location == "kitchen":
        scene kitchen night with dissolve
        call enabletalk from _call_enabletalk_36
    elif him_location == "kitchen":
        scene kitchen night with dissolve
        call enabletalk from _call_enabletalk_37
        
    else:
        scene kitchen night with dissolve

    call showUIhouse from _call_showUIhouse_46
    $ ui.interact()


label kitchentalkmenu:
    hide screen kitchen_hinata_day
    call hideUI from _call_hideUI_26
    menu:
        "..."
        "Talk to [hin_name]" if hin_location == "kitchen":
            bo"Hey [hin_rel]..."
            scene kitchen day with fade
            show shina shy at right
            show boruto normal at left
            with dissolve
            hin"Oh, hi! Didn't see you there... Something's up?"
            menu:
                hin"Oh, hi! Didn't see you there... Something's up?"
                "Let me help with the chores" if helphinadishes == False:
                    show boruto smirk with dissolve
                    bo"Let me help you with the dishes. I am sure you already have a lot... on your plate."
                    show boruto laughing2 with dissolve
                    bo"*Chuckles at his own joke*"
                    show boruto smirk2 with dissolve
                    show shina shy with dissolve
                    hin"I could always use some extra help! Thanks for volunteering..."
                    show shina smiling with dissolve
                    call changeRespect("Hinata",1) from _call_changeRespect_29
                    hin"I'll leave you to it then!"
                    hide shina with dissolve
                    hin"And that was a pretty bad joke! *Giggles*"
                    bo"Heh! I though it was pretty cool..."
                    hide boruto with dissolve
                    
                    "You spend some time taking care of some chores..."
                    default helphinadishes = False
                    $ helphinadishes = True
                    jump action_taken
                "Let me help with the chores" if helphinadishes == True:
                    show boruto smirk with dissolve
                    bo"Let me take care of that [hin_rel]..."
                    show shina shy with dissolve
                    hin"I appreciate the help..."
                    show shina smiling with dissolve
                    call changeRespect("Hinata",1) from _call_changeRespect_30
                    hin"I'll leave you to it then!"
                    hide shina with dissolve
                    bo"Sure thing!"
                    hide boruto with dissolve
                    
                    "You spend some time taking care of some chores..."

                    jump action_taken

                "Can we have lunch together?":
                    bo"I was thinking [hin_rel], maybe we can have lunch together today?"
                    show shina shy2 with dissolve
                    hin"Oh? It's very unlikely for you to sit down with us, but I am glad you asked!"
                    show shina smiling with dissolve
                    hin"I will prepare something right away!"
                    scene black with dissolve
                    "You sit by the table and wait for [hin_name] to prepare lunch..."
                    jump kitchen_events_eatafternoon

                "Return":
                    show boruto embarassed with dissolve
                    bo"Just checking in..."
                    hide boruto with dissolve
                    bo"I'll be going now!"
                    show shina assertive with dissolve
                    hin"..."
                    hide shina with dissolve
                    scene bg day with dissolve:
                        zoom 0.70
                    call showUIhouse from _call_showUIhouse_47
                    $ ui.interact()
                
        "Silently approach...":
            bo"What if I..."
            scene hinata ktichen_approach1 with dissolve
            bot"Fuck me! [hin_rel]'s ass is just..."
            menu kitchenapproachmenu:
                bot"Fuck me! [hin_rel]'s ass is just..."
                "Let me help-":
                    bo"Hey [hin_rel], Let me hel-"
                    scene black with vpunch
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                    $ renpy.sound.play("/audio/soun_fx/dishbreak.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    hin"EEEH!" with vpunch
                    scene kitchen day
                    show boruto surprised2 at left
                    show shina surprised2 at right
                    with dissolve
                    hin"[bo_name_stutter]! D-don't sneak up on me like that!"
                    show shina assertive with dissolve
                    show shina at smallshake
                    hin"I dropped a dish because of you..."
                    show shina shy with dissolve
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatasigh3.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                    hin"*Sigh*..."
                    hin"Come on, don't just stand there! Help me clean up..."
                    show boruto embarassed with dissolve
                    bo"R-right..."
                    scene black with dissolve
                    "You spend some time cleaning up..."
                    jump action_taken
                "{color=[obediencecolor]}Get handsy!":
                    jump kitchen_events_gethandsy
                "{color=[obediencecolor]}Can you prepare something to eat?{/color}" if hinata_kitchen_approachgrab == True:
                    jump kitchen_events_gethandsy2
                "{color=[obediencecolor]}????{/color}" if hinata_kitchen_approachgrab == False:
                    "Complete previous options to unlock!"
                    jump kitchenapproachmenu
                

            call showUIhouse from _call_showUIhouse_48
            $ ui.interact()
        "Talk to [him_name]" if him_location == "kitchen":
            bo" to do"
            call showUIhouse from _call_showUIhouse_49
            $ ui.interact()
        "Return":
            if hin_location == "kitchen":
                show screen kitchen_hinata_day
            call showUIhouse from _call_showUIhouse_50
            $ ui.interact()

label kitchenactionmenu:
    call hideUI from _call_hideUI_27
    menu:
        "..."
        "Choice 1":
            jump action_taken
        "Return":
            call showUIhouse from _call_showUIhouse_51
            $ ui.interact()
                


screen kitchen_hinata_day:
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "kitchen day hinata"  
        hover "kitchen day hinata_hover"
        focus_mask "kitchen day hinata_mask"
        mouse "handsmall"
        hovered [Show("displayTextScreen", displayText = "Interact with [hin_name]")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("displayTextScreen"), Jump("kitchentalkmenu")]