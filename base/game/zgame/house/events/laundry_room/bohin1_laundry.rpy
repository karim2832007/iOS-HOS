
screen gropetest():


    #ass
    imagebutton:
            mouse "hand"
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            auto "characters/hina/laundry/lvl1/Byoga/sweater/grptestass1_%s.png" xalign 0.455 yalign 1.0
            hovered Show("displayTextScreen", displayText = "Grope Ass")
            unhovered Hide("displayTextScreen")
            action [Hide("displayTextScreen"), Hide('gropetest'), Jump("laundry_gropeass")]
    #tits
    imagebutton:
            mouse "hand"
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            auto "characters/hina/laundry/lvl1/Byoga/sweater/grptesttits1_%s.png" xalign 0.468 yalign 0.16
            hovered Show("displayTextScreen", displayText = "Grope Tits")
            unhovered Hide("displayTextScreen")
            action [Hide("displayTextScreen"), Hide('gropetest'),Jump("laundry_groptits")]
    #return
    imagebutton:
        
        xalign 0.95 yalign 0.05
        auto "images/ui/return_button_%s.png"
        hovered Show("displayTextScreen", displayText = "Return")
        unhovered [Hide("displayTextScreen"), Hide("marketshop3")]
        action [Hide("displayTextScreen"), Hide('gropetest'), Jump("laundryreturn")]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"

label laundry_gropeass:
    "lule"
    show screen gropetest
    $ ui.interact()

label laundry_groptits:
    "lule"
    show screen gropetest
    $ ui.interact()




        






#LAUNDRY room events
label bohin1_1:
    show laundry quest2 with dissolve
    if hin_vulnerable_bohin1 == True:
        hin"*Sniffles*..."
        bot"Wait, is she... crying?"
        menu bohin1_1_menu_vuln:
            bot"Damn... I am almost tempted to do something stupid."
            "'Thank' her for all she does":
                scene black with vpunch
                bo"Hey [hin_rel]!"
                scene bg laundry day
                show boruto sceeming at right
                show shina surprised4 at shake:
                    xalign 0.5
                with fade
                show shina surprised4:
                    easein 1 xalign 0.1
                "[hin_name] wipes her face while actively trying to avoid facing you..."
                hin"You scared me, [bo_name]! Don't sneak behind me like that!"
                show shina concerned with dissolve
                bot"I don't want [hin_rel] to fall into despair yet... I should probably put on a facade for now."
                show boruto worried with dissolve
                bo"Is this about what happened this morning...? Come on [hin_rel], I wasn't serious. I am sorry, okay?"
                show boruto worried2 with dissolve
                bo"I just wanted to thank you for everything you do for us..."
                bo"I know it must be a heavy burden to shoulder all the responsibility now that [na_rel] is gone..."
                show boruto sceeming with dissolve
                bo"I wanted to let you know that I don't take that for granted."
                call changeRespect("Hinata", 1, "bohin1_1_menu_vuln") from _call_changeRespect_5
                hin"*Sniffles* T-thank you for saying that [bo_name]. You are right, it's hard..."
                hin"But know that I am trying my best. It's just that... sometimes I get stressed trying to process everything that's going on with you."
                hin"And even if your condition stands to be an obstacle between our bond, I'll just have to push through until you get better..."
                hin"You are my [hin_rel_to_bo] [bo_name], no matter what."
                hin"I would do anything for you and [him_name]."
                hin"But... help me out a little bit here, okay?"
                hin"Don't let yourself descend into madness, please!"
                bo"I know [hin_rel]..."
                show boruto sceeming2 with dissolve
                bot"I am afraid it's only going to get worse [hin_rel]! But if I take things slow..."
                bot"Maybe you'll understand that there's other ways to strengthen our 'bond'!"
            "{color=[dominancecolor]}locked{/color}":
                "Complete current quest objective to unlock"
                jump bohin1_1_menu_vuln
                bo"Hey [hin_rel]!"
                "You put your hand around her waist with confidence..."
                call changeDominance(1, "bohin1_1_menu") from _call_changeDominance_2
                #add cg
                if hin_vulnerable_bohin1 == True:
                    hin"*Sniffles*..."
                    "[hin_name] wipes her face while actively trying to avoid facing you..."
                    hin"...[bo_name]?"
                    bo"Is this about what happened this morning...? Come on [hin_rel], I wasn't serious. I am sorry, okay?"
                else:
                    hin"O-oh! [bo_name], W-what's wrong!?"
                    bo"Nothing! Just wanted to thank you for taking care of me..."
                bo"One day, I promise..."
                menu:
                    bo"One day, I promise..."
                    "{color=[obediencecolor]}Grope her ass!{/color}":
                        bo"I'll be the one taking care of you instead!" with vpunch
                        call checkObedience(16, "none", "Hinata") from _call_checkObedience_2
                        if hinata_obedience >= 16:
                            hin"O-okay. W-we'll see about that..."
                        else:
                            hin"H-hey! Your h-hand!?" with vpunch
                            call changeRespect("Hinata", -1, "none") from _call_changeRespect_6
                            bo"Oh, oops! Must have slipped."
                            hin"I don't know about that. Please, give me some time alone for now, will you?"
                    "I will be taking care of you instead":
                        bo"I will be taking care of you instead."
                        bo"For all you do... you deserve at least that much."
                        call changeRespect("Hinata", 1, "laundrydominancemenu") from _call_changeRespect_7
                        hin"We'll see about that. For now, focus on taking care of yourself first! Alright?"
                        bo"You are not wrong..."
                        bo"I am working on it!"
            "{color=[lovecolor]}locked{/color}":
                "Set quest on 'love' path to unlock"
                jump bohin1_1_menu_vuln
            "{color=[hatredcolor]}locked{/color}":
                "Set quest on 'hatred' path to unlock"
                jump bohin1_1_menu_vuln
            
    else:
        menu bohin1_1_menu:
            bot"Damn... I am almost tempted to do something stupid."
            "Thank her for all she does":
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                scene black with vpunch
                bo"Hey [hin_rel]..."
                scene bg laundry day
                show boruto smirk at right
                show shina surprised2 at shake:
                    xalign 0.5 zoom 1.1 ypos -30
                with fade
                show shina surprised:
                    easein 1 xalign 0.2
                hin"You scared me, [bo_name]! Don't sneak behind me like that!"
                show shina shy2 with dissolve
                hin"...Finally got off your bed?"
                bo"Would still be in there if it weren't for you. Heh!"
                bo"I just wanted to say, thank you for everything you do for us."
                show boruto worried with dissolve
                bo"I know it must be hard on you shouldering all the responsibility on your own. Even more so now that [na_rel] is away..."
                show boruto smirk with dissolve
                bo"I wanted to let you know that I don't take that for granted..."
                call changeLove("Hinata", 1, "bohin1_1_menu") from _call_changeLove_4
                show shina worried with dissolve
                hin"[bo_name]... You are my [hin_rel_to_bo], no matter what."
                show shina shy with dissolve
                hin"And even if your condition stands to be an obstacle between our bond, we'll just have to help each other out until you get better, right?"
                show shina smiling with dissolve
                hin"Don't worry about me, I can shoulder this and much more! You know I am strong, don't you?"
                hin"I would do this much and more for you and [him_name]..."
                hin"Just promise me that you'll take care of yourself and that's all I need to keep moving forward!"
                show boruto laughing2 with dissolve 
                bo"Of course [hin_rel]"
            "{color=[dominancecolor]}Locked{/color}":
                "Complete the current quest objective of '[hin_name]'s Hospitality' to unlock."
                jump bohin1_1_menu
                bo"Hey [hin_rel]!"
                "You put your hand around her waist with confidence..."
                call changeDominance(1, "bohin1_1_menu") from _call_changeDominance_3
                #add cg
                if hin_vulnerable_bohin1 == True:
                    hin"*Sniffles*..."
                    "[hin_name] wipes her face while actively trying to avoid facing you..."
                    hin"...[bo_name]?"
                    bo"Is this about what happened this morning...? Come on [hin_rel], I wasn't serious. I am sorry, okay?"
                else:
                    hin"O-oh! [bo_name], W-what's wrong!?"
                    bo"Nothing! Just wanted to thank you for taking care of me..."
                bo"One day, I promise..."
                menu:
                    bo"One day, I promise..."
                    "{color=[obediencecolor]}Grope her ass!{/color}":
                        bo"I'll be the one taking care of you instead!" with vpunch
                        call checkObedience(16, "none", "Hinata") from _call_checkObedience_3
                        if hinata_obedience >= 16:
                            hin"O-okay. W-we'll see about that..."
                        else:
                            hin"H-hey! Your h-hand!?" with vpunch
                            call changeRespect("Hinata", -1, "none") from _call_changeRespect_8
                            bo"Oh, oops! Must have slipped."
                            hin"I don't know about that. Please, give me some time alone for now, will you?"
                    "I will be taking care of you instead":
                        bo"I will be taking care of you instead."
                        bo"For all you do... you deserve at least that much."
                        call changeRespect("Hinata", 1, "laundrydominancemenu") from _call_changeRespect_9
                        hin"We'll see about that. For now, focus on taking care of yourself first! Alright?"
                        bo"You are not wrong..."
                        bo"I am working on it!"
            "{color=[lovecolor]}Locked{/color}":
                "Advance '[hin_name]'s Hospitality' quest to 'love' path to unlock."
                jump bohin1_1_menu
            "{color=[hatredcolor]}Locked{/color}":
                "Advance '[hin_name]'s Hospitality' quest to 'hatred' path to unlock."
                jump bohin1_1_menu

        
    if not quest.is_state("bohin_1", "done"):        
        $ notification("Quest Updated")
        $ quest.check("bohin1_1", "completed")
        $ quest.check("bohin1_2", "in progress")
    jump action_taken
    
