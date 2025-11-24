label empty_bathroom_actions:
    call enableaction from _call_enableaction_24
    menu:
        "..."
        "Take a Shower":
            jump take_a_shower
        "Return":
            pass
    call showUIhouse from _call_showUIhouse_38
    $ ui.interact()

transform transparency_cycle(min_alpha=0.7, max_alpha=1.0, cycle_time=2.0):
    # First preserve ALL current positioning with Function
    
    align (0.5, 1.0)
    zoom 1.0
    subpixel True
    alpha min_alpha
    block:
        linear cycle_time/2.0 alpha max_alpha
        pause 0.5
        linear cycle_time/2.0 alpha min_alpha
        repeat


label take_a_shower:
    if day_part == 4:
        bot"It's too late for that."
        call showUIhouse from _call_showUIhouse_72
        $ ui.interact()
    $ chance = random.random() < 0.4
    default shower_curtain_on = True
    default shower_erection_on = False
    default shower_masturbate = False
    $ shower_masturbate = False
    $ shower_curtain_on = True
    $ shower_erection_on = False
    bot"Might as well take a shower..."
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/showering.opus", channel="sfx2", loop=True, relative_volume = 1)
    "..."
    scene bh_boshower 1
    show bathroom_curtains at transparency_cycle(0.82, 1, 4)
    show particleFog_low
    with dissolve
    call increaselust(5) from _call_increaselust_239
    bo"Even something as coming in contact with warm water is enough to arouse me..."
    menu:
        "..."
        "Pull the Curtain":
            $ shower_curtain_on = False
            bo"Why do people do this anyway..."
            $ renpy.sound.play("/audio/soun_fx/curtainopening.opus", channel="sfx1", loop=False, relative_volume = 0.6)
            hide bathroom_curtains with fade

            bo"It's not like there's anybody else in the bathroom!"
        "Leave it be":
            pass

    call checkLust(60) from _call_checkLust_17
    if percentage >= 60:
        $ shower_erection_on = True
        show bh_boshower 1_1 with dissolve
        bo"F-fuck! Can't even relax while showering with this damn curse of mine..."
        menu:
            bo"F-fuck! Can't even relax while showering with this damn curse of mine..."
            "Take care of it":
                bo"I should probably do something about it..."
                $ shower_masturbate = True
                $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                show bh_boshower 3 with dissolve

            "Leave it be...":
                bo"D-damn it! Can't do much about it without some stimuli..."
                bo"Better keep my mind off of it for now."
            
    else:
        bo"..."
    $ renpy.sound.play("/audio/soun_fx/whistling.opus", channel="sfx1", loop=False, relative_volume = 0.4)
    bo"*Whistling*"
    if chance:
        jump hinata_knocks_bathroom
    else:

        if day_part == 2 or day_part == 3:
            jump himawari_outside_bathroom
        else:

            call randomCheck("Nothing interesting happened this time...") from _call_randomCheck

            stop sfx2 fadeout 3
            scene black with dissolve
            if shower_masturbate == True:
                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                with flash
                call decreaselust(40) from _call_decreaselust_125
            scene bg bathroom_new
            show boruto embarassed at center
            with dissolve
            bot"I am feeling a little better after that..."
            scene black with dissolve
            jump action_taken
        pass

image black_border = Solid("#000000", xsize=15, ysize=config.screen_height)

