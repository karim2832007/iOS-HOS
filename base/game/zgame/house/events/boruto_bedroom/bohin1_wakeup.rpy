

default unlock_wakeuphjeventoption = False #Hinata's Hospitality quest completion check to unlock hj event
default laundryquestadded_1 = False # used right below to handle adding the quest the first time
default laundryquestcompleted_1 = False # will be marked true when quest is finished. Handles menu options in events_laundryroom.rpy


label bohin_1:

    if quest.exists("bohin_1"):
        if quest.is_state("bohin_1", "done"):
            $ unlock_wakeuphjeventoption = True

    # Random v0.21 wakeup handjob love path entry
    if chosen_love_path and hatredlevel2_handjobcounter >=4 and percentage>=50:
        $ rand_num = renpy.random.random()
        if rand_num < 0.5:
            jump v21_hinatawakeup_handjob
    
    if laundryquestadded_1 == True:
            jump wakeupquest
    else:
        $ hin_location = "laundryroom"
        $ laundryquestadded_1 = True
        $ notification("Quest discovered")
        $ quest.check("bohin_1", "unlocked")
        $ quest.add([
            Quest("bohin1_1", ("Look for [hin_name] in the laundry room"), ("[hin_name]'s hospitality"), ("in progress")), #completes when visintg laundry room first time
            Quest("bohin1_2", ("Let [hin_name] wake you up a few times"), ("[hin_name]'s hospitality"), ("pending")),      #completes when interacting 4 times in either love/hate options when hinata wakes you up and selecting 'enjoy the sight'
            Quest("bohin1_3", ("Find ways to express your 'gratitude'"), ("[hin_name]'s hospitality"), ("pending")),       #completes when final cum on love/hatred path
        ])

        jump wakeupquest


default bohin1_love_statcounter = 0 #counter that needs to reach 4
default bohin1_hatred_statcounter = 0 #counter that needs to reach 4
default bohin1_lovepath = False  # after interact 4 times with hinata when waking up, unlocks path
default bohin1_hatredpath = False  # after interact 4 times with hinata when waking up, unlocks path
default bohin2completion = False  #updates quest once bohin1_2 is done

default bohin1_3_laundrytalked = 0 #if talked with hinata in laundry about moring jackoffs
default bohin1_3_hinatacoerced = False #if coerced hinata in hatredpath
default hin_vulnerable_bohin1 = False  # changes laundry interactions and should reset on action_taken
default hin_broken_bohin1 = False      # changes laundry interactions and should reset on action_taken

