label infirmary_substart:
    default infirmary_substart_1sttime = 0
    if infirmary_substart_1sttime == 0:
        pass
    else:
        jump infirmary_substart_repeat
    show boruto worried with dissolve:
        xalign 0.0
    $ semendtoadd = 12
    bo"I... I am not sure if I can do it alone anymore..."
    show tsuna annoyed with dissolve
    ts"...Huh? What seems to be the problem..."
    bo"Well, uh... Visual stimuli is quickly becoming inadequate..."
    show tsuna angry2 with dissolve
    ts"...[bo_name]?"
    show boruto worried2 with dissolve
    bo"I-"
    ts"...Are you playing games with me?" with vpunch
    show boruto surprised2 with dissolve
    bo"N-no! I am serious... Why do you think [hin_name] sent me to you!"
    bo"I've been losing control trying to find ways to h-help myself..."
    bo"Jerking off simply isn't doing it for me... Not anymore..."
    show tsuna smug with dissolve
    ts"Is that right..."
    tst"Based on what [hin_name] said, along with my observations, I know that he is being honest..."
    hide tsuna
    show tsuna smug with dissolve:
        xalign 0.7
    tst"I suppose the least I could do if I want to keep extracting important material from him would be..."
    show tsuna:
        easein 0.5 xalign 0.5
    show boruto surprised3 with dissolve
    bo"...T-tsunade?"
    ts"...[bo_name]!"
    show tsuna:
        easeout 0.2 xalign 0.3
    show boruto:
        linear 0.5 xpos -1000
    pause 0.3
    show tsuna at smallshake
    pause 0.3
    scene black with vpunch
    label replay_infirmary_substart1:
    $ initialize_replay_defaults()
    "Tsunade pushes you to the ground!"
    show start1:
        zoom 0.71 xalign 0.1
    with dissolve
    "She took off her heels and stood over you menacingly..."
    ts"If I am to... 'help' you, then you will do exactly as I say, and obey my every instruction..."
    bot"W-what the hell...?"
    show start2_1 with dissolve:
        zoom 0.71 xalign 0.9
    ts"Do I make myself clear!" with vpunch
    bot"I m-mean... I am not going to say no to that!"
    bo"Uuuuh, whatever you say..."
    ts"I said... Do, I, make, myself..."
    show start2:
        zoom 0.71 xalign 0.1
    ts"CLEAR?" with vpunch
    call increaselust(10) from _call_increaselust_78
    bo"Y-yes Ma'am!"
    bot"I don't know what's going on, but if this crazy bitch wants to put on an act..."
    bot"I will enjoy it!"
    scene start3 with dissolve
    call increaselust(20) from _call_increaselust_79
    ts"Before we begin, it's important to understand that I am only doing this to extract an important resource for my expirimentations..."
    ts"At the same time, we are managing your condition to avoid any future flare-ups."
    ts"Make no mistake, this is a medical procedure! Under which, you'll follow my directions, understood?"
    menu:
        ts"Make no mistake, this is a medical procedure! Under which, you'll follow my directions, understood?"
        "Yes ma'am!":
            bo"Yes Ma'am!"
        "Get on with it already!":
            bo"Get on with it already, you damned ha-"
            scene black with vpunch
            bo"Ow!"
            ts"KEEP IT SHUT!" with vpunch
            call changetsunadedominance(3) from _call_changetsunadedominance_19
            "Tsunade stomps your pelvic area with her bare foot..."
            bot"W-what the hell..."
            ts"You follow my rules, or I am calling this off!"
    scene black with dissolve
    ts"Now take off your clothes and lay on the bed..."
    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    bo"S-sure..."
    ts"The rules are simple..."
    ts"You cannot touch me..."
    show repeat1 with dissolve:
        xalign 0.05 zoom 0.44
    ts"But I can touch you!" with vpunch
    bo"S-sure thing..."
    bot"D-damn... She is stepping on my cock!"
    $ renpy.sound.play("/audio/soun_fx/jerkoffclothes.opus", channel="sfx2", loop=False, relative_volume = 0.3)
    bot"H-her nylon pantyhose rubbing against the shaft... It f-feels s-so fucking good!"
    ts"From now on..."
    show repeat2 with dissolve:
        xalign 0.5 zoom 0.44
    ts"You will also not speak until we are done!" with vpunch
    bo"*Groans in mild pain* Uh-ah!"
    "Tsunade pressed down harder on your shaft. The force she applied caused your legs to recoil up in the air behind her..."
    ts"Unless I let you of course..."
    bot"F-fuck! W-why does this... f-feel so nice..."
    ts"But for now, sit there like a good little runt..."
    show repeat3 with dissolve:
        xalign 0.95 zoom 0.44
    $ renpy.sound.play("/audio/soun_fx/jerkoffclothes.opus", channel="sfx3", loop=False, relative_volume = 0.3)
    ts"And produce for me!"
    bo"*Moans* Ah-mmh..." with flash
    bo"I..."
    ts"Good boy! Let it all out for me!" with flash
    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    show repeat3_1 with longerflash:
        xalign 0.95 zoom 0.44
    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    call decreaselust(100) from _call_decreaselust_98
    bo"Hnn-hng!"
    "Tsunade carefully kept moving her foot up and down your shaft trying to squeeze every last drop out of you..."
    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    bo"Ah-ah... T-tsunade..." with flash
    ts"Shhh, little runt!"
    "She knew what she was doing, evident by her still spotless pantyhose that kept rubbing your shaft, but skilfully avoided the glans..."
    "Up, and down..."
    scene black with dissolve
    "...Down and up"
    "She finally stopped when she made sure she extracted even the final drop of your semen..."
    show repeat4 with dissolve
    ts"Excellent produce, [bo_name]. This will certainly prove useful..."
    "Tsunade  sat down alongside you and rested her foot on your thigh."
    $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.4)
    bo"*Panting*..."
    "You lay on your back motionless with your hands resting up and behind your head as you drew several much-needed breaths..."
    "The semen was conveniently pooled around your navel, as Tsunade made sure of that with her careful and skillful manipulation of your cock..."
    ts"Lost your breath... Have you? Go on, you can speak now!"
    menu tsunade_submenu_lvl1:
        ts"Lost your breath... Have you? Go on, you can speak now!"
        "T-thanks for that...":
            bo"T-thanks for that. I f-feel, much better..."
            ts"Good! I trust you'll recover well... and fast!"
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/heels1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
            ts"I am going to be needing much more than this measely amount of yours..."
            "Tsunade stood up, put on her heels and fetched a container..."
            "She kneeled on the mattress alongside you and carefully scooped as much of the semen as she could by dragging her delicate fingers across your stomach... "
            call changetsunadedominance(5) from _call_changetsunadedominance_20
            ts"What are you still laying there for! Get up and put on some clothes!" with vpunch
            "You obey her instructions..."
            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            bo"R-right!"
        "{color=[dominancecolor]}I didn't know you had it in you...{/color}":
            bo"T-tsunade... *Heavy breathing*..."
            ts"Winded now, are you?"
            bo"No... I was just thinking..."
            bo"I didn't know you had it in you!"
            show repeat4_1 with dissolve
            call changeDominance(1,"tsunade_submenu_lvl1") from _call_changeDominance_52
            bo"That was an excellent display of your qualities, qualities I always knew you had in you! You sly fox..." with vpunch
            show repeat4_1 with dissolve:
                zoom 1.2 xalign 0.6 yalign 0.0
            ts"You little..."
            ts"My mistake for helping in the first place!" with vpunch
            scene black with vpunch
            $ renpy.sound.play("/audio/soun_fx/heels1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
            "Tsunade, annoyed by your remarks, quickly stood up, put on her heels, and fetched a container..."
            ts"Here! Use this and gather all of the fluid from your stomach yourself!"
            call changetsunadedominance(3) from _call_changetsunadedominance_21
            ts"Dare to miss a drop, and you are never stepping a foot in my office ever again!"
            bo"U-uh... S-sure!"
            bot"Shit... I shouldn't have said a thing..."
            bot"Scooping my own cum... Yuck!"
            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            "You finish collecting your semen and put on some clothes..."


        
    scene bg infirmary room day with dissolve
    show boruto surprised3 at left with dissolve
    show tsuna smug behind boruto:
        xalign 0.3
    show tsuna:
        easein 1 xalign 0.8
    call addSemen(semendtoadd) from _call_addSemen_3
    ts"Excellent... This sample will certainly be of use!"
    bo"N-now what..."
    ts"Now you turn around and walk out the door..."
    ts"Your urges have settled, have they not?"
    bo"Y-yes but..."
    show boruto surprised2 with dissolve
    ts"No buts!" with vpunch
    ts"I'll see you again when and if your condition happens to flare up..."
    ts"And remember, we have an important task to fulfil! This was nothing more than a medical procedure to assist my hypothesis..."
    bo"R-right..."
    bo"See you... next time? I suppose..."
    hide boruto with dissolve
    show tsuna angry2 with dissolve
    ts"*Scoffs*"
    ts"Damned brat... Of all the people, did it have to be him?"
    hide tsuna with dissolve
    ts"No matter, I got what I needed!"
    $ renpy.end_replay()
    $ infirmary_substart_1sttime = 1
    jump action_taken
            
        



    
    





label infirmary_substart_repeat:
    bo"You know that I struggle to do it alone..."
    show tsuna annoyed with dissolve
    ts"[bo_name]... You aren't lying to me, are you?"
    bo"N-no, it's like I said last time. Visual stimuli is just not cutting it...."
    show tsuna smug with dissolve
    ts"Is that right..."
    tst"Might as well make sure I get what I want..."
    hide tsuna
    show tsuna smug with dissolve:
        xalign 0.7
    tst"[bo_name]..."
    show tsuna:
        easein 0.5 xalign 0.5
    show boruto surprised3 with dissolve
    bo"Uuuh...T-tsunade?"
    ts"..."
    show tsuna:
        easeout 0.2 xalign 0.3
    show boruto:
        linear 0.5 xpos -1000
    pause 0.3
    show tsuna at smallshake
    pause 0.3
    scene black with vpunch
    ts"Get on the floor!"
    show start1:
        zoom 0.71 xalign 0.1
    with dissolve
    "Tsunade  took off her heels and stood over you menacingly, but..."
    "You knew what was coming..."
    ts"If I am to... 'help' you again, then you will do exactly as I say, and obey my every instruction..."
    bo"S-sure..."
    show start2_1 with dissolve:
        zoom 0.71 xalign 0.9
    ts"Do I make myself clear!" with vpunch
    bo"M-maybe go easy on me this time?"
    ts"I said... Do, I, make, myself..."
    show start2:
        zoom 0.71 xalign 0.1
    ts"CLEAR?" with vpunch
    call increaselust(10) from _call_increaselust_80
    bo"Y-yes Ma'am!"
    bot"I... I can get used to this."
    scene start3 with dissolve
    call increaselust(20) from _call_increaselust_81
    ts"I don't need to state the obvious..."
    ts"You'll do as I say, yes?"
    menu:
        ts"You'll do as I say, yes?"
        "Yes ma'am!":
            bo"Yes Ma'am!"
        "Get on with it already!":
            bo"Come on! Get to it alre-"
            scene black with vpunch
            bo"Ow!"
            ts"KEEP IT SHUT!" with vpunch
            call changetsunadedominance(3) from _call_changetsunadedominance_22
            "Tsunade stomps your pelvic area with her bare foot..."
            bot"W-what the hell..."
            ts"You follow my rules, or I am calling this off!"
    scene black with dissolve
    ts"Now take off your clothes and lay on the bed..."
    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    bo"S-sure..."
    ts"The rules are simple..."
    ts"You cannot touch me..."
    show repeat1 with dissolve:
        xalign 0.05 zoom 0.44
    ts"But I can touch you!" with vpunch
    bot"F-fuck! Here she goes again..."
    tst"Hmm, shall I have some fun with this runt today?"
    call checkTsunadedominance(25, None) from _call_checkTsunadedominance_6
    if tsunadedominance >= 25:
        tst"Why shouldn't I, this could even lead to increased quantities of his sperm..."
        $ renpy.sound.play("/audio/soun_fx/jerkoffclothes.opus", channel="sfx2", loop=False, relative_volume = 0.3)
        bot"D-damn... She is doing that thing with her foot again!"
        bot"H-her nylon pantyhose rubbing against the shaft... It f-feels fucking amazing!"
        ts"Don't go climaxing on me just yet..."
        label replay_infirmary_substart2:
        $ initialize_replay_defaults()
        show repeat2 with dissolve:
            xalign 0.5 zoom 0.44
        bot"I am just about to cum and she hasn't e-even started yet. I t-think she's putting on more p-pressure than before!"
        ts"I am going to need your arousal levels to hit new heights!"
        hide repeat2 with dissolve
        bot"N-no! Why did she stop..."
        hide repeat1 with dissolve
        bot"I was so close to cumming!"
        ts"Get on the bed for me, will you?"
        bot"O-oh...? What d-does she have in mind?"
        show screen parallax1280("ifyou2") with dissolve
        call showscrollingimage from _call_showscrollingimage_10
        "Tsunade placed her leg on your upper thigh and wrapped the inner part of her foot around your shaft..."
        ts"Are you doing okay, little runt? Do you want me to continue...?"
        bot"Y-yes please!"
        ts"Nod if you do..."
        "Click twice to Nod at Tsunade..."
        call clicktwice from _call_clicktwice_15
        hide screen parallax1280
        hide scrollingimage onlayer screens
        scene bg infirmary_dom_lvl1
        show tsunade_infirmarysub_fj
        with dissolve
        $ renpy.sound.play("/audio/soun_fx/jerkoffclothes.opus", channel="sfx2", loop=False, relative_volume = 0.3)
        "Tsunade started working her foot around your shaft..."
        bot"F-fuck! How is she so fucking good at this..."
        bot"The way she t-twirls her foot, the feeling of her pantyhose rubbing against my cock..."
        bot"I c-can't..." with flash
        show tsunade_infirmarysub_fj:
            easein 1 yalign 0.2
        ts"It would seem by your expression you are running into some trouble..."
        hide tsunade_infirmarysub_fj
        show tsunade_infirmarysub_fj_slow:
            yalign 0.2
        with dissolve
        ts"But I can't have you climaxing just yet!"
        show tsunade_infirmarysub_fj_slow:
            easein 1 yalign 1.0
        "Tsunade slowed the pace considerably, leaving you right on the edge of climaxing..."
        "She knew exactly how far too push, and how far to pull..."
        bot"F-fuuck! This is so f-frustrating, just let me c-cum already!"
        ts"Getting frustrated... are you?"
        bo"P-please..."
        ts"Oh!" with vpunch
        ts"Begging even..."
        ts"You are so much cuter when you are like this [bo_name]..."
        ts"Maybe I will consider teaching you some stuff if you keep being a good boy for me..."
        scene black with dissolve
        ts"Come on, lean back on the bed! Make some room for me..."
        "Tsunade climbed on top of the bed and sat at the opposite direction of you..."
        show sub_final2 with dissolve
        "She put her legs on top of yours and reached for your cock with both of her feet..."
        bo"T-tsunade, I am..."
        show sub_final1 with dissolve
        ts"Uh-uh!" with vpunch
        ts"No talking, remember?"
        "She assertively squeezed your shaft in between both of her feet, as if she demanded for you to shut up... "
        bot"F-fucking heavens above... I w-was going to tell her I am about to b-bust on her!"
        show tsunade_infirmarysub_fj2 with dissolve
        bot"But if s-she wants me to cover her feet in my c-cum..."
        bot"T-then I will do just t-that"
        bo"*Groans*! Ar-hnng!"with flash
        ts"Do not fret, my little runt..."
        ts"This time..." with flash
        ts"I shall allow you to climax."
        ts"But of course..."
        bot"H-here it c-comes...!"
        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        show repeat4 with longerflash
        call decreaselust(100) from _call_decreaselust_99
        "At the very last moment, Tsunade pushed your cock away and straight to your stomach..."
        ts"I am not allowing you to make a mess of me!"
        $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx3", loop=False, relative_volume = 0.4)
        bo"*Panting*..."
        ts"An even larger amount of sperm than before..."
        ts"Impressive, [bo_name]. This will certainly prove useful!"
        "You lay on your back motionless with your hands resting up and behind your head as you drew several much-needed breaths..."
        "The semen was conveniently pooled around your navel, as Tsunade made sure of that with her careful and skillful manipulation of your cock..."
        ts"Lost your breath... Have you? Go on, you can speak now!"
        dev"You'll be able to let Tsunade continue to do with you as she pleases in future updates!"
        $ semendtoadd = 15
        jump tsunade_submenu_lvl1
        






        
    else:
        tst"Maybe that's a bad idea. He could get the wrong idea..."
        $ renpy.sound.play("/audio/soun_fx/jerkoffclothes.opus", channel="sfx2", loop=False, relative_volume = 0.3)
        bot"D-damn... She is stepping on my cock!"
        bot"H-her nylon pantyhose rubbing against the shaft... It f-feels s-so fucking good!"
        ts"From now on..."
        show repeat2 with dissolve:
            xalign 0.5 zoom 0.44
        ts"You will also not speak until we are done!" with vpunch
        bo"*Groans in mild pain* Uh-ah!"
        "Tsunade pressed down harder on your shaft. The force she applied caused your legs to recoil up in the air behind her..."
        ts"Unless I let you of course..."
        bot"F-fuck! W-why does this... f-feel so nice..."
        ts"But for now, sit there like a good little runt..."
        show repeat3 with dissolve:
            xalign 0.95 zoom 0.44
        $ renpy.sound.play("/audio/soun_fx/jerkoffclothes.opus", channel="sfx3", loop=False, relative_volume = 0.3)
        ts"And produce for me!"
        bo"*Moans* Ah-mmh..." with flash
        bo"I..."
        ts"Good boy! Let it all out for me!" with flash
        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        show repeat3_1 with longerflash:
            xalign 0.95 zoom 0.44
        call decreaselust(100) from _call_decreaselust_100
        $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
        bo"Hnn-hng!"
        "Tsunade carefully kept moving her foot up and down your shaft trying to squeeze every last drop out of you..."
        $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        bo"Ah-ah... T-tsunade..." with flash
        ts"Shhh, little runt!"
        "She knew what she was doing, evident by her still spotless pantyhose that kept rubbing your shaft, but skilfully avoided the glans..."
        "Up, and down..."
        scene black with dissolve
        "...Down and up"
        "She finally stopped when she made sure she extracted even the final drop of your semen..."
        show repeat4 with dissolve
        ts"Excellent produce, [bo_name]. This will certainly prove useful..."
        "Tsunade sat down alongside you and rested her foot on your thigh."
        $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.4)
        bo"*Panting*..."
        "You lay on your back motionless with your hands resting up and behind your head as you drew several much-needed breaths..."
        "The semen was conveniently pooled around your navel, as Tsunade made sure of that with her careful and skillful manipulation of your cock..."
        ts"Lost your breath... Have you? Go on, you can speak now!"
        $ semendtoadd = 12
        jump tsunade_submenu_lvl1

