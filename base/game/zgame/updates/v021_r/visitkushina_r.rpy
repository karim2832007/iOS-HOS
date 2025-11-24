label visitkushina_love_repeat:
    "fill"




label kushinavisit_hate_repeat:
    scene black with dissolve
    $ playmusic("/audio/ost/evilhymn.opus", 1.2)
    $ renpy.sound.play("/audio/soun_fx/growl2.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    show kurama1 with flashred
    show kurama1:
        easein 1 alpha 0.0
    show red_shockwave with dissolve
    show red_shockwave:
        easein 2 alpha 0.0
    show screen parallax1280("kushina_dream hate1",1,0.2) with dissolve
    call showscrollingimage from _call_showscrollingimage_303
    ku"[bo_name],You are here! Have you finally regained your senses?"
    bo"Show her our power, child!"
    ku"[bo_name_stutter]...?"
    call hidescrollingimage("Click twice to show her your power!") from _call_hidescrollingimage_248
    scene black
    $ renpy.sound.play("/audio/soun_fx/thunderstrike.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    show kushina_dream hate1_1 with flash:
        yalign 1.0
    show kushina_dream hate1_1:
        easein 4 yalign 0.3
    if kushina_resistance <=10:
        ku"W-what is the meaning of this!{p}Kurama, you bastard! Let go of him!"
        beast"Bwa-ha-hahaaa! She still thinks this is my will alone..."
    elif kushina_resistance <=30:
        ku"N-not again... [bo_name] please!{p}Snap out of it!"
    else:
        ku"Kurama... you BASTARD!{p}Let the child free of your clutches!"
    $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    show kushina_dream hate1_2 with flash:
        yalign 0.2
    beast"Show her!"
    scene black with dissolve
    bot"Kurama, go easy on her. She is my granny, you know..."
    ku"Th-thank you, [bo_name]-"
    if kushina_resistance <=10:
        bot"I was thinking ropes instead of chains would be better!" with vpunch
    else:
        bot"Just make sure we keep her tied! Just in case she tries anything, hehe!"
    ku"Wh-what!?"
    scene v21_kushina_hate_bg
    show v21_kushina_hate_t standing:
        zoom 0.75 xalign 0.5
    with dissolve
    beast"Oooh? I like where this is going, kid..."

    default kushina_resistance = 0
    default kushina_resistance_actionstaken = 0

    menu kushina_starting_menu_repeat:
        ku"W-what is the meaning of this!{p}Kurama, you bastard! Let go of him!"
        "{color=[hatredcolor]}Break her resistance!{/color}" if kushina_tiedup == False:
            jump kushina_break_resistance

        "{color=[hatredcolor]}Tie her up!{/color}" (supporter_scene = True) if kushina_resistance >= 25 and kushina_tiedup == False:
            default kushina_tiedup = False
            label replayjump_kushinatieherup:
            $ initialize_replay_defaults()
            $ call_label_action("kushina_tierherup_shibari")
            call supp_rew from _call_supp_rew_20
            jump kushina_starting_menu_repeat
            
            

        # "{color=[hatredcolor]}Untie her{/color}" if kushina_resistance >= 25 and kushina_tiedup == True:
        #     $ kushina_tiedup = False
        #     "fill"
        #     jump kushina_starting_menu_repeat
        
        # "{color=[hatredcolor]}Punish her!{/color}" if kushina_resistance >= 50 and kushina_tiedup == True:
        #     "fill"
        #     jump action_taken

        "{color=[hatredcolor]}Take her! (WIP){/color}" if kushina_resistance >= 50 and kushina_tiedup == True:
            dev"Coming soon!"
            jump kushina_starting_menu_repeat

        "{color=[hatredcolor]}???{/color}" if kushina_resistance < 25:
            "Continue breaking Kushina's resistance until she succumbs to your powers!"
            jump kushina_starting_menu_repeat
        "{color=[hatredcolor]}???{/color}" if kushina_resistance < 50:
            "Continue breaking Kushina's resistance until she succumbs to your powers!"
            jump kushina_starting_menu_repeat
       
        
        "Information":
            show screen kushinamenuinfo
            jump kushina_starting_menu_repeat
        

label kushinavisit_love_repeat:
    scene black with dissolve
    dev"Kushina's love options aren't yet available, but you can still discover new love related events in your house!"
    dev"Check back here once v0.22 drops!"
    jump repeat_kushina_love_introscene
    # jump action_taken



        






label hatred_path_success_transition:
    $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.9)    
    show kurama1 with flash
    show kurama1:
        easein 2 alpha 0.0
    "A path of darkness has been chosen. There is no turning back."
    stop sfx1 fadeout 1
    stop sfx2 fadeout 1
    call chosen_hate_path from _call_chosen_hate_path
    "..."
    jump v20_testhatepath_temp    
    jump action_taken

label love_path_success_transition:
    
    $ renpy.sound.play("/audio/soun_fx/ominous_sound.opus", channel="sfx3", loop=False, relative_volume = 0.9)    
    show kushina_dream intro1_0 with flash
    show kushina_dream intro1_0:
        easein 2 alpha 0.0
    "A path of light has been chosen. There is no turning back."
    stop sfx1 fadeout 1
    stop sfx2 fadeout 1
    call chosen_love_path from _call_chosen_love_path
    jump v20_testlovepath_temp




















init python:
    def close_kushinamenuinfo():
        renpy.hide_screen("kushinamenuinfo")
        renpy.hide_screen("displayTextScreen")
        renpy.hide_screen("test_kushinamenuinfo")


default selected_kushinamenuinfo = "kushina"
screen kushinamenuinfo():
    on "show" action If(
        renpy.has_screen("test_kushinamenuinfo"),
        [Hide("kushinamenuinfo"), Show("test_kushinamenuinfo"), SetVariable("selected_kushinamenuinfo", "kushina")],
        None
    )
    
    default dropdown_open = False
    zorder 100

    

    key "mouseup_3" action [Hide("kushinamenuinfo"),Hide("test_tsunade"), Hide("displayTextScreen")] #close with rightclick
    
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
            hovered Show("displayTextScreen", displayText = "Close Menu")
            unhovered Hide("displayTextScreen")
            action [Function(close_kushinamenuinfo)]

        #left selection menu
        vbox:
            xalign 0.05 yalign 0.2
            text "Menu" xalign 0.5 size (50 if renpy.variant("pc") else 40)
        vbox:
            
            xalign (0.05 if renpy.variant("pc") else 0.02) yalign (0.5 if renpy.variant("pc") else 0.55)
            spacing 30
            #Tsunade
            textbutton "Kushina":
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "Open Kushina's panel")
                unhovered Hide("displayTextScreen")
                action SetVariable("selected_kushinamenuinfo", "kushina")

        vbox:
            xalign 1.2 yalign 0.5
            if selected_kushinamenuinfo ==  "kushina":
                add "kushina_dream int0_1t" at dissolvehack:
                    zoom 0.75 xalign 0.5



        if selected_kushinamenuinfo == "kushina":
            vbox:
                xalign 0.4 yalign 0.4
                text "Name: Kushina Uzumaki" xalign 0.5
                text "Age: ??" xalign 0.5
                null height 40 #add space
                frame:
                    xalign 0.65 yalign 0.53
                    background "#d3d3d320"
                    vbox:
                               
                        text "A former host of your curse." xalign 0.5
                        text "Now a formidable ally, or foe." xalign 0.5
                        text "Your [na_rel]'s mother." xalign 0.5
                 
                        null height 20 #add space
                        use kushina_relationship_bar







screen kushina_relationship_bar:
    frame:
        xalign 0.5
        yalign 0.5
        background None  # Removes the background
        padding (0,0)    # Removes the padding
        vbox:
            spacing 10
            text "Broken resistance: [kushina_resistance]" xalign 0.5
            $ relationship_text = ""
            $ text_color = "#ffffff"  # default white
            if kushina_resistance <= 25:
                $ relationship_text = "Holding Strong"
                $ text_color = "#a3d9ff"
            elif kushina_resistance <= 50:
                $ relationship_text = "Damaged"
                $ text_color = "#7fc8f8"
            elif kushina_resistance <= 75:
                $ relationship_text = "Broken" # Friends with Benefits?
                $ text_color = "#5cb7f5"
  
            text "[relationship_text]" xalign 0.5 color text_color
            fixed:
                xsize 400
                ysize 30
                add PartnershipBar(400, 30, kushina_resistance, 0, 100)