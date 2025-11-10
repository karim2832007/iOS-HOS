label hinata_bathroom_event1:
    $ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    bo"Can you hurry up? I need to use the bathroom..."
    show bh_hin anim1
    show bathroom_curtains at transparency_cycle(0.95,1,5)
    with dissolve
    hin"I'll be done in a minute [bo_name]. Can you not wait?"
    scene bathroom door with dissolve:
        zoom 1.5 xalign 0.9 yalign 0.2
    menu:
        hin"I'll be done in a minute [bo_name]. Can you not wait?"
        "{color=[obediencecolor]}You know about my condition!{/color}":
            bo"I can't [hin_rel]. It's an emergency!"
            hin"Is it about y-your... condition?"
            bo"I'll be quick I promise! It's not like we can see each other anyway."
            if hinata_obedience >= 15:
                call checkObedience(15,"none","Hinata") from _call_checkObedience_29
                label replay_hinatashowerletinobedience15:
                $ initialize_replay_defaults()
                hin"O-okay, okay! Give me a moment. I'll let you know when you can come in..."
                bot"Nice! That's a start..."
                $ renpy.sound.play("/audio/soun_fx/locked_door.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                default bathrooroom_hin_event1_barge = False
                default bathrooroom_hin_event1_turn = False
                default bathrooroom_hin_event1_counter = 0
                $ bathrooroom_hin_event1_counter = 0
                $ bathrooroom_hin_event1_turn = False
                "*Door unlocks*" with vpunch
                menu :
                    "*Door unlocks*"
                    "Barge in!" if bathrooroom_hin_event1_barge == False:
                        $ bathrooroom_hin_event1_barge = True
                        bot"If I am fast enough, I must just catch a peek of her!"
                        $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                        scene black with vpunch
                        show bh_hin barge1 with flash:
                            zoom 1.3 xalign 0.6 yalign 1.0
                        show bh_hin with dissolve:
                            easein 6 yalign 0.1
                        call increaselust(10) from _call_increaselust_251
                        bot"F-fuck me! Fully naked too! [hin_rel]'s so fucking hot..."
                        hin"...H-huh!?"
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                        show bh_hin barge1_1 with dissolve:
                            zoom 1.32
                        hin"*Gasps!* [bo_name_stutter]!?" with vpunch
                        scene bh_hin barge1_2 with dissolve
                        hin"W-why- I told you to W-WAIT!" with vpunch
                        "[hin_name] ducks in embarrassment, and quickly runs back to the shower, trying her best to hide her bare body from you."
                        bo"E-emergency, remember?"
                        $ renpy.sound.play("/audio/soun_fx/curtainopening.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                        scene black with vpunch
                        $ renpy.sound.play("/audio/soun_fx/showering.opus", channel="sfx1", loop=True, relative_volume = 0.6)
                        scene bh_hin 4
                        show bathroom_curtains at transparency_cycle(0.9,1,4)
                        show particleFog_low
                        with dissolve
                        call changeRespect("Hinata", -1) from _call_changeRespect_221
                        hin"Emergency or n-not, you can't just barge in on your [hin_rel_mother] showering, you dummy!" with vpunch
                        show bh_bo 1 with dissolve
                        label bathroom_hinata_event1_jump:
                        bo"It's no big deal, [hin_rel]. I still remember when we used to shower together when I was little!"
                        hin"That's different, you klutz! You are an adult now, start acting like one for goodness' sake!"
                        show bh_bo 2 with dissolve
                        bo"In any case, it's not like I s-see you like that, right? Sexually, I mean!" with vpunch
                        hin"Good g-grief, [bo_name]! Can you please stay silent while you are dealing with your c-condition?"
                        bo"I'll try..."
                        show bathroom_curtains at transparency_cycle(0.8,0.9,4)
                        show bh_hin anim1
                        with dissolve
                        hin"*Sigh...*"
                        show bh_bo at smallshake
                        $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                        "[hin_name] gets back to her showering while you try to get yourself off right next to her..."
                        "Through the corner of your eye, you notice that her silhouette is becoming more and more apparent as time goes by..."
                        bot"I can make out her silhouette through the curtain!"
                        bot "Must be all this steam and humidity building up..."
                        bot"Hehe! I don't mind some extra help from you, [hin_rel]!"
                        show bh_hin 1_2
                        with dissolve
                        bot"O-oh! Especially when you bend over like that!" with vpunch
                        $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                        show bh_hin anim1_1 with dissolve
                        hin"Let me know when you are done with your treatment, okay?"
                        bo"Right..."
                        bot"She has no idea I am perving on her!"
                        menu bathroom_hina_event1_menu:
                            bot"She has no idea I am perving on her!"
                            "Take your sweet time..." if bathrooroom_hin_event1_counter <= 2:
                                if bathrooroom_hin_event1_counter == 0:
                                    $ bathrooroom_hin_event1_counter +=1
                                    show bh_bo at smallshake
                                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                    bot"I am not passing this opportunity to perv on you, [hin_rel]!"
                                    show bh_hin anim2 with dissolve
                                    bot"O-oh shit! A front view too?"
                                    show bh_bo at smallshake
                                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                    bot"Nice tits, [hin_rel]! Wait a second..."
                                    bot"Does that mean she can see me too?"
                                    bot"I guess she has her eyes closed though..."
                                    show bathroom_curtains at transparency_cycle(0.7,0.95,4) with dissolve
                                    "You notice the translucency of the curtain increasing as time goes by..."
                                    jump bathroom_hina_event1_menu
                                elif bathrooroom_hin_event1_counter == 1:
                                    $ bathrooroom_hin_event1_counter +=1
                                    show bh_bo at smallshake
                                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                    show bh_hin anim1_1 with dissolve
                                    show bathroom_curtains at transparency_cycle(0.6,0.9,4) with dissolve
                                    bot"N-nice [hin_rel]! Show me more of that ass..." with flash
                                    show bh_bo at smallshake
                                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                    bot"Good thing she turned around! That way she won't realize that the curtain isn't hiding much by now..."
                                    "You notice the translucency of the curtain increasing even more as time goes by..."
                                    jump bathroom_hina_event1_menu
                                else:
                                    $ bathrooroom_hin_event1_counter +=1
                                    show bh_bo at smallshake
                                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                    show bathroom_curtains at transparency_cycle(0.5,0.85,4) with dissolve
                                    bot"Bending over, showing your ass to your [hin_rel_to_bo] like that!" with flash
                                    bot"You are so f-freaking hot [hin_rel]!" with flash
                                    hin"Still having issues... [bo_name]?"
                                    bo"Y-yeah..."
                                    hint"Poor boy..."
                                    show bh_hin anim2 with dissolve
                                    bot"Oh s-shit! Her tits ar as clear as day! Pretty sure she'd see me too if she..."
                                    show bh_hin 3 with dissolve
                                    camera:
                                        easein 2 zoom 1.4 xalign 0.5 yalign 0.1
                                    pause 0.5
                                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                                    hin"*Sharp Gasp*" with vpunch
                                    show bh_hin 3_1 with dissolve
                                    hint"The c-curtain, I can see through it! That means [bo_name]..."
                                    show bh_bo at smallshake
                                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                    show bh_hin 3_2 with dissolve
                                    hint"Is he looking at m-me!?" with vpunch
                                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                                    show bh_hin 4 with dissolve
                                    hint"I am s-sure of it! He was w-watching me..."
                                    if bathrooroom_hin_event1_turn == True:
                                        hint"It seemed like he was standing right across me, staring at me. I could even see his..."
                                        call changeRespect("Hinata",-1) from _call_changeRespect_222
                                        hint"D-darn it [bo_name]! Why did I let this happen in the first place..."
                                    "[hin_name] turns around in shame, after realizing what was happening. She curled into herself, waiting for the inevitable..."
                                    show bh_bo at smallshake
                                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                    bot"S-she must have realized!" with flash
                                    jump bathroom_hina_event1_menu
                                    

                            "Finish the job":
                                show bh_bo at smallshake
                                $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                bot"F-fuck! T-this feels weird..." with flash
                                bot"P-perving on [hin_rel] without her knowing..."
                                bot"But it also feels..." with flash
                                scene black with longerflash
                                $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                bot"So g-good! *Moans*" with vpunch
                                bo"*Panting...*"
                                hin"A-are you... done?"
                                $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                bo"I am. T-thanks for helping, [hin_rel]!"
                                stop sfx2 fadeout 3
                                camera:
                                    perspective True
                                    reset
                                scene bh_hin 4
                                with fade
                                call changeObedience("Hinata", 1) from _call_changeObedience_135
                                hint"T-that was weird, but I am glad he is able to take care of himself on his own..."
                                scene black with dissolve
                                jump action_taken
                            
                            "{color=[hatredcolor]}Cum on her!{/color}" if bathrooroom_hin_event1_counter >= 2 and bathrooroom_hin_event1_turn == True:
                                show bh_bo at smallshake
                                $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                bot"Too little too l-late, [hin_rel]!" with flash
                                bot"You've put on a nice show, and n-now..." with flash
                                $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                show bathroom_curtains_cum at transparency_cycle(0.7,1,3) with longerflash
                                call changeHatred(1) from _call_changeHatred_171
                                bot"I h-have to reward you, you s-slut! *Moans*"
                                "Standing just a couple feet away from [hin_name]. you shot your load onto the curtain itself..."
                                bo"*Panting...*"
                                hin"A-are you... done?"
                                hide bh_bo with dissolve
                                $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                bo"Sure am. T-thanks for helping, [hin_rel]!"
                                stop sfx2 fadeout 3
                                camera:
                                    perspective True
                                    reset
                                scene bh_hin 4
                                with fade
                                hint"H-helping? [bo_name] cannot possibly be thinking of me that w-way. Can he?"
                                hint"Maybe I should consult Lady Tsunade again!"
                                scene black with dissolve
                                bot"That was fun!"
                                jump action_taken
                            "{color=[dominancecolor]}Get comfortable!{/color}" if bathrooroom_hin_event1_turn == False:
                                call checkDominance(10,"bathroom_hina_event1_menu") from _call_checkDominance_46
                                show bh_bo 3 with dissolve:
                                    xzoom -1 xpos 0
                                $ bathrooroom_hin_event1_turn = True
                                bot"This ought to make the process easier!"
                                bot"I am pretty sure she'd be able to make out my silhouette too from her side!"
                                show bh_bo at smallshake
                                $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                bot"I wonder what you'd think seeing me jerk off to you up close, [hin_rel]!"
                                jump bathroom_hina_event1_menu
                      
                            

                    "{color=[hatredcolor]}Barge in again!{/color}" if bathrooroom_hin_event1_barge == True:
                        bot"I am not missing another view of your bare curves, [hin_rel]!"
                        $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                        scene black with vpunch
                        show bh_hin barge1 with flash:
                            zoom 1.3 xalign 0.6 yalign 1.0
                        show bh_hin with dissolve:
                            easein 6 yalign 0.1
                        call increaselust(10) from _call_increaselust_252
                        call changeHatred(1) from _call_changeHatred_172
                        bot"You sexy piece of ass! The things I'd do to you, [hin_rel]!"
                        hin"...H-huh!?"
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                        show bh_hin barge1_1 with dissolve:
                            zoom 1.32
                        hin"*Gasps!* [bo_name_stutter]!?" with vpunch
                        scene bh_hin barge1_2 with dissolve
                        hin"A-again with this!?" with vpunch
                        "[hin_name] ducks in embarrassment, and quickly runs back to the shower, trying her best to hide her bare body from you."
                        bo"I told you, it's an emergency!"
                        $ renpy.sound.play("/audio/soun_fx/curtainopening.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                        scene black with vpunch
                        $ renpy.sound.play("/audio/soun_fx/showering.opus", channel="sfx1", loop=True, relative_volume = 0.6)
                        scene bh_hin 4
                        show bathroom_curtains at transparency_cycle(0.9,1,4)
                        show particleFog_low
                        with dissolve
                        call changeRespect("Hinata", -2) from _call_changeRespect_223
                        hin"Emergency or n-not, I told you before, you can't just barge in on your [hin_rel_mother] showering, you idiot!" with vpunch
                        show bh_bo 1 with dissolve
                        jump bathroom_hinata_event1_jump
                    "Wait for her call":
                        bot"..."
                        hin"Okay, you can come in now..."
                        $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                        scene bh_hin 4
                        show bathroom_curtains at transparency_cycle(0.9,1,4)
                        show particleFog_low
                        with dissolve
                        bo"Thanks [hin_rel]..."
                        hin"You do what you need to do [bo_name]. I understand you are in p-pain so... I'll wait until you are done."
                        show bh_bo 1 with dissolve
                        bo"I'll try my best..."
                        hin"You should know though, this feels a bit off to me..."
                        hin "Let's try to not share the bathroom in the f-future, okay?"
                        jump bathroom_hinata_event1_jump
                    

            else:
                call checkObedience(20,"none","Hinata") from _call_checkObedience_30
                hin"I don't know [bo_name], can't you just hold on for a minute longer? Or, y-you know... do it elsewhere?"
                menu:
                    hin"I don't know [bo_name], can't you just hold on for a minute longer? Or, y-you know... do it elsewhere?"
                    "Fine, I'll wait":
                        bo"Fine, I'll wait."
                        hin"I'll be out in a minute!"
                        call showUIhouse from _call_showUIhouse_74
                        $ ui.interact()
                    "Eat something while you wait for her":
                        jump eatsomethingwhileyouwait
                        
                    


        "Fine, I'll wait":
            bo"Fine, I'll wait."
            hin"I'll be out in a minute!"
            call showUIhouse from _call_showUIhouse_75
            $ ui.interact()

        "{color=[obediencecolor]}Wait for her outside...{/color}":
            label eatsomethingwhileyouwait:
            $ initialize_replay_defaults()
            bot"Better keep myself busy until [hin_rel]'s done then..."
            scene black with dissolve
            bot"I was getting kinda hungry anyway!"
            if day_part == 3:
                scene kitchen night
            else:    
                scene kitchen day
            show boruto normal
            with dissolve
            show boruto normal:
                easeout 2.5 xpos -1300
            "You scour the fridge for something to eat..."
            bot"Nothing tasty..." with vpunch
            scene black with dissolve
            bot"This will have to do!"
            show boruto_banana 0 with dissolve:
                fit "contain" xalign 0.5
            bot"I should check if she's done. If I am lucky, I might even chance upon her only wearing her towel! Hehe..."
            menu secretmenu_boruto_ending:
                bot"I should check if she's done. If I am lucky, I might even chance upon her only wearing her towel! Hehe..."
                "Check on [hin_name]...":
                    scene black with dissolve
                    show bg bathroom_banana1 with dissolve:
                        yalign 1.0 alpha 0.4
                    show bg:
                        easein 4 alpha 0.1 yalign 0.3
                    pause 1
                    show boruto_banana 0 with dissolve:
                        fit "contain" xalign 0.5
                    bot"Door's closed. She's still at it it seems..."
                    bot"Well, nothing to do but to finish this banana!"
                    show boruto_banana 1 with dissolve:
                        fit "contain" xalign 0.5
                    "You take a generous bite!" with vpunch
                    show boruto_banana 2
                    "The banana appears to be lodged in your throat..."
                    bot"W-what the fuck! Is someone wishing for me to d-die or something?"
                    scene black with vpunch
                    bo"*Cough cough! D-damn..." with vpunch
                    show bg bathroom_banana1 with dissolve:
                        yalign 1.0
                    bo"Can't believe I almost choked on a banana!"
                    menu:
                        bo"Can't believe I almost choked on a banana!"
                        "Toss the peel on the ground!":
                            show boruto_bananapeel_floor with dissolve:
                                yalign 1.0 alpha 0.5
                            bot"Freaking banana..."
                            hide boruto_bananapeel_floor
                            show bananapeel_floor:
                                yalign 1.0
                            with dissolve
                            bot"Damn near killed me!"
                            $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                            bot"S-shit, [hin_rel]'s coming out! Better hide before she starts nagging me about littering."
                            scene black with vpunch
                            bot"I'll just blame it on [him_name] instead. Hehe!"
                            scene bg bathroom_banana1
                            show bananapeel_floor
                            with dissolve
                            "You hide behind a hallway corner until [hin_name] leaves the bathroom..."
                            bot"There's no way [hin_rel] would not notice the peel, right?"
                            scene hin_bath bananaslip with dissolve:
                                yalign 1.0
                            show hin_bath:
                                easein 3 yalign 0.0
                            bot"No shot! People slipping on banana peels is only a thing in kid's shows..."
                            show screen parallax1280("hin_bath bananaslip",1,1.0,False) with dissolve
                            call showscrollingimage from _call_showscrollingimage_170
                            call hidescrollingimage from _call_hidescrollingimage_94
                            "[hin_name] walks towards the discarded banana peel..."
                            $ chance_banana = random.random() < 0.7
                            if chance_banana:
                                
                                default hinata_slipped_banana = False
                                $ hinata_slipped_banana = True
                                call randomCheck(True,"She doesn't spot the banana peel!") from _call_randomCheck_3
                                show hin_bath:
                                    easein 2 yalign 1.0
                                "It doesn't seem like she noticed the discarded banana peel..."
                                if hinata_slipped_banana == True and himawari_waitoutside == True: #complete wait outside quest
                                    if quest.exists("bo_shower_1"):
                                        if quest.is_state("bo_shower_1", "unlocked"):
                                            if quest.exists("shower1_3"):
                                                $ quest.check("shower1_3", "completed")
                                            $ quest.check("bo_shower_1", "done") #marks left quest as complete (make sure any references now check if quest is completed to avoid errors)
                                            # $ quest.remove("Just a peek!") #remove from right page
                                            $ notification ("Quest Completed: Just a peek...")
                                scene black with vpunch
                                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                                hin"H-huh!?" with vpunch
                                $ renpy.sound.play("/audio/soun_fx/bananaslip.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                show hin_bath bananaslip 1 with dissolve:
                                    yalign 0.0 xalign 0.5
                                show hin_bath:
                                    easein 2 yalign 1.0
                                bot"Cartoon logic is real!?" with vpunch
                                scene black
                                $ renpy.sound.play("/audio/soun_fx/bodythud.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                "[hin_name] slipped, and awkwardly fell on her back!" with vpunch
                                show screen parallax1280("hin_slip start1",1,1.0,True) with dissolve
                                call showscrollingimage from _call_showscrollingimage_171
                                bot"D-damn! Is she okay?" with vpunch
                                bo"[hin_rel_stutter]...?"
                                "Concussed by the fall, she laid temporarily unconscious on the floor..."
                                menu hin_slipped_menu2:
                                    "Concussed by the fall, she laid temporarily unconscious on the floor..."
                                    "{color=[hatredcolor]}Use her!{/color}":
                                        default hinata_slipped_banana_usedher = False
                                        $ hinata_slipped_banana_usedher = True

                                        call checkHatred(20,"hin_slipped_menu2") from _call_checkHatred_29
                                        if quest_hin.exists("hin1H_1") and not _in_replay: #check if quest exists
                                            if quest_hin.is_state("hin1H_1", "pending"): #check quest state
                                                
                                                $ quest_hin.check("hin1H_1", "done") #update hinata shower quest to strikethrough if already completed
                                                $ notification (f"{hin_name} Hatred objective completed")
                                        bot"No response. She's out cold! Which means, she's mine for the taking!"
                                        hide screen parallax1280
                                        show screen parallax1280("hin_slip start1_1",1,1.0,False)
                                        with dissolve

                                        bot"She's mine for the taking! Hehehe..."
                                        hin"*Shallow breathing*... ugh..."
                                        bot"Fuck, she's recovering quick! I don't have much time to savor her body. I should..."
                                        menu:
                                            bot"Fuck, she's recovering quick! I don't have much time to savor her body. I should..."
                                            "Focus on her lower body":
                                                bot"Better act quick. I am not missing this chance!"
                                                hide screen parallax1280
                                                show screen parallax1280("hin_slip lower0_11")
                                                with dissolve

                                                bot"Even unconscious, you look so damn sexy [hin_rel]! It makes me wanna..."
                                                menu lowerbody_slip_menu_hiu:
                                                    bot"Even unconscious, you look so damn sexy [hin_rel]! It makes me wanna..."
                                                    "Caress her thighs":
                                                        bot"Your legs are so d-damn sexy!"
                                                        hide screen parallax1280
                                                        show screen parallax1280("hin_slip thighs_anim1",1.25,1.0)
                                                        with dissolve
                                                        $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                                                        bot"All those squats you do, I can feel every fiber of muscle beneath your soft skin..."
                                                        hin"Mfh... Na... [na_name]...?" with vpunch
                                                        bot"Oh s-shit!" with vpunch
                                                        bot"Is she d-dreaming about [na_rel]?"
                                                        hide screen parallax1280
                                                        show screen parallax1280("hin_slip lower2",1.25,0.0, menuenabled=True)
                                                        with dissolve
                                                        hin"...Ah.. *Softly Moaning*... Mff..." with vpunch
                                                        "[hin_name] shifted her posture slightly, and placed her arm upon her chest in a peculiar way..."
                                                        bot"Is she... t-touching herself?"
                                                        bot"M-maybe now's my chance!" with vpunch
                                                        menu:
                                                            bot"M-maybe now's my chance!"
                                                            "Expose her pussy!":
                                                                pass
                                                        show screen parallax1280("blackscreen",1.25,0.0, menuenabled=False) with dissolve

                                                        "You opportunistically try your luck in revealing [hin_name]'s erogenous zones..."
                                                        show screen parallax1280("hin_slip lowerundress 1",1.0,1.0) with dissolve
                                                        "Her posture shifts slightly as you grab her towel, but you do not relent..."
                                                        hin"..."
                                                        bot"Just a little higher!" with vpunch
                                                        show screen parallax1280("blackscreen",1.0,1.0) with dissolve
                                                        $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                                        show screen parallax1280("hin_slip lowerundress 2",1.0,1.0,menuenabled=True) with dissolve
                                                        bot"[hin_rel]'s bald pussy, in plain sight..." with vpunch
                                                        bot"If I could just spread her legs a tad bit..."
                                                        menu:
                                                            bot"If I could just spread her legs a tad bit..."
                                                            "Spread her legs!":
                                                                pass
                                                        hide screen parallax1280
                                                        show screen parallax1280("hin_slip lowerundress 2push",1.0,1.0,menuenabled=False)
                                                        with dissolve
                                                        bot"Come on [hin_rel]! Spread your sexy legs open, just a tiny bit for me!"
                                                        scene black
                                                        call hidescrollingimage("Click twice to spread her legs!") from _call_hidescrollingimage_95
                                                        show screen parallax1280("hin_slip lowerundress 3",1.0,1.0,menuenabled=False) with dissolve
                                                        call showscrollingimage from _call_showscrollingimage_172

                                                        call increaselust(50) from _call_increaselust_253
                                                        bot"D-damn! It's fucking beautiful..."
                                                        hin"...N-not... t-there!" with vpunch
                                                        bot"[hin_rel_stutter]!?" with vpunch
                                                        hide screen parallax1280
                                                        show screen parallax1280("hin_slip lowerundress 4",1.0,1.0,menuenabled=True)
                                                        with dissolve
                                                        hin"Ah-ah... y-your h-hands... so cold..." with vpunch
                                                        bot"S-she spread her legs even wider!" with vpunch
                                                        hin"N-not... t-there... [na_name]!" with vpunch
                                                        bot"W-what the fuck is she d-dreaming about!"
                                                        hin"*Moans Softly*... A-ah!" with vpunch
                                                        bot"W-well then, [hin_rel]... If y-you are so cold, maybe I could p-play into your fantasies and warm you up!"
                                                        menu:
                                                            bot"W-well then, [hin_rel]... If y-you are so cold, maybe I could p-play into your fantasies and warm you up!"
                                                            "Warm her up!":
                                                                pass
                                                        bot"How can I not indulge myself, when you present yourself like that, [hin_rel_stutter]!"
                                                        show screen parallax1280("blackscreen",1.0,1.0,menuenabled=False) with dissolve
                                                        bot"I have to..."
                                                        "You lay on your stomach..."
                                                        show screen parallax1280("hin_slip lowerundress 5",1.0,1.0,menuenabled=False) with dissolve
                                                        $ renpy.sound.play("/audio/soun_fx/suck3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                                        bot"I have to have a t-taste of you!" with vpunch
                                                        $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                                        show screen parallax1280("hin_slip pussyrum_anim1",1.0,1.0,menuenabled=False) with dissolve
                                                        bot"Oh my f-fucking days! I am eating out [hin_rel]! My face is b-buried in her pussy!"
                                                        hin"...Mfph! *Moans*... N-no!"
                                                        bot"She is so w-wet, her juices are leaking straight into my mouth! S-she tastes so goddamn good!" with vpunch
                                                        bot"F-fuck I am g-getting so d-damn horny [hin_rel]! If [na_rel] won't satisfy you, then  m-maybe I coul-"
                                                        hide screen parallax1280
                                                        show screen parallax1280("hin_slip lowerundress 5_2",1.0,0.0,menuenabled=False)
                                                        with dissolve
                                                        $ renpy.sound.play("/audio/soun_fx/suck3.opus", channel="sfx2", loop=False, relative_volume = 1.1)
                                                        $ renpy.sound.play("/audio/soun_fx/mgsalert.opus", channel="sfx3", loop=False, relative_volume = 1.1)
                                                        hin"Na... ru... W-where... am I...? [bo_name_stutter]?" with vpunch
                                                        scene black
                                                        call hidescrollingimage from _call_hidescrollingimage_96
                                                        bot"O-oh shit, oh fuck! Fuck, fuck!" with vpunch
                                                        show hin_slip lowerundress 0:
                                                            yalign 1.0
                                                        show wakeup_overlay_face 1:
                                                            yalign 1.0
                                                        with dissolve
                                                        show wakeup_overlay_face:
                                                            easein 2 yalign 0.0
                                                        show hin_slip:
                                                            easein 2 yalign 0.0
                                                        # camera:
                                                        #     easein 2 ypos -200  
                                                        "Realizing [hin_name] was regaining her senses, you quickly pull her towel down, hiding the evidence to the best of your abilities..."                                                            
                                                        hin"...Ah...E-eh? [bo_name_stutter]? Is t-that... you?"
                                                        bo"Y-yes, [hin_rel_stutter]. It's me! C-come on, w-w-wake up..."
                                                        bo"Y-you hit your head p-pretty hard! I t-think you've been out for a while!"
                                                        show wakeup_overlay_face 2 with dissolve
                                                        hin"M-my head? Oh r-right... I slipped, didn't I?"
                                                        hin"B-but... It felt like I was still p-present... f-feeling t-things..."
                                                        bo"T-things? W-what things [hin_rel]?"
                                                        hin"I... don't know. I think I was d-dreaming about your [na_rel]. I could even sense the cold air brushing against my skin..."
                                                        hin"E-even your [na_rel]'s... touch."
                                                        scene hin_slip lowerundress 0 with dissolve:
                                                            yalign 1.0
                                                        hin"S-such a strange feeling..." with vpunch
                                                        hin"Can you please h-help me get on my feet?"
                                                        scene black with dissolve
                                                        bot"Of course..."
                                                        
                                                     
                                                        scene bg day:
                                                            zoom 0.7
                                                        show boruto surprised2 at left
                                                        show thina thinking at right:
                                                            zoom 1.1
                                                        with dissolve
                                                        hin"T-that was... surreal. I feel like I am losing grip with reality... How did I e-even slip in the first place?"
                                                        bo"W-wet floor? Eh-eh... *Nervous chuckle*" 
                                                        show thina b1 with dissolve
                                                        hin"In any case... Thank you, [bo_name]. I'll go lay down for a bit. I still feel...strange, light-headed..."
                                                        show boruto snob with dissolve
                                                        bo"You do that [hin_rel]..."
                                                        hide thina with dissolve
                                                        call changeHatred(1) from _call_changeHatred_173
                                                        show boruto sceeming with dissolve
                                                        bot"Holy shit! She has no idea I've been eating her pussy like a damn maniac!" with vpunch
                                                        bot"Can't believe I am off the hook scot-free! I should be thanking you instead [hin_rel]!"
                                                        jump action_taken

                                                    "Go lower (Feet)":# (supporter_scene = True)
                                                        jump golowerfeet_hina
                                                        # $ call_label_action("golowerfeet_hina")
                                                        call supp_rew from _call_supp_rew_10
                                                        jump lowerbody_slip_menu_hiu
                                                        

                                                                
                                                            


                                                        
                                                    
                                                    "{color=[obediencecolor]}????{/color}" if lr_massagecounter < 100:
                                                        "To unlock this option, offer [hin_name] a foot massage in the living room first!"
                                                        jump lowerbody_slip_menu_hiu

                                                        
                                         
                                            "Focus on her upper body":
                                                bot"Better act quick. I am not missing this chance!"
                                                show screen parallax1280("hin_slip tits1") with dissolve
                                                bot"Even unconscious, you look so damn sexy [hin_rel]! It makes me wanna..."
                                                menu:
                                                    bot"Even unconscious, you look so damn sexy [hin_rel]! It makes me wanna..."
                                                    "Savor your tits!":
                                                        bot"I can't leave that magnificent rack of yours unattended, can I [hin_rel]?"
                                                        bot"Let's get those hands out of the way!"
                                                        show screen parallax1280("hin_slip tits1_1") with dissolve
                                                        bot"Looking good [hin_rel]!"
                                                        show screen parallax1280("blackscreen") with dissolve
                                                        bot"Now for the grand prize..."
                                                        label tits_from_playface_label:
                                                        show screen parallax1280("hin_slip titgrope 1", 1.25) with dissolve
                                                        bot"Can't believe you carry those around every day!" with vpunch
                                                        menu hin_slip_tit123_menu:
                                                            bot"Can't believe you carry those around every day!"
                                                            "Make them jiggle!":
                                                                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                                                                show screen parallax1280("hin_slip tits_anim1", 1.25) with dissolve
                                                                bot"Titties really are the best! So soft, so squishy..." with vpunch
                                                                bot"I want to stuff my face in them!" with vpunch
                                                                jump hin_slip_tit123_menu
                                                            "Carefully expose her!":
                                                                bot"If she questions it, I can just say her towel slipped off during her fall! Hehe..."
                                                                show screen parallax1280("hin_slip titgrope 2", 1.25) with dissolve
                                                                bot"Just a little bit..."
                                                                bot"D-damn! [hin_rel] has such an erotic body..."
                                                                pass

                                                            
                                                        
                                                        bot"Who am I kidding, I am not stopping here!" with vpunch
                                                        show screen parallax1280("hin_slip titgrope 3", 1.25,menuenabled=True) with dissolve
                                                        bot"Just look at them!" with vpunch
                                                        bot"They were made to be sucked on!"
                                                        menu:
                                                            bot"They were made to be sucked on!"
                                                            "Suck them tiddies!":
                                                                pass
                                                        $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                                                        $ renpy.sound.play("/audio/soun_fx/suck5.opus", channel="sfx2", loop=False, relative_volume = 1.1)
                                                        show screen parallax1280("hin_slip titsuck_anim1") with dissolve
                                                        bo"Mhmph! *Sucking*" with vpunch
                                                        $ renpy.sound.play("/audio/soun_fx/suck4.opus", channel="sfx3", loop=False, relative_volume = 1.1)
                                                        bot"You even have a sweet taste to you [hin_rel]..." with vpunch
                                                        bot"How can a woman be as p-perfect as you are!" with vpunch
                                                        menu randommenu1238_ts:
                                                            bot"How can a woman be as p-perfect as you are!"
                                                            "Check how she's doing":
                                                                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                                                                $ renpy.sound.play("/audio/soun_fx/suck5.opus", channel="sfx2", loop=False, relative_volume = 1.1)
                                                                bot"I should make sure she is still asleep. Don't worry my beloved titties..."
                                                                show screen parallax1280("hin_slip titgrope 3_lactating", 1.25,menuenabled=True) with dissolve
                                                                bot"I shall get back to you... s-soon!" with vpunch
                                                                "You notice [hin_name] lactating..."
                                                                bot"[hin_rel]'s breast milk! It's pouring out..."
                                                                bo"[hin_rel_stutter]...?"
                                                                hin"..."
                                                                bot"She is still out cold which means..."
                                                                menu milkingtimemnu:
                                                                    bot"She is still out cold which means..."
                                                                    "{color=[hatredcolor]}It's milking time!{/color}":
                                                                        call checkHatred(20,"milkingtimemnu") from _call_checkHatred_30
                                                                        bot"It's time I get a proper taste of you, [hin_rel]!" with vpunch
                                                                        show screen parallax1280("hin_slip titgrope 7",menuenabled=True) with dissolve
                                                                        $ renpy.sound.play("/audio/soun_fx/suck3.opus", channel="sfx2", loop=False, relative_volume = 1.1)
                                                                        call changeHatred(1) from _call_changeHatred_174
                                                                        bot"Look at you sprouting milk all over! Just like a bitch in heat..."
                                                                        menu:
                                                                            bot"Look at you sprouting milk all over! Just like a bitch in heat..."
                                                                            "{color=[hatredcolor]}Suck them dry!{/color}":
                                                                                pass
                                                                        show screen parallax1280("hin_slip milking_anim1") with dissolve
                                                                        $ renpy.sound.play("/audio/soun_fx/suck5.opus", channel="sfx2", loop=False, relative_volume = 1.1)
                                                                        bot"Don't worry you, [hin_rel]! You fucking cow... I'll suck your tits dry!"
                                                                        $ renpy.sound.play("/audio/soun_fx/suck2.opus", channel="sfx2", loop=False, relative_volume = 1.1)
                                                                        bot"Getting your tits stretched and milked like this..."
                                                                        call changeHatred(1) from _call_changeHatred_175
                                                                        $ renpy.sound.play("/audio/soun_fx/suck4.opus", channel="sfx2", loop=False, relative_volume = 1.1)
                                                                        bot"Have you no shame, [hin_rel]? If you are such an animal, perhaps I shall breed you too soon!"
                                                                        call hidescrollingimage from _call_hidescrollingimage_97
                                                                        scene black with vpunch
                                                                        $ renpy.sound.play("/audio/soun_fx/suck3.opus", channel="sfx2", loop=False, relative_volume = 1.1)
                                                                        $ renpy.sound.play("/audio/soun_fx/mgsalert.opus", channel="sfx3", loop=False, relative_volume = 1.1)
                                                                        hin"...[bo_name_stutter]"
                                                                        bot"Oh s-shit, oh fuck!" with vpunch
                                                                        "You quickly fell back, hoping [hin_name] did not quite understand what was going on..."
                                                                        show hin_slip lowerundress 0:
                                                                            yalign 1.0
                                                                        show wakeup_overlay_face 1:
                                                                            yalign 1.0
                                                                        show wakeup_overlay_tits 1:
                                                                            yalign 1.0
                                                                        with dissolve
                                                                        camera:
                                                                            easein 2 ypos -200                                                              
                                                                        hin"...Ah... [bo_name_stutter]? W-what is..."
                                                                        bo"Y-yes, [hin_rel_stutter]. It's me! C-come on, wake up..."
                                                                        bot"S-shit! Her tits are still out. Guess I'll have to blame the fall..."
                                                                        bo"U-uhm, Y-you hit your head pretty hard. Are you okay?"
                                                                        show wakeup_overlay_face 2 with dissolve
                                                                        hin"M-my head? Oh r-right... I slipped, didn't I?"
                                                                        show wakeup_overlay_face 3 with dissolve
                                                                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                                                                        hin"T-the towel!" with vpunch
                                                                        camera:
                                                                            reset
                                                                        scene black
                                                                        with vpunch
                                                                        "[hin_name] quickly covered herself up upon realizing she was exposed right in front of you..."
                                                                        hin"G-good lords! How l-long was I like that!" with vpunch
                                                                        scene bg day:
                                                                            zoom 0.7
                                                                        show boruto snob at left
                                                                        show thina b1 at right:
                                                                            zoom 1.1
                                                                        with dissolve
                                                                        "What she didn't realize, is that you were responsible for it!"
                                                                        bo"It's been a m-minute. I was t-trying to get you back to your senses..."
                                                                        hin"T-thank you [bo_name]. I'll go lay down for a bit, okay? I still feel a bit light-headed..."
                                                                        bo"N-no worries..."
                                                                        hide thina with dissolve
                                                                        call changeHatred(1) from _call_changeHatred_176
                                                                        bot"Can't believe I am off the hook scot-free after sucking your titties! I should be thanking you instead [hin_rel]!"
                                                                        scene black with dissolve
                                                                        bot"Hehe! I should invest in more banana peels!"
                                                                        jump action_taken


                                                                        
                                                                            
                                                                            
                                                                    "Keep sucking tenderly...":
                                                                        bot"I get to have another taste..."
                                                                        $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                                                                        $ renpy.sound.play("/audio/soun_fx/suck5.opus", channel="sfx2", loop=False, relative_volume = 1.1)
                                                                        show screen parallax1280("hin_slip titsuck_anim1_1") with dissolve
                                                                        bot"Breastfeed me like an infant! Am I asking for much [hin_rel]?" with vpunch
                                                                        bot"I just need to..."
                                                                        $ renpy.sound.play("/audio/soun_fx/suck4.opus", channel="sfx2", loop=False, relative_volume = 1.1)
                                                                        show screen parallax1280("hin_slip titgrope 6") with dissolve
                                                                        bot"Taste the milk straight out of you!" with vpunch
                                                                        $ renpy.sound.play("/audio/soun_fx/suck3.opus", channel="sfx2", loop=False, relative_volume = 1.1)
                                                                        $ renpy.sound.play("/audio/soun_fx/mgsalert.opus", channel="sfx3", loop=False, relative_volume = 1.1)
                                                                        show screen parallax1280("hin_slip titgrope 6_1") with dissolve
                                                                        hin"*Regaining consciousness* ...A-ah... [bo_name_stutter]...?" with vpunch
                                                                        call hidescrollingimage from _call_hidescrollingimage_98
                                                                        scene black with vpunch
                                                                        bot"Oh s-shit, oh fuck!" with vpunch
                                                                        "You quickly fell back, hoping [hin_name] did not quite understand what was going on..."
                                                                        show hin_slip lowerundress 0:
                                                                            yalign 1.0
                                                                        show wakeup_overlay_face 1:
                                                                            yalign 1.0
                                                                        show wakeup_overlay_tits 1:
                                                                            yalign 1.0
                                                                        with dissolve
                                                                        camera:
                                                                            easein 2 ypos -200                                                              
                                                                        hin"...Ah... [bo_name_stutter]? W-what is..."
                                                                        bo"Y-yes, [hin_rel_stutter]. It's me! C-come on, wake up..."
                                                                        bot"S-shit! Her tits are still out. Guess I'll have to blame the fall..."
                                                                        bo"U-uhm, Y-you hit your head pretty hard. Are you okay?"
                                                                        show wakeup_overlay_face 2 with dissolve
                                                                        hin"M-my head? Oh r-right... I slipped, didn't I?"
                                                                        show wakeup_overlay_face 3 with dissolve
                                                                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                                                                        hin"T-the towel!" with vpunch
                                                                        camera:
                                                                            reset
                                                                        scene black
                                                                        with vpunch
                                                                        "[hin_name] quickly covered herself up upon realizing she was exposed right in front of you..."
                                                                        hin"G-good lords! How l-long was I like that!" with vpunch
                                                                        scene bg day:
                                                                            zoom 0.7
                                                                        show boruto snob at left
                                                                        show thina b1 at right:
                                                                            zoom 1.1
                                                                        with dissolve
                                                                        "What she didn't realize, is that you were responsible for it!"
                                                                        bo"It's been a m-minute. I was t-trying to get you back to your senses..."
                                                                        hin"T-thank you [bo_name]. I'll go lay down for a bit, okay? I still feel a bit light-headed..."
                                                                        bo"N-no worries..."
                                                                        hide thina with dissolve
                                                                        call changeHatred(1) from _call_changeHatred_177
                                                                        bot"Can't believe I am off the hook scot-free after sucking your titties! I should be thanking you instead [hin_rel]!"
                                                                        scene black with dissolve
                                                                        bot"Hehe! I should invest in more banana peels!"
                                                                        jump action_taken
                                                                    
                                                            "Grope her!":
                                                                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                                                                $ renpy.sound.play("/audio/soun_fx/suck5.opus", channel="sfx2", loop=False, relative_volume = 1.1)
                                                                show screen parallax1280("hin_slip titsuck_anim1",zoom=1,initial_ypos=1.0, facetoadd="hin_slip titsuck_gropeanim1")
                                                                with dissolve
                                                                bot"Your tits are fucking amazing [hin_rel]!"
                                                                jump randommenu1238_ts
                                                            "Kiss her":
                                                                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                                                                $ renpy.sound.play("/audio/soun_fx/suck5.opus", channel="sfx2", loop=False, relative_volume = 1.1)
                                                                bot"As nice as your boobs are. what I truly want to taste..."
                                                                show screen parallax1280("hin_slip titgrope 8") with dissolve
                                                                bot"Is you [hin_rel]!" with vpunch
                                                                hin"*Regaining consciousness* ...A-ah... [bo_name_stutter]...?" with vpunch
                                                                show screen parallax1280("hin_slip titgrope 8_1") with dissolve
                                                                bot"F-fuck!" with vpunch
                                                                call hidescrollingimage from _call_hidescrollingimage_99
                                                                "Realizing [hin_name] was regaining her senses, you fall back trying to act innocent..."
                                                                show hin_slip lowerundress 0:
                                                                    yalign 1.0
                                                                show wakeup_overlay_face 1:
                                                                    yalign 1.0
                                                                show wakeup_overlay_tits 1:
                                                                    yalign 1.0
                                                                with dissolve
                                                                camera:
                                                                    easein 2 ypos -200                                                              
                                                                hin"...Ah... [bo_name_stutter]? W-what is..."
                                                                bo"Y-yes, [hin_rel_stutter]. It's me! C-come on, wake up..."
                                                                bot"S-shit! Her tits are still out!"
                                                                bot"Guess I'll have to blame the fall..."
                                                                bo"U-uhm, Y-you hit your head pretty hard. Are you okay?"
                                                                show wakeup_overlay_face 2 with dissolve
                                                                hin"M-my head? Oh r-right... I slipped, didn't I?"
                                                                show wakeup_overlay_face 3 with dissolve
                                                                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                                                                hin"T-the towel!" with vpunch
                                                                camera:
                                                                    reset
                                                                scene black
                                                                with vpunch
                                                                "[hin_name] quickly covered herself up upon realizing she was exposed right in front of you..."
                                                                hin"G-good lords! How l-long was I like that!" with vpunch
                                                                scene bg day:
                                                                    zoom 0.7
                                                                show boruto snob at left
                                                                show thina b1 at right:
                                                                    zoom 1.1
                                                                with dissolve
                                                                "What she didn't realize, is that you were responsible for it!"
                                                                bo"It's been a m-minute. I was t-trying to get you back to your senses..."
                                                                hin"T-thank you [bo_name]. I'll go lay down for a bit, okay? I still feel a bit light-headed..."
                                                                bo"N-no worries..."
                                                                hide thina with dissolve
                                                                call changeHatred(1) from _call_changeHatred_178
                                                                bot"Can't believe I am off the hook scot-free after sucking your titties! I should be thanking you instead [hin_rel]!"
                                                                scene black with dissolve
                                                                bot"Hehe! I should invest in more banana peels!"
                                                                jump action_taken
                                                                
                            

                                                            
                                                    "Play with your face!":
                                                        bot"It makes me want to use your face..."
                                                        show screen parallax1280("blackscreen") with dissolve
                                                        "You kneel down close to her face..."
                                                        $ renpy.sound.play("/audio/soun_fx/zipper.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                                        "*Unzip*" with vpunch
                                                        bot"I wonder how you'd look with..."
                                                        show screen parallax1280("hin_slip cockslap 1") with dissolve
                                                        bot"With my cock over your face!"
                                                        bot"Look at you [hin_rel]. Looking so serene..."
                                                        show screen parallax1280("hin_slip cockslap 1_1") with dissolve
                                                        bot"And yet this monster inside of me calls for me to defile you!" with vpunch
                                                        default cockslap_hinata_shower = 0
                                                        $ cockslap_hinata_shower = 0
                                                        menu cockslapmenu_hinshower1:
                                                            bot"And yet this monster inside of me calls for me to defile you!"
                                                            "{color=[hatredcolor]}Cock-slap her!{/color}" if cockslap_hinata_shower == 0:
                                                                bot"I might not be able to risk shoving my cock in your mouth just yet, but..."
                                                                $ renpy.sound.play("/audio/soun_fx/sexslaps2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                                                show screen parallax1280("hin_slip cockslap_anim1") with dissolve
                                                                bot"I can still have some fun with you!" with vpunch
                                                                bot"Look at how hard your pretty face gets me..."
                                                                bot"Consider this your punishment for blue-balling me with your existence [hin_rel]!"
                                                                $ cockslap_hinata_shower += 1
                                                                jump cockslapmenu_hinshower1

                                                            "{color=[hatredcolor]}Cock-slap her harder!{/color}" if cockslap_hinata_shower == 1:
                                                                bot"I just can't resist your pretty face, [hin_rel]!"
                                                                $ renpy.sound.play("/audio/soun_fx/sexslaps2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                                                show screen parallax1280("hin_slip cockslap_anim2") with dissolve
                                                                bot"You could easily be a top-tier whore! Instead, all you are good for is blue-balling me for all eternity..." with vpunch
                                                                bot"Consider this my payback..."
                                                                show screen parallax1280("hin_slip cockslap 1_3") with dissolve
                                                                bot"You fucking bi-" with vpunch
                                                                hin"W-what... is..."
                                                                bot"Oh s-shit, shit, shit, fuck, shit!" with vpunch
                                                                call hidescrollingimage("Click twice to hide the evidence!") from _call_hidescrollingimage_100
                                                                $ renpy.sound.play("/audio/soun_fx/zipper.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                                                "Realizing [hin_name] was regaining her senses, you quickly hide the evidence..."
                                                                show hin_slip lowerundress 0:
                                                                    yalign 1.0
                                                                show wakeup_overlay_face 1:
                                                                    yalign 1.0
                                                                with dissolve
                                                                camera:
                                                                    easein 2 ypos -200                                                              
                                                                hin"...Ah...Eh?...[bo_name_stutter]?"
                                                                bo"Y-yes, [hin_rel_stutter]. It's me! C-come on, wake up..."
                                                                bo"Y-you hit your head pretty hard..."
                                                                show wakeup_overlay_face 2 with dissolve
                                                                hin"M-my head? Oh r-right... I slipped, didn't I?"
                                                                bot"Close call! Think she hasn't realized I've been rubbing my cock on her face! Hehe..."
                                                                camera:
                                                                    reset
                                                                scene black
                                                                with dissolve
                                                                hin"Can you h-help me get on my feet?"
                                                                bo"Sure can!"
                                                                scene bg day:
                                                                    zoom 0.7
                                                                show boruto snob at left
                                                                show thina b1 at right:
                                                                    zoom 1.1
                                                                with dissolve
                                                                hin"Thank you, [bo_name]. I'll go lay down for a bit. I still feel a bit light-headed..."
                                                                bo"N-no worries..."
                                                                hide thina with dissolve
                                                                call changeHatred(1) from _call_changeHatred_179
                                                                bot"Can't believe I am off the hook scot-free! I should be thanking you instead [hin_rel]!"
                                                                jump action_taken

                                                            "{color=[hatredcolor]}???{/color}" if cockslap_hinata_shower ==1:
                                                                bot"Fuck! I want to do so much more to you [hin_rel]..."
                                                                bot"But risking it now would jeopardize my life... or my cock!"
                                                                bot"One day, I'll have my way with you. I swear it!"
                                                                jump cockslapmenu_hinshower1
                                                            "Your tits deserve some attention too!":
                                                                show screen parallax1280("blackscreen") with dissolve
                                                                $ renpy.sound.play("/audio/soun_fx/zipper.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                                                bot"I can still have some fun with you!"
                                                                jump tits_from_playface_label
                                            
                                            "You are just so damn pretty [hin_rel]!":
                                                call hidescrollingimage from _call_hidescrollingimage_101
                                                scene hin_slip lowerundress 0 with dissolve:
                                                    zoom 1.2 xalign 0.0 yalign 1.0
                                                show hin_slip:
                                                    easein 4 xalign 0.9 yalign 0.0
                                                bot"Even as you lay there..."
                                                bot"You are just so damn pretty [hin_rel]!"
                                                bot"Sometimes, I just get this urge to..."
                                                scene hin_slip lowerundress 0 with dissolve:
                                                    zoom 1.3 xalign 1.0 yalign 0.0
                                                bot"F-feel you, taste you..."
                                                bot"Maybe I could..."
                                                scene black
                                                $ renpy.sound.play("/audio/soun_fx/suck1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                                                show hin_slip kiss1:
                                                    fit "contain" xalign 0.5
                                                with dissolve
                                                bot"Give you the kiss of life!" with vpunch
                                                $ kissmenu1_hin1 = []
                                                menu kissmenu1_hin1_menu:
                                                    set kissmenu1_hin1
                                                    bot"Give you the kiss of life!"
                                                    "Lean in for a french kiss!":
                                                        pass
                                                    "Grope her":
                                                        $ renpy.sound.play("/audio/soun_fx/suck1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                                                        bot"I know it's wrong, but..."
                                                        show hin_slip kiss1_1 with dissolve
                                                        bot"I don't care!"
                                                        jump kissmenu1_hin1_menu

                                                bot"Your lips, your taste..."
                                                show hin_slip kiss2 with dissolve
                                                bot"Like lilac and roses. I need more..."
                                                show hin_slip kssing_anim1 with dissolve
                                                $ renpy.sound.play("/audio/soun_fx/suck3.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                                                "You lean in and slip your tongue in her..."
                                                bot"So what if we are [hin_rel_mother] and [hin_rel_to_bo]..."
                                                bot"Do my feelings for you not matter?"
                                                show hin_slip kiss3 with dissolve
                                                bot"Or is it just me lusting over y-you..."
                                                show hin_slip kiss3_1 with dissolve
                                                hin"*Heavy Breathing*... Ah..."
                                                bo"[hin_rel_stutter]!?" with vpunch
                                                show hin_slip kiss3_2 with dissolve
                                                hin"...[bo_name_stutter]? W-what is..."
                                                show hin_slip kiss3_3 with dissolve:
                                                    zoom 1.25 yalign 0.4 xalign 0.6
                                                hin"...H-happening?"
                                                scene black with vpunch
                                                "You quickly pull back, trying to act innocent..."
                                                bo"N-nothing! You just..."
                                                show hin_slip lowerundress 0:
                                                    yalign 0.0
                                                show wakeup_overlay_face 1:
                                                    yalign 0.0
                                 
                                                with dissolve
                                                camera:
                                                    easein 2 ypos -200                                                              
                                                bo"Had a small a-accident!"
                                                hin"A-accident? [bo_name_stutter]... is that you?"
                                                bo"Y-yes, [hin_rel_stutter]. It's me! C-come on, wake up..."
                                 
                                                bo"Y-you hit your head pretty hard. Are you okay?"
                                                show wakeup_overlay_face 2
                                                camera:
                                                    zoom 1.1 yalign 0 xalign 1.0
                                                with dissolve
                                                hin"M-my head? Oh r-right... I slipped, didn't I?"
                                                camera:
                                                    reset
                                                scene black
                                                hin"*Gasp*!" with vpunch
                                                "[hin_name] quickly covered herself up upon realizing she was almost exposed right in front of you..."
                                                hin"G-good lords! How l-long was I out for..." with vpunch
                                                scene bg day:
                                                    zoom 0.7
                                                show boruto surprised2 at left
                                                show thina b1 at right:
                                                    zoom 1.1
                                                with dissolve
                                                bo"It's been a m-minute. I was t-trying to get you back to your senses..."

                                                hin"T-thank you [bo_name]. I'll go lay down for a bit, okay? I still feel a bit light-headed..."
                                                bo"N-no worries..."
                                                hide thina with dissolve
                                                show boruto snob with dissolve

                                                bot"Can't believe I am off the hook scot-free after tongue kissing her! I should be thanking you instead [hin_rel]!"
                                                scene black with dissolve
                                                bot"Hehe! I should invest in more banana peels!"
                                                jump action_taken



                                            
                                    "{color=[lovecolor]}Carry her to her bedroom{/color}":# (supporter_scene = True)
                                        if strength >= 1:
                                            if quest_hin.exists("hin1L_1") and not _in_replay: #check if quest exists
                                                if quest_hin.is_state("hin1L_1", "pending"): #check quest state
                                                    
                                                    $ quest_hin.check("hin1L_1", "done")
                                                    $ notification (f"{hin_name} Love objective completed")
                                        jump carryhertoherbedroom
                                        # $ call_label_action("carryhertoherbedroom")
                                        call supp_rew from _call_supp_rew_11

                                        
                                        jump hin_slipped_menu2
                                        

                                                

                                    "Make your escape!":
                                        scene black with vpunch
                                        bot"I am out of here before I get in trouble!"
                                        jump action_taken
                                    

                            else:
                                call randomCheck(False,"She notices the banana peel!") from _call_randomCheck_4
                                show hin_bath:
                                    easein 0.4 yalign 1.0
                                hin"H-huh!?" with vpunch
                                scene black with vpunch
                                $ renpy.sound.play("/audio/soun_fx/woosh1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                "[hin_name] notices the banana peel, a second too late!"
                                $ renpy.sound.play("/audio/soun_fx/woosh4.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                show hin_bath bananaslip_fail1 with dissolve
                                "But even so, her reactions along with her athleticism, averted a catastrophe."
                                "She expertly sommersaulted over the hazardous peel."
                                scene black with vpunch
                                show hin_bath bananaslip_fail1_1 with dissolve:
                                    yalign 0.0
                                show hin_bath:
                                    easein 4 yalign 1.0
                                hin"Hya! *Exhales...* A discarded banana peel?" with vpunch
                                bot"I-impressive..."
                                hin"[bo_name]'s antics! I'll have to scold him about it later..."
                                show hin_bath:
                                    easein 0.3 zoom 1.3 yalign 0.7
                                bot"Why am I always the first one to blame!" with vpunch
                                hin"Then again, it could be [him_name]'s doing..."
                                bot"Yes, yes! Let's just blame her instead! Hehe..." with vpunch
                                call changeRespect("Hinata", -1) from _call_changeRespect_224
                                scene hin_bath bananaslip_fail1_1 with dissolve:
                                    yalign 1.0

                                hin"No. It's definitely [bo_name]'s!" with vpunch
                                scene black with dissolve
                                bot"Goddamn it..."
                                bot"Better make my exit before I get roasted!"
                                jump action_taken


                        "'Joke' about it":
                            bot"Is that how it feels to suck on a cock!?"
                            bot"How do girls even do it!" with vpunch
                            bot"*Sigh* I am losing my freaking mind..."
                            scene black with dissolve
                            $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                            scene hin_bath_waitexit with dissolve:
                                yalign 1.0
                            show hin_bath_waitexit:
                                easein 5 yalign 0.05
                            bot"[hin_rel]'s coming out!"
                            scene bg day:
                                zoom 0.7
                            show boruto normal at left
                            show thina thinking at right:
                                zoom 1.1
                            with dissolve
                            hin"Oh, [bo_name]! Were you sitting here waiting for me all this time?"
                            menu:
                                hin"Oh, [bo_name]! Were you sitting here waiting for me all this time?"
                                "{color=[obediencecolor]}Looking good, [hin_rel]!{/color}":
                                    show boruto snob with dissolve
                                    bo"Damn [hin_rel], you are looking good in just the towel!"
                                    if hinata_obedience >= 20:
                                        call checkObedience(20,"none","Hinata") from _call_checkObedience_31
                                        show thina annoyed with dissolve
                                        hin"[bo_name]! You can't just s-say that yo your [hin_rel_mother]!"
                                        bo"Why not? You are beautiful [hin_rel], what else am I supposed to say?"
                                        call changeObedience("Hinata", 1) from _call_changeObedience_136
                                        show thina shy with dissolve
                                        hin"M-maybe save the compliments for, you know... when you meet the one?"
                                        show boruto embarassed with dissolve
                                        bo"There's no room for another in my heart [hin_rel], you are the only one!"
                                        show thina b1 with dissolve
                                        hin"G-good grief! "
                                        show thina:
                                            easein 3 xpos -900
                                        hin"Even cheesier than your [na_rel]..."
                                        show boruto snob with dissolve
                                        bot"Thanks for the backside view, [hin_rel]!"
                                        hide boruto with dissolve
                                        $ hin_location = "afk"
                                        jump house
                                    else:
                                        call checkObedience(20,"none","Hinata") from _call_checkObedience_32
                                        show thina annoyed with dissolve
                                        hin"[bo_name]! That's inappropriate, and don't cuss!"
                                        show thina angry with dissolve
                                        call changeRespect("Hinata", -1) from _call_changeRespect_225
                                        bo"Just making an observation [hin_rel]..."
                                        show thina annoyed with dissolve
                                        show thina:
                                            easein 2 xpos -1100
                                        hin"Good lord, [bo_name]..."
                                        hide boruto with dissolve
                                        bo"Well, that's that!"
                                        $ hin_location = "afk"
                                        jump house


                                "You know how crucial this is, [hin_rel]!":
                                    show boruto worried with dissolve
                                    bo"You know how important this is [hin_rel], with my condition and all..."
                                    call changeRespect("Hinata", 1) from _call_changeRespect_226
                                    show thina thinking with dissolve
                                    hin"I know, I know. Thank you for patiently waiting for me..."
                                    show thina b1 with dissolve
                                    hin"I'll leave you to it, okay...?"
                                    show thina:
                                        easein 2 xpos -1100
                                    hin"Good lord, [bo_name]..."
                                    hide boruto with dissolve
                                    bot"..."
                                    $ hin_location = "afk"
                                    jump house

                                    
                                
                        

                "{color=[hatredcolor]}(Boruto sucks! I wish this fucker would die already!){/color}":
                    label clownending_boruto:
                    $ initialize_replay_defaults()
                    scene black with dissolve
                    show bg bathroom_banana1 with dissolve:
                        yalign 1.0 alpha 0.4
                    show bg:
                        easein 4 alpha 0.1 yalign 0.3
                    show boruto_banana 0 with dissolve:
                        fit "contain" xalign 0.5
                    bot"I've just had a crazy thought!"
                    bot"Can you believe people sit and watch shows they hate? Wasting precious time, just to shit on the main characters..."
                    bot"Burning daylight, all to type 'FIRST' and then 'This show is trash LMAO' on a forum..."
                    bot"I mean, who would do that. What are they, stupid?"
                    bot "Of course, If I ever had my own show, people would never do that to me. They'd be swooning over me instead! Hehe..."
                    bot "My merch would sell out faster than toilet paper during a pandemic!"
                    show boruto_banana 1 with dissolve:
                        fit "contain" xalign 0.5
                    
                    bot"Oh s-shit! The banana... it's stuck in my t-throat!" with vpunch
                    bot"W-what the fuck! It's lodged in there!"
                    bot"I can't... b-breathe..."
                    show boruto_banana 2 with dissolve
                    bot"M-Mother of all fillers! It's not... b-budging! This is NOT how the hero... goes... out!"
                    show boruto_banana with dissolve:
                        zoom 1.4 xalign 0.5 yalign 0.1
                    bot "Death by a banana... talk about... a-peeling..."
                    bot"I am the... greatest... ever!"
                    scene black with vpunch
                    $ renpy.sound.play("/audio/soun_fx/bodythud.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    "*Body Thuds*"
                    $ renpy.sound.play("/audio/soun_fx/yay.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                    dev"Boruto is dead, the actual show is cancelled, the world breathes a collective sigh of relief. Congratulations!"
                    dev"Crisis averted, the cosmos is saved. Yippee!"
                    dev "Oh shit, Oh dear! Wait a sec... holy smokes! His death episode just tripled our ratings! People are LOVING this!"
                    dev"Now please revive him, so I can redeem his shitty character sometime down the line..."
                    menu:
                        dev"Now please revive him, so I can redeem his shitty character sometime down the line..."
                        "Revive him":
                            bot"Fucking haters, I am telling you!"
                            $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                            scene black with dissolve:
                                fit "contain" xalign 0.5
                                matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
                            with Shake((0, 0, 0, 0), 1, dist=20, peak_time=0.8, smoothness=50)
                            show boruto_banana 0 at brightreveal:
                                fit "contain" xalign 0.5
                            with longerflash
                            bot"I've just had the weirdest dream ever."
                            bot"Where was I... Oh right, [hin_rel]!"
                            jump secretmenu_boruto_ending
                        "{color=[hatredcolor]}No! I hope he rots in anime hell!{/color}":
                            dev "At least we saved on animation budget! GG <3"
                            $ renpy.quit()
                        
                


        