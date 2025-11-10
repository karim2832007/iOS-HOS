label infirmary_domstart:
    default infirmary_domstart_1sttime = 0
    if infirmary_domstart_1sttime == 0:
        pass
    else:
        jump infirmary_domstart_repeat
    show boruto snob with dissolve
    bo"I don't think that's going to work any more, Tsunade..."
    show tsuna annoyed with dissolve
    ts"Don't get started [bo_name]..."
    bo"I think it's about time YOU start working for what you want..."
    show tsuna angry2 with dissolve
    hide tsuna
    show tsuna angry2  at smallshake, right
    ts"W-what do you mean?"
    show boruto sceeming2 with dissolve
    bo"You know very well what I mean..."
    show boruto:
        easeout 0.5 xalign 0.7
    pause 0.4
    label replay_infirmary_domstart1:
    $ initialize_replay_defaults()
    if  _in_replay and infirmary_domstart_1sttime >= 1:
        $ tsunadedominance = -21

    scene black with vpunch
    bo"I am tired of all this teasing!"
    show infirmary_dom_lvl1_1 with dissolve
    bo"Ever since our first encounter..."
    bo"Ever since you used me in my sleep for your satisfaction!" with vpunch
    bo"All I could ever think about is burying my cock in between those tits of yours!"
    ts"What do you think you are doing!" with vpunch
    show infirmary_dom_lvl1_2 with dissolve
    bo"What I should have done the first time we met..."
    show infirmary_dom_lvl1_3 with dissolve
    bo"Giving you exactly what you want!" with vpunch
    show infirmary_dom_lvl1_4 with dissolve
    "You push Tsunade with relative ease up against the wall and assertively place your hand next to her..." with vpunch
    "In her surprise by your sudden advances, Tsunade did not exert much resistance..."
    ts"W-what I want? Have you went and lost it,[bo_name]?"
    ts"I told you m-multiple ti-"
    menu:
        ts"I told you m-multiple ti-"
        "Interrupt her":
            bo"What you say..." with vpunch
            bo"...And what you want, are two different things, I've come to realize that about you...Tsunade!"
            bo"You like to tease and watch me struggle with my temptations..."
            ts"W-what? No!"
            bo"You like to think you are in control, don't you?"
            ts"Y-you are wrong..."
            bo"But I think what you really want, is someone to strip you of that authority you like to cling on, and use it against you!"
            call changetsunadedominance(-3) from _call_changetsunadedominance_9
            ts"Y-you are wrong on so many levels!"
        "Let her plead her case...":
            ts"I told you multiple times! What happened back then was a mistake, and it won't happen again!"
            ts"I simply did what I had to do..."

    bo"I don't buy that!" with vpunch
    scene black with vpunch
    ts"I don't care whether you believe me or not!"
    show infirmary_dom_lvl1_5 with dissolve
    "Tsunade pushes you off and sits down on her office chair to gather her thoughts..."
    tst"His condition... It might be getting out of hand!"
    show infirmary_dom_lvl1_5_2 with dissolve
    ts"Look, I understand your frustrations given your condition but..."
    call checkTsunadedominance(-20) from _call_checkTsunadedominance
    
    ts"Your imagination is running wild, you are perceiving things in ways that are simply untrue!"
    bo"My semen, Tsunade... Do you require more of it, or not!" with vpunch
    ts"You know I do..."
    bo"Then you better start helping! It's becoming harder and harder for me you know..."
    scene black with dissolve
    ts"*Sigh*..."
    ts"Just... Lay down on the bed over here..."
    show infirmary_dom_lvl1_6 with dissolve
    "Tsunade lightly pushes you so that you fall on your back on top of the clinic bed..."
    if tsunadedominance >= -20:
        pass
    else:
        call checkTsunadedominance(-20,"infirmary_domstart_pass") from _call_checkTsunadedominance_1
        jump infirmary_domstart_pass
    ts"I am not about to help you with your..."
    "Tsunade took notice of your violent erection pushing against your pants..."
    show infirmary_dom_lvl1_6_1 with dissolve
    ts"...condition. But, perhaps you can help yourself once more..."
    menu:
        ts"...condition. But, perhaps you can help yourself once more..."
        "{color=[dominancecolor]}Reach for her womanhood...{/color}":
            show infirmary_dom_lvl1_7 with dissolve
            call changeDominance(1) from _call_changeDominance_49
            bo"But I need YOU to help, Tsunade..."
            scene black with vpunch
            ts"We can't do that!"
            "Tsunade slaps your hand away and instead..."
            show screen parallax1280("ts_introfinal", 0.625) with dissolve
            call showscrollingimage from _call_showscrollingimage_7
            ts"But you can... w-watch me if it helps."
        "{color=[hatredcolor]}Damn it! (You will pay for this...){/color}":
            bo"You want me to jerk myself off? Again!?" with vpunch
            ts"Y-yes, but..."
            show screen parallax1280("ts_introfinal", 0.625) with dissolve
            call showscrollingimage from _call_showscrollingimage_8
            ts"But you can... w-watch me if it helps."
            bo"Again with the fucking teasing?"
            ts"..."
            bo"Fine, have it your way..."
            call changeHatred(1) from _call_changeHatred_91
            bo"One day you will pay for this you know..."
            call changetsunadedominance(-3) from _call_changetsunadedominance_10
            ts"...!"
            "Tsunade tried to hide her reaction to your comment, but her slight body movements betrayed her surprise..."
    
    jump dropyourpants_0_jumpfromdom

