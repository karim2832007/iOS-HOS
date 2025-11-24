
default bathroom_locked = False
label bathroom_morning:
    call resetbuttons from _call_resetbuttons
    call hideUI from _call_hideUI_2
    if hin_location == "bathroom" and him_location == "bathroom":
        scene bathroom door with dissolve
        call enableaction from _call_enableaction
        bot"Someone is inside..."
    elif hin_location == "bathroom":
        scene bathroom door with dissolve
        call enableaction from _call_enableaction_1
        bot"Someone is inside..."
    elif him_location == "bathroom":
        scene bathroom door with dissolve
        call enableaction from _call_enableaction_2
        bot"Someone is inside..."
        
    else:
        scene bg bathroom_new with dissolve
        jump empty_bathroom_actions #v0.19
    call showUIhouse from _call_showUIhouse_3
    $ ui.interact()

label bathroom_evening:
    call resetbuttons from _call_resetbuttons_1
    call hideUI from _call_hideUI_3
    if hin_location == "bathroom" and him_location == "bathroom":
        scene bathroom door with dissolve
        call enableaction from _call_enableaction_3
        bot"Someone is inside..."
    elif hin_location == "bathroom":
        scene bathroom door with dissolve
        call enableaction from _call_enableaction_4
        bot"Someone is inside..."
    elif him_location == "bathroom":
        scene bathroom door with dissolve
        call enableaction from _call_enableaction_5
        bot"Someone is inside..."
        
    else:
        scene bg bathroom_new with dissolve
        jump empty_bathroom_actions #v0.19

    call showUIhouse from _call_showUIhouse_4
    $ ui.interact()

label bathroom_night:
    call resetbuttons from _call_resetbuttons_2
    call hideUI from _call_hideUI_4
    if hin_location == "bathroom" and him_location == "bathroom":
        scene bathroom door with dissolve
        call enableaction from _call_enableaction_6
        bot"Someone is inside..."
    elif hin_location == "bathroom":
        scene bathroom door with dissolve
        call enableaction from _call_enableaction_7
        bot"Someone is inside..."
    elif him_location == "bathroom":
        scene bathroom door with dissolve
        call enableaction from _call_enableaction_8
        bot"Someone is inside..."
        
    else:
        scene bg bathroom_new with dissolve
        jump empty_bathroom_actions #v0.19

    call showUIhouse from _call_showUIhouse_5
    $ ui.interact()

label bathroomntalkmenu:
    call hideUI from _call_hideUI_5
    menu:
        "..."
        "Talk to [hin_name]" if hin_location == "bathroom":
            bo"a"
            call showUIhouse from _call_showUIhouse_6
            $ ui.interact()
        "Talk to [him_name]" if him_location == "bathroom":
            bo"a"
            call showUIhouse from _call_showUIhouse_7
            $ ui.interact()
        "Return":
            call showUIhouse from _call_showUIhouse_8
            $ ui.interact()


