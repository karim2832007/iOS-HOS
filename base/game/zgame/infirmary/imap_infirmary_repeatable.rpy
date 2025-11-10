
label visitclinicrepeatable:
    # Check if the discovery event should trigger
    if semenquantity >= 30 and tsunade_discovery_seen == False:
        jump tsunade_discovery

    # Standard repeatable visit
    scene bg infirmaryinside with dissolve
    show boruto worried at center with dissolve
    bot"I should make my way to her office..."
    hide boruto with dissolve
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    ts"Come in..."
    scene bg infirmary room day
    show boruto sceeming at left 
    show tsuna normal at right
    with dissolve
    show screen infirmarymenutopright with dissolve
    ts"I was expecting you..."
    show tsuna:
        easein 1 xalign 0.4
    show tsuna normal2 at center with dissolve
    show boruto surprised2 with dissolve
    ts"Here, take this container..."
    "Tsunade hands you an empty container..."
    show boruto normal with dissolve
    bo"This again..."
    show tsuna normal at right with dissolve
    ts"You know very well what I expect you to do..."
    default tsunadeencounters = 0
    menu infirmary_tsunademenu:
        ts"You know very well what I expect you to do..."
        "Talk":
            bo"Can I talk to you about something?"
            ts"What do you need, [bo_name]?"
            menu:
                ts"What do you need, [bo_name]?"
                "About your experiments...":
                    bo"You said that my semen is important, that it could alter h-history... or something?"
                    show boruto embarassed with dissolve
                    bo"Were you s-serious?"
                    show tsuna serious with dissolve
                    ts"Very much so..."
                    show boruto surprised2 with dissolve
                    bo"How can that be!"
                    ts"It's way too early to draw conclusions, but..."
                    show tsuna smug with dissolve
                    ts"Imagine if a discovery was made that could allow for things outside the realm of scientific reason to occur..."
                    ts"Imagine if bioengineered humans could be selectively bred..."
                    ts"Imagine if a previously infertile woman could now be as fertile as when their wombs were young and fresh..."
                    ts"Imagine if...!" with vpunch
                    show tsuna normal2 with dissolve
                    ts"*Sigh*..."
                    show boruto worried with dissolve
                    bo"I don't know what any of that means..."
                    ts"Let's not get ahead of ourselves..."
                    ts"Look, I'll keep you informed with any of my new findings..."
                    ts"For now, just keep supplying your... resource, Okay?"
                    show boruto normal with dissolve
                    bo"I'll see what I can do..."
                    show tsuna smug with dissolve
                    ts"Take this. You know what I need you to do..."
                    jump infirmary_tsunademenu

                "Can you remind me about your discovery?" if tsunade_discovery_seen == True:
                    # Dialogue summarizing the discovery
                    bo "You mentioned something important you discovered about my... condition?"
                    show tsuna angry
                    ts "YOU ALREADY FORGOT?!" with hpunch
                    show tsuna serious with dissolve
                    ts "Listen carefully, if you don't wanna be stuck paying child support."
                    show boruto surprised2 with vpunch
                    pause 1.0
                    ts "My research indicates your semen possesses unique properties."
                    ts "Properties that could potentially alter biological processes, perhaps even related to fertility or genetic manipulation."
                    show tsuna smug with dissolve
                    ts "It's still early, but the implications are significant."
                    ts "That's why your continued cooperation is vital."
                    show boruto normal with dissolve
                    bo "Right... I understand."
                    show tsuna normal2 with dissolve
                    jump infirmary_tsunademenu

                "Return":
                    jump infirmary_tsunademenu
                
        "Actions":
            menu infirmary_actionmenu:
                ts"You know very well what I expect you to do..."
                "Drop your pants...":
                    jump dropyourpants_0

                "Locked" if droppedpantsonce == False:
                    "Complete other actions to unlock more choices."
                    jump infirmary_actionmenu
                
                "{color=[dominancecolor]}I am going to need you to do more!{/color}" if droppedpantsonce == True:
                    call checkDominance(10, "infirmary_tsunademenu") from _call_checkDominance_6
                    jump infirmary_domstart


                "C-can you please h-help?" if droppedpantsonce == True:
                    jump infirmary_substart
                    

                # --- New option for post-discovery repeatable treatment ---
                "{color=[obediencecolor]}Proceed with 'safe' treatment{/color}" if tsunade_discovery_seen == True:
                    jump repeat_tsunadediscovery
                # --- End new option ---

                "Return":
                    jump infirmary_tsunademenu




























                
        "Information":
            show screen infirmarymenu
            jump infirmary_tsunademenu
      

        "Leave":
            show boruto surprised2 with dissolve
            bo"Wait, I forgot something..."
            show boruto embarassed with dissolve
            bo"Sorry! Gotta go!"
            hide boruto with dissolve
            show tsuna angry with dissolve
            ts"Tsk... Damned brat!"
            hide screen infirmarymenutopright
            if day_part == 1 or day_part == 2 and tsunadeintroduction == True:
                scene black
                scene bg infirmaryday with dissolve
                menu:
                    bot"..."
                    "Visit Tsunade":
                        if tsunadeintroductionseen == False:
                            jump visitclinic
                        else:
                            jump visitclinicrepeatable
                    "Leave":
                        show screen topleftbuttons
                        $ ui.interact()
                    


            elif day_part == 1 or day_part == 2:
                scene black
                scene bg infirmaryday with dissolve
            else:
                scene black
                scene bg infirmary with dissolve


            hide screen housemap
            show screen topleftbuttons
            $ ui.interact()