label infirmary_domstart_pass:
    "She took notice of your of your violent erection pushing against your pants..."
    show infirmary_dom_lvl1_6_1 with dissolve
    ts"I will c-consider helping you out, but only if you promise that you'll let me dictate the pace..."
    ts"No more violent outbursts, okay?"
    bo"Heh, still trying to cling on your authoritarian nature I see..."
    menu:
        bo"Heh, still trying to cling on your authoritarian nature I see..."
        "{color=[dominancecolor]}Reach for her womanhood...{/color}":
            show infirmary_dom_lvl1_7 with dissolve
            call changeDominance(1) from _call_changeDominance_50
            bo"I won't abide by that, you know..."
            scene black with vpunch
            ts"...S-stop that!"
            call changetsunadedominance(-3) from _call_changetsunadedominance_11
            "Tsunade lightly pushes your hand away and instead..."
            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            "She wraps her hands around your waist and hesitantly pulls off your pants..."
                
        "{color=[hatredcolor]}No matter! (You'll be begging for my cock soon){/color}":
            bo"No matter, soon enough you will be-" with vpunch
            scene black with vpunch
            call changetsunadedominance(3) from _call_changetsunadedominance_12
            ts"If I am going to help you will at the very least keep it shut!" with vpunch
            bo"Fine, have it your way..."
            call changeHatred(1) from _call_changeHatred_92
            bot"Bitch... Soon enough I'll have you begging for my cock!"
            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            "Tsunade wraps her hands around your waist and pulls off your pants..."
                
    "Your erection quickly sprung up, but Tsunade wasn't caught off guard. She was already familiar with your... potency"
    bo"O-oh!" with vpunch
    show infirmary_dom_lvl1_8 with dissolve
    "With a hesitant look on her face, Tsunade promptly got to work by dropping on her knees and pushing your erect cock in between a small opening of her buttoned shirt, and right through her enormous breasts..."
    "Click twice to continue"
    call clicktwice from _call_clicktwice_9
    ts"...This is what you w-wanted, right?" with vpunch
    scene bg infirmary_dom_lvl1
    show tsunade_infirmarydom_paizuri
    with longerflash
    "Tsunade squeezed her breasts together with her own hands, and started moving her upper body around your cock..."
    show layer master at dizzyflashshort
    bo"Y-es, keep it g-going!"
    ts"S-stop moving, you are s-supposed to let me set the pace!"
    "You occasionally looked for opportunities to thrust your hips upwards and push your cock through her breasts."
    "Every time you did so, you would catch Tsunade by surprise as your cock inched closer and closer to her face..."
    bo"Ar-ah! I w-won't last much longer..."
    ts"Just... Let me know when you are close!"
    ts"We have to use the container!"
    hide tsunade_infirmarydom_paizuri
    show tsunade_infirmarydom_paizuri2
    with dissolve
    bo"T-the container?"
    "You paid no regard to her request..."
    "The sensation was overwhelming... You started violently thrusting knowing full that when the time came..."
    "She would serve as your container!"
    bo"F-fuck the container!" with flash
    show layer master at dizzyflashshort
    bo"I am c-cumming!"
    "Click twice to cum!"
    call clicktwice from _call_clicktwice_10
    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    scene infirmary_dom_lvl1_cum with flash
    ts"Y-you...!"
    show layer master at dizzyflashshort
    bo"G-get ready for m-more!"
    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    scene infirmary_dom_lvl1_cum2 with longerflash
    bo"*Groans* Aaa-arh!"
    ts"You b-bastard!" with vpunch
    "Your exerted enough semen to cover Tsunade's face..."
    "As it slid down her face, she tried her best to prevent it from dripping down any further by squeezing her chest, pooling the remainder of the semen in between it..."
    $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.4)
    bo"*Panting* Heh!..."
    ts"I told you to use the container!"
    bo"I am sorry but your tits felt way too good for me to do that..."
    bo"I couldn't react in time... Besides, you are 'containing' your prized cum pretty good by the looks of it!"
    ts"I am trying to not let it drip down you fucking idiot!"
    scene black with vpunch
    ts"Now help me retrieve the semen..."
    label infirmarydom_repeatend:
    scene bg infirmary room day with dissolve
    show boruto naked2 with dissolve:
        zoom 0.36
    show boruto:
        easein 1 xalign 0.8
    "You strouted around the room proud of your 'work' and went off to fetch a container to help Tsunade gather up your semen..."
    bo"Where's the damn thing..."
    "Your still, cum-dripping cock dangled around Tsunade as she kept waiting for you to fetch her the container while she sat there on her knees, with the breasts still held together..."
    ts"Hurry up!" with vpunch
    menu:
        ts"Hurry up!"
        "Shut it!":
            bo"Shut it! I am looking for the damn thing..."
            ts"It's right there on my desk you imbecile!"
            call changetsunadedominance(-3) from _call_changetsunadedominance_13
            $ semendtoadd = 5
            ts"H-hurry up, the semen is d-drying off on my skin..."
        "Oh there, it is!":
            bo"Oh, found it!"
            $ semendtoadd = 10
        
    show boruto:
        easein 1 xalign -0.5
    scene black with dissolve
    bo"There you go..."
    ts"And put on s-some clothes!"
    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    if semendtoadd == 5:

        call addSemen(5) from _call_addSemen_1
        "Some of the semen dried off on Tsunade's skin before she could extract it..."
    else:
        call addSemen(10) from _call_addSemen_2
    
    scene bg infirmary room day with dissolve
    show boruto snob at left
    show tsuna annoyed at right
    with dissolve
    bo"There you go, happy now?"
    ts"We are n-never doing that again..."
    bo"We'll see about that!"
    show boruto sceeming2 with dissolve
    bo"At least you got what you wanted, right?"
    show tsuna angry with dissolve
    ts"*Scoffs*"
    ts"I think you are the one who got what they wanted..."
    ts"In any case, your urges have settled, this session is over!"
    ts"You'll visit me again whenever your condition flares up, understood?"
    show boruto snob with dissolve
    bo"You can bet on that!"
    ts"Remember, we have an important task on our hands! And please, no one hears of this!"
    bo"Mhm..."
    hide tsuna with dissolve
    ts"I'll be in my lab analyzing your... s-semen."
    hide boruto with dissolve
    scene black with dissolve
    "You make your way back home..."
    $ renpy.end_replay()
    $ infirmary_domstart_1sttime = 1
    jump action_taken


