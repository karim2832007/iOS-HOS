label hinatawatchnormal:
    $ initialize_replay_defaults()
    scene bg lr_day with dissolve:
        zoom 0.68
    show boruto snob with dissolve
    bot"This will be a fun opportunity to entertain myself..."
    hide boruto with dissolve
    show watch_mast0 with dissolve
    bot"Tsk!" with vpunch
    scene black with dissolve
    "You wait for [hin_name] to start her typical yoga posing at her usual spot..."
    bot"."
    bot".."
    bot"There she goes..."
    show watch2 with dissolve
    bot"Always starting off with her impressive stretches..."
    bot"I wonder how a woman her age can be as flexible... and as sexy as she is!"
    scene watch2_1 with dissolve:
        zoom 1.2 xalign 0.5 yalign 0.0
    hint"[bo_name]... He is staring so intensly..."
    hint"I wonder what he is thinking about..."
    scene watch2_1 with dissolve
    hin"E-everything okay, [bo_name]?"
    scene watch_mast0_1 with dissolve
    bo"I am just... r-relaxing! You keep doing your thing..."
    scene watch2_1 with dissolve:
        zoom 1.2 xalign 0.5 yalign 0.0
    hin"If you say so..."
    scene watch2 with dissolve
    hint"Not much I can do I suppose..."
    show watch3 with dissolve
    hint"I shouldn't take too long this time around..."
    hint"Wouldn't want to complicate things for him given his... condition."
    bot"Fuck, [hin_rel]..."
    bot"Do you have to arch your back like that knowing I am watching?"
    call increaselust(10) from _call_increaselust_172
    scene watch_mast0_1 with dissolve
    menu:
        bot"Do you have to arch your back like that knowing I am watching?"
        "{color=[obediencecolor]}Jerk off to her!{/color}":
            default watchmasturbate = False
            $ watchmasturbate = True
            scene watch3 with dissolve
            bot"If she's gonna be bending like that in front of me then..."
            $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
            scene watch_mast1 with dissolve
            bot"It's not like she doesn't know what's going on with me..."
            scene watch_mast1_1 with dissolve
            bot"This should keep me safe!"
            scene watch3 with dissolve
        "Keep watching...":
            scene watch3 with dissolve
    if watchmasturbate == True:
        $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
    bot"..."
    show watch4 with dissolve
    bot"!" with vpunch
    call increaselust(10) from _call_increaselust_173
    if watchmasturbate == True:
        $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
    bot"I swear... Living with [hin_rel] and being affected by this shit is literal torture..."
    scene watch4 with dissolve:
        zoom 1.3 xalign 0.0 yalign 1.0
    show watch4:
        easein 10 xalign 1.0 yalign 0.0
    bot"What am I even supposed to do besides jerk off to her"
    if watchmasturbate == True:
        $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
    bot"Every time I lay my eyes on her I get this sudden rush of blood running through my body... and my cock!"
    bot"And every time I jerk off... my fantasies of her just spiral further and further..."
    scene watch4 with dissolve
    bot"She has to know what she does to me..."
    scene watch5 with dissolve
    bot"And yet, she keeps being this alluring... this sexy..."
    if watchmasturbate == True:
        $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
    bot"All she does by denying me any pleasure is adding fuel to my desires..."
    show watch1 with dissolve
    bot"One of these days, I swear..." with flash
    if watchmasturbate == True:
        scene watch1_1 with dissolve:
            zoom 1.1 xalign 0.0 yalign 0.2
        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
        hint"*Gasp* W-what is [bo_name] doing! He l-looks..."
        scene watch_mast1_2 with dissolve
        hint"F-flustered! And what's with the p-pillow..." with vpunch 
        bot"I'll make these f-fantasies... a r-reality!"
        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.3)
        scene watch1_2 with flash
        hint"He cannot possibly..."
        call decreaselust(50) from _call_decreaselust_94
        hint"N-no, no! What am I even thinking. He wouldn't..."
        scene watch6 with dissolve:
            zoom 0.69
        hint"But I really shouldn't let this go on for much longer..."
        hint"It feels strange having [bo_name] around knowing his p-problems..."
        scene bg lr_day with dissolve:
            zoom 0.68
        show boruto snob with dissolve
        bo"I am off! Thanks for the show [hin_rel]!"
        call changeObedience("Hinata",1 ,"theshowlivingroom") from _call_changeObedience_115
        hin"T-the... show?"
        hide boruto with dissolve
        bo"You of course! I thoroughly enjoyed watching you..."
        bo"See you around!"
        hin"O-Okay..."
        bo"Oh and I'll be taking this pillow with me!" with vpunch
        hin"...?"
        
    else:
        bot"I'll make these fantasies... a reality!"
        scene watch6 with dissolve
        bot"[hin_rel]... What do I need to do to get through to you..."
        bot"You sit there looking tranquil, while I sit here with a storm of emotions running through me..."
        bot"I can't do this to myself anymore..."
        scene bg lr_day with dissolve:
            zoom 0.68
        show boruto worried with dissolve
        bo"I am off, see you around [hin_rel]..."
        hide boruto with dissolve
        hin"S-see you..."
    $ watchmasturbate = False
    $ renpy.end_replay()
    jump action_taken

    




        


