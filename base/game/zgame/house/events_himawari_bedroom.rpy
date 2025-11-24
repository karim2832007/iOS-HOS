label bedroom_himawari_morning:
    call resetbuttons from _call_resetbuttons_6
    call hideUI from _call_hideUI_13
    if hin_location == "himawaribedroom" and him_location == "himawaribedroom":
        scene himawari_bedroom_1 with dissolve
        call enabletalk from _call_enabletalk_10
    elif hin_location == "himawaribedroom":
        scene himawari_bedroom_1 with dissolve
        call enabletalk from _call_enabletalk_11
    elif him_location == "himawaribedroom":
        if (day_name == "Saturday" or day_name == "Sunday") and day_part == 1:
            show bathroom door with dissolve
            menu:
                bot"Her door is closed..."
                "Open it!":
                    $ renpy.sound.play("/audio/soun_fx/locked_door.opus", channel="sfx2", loop=False, relative_volume = 1)
                    "*Door rattles*"
                    if tryopendoorhimawari == 0:
                        $ tryopendoorhimawari += 1
                        bot"[him_name] sleeps until the noon during weekends. Must be from all the exhaustion from her excessive excercising..."
                    elif tryopendoorhimawari == 1:
                        $ tryopendoorhimawari += 1
                        bot"Maybe I can convince her to keep the door unlocked somehow..."

                "return":
                    pause 0.01
        else:
            scene himawari_bedroom_1 with dissolve
            call enabletalk from _call_enabletalk_12
        
    else:
        scene himawari_bedroom_1 with dissolve
        if day_number >= 1 and him_item1 == False:
            call bohim_1 from _call_bohim_1 #hidden item quest

    call showUIhouse from _call_showUIhouse_24
    $ ui.interact()

label bedroom_himawari_evening:
    call resetbuttons from _call_resetbuttons_7
    call hideUI from _call_hideUI_14
    if hin_location == "himawaribedroom" and him_location == "himawaribedroom":
        scene himawari_bedroom_1 with dissolve
        call enabletalk from _call_enabletalk_13
    elif hin_location == "himawaribedroom":
        scene himawari_bedroom_1 with dissolve
        call enabletalk from _call_enabletalk_14
    elif him_location == "himawaribedroom":
        scene himawari_bedroom_2
        show screen himawari_stretching_talk
        with dissolve
        call enabletalk from _call_enabletalk_15
        call showUIhouse from _call_showUIhouse_23
        $ ui.interact()
        
    else:
        scene himawari_bedroom_1 with dissolve
        if day_number >= 1 and him_item1 == False:
            call bohim_1 from _call_bohim_1_1

    call showUIhouse from _call_showUIhouse_25
    $ ui.interact()

label bedroom_himawari_night:
    call resetbuttons from _call_resetbuttons_8
    call hideUI from _call_hideUI_15
    if hin_location == "himawaribedroom" and him_location == "himawaribedroom":
        scene himawari_bedroom_2 with dissolve
        call enabletalk from _call_enabletalk_16
    elif hin_location == "himawaribedroom":
        scene himawari_bedroom_2 with dissolve
        call enabletalk from _call_enabletalk_17

    
    elif him_location == "himawaribedroom":
        if day_part == 3:
            scene himawari_bedroom_2
            show screen himawari_stretching_talk
            with dissolve
            call enabletalk from _call_enabletalk_18
            call showUIhouse from _call_showUIhouse_26
            $ ui.interact()


        #midnight events
        if day_part == 4:
            show bathroom door with dissolve
            menu:
                bot"Her door is closed..."
                "Open it!":
                    $ renpy.sound.play("/audio/soun_fx/locked_door.opus", channel="sfx2", loop=False, relative_volume = 1)
                    "*Door rattles*"
                    default tryopendoorhimawari = 0
                    if tryopendoorhimawari == 0:
                        $ tryopendoorhimawari += 1
                        bot"What did I expect... [him_name] always locks her door at nights."
                    elif tryopendoorhimawari == 1:
                        $ tryopendoorhimawari += 1
                        bot"This brat..."
                    elif tryopendoorhimawari == 2:
                        bot"I'll have to find a way to convince her to leave the door open. Or I simply break in, heh!"

                "return":
                    pause 0.01
                



        else:
            scene himawari_bedroom_2 with dissolve
            call enabletalk from _call_enabletalk_19
        
    else:
        scene himawari_bedroom_2 with dissolve         

    call showUIhouse from _call_showUIhouse_27
    $ ui.interact()