label bohin1_2: #repeatable dialogue similar to above until fap to hin when wake up + give soiled briefs + force to not wear sweater if hatred
    if bohin3_surpriselaundry == True and (boruto_clothes=="Underwear" or boruto_clothes=="Naked") :
        scene black with dissolve
        $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.7)
        bot"This'll be interesting!"
        show laundry quest2_h with dissolve
    else:
        show laundry quest2 with dissolve
    if hin_vulnerable_bohin1 == False:
        bot"Here she is again, blissfully unaware of the effect she has on me..."
        call increaselust(5) from _call_increaselust_8
        bot"I want to feel her body so bad..."
        menu bohin1_2_menulove:
            bot"I want to feel her body so bad..."
            "Thank her again" if bohin3_surpriselaundry == False:
                scene black with vpunch
                bo"Hey [hin_rel]..."
                scene bg laundry day
                show boruto smirk at right
                show shina surprised2 at shake:
                    xalign 0.5
                with fade
                show shina surprised:
                    easein 1 xalign 0.2
                hin"My lord! *Sigh*..." with vpunch
                
                hin"Hey [bo_name]. Finally off your bed?"
                bo"Yep. Just wanted to thank the best [hin_rel] in the world!"
                bo"What would I ever do without you!"
                call changeLove("Hinata", 1, "bohin1_2_menulove") from _call_changeLove_5
                hin"Come on, [bo_name]! You know I am not good when you say things like that."
                hin"Besides, It's no big deal! I'd do anything for you and [him_name]..."
                hin"Now do me a favour and stop sneaking behind me, will you?"

            "{color=[dominancecolor]}Hug from behind{/color}" if bohin3_surpriselaundry == False:

                show laundry quest3_1 with fade
                "You put your hand around her waist with confidence..."
                scene bg laundry day
                show shina surprised2 at left and shake
                show boruto smirk behind shina:
                    xalign 0.3
                with fade
                show shinapretend1:
                    zoom 0.5 xalign 0.9 yalign 0.1
                    
                show cutoutborder_white:
                    zoom 0.75 pos (559, -109)
                with dissolve
                bo"Hey [hin_rel]!"
                call changeDominance(1, "bohin1_2_menulove") from _call_changeDominance_4
                show shina concerned with dissolve
                hin"O-oh! [bo_name_stutter], are y-you alright?"
                show boruto smirk2 with dissolve
                bo"With you around? Always!"
                bo"Thanks for being the best, [hin_rel]."
                show boruto snob with dissolve
                bo"One day, I promise..."
                menu laundrydominancemenu2love:
                    bo"One day, I promise..."
                    "{color=[obediencecolor]}Lower your hand{/color}":
                        show shinapretend1_1 with dissolve:
                            zoom 0.5 xalign 0.9 yalign 0.1
                        show shina surprised2 with dissolve
                        bo"I'll be the one taking care of you instead!" with vpunch
                        call checkObedience(12, "none", "Hinata") from _call_checkObedience_4
                        if hinata_obedience >= 12:
                            default laundrydominancemenu2love_grope = 0
                            $ dialogue = renpy.call("get_dialogue", laundrydominancemenu2love_grope,
                                f"O-okay. W-we'll see about that...",
                                f"{bo_name_stutter}? We t-talked about this last time...")
                            $ renpy.say(hin, dialogue)
                            call changeObedience("Hinata",1,"laundrydominancemenu2love", 2) from _call_changeObedience_13
                            show shina concerned with dissolve
                            $ dialogue = renpy.call("get_dialogue", laundrydominancemenu2love_grope,
                                f"B-but your hand {bo_name_stutter}! You can't be doing that with me...",
                                f"P-please...")
                            $ renpy.say(hin, dialogue)
                            show shinapretend1 zorder 100 with dissolve:
                                zoom 0.5 xalign 0.9 yalign 0.1
                            bo"It's not a big deal [hin_rel]! I am just showing you my appreciation."
                            if laundrydominancemenu2love_grope >=1:
                                menu laundrygrope1:
                                    bo"It's not a big deal [hin_rel]! I am just showing you my appreciation."
                                    "{color=[obediencecolor]}Grope her ass!{/color}":
                                        call checkObedience(14,"laundrygrope1","Hinata") from _call_checkObedience_5
                                        bo"Now if I did something like this..."
                                        show shinapretend1_1 zorder 101 with dissolve:
                                            zoom 0.5 xalign 0.9 yalign 0.1
                                        show hinagropemoneyproblems2 zorder 102 with dissolve:
                                            zoom 0.5 xalign 0.9 yalign 0.1
                                        $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                        call changeObedience("Hinata",1,"laundrydominancemenu2love_grope",1) from _call_changeObedience_14
                                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                        show shina surprised4 with dissolve
                                        show shina at smallshake
                                        hin"*Gasps*"
                                        hin"[bo_name_stutter]! That's too far!"
                                        bo"I am just joking around of course [hin_rel]!"
                                        bo"...It's like a soft pillow, do you think I could sleep on it some time?"
                                        bo"I think mine sucks!"
                                        hide hinagropemoneyproblems2
                                        show shinapretend4 zorder 103:
                                            zoom 0.5 xalign 0.9 yalign 0.1
                                        with dissolve
                                        call changeRespect("Hinata",-1) from _call_changeRespect_10
                                        show shina shy2 with dissolve
                                        hin"W-what the heck are you talking about [bo_name]! That's enough!"
                     
                                        scene bg laundry day
                                        show boruto smirk:
                                            xalign 0.5
                                        show shina surprised4 at shake:
                                            xalign 0.15
                                        with fade
                                        show shina surprised3:
                                            easein 1 xalign 0.05
                                        show boruto:
                                            easein 1 xalign 0.8
                                        show shina shy2 with dissolve
                                        hin"You have to stop doing that [bo_name]. Even if you think it's a joke!"
                                        bo"But it feels so nice..."
                                        show shina angry3 with dissolve 
                                        hin"That's not the point you idiot!" with vpunch
                                        show shina assertive with dissolve


                                        

                                    "Don't":
                                        bot"That'd be too much for her I think..."
                            hin"In any case, can I have the room now p-please?"
                            show boruto smirk with dissolve
                            bo"Sure thing..."     
                            $ laundrydominancemenu2love_grope+= 1
                            
                        else:
                            default laundrydominancemenu2love_gropefail = 0
                            hin"H-hey! Your h-hand!?" with vpunch
                            show shina concerned with dissolve
                            call changeRespect("Hinata", -1, "none") from _call_changeRespect_11
                            show boruto surprised2 with dissolve
                            show shinapretend1 zorder 100 with dissolve:
                                zoom 0.5 xalign 0.9 yalign 0.1
                            bo"Oh, oops! Must have slipped."
                            hin"[bo_name], please... Don't do that!"
                            hin"Now give me some time alone please, will you?"
                    "I will be taking care of you instead":
                        bo"I will be taking care of you instead."
                        bo"For all you do... you deserve at least that much."
                        call changeRespect("Hinata", 1, "laundrydominancemenu2love") from _call_changeRespect_12
                        hin"We'll see about that. For now, focus on taking care of yourself first! Alright?"
                        bo"Heh, you are not wrong..."
                        bo"I am working on it!"

            "{color=[lovecolor]}'About what you saw me doing...'{/color}" if bohin1_lovepath == True and bohin1_lovepath_repeat_cum <1:
                "Have [hin_name] watch you jerk off first."
                jump bohin1_2_menulove
            "{color=[lovecolor]}'About what you saw me doing...'{/color}" if bohin1_lovepath == True and bohin1_lovepath_repeat_cum >=1 and laundrytalkcheck == True and bohin1_3_laundrytalked == 0:
                label laundrytalk_onetime:
                $ bohin1_3_laundrytalked = 1
                bo"About what you saw me doing-"
                scene black with vpunch
                bo"Are you alright?"
                scene bg laundry day
                show boruto surprised2 at right
                show shina surprised2 at shake:
                    xalign 0.5
                with fade
                show shina surprised2:
                    easein 1 xalign 0.2
                hin"G-good grief!" with vpunch
                show shina serious with dissolve:
                    zoom 1.1 ypos -40
                hin"You scared me, [bo_name_stutter]!"
                show boruto worried with dissolve
                bo"I didn't mean to..."
                show boruto worried2
                show shina assertive
                with dissolve
                bo"Just like I didn't mean to scare you when you saw me doing... that, in my bedroom."
                show shina shy2 with dissolve
                hin"C-can we not talk about that? It's quite awkward for the b-both of us I imagine..."
                hin"I'll consult Lady Tsunade and find a solution, okay?"
                bo"I am afraid that might not be as helpful as you think..."
                hin"...And w-why is that the case?"
                bo"[hin_rel]... You don't have to talk, you only have to listen."
                bo"I know I shouldn't have done what I did while you were there but..."
                bo"The fact that you were there could be the only reason why it was easy for me to... handle my condition."
                bo"I am not d-doing that because I want to, but because I need to..."
                bo"You saw how I can get when my curse is left to fester for too long. I don't want that to happen again..."
                bo"Not when It could hurt you, or [him_name] for that matter."
                bo"So... Is it really that big of a deal if I use some stimuli to control my condition?"
                hin"..."
                show shina concerned with dissolve
                hin"W-what do you want me to say, [bo_name]..."
                hin"That I'll act as your medication? I..."
                show shina shy with dissolve
                hin"I can't do that! There needs to be another way..."
                show shina with dissolve:
                    xzoom -1
                show shina:
                    easein 2 xpos -700
                call changeLove("Hinata", 1) from _call_changeLove_31
                hin"But until we figure that out... I'll t-try to be understanding, okay?"
                hin"T-thanks for looking out for us..."
                bot"She'll... try?"
                show boruto surprised2 with dissolve
                bot"I wonder how she'll act the next time she catches me jerking off to her..."
                jump action_taken

            "{color=[lovecolor]}'T-thanks for that...'{/color}" if bohin1_lovepath == True and bohin1_3_laundrytalked >= 1 and laundrycumcheck == True:
                $ laundrycumcheck = False
                bot"She seems to be doing better after we had that talk the other day..."
                bot"I am curious how she'd react to..."
                if bohin1_3_laundrytalked == 2:
                    menu:
                        bot"I am curious how she'd react to..."
                        "{color=[obediencecolor]}Push your luck...{/color}":
                            bot"I want to find out how far [hin_rel]'s willing to let me go..."
                            show laundry quest3_1 with dissolve
                            bo"Hey [hin_rel]..."
                            $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                            call changeObedience("Hinata",1,"laundrydominancemenu2love_grope_obe",1) from _call_changeObedience_56
                            show laundry quest3_2 with dissolve
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                            show laundry quest3_3 with dissolve
                            bo"I really appreciate your help back there..."
                            "You squeezed her inner upper thigh, your fingers were an inch away from brushing against her vulva..."
                            scene black with vpunch
                            hin"[bo_name_stutter]! N-no!"
                            scene bg laundry day
                            show boruto surprised2 at right
                            show shina assertive at shake:
                                xalign 0.5 zoom 1.1 ypos -30
                            with fade
                            show shina:
                                easein 0.5 xalign 0.2
                            call changeRespect("Hinata",-1) from _call_changeRespect_92
                            hin"If you think what's happening is an invitation for you to do whatever you please, think again!"
                            show shina with dissolve:
                                xzoom -1
                            hin"You push your luck any further and I swear, I'll lock you in the infirmary until you get better!"
                            show shina:
                                easein 1 xpos -700
                            hin"*Scoffs*"
                            bot"Oops! It would seems she's not quite there yet..."
                            bot"I'll have to slow things down a bit if I want to get anywhere with [hin_rel]..."
                            jump action_taken



                        "Don't":
                            pass
                        
                show laundry quest4 with dissolve
                bo"Something like this..." with vpunch
                "You inconspicuously place your hand on [hin_name]'s upper thigh..."
                hin"[bo_name_stutter]?"
                scene bg laundry day
                show boruto surprised2 at right
                show shina surprised2 at shake:
                    xalign 0.5
                with fade
                show shina surprised2:
                    easein 1 xalign 0.2
                bo"Thanks for... doing that [hin_rel]. It really helps me out you know..."
                show shina shy2 with dissolve:
                    zoom 1.1 ypos -40
                hin"Can we n-not talk about that?"
                bo"If you say so..."
                hin"Yes p-please. Now give me some time alone if you don't mind..."
                if not quest.is_state("bohin_1", "done"):
                    $ notification("Quest Completed")
                    $ quest.check("bohin_1", "done") #marks left quest as complete (make sure any references now check if quest is completed to avoid errors)
                    $ quest.remove("[hin_name]'s hospitality") # removes the quest from the right page (use when completed)
                    $ quest_hin.check("hin1L_4", "done") #mark hin love log complete
                    $ renpy.block_rollback() # have to disable rollback to prevent errors when using quest.remove
                hin"I... have a lot to do, and a lot more to think about..."
                bo"S-sure..."
                hide boruto with dissolve
                bot"She didn't even mention me touching her like that... Is she slowly becoming more accepting of the situation?"
                hide shina with dissolve
                $ bohin1_3_laundrytalked = 2
                jump action_taken
            "{color=[dominancecolor]}Locked{/color}" if bohin1_hatredpath == True and bohin3_surpriselaundry == False:
                "Coerce [hin_name] into watching you jerk off and then take off your clothes to unlock this option."
                jump bohin1_2_menulove


    
    else:
        bot"Fucking hell, she has no idea what effect she has on me..."
        hin"*Sniffles*..."
        bot"Aww is she crying again?"
        call increaselust(5) from _call_increaselust_9
        bot"I want to grab that ass so bad..."
        menu bohin1_2_menuhatred:
            bot"I want to grab that ass so bad..."
            "[hin_rel], are you alright?" if boruto_clothes=="Casual":
                bo"Hey [hin_rel]..."
                scene black with vpunch
                bo"Are you alright?"
                scene bg laundry day
                show boruto sceeming at right
                show shina surprised5 at shake:
                    xalign 0.5
                with fade
                show shina surprised5:
                    easein 1 xalign 0.2
                hin"*Sniffles*..."
                "[hin_name] tries to hide her emotional outburst before she turns to address you..."
                bot"Was it really that bad?"
                show shina concerned with dissolve
                hin"W-what do you need, [bo_name]?"
                menu:
                    "Apologize":
                        show boruto worried2 with dissolve
                        bo"I am sorry [hin_rel], I did not mean to hurt you."
                        bo"I might be a bit spontatenous lately but I am not an asshole, I can see you are trying to help."
                        bo"I appreciate all you do, it's just sometimes... my condition messes with my brain."
                        call changeRespect("Hinata",1) from _call_changeRespect_13
                        hin"I know... I just need some time."
                        show boruto smirk with dissolve
                        bo"Thanks, [hin_rel] you are the best."
                        hin"It's alright [bo_name]... Can you give me some space now please?"
                        hin"I have to get back to work."
                        bo"Sure..."
                        hide boruto with dissolve
                    "{color=[hatredcolor]}Berate her{/color}":
                        show boruto angry with dissolve
                        bo"Are you seriously emotional over what happened this morning?"
                        bo"That was nothing [hin_rel]! I thought you were stronger than this..."
                        show shina surprised5 with dissolve
                        hin"*Sniffles* [bo_name_stutter]... Are you serious?"
                        # hug waist cg
                        call changeHatred(1,"bohin1_2_menuhatred",2) from _call_changeHatred_3
                        show boruto furious with dissolve
                        show boruto at smallshake
                        bo"Damn it [hin_rel] get your shit together! I am the one suffering here..."
                        show boruto pissy with dissolve
                        bo"Do you see me crying over petty shit?"
                        show boruto angry with dissolve
                        bo"I am doing my best, okay? You should try that too!" with vpunch
                        hide boruto with dissolve
                        hint"What's wrong with [bo_name]!"
                        hin"*Sniffles*"
                        show shina concerned with dissolve
                        hint"I... I should consult Tsunade again, this cannot be how [bo_name] is."
                        if tsunadeintroduction == False:
                            $ tsunadeintroduction = True
                            $ notification ("Infirmary unlocked")
                            "You can now visit the Infirmary during mornings or evenings using the map."


            "{color=[dominancecolor]}Hug from behind{/color}" if boruto_clothes=="Casual":
                show laundry quest3_1 with fade
                "You put your hand around her waist with confidence..."
                scene bg laundry day
                show shina surprised2 at left and shake
                show boruto sceeming behind shina:
                    xalign 0.3
                with fade
                show shinapretend1:
                    zoom 0.5 xalign 0.9 yalign 0.1
                    
                show cutoutborder_white:
                    zoom 0.75 pos (559, -109)
                with dissolve
                bo"Hey [hin_rel]!"
                show shina concerned with dissolve
                call changeDominance(1, "bohin1_2_menuhatred",2) from _call_changeDominance_5
                hin"*Sniffles*..."
                "[hin_name] wipes her face while actively trying to avoid facing you..."
                bo"Come on... [hin_rel], It was nothing serious!"
                menu randomassmenuidontknow:
                    "Apologize":
                        bo"I am sorry [hin_rel], I did not mean to hurt you."
                        bo"I appreciate all you do, it's just sometimes... my condition messes with my brain."
                        call changeRespect("Hinata",1,"none") from _call_changeRespect_14
                        hin"I know... I just need some time."
                        bo"One day, I promise..."
                        menu laundrydominancemenu2hatred:
                            bo"One day, I promise..."
                            "{color=[obediencecolor]}Lower your hand{/color}":
                                show shinapretend1_1 with dissolve:
                                    zoom 0.5 xalign 0.9 yalign 0.1
                                show shina surprised2 with dissolve
                                bo"I'll be the one taking care of you instead!" with vpunch
                                call checkObedience(12, "none", "Hinata") from _call_checkObedience_6
                                if hinata_obedience >= 12:
                                    default laundrydominancemenu2love_grope_hate = 0
                                    $ dialogue = renpy.call("get_dialogue", laundrydominancemenu2love_grope_hate,
                                        f"O-okay. W-we'll see about that...",
                                        f"{bo_name_stutter}? We t-talked about this last time...")
                                    $ renpy.say(hin, dialogue)
                                    call changeObedience("Hinata",1,"laundrydominancemenu2love", 2) from _call_changeObedience_15
                                    show shina concerned with dissolve
                                    $ dialogue = renpy.call("get_dialogue", laundrydominancemenu2love_grope_hate,
                                        f"B-but your hand {bo_name_stutter}! You can't be doing that with me...",
                                        f"P-please...")
                                    $ renpy.say(hin, dialogue)
                                    show shinapretend1 zorder 100 with dissolve:
                                        zoom 0.5 xalign 0.9 yalign 0.1
                                    bo"It's not a big deal [hin_rel]! I am just showing you my appreciation."
                                    if laundrydominancemenu2love_grope_hate >=1:
                                        menu laundrygrope1hatred:
                                            bo"It's not a big deal [hin_rel]! I am just showing you my appreciation."
                                            "{color=[obediencecolor]}Grope her ass!{/color}":
                                                call checkObedience(14,"laundrygrope1hatred","Hinata") from _call_checkObedience_7
                                                bo"Now if I did something like this..."
                                                show shinapretend1_1 zorder 101 with dissolve:
                                                    zoom 0.5 xalign 0.9 yalign 0.1
                                                show hinagropemoneyproblems2 zorder 102 with dissolve:
                                                    zoom 0.5 xalign 0.9 yalign 0.1
                                                $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                                call changeObedience("Hinata",1,"laundrydominancemenu2love_grope_hate",1) from _call_changeObedience_16
                                                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                                show shina surprised4 with dissolve
                                                show shina at smallshake
                                                hin"*Gasps*"
                                                hin"[bo_name_stutter]! That's too far!"
                                                bo"I am just joking around of course [hin_rel]!"
                                                bo"...It's like a soft pillow, do you think I could sleep on it some time?"
                                                bo"I think mine sucks!"
                                                hide hinagropemoneyproblems2
                                                show shinapretend4 zorder 103:
                                                    zoom 0.5 xalign 0.9 yalign 0.1
                                                with dissolve
                                                call changeRespect("Hinata",-1) from _call_changeRespect_15
                                                show shina shy2 with dissolve
                                                hin"W-what the heck are you talking about [bo_name]! That's enough!"
                            
                                                scene bg laundry day
                                                show boruto smirk:
                                                    xalign 0.5
                                                show shina surprised4 at shake:
                                                    xalign 0.15
                                                with fade
                                                show shina surprised3:
                                                    easein 1 xalign 0.05
                                                show boruto:
                                                    easein 1 xalign 0.8
                                                show shina shy2 with dissolve
                                                hin"You have to stop doing that [bo_name]. Even if you think it's a joke!"
                                                bo"But it feels so nice..."
                                                show shina angry3 with dissolve 
                                                hin"That's not the point you idiot!" with vpunch
                                                show shina assertive with dissolve


                                            "Don't":
                                                bot"That'd be too much for her I think..."
                                    hin"In any case, can I have the room now p-please?"
                                    show boruto sceeming with dissolve
                                    bo"Sure thing..."     
                                    $ laundrydominancemenu2love_grope_hate+= 1
                                    
                                else:
                                    hin"H-hey! Your h-hand!?" with vpunch
                                    show shina concerned with dissolve
                                    call changeRespect("Hinata", -1, "none") from _call_changeRespect_16
                                    show boruto sceeming2 with dissolve
                                    show shinapretend1 zorder 100 with dissolve:
                                        zoom 0.5 xalign 0.9 yalign 0.1
                                    bo"Oh, oops! Must have slipped."
                                    hin"[bo_name], please... Don't do that!"
                                    hin"Now give me some time alone please, will you?"
                            "I will be taking care of you instead":
                                bo"I will be taking care of you instead."
                                bo"For all you do... you deserve at least that much."
                                call changeRespect("Hinata", 1, "laundrydominancemenu2love") from _call_changeRespect_17
                                hin"We'll see about that. For now, focus on taking care of yourself first! Alright?"
                                bo"Heh, you are not wrong..."
                                bo"I am working on it!"

                    "{color=[hatredcolor]}Take advantage of her vulnerability{/color}":
                        call checkHatred(20, "randomassmenuidontknow") from _call_checkHatred_3
                        bot"Now is my chance!"
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        
                        show shinapretend2 with dissolve:
                            zoom 0.5 xalign 0.9 yalign 0.1
                        show shina surprised2 at shake
                        hin"A-ah!"
    
                        
                        show cutoutborder_white:
                            zoom 0.75 pos (559, -109)
                        show shina surprised4 with dissolve and vpunch
                        show hinagropemoneyproblems2:
                            zoom 0.5 xalign 0.9 yalign 0.1
                        $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                        bo"I didn't mean to hurt... I was just a bit emotional because of my condition"
                        hin"*Sniffles*"
                        bo"You know how I am... Tsunade told us that much."
                        show shina surprised5 with dissolve
                        hin"*Sniffles* P-please... stop doing that!"
                        show shinapretend1 zorder 100 with dissolve
                        bo"Oh! I am sorry... My hand must have slipped."
                        call changeHatred(1, "vulnr123", 1) from _call_changeHatred_4
                        bot"Fuck me! [hin_rel]'s ass feels amazing to squeeze..."
                        bo"I'll get better [hin_rel] trust me. I don't want to be seeing you like this."
                        show shina concerned with dissolve
                        hin"O-okay... I just need some time alone if you don't mind."
                        bo"Sure..."
                        scene black with dissolve

  





            "{color=[lovecolor]}'About what you saw me doing...'{/color}" if bohin1_lovepath == True and laundrytalkcheck == False:
                "Have [hin_name] watch you jerk off to unlock this option."
                jump bohin1_2_menulove
            "{color=[lovecolor]}'About what you saw me doing...'{/color}" if bohin1_lovepath == True and laundrytalkcheck == True and bohin1_3_laundrytalked == 0:
                $ bohin1_3_laundrytalked = 1
                jump laundrytalk_onetime

            "{color=[dominancecolor]}'[hin_rel]! I need a pair of-'{/color}" if bohin1_hatredpath == True and bohin3_surpriselaundry == True and (boruto_clothes=="Naked" or boruto_clothes=="Underwear"):
                default ineedapair = 0
                if ineedapair == 1:
                    jump ineedapairrepeat
                bo"[hin_rel]! I need a pair of-" with vpunch
                show laundry quest2_hh with dissolve
                hin"[bo_name]! Will you stop sneaking on m-!?"
                show laundry quest2_hhh with dissolve
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                pause 0.5
                show laundry quest2_h1 with dissolve 
                hin"*Gasps*" with vpunch
                show laundryquest_boner_cutout:
                    zoom 0.5 xalign 1.0 yalign 0.5
                show laundry quest2_h2:
                    zoom 1.2 xalign 0.5 yalign 0.1
                with dissolve
                hin"[bo_name_stutter]!!?" with vpunch
                "Having realized you stood behind her with your still, half-erect cock dripping with cum..."
                
                scene laundry quest2_h0 with dissolve:
                    xalign 0.5 yalign 1.0
                pause 0.5
                show laundry quest2_h0:
                    easein 3 yalign 0.1
                "[hin_name] could only stare, paralyzed in disbelief. What little she could speak, only came out in a slurred mess of a speech..."
                hin"W-w-w-why a-are you n-naked w-with your t-t-thing l-looking like t-that!?" with vpunch
                menu:
                    hin"W-w-w-why a-are you n-naked w-with your t-t-thing l-looking like t-that!?"
                    "{color=[dominancecolor]}Because I want to be!{/color}":
                        scene bg laundry day
                        show boruto naked cum at left:
                            zoom 0.35
                        show shina surprised3 at right
                        with dissolve
                        call changeDominance(1) from _call_changeDominance
                        bo"Why else? Because I want to be! I am in my house, am I not?"
                        

                    "{color=[obediencecolor]}What do you mean, you've seen what happened...{/color}":
                        scene bg laundry day
                        show boruto naked cum at left:
                            zoom 0.35
                        show shina surprised3 at right
                        with dissolve
                        bo"You've seen what happened [hin_rel], I soiled my clothes..."
                        hin"T-then put s-something else on for goodness' sake!"
                        hin"D-don't just walk around naked around the house!" with vpunch
                        call changeObedience("Hinata", 1) from _call_changeObedience_57
                        hin"Especially w-when your... t-thing is like that!"
                        bo"Well, that's why I am here. I am going to need a new pair of briefs to wear, aren't I?"
                show boruto:
                    easein 1 xalign 0.3
                bo"Here... take this!"
                show shina at smallshake
                hin"W-what!?" with vpunch
                show shina:
                    easein 0.5 xalign 1.1
                hin"P-please just put something on right now!"
                show boruto:
                    easein 1 xalign 0.5
                show shina:
                    easein 1 xalign 1.2
                
                bo"I will..."
                show boruto:
                    easein 1 xalign 0.8
                show shina:
                    easein 1 xalign 1.5
                bo"As soon as you take this soiled pair and hand me a new one!" with vpunch
                show shina:
                    easein 1 xalign 2.0
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                hin"*Gasps!*"
                "[hin_name] run outside the room in shock and shouted from afar..."
                hin"J-just pick a clean one from the basket! For goodness's sake [bo_name_stutter]!" with vpunch
                default tsunadeintroduction = False
                
                hin"I am having you see Lady Tsunade as soon as possible! This is highly abnormal behavior and I won't have any more of it!" with vpunch
                if tsunadeintroduction == False:
                    $ tsunadeintroduction = True
                    $ notification ("Infirmary unlocked")
                    "You can now visit the Infirmary during mornings or evenings using the map."
                bo"Sure, sure..."
                hin"And leave your soiled briefs somewhere safe! Do not mix them with the rest of our clothes!" with vpunch
                bot"Heh! I don't think Lady Tsunade will be of any help [hin_rel]..."
                bot"Well, she might be... but not for the kind of 'help' you are expecting!"
                hide boruto with dissolve
                $ ineedapair = 1
                jump action_taken
                
            "{color=[hatredcolor]}Why shouldn't I?!{/color}" if bohin1_hatredpath == True and ineedapair >= 1 and bohin3_surpriselaundry == True and (boruto_clothes=="Naked" or boruto_clothes=="Underwear"):
                show laundry quest2_hgrab with dissolve
                $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                bo"Hey [hin_rel]!"
                show laundry quest2_hgrab1 with dissolve
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                show laundry quest2_hgrab2 with dissolve
                scene bg laundry day
                show boruto naked cum at left:
                    zoom 0.35
                show shina surprised3:
                    xalign 0.35
                with dissolve
                show shina at smallshake
                show shina:
                    easein 0.5 xalign 0.6
                hin"*Gasps* W-what the heck is wrong with you!" with vpunch
                show shina:
                    easein 1 xalign 2.0
                hin"AND PLEASE, PUT SOME CLOTHES ON!" with vpunch
                bot"Shit, I scared her off..."
                call changeRespect("Hinata",-1) from _call_changeRespect_93
                hin"Get a grip [bo_name_stutter]!" with vpunch
                hin"I am having a talk with Lady Tsunade, you are way out of line!" with vpunch
                if tsunadeintroduction == False:
                    $ tsunadeintroduction = True
                    $ notification ("Infirmary unlocked")
                    "You can now visit the Infirmary during mornings or evenings using the map."
                if not quest.is_state("bohin_1", "done"):
                    $ notification("Quest Completed")
                    $ quest.check("bohin_1", "done") #marks left quest as complete (make sure any references now check if quest is completed to avoid errors)
                    $ quest.remove("[hin_name]'s hospitality") # removes the quest from the right page (use when completed)
                    $ quest_hin.check("hin1H_4", "done") #mark fantasize hatred in hima's log complete
                    $ renpy.block_rollback() # have to disable rollback to prevent errors when using quest.remove

                bot"As if that will make a difference..."
                bot"No matter..."
                call changeHatred(1) from _call_changeHatred_78
                bot"If it's you I want [hin_rel], then it's you I shall have!"
                jump action_taken

                label ineedapairrepeat:
                bo"[hin_rel]! I need a pair of-" with vpunch
                show laundry quest2_hh with dissolve
                hin"[bo_name]! How many times do I hav-!?"
                show laundry quest2_hhh with dissolve
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                pause 0.5
                show laundry quest2_h1 with dissolve 
                hin"*Gasps*" with vpunch
                show laundryquest_boner_cutout:
                    zoom 0.5 xalign 1.0 yalign 0.5
                show laundry quest2_h2:
                    zoom 1.2 xalign 0.5 yalign 0.1
                with dissolve
                hin"Again!? [bo_name_stutter]?" with vpunch
                "[hin_name] stared for a second before she gathered herself up to scold you..."
                
                scene laundry quest2_h0 with dissolve:
                    xalign 0.5 yalign 1.0
                pause 0.5
                show laundry quest2_h0:
                    easein 3 yalign 0.1
                hin"We've been through this, [bo_name_stutter] please!" with vpunch
                
                scene bg laundry day
                show boruto naked cum at left:
                    zoom 0.35
                show shina surprised3 at right
                with dissolve
                bo"Well, you keep waking me up so... I am going to keep needing new briefs I am afraid!"
                show shina at smallshake
                hin"W-what are you on about!" with vpunch
                show shina:
                    easein 0.5 xalign 1.1
                hin"P-please just... stop being indecent around the house!"
                show boruto:
                    easein 1 xalign 0.5
                show shina:
                    easein 1 xalign 1.2
                
                bo"I will..."
                show boruto:
                    easein 1 xalign 0.8
                show shina:
                    easein 1 xalign 1.5
                bo"As soon as you hand me a new pair!" with vpunch
                show shina:
                    easein 1 xalign 2.0
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                hin"*Gasps!*"
                "[hin_name] run outside the room in shock and let out a few loud disapproving remarks!"
                hin"Goodness gracious!" with vpunch
                call changeRespect("Hinata", -1) from _call_changeRespect_94
                hin"What if [him_name] is around you i-idiot!" with vpunch
                hin"Stop acting weird, please! And cover yourself up!" with vpunch
                jump action_taken  


            

    jump action_taken