label infirmary_domstart_repeat:
    show boruto snob with dissolve
    bo"I had another idea in mind, Tsunade..."
    show tsuna annoyed with dissolve
    ts"Don't get started [bo_name]..."
    bo"I think it's time YOU start working for what YOU want..."
    show tsuna angry2 with dissolve
    hide tsuna
    show tsuna angry2  at smallshake, right
    ts"You are not t-thinking of..."
    show boruto sceeming2 with dissolve
    bo"You know very well what I am thinking off!"
    show boruto:
        easeout 0.5 xalign 0.7
    pause 0.4
    scene black with vpunch
    
    bo"I am tired of all this teasing!"
    show infirmary_dom_lvl1_1 with dissolve
    bo"Ever since last time..."
    bo"All I could ever think about is burying my cock in between those tits of yours again!" with vpunch
    ts"What do you think you are doing!" with vpunch
    show infirmary_dom_lvl1_2 with dissolve
    bo"I am doing what you need me to do!"
    show infirmary_dom_lvl1_3 with dissolve
    bo"I am giving you exactly what you want!" with vpunch
    show infirmary_dom_lvl1_4 with dissolve
    "You confidence took Tsunade by surprise..." with vpunch
    ts"W-what I want is for you to calm d-down..."
    ts"I told you m-multiple ti-"
    menu:
        ts"I told you m-multiple ti-"
        "Interrupt her":
            bo"What you say..." with vpunch
            bo"...And what you want, are two different things, I've come to realize that about you...Tsunade!"
            bo"You like to tease and watch me struggle with my temptations..."
            ts"W-what? No!"
            bo"You like to think you are in control, don't you?"
            ts"Y-you are wrong..."
            bo"But I think what you really want, is someone to strip you of that authority you like to cling on, and use it against you!"
            call changetsunadedominance(-3) from _call_changetsunadedominance_14
            ts"...You h-have no idea what you are talking about..."
        "Let her plead her case...":
            ts"I told you multiple times! What happened back then was a mistake, and it won't happen again!"
            call changetsunadedominance(3) from _call_changetsunadedominance_15
            ts"I simply did what I had to do..."

    bo"I don't buy that!" with vpunch
    scene black with vpunch
    ts"I don't care whether you believe me or not!"
    show infirmary_dom_lvl1_5 with dissolve
    "Tsunade pushes you off and sits down on her office chair to gather her thoughts..."
    tst"Damn it... T-this is getting out of hand!"
    show infirmary_dom_lvl1_5_2 with dissolve
    ts"Look, I understand your frustrations given your condition but..."    
    ts"Your imagination is running wild, you are perceiving things in ways that are simply untrue!"
    bo"My semen, Tsunade... Do you require more of it, or not!" with vpunch
    ts"You know h-how important that is to m-me, to everyone even!"
    bo"Then you better start helping! It's becoming harder and harder for me you know..."
    scene black with dissolve
    ts"Ok, calm down... I will..."
    ts"Just... Lay down on the bed over here..."
    show infirmary_dom_lvl1_6 with dissolve
    "Tsunade gently pushes you so that you fall on your back on top of the clinic bed..."
    if tsunadedominance <= -20:
        pass
    else:
        show infirmary_dom_lvl1_6_1 with dissolve
        ts"I know you are frustrated, but..."
        ts"This time you will have to settle with watching..."
        scene black with vpunch
        bo"W-what? No!"
        ts"Shut it, [bo_name]!" with vpunch
        bot"Bah... She's getting back her confidence."
        bot"I'll try subjugating her further in the future..."
        call checkTsunadedominance(-20,"dropyourpants_0_jumpfromdom") from _call_checkTsunadedominance_2

    "She knew very well what you needed by now..."
    show infirmary_dom_lvl1_6_1 with dissolve
    call checkTsunadedominance(-20) from _call_checkTsunadedominance_3
    ts"Remember our agreement...?"
    menu:
        ts"Remember our agreement...?"
        "{color=[dominancecolor]}Reach for her womanhood...{/color}":
            show infirmary_dom_lvl1_7 with dissolve
            call changeDominance(1) from _call_changeDominance_51
            bo"Oh I do... you'll get your semen, and you will dictate the pace..."
            bo"And then one day, I'll..."
            scene black with vpunch
            ts"W-wait!"
            "Tsunade slaps your hand away and instead..."
            ts"My pace... remember?"
        "{color=[hatredcolor]}Get on with it... you bitch!{/color}":
            bo"You'll get your semen, and you'll dictate the pace..." with vpunch
            call changeHatred(1) from _call_changeHatred_93
            bo"So get on with it, you bitch!" with vpunch
            ts"...You can at least act appreciative of my h-help."
            bo"I'll consider it..."
            call changetsunadedominance(-3) from _call_changetsunadedominance_16
            bo"If you do a good job working my cock!" with vpunch
            ts"..."
            "Tsunade tried to appear reluctant, But..."
    scene black with dissolve
    "She wrapped her hands around your waist and pulled off your pants..."            
    "Your erection quickly sprung up, but Tsunade wasn't caught off guard. She was already familiar with your... potency"
    show infirmary_dom_lvl1_8 with dissolve
    bo"Good girl..."
    call changetsunadedominance(-2) from _call_changetsunadedominance_17
    "With a hesitant look on her face, Tsunade promptly got to work by dropping on her knees and pushing your erect cock in between a small opening of her buttoned shirt  and right through her enormous breasts..."
    "Click twice to continue"
    call clicktwice from _call_clicktwice_11
    bo"Come on then, work it!"
    ts"...Can you at least keep quiet?"
    scene bg infirmary_dom_lvl1
    show tsunade_infirmarydom_paizuri
    with longerflash
    "Tsunade squeezed her breasts together with her own hands, and started moving her upper body around your cock..."
    bo"Y-es, keep it g-going!"
    "You occasionally looked for opportunities to thrust your hips upwards and push your cock through her breasts."
    "Every time you did so, you would catch Tsunade by surprise as your cock inched closer and closer to her face..."
    ts"Stop moving so much!"
    menu stopmovingsomuch:
        ts"Stop moving so much!"
        "{color=[dominancecolor]}Maybe I wouldn't if you...{/color}":
            call checkDominance(18, "stopmovingsomuch") from _call_checkDominance_10
            bo"M-maybe I wouldn't have to move as much if you did a better job..."
            bo"I bet you that if you used your mouth I'd produce much more semen for you..."
            if tsunadedominance <= -30:
                call checkTsunadedominance(-30) from _call_checkTsunadedominance_4
                label replay_infirmary_domstart2:
                show tsuna_dom2_anim3
                hide tsuna_dom2_anim3
                $ initialize_replay_defaults()

                ts"My... mouth?"
                scene bg infirmary_dom_lvl1
                hide tsunade_infirmarydom_paizuri
                show tsunade_infirmarydom_paizuri2
                with dissolve
                ts"Is this not e-enough for the likes of you, you little shit?"
                "Tsunade picked up the pace but..."
                show layer master at dizzyflashshort
                bo"E-eh... It's not doing much for me!"
                "You tried pretending that her efforts weren't enough, even though you were at the brink of climaxing..."
                ts"A-are you serious..."
                bo"B-besides, it's j-just your mouth..."
                bo"What's the big deal, I've seen you taking glimpes of my cock you know..."
                bo"Now would be your chan-"
                scene black with vpunch
                hide tsunade_infirmarydom_paizuri2
                bo"O-oh!" with vpunch
                scene tsuna_dom2_anim3 with dissolve
                "Tsunade seemed to take some offense in your comments. She put your cock in her mouth and looked at you as if she had something to prove..."
                "Click twice to continue"
                call clicktwice from _call_clicktwice_12
                scene bg infirmary_dom_lvl1
                show tsunade_infirmarydom_paizuri_bj
                with longerflash
                $ renpy.sound.play("/audio/soun_fx/bjsfx.opus", channel="sfx2", loop=False, relative_volume = 1)
                bot"H-holy fuck, she is actually doing it!"
                bot"Tsunade is s-sucking my cock while stroking it with her tits!"
                ts"*Slurping noises*"
                bo"I k-knew you wanted t-this..."
                $ renpy.sound.play("/audio/soun_fx/bjsfx.opus", channel="sfx2", loop=False, relative_volume = 1)
                "Your comment did not dissuade her. She kept picking up her breasts and letting them drop on your stomach, massaging your shaft in the process."
                "At the same time, she made sure to suck on the head whenever your thrusts brought it closer to her mouth..."
                "The combined sensation of her breasts and her mouth working your cock left you winded after just a few thrusts..."
                ts"T-tell me when..."
                ts"*Slurps*... Y-you are c-close!"
                bo"Ar-ah!" with flash
                bot"She still clings on to h-hope..."
                menu:
                    bot"She still clings on to h-hope..."
                    "{color=[hatredcolor]}Cum in her mouth!{/color}":
                        bot"Little does she k-know..."
                        $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        scene tsuna_dom2_thrust1 with flash
                        bot"I want to fill her t-throat with my cum!"
                        "You violently thrusted forward and came inside of Tsunade's mouth, popping one the buttons of her shirt in the process..."
                        ts"M...mhm!" with vpunch
                        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        show tsuna_dom2_thrust2 with longerflash
                        bot"M-more!"
                        $ renpy.sound.play("/audio/soun_fx/gags/SDTGag11.opus", channel="sfx3", loop=False, relative_volume = 1)
                        show tsuna_dom2_thrust2 with dissolve:
                            zoom 1.2 xalign 0.5 yalign 0.0
                        ts"*Gag*"
                        "Your sudden outburst quickly poured down and around Tsunade's mouth, some of it even shooting out from her nostirls..."
                        $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        show screen parallax1280("tsuna_dom2_cumfinal1", 0.625) with flash
                        $ renpy.sound.play("/audio/soun_fx/gaspforair3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        "Tsunade quickly withdew..."
                        ts"*Gasps* [bo_name_stutter]!?-"
                        $ renpy.sound.play("/audio/soun_fx/cum9.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        show screen parallax1280("tsuna_dom2_cumfinal2", 0.625) with longerflash
                        call decreaselust(100) from _call_decreaselust_96
                        "You drenched Tsunade in semen..."
                        bo"*Panting*"
                        ts"..."
                        "Tsunade stares at you in awe..."
                        bo"What did you expect when you started sucking on my cock..."
                        bo"Your mouth is as good as a container as any, isn't it?"
                        ts"You..."
                        scene black
                        call hidescrollingimage from _call_hidescrollingimage_14
                        scene black with vpunch
                        ts"YOU FREAKING IDIOT!"
                        ts"The semen will lose it's properites when it's mixed with my saliva..."
                        bo"Good thing I produced enough to cover your tits too then. Heh!"
                        ts"H-how am I suppsoed to gather all of this up you idiot!"
                        bo"Don't worry, there'll be much more of it to collect if you keep this up..."
                        scene black with dissolve
                        dev"You'll be able to push Tsunade further in future updates..."
                        bo"Let me help you with it..."
                        $ semendtoadd = 6
                        jump infirmarydom_repeatend
                    "I am c-cumming!":
                        show layer master at dizzyflashshort
                        bo"I am c-cumming!"
                        ts"The c-container!"
                        "Click twice to cum!"
                        call clicktwice from _call_clicktwice_13
                        show screen parallax1280("tsuna_dom2_cumfinal0", 0.625) with flash
                        call showscrollingimage from _call_showscrollingimage_9
                        bo"N-no time for that!"
                        ts"Just... s-shoot it on my chest! B-better than all over the place..."
                        $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        show screen parallax1280("tsuna_dom2_cumnomouth0", 0.625) with flash
                        ts"...My goodness-"
                        bo"I am n-not d-done yet!" with vpunch
                        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        show screen parallax1280("tsuna_dom2_cumnomouth1", 0.625) with longerflash
                        "A second burst shot through the air and covered Tsunade's face..."
                        ts"D-damn it! [bo_name]..."
                        bo"*Panting*..."
                        ts"How difficult is it to inform me in time-" with vpunch
                        bo"I am n-not d-done yet!" with vpunch
                        $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        show screen parallax1280("tsuna_dom2_cumnomouth2", 0.625) with longerflash
                        call decreaselust(100) from _call_decreaselust_97
                        bo"*Heavy breathing* I think... That's the last of it..."
                        ts"Goodness gracious..."
                        bo"See what you can achieve if you put some effort into it?"
                        call changetsunadedominance(-2) from _call_changetsunadedominance_18
                        ts"H-how am I suppsoed to gather all of this up you idiot!"
                        bo"Don't worry, there'll be much more of it to collect if you keep this up..."
                        call hidescrollingimage from _call_hidescrollingimage_15
                        scene black with dissolve
                        bo"Let me help you with it..."
                        dev"You'll be able to push Tsunade further in future updates..."
                        $ semendtoadd = 6
                        jump infirmarydom_repeatend
                    




            else:
                call checkTsunadedominance(-30) from _call_checkTsunadedominance_5
                ts"Are y-you out of your mind?"
                ts"I am not about to use my mouth on a little runt like you..."
                bo"But..."
                ts"Shut it!" with vpunch
                show layer master at dizzyflashshort
                "Tsunade picked up the pace and knocked the wind right out of you!"
        "A-almost there...!":
            pass
        
    bo"Ar-ah! I w-won't last much longer..."
    ts"Just... Let me know when you are close!"
    ts"We have to use the container!"
    hide tsunade_infirmarydom_paizuri
    show tsunade_infirmarydom_paizuri2
    with dissolve
    bo"T-the container?"
    "You paid no regard to her request..."
    "The sensation was overwhelming... You started violently thrusting knowing full that when the time came..."
    "She would serve as your container!"
    bo"F-fuck the container!" with flash
    show layer master at dizzyflashshort
    bo"I am c-cumming!"
    "Click twice to cum!"
    call clicktwice from _call_clicktwice_14
    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    scene infirmary_dom_lvl1_cum with flash
    ts"Y-you...!"
    show layer master at dizzyflashshort
    bo"G-get ready for m-more!"
    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    scene infirmary_dom_lvl1_cum2 with longerflash
    bo"*Groans* Aaa-arh!"
    ts"You b-bastard!" with vpunch
    "Your exerted enough semen to cover Tsunade's face..."
    "As it slid down her face, she tried her best to prevent it from dripping down any further by squeezing her chest, pooling the remainder of the semen in between it..."
    $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.4)
    bo"*Panting* Heh!..."
    ts"I told you to use the container!"
    bo"I am sorry but your tits felt way too good for me to do that..."
    bo"I couldn't react in time... Besides, you are 'containing' your prized cum pretty good by the looks of it!"
    ts"I am trying to not let it drip down you fucking idiot!"
    scene black with vpunch
    jump infirmarydom_repeatend


        


    


        



