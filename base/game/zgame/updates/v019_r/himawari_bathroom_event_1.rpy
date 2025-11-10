label hima_bathroom_event1:
    $ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    bo"Can you hurry up? I need to use the bathroom..."
    him"Piss off! I'll be done when I am done!" with vpunch
    scene bathroom door with dissolve:
        zoom 1.5 xalign 0.9 yalign 0.2
    menu:
        him"Piss off! I'll be done when I am done!"
        "{color=[obediencecolor]}This is important...{/color}":
            bo"This is important [him_name], it's about my diagnosis, remember? [hin_rel] talked to you about it..."
            label hima_bathroom_event1_replay:
            $ initialize_replay_defaults()
            scene black with vpunch
            $ renpy.sound.play("/audio/soun_fx/showering.opus", channel="sfx1", loop=True, relative_volume = 0.6)
            scene bathroom_hima showering
            show bathroom_curtains at transparency_cycle(0.9,1,4)
            show particleFog_low
            with dissolve
            him"What do you want me to do about that, stop showering midway? Weirdo..." with vpunch
            him"Just wait until I am done like a normal person would!"   
            stop sfx1 fadeout 2           
            scene bg day:
                zoom 0.7
            show boruto angry
            with dissolve
            bot"Damned brat..."
            bo"Can you at least hurry up? I am... dying out here!"
            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
            him"Hmph! Good riddance..." with vpunch
            scene black with dissolve
            "A few minutes pass..."
            $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            bot"Oh? She must be done!"
            show screen parallax1280("him_aftershower check1",1,0.4) with dissolve
            call showscrollingimage from _call_showscrollingimage_168
            him"W-what are you standing outside the door for, you weirdo!" with vpunch
            him"Move out the way!" with vpunch
            menu:
                him"Move out the way!"
                "{color=[obediencecolor]}How about you move out the way!{/color}":
                    default him_aftershower_pulltowel = False
                    default him_aftershower_pinchnipple = False
                    bo"How about you move out of the way, brat..."
                    him"You are the one blocking my way, stupid!" with vpunch
                    bo"I could say the same to you, you stuck up bit-"
                    him"I said..."
                    scene black
                    call hidescrollingimage from _call_hidescrollingimage_89
                    him"...M-move!" with vpunch
                    show him_aftershower start1 with dissolve:
                        fit "contain" xalign 0.5
                    him"Y-you... *Grrr* s-spiky haired retard!" with vpunch
                    if is_opportunity_unlocked("l0_opportunity3", strength):
                        call screen strength_minigame2("after_shower_him_win", "after_shower_him_lose", "him_aftershower start1", 0.55,False,strengthlevel)
                    else:
                        call screen strength_minigame2("after_shower_him_win", "after_shower_him_lose", "him_aftershower start1", 0.55,True,strengthlevel)
                    label after_shower_him_win:
                        $ is_opportunity_unlocked("l1_opportunity1", strength)
                        bo"Did you really think you could..."
                        default himawari_waitoutside = False
                        $ himawari_waitoutside = True
                        if hinata_slipped_banana == True and himawari_waitoutside == True: #complete wait outside quest
                            if quest.exists("bo_shower_1"):
                                if quest.is_state("bo_shower_1", "unlocked"):
                                    if quest.exists("shower1_3"):
                                        $ quest.check("shower1_3", "completed")
                                    $ quest.check("bo_shower_1", "done") #marks left quest as done (make sure any references now check if quest is completed to avoid errors)
                                    # $ quest.remove("Just a peek!") #remove from right page
                                    $ notification ("Quest Completed: Just a peek...")
                        menu him_aftershower_overpowert:
                            bo"Did you really think you could..."
                            "Let her 'win'":
                                bo"...you could win?"
                                him"Hmph! Y-you are s-so... w-weak! *Pushes harder*" with vpunch
                                $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                show him_aftershower fight1 with dissolve:
                                    fit "contain" xalign 0.5
                                "[him_name]'s towel slowly slid off while she helplessly kept trying to push you away!"
                                bo"O-oh? Y-you are trying so hard it seems..."
                                bot"N-nice nips, lil [him_rel]!"
                                him"I am n-not... even... t-trying!" with vpunch
                                bo"Is that why your-"
                                $ renpy.sound.play("/audio/soun_fx/himawari/himagasp.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                                show him_aftershower fight1_win1 with dissolve:
                                    fit "contain" xalign 0.5
                                him"*Gasps*!"
                                show him_aftershower fight1_win1_1 with dissolve:
                                    fit "contain" xalign 0.5
                                bo"Cute effort, [him_name]..."
                                call changeObedience("Himawari", 1) from _call_changeObedience_132
                                him"S-screw you, loser! Why are you even looking t-there..." with vpunch
                                bo"I really wasn't, you are just a bit short..."
                                scene black with vpunch
                                him"You w-were looking! I saw your eyes!"
                                $ renpy.sound.play("/audio/soun_fx/punch.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                bo"Awww! *Cries of Agony*" with vpunch
                                "In your moment of distraction, [him_name] opportunistically unleashed her special move on you..."
                                jump aftershower_kickballs

                            "{color=[dominancecolor]}Overpower her!{/color}":
                                call checkDominance(15,"him_aftershower_overpowert") from _call_checkDominance_44
                                show him_aftershower fight2 with dissolve:
                                    fit "contain" xalign 0.5
                                bo"...Overpower me? I could pick you up like a child if I wanted to!" with vpunch
                                scene black
                                show him_aftershower fight3:
                                    xalign 0.5 zoom 1 yalign 0.8
                                with dissolve
                                him"*Exerts force* Hnmmmm!! I am n-not... even... t-trying!" with vpunch
                                bot"Her towel is slipping off. Her little nipples are peeking through!"
                                bo"Oh y-yeah? Sure looks like you a-are!"
                                menu him_aftershower_overpowert2:
                                    bo"Oh y-yeah? Sure looks like you a-are!"
                                    "'Tickle' her...":
                                        bo"You are so weak [him_name]! Look..." with vpunch
                                        $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 1.2)
                                        show him_aftershower grope_anim1 with dissolve
                                        bo"...I can even tickle you even as you are trying to push me away! Hehe..."
                                        him"W-where... *Grr* do you t-think... y-you are *Exerts force*!" with vpunch
                                        bot"N-nice little boobies, you brat! T-they are quite n-nice, reall-"
                                        scene black
                                        $ renpy.sound.play("/audio/soun_fx/punch.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                        bo"Awww! *Cries of Agony*" with vpunch
                                        "In your moment of distraction, [him_name] opportunistically unleashed her special move on you..."
                                        jump aftershower_kickballs
                                    "{color=[hatredcolor]}Pinch her nipple!{/color}":
                                        $ him_aftershower_pinchnipple = True
                                        bo"Your feeble attempts to push me off has exposed your weakness!"
                                        him"W-what the hell... *Grr* a-are you talking about! *Exerts force!*" with vpunch
                                        show him_aftershower fight4 with dissolve
                                        bo"Special move, nipple twister!"
                                        him"*Gasps!* W-what-" with vpunch
                                        show him_aftershower fight4_1 with dissolve
                                        call changeHatred(1) from _call_changeHatred_169
                                        bo"H-how's that feel, you bitch!" with vpunch
                                        scene black
                                        $ renpy.sound.play("/audio/soun_fx/punch.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                        bo"Aw-ouch! *Cries of Agony*" with vpunch
                                        "In your moment of distraction, [him_name] opportunistically unleashed her special move on you..."
                                        call changeRespect("Himawari", -2) from _call_changeRespect_215
                                        him"W-what the hell do you think you are doing, you retard! D-don't touch me there..."
                                        jump aftershower_kickballs
                                    "{color=[dominancecolor]}Pull the towel down!{/color}":
                                        call checkDominance(20,"him_aftershower_overpowert2") from _call_checkDominance_45
                                        
                                        $ him_aftershower_pulltowel = True
                                        bo"Your feeble attempts to push me off has exposed your weakness!"
                                        him"W-what the hell... *Grr* a-are you talking about! *Exerts force!*" with vpunch
                                        bo"You haven't realized yet, have you? Your towel..."
                                        him"H-huh?"
                                        show him_aftershower hate1 with dissolve:
                                            yalign 0.9
                                        pause 0.3
                                        show him_aftershower fight5 with dissolve
                                        call changeDominance(1) from _call_changeDominance_118
                                        $ renpy.sound.play("/audio/soun_fx/himawari/himagasp.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                                        him"*Gasps!*"
                                        bo"You've been flaunting your non-existent boobies for some time now!" with vpunch
                                        
                                        menu:
                                            him"*Gasps!*"
                                            "Expose her fully!":
                                                pass
                                        bo"If you are going to run around naked, then do it properly!" with vpunch
                                        scene black
                                        $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                        show him_aftershower hate2 with fade:
                                            xalign 0.5 zoom 1.4 yalign 0.85
                                        pause 0.5
                                        "In one swift movement, you pull down her towel and cop a feel of her breasts..."
                                        scene black
                                        $ renpy.sound.play("/audio/soun_fx/punch.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                        bo"Awww! *Cries of Agony*" with vpunch
                                        call changeRespect("Himawari", -1) from _call_changeRespect_216
                                        "In your moment of distraction, [him_name] opportunistically unleashed her special move on you..."
                                        show him_aftershower hate3 with dissolve:
                                            xalign 0.5 zoom 1.1 yalign 1.0
                                        show him_aftershower:
                                            easein 4 yalign 0.2
                                        him"W-w-w--why would you do that, y-you..."
                                        show him_aftershower with dissolve:
                                            xalign 0.5 fit "contain"
                                        him"Y-y-y-y-you..."
                                        show him_aftershower fight1_win1_1 with dissolve:
                                            xalign 0.5 zoom 1.1 yalign 0.2
                                        call changeObedience("Himawari",1) from _call_changeObedience_133
                                        him"Y-YOU FREAKING PERVERT!" with vpunch
                                        bo"*Groans in Pain*"
                                        jump aftershower_kickballs
                                        
                                        
                          

                                

                            

                    label after_shower_him_lose:
                        "Her sudden outburst pushed you off-balance!"
                        bo"W-why you..."
                        scene black with vpunch
                        $ renpy.sound.play("/audio/soun_fx/punch.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                        him"Take t-that!" with vpunch
                        "[him_name] took the chance to surprise you with her special move!"
                        call changeRespect("Himawari", -1) from _call_changeRespect_217
                        him"I can't believe you are such a weakling!" with vpunch
                        jump aftershower_kickballs



                    

                "{color=[obediencecolor]}Yes, your grace...! (Prank){/color}":
                    bot"This little brat..."
                    bo"Yes, your grace! I shall make way for you..."
                    scene black
                    call hidescrollingimage("Click twice to move out of her way...") from _call_hidescrollingimage_90
                    scene black
                    bot"But you see, I have something in store for you!"
                    show him_aftershower movedaway with dissolve:
                        fit "contain" xalign 0.5
                    $ renpy.sound.play("/audio/soun_fx/himawari/himascoff1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                    him"Hmph! You should start addressing me like that more often..." with vpunch
                    bo"Oh...? You think you are royalty now?"
                    scene black
                    show him_aftershower moveover1_1:
                        yalign 1.0
                    with dissolve
                    show him_aftershower:
                        easein 5 yalign 0.0 xalign 0.5
                    him"In contrast to a peasant like you, I could very well be a princess!"
                    show him_aftershower moveover1_1 with dissolve:
                        fit "contain" xalign 0.5
                    "You let [him_name] walk past you, but as she turned her back on you..."
                    menu randommenu_him23487:
                        "You let [him_name] walk past you, but as she turned her back on you..."
                        "{color=[hatredcolor]}Pull down her towel!{/color}":
                            scene black with dissolve
                            "...You sneakily approached from behind!"
                            show him_aftershower prank1 with dissolve:
                                fit "contain" xalign 0.5
                            bo"A peasant, am I?"
                            show him_aftershower prank1_1 with dissolve
                            $ renpy.sound.play("/audio/soun_fx/himawari/himagasp3.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                            him"*Gasps!*" with vpunch
                            call changeHatred(1) from _call_changeHatred_170
                            bo"Does royalty expose themselves in front of peasants, you whore?" with vpunch
                            scene black with vpunch
                            "[him_name] bend her knees in a flustered manner, and quickly raised her towel back up..."
                            show him_aftershower prank2 with dissolve:
                                yalign 1.0
                            show him_aftershower prank2:
                                easein 4 yalign 0.1
                            
                            him"I am t-telling [hin_rel]!" with vpunch
                            show him_aftershower prank2_1 with dissolve:
                                fit "contain" xalign 0.5
                            call changeRespect("Himawari", -2) from _call_changeRespect_218
                            him"S-stupid perv!" with vpunch
                            bo"Who cares! It was just a prank..."
                            scene black with vpunch
                            $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            "[him_name] walked away embarrassed, and locked herself in her bedroom."
                            bot"Serves you right!"
                            jump action_taken
                        "{color=[obediencecolor]}Playfully spank her!{/color}":
                            call checkObedience(10,"randommenu_him23487","Himawari") from _call_checkObedience_28
                            show him_aftershower:
                                xalign 1.0
                            show moveover_look_down 0:
                                zoom 0.53 xalign 0.0 yalign 0.0
                            with dissolve
                            bo"So dismissive, princess..."
                            show moveover_look_down 1
                            scene moveover 0_1:
                                zoom 1.6 xalign 0.0 yalign 0.8
                            with dissolve
                            $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx2", loop=False, relative_volume = 1)
                            "You gently pat her behind as she was walking past you!" with vpunch
                            show moveover_look_down 1 with dissolve:
                                xalign 1.0 fit "contain"

                            call increaselust(10) from _call_increaselust_247
                            scene black
                            show moveover_look_down 2:
                                zoom 0.53 xalign 0.0 yalign 0.0
                            with dissolve
                            bo"Could show a little appreciation to your humble servant, you know..."
                            show him_aftershower moveover1:
                                xalign 1.0 fit "contain"
                            show moveover_look_down:
                                alpha 0.2
                            with dissolve
                            "She quickly pushed your hand away..."
                            call changeObedience("Himawari", 1) from _call_changeObedience_134
                            him"D-don't touch my behind, you p-pervy peasant!" with vpunch
                            bo"Aww, look at you all flustered! You are so cute... princess!"
                            scene black with vpunch
                            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                            him"Hmph!" with vpunch
                            $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                            "[him_name] ran away in a flustered manner!"
                            bot"Her cute little tough act isn't going to last long..."
                            jump action_taken
                            
                            
                        

                "Thanks for not taking too long!":
                    bo"Okay, tigress..."
                    scene black
                    call hidescrollingimage("Click twice to move out of her way.") from _call_hidescrollingimage_91
                    scene black
                    "You make way for her..."
                    show him_aftershower movedaway with dissolve:
                        fit "contain" xalign 0.5
                    $ renpy.sound.play("/audio/soun_fx/himawari/himascoff1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                    him"Hmph!" with vpunch
                    bo"Thanks for not taking too long, I was struggling out here you know..."
                    scene black
                    show him_aftershower moveover1_1:
                        yalign 1.0
                    with dissolve
                    show him_aftershower:
                        easein 5 yalign 0.0 xalign 0.5
                    him"And why would I care..."
                    show him_aftershower moveover1_1 with dissolve:
                        fit "contain" xalign 0.5
                    call changeRespect("Himawari", 1) from _call_changeRespect_219
                    him"At least you aren't being a weirdo about it this time..."
                    scene black with vpunch
                    $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                    him"Teehee!" with vpunch
                    "[him_name] runs away with a teasing look on her face."
                    bo"Little rascal..."
                    $ him_location = "afk"
                    jump house
                    
                


            


        "Fine, I'll wait.":
            bo"Fine, I'll wait..."
            him"Hmph! You better not be waiting for me outside!" with vpunch
            call showUIhouse from _call_showUIhouse_73
            $ ui.interact()





label aftershower_kickballs:
    scene black
    show him_aftershower defeated1:
        fit "contain" xalign 0.5
    with dissolve
    bo"*Groans* Aargh! Don't just... kick m-my balls! *Wheezing*"

    if him_aftershower_pulltowel:
        $ him_aftershower_pulltowel = False
        default him_aftershower_pulltowel_talk = False
        $ him_aftershower_pulltowel_talk = True
        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
        him"Hmph! Y-you deserved that for trying to e-expose me! F-freaking weirdo! Also, your fault for being a weakling in the first place..." with vpunch
    elif him_aftershower_pinchnipple:
        default him_aftershower_pinchnipple_talk = False
        $ him_aftershower_pinchnipple_talk = True
        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
        him"Hmph! Y-you deserved that! Next time you try that I'll twist your t-thing off instead! F-freaking weirdo! Also, your fault for being a weakling in the first place..." with vpunch
    else:

        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
        show him_aftershower defeated1_1 with dissolve:
            zoom 1.25 yalign 0.0
        him"Hmph! Maybe don't be an asshole in the first place! Also, your fault for being a weakling." with vpunch
    show him_aftershower:
        easein 1 yalign 1.0
    bo"Y-you... *Wheezing* b-bitch..."
    show him_aftershower:
        easein 1 yalign 0.0
    him"How comes you are still in my way, even while you are wheezing like a fish on the floor?"
    show him_aftershower:
        easein 3 yalign 1.0
    bo"S-screw you... *Wheezing*"
    scene black
    show him_aftershower 1:
        zoom 1.25 xalign 0.5 yalign 1.0
    with dissolve
    show him_aftershower:
        easein 5 yalign 0.0
    him"Guess I'll have to walk over you! Loser..."
    show screen parallax1280("him_aftershower 1", 1.25, 1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_169
    call increaselust(10) from _call_increaselust_248
    bo"Aww-ouch! *Groans* Y-you bitch..." with vpunch
    menu:
        bo"Aww-ouch! *Groans* Y-you bitch..."
        "Admit defeat...":
            bo"*Groans* I s-surrender! S-step... off my b-balls, you demon!" with vpunch
            him"Only if you beg first, loser! *Teehee*" with vpunch
            bo"P-please... It h-hurts! You'll castrate me you f-fiend!"
            show him_aftershower 1:
                zoom 1.3, xalign 0.5 yalign 1.0
            call hidescrollingimage from _call_hidescrollingimage_92

            $ renpy.sound.play("/audio/soun_fx/grope2.opus", channel="sfx3", loop=False, relative_volume = 0.9)
            him"I don't even know what that means, but I am having fun!" with vpunch
            "She violently twists her feet one last time, before letting you off the hook!"
            bo"A-argh! *Painful Groans*" with vpunch
            him"But since you said 'please', I'll let you off the hook, this time..."
            scene black with vpunch
            him"Teehee!"
            show him_aftershower moveover1_1 with dissolve:
                zoom 1.25 yalign 1.0
            show him_aftershower:
                easein 4 yalign 0.0
            him"Know your place, bozo!"
            him"Next time I catch you being weird, I'll do even worse!" with vpunch
            scene black with dissolve
            bot"I can't feel m-my balls..."
            jump action_taken


        "(This is kinda hot!)":
            bot"F-fuck! Why does being stepped on like this f-feel nice!?"
            call increaselust(10) from _call_increaselust_249
            bo"*Groans* S-step off my b-balls, you demon!" with vpunch
            hide screen parallax1280
            show screen parallax1280("him_aftershower 1", 1.3, 1.0)
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/grope2.opus", channel="sfx3", loop=False, relative_volume = 0.9)
            bo"A-argh! *Painful Groans*" with vpunch
            "She violently twists her feet on your groin, as if it make it even more painful..."
            him"Shut your damn trap, loser!" with vpunch
            bot"Your ball kick almost p-paralyzed me, but I can still use my mouth!"
            $ renpy.sound.play("/audio/soun_fx/suck3.opus", channel="sfx3", loop=False, relative_volume = 0.9)
            hide screen parallax1280
            show screen parallax1280("him_aftershower 1_1", 1.3, 1.0)
            with dissolve
            bot"If you are gonna shove your feet in my face, then I might as well get a taste!"
            him"W-what the..." with vpunch
            hide screen parallax1280
            show screen parallax1280("him_aftershower 1_2", 1.35, 1.0)
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/suck6.opus", channel="sfx3", loop=False, relative_volume = 0.9)
            "She pushed your head back by shoving her front foot forwards. You opportunistically pushed your tongue between her toes!" with dissolve
            him"A-are you trying to bite me, you w-weirdo!?" with vpunch
            call increaselust(10) from _call_increaselust_250
            bot"F-fuck! She is smashing my cock with her bare feet!"
            bot"I am g-getting a massive erection! S-she must be feeling it pressing against her sole!"
            show screen parallax1280("him_aftershower 2", 1.25, 1.0) with dissolve
            "She took a step forward..."
            him"Disgusting...You r-really are hopeless!" with vpunch
            hide screen parallax1280
            show screen parallax1280("him_aftershower 3", 1.25, 1.0)
            with dissolve
            "...And another"
            hide screen parallax1280
            show screen parallax1280("him_aftershower 3", 1.25, 0.0)
            with dissolve
            "You caught a glimpse of her womanhood, but the view was heavily obscured by her foot, as she was stepping off your face."
            scene black
            call hidescrollingimage from _call_hidescrollingimage_93
            him"Now stay down where you belong, insect!" with vpunch
            menu:
                him"Now stay down where you belong, insect!"
                "Reach for another degenerate taste!":
                    bot"I think I am sick in the head... I need more!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    show him_aftershower 4 with dissolve:
                        zoom 1.25 yalign 1.0 xalign 0.5
                    him"W-what the... What's with this slimy f-feeling!" with vpunch

                    show him_aftershower 4 with dissolve:
                        zoom 1.25 yalign 0.0 xalign 0.5
                    call changeRespect("Himawari", -2) from _call_changeRespect_220
                    him"W-what are you trying to do, you freak!" with vpunch
                    scene black with vpunch
                    $ renpy.sound.play("/audio/soun_fx/punch.opus", channel="sfx2", loop=False, relative_volume = 0.2)
                    "A kick to the face sets your lights out!"
                    show him_aftershower moveover1 with dissolve:
                        zoom 1.25 yalign 1.0 xalign 0.5

                    him"T-that'll teach you! Freaking w-weirdo..."
                    bot"...W-worth it! *Faints*"
                    jump action_taken


                "Concede":
                    show him_aftershower moveover1_1 with dissolve:
                        zoom 1.25 yalign 1.0
                    show him_aftershower:
                        easein 4 yalign 0.0
                    him"Next time I catch you being weird, I'll do even worse!" with vpunch
                    scene black with dissolve
                    bot"I can't feel m-my balls..."
                    jump action_taken
                




        