label bohin1_3:
    # dev"This is the end of this questline for now. It'll be completed in the next update!"
    # dev"There's still some options you can unlock in the 'Wake up' part of this quest."
    jump bohin1_2
    # if bohin1_lovepath == True:
    #     bot"Here she is again, blissfully unaware of the effect she has on me..."
    #     call increaselust(5)
    #     bot"I want to feel her body so bad..."
    #     menu bohin1_2_menulove: #todo fix dialogue / add cg
    #         bot"I want to feel her body so bad..."
    #         "Thank her again":
    #             bo"Hey [hin_rel]..."
    #             if hin_vulnerable_bohin1 == True:
    #                 hin"*Sniffles*..."
    #                 "[hin_name] wipes her face before she addresses you..."
    #                 bot"Is she crying because of what happened earlier?"
    #                 hin"H-hey [bo_name]..."
    #                 bot"There's no reason to be upset [hin_rel]."
    #                 bot"It was nothing serious..."
    #             else:
    #                 hin"Hey [bo_name]. Finally off your bed?"
    #                 bo"Yep. Just wanted to thank the best [hin_rel] in the world!"
    #                 bo"What would I ever do without you!"
    #                 call changeLove("Hinata", 1, "bohin1_2_menu")
    #                 hin"Come on, [bo_name] you know I am not good when you say things like that."
    #                 hin"Besides, It's no big deal! Anything for my sweet boy"

    #         "{color=[dominancecolor]}Hug from behind{/color}":
    #             bo"Hey [hin_rel]!"
    #             "You put your hand around her waist with confidence..."
    #             call changeDominance(1, "bohin1_2_menu")
    #             #add cg
    #             if hin_vulnerable_bohin1 == True:
    #                 hin"*Sniffles*..."
    #                 "[hin_name] wipes her face while actively trying to avoid facing you..."
    #                 hin"...[bo_name]?"
    #                 bo"I hope you aren't sad [hin_rel], just wanted to thank you for taking care of me"
    #             else:
    #                 hin"O-oh! [bo_name], y-you alright?"
    #                 bo"With you around? Always!"
    #                 bo"Thanks for being the best, [hin_rel]."
    #             bo"One day, I promise..."
    #             menu laundrydominancemenu2love:
    #                 bo"One day, I promise..."
    #                 "{color=[obediencecolor]}Grope her ass!{/color}":
    #                     bo"I'll be the one taking care of you instead!" with vpunch
    #                     call checkObedience(10, "none", "Hinata")
    #                     if hinata_obedience >= 10:
    #                         hin"O-okay. W-we'll see about that..."
    #                     else:
    #                         hin"H-hey! Your h-hand!?" with vpunch
    #                         call changeRespect("Hinata", -1, "none")
    #                         bo"Oh, oops! Must have slipped."
    #                         hin"I don't know about that. Please, give me some alone time for now, will you?"
    #                 "I will be taking care of you instead":
    #                     bo"I will be taking care of you instead."
    #                     bo"For all you do... you deserve at least that much."
    #                     call changeRespect("Hinata", 1, "laundrydominancemenu2love")
    #                     hin"We'll see about that. For now, focus on taking care of yourself first! Alright?"
    #                     bo"Heh, you are not wrong..."
    #                     bo"I am working on it!"

    #         "locked":
    #             bo"add" #give soiled pants
    #             jump bohin1_2_menulove


    # #todo quest2 hatred path
    # elif bohin1_hatredpath == True:
    #     bot"Fucking hell, she has no idea what effect she has on me..."
    #     call increaselust(5)
    #     bot"I want to grab that ass so bad..."
    #     menu bohin1_2_menuhatred: #todo fix dialogue / add cg
    #         bot"I want to grab that ass so bad..."
    #         "'Thank' her again":
    #             bo"Hey [hin_rel]..."
    #             if hin_vulnerable_bohin1 == True:
    #                 hin"*Sniffles*..."
    #                 "[hin_name] tries to hide her emotional burst before she turns to address you..."
    #                 bot"She must be crying because of how I treated her earlier."
    #                 hin"H-hey... W-what do you need?"
    #                 menu:
    #                     "Apologize":
    #                         bo"I am sorry [hin_rel], I did not mean to hurt you."
    #                         bo"I appreciate all you do, it's just sometimes... my condition messes with my brain."
    #                         call changeRespect("Hinata",1,"bohin1_2_menuhatred")
    #                         hin"It's... It's ok. I just need some time..."
    
    #             else:
    #                 hin"H-hey [bo_name]..."
    #                 bo"I just wanted to thank you for all you do..."
    #                 bo"I might be a bit spontatenous lately but I am not an asshole, I can see you are trying to help."
    #                 # hug waist cg
    #                 bo"Thanks, [hin_rel] you are the best."
    #                 call changeObedience("Hinata", 1, "bohin1_2_menuhatred")
    #                 hin"It'- It's alright, [bo_name]... Can you let go of me now please?"
    #                 hin"I have to get back to work..."

    #         "{color=[dominancecolor]}Hug from behind{/color}":
    #             #add cg
    #             bo"Hey [hin_rel]!"
    #             "You put your hand around her waist with confidence..."
    #             call changeDominance(1, "bohin1_2_menuhatred")
    #             if hin_vulnerable_bohin1 == True:
    #                 hin"*Sniffles*..."
    #                 "[hin_name] wipes her face while actively trying to avoid facing you..."
    #                 bo"Come on... [hin_rel], It was nothing!"
    #                 menu:
    #                     "Apologize":
    #                         bo"I am sorry [hin_rel], I did not mean to hurt you."
    #                         bo"I appreciate all you do, it's just sometimes... my condition messes with my brain."
    #                         call changeRespect("Hinata",1,"none")
    #                         hin"It's... It's ok. I just need some time..."

    #                     "{color=[hatredcolor]}Take advantage of her vulnerability{/color}" if hin_vulnerable_bohin1 == True:
    #                         call checkHatred(20, "bohin1_1_menu")
    #                         bot"Now is my chance!"
    #                         #grope cg animation (maybe cutout box)
    #                         "You abruptly move your hand down on her bottom assuming she wouldn't protest it in her current state..."
    #                         bo"I didn't mean to hurt... I was just a bit emotional because of my condition"
    #                         hin"*Sniffles*"
    #                         bo"You know how I am... Tsunade told us that much."
    #                         hin"*Sniffles* P-please... stop doing that!"
    #                         bo"Oh! I am sorry... My hand must have slipped."
    #                         bo"I'll get better [hin_rel] trust me. I don't want to be seeing you like this."
    #                         hin"O-okay... I just need some time alone if you don't mind."
    #                         bo"Sure"
    #             else:
    #                 hin"O-oh! [bo_name], W-what's wrong!?"
    #                 bo"Nothing! Just wanted to thank you for taking care of me..."
    #             bo"One day, I promise..."
    #             menu laundrydominancemenu2hatred:
    #                 bo"One day, I promise..."
    #                 "{color=[obediencecolor]}Touch her ass{/color}": #todo
    #                     bo"I'll be the one taking care of you instead!" with vpunch
    #                     call checkObedience(10, "none", "Hinata")
    #                     if hinata_obedience >= 10:
    #                         call changeObedience("Hinata", 1 , "none")
    #                         hin"O-okay. W-we'll see about that..."
    #                     else:
    #                         hin"H-hey! Your h-hand!?" with vpunch
    #                         call changeRespect("Hinata", -1, "none")
    #                         bo"Oh, oops! Must have slipped."
    #                         hin"I don't know about that. Please, give me some alone time for now, will you?"
    #                 "I will be taking care of you instead":
    #                     bo"I will be taking care of you instead."
    #                     bo"For all you do... you deserve at least that much."
    #                     call changeRespect("Hinata", 1, "laundrydominancemenu2hatred")
    #                     hin"We'll see about that. For now, focus on taking care of yourself first! Alright?"
    #                     bo"Heh, you are not wrong..."
    #                     bo"I am working on it!"
    #         "locked":
    #             bo"add" #give soiled pants / secret objective = enter naked dripping
    #             jump bohin1_2_menuhatred
    jump action_taken

label bohin1_4:
    dev"4"
    #todo quest1
    jump action_taken
 
screen v1_laundry_hinata:
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "laundry quest1_idle"  #image in ui / needs to be seperate for correct images to be displayed when hovering
        hover "laundry quest1_hover"
        focus_mask "laundry quest1_mask"
        mouse "handsmall"
        hovered [Show("displayTextScreen", displayText = "Interact with [hin_name]")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("displayTextScreen"), Hide("v1_laundry_hinata"), Jump("laundryroomactionmenu")]