label daimyopalace:
    $ playmusic("audio/ost/Senya.opus",0.5)
    call hidemarketUI from _call_hidemarketUI_13
    call hideUI from _call_hideUI_66
    if day_part == 1 or day_part == 2:
        scene black
        scene palace with dissolve
    else:
        scene black
        scene palace_night bg with dissolve
        hide screen housemap
        hide screen topleftbuttons
        menu:
            "..."
            "Sneak inside!" if hin_captured_gameover == False:
                jump sneakinsidepalace

            "Try to save [hin_name]!" if hin_captured_gameover == True:
                bot"I am not leaving [hin_rel] to rot in there!"
                scene black with dissolve
                bot"I'll find a way in and rescue her. I swear it..."
                "You began a thorough search for [hin_name], vowing to help her escape captivity."
                jump hinata_captured_midnight3
            "Leave":
                hide screen housemap
                show screen topleftbuttons
                $ ui.interact()
            


    hide screen housemap
    if hin_captured_gameover == False:
        bot"This place is well guarded. There's no way I'll be able to sneak inside during daytime..."
        bot"I should try my luck during nighttime."
        show screen topleftbuttons
        $ ui.interact()
    else:
        hide screen topleftbuttons
        menu:
            "..."
            "Sneak inside!" if hin_captured_gameover == False:
                jump sneakinsidepalace

            "Try to save [hin_name]!" if hin_captured_gameover == True:
                bot"I am not leaving [hin_rel] to rot in there!"
                scene black with dissolve
                bot"I'll find a way in and rescue her. I swear it..."
                jump hinata_captured_midnight3
            "Leave":
                hide screen housemap
                show screen topleftbuttons
                $ ui.interact()



label sneakinsidepalace:
    bot"It's now or never!"
    scene black with dissolve
    "You skirt around the estate, looking for an unguarded opening."
    bot"There!" with vpunch
    show daimy_quartersrun1 with dissolve
    "You climb up the estate's walls effortlessly, but not before long..."
    show daimy_quartersrun1 with dissolve:
        zoom 1.1 xalign 0.5 yalign 0.0
    "Guard" "What the..."
    show daimy_quartersrun1 with dissolve:
        zoom 1.2 xalign 0.5 yalign 0.0
    "Guard" "YOU UP THERE! IDENTIFY YOURSELF!" with vpunch
    bot"Like hell I will!"
    show daimy_quartersrun2 with dissolve:
        zoom 1.2 xalign 0.0 yalign 0.0
    "Guard" "STOP AT ONCE!" with vpunch

    scene black with dissolve
    bot"Nope!"
    "Guard" "Find the intruder!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    "You make your way towards the residential area and drop down the walls to navigate further."
    show palace3_night with dissolve
    show boruto snob with dissolve
    bot"Easy enough!"
    label jumpbackdaimyoquarters:
    show boruto surprised2 with dissolve
    bot"Where to now..."
    hide boruto with dissolve
    menu:
        bot"Where to now..."
        "Through the rocky pathway":
            show palace3_night:
                zoom 1.1
            with dissolve
            bot"Uuuh, in there I guess!"
            if onsen_information_attempt_done == True: #not sure about this variable lue
                jump ch1_d14_onsen_repeatable
            else:
                jump ch1_d14_onsen
        "Up the stairs":
            bot"The place up there looks important!"
            $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            scene black with dissolve
            "..."
            show bg daimyo_quarters with dissolve
            bot"S-shit!"
            show bg daimyo_quarters with dissolve:
                zoom 1.15 xalign 0.5 yalign 1.0
            "Guards" "Oi! Who goes there!?" with vpunch
            scene black with vpunch
            $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            bot"I am outa there!"
            scene palace3_night with dissolve
            jump jumpbackdaimyoquarters


        "Escape":
            bot"It's too risky to continue!"
            scene black with dissolve
            "You abandon your rescue attempt for now..."
            jump daimyopalace
        