label bathroomactionmenu:
    call hideUI from _call_hideUI_6
    menu tryopendoor:
        "..."
        "Take a shower" if hin_location != "bathroom" and him_location != "bathroom":
            jump take_a_shower
        
        "Open the door" if hin_location == "bathroom" or him_location == "bathroom":
            default tryopen = False
            if tryopen == True:
                if hin_location == "bathroom":
                    $ renpy.sound.play("/audio/soun_fx/locked_door.opus", channel="sfx2", loop=False, relative_volume = 1)
                    "*Door rattles*"
                    call changeRespect("Hinata",-1, "none") from _call_changeRespect_26
                    hin "[bo_name], Stop it!" with vpunch            
                    bot "What did I expect..."
                elif him_location == "bathroom":
                    $ renpy.sound.play("/audio/soun_fx/locked_door.opus", channel="sfx2", loop=False, relative_volume = 1)
                    call changeRespect("Himawari",-1, "none") from _call_changeRespect_27
                    "*Door rattles*"
                    him "Is it you again!?" with vpunch
                    him "Don't make me get out there, [bo_name]!"          
                    bot "What did I expect..."
                jump tryopendoor
            else:   
                if hin_location == "bathroom":
                    $ renpy.sound.play("/audio/soun_fx/locked_door.opus", channel="sfx2", loop=False, relative_volume = 1)
                    "*Door rattles*"
                    hin"Occupied!" with vpunch            
                elif him_location == "bathroom":
                    $ renpy.sound.play("/audio/soun_fx/locked_door.opus", channel="sfx2", loop=False, relative_volume = 1)
                    "*Door rattles*"
                    him"Hey! I am inside!" with vpunch
                bo "My bad, I didn't realize!"
                bot "It's locked from the inside..."
                $ tryopen = True
                jump tryopendoor
            
        "Peek inside" if hin_location == "bathroom" or him_location == "bathroom":
            show bathroom door with dissolve:
                zoom 1.5 xalign 0.9 yalign 0.2
            "You use the small creek of the door to peek inside..."
            scene black with dissolve
            default showerquestadded_1 = False
            if showerquestadded_1 == True:
                jump showerpeakquest
            else:
                $ showerquestadded_1 = True
                $ notification("Quest discovered")
                $ quest.check("bo_shower_1", "unlocked")
                $ quest.add([
                    Quest("shower1_1", ("Spy on someone showering"), ("Just a peek!"), "in progress"),
                    Quest("shower1_2", ("Keep spying..."), ("Just a peek!"), "pending"),
                    Quest("shower1_3", ("Wait outside..."), ("Just a peek!"), "pending"),
                ])
                jump showerpeakintro

        "{color=[obediencecolor]}I need to use the bathroom!{/color}" if (hinabathroom_counter == 2 or himabathroom_counter == 2) and (him_location == "bathroom" or hin_location == "bathroom"): #essentially if shower1_2 completed
            if him_location == "bathroom":
                jump hima_bathroom_event1
            elif hin_location == "bathroom":
                jump hinata_bathroom_event1
        


        "Return":
            call showUIhouse from _call_showUIhouse_9
            $ ui.interact()


label showerpeakquest:
    if quest.is_state("bo_shower_1", "unlocked"): #check if quest is not completed yet.
        if quest.is_state("shower1_2", "in progress"):
            jump shower1_2

        else:
            jump shower1_2
    else:
        jump shower1_2 #todo change in the future if new content is added

label showerpeakintro:
    if hin_location == "bathroom":
        label hinabathroompeakfirst:
        $ initialize_replay_defaults()
        default hinabathroom_counter = 0
        $ hinabathroom_counter = 1
        pause 1
        show screen bathroom_peaking("bathroomhina1")
        show screen peaking_overlay
        
        
        bo"H-holy Shit!" with vpunch
        "Move your cursor in any direction to get a better view."
        bot"[hin_rel] has such an unbelievable body for her age..."
        call increaselust(10) from _call_increaselust_11
        bot"I am getting hard again just perving on her..."
        bot"I really am the worst..."
        bot"But fuck me! Those perfectly shaped tits... Her plump ass..."
        bot"[hin_rel] is a living goddess."
        call hidescrollingimage from _call_hidescrollingimage_127
        scene black
        hide screen bathroom_peaking
        hide screen peaking_overlay
        show bathroom door with dissolve:
            zoom 1.5 xalign 0.9 yalign 0.2
        bot"I better stop before I get caught..."
        show bathroom door with dissolve:
            zoom 1.0
        scene black with dissolve
        $ renpy.end_replay()
        show boruto boner0 with dissolve:
            zoom 1
        bot"Or worse, do something stupid."
        if quest.is_state("shower1_1", "in progress"):
            $ notification ("Quest updated")
            $ quest.check("shower1_1", "completed")
            $ quest.check("shower1_2", "in progress")
        call increaselust(10) from _call_increaselust_12
        jump action_taken
    elif him_location == "bathroom":
        label himabathroompeakfirst:
        $ initialize_replay_defaults()
        default himabathroom_counter = 0
        $ himabathroom_counter = 1
        pause 1
        show screen bathroom_peaking("himabathroomstart")
        show screen peaking_overlay    
        bo"F-fuck me!" with vpunch
        "Move your cursor in any direction to get a better view."
        bot"[him_name] is just about ready to take a shower..."
        bot"She seems to be soaping up her small titties..."
        call increaselust(10) from _call_increaselust_13
        bot"Relative to [hin_rel]'s of course. But still, her toned tummy is quite the sight..."
        bot"Come on you little cock-tease, put on a show for your [him_rel_to_bo]!"
        show screen bathroom_peaking("bathroomhima1") with dissolve
        bot"That's it! Show me that tight little ass of yours..."
        bot"You might not have your [hin_rel_mother]'s curves, but your well-trained, tight little body more than makes up for it." 
        bot"I swear if you weren't such a total bitch, you'd be close to my perfect kind of girl..."
        bot"It's a shame you are my [him_rel], otherwise I'd teach that bratty ass of yours a lesson in humility..."
        bot"Then again, do I care that you are my [him_rel]?"
        call increaselust(10) from _call_increaselust_14
        bot"Maybe that's an extra incentive to teach you a thing or two..."
        call hidescrollingimage from _call_hidescrollingimage_128
        show bathroom door with dissolve:
            zoom 1.5 xalign 0.9 yalign 0.2
        bot"I better stop before I get caught..."
        show bathroom door with dissolve:
            zoom 1.0
        scene black with dissolve
        $ renpy.end_replay()
        show boruto boner0 with dissolve:
            zoom 1
        bot"Or worse, do something stupid."
        if quest.is_state("shower1_1", "in progress"):
            $ notification ("Quest updated")
            $ quest.check("shower1_1", "completed")
            $ quest.check("shower1_2", "in progress")
        call increaselust(10) from _call_increaselust_15
        jump action_taken