label wakeupquest:
    if wakeupquestinitiated == True:
        scene black
        scene bg day with dissolve:
            zoom 0.70
        show screen topleftbuttons
        call screen housemap
    $ hin_location = "laundryroom"
    $ boruto_location = "borutobedroom"
    default wakeupquestinitiated = False
    $ wakeupquestinitiated = True
    bot"ZzZz"
    show eyeclosed
    show hinaq1bg behind eyeclosed:
        blur 6
    show hina quest1_1t behind eyeclosed with dissolve:
        blur 6
    show bobedx 3:
        matrixtransform ScaleMatrix(1.0, 0.6, 1.0)*OffsetMatrix(1.0, 238.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
        alpha 1
    call blink("...Is that", hin_rel + "...?","She is just cleaning around it seems...") from _call_blink
    show hina quest1_1t:
        blur 0
    show hinaq1bg:
        blur 0
    with dissolve
    
    call increaselust(10) from _call_increaselust_3
    show bobedx 3 with dissolve:
        alpha 0.20
    
    default wakeup_repeat = 0
    if wakeup_repeat == 0:
        bot"Even the sight of her cleaning is enough to... excite me."
    elif wakeup_repeat == 1:
        bot"I can't believe this is arousing..."
    elif wakeup_repeat ==2:
        bot"Do I really find my [hin_rel] arousing..."
    elif wakeup_repeat >=3:
        bot"[hin_rel] is really making me horny..."
    if wakeup_repeat == 0:
        bot"Either I am the world's biggest pervert or this condition of mine is more potent than I realized..."
    $ wakeup_repeat += 1

    # Notification guiding player to hatred level 2 advancement event #
    if day_number>=14 and chosen_hate_path == True and bohin1_hatredpath == True and quest.is_state("bohin_1", "done") and hatred.level == 1:
        $ notification("New repayment option available for 'You woke me up!'")
    if day_number>=14 and chosen_love_path == True and bohin1_lovepath == True and quest.is_state("bohin_1", "done") and hatredlevel2_handjobcounter == 0:
        $ notification("New help option available for 'Good Morning'")
    ####---------------------------------------------------------------

    menu wakeupmenu:
        #-----------------------------------------------------------------------------
        #complete bohin1_2 and advance to bohin1_3 when love/hatred path complete
        bot"..."
        "{color=[lovecolor]}'Enjoy' the sight{/color}" if bohin1_lovepath == True:
            if bohin2completion == False:
                $ quest.check("bohin1_2", "completed")
                $ quest.check("bohin1_3", "in progress")
                $ notification("Quest updated")
                $ bohin2completion = True
            jump bohin1_lovepath
        "{color=[hatredcolor]}'Enjoy' the sight{/color}" if bohin1_hatredpath == True:
            if bohin2completion == False:
                $ quest.check("bohin1_2", "completed")
                $ quest.check("bohin1_3", "in progress")
                $ notification("Quest updated")
                $ bohin2completion = True
            jump bohin1_hatredpath
            #-----------------------------------------------------------------------------

        "Enjoy the sight" if bohin1_hatredpath == False and bohin1_lovepath == False:
            #repeatable
            default wakeupmenu_repeat = 0
   
            if wakeupmenu_repeat == 0:
                bot"But can you blame me?"
            elif wakeupmenu_repeat >= 1:
                bot"I can't get enough of her swaying around."
            
            scene black with dissolve
            show blackscreen zorder 101
            show hinaq1bg
            show hina_quest_animation
            show bobedx 3 zorder 100:
                matrixtransform ScaleMatrix(1.0, 0.6, 1.0)*OffsetMatrix(1.0, 238.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
                alpha 0.20
            pause 1
            hide blackscreen with dissolve
            bot"I mean... look at that ass."
            call increaselust(10) from _call_increaselust_4


            #repeatable
            if wakeupmenu_repeat == 0:
                bot"She is just picking up things and tidying my bedroom..."
            elif wakeupmenu_repeat >= 1:
                bot"Watching her move around is... kinda sexy!"
            #----
            bot"I am almost mesmerized by her simple movements..."
            if wakeupmenu_repeat == 0:
                bot"Every step she takes sends visible ripples down her body. Her tight yoga pants don't help much in hiding those."
                bot"I bet she wears those cause they are comfy... She has no Idea I find them sexy!"
            
            #repeatable
            hide hina_quest_animation
            show hina quest1_3t:
                xpos 0
            with dissolve
            bot"Damn..."
 
            if wakeupmenu_repeat == 0:
                bot"She keeps letting her sweater slide down."
            elif wakeupmenu_repeat == 1:
                bot "She is so careless with that sweater of hers..."
            elif wakeupmenu_repeat ==2:
                bot"So careless [hin_rel]. I Wonder if one day I'll see what you are so desperately hiding under there"
            elif wakeupmenu_repeat >=3:
                bot"Such a sexy back..."
            #----
            call increaselust(10) from _call_increaselust_5
            call checkLust(90) from _call_checkLust
            if percentage >=90:
                default bohin1_nopath_cum = 0
                $ bohin1_nopath_cum += 1
                bot"I can't take this anymore. I 'll just rub one out under the sheets."
                show bobedx 5 with dissolve:
                    alpha 1.0
                bot"If I am careful she won't know a thing!"
                show bobedx 6 with dissolve
                bot"Come on [hin_rel]! Put on a show for me..."
                show bobedx 6:
                    alpha 0.15
                show hina_quest_animation
                $ renpy.pause(1.2, hard=True)
                hide hina quest1_3t
                with dissolve
                bot"My god [hin_rel]..."
                bot"You have no idea the effect you have on me!"
                if secretscenelovehandjob == True:
                    bot"I still remember that day when you stroked me dry in the bathroom..."
                if introhatredplan == True:
                    bot"What I'd give to cum all over you, just like the other night when I sneaked into your room..."
                bot"I need to feel more of you..."
                bot"I yearn for your touch... your affection!"
                hide hina_quest_animation
                show hina quest2_1:
                    xzoom -1
                with dissolve
                bot"O-oh yes [hin_rel]!" with vpunch
                bot"Stay bend over, just like that..." with flash
                with flash
                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show bobedx cum1 with dissolve:
                    alpha 1
                call decreaselust(50) from _call_decreaselust
                bot"Hnnnhggg"
                show bobedx cum2:
                    alpha 1
                $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                with longerflash
                show hina quest2_2 with dissolve:
                    xzoom 1
                call decreaselust(50) from _call_decreaselust_1
                bo"*Moans*"
                bot"F-fuck!... I let out a moan!" with vpunch
                show hinaq1bg 2
                show hina quest3_final
                with dissolve
                hin"[bo_name_stutter]? You were awake?"
                show bobedx cum2 with dissolve:
                    alpha 0.15
                bo"...Uuuh"
                menu:
                    bo"...Uuuh"
                    "Just woke up, don't mind me!":
                        bo"Just woke up! Don't m-mind me..."
                        hin"Oh good! Thought I made too much noise and woke you up..."
                        bo"Not at all..."
                    "...Did you hear that?":
                        bo"D-did you hear that [hin_rel]!?"
                        if bohin1_nopath_cum ==1:
                            hin"Hear... what?"
                            bo"N-nevermind... I was having a nightmare of sorts, thought I let out weird noises..."
                            hin"Oh that? Don't worry! You used to speak to yourself in your sleep ever since you were a little kid! I don't pay much attention to it!"
                            bo"O-oh..."
                            bot"Well, that's one way to get out of it. Lucky me..."
                        else:
                            hin"You mean your typical sleep noises?"
                            hin"I told you last time, I don't pay much attention to that, you tend to speak to yourself while you sleep after all!"
                            bo"Y-yeah..."
                    "Just woke up! And to what a beautiful sight!":
                        if bohin1_nopath_cum == 1:
                            bo"Just woke up... And to such a beautiful sight too!"
                            hin"Come on [bo_name]! S-stop it with the cheesy lines. *Giggles*"
                            hin"I'll let you in on a secret. A well timed compliment can win a girl's heart... But dish them out too often and she'll quickly lose interest!"
                            show bobedx cum2 with dissolve:
                                alpha 1
                            bot"If only you knew my secret [hin_rel]..."
                            show bobedx cum2 with dissolve:
                                alpha 0.15
                            bo"Huh... Noted!"
                        else:
                            bo"Another day, another sunrise of waking up to my beautiful [hin_rel]!"
                            hin"*Giggles* Remember what I said about handing out compliments? Careful , [bo_name]!"
                            bo"Yes ma'am..."

                        
                hin"I was just leaving anyway..."
                hin"Just have to pick the laundry up and..."
                hide hina quest3_final
                show bobedx cum2:
                    alpha 1
                with dissolve
                hin"Off I go!"

                if bohin1_nopath_cum == 1:
                    bot"Fuck me! That was hot... she has no idea I came watching her move around her ass like that!"
                    bot"It was like my own private show..."
                    bot"I should change into some clean underwear, my boxers are soaked in my cum..."
                else:
                    bot"I can't stop masturbating while I am watching my [hin_rel]... She is just so hot!"
                    bot"My boxers are soaked again. Maybe I can do something about that..."
                scene black with dissolve
                $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                jump wakeupend
                    

                



            else:

                if wakeupmenu_repeat == 0:
                    bot"I would rub one out right now if I was horny enough!"
                elif wakeupmenu_repeat == 1:
                    bot "I am just about ready to rub one out under the sheets..."
                elif wakeupmenu_repeat >=2:
                    bot"Fuck me! I am getting the urge to stroke it under the bedsheets! She'd have no idea anyway..."

            hide hina quest1_3t
            hide hina_quest_animation
            show hina quest1_2t:
                xpos -50
            with dissolve

            if wakeupmenu_repeat == 0:
                bot"Fuck! She noticed and pulled it up..."
            elif wakeupmenu_repeat == 1:
                bot"Too bad she noticed and pulled it up..."
            elif wakeupmenu_repeat >=2:
                bot"Come on...! Next time let it drop all the way [hin_rel]"
            #---
            bot"Fun's over I suppose..."
            show hina quest1_4t with dissolve:
                zoom 1.1 xpos -100 ypos -50

            if wakeupmenu_repeat == 0:
                hin"Oh, did I wake you up? Sorry about that!"
            elif wakeupmenu_repeat >= 1:
                hin"Oh! Did I wake you up again? My apologies!"
            #---

            if wakeupmenu_repeat == 0:
                bo"Hey [hin_rel], I was just about to wake up anyway, don't worry about it."
            elif wakeupmenu_repeat >= 1:
                bo"I am getting used to it by now, don't worry about it."
            #----
            show hinaq1bg 2
            show hina quest3_final
            with dissolve
     
            if wakeupmenu_repeat == 0:
                hin "I am just picking up the laundry and I'll give you some space."
            elif wakeupmenu_repeat >= 1:
                hin "Right, I'll pick up the laundry and get out of your hair."
            #---
            hin"Wouldn't want to see anything I shouldn't!"
            bo"Yeah... Thanks [hin_rel]."
            hide hina with dissolve
            show bobedx with dissolve:
                alpha 1
            bot"God-damn it [hin_rel]... All I am thinking about lately is you."
            hide bobedx
            show bobedx 4:
                alpha 1
            with dissolve
            bot"I need some sort of release, otherwise I risk going fucking crazy..."
            bot"I'll have to see if there's a way I can take things further..."
            
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            "You put on some clothes and get up..."
            $ wakeupmenu_repeat += 1

        "{color=[lovecolor]}'Good morning'{/color}" if bohin1_hatredpath == False:
            default goodmorning_repeat = 0
            # scene black with dissolve
            show hinaq1bg
            show hina quest1_4t with dissolve

            if goodmorning_repeat == 0:
                bo"Good morning [hin_rel]..."
            elif goodmorning_repeat >= 1:
                bo"Morning, [hin_rel]..."
            #---


            if goodmorning_repeat == 0:
                hin "Oh, Good morning! I tried being quiet to not wake you up, sorry about that."
            elif goodmorning_repeat == 1:
                hin "Oh, Good morning! Did I wake you up again? Sorry about that!"
            elif goodmorning_repeat >=2:
                hin "Oh, Good morning! Did I wake you up again? Silly me!"
            #----
            $ goodmorning_repeat += 1
            menu wakeupcompliment:
                "..."
                "Compliment her":
                    default wakeupcompliment_repeat = 0
       
                    if wakeupcompliment_repeat == 0:
                        bo"Don't worry about it, Besides... What better way to wake up with you in my sights."
                        bo"Thanks for cleaning up, you are the best!"
                        call changeLove("Hinata", 1,"wakeupcompliment_repeat",2) from _call_changeLove_2
                        hin"*Giggles* S-stop it, you! I will be leaving your sights regardless, I was about to pick up laundry and leave..."
                        show hina quest1_2t with dissolve
                        hin"Wouldn't want to see anything I shouldn't!"
                        hide hina with dissolve
                        bot"Heh,I do tend to sleep in my underwear..."
                        bot"Maybe I can find a way to spice things up if this is a common occurrence..."
                    
                    elif wakeupcompliment_repeat >= 1:
                        bo"You need to stop worrying about it. Besides... I am starting to enjoy waking up like this."
                        hin"Ooh? What does that mean, [bo_name]?"
                        bo"It means you are a beautiful sight! Thanks for cleaning up again..."
                        call changeLove("Hinata", 1,"wakeupcompliment_repeat",2) from _call_changeLove_30
                        hin"This again? *Giggles* Thank you [bo_name], but I will be leaving your sights regardless. I was about to pick up the laundry and leave..."
                        show hina quest1_2t with dissolve
                        hin"Wouldn't want to see anything I shouldn't after all!"
                        hide hina with dissolve
                        bot"I on the other hand, would love for that to happen..."
                        bot"*Sigh...*"
                        bot"I'll think of something, one way or another." 
                    $ wakeupcompliment_repeat += 1
                    $ bohin1_love_statcounter += 1 #love path stat increase
                "{color=[dominancecolor]}Compliment her figure{/color}":
                    call checkDominance(4, "wakeupcompliment") from _call_checkDominance
                    default complimentherfigure_repeat = 0
                    if complimentherfigure_repeat == 0:
                        bo"You can be as loud as you want, [hin_rel]. I would enjoy the show regardless..."
                        hin"Huh? What is that supposed to mean [bo_name]..."
                        bo"It means, people would gladly pay to have someone as beautiful as you sweep and swoop around. I get that for free!"
                        call changeObedience("Hinata", 1, "complimentherfigure_repeat", 2) from _call_changeObedience_4 
                        hin"[bo_name_stutter]!" with vpunch
                        hin"You can't be saying things like that... I know it might be well-intended but still! I am your [hin_rel] you know..."
                        bo"Doesn't make it any less true!"
                        hin"Yare yare... I'll be picking up your laundry and I'll give you some space."
                        hin"Lord knows you need it!"
                        hide hina with dissolve
                        hin"Don't stay in bed too long..."
                        bot"Maybe I can find a way to spice things up if this is a common occurrence"
                    elif complimentherfigure_repeat >= 1:
                        bo"Don't worry about it, besides... I am starting to enjoy waking up like this..."
                        hin"Come on [bo_name]... This again?"
                        bo"I told you didn't I? You are a sexy woman, whether you like it or not..."
                        hin"*Gasp* I am a w-what now!?" with vpunch
                        call changeObedience("Hinata", 1, "complimentherfigure_repeat", 2) from _call_changeObedience_54
                        hin"[bo_name_stutter], please!"
                        hin"I told you last time, you can't be saying things like that! Have you forgotten that I am your [hin_rel_mother]?"
                        bo"Lucky me I suppose, hehe!. {p}Take it easy [hin_rel], I am just playing around!"
                        bot"Forgotten? That's all I can think about [hin_rel]..."
                        hin"*Sigh*... I'll be picking up your laundry and leave you to it..."
                        hide hina with dissolve
                        hin"And let's tone it down with the... remarks, okay?"
                        bot"No promises there!"
    
                    $ complimentherfigure_repeat += 1
                    $ bohin1_love_statcounter += 1 #love path stat increase

                    # Hatredlevel2 handjob entry for love path ---------------------------

                "{color=[hatredcolor]}I have had enough, I need MORE from you!{/color}" (advancement_event=True) if day_number>=14 and chosen_hate_path == True and unlock_wakeuphjeventoption and hatredlevel2_handjobcounter == 0:
                    jump hatredlevel2_intro

                "{color=[lovecolor]}I need more help from you...{/color}" if day_number>=14 and chosen_love_path == True and unlock_wakeuphjeventoption and hatredlevel2_handjobcounter == 0:
                    if hinata_love.level == 1:
                        call randomCheck(False,"You do not meet the requirements for this event yet.") from _call_randomCheck_13
                        "Advance [hin_name]'s Love to Level 2 first to unlock this option. Try talking to [hin_name] in the living room during nights..."
                        jump wakeupcompliment
                    jump hatredlevel2_intro_chosenlove


                "{color=[hatredcolor]}???{/color}" (advancement_event=True) if day_number>7 and chosen_love_path == False and not unlock_wakeuphjeventoption:
                    call randomCheck(False,"You do not meet the requirements for this event yet.") from _call_randomCheck_14
                    if day_number>=14 and (chosen_hate_path == True or chosen_love_path == True) and not quest.is_state("bohin_1", "done"):
                        "Unlock this option by completing the quest '[hin_name]'s hospitality'."
                    elif day_number>=14 and (chosen_hate_path == False and chosen_love_path == False) and quest.is_state("bohin_1", "done"):
                        "Unlock this option by choosing to embrace a path of hatred after visiting Kushina in your dreams."
                    elif day_number>=14 and (chosen_hate_path == False and chosen_love_path == False) and not quest.is_state("bohin_1", "done"):
                        "Unlock this option by choosing to embrace a path of hatred after visiting Kushina in your dreams, and also completing the quest '[hin_name]'s hospitality'."
                    elif day_number<14 and (chosen_hate_path == True or chosen_love_path == True) and quest.is_state("bohin_1", "done"):
                        "This option is only unlocked after Day 14."
                    elif day_number<14 and (chosen_hate_path == False and chosen_love_path == False) and quest.is_state("bohin_1", "done"):
                        "Unlock this option after Day 14, by choosing to embrace a path of hatred after visiting Kushina in your dreams."
                    elif day_number<14 and (chosen_hate_path == True or chosen_love_path == True) and not quest.is_state("bohin_1", "done"):
                        "Unlock this option after Day 14, by completing the quest '[hin_name]'s hospitality'."
                    elif day_number<14 and (chosen_hate_path == False and chosen_love_path == False) and not quest.is_state("bohin_1", "done"):
                        "Unlock this option after Day 14, by choosing to embrace a path of hatred after visiting Kushina in your dreams, and also completing the quest '[hin_name]'s hospitality'."
                    jump wakeupcompliment

                "{color=[lovecolor]}???{/color}" (advancement_event=True) if day_number>7 and chosen_love_path == True and not unlock_wakeuphjeventoption:
                    call randomCheck(False,"You do not meet the requirements for this event yet.") from _call_randomCheck_16
                    "This option unlocks after completing the quest '[hin_name]'s hospitality'."
                    jump wakeupcompliment
                "{color=[lovecolor]}???{/color}" (advancement_event=True) if day_number>7 and chosen_love_path == False and not unlock_wakeuphjeventoption:
                    call randomCheck(False,"You do not meet the requirements for this event yet.") from _call_randomCheck_26
                    "Unlock this option after Day 14, by choosing to embrace a path of love after visiting Kushina in your dreams."
                    # elif day_number>=14 and (chosen_hate_path == False and chosen_love_path == False) and quest.is_state("bohin_1", "done"):
                    #     "Unlock this option by choosing to embrace a path of love by visiting Kushina in your dreams."
                    # elif day_number>=14 and (chosen_hate_path == False and chosen_love_path == False) and not quest.is_state("bohin_1", "done"):
                    #     "Unlock this option by choosing to embrace a path of love by visiting Kushina in your dreams, and also completing the quest '[hin_name]'s hospitality'."
                    # elif day_number<14 and (chosen_hate_path == True or chosen_love_path == True) and quest.is_state("bohin_1", "done"):
                    #     "This option is only unlocked after Day 14."
                    # elif day_number<14 and (chosen_hate_path == False and chosen_love_path == False) and quest.is_state("bohin_1", "done"):
                    #     "Unlock this option after Day 14, and by choosing to embrace a path of love by visiting Kushina in your dreams"
                    # elif day_number<14 and (chosen_hate_path == True or chosen_love_path == True) and not quest.is_state("bohin_1", "done"):
                    #     "Unlock this option after Day 14, and by completing the quest '[hin_name]'s hospitality'."
                    # elif day_number<14 and (chosen_hate_path == False and chosen_love_path == False) and not quest.is_state("bohin_1", "done"):
                    #     "Unlock this option after Day 14, and by choosing to embrace a path of love or hatred by visiting Kushina in your dreams, and also completing the quest '[hin_name]'s hospitality'."
                    jump wakeupcompliment

                # Repeatable hatredlevel2 handjob love entry
                "{color=[hatredcolor]}I need help with the curse again!{/color}" if day_number>=14 and chosen_hate_path == True and unlock_wakeuphjeventoption and hatredlevel2_handjobcounter > 0:
                    if hinata_respect < 0:
                        call checkRespect(0,"Hinata",None) from _call_checkRespect_7
                        "[hin_name] does not want to help you with the curse right now."
                        jump wakeupcompliment
                    if percentage < 50:
                        call checkLust(50) from _call_checkLust_20
                        "You are not aroused enough to ask for help with the curse right now."
                        jump wakeupcompliment
                    jump hatredlevel2_handjob_repeatable

                "{color=[lovecolor]}I need help with the curse again!{/color}" if day_number>=14 and chosen_love_path == True and unlock_wakeuphjeventoption and hatredlevel2_handjobcounter > 0:
                    if hinata_respect < 0:
                        call checkRespect(0,"Hinata",None) from _call_checkRespect_8
                        "[hin_name] does not want to help you with the curse right now."
                        jump wakeupcompliment
                    if percentage < 50:
                        call checkLust(50) from _call_checkLust_21
                        "You are not aroused enough to ask for help with the curse right now."
                        jump wakeupcompliment
                    jump hatredlevel2_handjob_chosenlove_repeatable

                "Don't worry about it!":
                    #repeatable
                    default dwaboutit_repeat = 0
                    if dwaboutit_repeat == 0:
                        bo"Don't worry about it, I was about to wake up anyway."
                        call changeRespect("Hinata", 1, "dwaboutit_repeat", 2) from _call_changeRespect_1 
                        hin"Aww, nice of you to say that! I was just wrapping up... I'll pick up your laundry and leave you to it..."
                        show hina quest1_2t with dissolve
                        hin"Wouldn't want to see anything I shouldn't!"
                        hide hina with dissolve
                        bot"Heh,I do tend to sleep in my underwear..."
                        bot"Maybe I can find a way to spice things up if this is a common occurrence"
                    elif dwaboutit_repeat >= 1:
                        bo"Stop worrying about it, [hin_rel]. I owed to wake up either way.{p}You are like a human alarm clock by now, thanks I suppose!"
                        call changeRespect("Hinata", 1, "dwaboutit_repeat", 2) from _call_changeRespect_91
                        hin"*Giggles* I was just wrapping up. I'll pick up your laundry and get out of your hair..."
                        show hina quest1_2t with dissolve
                        hin"Wouldn't want to see anything I shouldn't after all!"
                        bot"I'll figure something out..."
                   
                    $ dwaboutit_repeat += 1
                    $ bohin1_love_statcounter += 1 #love path stat increase

        "{color=[hatredcolor]}'You woke me up!'{/color}" if bohin1_lovepath != True:
            default youwokemeup_repeat = 0

            #repeatable
            if youwokemeup_repeat == 0:
                bo"[hin_rel]! Do you have to be that noisy?"
                show hina quest1_4t with dissolve
                hin"Oh! I am sorry [bo_name]. I was trying to be as quiet as possible."
                call changeHatred(1,"youwokemeup_repeat", 2) from _call_changeHatred
                bo"And yet, you managed to wake me up..."
                
                
            elif youwokemeup_repeat >= 1:
                bo"Again, [hin_rel]? Can a man not sleep in this house?"
                show hina quest1_4t with dissolve
                hin"[bo_name], I am s-sorry. I wasn't trying to wake you up!"
                call changeHatred(1,"youwokemeup_repeat", 2) from _call_changeHatred_76
                bo"And yet you did... AGAIN!"

            menu wakeuphate:
                bo"Damn it..."
                "{color=[hatredcolor]}'How are you going to repay me!?'{/color}":
                    call checkHatred(8, "wakeuphate") from _call_checkHatred
                    $ bohin1_hatred_statcounter += 1 #hatred path stat increase
                    default howrepayme_repeat = 0

                    $ hin_vulnerable_bohin1 = True
                    if howrepayme_repeat == 0:
                        bo"You should be more considerate [hin_rel]! Is it not enough that I am suffering with my condition?"
                        bo"Do I need to lose sleep because of your clumsiness?"
                        hin"I am s-sorry, [bo_name]. I didn't mean to disturb..."
                        bo"You know, if I am to lose sleep over you, I am thinking you should repay me in some way..."
                        hin"W-what? Repay... you?" with vpunch
                        hin"Repay you how? You are scaring me [bo_name]... Is this your condition affecting you?"
                        bo"Might be, who knows. Right now, I need you to quiet down and do as i say!"
                    elif howrepayme_repeat >= 1:
                        bo"I am tired of this... You keep ruining my sleep, [hin_rel]!"
                        bo"This can't keep happening..."
                        hin"I am s-sorry... [bo_name]. I didn't mean to-"
                        bo"Garhh!" with vpunch
                        bo"If I am to keep losing sleep over you, I am thinking it's only fair you repay me in some way!"
                        hin"T-this... again?"
                        hin"You are scaring me, [bo_name]! Is this because of your condition again?"
                        bo"Stop trying to deflect [hin_rel]. You are the one at fault here.{p}For that, you are going to keep it shut and do as I say..."

                    call checkObedience(12,"none", "Hinata") from _call_checkObedience
                    if hinata_obedience >=12:
                        hin"As long as it isn't anything w-weird..."
                            
                        menu bohin1_demands:
                            hin"As long as it isn't anything w-weird..."
                            "{color=[obediencecolor]}I am still thinking about it, for now...{/color}" (greyed_out = (bohin1_demands_1>=1)):
                                default bohin1_demands_1 = 0
                                bo"I am still thinking about what your payment will be..."
                                bo"Until then, you have to keep cleaning my room on the daily!"
                                hin"Come on [bo_name]... Don't be weird! Can't you just ask for a double cheese sandwich or something?"
                                bo"You know what? I'll take that too along with your cleaning duties. But that won't be enough in the future!"
                                call changeObedience("Hinata",1,"bohin1_demands",1) from _call_changeObedience_5
                                show hina quest3_final with dissolve:
                                    zoom 0.95 ypos 0.06
                                hin"[bo_name], you are out of line! ...You dummy!"
                                scene hina leavebobedroom with dissolve
                                "[hin_name] picked up the laundry and hastily left..."
                                bot"You can't just rattle around while I sleep!"
                                scene black with dissolve
                                bot"Guess I'll have to teach you that in other ways [hin_rel]..."

                                $ bohin1_demands_1 +=1

                            "{color=[obediencecolor]}Next time you wake me up you will...{/color}" if bohin1_hatredpath == True:
                                default bohin1_demands_2 = 0
                                if bohin1_demands_2 >= 1:
                                    bo"You remember our agreement, right?"
                                    hin"Y-yes..."
                                    bo"Good... I trust that you won't complain next time!"
                                    jump bohin1_demands

                                else:
                                    bo"Next time you wake me up you are to ask for permission before you leave my room..."
                                    bo"If you keep waking me up, it's only fair I get to... entertain myself with you a little bit, don't you agree?"
                                    call checkObedience(15,"none", "Hinata") from _call_checkObedience_1
                                    if hinata_obedience >= 15:
                                        call changeObedience("Hinata",1,"bohin1_demands_2",1) from _call_changeObedience_6
                                        $ bohin1_3_hinatacoerced = True #allows final cum option when enjoying the show in hatred path
                                        hin"O-okay, If it's just that... I suppose it's not a big ask."
                                        hin"B-but I hope you are not thinking of anything weird..."
                                        bot"Hehe! My plan is in motion! Next time she wakes me up will be interesting..."
                                        $ bohin1_demands_2 +=1
                                    else:
                                        hin"I am not doing that [bo_name]! Not after how you've been acting."
                                        call changeRespect("Hinata",-1) from _call_changeRespect_2
                                        hin"Knowing you you are thinking of something weird, aren't you?"
                                        show hina quest3_final with dissolve:
                                            zoom 0.95 ypos 0.06
                                        hin"I am leaving!"
                                        hide hina
                                        hide hinaq1bg
                                        show hinaq1bg 2 
                                        with dissolve
                                        bot"I'll have to... train her a little bit more first!"
                                        scene black with dissolve
                                        "You can keep increasing [hin_name]'s obedience by selecting non greyed-out options from this quest's choices"

                            "Locked" if bohin1_hatredpath == False:
                                "Quest needs to be set on 'Hatred' path for this option to be available."
                                jump bohin1_demands

                            "{color=[obediencecolor]}Maid outfit (WIP){/color}":
                                dev"Work in progress"
                                jump bohin1_demands

                            "{color=[hatredcolor]}Sexual blackmail (WIP){/color}":
                                dev"Work in progress"
                                jump bohin1_demands



                        $ howrepayme_repeat+= 1
                        
                    else:
                        $ dialogue = renpy.call("get_dialogue", howrepayme_repeat,
                            f"I am not a lap dog {bo_name}! Certainly not yours! You'll stop treating me like that! It's... weird!",
                            f"I am not doing that {bo_name}! Stop making unreasonable demands of me! This is not like you!")
                        $ renpy.say(hin, dialogue)
                        hin"I am sorry, okay? I will be more careful..."
                        $ dialogue = renpy.call("get_dialogue", howrepayme_repeat,
                            f"You better be...",
                            f"I've heard that before, do better!")
                        $ renpy.say(bo, dialogue)
                        hin"..."
                        hide hina with dissolve
                        bot"Bitch!"
                        $ howrepayme_repeat+= 1
                "{color=[dominancecolor]}'Next time you WILL be quiet!'{/color}":
                    call checkDominance(6, "none") from _call_checkDominance_1
                    $ bohin1_hatred_statcounter += 1 #hatred path stat increase
                    default hinata_wakeup_toldoff = False
                    if hinata_wakeup_toldoff == True and dominance < 6:
                        bot"I better not try that again until I am ready..."
                        jump wakeuphate
                    bo"Next time you WILL be quiet, [hin_rel]!" with vpunch
                    bo"Understood?"
                    if dominance >= 6:
                        default howrepayme_repeat_dom1 = 0
                        call changeDominance(1,"howrepayme_repeat_dom1", 2) from _call_changeDominance_1
                        hin"...I am s-sorry."
     
                        if howrepayme_repeat_dom1 == 0:
                            hin"But why do you have to be so... a-assertive?"
                        elif howrepayme_repeat_dom1 >= 1:
                            hin"W-why are you doing this,[bo_name]..."
                        hin"This is not how you usually are!"
                        if howrepayme_repeat_dom1 == 0:
                            bo"Your carelessness has made me like this..."
                        elif howrepayme_repeat_dom1 >= 1:
                            bo"But it is who I will be if you keep being annoying..."

                        hin"W-what? Are you serious [bo_name_stutter]?"
                        bo"Dead serious..."
                        bo"Now finish what you were doing..."
                        show hina_quest_animation
                        $ renpy.pause(0.5, hard=True)
                        show hina quest1_1t with dissolve
                        $ renpy.pause(0.2, hard=True)
                        hide hina with dissolve
                        hin"O-Okay... I won't be much longer."
                        bot"..."
                        $ hin_vulnerable_bohin1 = True
                        $ howrepayme_repeat_dom1 += 1
                        menu bohin1domimenu:
                            bot"..."

                            "{color=[obediencecolor]}Watch her{/color}" (greyed_out = (bohin1domimenu_1>=2)):
                                default bohin1domimenu_1 = 0
               
                                bot"Funny... How quickly [hin_rel] drops her tough act when I put my foot down for once."
                                bot"I've never tried being like this with her before. Seeing [hin_rel] bending to my will..."
                                bot"It's frankly an enjoyable feeling..."
                                show bobedx 2 zorder 100 with dissolve:
                                    alpha 1.0 pos (-8, 18) 


                                bot"It excites me..."
                                bot"But I want more, I need more!"
                                hide hina_quest_animation
                                show hina quest3_2:
                                    zoom 0.8
                                with dissolve
                                hin"I am-"
                                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp1.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                show hina at smallshake
                                hin"*Gasps*"
                                show hina quest3_final with dissolve
                                call changeObedience("Hinata",1,"bohin1domimenu_1",2) from _call_changeObedience_7
                                hin"I am d-done, I'll be leaving you then...."
                                hide hina with dissolve
                                show hina leavebobedroom zorder 200 with dissolve
                                bot"Heh... her face when she saw me fiddling with my cock..."
                                scene blackscreen with dissolve
                                bot"You've seen nothing yet, [hin_rel]. This is just the start..."
                                $ bohin1domimenu_1 +=1

                            "locked" if bohin1domimenu_1 ==0:
                                "Complete previous option first"
                                jump bohin1domimenu

                            


                         
                            "{color=[obediencecolor]}Flash your erection{/color}" (greyed_out = True,threshold_value_grey=2, threshold_value_show=1, int_value_show=bohin1domimenu_1, int_value_grey=bohin1domimenu_2) :
                                default bohin1domimenu_2 = 0
         
                                bot"It'll be fun to see her reaction to this..."
                                $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                show bobedx 3 zorder 100 with dissolve:
                                    alpha 1.0
                                show bobedx 2 zorder 100 with dissolve
                                show bobedx 7 zorder 100 with dissolve:
                                    alpha 1.0
                                bot"But I should do this carefully, I shouldn't spook her off yet..."
                                bo"Hey [hin_rel]... Now that I am thinking about it, maybe you can..."
                                hin"T-thinking about what?"
                                hide hina_quest_animation
                                show hina closet5t:
                                    zoom 0.6 xalign 0.5 ypos -25
                                with dissolve
                                pause 0.2
                                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp1.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                show hina quest3_1 with dissolve:
                                    zoom 0.8 ypos 0
                                show hina at smallshake
                                pause 0.4
                                show hina quest3_2 with dissolve:
                                    zoom 0.8
                                call changeObedience("Hinata",1,"bohin1domimenu_2",2) from _call_changeObedience_8
                                hin"Y-you seem to be having a p-problem with your condition..."
                                show hina quest3_final with dissolve
                                bo"[hin_rel], Wait-"
                                hide hina
                                hide hinaq1bg
                                show hinaq1bg 2 
                                with dissolve
                                hin"I'll be leaving then so you can take care of t-that..."
                                show hina leavebobedroom zorder 200 with dissolve
                                bot"Heh! It'd be easier if you stayed and helped [hin_rel]..."
                                scene black with dissolve
                                bot"Maybe next time!"
                                $ bohin1domimenu_2 +=1


                            "locked" if bohin1domimenu_2 ==0:
                                "Complete previous option first"
                                jump bohin1domimenu
                            
                            




                            "{color=[obediencecolor]}Show her how serious you are{/color}" if bohin1domimenu_2 >= 1: #stand up spank
                                default bohin1domimenu_3_spank = 0
                                default bohin1domimenu_3_grab = 0
                                $ hin_broken_bohin1 = True
                                bot"It's time to teach [hin_rel] a lesson..."
                                bot"I will sneakily approach her from behind while she's picking up my clothes..."
                                $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                show bobedx 3 zorder 100 with dissolve:
                                    alpha 1.0
                                show bobedx 2 zorder 100 with dissolve
                                scene black with dissolve
                                "You stealthily position yourself behind [hin_name]..."
                                show hina domi1 with dissolve
                                bot"You keep sticking out your ass like that [hin_rel]..."
                                bot"Do you seriously expect me not to..."
                                menu:
                                    bot"Do you seriously expect me not to..."
                                    "{color=[obediencecolor]}Smack it{/color}" (greyed_out = (greyoutbohin1domimenu_3_spank>=2)):
                                        default greyoutbohin1domimenu_3_spank = 0 #just for greying out
                                        $ greyoutbohin1domimenu_3_spank +=1
                                        show hina domi2 with dissolve
                                        bot"Just look at you [hin_rel]..."
                                        bot"You are almost asking for it, how can I not smack your ass!"
                                        show hina domi2_1 with dissolve
                                        $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                        show hina domi3 with Dissolve(0.2)
                                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                                        with vpunch
                                        show hina domi4 with Dissolve(0.7)
                                        show hina domi5 with Dissolve(0.7)
                                        hin"*Gasps* Ah!"
                                        scene black with vpunch
                                        show hinaq1bg
                                        show shina surprised3
                                        show boruto box1smirk at right
                                        with dissolve
                                        show shina at smallshake
                                        hin"[bo_name_stutter]!? W-wha-What are you d-doing!?"
                                        bo"Isn't it obvious? That was your punishment for waking me up!"
                                        show shina surprised5 with dissolve
                                        show shina at smallshake
                                        call changeObedience("Hinata",1,"greyoutbohin1domimenu_3_spank", 2) from _call_changeObedience_9
                                        hin"P-punishment!?"
                                        show shina angry3 with dissolve
                                        hin"H-have you lost your mind, [bo_name]!?"
                                        hide shina
                                        show hina quest3_final at left:
                                            zoom 0.90 xpos -0.20
                                        with dissolve
                                        hin"Never do anything like that again! I am leaving!"
                                        hide hina with dissolve
                                        bot"Heh! To think that I smacked [hin_rel]'s ass and I am still standing here alive. A few days ago I would have never dreamt of this..."
                                        bot"Now all I can dream about is how far I can push her!"
                                        scene black with dissolve
                                        $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                        $ bohin1domimenu_3_spank += 1
                                


                                    "{color=[obediencecolor]}Grab it{/color}" (greyed_out = (greyoutbohin1domimenu_3_grab>=2)):
                                        default greyoutbohin1domimenu_3_grab = 0 #just for greying out
                                        $ greyoutbohin1domimenu_3_grab +=1
                                        show hina domi2 with dissolve
                                        bot"I can't stand waking up to you bending over and teasing me with your ass [hin_rel]!"
                                        bot"You are almost asking for it, how can I not grab that ass!"
                                        $ renpy.sound.play("/audio/soun_fx/grope2.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                                        show hina grab1 with Dissolve(0.7)
                                        show hina grab1r with Dissolve(0.3)
                                        pause 0.2
                                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                                        with vpunch
                                        show hina grab2r with Dissolve(0.7)
                                        hin"*Gasps* Ah!"
                                        scene black with vpunch
                                        show hinaq1bg
                                        show shina surprised3
                                        show boruto box1smirk at right
                                        with dissolve
                                        show shina at smallshake
                                        hin"[bo_name_stutter]!? W-wha-What are you d-doing!?"
                                        bo"Isn't it obvious? That was your punishment for waking me up!"
                                        show shina surprised5 with dissolve
                                        show shina at smallshake
                                        call changeObedience("Hinata",1,"greyoutbohin1domimenu_3_grab", 2) from _call_changeObedience_10
                                        hin"P-punishment!?"
                                        show shina angry3 with dissolve
                                        hin"H-have you lost your mind, [bo_name]!?"
                                        hide shina
                                        show hina quest3_final at left:
                                            zoom 0.90 xpos -0.20
                                        with dissolve
                                        hin"Never do anything like that again! I am leaving!"
                                        hide hina with dissolve
                                        bot"Heh! To think that I grabbed [hin_rel]'s ass and I am still standing here alive. A few days ago I would have never dreamt of this..."
                                        bot"Now all I can dream about is how far I can push her!"
                                        scene black with dissolve
                                        $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                        $ bohin1domimenu_3_grab += 1
                                    
                       

                            "{color=[hatredcolor]}Punish her!{/color}" if greyoutbohin1domimenu_3_grab >= 1 or greyoutbohin1domimenu_3_spank >=1:
                                
                                default bohin1_lockedscene1 = 0
                                $ hin_broken_bohin1 = True
                                bot"You are not getting off this easy this time [hin_rel]..."
                                bot"It's about time you realize that your actions have..."
                                $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                show bobedx 3 zorder 100 with dissolve:
                                    alpha 1.0
                                show bobedx 2 zorder 100 with dissolve
                                scene black with dissolve
                                bot"Severe consequences!"
                                "You stealthily position yourself behind [hin_name]..."
                                show hina domi1 with dissolve
                                bot"Even after all my warnings..."
                                show hina domi2 with dissolve
                                bot"You still shake this fucking ass of yours around every morning"
                                bot"I didn't want to go this hard on you but..."
                                show hina pull1 with dissolve
                                bot"It's nigh time you understand!" with vpunch
                                "You sneakily raised her sweater up so that you could..."
                                show hina pull2 with dissolve
                                show hina pull3 with dissolve
                                show hina pull4 with dissolve
                                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                                show hina pull4_1 with dissolve
                                bo"Take..."
                                $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                show hina pull5 with Dissolve(0.2)
                                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                                show hina pull6 with Dissolve(0.8)
                                
                                $ renpy.sound.play("/audio/soun_fx/spank8.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                                show hina pull7 with Dissolve(0.2)
                                with vpunch
                                $ renpy.sound.play("/audio/soun_fx/gruntwoman1.opus", channel="sfx1", loop=False, relative_volume = 1.0)
                                call changeHatred(1,"bohin1_lockedscene1",2) from _call_changeHatred_1
                                bo"...This!"
                                scene black with vpunch
                                $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                bo"Maybe this will teach you to keep quiet!"
                                hin"[bo_name_stutter]!?!"
                                show hinaq1bg
                                show shina surprised4
                                show boruto box1smirk at right
                                with dissolve
                                show shina at smallshake
                                show shina concerned with dissolve
                                show shina:
                                    easein 1 xalign 0.3
                                hin"H-how coul-... How could you do..."
                                bo"Don't look at me like that [hin_rel]! You know you deserved th-"
                                show shina angry3 with dissolve
                                show shina at smallshake
                                hin"HOW COULD YOU DO THAT TO ME YOU IDIOT!" with vpunch
                                show shina surprised5 with dissolve
                                hin"I am your [hin_rel_mother]... [bo_name]!"
                                show boruto box1surprised
                                bot"She looks like she is about to cry..."
                                show shina:
                                    easeout 1 xpos -0.5
                                hin"*Sniffles* What... has gotten into you? Why are you like this..."
                                "[hin_name] ran off, evidently holding back tears..."
                                if bohin1_lockedscene1 == 0:
                                    bot"Did I... push her too far?"
                                    menu:
                                        bot"Did I... push her too far?"
                                        "Maybe I should apologize":
                                            bot"I know she is more lenient than usual because of my condition... but I don't want to break her spirits."
                                            bot"Maybe I should apologize and take things slower for now. Otherwise she might stray further away..."
                                        "She deserved it!":
                                            show boruto box1smirk with dissolve
                                            bot"Nah! She deserved that. I tried warning her before and she wouldn't listen."
                                            bot"If she keeps pulling off this shit, I might have to prove my point to her sometimes!"
                                
                                else:
                                    show boruto box1smirk with dissolve
                                    bot"Not my fault you keep being an annoying bi-..."
                                scene black with dissolve
                                bot"*Sigh*"
                                $ bohin1_lockedscene1+=1
                                $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                
                    else:
                        hin"W-what!? [bo_name]!"
                        hin"What has gotten into you? Do you think I am your house servant to do with as you please!?"
                        call changeLove("Hinata", -1, "none") from _call_changeLove_3
                        hin"Never again, will YOU raise your voice towards ME! I will not tolerate it."
                        hin"Do YOU... understand?" with vpunch
                        bo"..."
                        hide hina with dissolve
                        $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                        "Thud!" with vpunch
                        "[hin_name] slams the door behind her, evidently annoyed by your remarks."
                        bot"With my condition, I am easily agitated. I should be more careful..."
                        $ hin_vulnerable_bohin1 = True
                        $ hinata_wakeup_toldoff = True

                "Forgive her...":
                    $ bohin1_hatred_statcounter += 1 #hatred path stat increase
                    bo"Bah! Just try to be quiet next time please..."
                    hin"I was only trying to help, [bo_name]. You don't have to be mad..."
                    hide hina with dissolve
            $ youwokemeup_repeat += 1
        
        # Hatredlevel2 handjob entry for hatred path ---------------------------

        "{color=[hatredcolor]}I have had enough, I need MORE from you!{/color}" (advancement_event=True) if day_number>=14 and chosen_hate_path == True and unlock_wakeuphjeventoption and hatredlevel2_handjobcounter == 0:
            jump hatredlevel2_intro

        "{color=[lovecolor]}I need more help from you...{/color}" if day_number>=14 and chosen_love_path == True and unlock_wakeuphjeventoption and hatredlevel2_handjobcounter == 0:
            if hinata_love.level == 1:
                call randomCheck(False,"You do not meet the requirements for this event yet.") from _call_randomCheck_15
                "Advance [hin_name]'s Love to Level 2 first to unlock this option. Try talking to [hin_name] in the living room during nights..."
                jump wakeupmenu
            jump hatredlevel2_intro_chosenlove

        # "{color=[hatredcolor]}???{/color}" (advancement_event=True) if day_number>7 or (chosen_hate_path == False and chosen_love_path == False) or not unlock_wakeuphjeventoption:
        #     call randomCheck(False,"You do not meet the requirements for this event yet.") from _call_randomCheck_16
        #     if day_number>=14 and (chosen_hate_path == True or chosen_love_path == True) and not quest.is_state("bohin_1", "done"):
        #         "Unlock this option by completing the quest '[hin_name]'s hospitality'."
        #     elif day_number>=14 and (chosen_hate_path == False and chosen_love_path == False) and quest.is_state("bohin_1", "done"):
        #         "Unlock this option by choosing to embrace a path of hatred after visiting Kushina in your dreams."
        #     elif day_number>=14 and (chosen_hate_path == False and chosen_love_path == False) and not quest.is_state("bohin_1", "done"):
        #         "Unlock this option by choosing to embrace a path of hatred after visiting Kushina in your dreams, and also completing the quest '[hin_name]'s hospitality'."
        #     elif day_number<14 and (chosen_hate_path == True or chosen_love_path == True) and quest.is_state("bohin_1", "done"):
        #         "This option is only unlocked after Day 14."
        #     elif day_number<14 and (chosen_hate_path == False and chosen_love_path == False) and quest.is_state("bohin_1", "done"):
        #         "Unlock this option after Day 14, and by choosing to embrace a path of hatred after visiting Kushina in your dreams."
        #     elif day_number<14 and (chosen_hate_path == True or chosen_love_path == True) and not quest.is_state("bohin_1", "done"):
        #         "Unlock this option after Day 14, and by completing the quest '[hin_name]'s hospitality'."
        #     elif day_number<14 and (chosen_hate_path == False and chosen_love_path == False) and not quest.is_state("bohin_1", "done"):
        #         "Unlock this option after Day 14, and by choosing to embrace a path of hatred after visiting Kushina in your dreams, and also completing the quest '[hin_name]'s hospitality'."
        #     jump wakeupmenu
        "{color=[hatredcolor]}???{/color}" (advancement_event=True) if day_number>7 and chosen_hate_path == True and not unlock_wakeuphjeventoption:
            call randomCheck(False,"You do not meet the requirements for this event yet.") from _call_randomCheck_27
            "This option unlocks after completing the quest '[hin_name]'s hospitality'."
            jump wakeupmenu
        "{color=[hatredcolor]}???{/color}" (advancement_event=True) if day_number>7 and chosen_hate_path == False and chosen_love_path == False and not unlock_wakeuphjeventoption:
            call randomCheck(False,"You do not meet the requirements for this event yet.") from _call_randomCheck_28
            "Unlock this option after Day 14, by choosing to embrace a path of hatred after visiting Kushina in your dreams."
            jump wakeupmenu

        "{color=[lovecolor]}???{/color}" (advancement_event=True) if day_number>7 and chosen_love_path == True and not unlock_wakeuphjeventoption:
            call randomCheck(False,"You do not meet the requirements for this event yet.") from _call_randomCheck_29
            "This option unlocks after completing the quest '[hin_name]'s hospitality'."
            jump wakeupmenu
        "{color=[lovecolor]}???{/color}" (advancement_event=True) if day_number>7 and chosen_love_path == False and not unlock_wakeuphjeventoption:
            call randomCheck(False,"You do not meet the requirements for this event yet.") from _call_randomCheck_30
            "Unlock this option after Day 14, by choosing to embrace a path of love after visiting Kushina in your dreams."
            jump wakeupmenu

        # Repeatable hatredlevel2 handjob hate entry
        "{color=[hatredcolor]}'I need help with the curse again!'{/color}" if day_number>=14 and chosen_hate_path == True and unlock_wakeuphjeventoption and hatredlevel2_handjobcounter > 0:
            if hinata_respect < 0:
                call checkRespect(0,"Hinata",None) from _call_checkRespect_9
                "[hin_name] doesn't respect you enough to help right now."
                jump wakeupmenu
            if percentage < 50:
                call checkLust(50) from _call_checkLust_22
                "You are not aroused enough to ask for help with the curse right now."
                jump wakeupmenu
            jump hatredlevel2_handjob_repeatable

        "{color=[lovecolor]}'I need help with the curse again!'{/color}" if day_number>=14 and chosen_love_path == True and unlock_wakeuphjeventoption and hatredlevel2_handjobcounter > 0:
            if hinata_respect < 0:
                call checkRespect(0,"Hinata",None) from _call_checkRespect_10
                "[hin_name] doesn't respect you enough to help right now."
                jump wakeupmenu
            if percentage < 50:
                call checkLust(50) from _call_checkLust_23
                "You are not aroused enough to ask for help with the curse right now."
                jump wakeupmenu
            jump hatredlevel2_handjob_chosenlove_repeatable



    #event ends here
    label wakeupend:
        default bohin1_pathchosen = False
        if bohin1_pathchosen == False:            
            if bohin1_love_statcounter >= 4:
                $ bohin1_lovepath = True
                $ bohin1_pathchosen = True
                $ notification("Event option unlocked")
                "You locked this event to its love path. New options are unlocked, hatred-related options are removed."

            if bohin1_hatred_statcounter >= 4:
                $ bohin1_hatredpath = True
                $ bohin1_pathchosen = True
                $ notification("Event option unlocked")
                "You locked this event to its hatred path. New options are unlocked, love-related options are removed."             
        scene bg bb day with dissolve
        if v12ending == False:
            default v12ending = False
            $ v12ending = True
            dev"From this point onwards, the freeroam aspect will be quite barren. Remember, the focus of the next few updates is to enrich it with multiple sexy events!"
            dev"For now, take a look around the ramen shop if you haven't already! (There's a lot of content in there)"
            dev"You can consider this version completed when all your quest objectives are marked with 'WIP' (Work in Progress)"
            dev"That'll be it from me, have fun exploring!"
        call showUIhouse from _call_showUIhouse
        $ strengthbutton = True
        $ ui.interact()

label bohin1_2_wakeup:          
    # elif quest.is_state("bohin1_2", "in progress"):
    bot"Damn..."
    bot"[hin_rel]'s ass bend over like that, it awakens something in me."
    bot"Maybe I'll go mess with her in the laundry room after, hehe!"
    return

label bohin1_3_wakeup:

    # elif quest.is_state("bohin1_3", "in progress"):
    bot"It's time I pull my dirty trick on her"
    bo"Oh hey [hin_rel]..."
    hin"Oh! Sorry... Did I wake you up?"
    bo"Kinda but just in time. You see..."
    bo"During nights sometimes I..."
    bo"give her stained"
    return

label bohin1_4_wakeup:
    # elif quest.is_state("bohin1_3", "completed"):
    bot"All this pent up lust..."
    bot"It hurts. I need to get rid of it!"
    $ notification("Hidden objective available")
    return














label bohin1_lovepath:
    #repeatable
    default bohin1_lovepath_repeat = 0
    show hinaq1bg
    show hina quest2_2
    show bobedx 3 zorder 100:
        matrixtransform ScaleMatrix(1.0, 0.6, 1.0)*OffsetMatrix(1.0, 238.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
        alpha 0.20
    with dissolve
    bot"I don't know how much more I can endure this for..."
    #repeatable
    if bohin1_lovepath_repeat == 0:
        bot"You are so fucking amazing [hin_rel]!"
    elif bohin1_lovepath_repeat >= 1:
        bot"I can't get enough of you [hin_rel]..."

    bot"Especially when you bend over like that..."
    call increaselust(20) from _call_increaselust_6
    call checkLust(90) from _call_checkLust_1
    if percentage >=90:
        default bohin1_lovepath_repeat_cum = 0
        bot"There's no way I can resist the temptation when you do that [hin_rel]..."
        show bobedx 5 with dissolve:
            alpha 1.0
        
        #repeatable
        if bohin1_lovepath_repeat_cum == 0:
            bot"If I am careful she won't know a thing anyway!"
            show bobedx 6 with dissolve
            bot"I can't believe I am doing this behind [hin_rel]'s back..."
        elif bohin1_lovepath_repeat_cum >= 1:
            bot"Just like last time... only a bit more methodical!"
            show bobedx 6 with dissolve
            bot"But am  I really going to do this again? I am losing myself in my depravity..."

        show bobedx 6 with dissolve:
            alpha 0.15
        show hina_quest_animation2
        $ renpy.pause(1.2, hard=True)
        hide hina quest2
        with dissolve

        #repeatable
        if bohin1_lovepath_repeat_cum == 0:
            bot"But come on... who could resist an ass sticking out like that!"
            bot"How can a woman be as pretty, as caring and as sexy as you. That's just unfair..."
            bot"What's even more unfair is that you happen to be my [hin_rel]..."
        elif bohin1_lovepath_repeat_cum >= 1:
            bot"But goddamn it [hin_rel] it's almost as if you are doing this on purpose..."
            bot"Every day I am waking up with you shaking your ass around, it's unfair..."
            bot"If only you weren't my [hin_rel]..."

        
        menu bohin1_lovepath_menu:
            bot"But am I going to let that stop me?"
            "Is there anything I can do?" if bohin1_lovepath_repeat_cum >=0:
                bot"But how do I breach that prohibitive bond between us... Is there anything I can do?"
                hide hina_quest_animation2
                show hina quest1_1t:
                    xpos -0.25
                with dissolve
                hin"It's getting so humid in here... phew!"
                show hina closet0 with dissolve:
                    zoom 0.6
                hin"And I still have [bo_name]'s closet to clean up... *Sigh*"
                show bobedx 6 with dissolve:
                    alpha 1
                bot"F-fuck! She turned around!" with vpunch
                show hina closet0:
                    easein 2 xpos (-0.5)
                show bobedx 6 with dissolve:
                    alpha 0.15
                bot"But I don't think she noticed..."
                hide hina
                bot"But now she is out of my line of sight... I'll just have to use my imagination for now!"
                show hinabobedroom border zorder 90:
                    zoom 0.55 yalign 0.5
                show hina closet1:
                    zoom 0.55 yalign 0.5
                with dissolve
                hin"Every summer the heat keeps getting worse..."
                show hina closet2 with dissolve
                hin"I should probably lose the sweater given how hot it is..."
                bot"I concur [hin_rel]! In fact, you should probably lose as much clothing as possible..."
                show hina closet3 with dissolve
                hin"But what if [bo_name]'s condition worsens because of me..."
                hin"He's been acting weird after his diagnosis, I need to be careful to avoid triggering any of his... reactions."
                bot"No... No, [hin_rel]! Quite the opposite..."
                show bobedx 6 with dissolve:
                    alpha 1
                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show bobedx cum1
                with flash
                call decreaselust(50) from _call_decreaselust_2
                bot"You'll have to h-help with my reactions!"
                $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show bobedx cum2
                with longerflash
                $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                call decreaselust(50) from _call_decreaselust_3
                bo"*Panting*"
                bot"Otherwise I'll slowly descend to fucking madness..."
                bot"Although I might already be way past that given what I am doing..."
                show bobedx 6 with dissolve:
                    alpha 0.15
                show hina closet4 with dissolve
                hin"*Phew* Done with the closet too. Now to pick up the laundry..."
                bot"I'll just have to pretend I just woke up..."
                show blackscreen zorder 150 with dissolve
                hide hina closet4
                hide hinabobedroom border
                "You close your eyes..."
                show hina closet4t:
                    zoom 0.6
                
                show fullblack zorder 200
                hide blackscreen with dissolve
                show eyehalfopen zorder 200
                hide fullblack
                hide eyeclosed
                show hina:
                    easein 1 xalign 0.5
                with dissolve
                bo"..."
                pause 0.2
                show eyeclosed zorder 200 with dissolve
                bo"*Fakes yawning*"
                show eyefullopen zorder 200
                hide eyeclosed with dissolve
                pause .2
                
                hide eyehalfopen with dissolve
                bo"[hin_rel]?"
                show hina at smallshake
                pause 0.3
                show hina closet5t with dissolve
                with dissolve
                hin"Oh, [bo_name_stutter]!" with vpunch
                bot"Fuck me, her tits were almost bursting out!"
                 
                hide eyefullopen with dissolve
                bot"She shyly turned away as soon as she took notice of me..."
                bot"I am not complaining though... the back view might be greater than the front."
                hide hina
                
                show hina quest3_final
                with dissolve
                hin"I'll be out of your hair, I was just wrapping up!"
                hide hina
                hide hinaq1bg
                show hinaq1bg 2
                
                with dissolve
                hin"S-sorry if I disturbed your sleep!"
                show bobedx 2 with dissolve:
                    alpha 1
                bot"You could not have disturbed me if you tried [hin_rel]..."
                bot"Next time I'll have to try something!"
                $ notification("Event option unlocked")

                



            "I have a plan..." if bohin1_lovepath_repeat_cum >=1:
                default laundrytalkcheck = False
                $ laundrytalkcheck = True

                default laundrycumcheck = False
                $ laundrycumcheck = True
                bot"Not today I won't!"
                hide hina_quest_animation2
                show hina quest1_1t:
                    xpos -0.25
                with dissolve
                hin"This heat is unbearable..."
                show hina closet0 with dissolve:
                    zoom 0.6
                hin"How do you manage to keep your room this messy on the daily [bo_name]...*Sigh*"
                show bobedx 6 with dissolve:
                    alpha 1
                bot"Heh, maybe that's so you can wake me up like this every day [hin_rel]..."
                show hina closet0:
                    easein 2 xpos (-0.5)
                show bobedx 6 with dissolve:
                    alpha 0.15
                bot"She is off to the closet..."
                hide hina
                bot"Time to execute my plan!"
                $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                hide bobedx with dissolve
                show bobedx 1 with dissolve:
                    alpha 1.0
                bot"If I pretend that I've no idea she was in here as she comes out of the closet..."
                show bobedx 1_1 with dissolve:
                    alpha 1.0
                
            
                bot"This might just work..."
                show bobedx 1_2:
                        ypos 200 xzoom 1.0 yzoom 0.85 crop (0.0, 0.0, 1.0, 1.0) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
                show hinabobedroom border zorder 90:
                    zoom 0.55 yalign 0.5
                show hina closet1:
                    zoom 0.55 yalign 0.5
                show bobedx 1_2:
                    alpha 0.15
                with dissolve

                hin"I am getting so sweaty doing this..."
                show hina closet2 with dissolve
                hin"I'll have to take another shower after I am done..."
                if secretscenelovehandjob == True:
                    bot"I could join in on that [hin_rel]... Just like last time when you 'helped'!"
                    bot"I'd scrub you clean and you would do the same for me..."
                else:
                    bot"We could do that together [hin_rel]. I'd scrub you clean and you would do the same for me..."
                show hina closet3 with dissolve
                hin"Everything's so dusty..."
                show bobedx 1_2 zorder 200 with dissolve:
                    alpha 1
                bot"I am close but... I need to hold on until...!"
                show bobedx 1_2 with dissolve:
                    alpha 0.15

                show hina at smallshake
                hin"*Sprays and sweeps*"
                hin"There... that should do it!"
                show hina closet5 with dissolve
                hin"Now to pick up the laundry..."
                hint"[bo_name] has been leaving multiple of his underwear lying around lately..."
                hint"Could it be due to his condition? I can't imagine how hard it must be on him..."
                hide hina closet4
                hide hinabobedroom border
                with dissolve
                show hina closet4t with dissolve:
                    zoom 0.7 xalign -0.4
                bot"P-perfect timing, [hin_rel]!"
                show hina closet4t:
                    easein 2 xalign 0.5
                with flash
                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show bobedx 1_2cum1 with dissolve:
                    alpha 1.0
                show hina closet4_1t with Dissolve(1)
                call decreaselust(50) from _call_decreaselust_4
                # show hina at smallshake
                show hina closet4_2t with Dissolve(2)
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                show hina at smallshake
                hin"*Gasps!* [bo_name_stutter]!? "
                show bobedx 1_2cum2:
                    alpha 1.0
                $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                with longerflash
                $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                call decreaselust(50) from _call_decreaselust_5
                show bobedx 1_2cum2 with dissolve:
                    alpha 0.15
                bo"*Panting*"
                bot"Now to put on an act..."
                bo"[hin_rel]!? Why are you in here!" with vpunch
                hide hina
                show hina quest3_2
                with dissolve
                call changeObedience("Hinata",1,"bohin1_hlovepath_menu_withflashingyou") from _call_changeObedience_55
                hin"I-I-i am so s-sorry! I didn't realize you were a-awake!"
                
                show hina quest3_final
                with dissolve
                hin"I'll just... pick up t-this!"
                hide hina
                hide hinaq1bg
                show hinaq1bg 2
                
                with dissolve
                hin"And leave you to it!"
                scene hina leavebobedroom with dissolve
                bo"[hin_rel], wait..."
                scene black with dissolve
                bot"...She wasn't mad! Just as planned..."
                bot"Now if I am careful with how I reason with her..."
                bot"Maybe I can push things further next time!"
                $ notification("Event option unlocked")


            "{color=[obediencecolor]}[hin_rel], I need to...{/color}" if bohin1_lovepath_repeat_cum >=2:
                $ laundrytalkcheck = True
                $ laundrycumcheck = True
                if bohin1_3_laundrytalked == 0:
                    bot"[hin_rel] knows what I have to deal with. She wouldn't mind if I..."
                elif bohin1_3_laundrytalked == 1:
                    bot"We've had that talk in the laundry room the other day, [hin_rel] knows I need this!"

                hide hina_quest_animation2 with dissolve
                pause 0.1
                show hina quest2_5:
                    zoom 0.7 xalign 0.2 ypos 40
                with dissolve
                bot"F-fuck me!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                show bobedx 1 with dissolve:
                    alpha 0.15
                show hina quest2_4 with dissolve:
                    zoom 0.6 ypos 50
                show hina quest2_4:
                    easein 1 xalign 0.0 ypos 60
                bot"There's no way I am holding back when you bend over like that!"
                hide bobedx 1 with dissolve
                
                show bobedx f1 zorder 100 with dissolve:
                    yanchor 1 yzoom 1.0 matrixtransform ScaleMatrix(1.0, 0.85, 1.0)*OffsetMatrix(0.0, 74.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
                bot"What's the worst that can happen..."
                $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                show bobedx f2 with dissolve
                show bobedx f1 with dissolve
                show bobedx f2 with dissolve
                show bobedx f1 with dissolve:
                    alpha 0.15
                bot"I'll just blame my condition..."
                bo"[hin_rel]?"
                show hina closet5t with dissolve:
                    zoom 0.6 ypos -46 xalign 0.3
                hin"...Huh?"
                $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                show bobedx f2 with dissolve:
                    alpha 0.8
                show bobedx f1 with dissolve
                show bobedx f2 with dissolve
                show bobedx f1 with dissolve:
                    alpha 0.15
                
                if bohin1_3_laundrytalked == 0: #if statement if talked in laundry increases by 1
                    bo"I need to..."
                    hide hina
                    show hina quest3_1:
                        zoom 0.9 ypos 74
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    hin"[bo_name_stutter]!?" with vpunch
                    hin"W-what are you d-"
                    show hina quest3_final with dissolve 
                    bo"I am s-sorry [hin_rel] but..."
                    hide hina
                    hide hinaq1bg
                    show hinaq1bg 2
                    with dissolve
                    bo"You know I need this!"
                    scene hina leavebobedroom with dissolve
                    call changeRespect("Hinata", -1,"none") from _call_changeRespect_3
                    hin"D-don't just start doing that in front of me!"
                    scene black with dissolve
                    bot"I s-scared her off. I should talk to her before I try this again..."
                    $ hin_vulnerable_bohin1 = True

                else:
                    bo"Remember the t-talk we had?"
                    hide hina
                    show hina quest3_2:
                        zoom 0.9 ypos 74
                    with dissolve
                    show hina at smallshake
                    hin"[bo_name_stutter]!?" with vpunch
                    bo"I c-can't control myself, it hurts!"
                    show hina at smallshake
                    hin"...R-right now!?"
                    show hina closet4_2t with dissolve:
                        zoom 0.65 pos(227,-37)
                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    show bobedx f2 with dissolve:
                        alpha 1.0
                    show bobedx f1 with Dissolve(0.35)
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with Dissolve(0.35)
                    show hina at smallshake
                    show hina quest3_1 with dissolve:
                        zoom 0.9 ypos 74 xpos -20
                    show hina at smallshake
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with Dissolve(0.35)
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with dissolve:
                        alpha 0.15
                    show hina quest3_2 with dissolve:
                        zoom 0.9 ypos 74
                    call changeObedience("Hinata", 1, "jeroffinfront1", 2) from _call_changeObedience_58
                    hin"Do y-you h-have to do that in front of me!?"
                    bo"I told you, s-sometimes it hurts too much!"
                    show hina quest2_4 with dissolve:
                        zoom 0.6 xalign 0.0 ypos 60
                    bo"There's no other way [hin_rel]..."     
                    hin"I..."
                    show hina quest2_5 with dissolve:
                        zoom 0.7 xalign 0.2 ypos 40
                    hin"... I'll just wrap up what I am doing."
                    show hina_quest_animation3
                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    show bobedx f2 with dissolve:
                        alpha 1.0
                    show bobedx f1 with Dissolve(0.35)
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with Dissolve(0.35)
                    $ renpy.pause(0.7, hard=True)
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with Dissolve(0.35)
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with dissolve:
                        alpha 0.15
                    $ renpy.pause(0.7, hard=True)
                    hide hina with dissolve
                    hin"D-don't mind me..."
                    bot"H-holy shit, she's putting up with me!" with vpunch
                    bot"All I can do is mind you... [hin_rel]!"
                    bot"I can't believe you are sticking your ass out like that knowing what I am doing..."
                    bot"It's as if you are trying to make this easy for me!"
                    show bobedx f2 with dissolve:
                        alpha 1.0
                    show bobedx f1 with Dissolve(0.35)
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with Dissolve(0.35)
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with Dissolve(0.35)
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with dissolve:
                        alpha 0.15
                    bot"Could that actually be what you are thinking?"
                    bot"I will have to try pushing you further to figure that out..."
                    bot"In fact, why don't I do that right now..."
                    menu bohin1_love_endcum:
                        bot"In fact, why don't I do that right now..."
                        "Call out for her before you cum":
                            bo"[hin_rel]! Can you..."
                            show bobedx f2 with dissolve:
                                alpha 1.0
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            bo"...Turn around?"
                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            show bobedx f1 with dissolve:
                                alpha 0.15
                            hide hina_quest_animation3                         
                            show hina closet5t:
                                zoom 0.6 ypos -46 xalign 0.3
                            with dissolve
                            hin"W-what for...?"
                            show hina closet4_2t with dissolve:
                                zoom 0.65 pos(327,-37)
                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            show bobedx f2 with dissolve:
                                alpha 1.0
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                            show bobedx fcum1
                            with flash
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            show hina at smallshake
                            show bobedx fcum1 with dissolve:
                                alpha 0.15
                            show hina quest3_2 with dissolve:
                                zoom 0.9 ypos 74
                            hin"*Gasps* E-eeh!?" with vpunch
                            show bobedx fcum2:
                                alpha 1.0
                            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                            with longerflash
                            call decreaselust(100) from _call_decreaselust_62
                            show hina quest3_final with dissolve
                            show hina at smallshake
                            hin"W-why did you call me o-out for that!"  
                            bo"I... had to see you."
                            $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                            hide hina
                            hide hinaq1bg
                            show hinaq1bg 2
                            with dissolve
                            hin"I... am leaving now!"
                            bot"*Panting* Holy shit! I can't believe [hin_rel] put up with that..."
                            scene hina leavebobedroom with dissolve
                            bot"If she is now willing to put up with me using her as stimuli, what else could I push her to do..."



                        "...":
                            bo"I am..."
                            show bobedx f2 with dissolve:
                                alpha 1.0
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            bot"I can't take this anymore!"
                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            show bobedx f1 with dissolve:
                                alpha 0.15
              
                            hin"..."
                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            show bobedx f2 with dissolve:
                                alpha 1.0
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                            show bobedx fcum1
                            with flash
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            show bobedx fcum1 with dissolve:
                                alpha 0.15
                            hide hina_quest_animation3 
                            show hina quest3_2:
                                zoom 0.9 ypos 74
                            with dissolve
                            show hina at smallshake
                            hin"*Gasps*" with vpunch
                            show bobedx fcum2:
                                alpha 1.0
                            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                            with longerflash
                            call decreaselust(100) from _call_decreaselust_63
                            show hina quest3_final with dissolve
                            bo"*Moans*"
                            show hina at smallshake
                            hin"A-are you d-done with t-that?"  
                            $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                            hide hina
                            hide hinaq1bg
                            show hinaq1bg 2
                            with dissolve
                            bo"*Panting* Y-yeah..."
                            hin"G-good, I-i am leaving now!"
                            bot"...Holy shit!"
                            scene hina leavebobedroom with dissolve
                            bot"Did she intentionally stay until I was done? If she is putting up with this I wonder what else could I push her to do..."

                        
                        


            "locked" if bohin1_lovepath_repeat <1:
                "Complete previous option first"
                jump bohin1_lovepath_menu

            "locked" if bohin1_lovepath_repeat <2:
                "Complete previous option first"
                jump bohin1_lovepath_menu


            



        scene black with dissolve
        $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        "You put on some clothes and get up..."
        $ bohin1_lovepath_repeat += 1
        $ bohin1_lovepath_repeat_cum +=1
        jump wakeupend




    else:
        bot"Fun's over I suppose..."
        show hina quest1_4t with dissolve:
            zoom 1.1 xpos -100 ypos -50
        #repeatable
        $ dialogue = renpy.call("get_dialogue", wakeupmenu_repeat,
            "Oh, did I wake you up? Sorry about that!",
            "Oh, did I wake you up again? Sorry!")
        $ renpy.say(hin, dialogue)
        $ dialogue = renpy.call("get_dialogue", wakeupmenu_repeat,
            "Hey [hin_rel], I was just about to wake up anyway, don't worry about it.",
            "I am getting used to it by now, don't worry about it.")
        $ renpy.say(bo, dialogue)
        show hinaq1bg 2
        show hina quest3_final
        with dissolve
        $ dialogue = renpy.call("get_dialogue", wakeupmenu_repeat,
            "I am just picking up the laundry and I'll give you some space.",
            "Right, I'll pick up the laundry and get out of your hair.")
        $ renpy.say(hin, dialogue)
        hin"Wouldn't want to see anything I shouldn't!"
        bo"Yeah... Thanks [hin_rel]."
        hide hina with dissolve
        show bobedx with dissolve:
            alpha 1
        bot"God-damn it [hin_rel]... All I am thinking about lately is you."
        hide bobedx
        show bobedx 4:
            alpha 1
        with dissolve
        bot"I need some sort of release, otherwise I risk going fucking crazy..."
        bot"I'll have to see if there's a way I can take things further..."
        
        scene black with dissolve
        $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        "You put on some clothes and get up..."
        $ bohin1_lovepath_repeat += 1
        jump wakeupend


























label bohin1_hatredpath:
    default bohin1_hatredpath_repeat = 0
    show hinaq1bg
    show hina quest2_2
    show bobedx 3 zorder 100:
        matrixtransform ScaleMatrix(1.0, 0.6, 1.0)*OffsetMatrix(1.0, 238.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
        alpha 0.20
    with dissolve
    bot"I am losing my fucking mind watching your ass every morning..."

    if bohin1_hatredpath_repeat == 0:
        bot"You are so freaking sexy [hin_rel]!"
    elif bohin1_hatredpath_repeat >=1:
        bot"You have no idea how I lust over you [hin_rel]!"

    bot"That ass will be mine soon!"
    call increaselust(20) from _call_increaselust_7
    call checkLust(90) from _call_checkLust_2
    if percentage >=90:
        default bohin1_hatredpath_repeat_cum = 0
        bot"But for now, I'll have to settle with paying a tribute to it!"
        show bobedx 5 with dissolve:
            alpha 1.0

        if bohin1_hatredpath_repeat_cum == 0:
            bot"She won't know a thing anyway!"
        elif bohin1_hatredpath_repeat_cum >=1:
            bot"Just like last time..."

        show bobedx 6 with dissolve
        if bohin1_hatredpath_repeat_cum == 0:
            bot"Look how you my cock yearns for you [hin_rel]!"
        elif bohin1_hatredpath_repeat_cum >=1:
            bot"Even this guy is excited to have another go!"
 
        show bobedx 6 with dissolve:
            alpha 0.15
        show hina_quest_animation2
        $ renpy.pause(1.2, hard=True)
        hide hina quest2
        with dissolve

        if bohin1_hatredpath_repeat_cum == 0:
            bot"Now put on a show for me [hin_rel]. Move your sexy ass while I secretly jerk it behind your back!"
            bot"It's unreal how you manage to be as sexy as you are while doing menial shit around the house"
            bot"I swear , if you weren't my [hin_rel]... I'd worship your body every single day..."
        elif bohin1_hatredpath_repeat_cum >=1:
            bot"The way you bend that ass over... it's like you want me to get up and shove my cock deep inside of you!"
            bot"I am not that far off from doing that! If only we weren't... F-fuck!"
            bot"For now I'll have to settle..."

        menu bohin1_hatredpath_menu:
            bot"For now I'll have to settle..."
            "{color=[obediencecolor]}With this!{/color}" (greyed_out = True,threshold_value_grey=1, int_value_grey=bohin1_hatredpath_menu_withthis) if bohin1_hatredpath_repeat_cum >=0:
                default bohin1_hatredpath_menu_withthis = 0
                bot"With this!"
                hide hina_quest_animation2
                show hina quest1_1t:
                    xpos -0.25
                with dissolve
                hin"It's getting so humid in here... phew!"
                show hina closet0 with dissolve:
                    zoom 0.6
                hin"And I still have [bo_name]'s closet to clean up... *Sigh*"
                show bobedx 6 with dissolve:
                    alpha 1
                bot"F-fuck! Don-t turn around now you w-" with vpunch
                show hina closet0:
                    easein 2 xpos (-0.5)
                show bobedx 6 with dissolve:
                    alpha 0.15
                bot"Phew... I don't think she noticed. [hin_rel] is such a klutz sometimes!"
                hide hina
                bot"But now she is out of my line of sight... "
                show hinabobedroom border zorder 90:
                    zoom 0.55 yalign 0.5
                show hina closet1:
                    zoom 0.55 yalign 0.5
                with dissolve
                hin"Every summer the heat keeps getting worse..."
                show hina closet2 with dissolve
                hin"I should probably lose the sweater given how hot it is..."
                bot"I concur [hin_rel]! In fact, maybe I should have you wear a maid outfit next time as your punishment!"
                show hina closet3 with dissolve
                hin"But what if [bo_name]'s condition worsens because of me..."
                hin"He's been acting weird after his diagnosis, I need to be careful to avoid triggering any of his... reactions."
                bot"We are way past that now [hin_rel]..."
                show bobedx 6 with dissolve:
                    alpha 1
                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show bobedx cum1
                with flash
                call decreaselust(50) from _call_decreaselust_6
                bot"There's n-nothing you can do to stop my r-reactions!"
                $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show bobedx cum2
                with longerflash
                $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                call decreaselust(50) from _call_decreaselust_7
                bo"*Panting*"
                bot"I reckon things are about to get much worse in that regard..."
                bot"I am losing my fucking mind over you!"
                show bobedx 6 with dissolve:
                    alpha 0.15
                show hina closet4 with dissolve
                hin"*Phew* Done with the closet too. Now to pick up the laundry..."
                bot"Time to put on my own little show..."
                show blackscreen zorder 150 with dissolve
                hide hina closet4
                hide hinabobedroom border
                "You close your eyes..."
                show hina closet4t:
                    zoom 0.6
                
                show fullblack zorder 200
                hide blackscreen with dissolve
                show eyehalfopen zorder 200
                hide fullblack
                hide eyeclosed
                show hina:
                    easein 1 xalign 0.5
                with dissolve
                bo"..."
                pause 0.2
                show eyeclosed zorder 200 with dissolve
                bo"*Fakes yawning*"
                show eyefullopen zorder 200
                hide eyeclosed with dissolve
                pause .2
                
                hide eyehalfopen with dissolve
                bo"[hin_rel]?"
                show hina at smallshake
                pause 0.3
                show hina closet5t with dissolve
                with dissolve
                hin"Oh, [bo_name_stutter]!" with vpunch
                label testjump:
                bot"Fuck me, her tits were almost bursting out!"
                 
                hide eyefullopen with dissolve
                bot"She shyly turned away as soon as she took notice of me..."
                bot"I am not complaining though... her ass might be the best part about her!"
                bot"Let's see how she reacts to this then!"
                show bobedx cum2 with dissolve:
                    alpha 1.0
                show bobedx 2 with dissolve
                bo"Morning [hin_rel], you are looking real nice from behind. Thanks for the show!"
                show hina at smallshake
                call changeObedience("Hinata",1,"bohin1_hatredpath_menu_withthis") from _call_changeObedience_11
                hin"W-what? What does that even mean..."

                hide hina
                
                show hina quest3_final
                with dissolve
                hin"I'll be out of your hair, I was just wrapping up!"
                hide hina
                hide hinaq1bg
                show hinaq1bg 2
                
                with dissolve
                hin"S-sorry if I disturbed your sleep!"
                show bobedx 2 with dissolve:
                    alpha 1
                bot"You can disturb me anytime [hin_rel]... As long as I get to do that right back at you!"
                bot"Next time I'll push things further!"
                if bohin1_hatredpath_menu_withthis == 0:
                    $ notification("Event option unlocked")
                $ bohin1_hatredpath_menu_withthis += 1

                



            "{color=[obediencecolor]}With flashing you!{/color}" (greyed_out = True,threshold_value_grey=1, threshold_value_show=1, int_value_show=bohin1_hatredpath_menu_withthis, int_value_grey=bohin1_hatredpath_menu_withflashingyou):
                default bohin1_hatredpath_menu_withflashingyou = 0
                bot"With showing you the effect you have on me!"
                bot"But I'll have to be smart about it to not scare you off..."
                hide hina_quest_animation2
                show hina quest1_1t:
                    xpos -0.25
                with dissolve
                hin"This heat is unbearable..."
                show hina closet0 with dissolve:
                    zoom 0.6
                hin"How do you manage to keep your room this messy on the daily [bo_name]...*Sigh*"
                show bobedx 6 with dissolve:
                    alpha 1
                bot"Heh, maybe that's so you can wake me up like this every day [hin_rel]..."
                show hina closet0:
                    easein 2 xpos (-0.5)
                show bobedx 6 with dissolve:
                    alpha 0.15
                bot"She is off to the closet..."
                hide hina
                bot"Time to execute my plan!"
                $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                hide bobedx with dissolve
                show bobedx 1 with dissolve:
                    alpha 1.0
                bot"If I pretend that I've no idea she was in here as she comes out of the closet..."
                show bobedx 1_1 with dissolve:
                    alpha 1.0
                
            
                bot"This might just work..."
                show bobedx 1_2:
                        ypos 200 xzoom 1.0 yzoom 0.85 crop (0.0, 0.0, 1.0, 1.0) matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
                show hinabobedroom border zorder 90:
                    zoom 0.55 yalign 0.5
                show hina closet1:
                    zoom 0.55 yalign 0.5
                show bobedx 1_2:
                    alpha 0.15
                with dissolve

                hin"I am getting so sweaty doing this..."
                show hina closet2 with dissolve
                hin"I'll have to take another shower after I am done..."
                if introsecrethatredcummed == True:
                    bot"You'll be taking plenty of those after I keep covering you with my cum [hin_rel]! Just like that night when you were sleeping..."
                else:
                    bot"You'll be taking plenty of those after you get used to getting covered with my cum [hin_rel]!"
                show hina closet3 with dissolve
                hin"Everything's so dusty..."
                show bobedx 1_2 zorder 200 with dissolve:
                    alpha 1
                bot"I am close but... I need to hold on until...!"
                show bobedx 1_2 with dissolve:
                    alpha 0.15

                show hina at smallshake
                hin"*Sprays and sweeps*"
                hin"There... that should do it!"
                show hina closet5 with dissolve
                hin"Now to pick up the laundry..."
                hint"[bo_name] has been leaving multiple of his underwear lying around lately..."
                hint"Could it be due to his condition? I can't imagine how hard it must be on him..."
                hide hina closet4
                hide hinabobedroom border
                with dissolve
                show hina closet4t with dissolve:
                    zoom 0.7 xalign -0.4
                bot"P-perfect timing, [hin_rel]!"
                show hina closet4t:
                    easein 2 xalign 0.5
                with flash
                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show bobedx 1_2cum1 with dissolve:
                    alpha 1.0
                show hina closet4_1t with Dissolve(1)
                call decreaselust(50) from _call_decreaselust_8
                # show hina at smallshake
                show hina closet4_2t with Dissolve(2)
                show hina at smallshake
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                hin"*Gasps!* [bo_name_stutter]!? "
                show bobedx 1_2cum2:
                    alpha 1.0
                $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                with longerflash
                $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                call decreaselust(50) from _call_decreaselust_9
                show bobedx 1_2cum2 with dissolve:
                    alpha 0.15
                bo"*Panting*"
                bot"Now to put on an act..."
                bo"[hin_rel]!? Why are you in here!" with vpunch
                hide hina
                show hina quest3_2
                with dissolve
                call changeObedience("Hinata",1,"bohin1_hatredpath_menu_withflashingyou") from _call_changeObedience_12
                hin"I-I-i am so s-sorry! I didn't realize you were a-awake!"
                
                show hina quest3_final
                with dissolve
                hin"I'll just... pick up t-this!"
                hide hina
                hide hinaq1bg
                show hinaq1bg 2
                
                with dissolve
                hin"And leave you to it!"
                scene hina leavebobedroom with dissolve
                bo"[hin_rel], wait..."
                scene black with dissolve
                bot"Heh! [hin_rel] was flustered!"
                bot"I can probably come up with some bullshit excuse if she happens to question me..."
                bot"But next time, I'll push things even further!"
                if bohin1_hatredpath_menu_withflashingyou == 0:
                    $ notification("Event option unlocked")
                $ bohin1_hatredpath_menu_withflashingyou+=1


            "{color=[hatredcolor]}I am not settling for shit!{/color}" if bohin1_hatredpath_menu_withflashingyou>=1:
                default bohin1_hatredpath_menu_final = 0
 
                bot"Fuck it! I've had enough of [hin_rel]'s teasing!"
                hide hina_quest_animation2 with dissolve
                pause 0.1
                show hina quest2_5:
                    zoom 0.7 xalign 0.2 ypos 40
                with dissolve
                call changeHatred(1,"bohin1_hatredpath_menu_final",1) from _call_changeHatred_77
                bot"Just look at her! She's just like a strip club whore the way she bends over!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                show bobedx 1 with dissolve:
                    alpha 0.15
                show hina quest2_4 with dissolve:
                    zoom 0.6 ypos 50
                show hina quest2_4:
                    easein 1 xalign 0.0 ypos 60
                bot"I am not about to sit here and do nothing when you pose like that in front of me [hin_rel]"
                hide bobedx 1 with dissolve
                
                show bobedx f1 zorder 100 with dissolve:
                    yanchor 1 yzoom 1.0 matrixtransform ScaleMatrix(1.0, 0.85, 1.0)*OffsetMatrix(0.0, 74.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
                bot"What's the worst that can happen..."
                $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                show bobedx f2 with dissolve
                show bobedx f1 with dissolve
                show bobedx f2 with dissolve
                show bobedx f1 with dissolve:
                    alpha 0.15
                bot"I'll just blame my condition..."
                bo"[hin_rel]?"
                show hina closet5t with dissolve:
                    zoom 0.6 ypos -46 xalign 0.3
                hin"...Huh?"
                $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                show bobedx f2 with dissolve:
                    alpha 0.8
                show bobedx f1 with dissolve
                show bobedx f2 with dissolve
                show bobedx f1 with dissolve:
                    alpha 0.15
                
                if bohin1_3_hinatacoerced == False: #if hatredpath coerced hinata
                    bo"I have to..."
                    hide hina
                    show hina quest3_1:
                        zoom 0.9 ypos 74
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                    hin"[bo_name_stutter]!?" with vpunch
                    hin"W-what are you d-"
                    show hina quest3_final with dissolve 
                    bo"What do you think I am doing!"
                    hide hina
                    hide hinaq1bg
                    show hinaq1bg 2
                    with dissolve
                    bo"You know I need this... I am handling my condition!"
                    scene hina leavebobedroom with dissolve
                    call changeRespect("Hinata", -1,"none") from _call_changeRespect_4
                    hin"You can't just do that in front of me!" with vpunch
                    scene black with dissolve
                    bot"Fuck! I'll have to figure out a way to keep her around..."
                    $ hin_vulnerable_bohin1 = True

                else:
                    bo"You remember our agreement... right?"
                    default bohin1_agreement_hatred = 0 #dialogue
                    hide hina
                    show hina quest3_2:
                        zoom 0.9 ypos 74
                    with dissolve
                    show hina at smallshake
                    hin"[bo_name_stutter]!?" with vpunch
                    show hina at smallshake

                    if bohin1_agreement_hatred == 0:
                        hin"P-please... You can't be doing that in front of me!"
                    elif bohin1_agreement_hatred >=1:
                        hin"A-are you seriously d-doing this again?"
    

       
                    show hina closet4_2t with dissolve:
                        zoom 0.65 pos(227,-37)
                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    show bobedx f2 with dissolve:
                        alpha 1.0
                    show bobedx f1 with Dissolve(0.35)
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with Dissolve(0.35)
                    show hina at smallshake
                    show hina quest3_1 with dissolve:
                        zoom 0.9 ypos 74 xpos -20
                    show hina at smallshake
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with Dissolve(0.35)
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with dissolve:
                        alpha 0.15
                    show hina quest3_2 with dissolve:
                        zoom 0.9 ypos 74
                    
                    if bohin1_agreement_hatred == 0:
                        bo"You are staying right there until I am done."
                        bo"It's much easier to handle my problem with some visual stimuli."
                        hin"[bo_name_stutter], this isn't right... It isn't normal!"
                        bo"Well I am not normal [hin_rel]! Not anymore! Now get back to what you were doing!" with vpunch
                    elif bohin1_agreement_hatred >=1:
                        hin"Y-you cannot be serious!"
                        bo"Oh I am! And just like last time... you'll sit there until I am done!"
                        bo"It's much easier to handle my problem when you are around!."
                        hin"..."
   
                    show hina at smallshake
                    hin"Can I go... p-please?"
                    bo"N-not yet...!"
         
                    show hina quest2_4 with dissolve:
                        zoom 0.6 xalign 0.0 ypos 60  
                    hin"I..."
                    show hina quest2_5 with dissolve:
                        zoom 0.7 xalign 0.2 ypos 40
                    hin"... I'll just pick up your laundry and wrap up then..."
                    show hina_quest_animation3
                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    show bobedx f2 with dissolve:
                        alpha 1.0
                    show bobedx f1 with Dissolve(0.35)
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with Dissolve(0.35)
                    $ renpy.pause(0.7, hard=True)
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with Dissolve(0.35)
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with dissolve:
                        alpha 0.15
                    $ renpy.pause(0.7, hard=True)
                    hide hina with dissolve
                    hin"..."
                    bot"I am close, [hin_rel]!"

                    if bohin1_agreement_hatred == 0:
                        bot"I can't believe you are sticking your ass out like that knowing that I am jerking off to you."
                        bot"It's as if you want me to bust for you!"
                    elif bohin1_agreement_hatred >=1:
                        bot"Keep sticking that fat ass of yours out for me!"
                        bot"I am so close to busting a nut over you!"



                    show bobedx f2 with dissolve:
                        alpha 1.0
                    show bobedx f1 with Dissolve(0.35)
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with Dissolve(0.35)
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with Dissolve(0.35)
                    show bobedx f2 with Dissolve(0.35)
                    show bobedx f1 with dissolve:
                        alpha 0.15
                    bot"Is that what you actually want [hin_rel]!?"
                    bot"Let's find out!"
                    $ hin_broken_bohin1 = True
                    menu bohin1_hatred_endcum:
                        bot"Let's find out!"
                        "{color=[obediencecolor]}Turn around [hin_rel]!{/color}":
                            bo"Hey [hin_rel]!"
                            show bobedx f2 with dissolve:
                                alpha 1.0
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            bo"Turn around for me..."
                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            show bobedx f1 with dissolve:
                                alpha 0.15
                            hide hina_quest_animation3                         
                            show hina closet5t:
                                zoom 0.6 ypos -46 xalign 0.3
                            with dissolve
                            hin"T-turn around...?"
                            show hina closet4_2t with dissolve:
                                zoom 0.65 pos(327,-37)
                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            show bobedx f2 with dissolve:
                                alpha 1.0
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            show bobedx f1 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            show bobedx f2 with Dissolve(0.35)
                            $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                            show bobedx fcum1
                            with flash
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            show hina at smallshake
                            show bobedx fcum1 with dissolve:
                                alpha 0.15
                            show hina quest3_2 with dissolve:
                                zoom 0.9 ypos 74
                            hin"*Gasps* E-eeh!?" with vpunch
                            show bobedx fcum2:
                                alpha 1.0
                            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                            with longerflash
                            show hina quest3_final with dissolve
                            show hina at smallshake
                            call decreaselust(199) from _call_decreaselust_64
                            hin"W-why did you call me o-out for that!"  
                            bo"Why else... I wanted you to see!"
                            show hina at smallshake
                            hin"A-are you out of your m-mind!?" with vpunch
                            $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                            hide hina
                            hide hinaq1bg
                            show hinaq1bg 2
                            with dissolve
                            hin"I... am leaving now!" with vpunch
                            $ dialogue = renpy.call("get_dialogue", bohin1_agreement_hatred,
                                f"*Panting* Holy shit! I can't believe {hin_rel} put up with that..",
                                f"*Panting* Holy shit! I can't believe {hin_rel} put up with that.. AGAIN!")
                            $ renpy.say(bo, dialogue)
                            show hina leavebobedroom zorder 130 with dissolve
                            if bohin1_agreement_hatred == 0:
                                bot"If she is now willing to put up with me using her as stimuli, what else could I push her to do..."
                                $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                show blackscreen zorder 131 with dissolve
                                bot"I wonder..."
                                
                                $ notification ("Event option unlocked")
                                hide bobedx
                                hide hina
                                hide blackscreen
                                show bobedx cum1:
                                    matrixtransform ScaleMatrix(1.0, 0.7, 1.0)*OffsetMatrix(1.0, 158.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
                                with dissolve
                                bot"What If I clean myself up with my briefs..."
                                bot"Maybe I could flash her in the laundry room under the ruse of passing my cum-soaked underwear to her..."
                                scene black with dissolve
                                show bg bb day
                                show boruto box3smirk2
                                with dissolve
                                bot"Should I try that?"
                                default clotheremovetutorial = False
                                if clotheremovetutorial == False:
                                    $ clotheremovetutorial = True
                                    "Try removing your clothes before visiting the 'Laundry Room' after jerking off to [hin_name]."
                                    "To do so, use the 'Action Button' or the 'Information' panel while in your bedroom."
                            else:
                                bot"How far is she willing to go to protect me from this curse! This is getting more exciting day by day..."
                                $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                show blackscreen zorder 131 with dissolve
                                bot"Shall I try... that again?"
                                hide bobedx
                                hide hina
                                hide blackscreen
                                show bobedx cum1:
                                    matrixtransform ScaleMatrix(1.0, 0.7, 1.0)*OffsetMatrix(1.0, 158.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
                                with dissolve
                                bot"Last time it went pretty well!"
                                scene black with dissolve
                                show bg bb day
                                show boruto box3smirk2
                                with dissolve
                                bot"I should undress if I want to flash her again!"
                            default bohin3_surpriselaundry = False
                            $ bohin3_surpriselaundry = True
                            $ hin_vulnerable_bohin1 = True
                            $ bohin1_agreement_hatred += 1 #dialogue





                        "Locked (WIP)":
                            dev"WIP"
                            jump bohin1_hatred_endcum

                        "Locked (WIP)":
                            bo"I am..."
                            dev"WIP"
                            jump bohin1_hatred_endcum
                            
                        


            "locked" if bohin1_hatredpath_repeat_cum <1:
                "Complete previous option first"
                jump bohin1_hatredpath_menu

            "locked" if bohin1_hatredpath_repeat_cum <2:
                "Complete previous option first"
                jump bohin1_hatredpath_menu


            



        scene black with dissolve
        $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        "You put on some clothes and get up..."
        $ bohin1_hatredpath_repeat_cum += 1
        $ bohin1_hatredpath_repeat +=1
        jump wakeupend




    else:
        bot"Fun's over I suppose..."
        show hina quest1_4t with dissolve:
            zoom 1.1 xpos -100 ypos -50
        #repeatable
        $ dialogue = renpy.call("get_dialogue", wakeupmenu_repeat,
            "Oh, I am so sorry [bo_name_stutter]!",
            "D-did I wake you up again? I am sorry!")
        $ renpy.say(hin, dialogue)
        $ dialogue = renpy.call("get_dialogue", wakeupmenu_repeat,
            "You should be!",
            "Damn it [hin_rel], do you never learn!?")
        $ renpy.say(bo, dialogue)
        show hinaq1bg 2
        show hina quest3_final
        with dissolve
        $ dialogue = renpy.call("get_dialogue", wakeupmenu_repeat,
            "I'll be leaving you right away...",
            "I am sorry again, I just had to pick up your laundry. I'll be going now!")
        $ renpy.say(hin, dialogue)
        bo"Good..."
        hide hina with dissolve
        show bobedx with dissolve:
            alpha 1
        bot"God-damn it [hin_rel]... You are making me go crazy!"
        hide bobedx
        show bobedx 4:
            alpha 1
        with dissolve
        bot"I am going to need another release soon before I do some crazy shit...."
        
        scene black with dissolve
        $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        "You put on some clothes and get up..."
        $ bohin1_hatredpath_repeat += 1
        jump wakeupend
