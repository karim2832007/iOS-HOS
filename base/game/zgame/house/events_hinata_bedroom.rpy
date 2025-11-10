label bedroom_hinata_morning:
    call resetbuttons from _call_resetbuttons_9
    call hideUI from _call_hideUI_18
    if hin_location == "hinatabedroom" and him_location == "hinatabedroom":
        scene hinatabedroom day with dissolve
        call enabletalk from _call_enabletalk_20
    elif hin_location == "hinatabedroom":
        scene hinatabedroom day
        show screen hinata_bedroom_day1
        with dissolve
        call enabletalk from _call_enabletalk_21
    elif him_location == "hinatabedroom":
        scene hinatabedroom day with dissolve
        call enabletalk from _call_enabletalk_22
        
    else:
        scene hinatabedroom day with dissolve

    call showUIhouse from _call_showUIhouse_33
    $ ui.interact()

label bedroom_hinata_evening:
    call hideUI from _call_hideUI_19
    call resetbuttons from _call_resetbuttons_10
    if hin_location == "hinatabedroom" and him_location == "hinatabedroom":
        scene hinatabedroom day with dissolve
        call enabletalk from _call_enabletalk_23
    elif hin_location == "hinatabedroom":
        scene hinatabedroom day_idle
        show screen hinata_bedroom_day1
        with dissolve
        call enabletalk from _call_enabletalk_24
    elif him_location == "hinatabedroom":
        scene hinatabedroom day with dissolve
        call enabletalk from _call_enabletalk_25
        
    else:
        scene hinatabedroom day with dissolve

    call showUIhouse from _call_showUIhouse_34
    $ ui.interact()

label bedroom_hinata_night:
    call hideUI from _call_hideUI_20
    call resetbuttons from _call_resetbuttons_11
    if hin_location == "hinatabedroom" and him_location == "hinatabedroom":
        scene hinatabedroom night with dissolve
        call enabletalk from _call_enabletalk_26
        bo"Both are here"
    elif hin_location == "hinatabedroom":
        #midnight events
        if day_part == 4:
            show bathroom door with dissolve
            menu:
                bot"Her door is closed..."
                "Open it!":
                    $ renpy.sound.play("/audio/soun_fx/locked_door.opus", channel="sfx2", loop=False, relative_volume = 1)
                    "*Door rattles*"
                    default tryopendoorhinata = 0
                    if tryopendoorhinata == 0:
                        $ tryopendoorhinata += 1
                        bot"Huh? [hin_rel] doesn't usually lock her door at nights..."
                    elif tryopendoorhinata == 1:
                        $ tryopendoorhinata += 1
                        bot"Is she... scared of me?"
                    elif tryopendoorhinata == 2:
                        bot"I'll have to figure out a way in..."
                "return":
                    pause 0.01
        else:
            scene hinatabedroom night with dissolve
            call enabletalk from _call_enabletalk_27
    elif him_location == "hinatabedroom":
        scene hinatabedroom night with dissolve
        call enabletalk from _call_enabletalk_28
        
    else:
        scene hinatabedroom night with dissolve

    call showUIhouse from _call_showUIhouse_35
    $ ui.interact()
    #-------------------------------------------------



    
      
label hinatabedroomactionmenu:
    call hideUI from _call_hideUI_21
    menu:
        "..."
        "Choice 1":
            jump action_taken
        "Return":
            call showUIhouse from _call_showUIhouse_36
            $ ui.interact()