label hinata_knocks_bathroom:
    $ initialize_replay_defaults()
    call randomCheck(text="Someone's knocking on the door!") from _call_randomCheck_1
    $ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx1", loop=False, relative_volume = 0.8)
    "*Knocking on door*" with vpunch
    if shower_masturbate == True: 
        show bh_boshower 2 with dissolve
    elif shower_erection_on == True:
        show bh_boshower 1_1 with dissolve
    else:
        show bh_boshower 1 with dissolve

    show hin_outside_bath 0:
        xalign 1.0
        xzoom -1
        fit "contain"  # Preserves aspect ratio
        ysize config.screen_height
    show black_border:
        xpos 750
    with dissolve

    hin"Is there someone inside...?"
    bot"[hin_rel_stutter]?"
    menu shower_menu_hinata:
        bot"[hin_rel_stutter]?"
        "Answer her":
            if shower_masturbate == True:
                bo"I am inside, [hin_rel]. Give me some t-time..."
                hin"Oh, sorry! I'll just wait for you to be done then..."
                bo"Okay..."
                show bh_boshower 3 with dissolve
                $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                bo"M-might need a while t-though..."
                bot"W-would be nice if I had some help..."
                show hin_outside_bath 1 with dissolve
                hint"His voice was shaky..."
                show hin_outside_bath 0 with dissolve
                hin"Is... everything alright?"
                $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                bo"Y-yeah... I am j-just..."
                show hin_outside_bath 2 with dissolve
                hin"O-oh!" with vpunch
                hint"What am I doing! He's probably dealing with his..."
                hide hin_outside_bath with dissolve
                hin"T-take your time! I'll leave you to it..."
                scene black with dissolve
                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                with flash
                call decreaselust(30) from _call_decreaselust_126
                stop sfx2 fadeout 1
                scene bg bathroom_new
                show boruto surprised2 at center with dissolve
                bot"I am feeling somewhat better after that..."
                scene black with dissolve
                jump action_taken

            else:
                bo"I am inside, [hin_rel]. I need a few more minutes..."
                show hin_outside_bath 1 with dissolve
                hin"Oh, sorry! I'll just wait for you to be done then..."
                hide hin_outside_bath
                hide black_border
                with dissolve
                bo"I'll be quick, just for you!"
                call changeRespect("Hinata",1) from _call_changeRespect_208
                hin"T-thank you, take your time if you need to though!" with vpunch
                stop sfx2 fadeout 1
                scene bg bathroom_new
                show boruto normal at center
                with fade
                bot"Feeling refreshed!"
                jump action_taken
        "Stay silent...":
            bot"What if I don't respond..."
            bo"..."
            hint"Unoccupied it seems..."
            hint"How many times do I have to tell these two to leave the bathroom door open when it's unoccupied!"
            hide hin_outside_bath
            hide black_border
            with dissolve
            hint"*Sigh*..."

            $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            show bathroom_door_open with dissolve
            show hina_bathroom_lost 0:
                xpos 1500 fit "contain" ysize config.screen_height
            show hina_bathroom_lost:
                easein 2 xpos 750
            "[hin_name] entered the room facing away from you..."
            show hin_inside_bath 1 with dissolve
            hint"Wait a second, the water's on!" with vpunch
            hide hin_inside_bath with dissolve
            show hina_bathroom_lost at smallshake
            hin"[bo_name_stutter], is that you?"
            hin"S-sorry! I tried knocking but..."
            hin"Guess you didn't hear me. But don't worry I won't look!"
            menu:
                hin"Guess you didn't hear me. But don't worry I won't look!"
                "Try to flash her!" if shower_curtain_on == False and shower_erection_on == True:
                    bot"I may be able to pull this off If I am smart about it!"
                    bo"You are r-right, I didn't hear you knocking..."
                    bo"But It's okay [hin_rel]. Feel free to do your thing..."
                    hin"R-right. I think I must have dropped an earring of mine around here..."
                    show hina_bathroom_lost at smallshake
                    hin"But I can't find it around the sink..."
                    bo"Maybe it's around the shower?"
                    hin"Do you see anything in there?"
                    bo"I am a bit preoccupied, you know..."
                    bo"But you can look for it yourself if you want..."
                    hin"Hmm... I'll come by after you are done I suppose."

                    hide hina_bathroom_lost
                    show hina quest3_2:
                        xpos 400 fit "contain" ysize config.screen_height
                    with dissolve
                    hin"Sorry for the intru-"
                    hide hina
                    show hina_bathroom_lost 1:
                        xalign 0.8 fit "contain" ysize config.screen_height
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                    hin"*Gasps*!" with vpunch
                    hin"[bo_name_stutter]! W-why is..."
                    hide hina_bathroom_lost
                    show bh_boshower 2
                    with fade
                    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx1", loop=False, relative_volume = 0.7)
                    show hin_outside_bath 2:
                        xalign 1.0
                        xzoom -1
                        fit "contain"  # Preserves aspect ratio
                        ysize config.screen_height
                    show black_border:
                        xpos 750
                    with dissolve
                    hin"G-good heavens [bo_name]! W-why did you not say anything?" with vpunch
                    call changeHatred(1) from _call_changeHatred_166
                    bo"Sorry! Didn't want to scare you after you barged in..."
                    hin"B-barged in? I tried knocking! Besides, why are you not using the curtain in the first place!" with vpunch
                    show bh_boshower 1_1 with dissolve
                    bo"Well, I wasn't expecting company now, was I?"
                    bot"She is not having it, I fucked up!"
                    show hin_outside_bath 1 with dissolve
                    hin"Don't get snarky with me, [bo_name]! You could have done something a-about this..." with vpunch
                    show hin_outside_bath 0 with dissolve
                    call changeRespect("Hinata", -1) from _call_changeRespect_209
                    hin"Don't just s-stand behind your [hin_rel_mother] looking like that..."
                    hin"And you better do something about your condition. You looked s-swollen down t-there [bo_name]!" with vpunch
                    hin"If you need time alone you just have to say so, okay?"
                    bo"R-right... Sorry, I suppose."
                    hide hin_outside_bath
                    hide bathroom_door_open
                    hide black_border
                    with fade
                    call increaselust(10) from _call_increaselust_240
                    bot"I need more than time alone, [hin_rel]..."
                    scene black with dissolve
  
                    stop sfx2 fadeout 1
                    scene bg bathroom_new
                    show boruto bonersurprised at center
                    with dissolve
                    bot"Now what do I do with this..."
                    scene black with dissolve
                    jump action_taken


                "Curtain's on anyway..." if shower_curtain_on == True and shower_erection_on == True:
                    bo"It's not a big deal [hin_rel]. Curtain's on anyway..."
                    hin"R-right. I think I must have dropped an earring of mine around here..."
                    show hina_bathroom_lost at smallshake
                    hin"But I can't find it around the sink..."
                    bo"Maybe it's around the shower?"
                    hin"Do you see anything in there?"
                    scene black with dissolve
                    bo"N-not really..."
                    show hin_inside_bath 1
                    show full_curtain at transparency_cycle(0.9,1,3)
                    show particleFog_low
                    with dissolve
                    hin"Bummer..."
                    bot"Although I do see you, [hin_rel]. If I squint my eyes hard enough that is..."
                    bot"Which means she can probably see me too from the other side!"
                    scene bh_boshower 1_1
                    show bathroom_curtains at transparency_cycle(0.9,1,3)
                    show particleFog_low
                     
                    show hina_bathroom_lost 0:
                        fit "contain"  # Preserves aspect ratio
                        ysize config.screen_height
                        xpos 750
                    with dissolve
                    bot"Which means if you were to turn around, you'd be met by..."
                    show bh_boshower 2 with dissolve
                    bot"W-what am I even thinking. flashing my own [hin_rel]..."
                    hide hina_bathroom_lost
                    show hina_bathroom_lost 1:
                        fit "contain"  # Preserves aspect ratio
                        ysize config.screen_height
                        xpos 550
                    with dissolve
                    hin"Well, I'll leave you to it then..."
                    show hina_bathroom_lost at smallshake
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                    hint"*Gasp* ...Is t-that!?" with vpunch
                    hin"Y-you okay in there?"
                    bo"Y-yeah. S-something wrong?"
                    show hin_outside_bath 1:
                        xzoom -1
                        xalign 1.0
                        fit "contain"  # Preserves aspect ratio
                        ysize config.screen_height
                    show black_border:
                        xpos 750
                    hide hina_bathroom_lost
                    $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx1", loop=False, relative_volume = 1.0)
                    with fade
                    call changeObedience("Hinata",1) from _call_changeObedience_130
                    hin"N-no, just making sure! I'll leave you to it then..."
                    show hin_outside_bath 0 with dissolve
                    hint"He must be struggling with his condition again..."

                    scene black with dissolve
                    hint"I hope he'll be alright by himself..."
                    stop sfx2 fadeout 1
                    scene bg bathroom_new
                    show boruto normal at center
                    with dissolve
                    bot"I am feeling somewhat better after that..."
                    scene black with dissolve
                    jump action_taken

                "{color=[hatredcolor]}Curtain's on anyway! (Lie){/color}" if shower_curtain_on == False and shower_erection_on == True and hatred >= 15:
                    bo"Not like it matters [hin_rel]. Curtain's hiding the goods..."
                    hin"R-right. I think I must have dropped an earring of mine around here..."
                    show hina_bathroom_lost at smallshake
                    hin"But I can't find it around the sink..."
                    bo"Maybe it's around the shower?"
                    hin"Do you see anything in there?"
                    show bh_boshower 3 with dissolve
                    bo"Oh? I think I do!"
                    hide hina_bathroom_lost
                    show hina quest3_2:
                        xpos 400 fit "contain" ysize config.screen_height
                    with dissolve
                    hin"Ah! Thank the-"
                    hide hina
                    show hina_bathroom_lost 1:
                        xalign 0.8 fit "contain" ysize config.screen_height
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                    hin"*Gasps*!" with vpunch
                    hide hina_bathroom_lost
                    show bh_boshower 2
                    with fade
                    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx1", loop=False, relative_volume = 0.7)
                    show hin_outside_bath 2:
                        xalign 1.0
                        xzoom -1
                        fit "contain"  # Preserves aspect ratio
                        ysize config.screen_height
                    show black_border:
                        xpos 750
                    with dissolve
                    hin"[bo_name_stutter]! W-why did you do that!?" with vpunch
                    call changeHatred(1) from _call_changeHatred_167
                    bot"Hehehe! She got a full glimpse of my cock!"
                    bo"Do what, [hin_rel]?"
                    hin"You said the curtain was d-drawn!"
                    show bh_boshower 3 with dissolve
                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                    bo"Sorry, must have made a mistake!"
                    show hin_outside_bath 1 with dissolve
                    hint"Did he... do that intentionally?" with vpunch
                    show hin_outside_bath 0 with dissolve
                    call changeRespect("Hinata", -1) from _call_changeRespect_210
                    hin"Y-you have to be more careful, [bo_name]!" with vpunch
                    hin"If you need time alone you just have to say so, okay?"
                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                    "You thought you might as well finish what you started..."
                    bo"R-right, right!"
                    hide hin_outside_bath
                    hide bathroom_door_open
                    hide black_border
                    with fade
                    bot"I need more than time alone, [hin_rel]..."
                    scene black with dissolve
                    bot"I need..."
                    $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                    with flash
                    bot"...you!"
                    call decreaselust(30) from _call_decreaselust_127
                    stop sfx2 fadeout 1
                    scene bg bathroom_new
                    show boruto sceeming at center
                    with dissolve
                    bot"I am feeling better after that!"
                    scene black with dissolve
                    jump action_taken



                "Discreetly try to flash your erection!" if shower_curtain_on == True and shower_erection_on == True:
                    bo"Curtain's on anyway [hin_rel]..."
                    hin"R-right. I think I must have dropped an earring of mine around here..."
                    bot"I wonder if I could..."
                    show bathroom_curtains:
                        easein 0.3 xalign 1.35
                    show bh_boshower 2 with dissolve
                    bot"Just enough to play it off as an accident..."
    
                    show hina_bathroom_lost at smallshake
                    hin"But I can't find it around the sink..."
                    bo"Maybe it's around the shower?"
                    hin"Do you see anything in there?"
                    show bh_boshower 3 with dissolve
                    bo"Not quite..."
                    hin"Bummer. I'll let you wrap up then..."
                    hide hina_bathroom_lost
                    show hina quest3_2:
                        xpos 400 fit "contain" ysize config.screen_height
                    with dissolve
                    hin"I guess I'll-"
                    hide hina
                    show hina_bathroom_lost 1:
                        xalign 0.8 fit "contain" ysize config.screen_height
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                    hin"*Gasps*!" with vpunch
                    hint"Is he!? He must have not realized..."
                    bo"Something wrong [hin_rel]? You cut yourself off..."
                    show hina_bathroom_lost at smallshake
                    hint"H-his condition is flaring up! I s-should leave him alone..."
                    hin"N-no! Nothing's wrong, sorry for disturbing!"
                    hide hina_bathroom_lost
                    show bh_boshower 2
                    with fade
                    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx1", loop=False, relative_volume = 0.7)
                    show hin_outside_bath 2:
                        xalign 1.0
                        xzoom -1
                        fit "contain"  # Preserves aspect ratio
                        ysize config.screen_height
                    show black_border:
                        xpos 750
                    with dissolve
                    bot"She sounded flustered! She must have caught a glimpse of it. Hehe!"
                    hint"That was awkward, but at least he didn't realize..." with vpunch
                    call changeObedience("Hinata", 1) from _call_changeObedience_131
                    scene black with dissolve
                    hint"I hope at least!"
                    stop sfx2 fadeout 1
                    scene bg bathroom_new
                    show boruto sceeming at center
                    with dissolve
                    bot"I am feeling better after that!"
                    scene black with dissolve
                    jump action_taken
                "{color=[hatredcolor]}Jerk off to her!{/color}" if shower_curtain_on == False and shower_masturbate == True:
                    bot"You can't just interrupt me and expect me not to use use, [hin_rel]!"
                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                    show bh_boshower 3 with dissolve
                    bo"You are right, I didn't hear you knocking at all!"
                    show hin_inside_bath 1 with dissolve
                    
                    hin"R-right. I think I must have dropped an earring of mine around here..."
                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                    bo"You do your thing, and I'll do mine..."
                    bot"Hehe! Would be nice if you bent that sweet ass a little more [hin_rel]!"
                    
                    bo"Where is it, where is it..."
                    show hin_inside_bath 2 with dissolve
                    hin"Do you see anything in there, [bo_name]?"
                    bot"All I am seeing is your ass, [hin_rel]!"
                    bot"Come on, let that sweater of yours drop down all the way to your waist."
                    bot"Now t-that would be a sight to behold!" with flash
                    hide hin_inside_bath with dissolve
                    hin"Hello...? [bo_name_stutter]? Are you t-there?"
                    
                    hide hina_bathroom_lost
                    show hina quest3_2:
                        xpos 300 fit "contain" ysize config.screen_height
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                    with flash
                    hin"You haven't said any-"
                    hide hina
                    show hina_bathroom_lost 1:
                        xalign 0.8 fit "contain" ysize config.screen_height
                    show bh_boshower 1_2
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                    hin"*Gasps*!" with vpunch
                    call changeHatred(1) from _call_changeHatred_168
                    bo"T-thank for the help, [hin_rel]!"
                    hide hina_bathroom_lost
                    show bh_boshower 1_2
                    with fade
                    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx1", loop=False, relative_volume = 0.7)
                    show hin_outside_bath 2:
                        xalign 1.0
                        xzoom -1
                        fit "contain"  # Preserves aspect ratio
                        ysize config.screen_height
                    show black_border:
                        xpos 750
                    with dissolve
                    hin"G-good heavens [bo_name]! H-have you been... all this time!?" with vpunch
                    bo"You know about my condition, [hin_rel]. Maybe don't barge in next time..."
                    hin"B-barged in? I tried knocking! Besides, why are you not using the curtain in the first place!" with vpunch
                    show bh_boshower 1_2 with dissolve
                    bo"Well, I wasn't expecting company now, was I?"
                    bot"Although I did enjoy yours!"
                    show hin_outside_bath 1 with dissolve
                    hin"Don't get snarky with me, [bo_name]! You could have said something!" with vpunch
                    show hin_outside_bath 0 with dissolve
                    call changeRespect("Hinata", -2) from _call_changeRespect_211
                    hin"What you did is extremely inappropriate!"
                    hin"Next time, If you need time alone you, you say that much! Understood?" with vpunch
                    bo"R-right, right..."
                    hide hin_outside_bath
                    hide bathroom_door_open
                    hide black_border
                    with fade
                    bot"Time alone, huh? How about time with you next time [hin_rel]..."
                    scene black with dissolve
  
                    stop sfx2 fadeout 2
                    scene bg bathroom_new
                    show boruto sceeming at center
                    with dissolve
                    bot"That's one way to settle my urges..."
                    scene black with dissolve
                    jump action_taken
                    
                "Keep secretely jerking off" if shower_curtain_on == True  and shower_masturbate == True:
                    show bh_boshower 3 with dissolve
                    bot"No harm in it if she never finds out!"
                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                    bo"It's not a big deal [hin_rel]. Curtain's on a-anyway..."
                    hin"R-right. I think I must have dropped an earring of mine around here..."
                    show hina_bathroom_lost at smallshake
                    hin"But I can't find it around the sink..."
                    bo"Maybe it's around the shower?"
                    hin"Do you see anything in there?"
                    scene black with dissolve
                    bo"N-not really..."
                    show hin_inside_bath 1
                    show full_curtain at transparency_cycle(0.9,1,3)
                    show particleFog_low
                    with dissolve
                    hin"Bummer..."
                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                    bot"Although I do see you, [hin_rel]..."
                    bot"Which means she can probably see me too..."
                    bot"F-fuck! I wish I could have you h-help me [hin_rel]..." with flash
                    scene bh_boshower 3
                    show bathroom_curtains at transparency_cycle(0.9,1,3)
                    show particleFog_low
                     
                    show hina_bathroom_lost 0:
                        fit "contain"  # Preserves aspect ratio
                        ysize config.screen_height
                        xpos 750
                    with dissolve
                    bot"Even this faint view of your ass is enough to make me c-cum..." with flash
                    hide hina_bathroom_lost
                    show hina_bathroom_lost 1:
                        fit "contain"  # Preserves aspect ratio
                        ysize config.screen_height
                        xpos 550
                    with dissolve
                    hin"Doesn't seem to be around here after all..."
                    bo"[hin_rel_stutter]..." with flash

                    show hina_bathroom_lost at smallshake
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                    hin"You sound... s-stressed! Everything okay?"
                    hint"*Gasp* Is he...!?" with vpunch
                    bot"She's... turned around. S-she's watching me!" with flash
                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                    with longerflash
                    show bh_boshower 1_2 with dissolve
                    call decreaselust(60) from _call_decreaselust_128
                    hin"...Y-you okay in there?"
                    bo"Y-yeah! *Heavy breathing* Is s-something wrong?"
                    hin"N-n-no! Sorry for the intrusion! I'll leave you to it..." with vpunch
                    show hin_outside_bath 1:
                        xzoom -1
                        xalign 1.0
                        fit "contain"  # Preserves aspect ratio
                        ysize config.screen_height
                    show black_border:
                        xpos 750
                        
                    hide hina_bathroom_lost
                    $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx1", loop=False, relative_volume = 1.0)
                    with fade
                    hint"Was he... dealing with his condition?"
                    show hin_outside_bath 0 with dissolve
                    hint"Talk about bad timing!"

                    scene black with dissolve
                    hint"I hope he'll be alright by himself..."
                    scene bh_boshower 1_2 with dissolve
                    bot"Secretly cumming behind my [hin_rel]'s back... I am something else."
                    stop sfx2 fadeout 1
                    scene bg bathroom_new
                    show boruto normal at center
                    with fade
                    bot"At lease I am feeling better after that..."
                    scene black with dissolve
                    jump action_taken
            if shower_erection_on == True:
                pass
            else:
                show hin_inside_bath 2
                show full_curtain at transparency_cycle(0.9,1,3)
                show particleFog_low
                with dissolve
                hin"I think I may have dropped an earring of mine somewhere in here..."
                scene bh_boshower 1_1
                show bathroom_curtains at transparency_cycle(0.9,1,3)
                show particleFog_low
                    
                show hina_bathroom_lost 0:
                    fit "contain"  # Preserves aspect ratio
                    ysize config.screen_height
                    xpos 750
                with dissolve
                show bh_boshower 1 with dissolve
                hide hina_bathroom_lost
                show hina_bathroom_lost 1:
                    fit "contain"  # Preserves aspect ratio
                    ysize config.screen_height
                    xpos 550
                with dissolve
                hin"Doesn't seem to be around here..."
                show hina_bathroom_lost at smallshake
                hin"Sorry for intruding..."
                bo"No problem!"
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                hint"I can almost see through the curtain..." with vpunch
                hin"Well, I'll leave you to it then!"
                bo"..."
                show hin_outside_bath 1:
                    xzoom -1
                    xalign 1.0
                    fit "contain"  # Preserves aspect ratio
                    ysize config.screen_height
                show black_border:
                    xpos 750
                hide hina_bathroom_lost
                $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx1", loop=False, relative_volume = 1.0)
                with fade
                hint"I hope he'll be alright alone. S-something looked off about him..."
                show hin_outside_bath 0 with dissolve
                scene black with dissolve
                stop sfx2 fadeout 1
                bot"That felt nice..."
                scene bg bathroom_new
                show boruto normal at center
                with dissolve
                bot"Right. Better get on with my day!"
                scene black with dissolve
                jump action_taken
            show hin_inside_bath 2 with dissolve
            call increaselust(10) from _call_increaselust_241
            bot"Uuuh. F-fuck. This was probably a bad idea..."
            hide hin_inside_bath with dissolve
            hin"It's not here either it seems..."
            show bh_boshower 1_1 with dissolve
            bo"S-shit..."
            hin"Huh? Did you say something, [bo_name_stutter]?"
            call increaselust(10) from _call_increaselust_242
            bo"Uhm... M-maybe don't t-turn around, [hin_rel]-"
            show hina quest3_2:
                xpos 400 fit "contain" ysize config.screen_height
            hide hina_bathroom_lost 0
            with dissolve
            hin"Are you o-" with vpunch
            hide hina
            show hina_bathroom_lost 1:
                xalign 0.8 fit "contain" ysize config.screen_height
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            hin"*Gasps*!" with vpunch
            hide hina_bathroom_lost
            with fade
            $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx1", loop=False, relative_volume = 0.7)
            show hin_outside_bath 2:
                xalign 1.0
                xzoom -1
                fit "contain"  # Preserves aspect ratio
                ysize config.screen_height
            show black_border:
                xpos 750
            with dissolve
            hin"G-good lord, [bo_name]! Why did you say nothing! W-what is wrong with you?"
            bo"I t-tried..."
            show hin_outside_bath 1 with dissolve
            hin"At least use the curtain! It's there for a reason..." with vpunch
            bo"Sorry, my head was elsewhere..."
            scene black with dissolve
            hin"I'll leave you to it! Remember what Lady Tsunade said, okay?"
            stop sfx2 fadeout 1
            scene bg bathroom_new
            show boruto bonersurprised at center
            with dissolve
            bot"Not sure what I am supposed to do with this!"
            hide boruto with dissolve
            bot"But at least I feel a little refreshed..."
            scene black with dissolve
            jump action_taken


        