label shower1_2:
    if hin_location == "bathroom":
        if hinabathroom_counter == 0:
            jump hinabathroompeakfirst
        else:
            $ hinabathroom_counter = 2
            pause 1
            show screen bathroom_peaking("bathroomhina1")
            show screen peaking_overlay
            with dissolve
            
            
            bo"There she is again..."
            "Move your cursor in any direction to get a better view."
            bot"I don't think I'll ever get tired of watching [hin_rel]'s sublime body..."
            call increaselust(10) from _call_increaselust_16
            bot"[hin_rel] is a living goddess."
            bot"But just watching her is quickly becoming inadequate..."
            bot"I need something more!"
            call hidescrollingimage from _call_hidescrollingimage_129
            show bathroom door with dissolve:
                zoom 1.5 xalign 0.9 yalign 0.2
            bot"But I better stop before I get caught..."
            show bathroom door with dissolve:
                zoom 1.0
            scene black with dissolve
            show boruto boner0 with dissolve:
                zoom 1
            bot"F-fuck! it kinda h-hurts..."
            if quest.is_state("bo_shower_1", "unlocked"): #check if quest is not strikethroughed on left side (completed)
                if quest.is_state("shower1_2", "in progress"):
                    $ notification ("Quest updated")
                    $ quest.check("shower1_2", "completed")
                    $ quest.check("shower1_3", "in progress")
            call increaselust(10) from _call_increaselust_17
            jump action_taken


    elif him_location == "bathroom":
        if himabathroom_counter == 0:
            jump himabathroompeakfirst
        else:
            $ himabathroom_counter = 2
            pause 1
            label replay_himabathroompeakfirst:
            $ initialize_replay_defaults()
            show screen bathroom_peaking("himabathroomstart")
            show screen peaking_overlay    
            bo"There's that little cock-tease again..."
            "Move your cursor in any direction to get a better view."
            bot"She almost looks like she is about to gulp down the soap bottle..."
            bot"I wouldn't put it past her, she is as stupid as they get..."
            call increaselust(10) from _call_increaselust_18
            bot"And as hot as they get too, as much as I hate to admit it..."
            bot"Come on now my dear [him_rel], do the one thing you are good at..."
            show screen bathroom_peaking("bathroomhima1") with dissolve
            bot"That's right..."
            bot"Showing off your sexy little body! Probably the only use you have around this house..." 
            call increaselust(10) from _call_increaselust_19
            call hidescrollingimage from _call_hidescrollingimage_130
            show bathroom door with dissolve:
                zoom 1.5 xalign 0.9 yalign 0.2
            bot"But I better stop before I get caught..."
            show bathroom door with dissolve:
                zoom 1.0
            scene black with dissolve
            $ renpy.end_replay()
            show boruto boner0 with dissolve:
                zoom 1
            bot"F-fuck! it kinda h-hurts..."
            if quest.is_state("bo_shower_1", "unlocked"): #check if quest is not strikethroughed on left side (completed)
                if quest.is_state("shower1_2", "in progress"):
                    $ notification ("Quest updated")
                    $ quest.check("shower1_2", "completed")
                    $ quest.check("shower1_3", "in progress")
            call increaselust(10) from _call_increaselust_20
            jump action_taken


