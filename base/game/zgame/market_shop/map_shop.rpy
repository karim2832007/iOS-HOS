label hidemarketUI:
    hide screen marketshop1
    hide screen marketshop2
    hide screen marketshop3
    hide screen marketmap
    hide screen marketnightmap
    hide screen displayTextScreen
    hide screen returnbutton
    hide screen shopkeeper
    hide screen returnbutton
    hide screen marketshopreturn
    hide screen marketreturn
    hide tap_icon_ramen
    hide tap_icon_alley
    hide tap_icon_shop
    return


default shopkeep_annoyance = 1
label shop:
    $ playmusic("/audio/ost/market.opus", volume=0.7)
    call hidemarketUI from _call_hidemarketUI_2
    $ shopkeep_interactions = 0
    if day_part >= 3:
        hide screen housemap
        call hideUI from _call_hideUI_49
        scene black
        show screen topleftbuttons
        show screen marketnightmap 
        scene bg ramenshop night
        if renpy.variant("touch") or renpy.variant("mobile"):
            show tap_icon_ramen at tap_icon_animation
            show tap_icon_alley at tap_icon_animation
            show tap_icon_shop at tap_icon_animation
        if tenten_date_agreed and not tenten_extorted and day_part == 3:
            show tenten_date_market_out:
                xzoom -1 xalign 1.2 zoom 0.75
        with dissolve 
        $ ui.interact()
    else:

        hide screen housemap
        call hideButtons from _call_hideButtons_3
        
        scene bg ramenshop with fade
        $ shopkeep_interactions = 0
        call hideUI from _call_hideUI_50
        call hidemarketUI from _call_hidemarketUI_3
        call hideButtons from _call_hideButtons_4
        scene bg ramenshop
        show screen topleftbuttons
        show screen marketmap
        if renpy.variant("touch") or renpy.variant("mobile"):
            show tap_icon_ramen at tap_icon_animation
            show tap_icon_alley at tap_icon_animation
            show tap_icon_shop at tap_icon_animation
        $ ui.interact()



label market:
    if day_part == 3 or day_part ==4:
        call hideUI from _call_hideUI_51
        call hidemarketUI from _call_hidemarketUI_4
        call hideButtons from _call_hideButtons_5
        scene bg ramenshop night
        show screen topleftbuttons
        show screen marketnightmap
        if renpy.variant("touch") or renpy.variant("mobile"):
            show tap_icon_ramen at tap_icon_animation
            show tap_icon_alley at tap_icon_animation
            show tap_icon_shop at tap_icon_animation
        $ ui.interact()
    else:
        $ shopkeep_interactions = 0
        call hideUI from _call_hideUI_52
        call hidemarketUI from _call_hidemarketUI_5
        call hideButtons from _call_hideButtons_6
        scene bg ramenshop
        show screen topleftbuttons
        show screen marketmap
        if renpy.variant("touch") or renpy.variant("mobile"):
            show tap_icon_ramen at tap_icon_animation
            show tap_icon_alley at tap_icon_animation
            show tap_icon_shop at tap_icon_animation
        $ ui.interact()