label himawaribedroomntalkmenu:
    call hideUI from _call_hideUI_16
    menu:
        "..."
        "Talk to [hin_name]" if hin_location == "himawaribedroom":
            "To do"
            call showUIhouse from _call_showUIhouse_28
            $ ui.interact()
        "Talk to [him_name]" if him_location == "himawaribedroom":
            if day_part == 3:
                hide screen himawari_stretching_talk
                show himawari_bedroom_2him
                with dissolve

                if himaintrotutorial2 == False:
                    bo"What the hell are you doing this late into the night..."
                    him"What does it look like I am doing you idiot..."
                    default himastretch_firsttimetalk = False
                    if himastretch_firsttimetalk == True:
                        him"Get the hell out of here, I am not having this conversation again!" with vpunch
                        $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                        scene black with vpunch
                        bot"...Bitch!"
                        dev"Hint: Redeem the 4200 high-score reward from the Ramen Shop and talk with [him_name] in the living room."
                        scene bg day with fade:
                            zoom 0.7
                        call hideButtons from _call_hideButtons_14
                        call showUIhouse from _call_showUIhouse_71
                        $ ui.interact()
                        
                    else:
                        pass
                    scene himawari_bedroom_2
                    with fade
                    show boruto normal at left 
                    show hima smug3 at right:
                        zoom 0.34
                    with dissolve
                    him"Ever heard of stretching?"
                    menu:
                        him"Ever heard of stretching?"
                        "Be condescending":
                            show boruto sceeming with dissolve
                            bo"It's the thing people do to avoid actual work, right?"
                            show boruto sceeming2 with dissolve
                            bo"Consider me thoroughly unstretched you crazy workout-holic pest."
                            show boruto snob with dissolve
                            bo"Now... Do you have time to actually do something productive?"
                            him"Imagine thinking stretching is unproductive..."
                            show hima smug with dissolve
                            call changeRespect("Himawari", -1) from _call_changeRespect_28
                            him"You really are dumb as rocks, aren't you?"
                            him"I am not doing anything with you! Get out of here, loser!" with vpunch
                            bo"Fine, sheesh!"
                        "There are important things we need to talk about...":
                            bo"Come on [him_name], enough with the snide remarks! There's important things we need to discuss..."
                            show hima at smallshake
                            him"I have nothing to talk about with you! Get out of here, loser!" with vpunch
                            bo"Fine, sheesh!"
                    $ himastretch_firsttimetalk = True
                    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    scene black with vpunch
                    bot"...Bitch!"
                    dev"Hint: Redeem the 4200 high-score reward from the Ramen Shop and talk with [him_name] in the living room."
                    scene bg day with fade:
                        zoom 0.7
                    call hideButtons from _call_hideButtons_13
                    call showUIhouse from _call_showUIhouse_70
                    $ ui.interact()
                else:
                    if d_wrestle3_stomach_finishingblow == True:
                        bo"I see you are taking your training even more seriously after getting your ass beat earlier today..."
                        him"D-drop it!"
                        bo"Hehe! Just messing around with ya..."
                        bo"I need to talk to you about something..."
                        him"Just... Give me a sec to wrap up."
                    else:
                        if hin_location == "captured":
                            if day_part == 3: 
                                scene himawari_bedroom_2
                            else:
                                scene himawari_bedroom_1
                            show hima worried2 at right:
                                zoom 0.34
                            show boruto normal at left
                            with dissolve
                            him"Hey, have you seen [hin_rel]?"
                            him"She is not usually away at this time, and she always let's me know in advance if she will be..."
                            bot"It's probably for the best to avoid involving [him_name]. At least not yet..."
                            show boruto embarassed with dissolve
                            bo"N-no idea! She's probably visiting friends or something!"
                            him"Hmm..."
                            show boruto normal with dissolve
                        else:
                            bo"Am I interrupting something here...?"
                            him"What do you want..."
                            bo"I need to talk to you about something..."
                            him"Just... Give me a sec to wrap up."
            else:
                hide screen himawari_stretching_talk
                show himawari_bedroom_2him_day
                with dissolve
                if hin_location == "captured":
                    if day_part == 3: 
                        scene himawari_bedroom_2
                    else:
                        scene himawari_bedroom_1
                    show hima worried2 at right:
                        zoom 0.34
                    show boruto normal at left
                    with dissolve
                    him"Hey, have you seen [hin_rel]?"
                    him"She is not usually away at this time, and she always let's me know in advance if she will be..."
                    bot"It's probably for the best to avoid involving [him_name]. At least not yet..."
                    show boruto embarassed with dissolve
                    bo"N-no idea! She's probably visiting friends or something!"
                    him"Hmm..."
                    show boruto normal with dissolve
                    bo"So... Can we talk?"
                elif d_wrestle3_stomach_finishingblow == True:
                    bo"I see you are taking your training even more seriously after getting your ass beat earlier today..."
                    him"D-drop it!"
                    bo"Hehe! Just messing around with ya!"
                    bo"I need to talk to you about something..."
                    him"Just... Give me a sec to wrap up."
                else:
                    bo"Am I interrupting something here...?"
                    him"What do you want..."
                    bo"I need to talk to you about something..."
                    him"Just... Give me a sec to wrap up."
            if day_part == 3: 
                scene himawari_bedroom_2
            else:
                scene himawari_bedroom_1
            label himastretchingsetupsprites:
            show hima normal at right:
                zoom 0.34
            show boruto normal at left
            show hima smugshy at right
            with dissolve
            $ himastretch_firsttimetalk = True
            him"So...? You wanted something?"
            default himastretchingmenu_talked = False
            menu himastretchingmenu:
                him"So...? You wanted something?"
                "Talk about..." if himastretchingmenu_talked == True:
                    menu:
                        "Talk about..."
                        "Why are you not wearing your new clothes?" if himatalk_newclothes == True:
                            jump labelhimatalk_newclothes
                        "About the modelling thing..." if himatalk_modellingthing == True:
                            jump labelhimatalk_modellingthing
                        "Return":
                            jump himastretchingmenu


                "Why are you not wearing your new clothes?" if himatalk_newclothes == False:
                    label labelhimatalk_newclothes:
                    $ himastretchingmenu_talked = True
                    default himatalk_newclothes = False
                    $ himatalk_newclothes = True
                    show boruto surprised2 with dissolve
                    bo"How come you are not wearing your new clothes..."
                    show boruto snob with dissolve
                    bo"Have I wasted my money on you?"
                    show hima shy with dissolve
                    him"W-what? No..."
                    show hima at smallshake
                    him"I just... I still feel uncomfortable with tight sportswear."
                    call changeRespect("Himawari", 2,"labelhimatalk_newclothes") from _call_changeRespect_154
                    show hima worried2 with dissolve
                    him"I appreciate y-your gesture by the way, but I..."
                    bo"Alright then, I'll cut you a deal..."
                    show hima at smallshake
                    him"A deal...? What kind of deal?"
                    bo"I'll see if I can get that particular sports brand to sponsor a photoshoot for their clothing line..."
                    him"Y-you can do that!?" with vpunch
                    bo"Sure can! I am a big deal, remember? That way, we can make some money for [hin_rel] and all you'd have to do is pose in your new clothes..."
                    bo"That should get you comfortable wearing those in no time!"
                    him"Y-yeah, but..."
                    show hima smugshy with dissolve
                    him"Aren't you making a few assumptions here?"
                    him"Who said I agreed to model for you anyway..."
                    show hima at smallshake
                    him"You'll have to earn my trust first!"
                    him"For all I know you are still a loser, creep, pervert, good for nothing [him_rel_to_bo]!"
                    menu asd92sd:
                        him"For all I know you are still a loser, creep, pervert, good for nothing [him_rel_to_bo]!"
                        "{color=[hatredcolor]}(What a bitch){/color}":
                            call checkHatred(10,"asd92sd") from _call_checkHatred_14
                            show boruto angry with dissolve
                            bot"Ugh... What a fucking bitch!"
                            bot"It doesn't matter how I feel about her right now. In reality, I'll never get anywhere with her if I don't put up an act..."
                            call changeHatred(2,"labelhimatalk_newclothes") from _call_changeHatred_109
                            bot"No matter, I'll put on a nice guy act. Slowly but surely... you'll be barking on my command!"
                        "We'll see about that...":
                            bot"Guess I'll have to find ways to earn her trust first..."
                            pass
                    bo"We'll see about that..."
                    $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                    him"Hmph!"
                    show boruto normal with dissolve
                    


                    jump himastretchingmenu
                "About the modelling thing..." if himatalk_modellingthing == False:
                    label labelhimatalk_modellingthing:
                    $ himastretchingmenu_talked = True
                    default himatalk_modellingthing = False
                    $ himatalk_modellingthing = True
                    show boruto surprised2 with dissolve
                    bo"About the modelling thing I brough up the other day... Have you considered it?"
                    show hima shy with dissolve
                    him"Y-yeah... About that..."
                    show hima worried1 with dissolve
                    him"I am not so sure I am cut out for that sort of work..."
                    bo"Huh? Where is this coming from? Besides..."
                    bo"Don't you remember? We are doing this for [hin_rel]'s sake..."
                    show hima at smallshake
                    him"Still, maybe it's better if I drop my studies and look for a real job or something. [hin_rel]'s been acting and looking real gloomy lately, I am worried about her..."
                    bo"Which is exactly the reason why you should be happy I am offering you this opportunity! We'd be helping [hin_rel] with the money we make and you wouldn't even have to drop your studies!"
                    bo"Don't give me that crap about 'not being cut out for it'!"
                    menu:
                        bo"Don't give me that crap about 'not being cut out for it'!"
                        "Besides, you'd have me to guide you along the way...":
                            show boruto laughing with dissolve
                            bo"Besides, you'd have me to show you the ropes and guide you along the way. What is there to be afraid off..."
                            call changeRespect("Himawari", 1,"labelhimatalk_modellingthing") from _call_changeRespect_155
                            show hima shy with dissolve
                            him"I a-appreciate that, but..."
                            him"That may be a problem in and of itself!"
                            him"How do I know that you are actually serious about this..."
                            him"All I have to go by is what the clothing clerk said..."
                            show hima smugshy with dissolve
                            him"You... a modelling expert? Since when! How...?"
                            him"I've never even seen you wear anything but a white shirt!"
                            show boruto snob with dissolve
                            bo"I only have to sell the product, not wear it you klutz!"
                            him"For all I know, this is just a stupid ploy of yours!"
                            him"If you can prove to me that you are what you say you are, I'll consider having a session with you..."
                        "{color=[obediencecolor]}You are the perfect fit for the job...{/color}":
                            show boruto snob with dissolve
                            bo"In fact, I think you are the perfect fit for the job!"
                            bo"Young, pretty, and not afraid to show it..."
                            bo"Those are the exact qualities that precisely MAKE you cut out for this..."
                            bo"...And don't let the compliment get to your head, you are still a demon on the outside!"
                            call changeObedience("Himawari", 1,"labelhimatalk_modellingthing") from _call_changeObedience_94
                            show hima shy with dissolve
                            him"Hmph! Y-yeah well, t-thanks. Still weird hear that coming from you..."
                            him"It feels like you are just saying what you think I want to hear..."
                            him"How do I know that you are actually serious about this..."
                            him"All I have to go by is what the clothing clerk said..."
                            show hima smugshy with dissolve
                            him"You... a modelling expert? Since when! How...?"
                            him"I've never even seen you wear anything but a white shirt!"
                            show boruto at smallshake
                            bo"I only have to sell the product, not wear it you klutz!"
                            him"For all I know, this is just a stupid ploy of yours!"
                            him"If you can prove to me that you are what you say you are, I'll consider having a session with you..."
                    him"Assuming you handsomely pay me for my efforts of course!" with vpunch
                    show boruto surprised2 with dissolve
                    bot"Hmm... Maybe I can use Yoru's help with this."
                    bot"If [him_name] sees me working with her, I am sure that'd convince her that I ain't fucking around..."
                    show boruto snob with dissolve
                    bot"Even though I totally am! Hehehe..."
                    show boruto normal with dissolve 
                    bo"Alright then, I'll hold you to that... But I fully expect you to cooperate when I prove to you I am a professional..."
                    show hima at smallshake
                    $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                    him"Hmph! We'll see about that..."
                        

                    jump himastretchingmenu    
                        
                "Give her a gift":
                    $ snacksininv = inventory.find_item_by_name("Snacks")
                    if snacksininv!= None:
                        menu himawarigiftmenu:
                            "Select a gift..."
                            "Her favorite Snacks" if himawari1sttimegift == True:
                                jump herfavoritesnakcs

                            "{color=[lovecolor]}Her favorite Snacks{/color}" if himawari1sttimegift == False:
                                label herfavoritesnakcs:
                                default himawari1sttimegift = False
                                if himawari1sttimegift == False:
                                    $ himawari1sttimegift = True
                                    bo"I have something for you..."
                                    show hima shy with dissolve
                                    him"...H-huh?" with vpunch
                                    him"F-first the clothes... now this. Since when do you care about anyone but yourself?"
                                    show hima mad with dissolve
                                    him"I hope this isn't another one of your s-stupid pranks..."
                                    show boruto embarassed with dissolve
                                    bo"Of course not, here, I bought you this..."
                                    call useItem(snacks,1) from _call_useItem_6
                                    bo"Your favorite snacks!"
                                    bo"I know we haven't been getting along all that well lately, but I..."
                                    show hima worried2 with dissolve
                                    himt"Is he really..."
                                    bo"...But I don't want us to keep going down that path, I really care about-"
                                    show hima:
                                        easein 0.5 xalign 0.4
                                    pause 0.4
                                    show blackscreen with vpunch
                                    hide hima
                                    hide boruto
                                    call changeLove("Himawari", 1) from _call_changeLove_43
                                    "Before you could finish your sentence, [him_name] charged into your arms..."
                                    show himahug1_1
                                    hide blackscreen
                                    with dissolve
                                    him"Shut up already... You don't have to ruin every half decent moment of yours with your annoying squeeky voice!"
                                    bo"O-oh..."
                                    him"But... t-thank you for thinking about me... and [hin_rel]."
                                    him"I appreciate this side of yours, I hope it's here to stay..."
                                    bo"Of course..."
                                    show blackscreen with dissolve
                                    "She pulled away..."
                                    show boruto surprised2 at left
                                    show hima shy at right:
                                        zoom 0.34
                                    hide blackscreen
                                    hide himahug1_1
                                    with dissolve
                                    himt"I don't think I can trust him just yet, but maybe he really is changing for the better..."
                                    bo"So uuh, we good now?"
                                    show hima mad with dissolve
                                    him"Of course not, dumbass!"
                                    bo"And here I though we were getting somewhere..."
                                    show hima smugshy with dissolve
                                    him"Did you think a simple gift is enough to absolve you of how shitty of a [him_rel_to_bo] you are?"
                                    $ renpy.sound.play("/audio/soun_fx/himawari/loserlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                    him"*Teehee*!" with vpunch
                                    menu firstttimegifttest:
                                        him"Did you think a simple gift is enough to absolve you of how shitty of a [him_rel_to_bo] you are? Teehee!"
                                        "{color=[hatredcolor]}(Just you wait you bitch){/color}":
                                            call checkHatred(15,"firstttimegifttest") from _call_checkHatred_15
                                            show boruto angry with dissolve
                                            bot"Just you wait you bitch..."
                                            bot"Now I know your weakness! I'll play this lovey dovey game you like. I'll pretend I care..."
                                            call changeHatred(2,"hima1sttimegift") from _call_changeHatred_110
                                            bot"Little by little, I'll corrupt your feeble mind and make you my bitch!"
                                            show boruto embarassed with dissolve
                                            bo"Hehe, guess you are right about that..."
                                        "*Awkward laugh* I suppose not":
                                            show boruto embarassed with dissolve
                                            bo"Ha...haha! I s-suppose not... But I hope it can be a start!"
                                    him"I am only half-joking of course!"
                                    show boruto normal with dissolve
                                    call changeRespect("Himawari", 10) from _call_changeRespect_156
                                    him"But really... T-thanks for trying lately, it really means a lot to me. I am sure [hin_rel] appreciates it too..."
                                    show boruto surprised2 with dissolve
                                    him"But don't think for a second you can buy me off with measly gifts! Stupid..."
                                    show hima:
                                        ease 2 xpos -1000
                                    him"Teehee! I am outa here, I've got things to do..."
                                    show boruto normal with dissolve
                                    bo"*Sigh*..."
                                else:
                                    bo"I have something for you..."
                                    show hima shy with dissolve
                                    him"Hmmmm? Is that what I think it is...?" with vpunch
                                    show boruto embarassed with dissolve
                                    bo"Hehe, you know me all too well..."
                                    call useItem(snacks,1) from _call_useItem_7
                                    bo"I got you this!"
                                    if himawari_respect >= 0:
                                        show hima happy with dissolve
                                        him"Yippee!"
                                        show hima at smallshake
                                        call changeRespect("Himawari", 3) from _call_changeRespect_157
                                        him"T-thanks! I appreciate it..."
                                    else:
                                        show hima worried2 with dissolve
                                        call changeRespect("Himawari", 4) from _call_changeRespect_158
                                        him"Huh... T-thanks, I suppose!"
                                        show hima at smallshake
                                        him"I hope you aren't thinking you can buy me off with simple gestures..."
                                    show hima smugshy with dissolve

                                    if himawari_respect >= 0:
                                        him"Keep it up and I might give you more than three seconds of attention..."
                                    else:
                                        him"Cause I wouldn't put that beneath a loser such as yourself!"
                                    show hima:
                                        ease 2 xpos -1000
                                    him"Teehee! I am outa here, I've got things to do..."
                                    show boruto normal with dissolve
                                    bo"*Sigh*..."


                                        

                                jump action_taken
                            "Return":
                                jump himastretchingmenu
                    else:
                        menu failhimawarigiftmenu:
                            "Select a gift..."
                            "{color=[lovecolor]}Her favorite Snacks{/color}":
                                "You don't have the required item..."
                                jump himastretchingmenu
                            "Return":
                                jump himastretchingmenu

                            
                    
                    jump himastretchingmenu
                "{color=[obediencecolor]}Try to earn her trust...{/color}":
                    jump hima_earnhertrust
                
                ############################# HIMAWARI OBEDIENCE ADVANCEMENT EVENT ##########################
                # Did not unlock advancement event and/or did not complete all previous quests
                "???" (advancement_event=True) if himamodel_firsttime == True or not (chosen_hate_path == True or chosen_love_path == True):
                    if himamodel_firsttime == True and not (chosen_hate_path == True or chosen_love_path == True):
                        "Complete all previous 'A Plan for [him_name]' objectives and choose the love or hatred path to unlock this option!"
                    elif himamodel_firsttime == False and not (chosen_hate_path == True or chosen_love_path == True):
                        "Choose the love or hatred path to unlock this option!"
                    else:
                        "Complete all previous 'A Plan for [him_name]' objectives to unlock this option!"
                    jump himastretchingmenu

                # May not yet meet all requirements to start advancement event (will be determined after the jump) but completed all previous quests (himamodel_firsttime == False) and made love/hatred choice
                "Try a different kind of photoshoot" (advancement_event=True) if himawari_obedience.level == 1 and himamodel_firsttime == False and (chosen_hate_path == True or chosen_love_path == True):
                    if chosen_hate_path == True:
                        jump hima_swimsuit_modelling_check
                    else: #Go to love variant
                        jump hima_swimsuit_modelling_check_love
                
                # Completed advancement event since level is higher than 1, thus remove advancement indicator
                "About that swimsuit photoshoot..." if himawari_obedience.level > 1:
                    if chosen_hate_path == True:
                        jump hima_swimsuit_modelling_start # No need to jump to the check label as advancement event was already completed once (himawari_obedience_level>1)
                    else: #Go to love variant
                        jump hima_swimsuit_modelling_start_love
                ############################# HIMAWARI OBEDIENCE ADVANCEMENT EVENT ##########################


                ############################# DOMINANCE ADVANCEMENT EVENT ##########################

                # Did not unlock advancement event and/or did not beat himawari at wrestling
                "???" (advancement_event=True) if hima_wrestling_won == False or not (chosen_hate_path == True or chosen_love_path == True):
                    if hima_wrestling_won == False and not (chosen_hate_path == True or chosen_love_path == True):
                        "Beat [him_name] at wrestling at least once and choose the love or hatred path to unlock this option!"
                    elif hima_wrestling_won == True and not (chosen_hate_path == True or chosen_love_path == True):
                        "Choose the love or hatred path to unlock this option!"
                    else:
                        "Beat [him_name] at wrestling at least once to unlock this option!"
                    jump himastretchingmenu

                # May not yet meet all requirements to start advancement event (will be determined after the jump) but beat himawari at wrestling (hima_wrestling_won == True) and made love/hatred choice
                "Talk to her about wrestling." (advancement_event=True) if dominance.level == 1 and hima_wrestling_won == True and (chosen_hate_path == True or chosen_love_path == True) and not hima_agreed_squat_competition:
                    if chosen_hate_path == True:
                        jump hima_strength_training_check
                    else: #Go to love variant
                        jump hima_strength_training_check_love
                
                # Agreed to competition - did not complete advancement event yet so show indicator
                "You ready to start squatting?" (advancement_event=True) if hima_agreed_squat_competition and dominance.level == 1:
                    if chosen_hate_path == True:
                        jump hima_agreed_squat_competition
                    else:
                        jump hima_agreed_squat_competition_love

                # Completed advancement event since level is higher than 1, thus remove advancement indicator
                "You ready to start squatting?" if hima_agreed_squat_competition and dominance.level > 1:
                    if chosen_hate_path == True:
                        jump hima_agreed_squat_competition
                    else:
                        jump hima_agreed_squat_competition_love

                ############################# DOMINANCE ADVANCEMENT EVENT ##########################

                
                "Nevermind...":
                    show boruto sceeming with dissolve
                    bo"Nevermind, I have something else to do..."
                    hide boruto with dissolve
                    show hima mad3 with dissolve
                    show hima at smallshake
                    him"Don't waste my time then you idiot! And knock on the door next time!"
                    $ boruto_location = "none"
                    scene bg day with fade:
                        zoom 0.7
                    

                
            
                
            call hideButtons from _call_hideButtons_11
            call showUIhouse from _call_showUIhouse_29
            $ ui.interact()
        "Return":
            call showUIhouse from _call_showUIhouse_30
            $ ui.interact()
            


label himawaribedroomnactionmenu:
    call hideUI from _call_hideUI_17
    menu:
        "..."
        "Choice 1":
            call showUIhouse from _call_showUIhouse_31
            jump action_taken
        "Return":
            call showUIhouse from _call_showUIhouse_32
            $ ui.interact()





screen himawari_stretching_talk:
    if day_part == 1 or day_part == 2:
        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            idle "himawari_bedroom_2him_day"  #image in ui / needs to be seperate for correct images to be displayed when hovering
            hover "himawari_bedroom_2him_hover_day"
            focus_mask "himawari_bedroom_2him_mask"
            mouse "handsmall"
            hovered [Show("displayTextScreen", displayText = "Interact with [him_name]")]
            unhovered [Hide("displayTextScreen")]
            action [Hide("displayTextScreen"), Jump("himawaribedroomntalkmenu")]
    
    else:
        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            idle "himawari_bedroom_2him"  #image in ui / needs to be seperate for correct images to be displayed when hovering
            hover "himawari_bedroom_2him_hover"
            focus_mask "himawari_bedroom_2him_mask"
            mouse "handsmall"
            hovered [Show("displayTextScreen", displayText = "Interact with [him_name]")]
            unhovered [Hide("displayTextScreen")]
            action [Hide("displayTextScreen"), Jump("himawaribedroomntalkmenu")]