label hinatawatchhate:
    $ initialize_replay_defaults()
    scene bg lr_day with dissolve:
        zoom 0.68
    show boruto angry with dissolve
    bot"If this bitch won't at least provide some... 'relief', then I'll have to do it myself!"
    hide boruto with dissolve
    show watch_mast0 with dissolve
    bot"Tsk!" with vpunch
    scene black with dissolve
    "You wait for [hin_name] to start her typical yoga posing at her usual spot..."
    bot"."
    bot".."
    bot"There she is!"
    show watch2 with dissolve
    bot"Damn you [hin_rel]..."
    bot"All you ever do is parade your sexy body in front of me..."
    scene watch2_1 with dissolve:
        zoom 1.2 xalign 0.5 yalign 0.0
    hint"[bo_name]... He is staring so intensly..."
    hint"I wonder what he is thinking about..."
    scene watch2_1 with dissolve
    hin"E-everything okay, [bo_name]?"
    scene watch_mast0 with dissolve
    bo"Nothing is okay [hin_rel]! Just... keep doing your thing!" with vpunch
    scene watch2_1 with dissolve:
        zoom 1.2 xalign 0.5 yalign 0.0
    hin"O-okay... you don't have to be mad!"
    scene watch2 with dissolve
    hint"He must be moody because of his c-condition..."
    show watch3 with dissolve
    hint"I shouldn't take too long this time around..."
    hint"Wouldn't want to complicate things for him..."
    bot"[hin_rel]... you teasing bitch!" with vpunch
    bot"Do you need to arch your back like that knowing I am here, fantasizing about you?"
    call increaselust(10) from _call_increaselust_174
    scene watch_mast0 with dissolve
    menu:
        bot"Do you need to arch your back like that knowing I am here, fantasizing about you?"
        "{color=[hatredcolor]}Jerk off to her!{/color}":
            $ watchmasturbate = True
            scene watch3 with dissolve
            bot"If you are gonna be posing like a whore then..."
            $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
            scene watch_mast1 with dissolve
            bot"I best make some use of that!"
            scene watch_mast1_1 with dissolve
            bot"This should keep me safe!"
            scene watch3 with dissolve
        
    if watchmasturbate == True:
        $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
    bot"..."
    show watch4 with dissolve
    bot"!" with vpunch
    call increaselust(10) from _call_increaselust_175
    if watchmasturbate == True:
        $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
    bot"Yes [hin_rel]! Spread your legs wide open for me..."
    scene watch4 with dissolve:
        zoom 1.3 xalign 0.0 yalign 1.0
    show watch4:
        easein 10 xalign 1.0 yalign 0.0
    bot"Just looking at your sexy ass body is enough to get me going..."
    if watchmasturbate == True:
        $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
    bot"I could cum a million times to your tits alone..."
    bot"And every time I would... my fantasies of you would spiral further and further..."
    scene watch4 with dissolve
    bot"You have to know what you are doing to me, don't you? You fucking cock-tease..."
    scene watch5 with dissolve
    bot"And yet, you keep strolling around the house looking the way you do, denying me my every advance..."
    if watchmasturbate == True:
        $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
    bot"All that accomplishes is adding more fuel to my desires..."
    show watch1 with dissolve
    bot"One of these days, I swear..." with flash
    if watchmasturbate == True:
        scene watch1_1 with dissolve:
            zoom 1.1 xalign 0.0 yalign 0.2
        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
        hint"*Gasp* W-what is [bo_name] doing! He l-looks..."
        scene watch_mast1_2 with dissolve
        hint"F-flustered! And what's with the p-pillow..." with vpunch 
        bot"I'll make these f-fantasies... a r-reality!"
        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.3)
        scene watch1_2 with flash
        hint"He cannot possibly..."
        call decreaselust(50) from _call_decreaselust_95
        hint"N-no, no! What am I even thinking. He wouldn't..."
        scene watch6 with dissolve:
            zoom 0.69
        hint"But I can't let this go on for much longer..."
        hint"It f-feels strange having [bo_name] around knowing his p-problems..."
        scene bg lr_day with dissolve:
            zoom 0.68
        show boruto snob with dissolve
        bo"I am off! Thanks for the show [hin_rel]!"
        call changeObedience("Hinata",1 ,"theshowlivingroom") from _call_changeObedience_116
        hin"T-the... show?"
        hide boruto with dissolve
        bo"You of course! I thoroughly enjoyed watching you..."
        bo"See you around!"
        hin"O-Okay..."
        bo"Oh and I'll be taking this pillow with me!" with vpunch
        hin"...?"
   
    $ watchmasturbate = False
    $ renpy.end_replay()
    jump action_taken