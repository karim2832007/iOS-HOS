init python:

    def close_relationships():
        renpy.hide_screen("relationships")
        renpy.hide_screen("displayTextScreen")
        renpy.hide_screen("test_relationships")

style dropdown_frame:
    background "#d3d3d320"
    padding (10, 10)
    xsize 250
default boruto_clothes = "Casual"
default himawari_clothes = "Casual"
default hinata_clothes = "Casual"









#cheat version / gymmenu


screen relationships():
    zorder 1001
    default selected_character = bo_name
    default dropdown_open = False
    on "show" action If(
        renpy.has_screen("test_relationships"),
        [Hide("relationships"), Show("test_relationships")],
        None
    )

    

    key "mouseup_3" action [Hide("relationships"), Hide("displayTextScreen")] #close with rightclick
    
    #full screen
    frame:
        xysize (1280,720)
        background Frame("gui/overlay/game_menu_2.png")
        button: #screen sized button to prevent lcicks from behind screen
            xysize (config.screen_width, config.screen_height)
            background None
            action NullAction() # No action to perform on click

        #close button
        imagebutton:    
            at customzoom3
            xalign 0.95
            yalign 0.05
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            auto "map/ui_close_%s.png"
            hovered Show("displayTextScreen", displayText = "Close Relationships screen")
            unhovered Hide("displayTextScreen")
            action [Function(close_relationships)]

        #portraits on left
        vbox:
            #boruto
            xalign 0.05 yalign 0.5
            text ""
            text "[bo_name]" color bo_color xalign 0.5
            imagebutton:
                at customzoom3
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "[bo_name] stats")
                unhovered Hide("displayTextScreen")
                auto "ui/icons/boru1_%s.png"
                action SetScreenVariable("selected_character", bo_name)
            #hinata
            text ""
            text "[hin_name]" color hin_color xalign 0.5
            imagebutton:
                at customzoom3
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "[hin_name] stats")
                unhovered Hide("displayTextScreen")
                auto "ui/icons/hina_%s.png"
                action SetScreenVariable("selected_character", hin_name)
            #himawari
            text ""
            text "[him_name]" color him_color xalign 0.5
            imagebutton:
                at customzoom3
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "[him_name] stats")
                unhovered Hide("displayTextScreen")
                auto "ui/icons/hima_%s.png"
                action SetScreenVariable("selected_character", him_name)

        #images of characters + outfits
        vbox:
            #Boruto
            xalign 0.4 yalign 0.5
            if selected_character == bo_name and boruto_clothes == "Casual":
                add "characters/headshots/boruto/boruto normal normal.webp" at dissolvehack:
                    zoom 0.36
            if selected_character == bo_name and boruto_clothes == "Underwear":
                add "characters/headshots/boruto/naked/boruto boxers1.webp" at dissolvehack:
                    zoom 0.36
            if selected_character == bo_name and boruto_clothes == "Naked":
                add "characters/headshots/boruto/naked/boruto naked1.webp" at dissolvehack:
                    zoom 0.36


            #Hinata
            if selected_character == hin_name and hinata_clothes == "Casual":

                if hinata_respect < 0:
                    add "characters/headshots/hinata/sweater/sweaterhina assertive.webp" at dissolvehack:
                        zoom 0.38
                elif hinata_respect <= 5:
                    add "characters/headshots/hinata/sweater/sweaterhina normal.webp" at dissolvehack:
                        zoom 0.38

                else:
                    add "characters/headshots/hinata/sweater/sweaterhina smiling.webp" at dissolvehack:
                        zoom 0.38


            if selected_character == hin_name and hinata_clothes == "Sportswear":
                add "characters/headshots/hinata/yoga/hinata hs concerned.webp" at dissolvehack:
                    zoom 0.7

            if selected_character == hin_name and hinata_clothes == "Dress":
                if hinata_respect < 0:
                    add "hinatadress shy2" at dissolvehack:
                        zoom 0.7
                elif hinata_respect <= 5:
                    add "hinatadress shy" at dissolvehack:
                        zoom 0.7

                else:
                    add "hinatadress normal" at dissolvehack:
                        zoom 0.7

            if selected_character == hin_name and hinata_clothes == "Maid":
                if hinata_respect < 0:
                    add "ramenhinata angry1" at dissolvehack:
                        zoom 0.7
                elif hinata_respect <= 5:
                    add "ramenhinata serious1" at dissolvehack:
                        zoom 0.7

                else:
                    add "ramenhinata smiling1" at dissolvehack:
                        zoom 0.7


            #Himawari
            if selected_character == him_name and himawari_clothes == "Casual":

                if himawari_respect < 0:
                    add "characters/headshots/himawari/himawari mad.webp" at dissolvehack:
                        zoom 0.34
                elif himawari_respect <= 5:
                    add "characters/headshots/himawari/himawari smug1.webp" at dissolvehack:
                        zoom 0.34

                else:
                    add "characters/headshots/himawari/himawari smugshy.webp" at dissolvehack:
                        zoom 0.37

            if selected_character == him_name and himawari_clothes == "School":
                if himawari_respect < 0:
                    add "himaschoolt angry" at dissolvehack:
                        zoom 0.57
                elif himawari_respect <= 5:
                    add "himaschoolt smug" at dissolvehack:
                        zoom 0.57
                else:
                    add "himaschoolt normal" at dissolvehack:
                        zoom 0.57

            if selected_character == him_name and himawari_clothes == "Bikini":
                if himawari_respect < 0:
                    add "hima_ss_angry" at dissolvehack:
                        zoom 0.7
                elif himawari_respect <= 5:
                    add "hima_ss_embarrassed" at dissolvehack:
                        zoom 0.7
                else:
                    add "hima_ss_normal" at dissolvehack:
                        zoom 0.7
   
        #stats of characters
        vbox:
            xalign 0.8 yalign 0.5
            #boruto
            if selected_character == bo_name:
                text "Name: {color=[bo_color]}[bo_name]{/color}"
                text "Age: [bo_age]"
                vbox:
                    align (-0.2, 0.0)  
                    
                    # Main button that toggles the dropdown and shows selected option
                    textbutton "Clothing: [boruto_clothes]":
                        action ToggleScreenVariable("dropdown_open")
                        hover_sound "audio/soun_fx/select2.opus"
                        hovered Show("displayTextScreen", displayText = "Click to change clothing when in [bo_name]'s bedroom")
                        unhovered Hide("displayTextScreen")

                    
                    # Change clothing only if in bedroom
                    if boruto_location == "borutobedroom":
                        showif dropdown_open:
                            frame:
                                style "dropdown_frame"
                                vbox:
                                    textbutton "Casual":
                                        action [SetVariable("boruto_clothes", "Casual"), SetScreenVariable("dropdown_open", False)]
                                    textbutton "Underwear":
                                        action [SetVariable("boruto_clothes", "Underwear"), SetScreenVariable("dropdown_open", False)]
                                    textbutton "Naked":
                                        action [SetVariable("boruto_clothes", "Naked"), SetScreenVariable("dropdown_open", False)]
                                



                text ""
                text ""
                #lust
                button:
                    text "Lust: [percentage]%"
                    action NullAction()
                    hover_sound "audio/soun_fx/select2.opus"
                    hovered Show("displayTextScreen", displayText = "[bo_name]'s demeanor heightened by his condition {p} -The higher your lust is, the more likely you are to perform depraved acts. {p} -Your lust passively increases by 10 each day {p} -Reduce your lust meter by climaxing or fantasizing. {p} -Keep your meter low if you value your {color=[lovecolor]}relationship{/color} with girls. {p} -Keep your meter high if your approach is more {color=[hatredcolor]}sinister{/color} in nature.")
                    unhovered Hide("displayTextScreen")

                #money
                button:
                    text "Money: [money]"
                    action NullAction()
                    hover_sound "audio/soun_fx/select2.opus"
                    hovered Show("displayTextScreen", displayText = "Currency currently held {p} -Can be used to purchase items from the shop {p} -Can be used in some cases to improve your stats or relationships")
                    unhovered Hide("displayTextScreen")
                hbox:
                    #Strength
                    button:
                        text "Strength: [strength] {color=#808080}([strengthlevel]/100){/color}"
                        action NullAction()
                        hover_sound "audio/soun_fx/select2.opus"
                        hovered Show("displayTextScreen", displayText = _("[bo_name]'s physical capabilities. {p} -Can be increased by finding different ways to 'Train' {p} -Can unlock different options/interactions when increased"))
                        unhovered Hide("displayTextScreen")
                    imagebutton:
                            idle Transform("info_hover", size=(35, 35))
                            hover Transform("info_idle", size=(35, 35))
                            hovered Show("displayTextScreen", displayText = "Open Strength Menu")
                            unhovered Hide("displayTextScreen")
                            action Show("gymmenu")
                            hover_sound "audio/soun_fx/select2.opus"

                #Dominance
                button:
                    text "{color=[dominancecolor]}Dominance: {/color}[dominance] (Level {color=[dominancecolor]}[dominance_level]{/color})"
                    action NullAction()
                    hover_sound "audio/soun_fx/select2.opus"
                    hovered Show("displayTextScreen", displayText = "How assertive [bo_name] is. {p} -Can be increased by selecting {color=[dominancecolor]}dominance{/color} related options {p} -Can unlock different {color=[dominancecolor]}options/interactions{/color} when increased")
                    unhovered Hide("displayTextScreen")

                # hatred / impulse
                # Check if the love path has been chosen
                if chosen_love_path:
                    # If YES, display the "Impulse" version of the stat
                    button:
                        # Text is changed, and the (Level...) part is removed
                        text "{color=[impulsecolor]}Impulse: {/color}[hatred]"
                        action NullAction()
                        hover_sound "audio/soun_fx/select2.opus"
                        # The description (displayText) is changed
                        hovered Show("displayTextScreen", displayText = _("How {color=[impulsecolor]}impulsive{/color} [bo_name] is. {p} -Can be increased by making {color=[impulsecolor]}impulsive{/color} choices. {p} -Can lead to a game over state if left uncontrolled."))
                        unhovered Hide("displayTextScreen")
                else:
                    # If NO (meaning hate path was chosen OR no choice was made yet), display the original "Hatred" stat
                    button:
                        text "{color=[hatredcolor]}Hatred: {/color}[hatred] (Level {color=[hatredcolor]}[hatred_level]{/color})"
                        action NullAction()
                        hover_sound "audio/soun_fx/select2.opus"
                        hovered Show("displayTextScreen", displayText = _("How hateful [bo_name] is. {p} -Can be increased by selecting {color=[hatredcolor]}hatred{/color} related options {p} -Can present different {color=[hatredcolor]}options/interactions{/color} when increased {p} -Can lock you out of {color=[lovecolor]}romance/love{/color} options when high {p} *Attributes with the 'Level' suffix can be upgraded up to Level 5 by reaching certain milestones"))
                        unhovered Hide("displayTextScreen")







            #hinata
            elif selected_character == hin_name:
                text "Name: {color=[hin_color]}[hin_name]{/color}"
                text "Relationship: [hin_rel]"
                text "Age: [hin_age]"
                #outfits
                textbutton "Outfit: [hinata_clothes]":
                    action ToggleScreenVariable("dropdown_open")
                    hover_sound "audio/soun_fx/select2.opus"
                    hovered Show("displayTextScreen", displayText = "Check [hin_name]'s available outfits")
                    unhovered Hide("displayTextScreen")

                showif dropdown_open:
                    frame:
                        style "dropdown_frame"
                        vbox:
                            textbutton "Casual":
                                action [SetVariable("hinata_clothes", "Casual"), SetScreenVariable("dropdown_open", False)]
                            textbutton "Sportswear":
                                action [SetVariable("hinata_clothes", "Sportswear"), SetScreenVariable("dropdown_open", False)]

                            if v21_hinatadate_progression >=1 or hinatadress_outfit_unlocked == True:
                                textbutton "Formal Dress":
                                    action [SetVariable("hinata_clothes", "Dress"), SetScreenVariable("dropdown_open", False)]
                            else:
                                textbutton "Formal Dress (Locked)":
                                    action [SetScreenVariable("dropdown_open", False)]
                                    
                            

                            if hinata_obedience.level >= 2 or hinata_maidoutfit_unlocked == True:
                                textbutton "Maid":
                                    action [SetVariable("hinata_clothes", "Maid"), SetScreenVariable("dropdown_open", False)]
                                    # action [SetScreenVariable("dropdown_open", False)]
                            else:
                                textbutton "Maid (Locked)":
                                    action [SetScreenVariable("dropdown_open", False)]
                            
                            textbutton "(Locked)":
                                action [SetScreenVariable("dropdown_open", False)]
                                    
                            
                text ""
                text ""


               


                #obedience
                button:
                    text "{color=[obediencecolor]}Obedience: {/color}[hinata_obedience] (Level {color=[obediencecolor]}[hinata_obedience_level]{/color})"
                    action NullAction()
                    hover_sound "audio/soun_fx/select2.opus"
                    hovered Show("displayTextScreen", displayText = "[hin_name]'s corruption and likelihood of accepting your advances. {p} -Can be increased by selecting {color=[obediencecolor]}obedience{/color} related options {p} -Can unlock different {color=[obediencecolor]}options/interactions{/color} when increased {p} *Attributes with the 'Level' suffix can be upgraded up to Level 5 by reaching certain milestones")
                    unhovered Hide("displayTextScreen")

                # hinata love / affection
                # Check if the hate path has been chosen
                if chosen_hate_path:
                    # If YES, display the "Affection" version of the stat
                    button:
                        # Text is changed, and the (Level...) part is removed
                        text "{color=[lovecolor]}Affection: {/color}[hinata_love]"
                        action NullAction()
                        hover_sound "audio/soun_fx/select2.opus"
                        # The description (displayText) is changed
                        hovered Show("displayTextScreen", displayText = _("[hin_name]'s {color=[lovecolor]}affection{/color} towards you. {p} -You can exploit this {color=[lovecolor]}affection{/color} through deceptive manipulation tactics to get what you want from her."))
                        unhovered Hide("displayTextScreen")
                else:
                    # If NO (meaning love path was chosen OR no choice was made yet), display the original "Love" stat
                    button:
                        text "{color=[lovecolor]}Love: {/color}[hinata_love] (Level {color=[lovecolor]}[hinata_love_level]{/color})"
                        action NullAction()
                        hover_sound "audio/soun_fx/select2.opus"
                        hovered Show("displayTextScreen", displayText = _("[hin_name]'s love towards you. {p} -Can be increased by selecting {color=[lovecolor]}love{/color} related options {p} -Can unlock different {color=[lovecolor]}options/interactions{/color} when increased {p} *Attributes with the 'Level' suffix can be upgraded up to Level 5 by reaching certain milestones"))
                        unhovered Hide("displayTextScreen")

                #respect
                button:
                    text "Respect: [hinata_respect]"
                    action NullAction()
                    hover_sound "audio/soun_fx/select2.opus"
                    hovered Show("displayTextScreen", displayText = "[hin_name]'s respect towards you. {p}-Can be increased/decreased based on selected options {p}-Can lock you out of options when low{p}-Can affect interactions in various ways")
                    unhovered Hide("displayTextScreen")
                
            #himawari
            elif selected_character == him_name:
                text "Name: {color=[him_color]}[him_name]{/color}"
                text "Relationship: [him_rel]"
                text "Age: [him_age]"
                #outfits
                textbutton "Outfit: [himawari_clothes]":
                    action ToggleScreenVariable("dropdown_open")
                    hover_sound "audio/soun_fx/select2.opus"
                    hovered Show("displayTextScreen", displayText = "Check [him_name]'s available outfits")
                    unhovered Hide("displayTextScreen")

                showif dropdown_open:
                    frame:
                        style "dropdown_frame"
                        vbox:
                            textbutton "Casual":
                                action [SetVariable("himawari_clothes", "Casual"), SetScreenVariable("dropdown_open", False)]
                            if himaintrotutorial == False:
                                textbutton "School (Locked)":
                                    action [SetScreenVariable("dropdown_open", False)]
                            else:
                                textbutton "School":
                                    action [SetVariable("himawari_clothes", "School"), SetScreenVariable("dropdown_open", False)]
                            if hima_swimsuit_first_time == True:
                                textbutton "Bikini (Locked)":
                                    action [SetScreenVariable("dropdown_open", False)]
                            else:
                                textbutton "Bikini":
                                    action [SetVariable("himawari_clothes", "Bikini"), SetScreenVariable("dropdown_open", False)]

                            textbutton "Skimpy (Locked)":
                                action [SetScreenVariable("dropdown_open", False)]
                text ""
                text ""

                #obedience
                button:
                    text "{color=[obediencecolor]}Obedience: {/color}[himawari_obedience] (Level {color=[obediencecolor]}[himawari_obedience_level]{/color})"
                    action NullAction()
                    hover_sound "audio/soun_fx/select2.opus"
                    hovered Show("displayTextScreen", displayText = "[him_name]'s corruption and likelihood of accepting your advances. {p} -Can be increased by selecting {color=[obediencecolor]}obedience{/color} related options {p} -Can unlock different {color=[obediencecolor]}options/interactions{/color} when increased {p} *Attributes with the 'Level' suffix can be upgraded up to Level 5 by reaching certain milestones")
                    unhovered Hide("displayTextScreen")

                # himawari love / affection
                # Check if the hate path has been chosen
                if chosen_hate_path:
                    # If YES, display the "Affection" version of the stat
                    button:
                        # Text is changed, and the (Level...) part is removed
                        text "{color=[lovecolor]}Affection: {/color}[himawari_love]"
                        action NullAction()
                        hover_sound "audio/soun_fx/select2.opus"
                        # The description (displayText) is changed
                        hovered Show("displayTextScreen", displayText = _("[him_name]'s {color=[lovecolor]}affection{/color} towards you. {p} -You can exploit this {color=[lovecolor]}affection{/color} through deceptive manipulation tactics to get what you want from her."))
                        unhovered Hide("displayTextScreen")
                else:
                    # If NO (meaning love path was chosen OR no choice was made yet), display the original "Love" stat
                    button:
                        text "{color=[lovecolor]}Love: {/color}[himawari_love] (Level {color=[lovecolor]}[himawari_love_level]{/color})"
                        action NullAction()
                        hover_sound "audio/soun_fx/select2.opus"
                        hovered Show("displayTextScreen", displayText = _("[him_name]'s love towards you. {p} -Can be increased by selecting {color=[lovecolor]}love{/color} related options {p} -Can unlock different {color=[lovecolor]}options/interactions{/color} when increased {p} *Attributes with the 'Level' suffix can be upgraded up to Level 5 by reaching certain milestones"))
                        unhovered Hide("displayTextScreen")

                #respect
                button:
                    text "Respect: [himawari_respect]"
                    action NullAction()
                    hover_sound "audio/soun_fx/select2.opus"
                    hovered Show("displayTextScreen", displayText = "[him_name]'s respect towards you. {p} -Can be increased/decreased based on selected options {p} -Can lock you out of options when low{p} -Can affect interactions in various ways")
                    unhovered Hide("displayTextScreen")