default tenten_fucked_cooldown = False
default tenten_rape_spank = 0
label visitshop:
        if day_part == 3 or day_part == 4:
            # v0.19 Tenten Quest Continuation - Night Entry Logic
            if tenten_date_agreed and not tenten_extorted:
                jump tenten_meet_at_shop # Jump to date logic in tenten_lake_date.rpy
            elif tenten_extorted:
                bot"The door's locked tight. Looks like she's not expecting visitors... especially not {b}me{/b}, I guess."
                jump market
            else:
                # Default closed message
                bot"The door's locked."
                jump market
        else: # Daytime logic starts here

            call hideUI from _call_hideUI_53
            call hidemarketUI from _call_hidemarketUI_6
            call hideButtons from _call_hideButtons_7
            show shop day with dissolve:
                zoom 0.5
            image shopkeeperimage = "images/characters/headshots/npcs/tenten/npc_shopkeep[shopkeep_annoyance]_idle.webp"

            if tenten_fucked_cooldown == True:
                show ten sad1 at right with dissolve
                ten "Hello..."
                bo"..."
                $ shopkeep_annoyance = 2
                ten"S-sorry, just a bad day. Feel free to look around..."
                bot"A bad day, huh? Hehe!"
                $ tenten_fucked_cooldown = False
                hide ten with fade
                show screen shopkeeper
                show screen marketreturn
                ten"So, you need anything?"
                $ ui.interact()
            
            if tenten_mild_grope == True:
                show ten sad1 at right with dissolve
                ten "Hey y-you!" with vpunch
                bo"W-who, me?"
                $ shopkeep_annoyance = 2
                ten"Did you happen to visit my place s-some time ago?"
                bot"I know what this is about..."
                bo"Uuuh, not really, no! Something happened?"
                ten"Some idiot strolled in here and put his hands where they don't belong... *Scoffs*"
                bo"Weirdos these days..."
                $ tenten_fucked_cooldown = False
                $ tenten_mild_grope = False
                hide ten with fade
                show screen shopkeeper
                show screen marketreturn
                ten"So, were you looking for something?"
                $ ui.interact()

            # v0.19 Tenten Quest Continuation - Daytime Post-Quest Dialogue Hook
            if tenten_pendant_returned == True:
                # If the initial quest is done, jump to new dialogue variations
                jump tenten_daytime_dialogue_entry

            if quest.exists("shop1_1") and tenten_quest_activated == False and day_number>=5 and tenten_fucked_cooldown == False:
                    if quest.is_state("shop1_1", "completed"):
                        default tenten_quest_activated = False
                        jump tenten_quest_start


            show npc_shopkeep1_idle
            hide npc_shopkeep1_idle
            show npc_shopkeep2_idle
            hide npc_shopkeep2_idle
            hide screen marketmap
            show shopkeeperimage with dissolve:
                zoom 0.7 xpos -60 ypos 0.01

            if shopkeep_annoyance == 2 and shopkeep_block == True:
                "Shopkeeper" "You are not welcome here!"
                scene black with vpunch
                "The shopkeeper kicked you out of her establishment."
                "Try visiting another time."
                jump market


            elif shopkeep_annoyance == 1:
                if tenten_quest_activated == False:
                    "Shopkeeper" "Hello and welcome to my humble establishment! How may I be of service?"
                else:
                    ten"Oh, you again! Welcome to my humble establishment! How may I be of service?"
                    menu tenten_shopmenu:
                        "Shop":
                            pass
                        "About your pendant..." if tenten_pendant_found == True and not tenten_pendant_returned: # Show only if player has pendant AND quest isn't done
                            jump tenten_pendant_continuation # Jump to the logic moved to the other file
                        "About your pendant..." if tenten_pendant_found == False:
                            ten"H-have you found it!?" with vpunch
                            bo"Not yet..."
                            ten"Argh! Bummer!" with vpunch
                            jump tenten_shopmenu
                        "Leave":
                            hide screen shopkeeper
                            scene black
                            with dissolve
                            jump market
                        

            elif shopkeep_annoyance == 2:
                "Shopkeeper" "Ugh... you again?"
                "Shopkeeper" "Don't try anything weird!"
            if shopintroductionseen == False:
                default shopintroductionseen = False
                $ shopintroductionseen = True
                dev"The shop is still early in development."
                dev"Items that cost $9999 are placeholders and will be updated when ready!"
                "Click the Shopkeeper to open the shop."
            hide shopkeeperimage
            show screen shopkeeper
            show screen marketreturn
            $ ui.interact()