label shower1_3:
    #todo in future
    bo"fill"

label peakrepeat:
    #todo in future
    bo"fill"




















#Screens
########################################
##########################################


       
# screen scrolling_test(baseImage):
 
#     viewport:

#         edgescroll (330, 500)
#         yinitial 0.5
#         arrowkeys True
#         xfill False
#         xalign 0.5
#         add baseImage subpixel True

                
image particleFog = SnowBlossom("images//transitions/fog5.png", count=100, border=1000, xspeed=60, yspeed=5, start=5, fast=True, horizontal=True)
image particleFog_low = SnowBlossom("images//transitions/fog5.png", count=60, border=1000, xspeed=60, yspeed=5, start=5, fast=True, horizontal=True)

screen peeking1024(baseImage):
    on "show" action Function(mark_screen_image_gallery, baseImage)
    key "K_SPACE" action Return()
    button:
        action Return()
    viewport id "peeking1024":
        child_size (1670, 1024)
        edgescroll (340, 550)
        draggable True
        yinitial 0.1
        xinitial 0.1
        
        frame:
            background None
            xalign 0.5
            
            # Main viewport for panning, without transform
            viewport:
                area (320, 0, 1.0, 1.0)
                child_size (1670, 1024)
                edgescroll (340, 550)
                frame:
                    background None
                    
                    # Separate frame for the wobble effect
                    frame:
                        background None
                        at smooth_peek_wobble
                        add baseImage:
                            subpixel True
                            
                


            
                    

# Optional: Transform for additional effects
transform smooth_peek_wobble:
    parallel:
        xoffset 0
        block:
            ease 3.0 xoffset -15
            ease 3.0 xoffset 15
            repeat
    parallel:
        yoffset 0
        block:
            ease 2.0 yoffset 12
            ease 2.0 yoffset 6
            repeat

screen bathroom_peaking(baseImage):
    on "show" action Function(mark_screen_image_gallery, baseImage)
    key "K_SPACE" action Return()
    button:
        action Return()
    viewport id "testScene":
        child_size (1600, 1328)
        edgescroll (340, 550)
        draggable True
        yinitial 0.1
        xinitial 0.1
    
        frame:
            background None
            foreground "particleFog"
            
            xalign 0.5
            viewport:
                area (300, 0, 1.0, 1.0)
                child_size (1600, 1328)
                edgescroll (340, 550)
                add baseImage subpixel True

screen peaking(baseImage):
    on "show" action Function(mark_screen_image_gallery, baseImage)
    key "K_SPACE" action Return()
    button:
        action Return()
    viewport id "peaking":
        child_size (1600, 1328)
        edgescroll (340, 550)
        draggable True
        yinitial 0.1
        xinitial 0.1
    
        frame:
            background None            
            xalign 0.5
            viewport:
                area (320, 0, 1.0, 1.0)
                child_size (1600, 1328)
                edgescroll (340, 550)
                add baseImage subpixel True
    

screen peaking_overlay(baseImage="bgp peak"):
    
    sensitive False
    add baseImage xalign 0.5



screen genericparallax(baseImage): #used in intro
    on "show" action Function(mark_screen_image_gallery, baseImage)
    key "K_SPACE" action Return()
    button:
        action Return()
    viewport id "parallax":
        child_size (1290, 730)
        edgescroll (340, 550)
        draggable True
        yinitial 0.2
        xinitial 0.2
        add baseImage subpixel True zoom 0.4


screen parallaxsecretlovescene(baseImage): #used in secretlovescene
    on "show" action Function(mark_screen_image_gallery, baseImage)
    key "K_SPACE" action Return()
    button:
        action Return()
    viewport id "parallaxsecretlovescene":
        xalign 0.5
        edgescroll (340, 550)
        draggable True
        yinitial 1.0
        xinitial 0.5
        add baseImage subpixel True