label himawari_outside_bathroom:
    $ initialize_replay_defaults()
    call randomCheck(text="Someone's outside the door!") from _call_randomCheck_2
    $ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    "*Knock Knock*" with vpunch
    if shower_masturbate == True:
        bot"S-shit..."
    else:
        bo"I am inside!"
    show bathroom hima_waiting with dissolve:
        xalign 0.5 fit "contain"
    him "Hurry up! You've been in there forever!" with vpunch
    hide bathroom with dissolve
    if shower_masturbate == True:
        bo"Y-yeah well, bad timing! Deal with it..."
    else:
        bo"Yeah well, give me some time!"
    
    him"If you aren't out in a minute or two, I'll spit in your food whenever I get the chance!" with vpunch
    bo"H-huh? No you wouldn't..."
    him"Time's ticking bozo!" with vpunch
    stop sfx2 fadeout 1
    scene black with dissolve
    if hatred > 20:
        bot"This bitch..."
    else:
        bot"This little rascal..."
    if shower_erection_on:
        pass
        
    else:
        stop sfx2 fadeout 1
        scene black with dissolve
        call checkLust(60) from _call_checkLust_18
        scene bg bathroom_new
        show boruto towelmad
        with dissolve
        bot"Better not chance it with this crazy brat..."
        show boruto:
            easein 1 xalign 1.5
        pause 0.5
        $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
        scene black with dissolve
        show aftershower1 with dissolve:
            fit "contain" xalign 0.5
        him"What are you standing there looking stupid for, move!" with vpunch
        menu:
            him"What are you standing there looking stupid for, move!"
            "Give her some space":
                bo"Sure, sure, your grace..."
                scene black with dissolve
                show moveover 0 with fade:
                    xalign 1.0 fit "contain"
                bo"Off you go, princess!"
                $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                him"Hmph!" with vpunch
                menu hima_out_bathroom_menu:
                    him"Hmph!"
                    "{color=[dominancecolor]}Playfully pat her behind!{/color}":
                        call checkDominance(15,"hima_out_bathroom_menu") from _call_checkDominance_43
                        show moveover_look_down 0 with dissolve:
                            zoom 0.53 xalign 0.0 yalign 0.0
                        bo"So dismissive, princess..."
                        show moveover_look_down 1
                        show moveover 0_1
                        with dissolve
                        $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx2", loop=False, relative_volume = 1)
                        "You gently pat her behind as she was walking past you!" with vpunch
                        call increaselust(10) from _call_increaselust_243
                        bo"Could show a little appreciation to your humble servant, you know..."
                        show moveover 2
                        show moveover_look_down 2
                        with dissolve
                        him"D-don't touch my behind, you w-weirdo!" with vpunch
                        scene black
                        show him_aftershower moveover1:
                            fit "contain" xalign 0.5
                        with dissolve
                        bo"Your wish is my command, princess..."
                        him"S-stop acting weird, and stop calling me that!"
                        him"And if my wish is your command, then I wish you disappeared!"
                        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                        him"Hmph!" with vpunch
                        scene black with vpunch
                        $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                        him"...Bozo!"
                        scene bg day:
                            zoom 0.69
                        with dissolve
                        show boruto towelsmirk with dissolve
                        bot"Hehe! Got a good feel of that brat's ass this time..."
                        hide boruto with dissolve
                        $ renpy.sound.play("/audio/soun_fx/showering.opus", channel="sfx2", loop=True, relative_volume = 1)
                        scene bathroom_hima showering
                        show bathroom_curtains at transparency_cycle(0.82, 1, 4)
                        with fade
                        himt"Idiot! He gets on my nerves so much..."
                        himt"To t-think he can just touch my behind like that. Is he stupid!?"
                        scene black with vpunch
                        stop sfx2 fadeout 2
                        himt"I'll get back to him somehow..."
                        default hima_bathroom_touchass = False
                        $ hima_bathroom_touchass = True

                        jump action_taken

                    "Stare at her ass":
                        show moveover_look_down 0 with dissolve:
                            zoom 0.53 xalign 0.0 yalign 0.0
                        call increaselust(10) from _call_increaselust_244
                        bot"Nice view you are giving me when you are standing like that, [him_name]..."
                        show moveover 2
                        hide moveover_look_down
                        with dissolve
                        call changeRespect("Himawari", -1) from _call_changeRespect_212
                        him"W-what the hell are you staring at, you w-weirdo..." with vpunch
                        scene black
                        show him_aftershower moveover1:
                            fit "contain" xalign 0.5
                        with dissolve
                        bo"N-nothing..."
                        him"Can you stop being weird for one second?" with vpunch
                        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                        him"Hmph!" with vpunch
                        scene black
                        $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                        him"Retard!" with vpunch
                        scene bg day:
                            zoom 0.69
                        with dissolve
                        show boruto towelmad with dissolve
                        bot"Damned brat..."
                        hide boruto with dissolve
                        bot"Can't even sneak a look without her going ballistic..."
                        jump action_taken
                    "Leave her be":
                        scene black with dissolve
                        bo"*Sigh...*"
                        show him_aftershower moveover1:
                            fit "contain" xalign 0.5
                        with dissolve
                        "You push yourself aside, allowing her to get on with her shower..."
                        call changeRespect("Himawari", 1) from _call_changeRespect_213
                        him"T-thanks..." with vpunch
                        bo"For what?"
                        scene black
                        $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                        pause 0.2
                        him"For not acting like a retard for once!" with vpunch
                        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                        him"Teehee!"
                        scene bg day:
                            zoom 0.69
                        with dissolve
                        show boruto towelmad with dissolve
                        bot"Damned brat..."
                        hide boruto with dissolve
                        jump action_taken
            "Flash her 'accidentally'":
                bot"Hehe... I can just pretend it was an accident!"
                him"Hey! Are you deaf? I said MOVE!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                show aftershower1_naked with dissolve:
                    zoom 1.25 yalign 1.0
                "You let your towel drop off pretending to be unaware of it..."
                bo"Huh? Did you say something? I can't hear y-"
                show aftershower1_naked:
                    easein 0.2 yalign 0.35
                pause 0.2
                scene aftershower_boner 1_6 with dissolve:
                    zoom 1.25 yalign 0.35
                him"Ee-e-ew!" with vpunch
                show aftershower_boner 1_7 with dissolve
                him"W-w-w-what the HELL is THAT!" with vpunch
                call increaselust(10) from _call_increaselust_245
                bo"W-what are you talking abou-"
                scene black with vpunch
                $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                pause 0.2
                call changeRespect("Himawari", -1) from _call_changeRespect_214
                him"DON'T JUST LET YOUR TOWEL DROP OFF YOU M-MUTANT!" with vpunch
                scene bg day:
                    zoom 0.69
                with dissolve
                show boruto towelsmirk with dissolve
                bot"Hehe! How about that! Damned brat..."
                bot"Although now I'll have to deal with this somehow..."
                hide boruto with dissolve
                jump action_taken

    stop sfx2 fadeout 1
    scene black with dissolve
    call checkLust(60) from _call_checkLust_19
    bot"That gives me an idea though!"
    scene bg bathroom_new
    show boruto towelsmirk
    with dissolve
    bot"I wanna see how she reacts to this!"
    show boruto:
        easein 1 xalign 1.5
    pause 0.5
    $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    scene black with dissolve
    bot"Hehe!"
    show aftershower_boner 1 with dissolve:
        fit "contain" xalign 0.5
    him"What are you standing there looking stupid for, move!" with vpunch
    show aftershower_boner 0 with dissolve
    bo"Not as stupid as y-" with vpunch
    call increaselust(10) from _call_increaselust_246
    bot"Didn't expect her to be standing out here naked!"
    show aftershower_boner 1 with dissolve 
    bot"Better keep my cool!"
    scene aftershower_boner 1 with dissolve:
        zoom 1.3 xalign 0.0 yalign 0.3
    him"I said move, bozo!" with vpunch
    show aftershower_boner 1_1 with dissolve
    show aftershower_boner:
        easein 3 yalign 0.5
    him"Has the doctor also diagnosed you with loss of hearing?"
    him"And what's with the lump on your waist!"
    scene black
    show aftershower_boner 1_1:
        fit "contain" xalign 0.5
    with dissolve
    him"You turning into a m-mutant or something?"
    bo"I don't know what you are talking about..."
    show aftershower_boner 1_3 with dissolve
    bo"AAAARGH!" with vpunch
    him"Sure you don't! Did I just find your weak spot? Teehee!" with vpunch
    "[him_name] grabbed what she thought was a lump around your waist and squeezed it lightly in her palm..."
    bot"Play it cool... stay c-cool!"
    show aftershower_boner 1_2 with dissolve
    him"You don't move out of the way, I pop this cancerous lump of yours and you die on the spot! Stupid mutant..."
    scene aftershower_boner 1_3 with dissolve:
        zoom 1.3 xalign 0.0 yalign 0.45
    "She squeezed once more, thinking she was inflicting pain to you..." with vpunch
    bo"T-that's not a lump, you stupid b-brat..."
    show aftershower_boner:
        easein 0.44 yalign 0.3
    him"Oh yeah?" with vpunch
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    scene black with vpunch
    "She tried going for it one more time, but this time..."
    pause 0.3
    show aftershower_boner 1_5 with dissolve:
        fit "contain" xalign 0.5
    scene aftershower_boner 1_6 with Dissolve(1):
        zoom 1.3 xalign 0.5 yalign 0.3
    him"W-w-w-what..."
    show aftershower_boner 1_7 with dissolve
    him"W-W-WHAT THE HELL IS T-THAT!" with vpunch
    show aftershower_boner:
        easein 0.44 yalign 0.9
    bo"I thought I told you-"
    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    him"MOOOOOOM! [bo_name_stutter] is t-t-t-turning into a mutant!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    scene bg day:
        zoom 0.69
    show boruto towelsmirk
    bot"Hehe! She is so damn stupid..."
    hide boruto with dissolve
    $ renpy.sound.play("/audio/soun_fx/showering.opus", channel="sfx2", loop=True, relative_volume = 1)
    scene bathroom_hima showering
    show bathroom_curtains at transparency_cycle(0.82, 1, 4)
    with fade
    himt"W-what the heck was that! Is it because of the s-stuff mom talked to be about the other day?"
    himt"And w-why the heck w-was it swollen like that! Did I h-hurt him? Not that I care..."
    himt"More importantly, d-d-d-id I just poke my [him_rel_to_bo]'s t-thing on accident!?" with vpunch
    scene black with vpunch
    stop sfx2 fadeout 2
    himt"Yuck, yuck, YUCK!"

    jump action_taken