label dropyourpants_0:
    default droppedpantsonce = False
    default semendtoadd = 0
    $ semendtoadd = 0
    show boruto surprised2 with dissolve
    bo"I think I do..."
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    scene bg infirmary room day with dissolve
    show boruto blue 2_1 with dissolve:
        zoom 0.36
    $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    show tsuna annoyed with dissolve:
        xalign 0.7
    bo"This is w-what you need from me, r-right?"
    show tsuna at smallshake
    ts"W-well, yes but..."
    show tsuna annoyed:
        easein 0.3 xalign 1.0
    if droppedpantsonce == True:
        ts"Y-you know what... N-nevermind. Just get it over with, okay?"
        bo"T-trying! But... I might need some help!"
        jump dropyourpants_0repeat
    else:
        pass
    $ droppedpantsonce = True
    ts"You could do it in a more private area, you know..."
    bo"N-nothing you haven't already seen, right?"
    bo"Besides, if you think this is e-easy for me, you are gravely mistaken..."
    label dropyourpants_0repeat:
    bo"I need some stimulation or nothing will ever come out..."
    show tsuna at smallshake
    ts"Am I to be your stimulant, then?"
    $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    bo"If not y-you, then who else?"
    show tsuna smug with dissolve
    ts"I s-suppose you are right. I might as well oversee the act, given your condition..."
    ts"Don't forget to use the container..."
    hide tsuna with dissolve
    label dropyourpants_0_jumpfromdom:
    ts"In the meantime..."
    scene ts_introfinal with dissolve:
        zoom 0.625 xalign 0.5 yalign 1.0
    show ts_introfinal:
        easein 2 yalign 0.2
    ts"I'll be taking care of some chores around the office..."
    call increaselust(10) from _call_increaselust_75
    show screen parallax1280("ts_introfinal", 0.625) with dissolve
    call showscrollingimage from _call_showscrollingimage_4
    bot"The way she bends forward with her ass hanging out..."
    call increaselust(10) from _call_increaselust_76
    bot"She knows what she is doing!"
    $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    "You kept masturbating while Tsunade 'worked' around the office..."
    bot"I can't take her teasing anymore!"
    menu menutakeherteasinganymore:
        bot"I can't take her teasing anymore!"
        "{color=[dominancecolor]}I need some extra stimulation...{/color}":
            call checkDominance(5,"menutakeherteasinganymore") from _call_checkDominance_7
            $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            bo"Tsunade..."
            ts"...Is there a problem?"
            bo"This isn't working..."
            "Click twice to make a move!"
            $ ui.interact()
            show screen parallax1280("ts_introfinal_1", 0.625) with dissolve
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            bo"I just n-need some..." with vpunch
            ts"*Gasps* H-hey!"
            "Click twice to grope her ass!"
            $ ui.interact()
            call changeDominance(1) from _call_changeDominance_45
            $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            show screen parallax1280("tsunade_infirmaryintroassgrab1", 0.625) with dissolve
            with vpunch
            $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            bo"I just need s-some extra s-stimulation..."
            "You started groping Tsunade's ass with one hand, while using the other to please yourself..."
            ts"O-okay, but this is as far as you will go!"
            menu menuasfarasyouwillgo:
                ts"O-okay, but this is as far as you will go!"
                "{color=[dominancecolor]}Raise her skirt{/color}":
                    call checkDominance(7,"menuasfarasyouwillgo") from _call_checkDominance_8
                    bo"I meant some..."
                    show screen parallax1280("ts_introfinal_3", 0.625) with dissolve
                    call changeDominance(1, "menuasfarasyouwillgo") from _call_changeDominance_46
                    bo"Visual s-stimuli..." with vpunch
                    ts"That wasn't our a-agreement" with vpunch
                    "Click twice to raise her skirt!"
                    $ ui.interact()
                    show screen parallax1280("ts_introfinal_4", 0.625) with dissolve
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                    ts"*Gasp*"
                    ts"Don't even think a-about that!"
                    menu menudonteventhink:
                        ts"Don't even think a-about that!"
                        "{color=[hatredcolor]}Fuck our agreement!{/color}":
                            call checkHatred(25,"menudonteventhink") from _call_checkHatred_7
                            bo"F-fuck our agreement-"
                            "Click twice to...!"
                            hide screen parallax1280
                            hide scrollingimage onlayer screens
                            
                            scene ts_introfinal_4:
                                zoom 0.7 xalign 1.0 yalign 0.5
                            with dissolve
                            call changeHatred(1, "menudonteventhink", 2) from _call_changeHatred_87
                            $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            bo"If you want my semen..."
                            #ts_introfinal_spankhand
                            show ts_introfinal_spankhand with moveinright:
                                zoom 1.5 xalign 0.8 yalign 0.5
                            
                            with vpunch
                            $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                            show ts_introfinal_6:
                                zoom 0.7 xalign 1.0 yalign 0.0
                            hide ts_introfinal_spankhand
                            with dissolve
                            ts"U-ah!" with vpunch
                            bo"Then you better be willing to work for it, bitch!" with vpunch
                            show screen parallax1280("ts_introfinal_6", 0.625) with dissolve
                            call showscrollingimage from _call_showscrollingimage_5
                            ts"Argh! Y-you piece of sh-" with vpunch
                            $ renpy.sound.play("/audio/soun_fx/cum0.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            show screen parallax1280("ts_introfinal_6_cum1", 0.625) with flash
                            $ renpy.sound.play("/audio/soun_fx//glasssmash.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                            bo"Y-you damned h-hag!" with vpunch
                            "You 'dropped' the glass container and instead..."
                            hide screen parallax1280
                            hide scrollingimage onlayer screens
                            
                            scene ts_introfinal_6_cum1:
                                zoom 0.7 xalign 1.0 yalign 0.5
                            with dissolve
                            call changeHatred(1, "menudonteventhink2", 2) from _call_changeHatred_88
                            $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            #ts_introfinal_spankhand
                            show ts_introfinal_spankhand with moveinright:
                                zoom 1.5 xalign 0.8 yalign 0.5
                            $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
        
                            hide ts_introfinal_spankhand
                            with flash
                            $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            show ts_introfinal_6_cum2 with flash:
                                zoom 0.625 yalign 0.6
                            bo"Take this!" with vpunch
                            show screen parallax1280("ts_introfinal_6_cum2", 0.625) with dissolve
                            call showscrollingimage from _call_showscrollingimage_6
                          
                            ts"*Grunts* [bo_name_stutter]! T-the container..." with vpunch
                            $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            bo"Fuck the container. Fuck you and your teasing you hag!"
                            bo"Your ass can contain the r-rest of my cum, b-bitch!"
                            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            show screen parallax1280("ts_introfinal_6_cum3", 0.625) with longerflash
                            bo"Arr-aaaaah!! *Moans*!" with vpunch
                            $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            call decreaselust(100) from _call_decreaselust_77
                            ts"Get your hands off me, you fucking animal!"
                            bo"*Panting* Heh!"
                            bo"Did you think extracting my semen would be either easy, or free?"
                            ts"...S-shut it!"
                            call changetsunadedominance(-5) from _call_changetsunadedominance
                            "Tsunade watched in horror as you brazenly unloaded your pent up rage and desires upon her..."
                            "She understood then and there, that things would perhaps not be as simple as she imagined them to be..."
                            call hidescrollingimage from _call_hidescrollingimage_7
                            scene black
                            ts"Get off m-me, little shit!" with vpunch
                            "Tsunade attempted to extract as much of your semen as she could off her clothes..."
                            "A panicked look on her face betrayed her feeble attempt to stay calm in spite of what just happened..."
                            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            "You take a breather and put your clothes back on while Tsunade cleans up..."
                            $ semendtoadd = 10
                            jump containerfilled

                        "{color=[dominancecolor]}Cum on her ass!{/color}":
                            call checkDominance(10,"menudonteventhink") from _call_checkDominance_9
                            $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            "With one arm you kept Tsunade's skirt raised and with the other, you furiously stroked your cock while enjoying the sight of what was right in front of you!"
                            bo"Y-your beautiful ass... hidden beneath your pantyhose... I t-think I am losing c-control!"
                            ts"Just... shut up and complete your task!" with vpunch
                            bo"I can't think straight! It's c-coming out!" with flash
                            ts"[bo_name_stutter]! The c-containe-"
                            bo"Aaa-arrh!" with vpunch
                            $ renpy.sound.play("/audio/soun_fx/cum0.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            show screen parallax1280("ts_introfinal_4_cum1", 0.625) with flash
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            "You pretended that you lost control, but in reality..." with longerflash
                            ts"W-what the hell did you do, you idiot! Use the d-damn thing-"
                            show screen parallax1280("ts_introfinal_4_cum2", 0.625) with longerflash
                            $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            bo"U-uh... *Moans*" with flash
                            call changeDominance(1,"menudonteventhink", 2) from _call_changeDominance_47
                            "You wanted an excuse to cover Tsunade's ass with your semen. You didn't pay any attention to her complaining..."
                            call decreaselust(90) from _call_decreaselust_71
                            bo"T-tsunade... *Panting*"
                            ts"W-what the hell were you t-thinking!" with vpunch
                            bo"It all just h-happened so quick... And your white laced panties just sent me off!"
                            ts"For goodness's sake! You are the biggest idiot this condition could ever inhibit, you know that?"
                            ts"You are wasting valuable fluids you god-damned imbecile! *Sigh*..."
                            ts"Not to mention you stained my expensive clothing in the process!"
                            call hidescrollingimage from _call_hidescrollingimage_8
                            scene black with vpunch
                            call changetsunadedominance(-3) from _call_changetsunadedominance_1
                            ts"Let go of my skirt and put some damned clothes on while I try to extract as much of your... fluid as I can." with vpunch
                            bo"Right..."
                            bot"Fuck me that felt good! I think enjoy this feeling of slowly breaking Tsunade's boundaries! Hehe..."
                            scene black with dissolve              
                            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            "You take a breather and put your clothes back on while Tsunade cleans up..."
                            $ semendtoadd = 7
                            jump containerfilled


                        "Fill the container to the brim!":
                            $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            call changeDominance(1,"menudonteventhink", 2) from _call_changeDominance_48
                            "With one arm you kept Tsunade's skirt raised and with the other, you furiously stroked your cock while enjoying the sight of what was right in front of you!"
                            bo"How can I not f-fill this little c-container..."
                            bo"When that ass is staring me d-down!" with flash
                            $ renpy.sound.play("/audio/soun_fx/cum0.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                            bo"Arr-ah! *Moans*" with flash
                            ts"Just... shut up and complete your task!" with vpunch
                            bo"O-oh don't you worry! There's m-much more coming, courtesy of your beautiful ass!"
                            $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            ts"Stop saying w-weird stuff and get it over with!" with longerflash
                            call changetsunadedominance(-3) from _call_changetsunadedominance_2
                            "You noticed Tsunade's gaze being firmly fixated on your manhood, it was evident she was intrigued by the situation..."
                            bo"*Moans*..." with vpunch
                            ts"...Are you done?"
                            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            bo"Your ass is f-fucking amazing... T-tsunade!" with longerflash
                            call decreaselust(90) from _call_decreaselust_72
                            "Tsunade's look of intrigue, quickly turned into one of surprise after seeing the abnormal amounts of semen you just ejaculated..."
                            bo"T-tsunade..."
                            ts"That's an... impressive amount of liquid. It'll surely prove to be useful to me!"
                            bo"I think... It's filled to the b-brim... *Panting*"
                            show screen parallax1280("ts_introfinal", 0.625) with dissolve
                            
                            ts"Good, good... Now let go of my skirt and please put some clothes on while I wrap up over here..."
                            call hidescrollingimage from _call_hidescrollingimage_9
                            scene black with dissolve
                            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            "You take a breather and put your clothes back on..."
                            $ semendtoadd = 15
                            jump containerfilled


                "{color=[hatredcolor]}Cum on her!{/color}":
                    call checkHatred(20,"menuasfarasyouwillgo") from _call_checkHatred_8
                    bo"Y-your ass feels so nice, I t-think I am losing c-control!"
                    ts"Just... shut up and complete your task!" with vpunch
                    bo"I can't think straight! It's c-coming out!" with flash
                    ts"[bo_name_stutter]! The c-containe-"
                    
                    bo"Aaa-arrh!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                    $ renpy.sound.play("/audio/soun_fx/cum0.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    show screen parallax1280("ts_introfinal_2_cum1", 0.625) with flash
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    "You squeezed Tsunade's ass and shot an impressive amount of liquid right on to her skirt, dripping down to her pantyhose..." with longerflash
                    ts"W-what the hell did you do you idiot! Use the d-damn thing-"
                    show screen parallax1280("ts_introfinal_2_cum2", 0.625) with longerflash
                    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    bo"U-uh... *Moans*" with flash
                    "She couldn't even finish complaining before you shot another impressive rope of liquid, drenching her legs in the process..."
                    call decreaselust(90) from _call_decreaselust_73
                    bo"T-tsunade... *Panting*"
                    ts"W-what the hell were you t-thinking!" with vpunch
                    bo"I wasn't! It all just h-happened so quick..."
                    ts"You are wasting valuable fluids you god-dmaned idiot! *Sigh*..."
                    call hidescrollingimage from _call_hidescrollingimage_10
                    scene black with vpunch
                    ts"Let go of my ass and put some damned clothes on while I try to extract as much of your... fluid as I can." with vpunch
                    bo"Right..."
                    call changeHatred(1, "menuasfarasyouwillgocumonher", 2) from _call_changeHatred_89
                    bot"Fuck me that felt good! I think enjoy this feeling of breaking Tsunade's boundaries! Hehe..."
                    show ts_introfinal_cum1 with dissolve:
                        zoom 0.625 xalign 0.5 yalign 0.7
                    bot"To see her carefully patting her own ass trying to preserve my semen... it's sorta... arousing!"
                    call increaselust(5) from _call_increaselust_77
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    "You take a breather and put your clothes back on while Tsunade cleans up..."
                    $ semendtoadd = 5
                    jump containerfilled

                "Cum in the container":
                    bo"Y-your ass feels so nice, it's making it so easy for-"
                    ts"Just... shut up and complete your task!" with vpunch
                    bo"I am about to shoot loads of it!" with flash
                    show screen parallax1280("ts_introfinal_2_1", 0.625) with dissolve
                    bo"Aaa-arrh!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                    $ renpy.sound.play("/audio/soun_fx/cum0.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    "You squeezed Tsunade's ass and shot an impressive amount of fluid into the container" with longerflash
                    "You notice Tsunade's gaze lingering on to you..."
                    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    bo"U-uh... *Moans*" with flash
                    "Her gaze was fixated on your manhood, her look of surprise, was quickly turned into one of intrigue..."
                    call changetsunadedominance(-3) from _call_changetsunadedominance_3
                    "She almost seemed unbothered by your incessive groping..."
                    $ renpy.sound.play("/audio/soun_fx/cum0.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    bo"T-tsunade..." with longerflash
                    call decreaselust(90) from _call_decreaselust_74
                    bo"I think... I f-filled it up!"
                    show screen parallax1280("ts_introfinal", 0.625) with dissolve
                    ts"Good, good... Now let go of my behind and please put some clothes on while I wrap up over here..."
                    call hidescrollingimage from _call_hidescrollingimage_11
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    "You take a breather and put your clothes back on..."
                    $ semendtoadd = 7
                    jump containerfilled
                       

        "Keep jerking off":
            $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            bo"T-tsunade..."
            ts"Everything okay back there?"
            bo"I think I am about t-to..."
            menu menukeepjerkingoff:
                bo"I think I am about t-to..."
                "Fill the container...":
                    bo"It's c-coming out!" with flash
                    show screen parallax1280("ts_introfinal_look", 0.625) with dissolve
                    call changetsunadedominance(3) from _call_changetsunadedominance_4
                    "You notice Tsunade discreetly turning around to take a good look at you..."
                    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    bo"U-uh... *Moans*" with flash
                    "Her gaze was fixated on your manhood, her look of surprise, was quickly turned into one of intrigue..."
                    $ renpy.sound.play("/audio/soun_fx/cum0.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    bo"T-tsunade..." with longerflash
                    call decreaselust(75) from _call_decreaselust_75
                    bo"I think... I f-filled it up!"
                    show screen parallax1280("ts_introfinal", 0.625) with dissolve
                    ts"Good, good..."
                    ts"Now, please put on some clothes while I wrap up over here..."
                    call hidescrollingimage from _call_hidescrollingimage_12
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    "You take a breather and put your clothes back on..."
                    $ semendtoadd = 5
                    jump containerfilled
                "{color=[hatredcolor]}Cum on her!{/color}":
                    call checkHatred(10,"menukeepjerkingoff") from _call_checkHatred_9
                    $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    bo"T-the container... I... l-lost it!"
                    ts"W-what-" with vpunch
                    bo"It's c-coming out!" with flash
                    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                    show screen parallax1280("ts_introfinal_cum1", 0.625) with flash
                    ts"[bo_name_stutter]! W-what are-"
                    $ renpy.sound.play("/audio/soun_fx/cum0.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    show screen parallax1280("ts_introfinal_cum2", 0.625) with flash
                    bo"Aaarr-aah!" with vpunch
                    ts"Y-you freaking IDIOT! Use the damned container!"
                    bo"I don't know where it is, but you..."
                    $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    show screen parallax1280("ts_introfinal_cum3", 0.625) with longerflash
                    bo"Y-you are right there... *Panting*"
                    call decreaselust(75) from _call_decreaselust_76
                    call changeHatred(1, "menukeepjerkingoff2", 2) from _call_changeHatred_90
                    bo"M-might as well gather it all up on one place! For your... convenience!"
                    call hidescrollingimage from _call_hidescrollingimage_13
                    scene black with dissolve
                    ts"You are an absolute idiot, you know that?!"
                    "Tsunade spends some time frantically retrieving as much of the semen as she could extract from herself..."
                    $ semendtoadd = 3
                    jump containerfilled






    label containerfilled:
        scene bg infirmary room day
        show boruto surprised2 at left 
        show tsuna serious:
            xalign 0.4
        with dissolve
        show tsuna:
            easein 0.5 xalign 0.8
        call addSemen(semendtoadd) from _call_addSemen
        if semendtoadd == 10:
            show boruto sceeming2 with dissolve
            show tsuna angry with dissolve
            bo"That's quite a lot of fluid you managed to extract, and that's all because of your sexy ass..."
            bo"You should be proud of yourself!"
            show tsuna angry2 with dissolve
            ts"If you think the situation allows for you to act like a piece of shit, think again [bo_name]!"
            show boruto sceeming3 with dissolve
            bo"Hmm, maybe I should stay away from here for a while..."
            show tsuna at smallshake
            ts"W-what do you mean, stay away...?"
            bo"You seen unappreciative, not to mention that you happen to bring out the worst in me..."
            show tsuna annoyed with dissolve
            ts"W-what!? [bo_name_stutter], no! You need to keep showing up, I need your... help."
            call changetsunadedominance(-10) from _call_changetsunadedominance_5
            show tsuna shy with dissolve
            ts"...And it would seem you need m-mine."
            show boruto sceeming with dissolve
            bo"Hmmm? I'll consider it, then..."
        elif semendtoadd == 15:
            show boruto snob with dissolve
            bo"Look! The container is almost overflowing with my cum, hehe!"
            ts"Hand that over!"
            ts"You did... a good job!"
            bo"That's mostly because of you, you know..."
            show tsuna at smallshake
            call changetsunadedominance(-5) from _call_changetsunadedominance_6
            ts"Hmph! This will be very useful in my experimintation. I appreciate your... help."
        else:
            ts"Hand that over!"
            ts"Can't trust you with holding any more of those containers..."
            menu:
                ts"Can't trust you with holding any more of those containers..."
                "Tread carefully, Tsunade...":
                    show boruto snob with dissolve
                    bo"I go through all that effort, and this is what I get?"
                    show boruto sceeming2 with dissolve
                    bo"Careful, Tsunade..."
                    call changetsunadedominance(-5) from _call_changetsunadedominance_7
                    ts"Don't play games with me, [bo_name]!"
                    ts"You know how important this is..."
                    ts"I am expecting more of this at your earliest convenience!"
                    bo"I am sure you do!"

                "Apologize":
                    show boruto embarassed with dissolve
                    bo"*Nervous laughter* S-sorry about that..."
                    call changetsunadedominance(5) from _call_changetsunadedominance_8
                    ts"As long as you keep delivering..."
                    ts"I am expecting more of this at your earliest convenience!"
                    bo"I'll do what I can..."
        show tsuna serious with dissolve
        ts"*Sigh*... Your urges have settled, this session is over!"
        ts"You'll visit me again whenever your condition flares up, understood?"
        show boruto normal with dissolve
        bo"Will do..."
        ts"Remember, we have an important task on our hands! And please, no one hears of this!"
        bo"Mhm..."
        hide tsuna with dissolve
        ts"I'll be in my lab checking... a few things!"
        hide boruto with dissolve
        scene black with dissolve
        "You make your way back home..."
        $ renpy.end_replay()
        jump action_taken

            