label visitalley:
    hide tenten_date_market_out
    
        
    if day_part == 3 or day_part ==4:
        if day_number >=  5:
            hide tap_icon_ramen
            hide tap_icon_alley
            hide tap_icon_shop
            jump nightmerchantintro

        else:
    
            default nightmerchant_seen = False
            $ nightmerchant_seen = True
            hide tap_icon_ramen
            hide tap_icon_alley
            hide tap_icon_shop
            show bg allerynight merchant
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/oldman_laugh9.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            "Mysterious Man" "*Snickering*"
            if nightmerchant_seen == True:
                bot"This guy again! He seems suspicious..."
                bo"Hey you, hold on a second!"
                $ renpy.sound.play("/audio/soun_fx/oldman_laugh1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                scene bg alleynight with flash
                $ renpy.sound.play("/audio/soun_fx/wind1.opus", channel="sfx1", loop=False, relative_volume = 0.8)
                "Mysterious Man" "Hehehe!"
                bot"He vanished into thin air..."
            else:
                
                bot"Huh...?"
                bot"Who's this shady looking guy?"
                menu:
                    bot"Who's this shady looking guy?"
                    "Try to approach...":
                        label findmerchantonetime:
                        $ nightmerchant_seen = True
                        bo"Hey you!"
                        $ renpy.sound.play("/audio/soun_fx/oldman_laugh10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        $ renpy.sound.play("/audio/soun_fx/wind1.opus", channel="sfx1", loop=False, relative_volume = 1.0)
                        scene bg alleynight
                        show boruto surprised2 at right
                        with flash
                        "Mysterious Man" "Hehehe!"
                        "The hooded man disappeared into the dark of night..."
                        show boruto suspicious with dissolve
                        bo"What the hell..."
                        hide boruto with dissolve
                    "Leave":
                        bot"Better not meddle..."
                
        show screen marketreturn
        show screen returnbutton
        $ ui.interact()
    else:
        
        call hideUI from _call_hideUI_54
        call hidemarketUI from _call_hidemarketUI_7
        scene bg alley with dissolve



        bot"There's nothing here..."

        show screen returnbutton
        show screen marketreturn




        $ ui.interact()

label visitramen:
    if day_part == 3:
        jump work
    elif day_part == 4:
        bot"The place is locked up. It's midnight after all..."
        jump market
    else:

        call hideUI from _call_hideUI_55
        call hidemarketUI from _call_hidemarketUI_8
        hide screen marketmap
        if mapintrotutorial == True:
            jump work
        else:
            jump ramenintro
            
        scene bg ramen with dissolve
        "Empty ramen place"
            
        show screen returnbutton
        show screen marketreturn
        $ ui.interact()
            

screen shopkeeper():
    imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            xpos -60
            ypos 0.01
            hover "characters/headshots/npcs/tenten/npc_shopkeep[shopkeep_annoyance]_hover.webp"
            idle "characters/headshots/npcs/tenten/npc_shopkeep[shopkeep_annoyance]_idle.webp"
            at customzoom
            hovered Show("displayTextScreen", displayText = "Talk to shopkeeper")
            unhovered Hide("displayTextScreen")
            action [Show("shopScreen"), Play('sound', 'soun_fx/shopbell.opus')]







#market day map
screen marketmap():
    button:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        xpos 920 ypos 90
        xysize (500,720)
        hovered [Show("displayTextScreen", displayText = "Visit Shop"), Show("marketshop1")]
        unhovered [Hide("displayTextScreen"), Hide("marketshop1")]
        action [Jump("visitshop")]
        # action [Hide("itemdescription"), Hide("displayTextScreen")]

    button:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        xpos 320 ypos 175
        xysize (626,541)
        hovered [Show("displayTextScreen", displayText = "Visit Alley"), Show("marketshop2")]
        unhovered [Hide("displayTextScreen"), Hide("marketshop2")]
        action [Jump("visitalley")]
        # action [Hide("itemdescription"), Hide("displayTextScreen")]

    button:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        xpos 0 yalign 1.0
        xysize (421,620)
        hovered [Show("displayTextScreen", displayText = "Visit Ramen Shop"), Show("marketshop3")]
        unhovered [Hide("displayTextScreen"), Hide("marketshop3")]
        action [Jump("visitramen")]
        # action [Hide("itemdescription"), Hide("displayTextScreen")]

#market night map
screen marketnightmap():
    
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "idle1"  #image in ui / needs to be seperate for correct images to be displayed when hovering
        hover "ramenshopnight_1"
        focus_mask "ramenshopnight_1"
        hovered [Show("displayTextScreen", displayText = "Visit Ramen Shop")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("marketnightmap"),Hide("displayTextScreen"), Jump("visitramen")]

    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "idle2"
        hover "ramenshopnight_2"
        focus_mask "ramenshopnight_2"
        hovered [Show("displayTextScreen", displayText = "Visit alley")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("marketnightmap"),Hide("displayTextScreen"), Jump("visitalley")]

    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "idle3"
        hover "ramenshopnight_3"
        focus_mask "ramenshopnight_3"
        hovered [Show("displayTextScreen", displayText = "Visit Shop")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("marketnightmap"), Hide("actionbuttonshouse"), Hide("displayTextScreen"), Jump("visitshop")]

    

screen marketshop1():
    imagemap:
        ground "bg ramenshop_shop1"

screen marketshop2():
    imagemap:
        ground "bg ramenshop_shop2"

screen marketshop3():
    imagemap:
        ground "bg ramenshop_shop3"

screen marketshopreturn():
    imagemap:
        ground "bg_return"

screen marketreturn(): #top right return

    imagebutton:
        xalign 0.95 yalign 0.05
        auto "images/ui/return_button_%s.png"
        hovered Show("displayTextScreen", displayText = "Return to Market")
        unhovered [Hide("displayTextScreen"), Hide("marketshop3")]
        action [Jump("_market_return_action")]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"

label _market_return_action: #Make return button transition smoother
    hide screen displayTextScreen
    hide screen shopkeeper
    hide screen marketreturn
    scene black
    with dissolve
    jump market

screen returnbutton():  #clickable bottom screen return

    button:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        xalign 0.0 yalign 1.2
        xysize (1280,260)
        hovered [Show("displayTextScreen", displayText = "Return to Market"), Show("marketshopreturn")]
        unhovered [Hide("displayTextScreen"), Hide("marketshopreturn")]
        action [Jump("market")]

#edit interactions here -------------------------------------------------------------------

label shoptocall:
    $ shopkeep_interactions += 1
    $ shopkeep_block = False
    if shopkeep_annoyance == 1:
        if shopkeep_interactions == 1:
            #Shopkeeper Quest
            if quest.is_state("boshop_1", "unlocked") == False:

                $ notification("Quest discovered!")
                $ quest.check("boshop_1", "unlocked")
                $ quest.add([
                
                    Quest("shop1_1", ("Try... touching(?) the shopkeeper"), ("Shopkeeper's burden"), ("in progress")),
                    Quest("shop1_2", ("Spend at least $200"), ("Shopkeeper's burden"), ("pending")),
                    Quest("shop1_3", ("Find the shopkeeper's keepsake"), ("Shopkeeper's burden"), ("pending")),
                    Quest("shop1_4", ("Spend at least $500"), ("Shopkeeper's burden"), ("pending"),wip=True),
                    Quest("shop1_5", ("Interact with the shopkeeper"), ("Shopkeeper's burden"), ("pending"),wip=True),
                    
                ]) 
            hide screen shopinteraction1
            $ texttosend = "Umm... Can I help you?"
            call screen shopinteraction1(texttosend)
            

        elif shopkeep_interactions == 2:
            $ texttosend = "Insistent... aren't you?"
            call screen shopinteraction1(texttosend)

        elif shopkeep_interactions == 3:
            $ texttosend = "Yes! I am here, Can you stop touching me?"
            call screen shopinteraction1(texttosend)

        elif shopkeep_interactions == 4:
            $ texttosend = "H-hey! No more touching!"
            call screen shopinteraction1(texttosend)

        elif shopkeep_interactions == 5:
            $ texttosend = "S-stop it right this moment"
            call screen shopinteraction1(texttosend)

        else:
            $ shopkeep_interactions = 0
            play sound("/audio/soun_fx/select1.opus")
            $ texttosend = "I've had enough!"
            hide screen shopScreen
            
            $ shopkeep_annoyance += 1
            hide screen shopkeeper
            hide screen displayTextScreen
            show shopkeeperimage with dissolve:
                zoom 0.7 xpos -60 ypos 0.01
            "She is getting irritated by your insistence with touching her..."
            show screen shopkeeper
            call screen shopinteraction1(texttosend)
            $ ui.interact()
                

    if shopkeep_annoyance == 2:
        if shopkeep_interactions == 1:
            $ texttosend = "Hands to yourself!"
            call screen shopinteraction1(texttosend)

        elif shopkeep_interactions == 2:
            $ texttosend = "This is your last warning!"
            call screen shopinteraction1(texttosend)

        elif shopkeep_interactions == 3:
            $ texttosend = "Do that one more time and I'll kick your ass out!"
            call screen shopinteraction1(texttosend)


        else:
            play sound("/audio/soun_fx/select1.opus")
            $ texttosend = "Piece of shit"
            hide screen shopScreen
            #Shopkeeper Quest
            $ shopkeep_block = True
                
            if shopkeep_block == True:
                show shopkeeperimage:
                    zoom 0.7 xpos -60 ypos 0.01
                hide screen shopkeeper
                hide screen displayTextScreen
                "Shopkeeper" "Get out of here you creep!"
                hide shopkeeperimage with dissolve
            if quest.exists("shop1_1"):
                if quest.is_state("shop1_1", "completed") == False:
                    $ notification("Quest updated")
                    $ quest.check("shop1_1", "completed")
                    $ quest.check("shop1_2", "in progress")
                    $ quest.check("shop1_3", "in progress")
                    scene bg ramenshop with dissolve
                    bo"Feisty... I was just poking around!"

            jump market
    $ ui.interact()
#------------------------------------------------------------------------------------------

#interaction scrolling text

screen shopinteraction1(text):
    frame:
        xpos 70 ypos 500
        ymaximum 200 xmaximum 300
        xfill True
        yfill True
        # background None
        text "[text]" xalign 0.5 yalign 0.5 size 30 at move_text
        background"scrollingtextbg" at move_text
        


image scrollingtextbg = "ui/bg_text_scrolling5.png"

transform move_text:
    parallel: 
        subpixel True
        xalign 0.1 yalign 0.75  
        linear 3 ypos 0.45
    parallel:
        pause 2                 
        linear 1 alpha 0


#------------------------------Mobile Animated Indicators---------------------------------------------
# 1. The animation transform.
transform tap_icon_animation:
    subpixel True
    zoom 1.0
    linear 0.5 zoom 1.1
    linear 0.5 zoom 1.0
    repeat

# 3. Positioned tap icons (without animation in definition).
image tap_icon_shop:
    "images/background/tap_icon.png"
    zoom 0.2
    pos (1100, 450)
    anchor (0.5, 0.5)

image tap_icon_alley:
    "images/background/tap_icon.png"
    zoom 0.2
    pos (633, 446)
    anchor (0.5, 0.5)

image tap_icon_ramen:
    "images/background/tap_icon.png"
    zoom 0.2
    pos (160, 450)
    anchor (0.5, 0.5)