label hinatabedroomntalkmenu:
    call hideUI from _call_hideUI_22
    menu:
        "..."
        "Talk to [hin_name]" if hin_location == "hinatabedroom":
            hide screen hinata_bedroom_day1
            bo"Hey [hin_rel]..."
            scene hinatabedroom day with fade
            show shina shy2 at right
            show boruto normal at left
            with dissolve
            if hinata_respect < 0:
                hin"Oh, [bo_name_stutter]..."
                hin"I was just about to start training..."
            else:
                hin"Oh, [bo_name]... I was just about to start my work out when you appeared out of thin air!"
            show shina shy with dissolve
            hin"Is there something I can help you with?"
            menu hinabedroomdaytalk:
                hin"Is there something I can help you with?"
                "{color=[obediencecolor]}Can I join your training?{/color}":
                    jump hinatabedroomtraining

                "Give her a gift":
                    $ flowersininv = inventory.find_item_by_name("Flowers")
                    menu hinatagiftmenu:
                        "Select a gift..."
                        "A bouquet" if hinatai1sttimegift == True:
                            jump hinata1sttimebouquet

                        "{color=[lovecolor]}A thoughtful gift...{/color}"if hinatai1sttimegift == False and flowersininv!= None:
                            label hinata1sttimebouquet:
                            default hinatai1sttimegift = False
                            if hinatai1sttimegift == False:
                                $ hinatai1sttimegift = True
                                bo"[hin_rel], I have something for you..."
                                show shina shy2 with dissolve
                                hin"You do?" with vpunch
                                show boruto embarassed with dissolve
                                bo"I wanted to buy something for you, but I didn't know what, so I got this..."
                                call useItem(flowers,1) from _call_useItem_8
                                bo"A beautiful bouquet for my beautiful [hin_rel]!"
                                show shina worried with dissolve
                                hin"[bo_name] you shouldn't..."
                                show boruto worried2 with dissolve
                                bo"I know I've been acting a bit weird lately. This is just a reminder that I am still... me, you know?"
                                show shina concerned with dissolve
                                hin"You..."
                                show shina:
                                    easein 0.5 xalign 0.4
                                pause 0.4
                                show blackscreen with vpunch
                                hide shina
                                hide boruto
                                call changeLove("Hinata", 1,"hinatagift1sttime") from _call_changeLove_45
                                show shinahug2t
                                hide blackscreen
                                with dissolve
                                hin"You shouldn't have done that for me [bo_name]..."
                                bo"You deserve it..."
                                hin"I told you that even if this thing inside of you runs rampant, I won't let it sever our bond..."
                                hin"Save your money for more important things, Okay?"
                                menu hinacanigetahug:
                                    hin"Save your money for more important things, Okay?"
                                    "{color=[obediencecolor]}You are important!{/color}":
                                        bo"But [hin_rel]..."
                                        show shinahug2t_1 with dissolve
                                        call checkObedience(25,"failyourareimportant","Hinata") from _call_checkObedience_18
                                        bo"You are important to me!" with vpunch
                                        call changeObedience("Hinata",1) from _call_changeObedience_108
                                        hin"I... I a-appreciate you saying that, but..."
                                        hin"S-sometimes actions can speak louder than words. Do you understand...?"
                                        call increaselust(5) from _call_increaselust_158
                                        hide shinahug2t_1
                                        show shinahug2t
                                        with dissolve
                                        bo"Of course..."
                                        bot"I just grabbed [hin_rel]'s ass and she..."
                                        bot"She took that surprisingly well!" with vpunch
                                    "You are important...":
                                        bo"But you are important [hin_rel]..."
                                        hin"I appreciate you saying that, but..."
                                        hin"Sometimes actions can speak louder than words..."
                                    "test" if eavesdropcountertutorial >= 1000:
                                        label failyourareimportant:
                                        show shinahug2t_1 with dissolve
                                        bo"You are important to me!" with vpunch
                                        call changeRespect("Hinata", -1) from _call_changeRespect_179
                                        hin"O-okay, I get it! Can you please let go off me...?"
                                        hide shinahug2t_1
                                        show shinahug2t
                                        with dissolve
                                        bo"Of course..."
                                        bot"I just can't resist squeezing that ass..."
                                
                                show blackscreen with dissolve
                                "She pulled away..."
                                show boruto normal at left
                                show shina concerned at right
                                hide blackscreen
                                hide shinahug2t
                                with dissolve
                                call changeRespect("Hinata", 10) from _call_changeRespect_180
                                hint"I am so glad to see he is still mindful of others, and himself..."
                                bo"Thanks for everything [hin_rel]..."
                                hin"I love you [bo_name]. Don't let this thing inside of you get the better of you, alright?"
                                menu firstttimegifttesthinata:
                                    hin"I love you [bo_name]. Don't let this thing inside of you get the better of you, alright?"
                                    "{color=[hatredcolor]}[hin_rel] is so easy to manipulate...{/color}" if hatred >=25:
                                        call checkHatred(25,"firstttimegifttesthinata") from _call_checkHatred_18
                                        show boruto embarassed with dissolve
                                        bo"Heh! You don't have to worry about that. I'll make sure I manage my condition!"
                                        show boruto snob with dissolve
                                        bot"Oh [hin_rel]... All it takes for you to see past my imperfections is one good gesture..."
                                        bot"You are so easy to toy around with!"
                                        call changeHatred(2,"hinamanipulate1stitmegist") from _call_changeHatred_133
                                        bot"Soon enough we'll find out how much you are willing to sacrifice for that bond you cherish so much..."
                                    "I love you too! And I won't...":
                                        show boruto embarassed with dissolve
                                        bo"I love you too [hin_rel], don't worry about me... I'll make sure I manage my condition!"
                                hin"I am happy to hear that!"
                                show shina shy with dissolve
                                hin"Let's get back to what we were doing, shall we?"
                                show boruto normal with dissolve
                                bo"Right..."
                                hide boruto with dissolve
                                jump action_taken
                            else:
                                bo"I have something for you..."
                                show shina shy with dissolve
                                hin"A-again...?" with vpunch
                                hin"I told you to not waste money on me [bo_name]..."
                                show boruto embarassed with dissolve
                                bo"What if I want to 'waste' money on you... Heh-eh!"
                                call useItem(flowers,1) from _call_useItem_9
                                bo"I got you this!"
                                if hinata_respect >= 0:
                                    show shina concerned with dissolve
                                    hin"It's... beautiful. Thank you..."
                                    call changeRespect("Hinata", 3) from _call_changeRespect_181
                                    hin"But this is the last time, okay?"
                                else:
                                    show shina concerned with dissolve
                                    call changeRespect("Hinata", 4) from _call_changeRespect_182
                                    hin"[bo_name]... T-thank you, I suppose..."
                                    show shina at smallshake
                                    hin"I would appreciate if you were more mindful of your actions instead of showering me with gifts..."
                                show shina shy2 with dissolve

                                if hinata_respect >= 0:
                                    hin"I don't want you to waste any more money on me, okay?"
                                else:
                                    hin"Some things are more important than others. Do you understand what I am saying, [bo_name]?"
                                show boruto normal with dissolve
                                bo"Sure..."
                                show shina shy with dissolve
                                hin"Good! Let's get back to what we were doing, shall we?"
                                hide boruto with dissolve
                                jump action_taken
                        "Return":
                            jump hinabedroomdaytalk

                "Return":
                    bo"I'll leave you to it then..."
                    $ boruto_location ="nowhere"
                    hide boruto with dissolve
                    hide shina with dissolve
                    scene bg day with dissolve:
                        zoom 0.70
                        
                    call showUIhouse from _call_showUIhouse_37
                    $ ui.interact()

                
            call showUIhouse from _call_showUIhouse_39
            $ ui.interact()
        "Talk to [him_name]" if him_location == "hinatabedroom":
            bo"a"
            call showUIhouse from _call_showUIhouse_40
            $ ui.interact()
        "Return":
            call showUIhouse from _call_showUIhouse_41
            $ ui.interact()








screen hinata_bedroom_day1:
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "hinatabedroom day_idle"  #image in ui / needs to be seperate for correct images to be displayed when hovering
        hover "hinatabedroom day_hover"
        focus_mask "hinatabedroom day_mask"
        mouse "handsmall"
        hovered [Show("displayTextScreen", displayText = "Interact with [hin_name]")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("displayTextScreen"), Jump("hinatabedroomntalkmenu")]

