label sakura_wine_date:
    $ initialize_replay_defaults()
    call hideUI from _call_hideUI_64
    if wine_counter >=1:
        jump sakura_wine_date2
    $ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    "*Knock Knock*"
    bot"."
    bot".."
    $ playmusic("audio/ost/zsakura.opus", volume=0.5)
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    bot"...Got my hopes up for nothin-" with vpunch
    show sakurwine intro1_1 with dissolve:
        yalign 1.0
    show sakurwine intro1_1 with dissolve:
        easein 4 yalign 0.0
    saku"[bo_name]! You came..."
    show sakurwine intro1_1 with dissolve:
        easein 0.2 yalign 1.0
    saku"Brought the good stuff too I see... Hihihi!" with vpunch
    show sakurwine intro1_1 with dissolve:
        easein 2 yalign 0.0
    saku"Come on, come inside! Don't be shy..."
    scene black with dissolve
    bo"Of course..."
    show sakurwine intro1_2 with dissolve:
        yalign 1.0
    show sakurwine intro1_2:
        easein 2 yalign 0.0
    pause 1
    show screen parallax1280("sakurwine intro1_2",initial_ypos=1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_178
    saku"It's just me and you at this time, but I hope you don't mind! Hehe! *Teasing Giggle*"
    bo"I don't mind at all, Auntie."
    bot"In fact, that may be preferable if this ass in front of me is any indication of what's coming!"
    "You followed Sakura as she led you towards the living room..."
    show screen parallax1280("blackscreen") with dissolve
    if not _in_replay:
        call useItem(wine,1) from _call_useItem_10
    "She fetched two wine glasses and placed them on a table..."
    saku"..." with vpunch
    "Sakura turned around in an uncharacteristically uncertain manner and run into your arms!"
    hide screen parallax1280
    show screen parallax1280("sakurwine intro2", initial_ypos=0.0)
    with dissolve
    bo"A-auntie!?"
    saku"S-sorry! It's just that..."
    saku"Most nights I sit here in the dark, alone... drinking my sorrows away, Trying my best to deal with... you know, life."
    saku"It's nice to have some company for once!"
    saku"Thank you for visiting so often [bo_name]. This lonely housewife appreciates it, very much so..."
    menu sakura_randommenu23489023985:
        saku"Thank you for visiting so often [bo_name]! This lonely housewife appreciates it, very much so..."
        "Of course, Auntie":
            bo"Of course, Auntie!"
            bo"I appreciate your friendship too!"
            call changesakura(2) from _call_changesakura_38
            saku"Awww... so sweet!"
        "{color=[dominancecolor]}I appreciate you too, Sakura!{/color}":
            call checkDominance(15,"sakura_randommenu23489023985") from _call_checkDominance_47
            bo"It's my pleasure, Auntie..."
            hide screen parallax1280
            show screen parallax1280("sakurwine intro2_1", initial_ypos=1.0)
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
            bo"I appreciate you as well, you know!" with vpunch
            call changeDominance(1) from _call_changeDominance_119
            "You pinch and raise her ass towards you with one hand!"
            call changesakura(3) from _call_changesakura_39
            saku"O-oh...? That's one way to 'appreciate' me! *Giggles*"
    show screen parallax1280("blackscreen") with vpunch
    saku"Right, enough dramatics! It's time to drink and celebrate!"
    "In an instant, Sakura seemed to bounce back to her typical light-hearted mood!"
    scene black with dissolve
    call hidescrollingimage("Click twice to start drinking!") from _call_hidescrollingimage_109
    "Sakura poured the two of you a glass of wine. You sat across each other in the living room..."
    show borutodrinking 1 with dissolve:
        fit "contain" xalign 0.0 xzoom -1
    bo"What exactly are we celebrating, Auntie?"
    show borutodrinking 1:
        easein 1 xalign -0.55
    show sakurwine drinkingtalk1 with dissolve:
        fit "contain" xalign 1.0
    saku"Our ever-enduring friendship of course!"
    saku"You like spending time with me, don't you?"
    show borutodrinking 2
    show sakurwine drinking1:
        xalign 1.0 fit "contain"
    with dissolve
    bo"I do..."
    "Sakura drinks some of the wine..."
    show sakurwine drinkingtalk1 with dissolve
    saku"Me too! See? Let's celebrate! *Giggles*" with vpunch
    saku"Oh! Oopsie daisy! Silly me..."
    saku"We still have to try and stay reserved, okay? Sarada's sleeping right around the hallway after all..."
    saku"She'd hate to be excluded from our little meeting!"
    saku"You understand why I try to keep some things between us, don't you?"
    menu:
        saku"You understand why I try to keep some things between us, don't you?"
        "Because you want me for yourself!":
            show borutodrinking 1 with dissolve
            bo"Because you want me all to yourself?"
            call changesakura(-2) from _call_changesakura_40
            saku"W-what! No, of course not! Don't even joke about that [bo_name]..." with vpunch
            saku"It's to protect Sarada of course..."
        "To protect Sarada...":
            show borutodrinking 1 with dissolve
            bo"To protect Sarada, right?"
            call changesakura(2) from _call_changesakura_41
            saku"Exactly..." with vpunch
    show sakurwine drinking1 with dissolve
    saku"Everything I do, I do for my daughter..."
    show sakurwine drinkingtalk1 with dissolve
    saku"Given Sarada's feelings, it's best we keep our friendship between us. At least until you two get back to your old habits..."
    saku"Until then, there's nothing wrong if her mother here spends some quality time with her ex boyfriend, Right? *Teasing Giggle*"
    show borutodrinking 1 with dissolve
    bo"You know we weren't like that, Auntie..."
    scene black
    show sakurwine drinkingtalk1:
        fit "contain" xalign 0.5
    with dissolve
    saku"Sure, Of course you weren't! You know I like to tease you two!" with vpunch
    show sakurwine drinking1 with dissolve
    "Sakura takes another sip of her wine..."
    show sakurwine drinkingtalk1 with dissolve
    saku"More importantly, I wouldn't want Sarada to turn into a drunkard!"
    saku"*Hic!* She doesn't have her mother's tolerance to this  s-stuff after all!" with vpunch
    show borutodrinking 1 with dissolve:
        fit "contain" xalign 0.5
    bot"Tolerance? What tolerance! Auntie looks drowsy already..." with vpunch
    scene black
    show sakurwine intro1_2:
        fit "contain" xalign 0.5
    with dissolve
    saku"*Hic!* Enough about that!"
    "Sakura got up, refilled her glass, and turned her back at you..."
    show  borutodrinking 2 with dissolve:
        yalign 0.2
    saku"We didn't come here to sulk did we...?"
    bot"What's she thinking..."
    saku"In fact, there's another reason I wanted you to come by at this hour... *Hic!*"
    scene borutodrinking 2_1 with dissolve:
        yalign 0.2
    bo"A-auntie!?" with vpunch
    "Sakura reached for the button on her pants..."
    show screen parallax1280("undressing1",initial_ypos=1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_179
    saku"A... final lesson, if you will!" with vpunch
    scene black
    call hidescrollingimage from _call_hidescrollingimage_110
    show borutodrinking 2_2 with dissolve:
        yalign 0.2
    bot"What the fuck is going on! Is she about to c-cheat on her husband with me?" with vpunch
    show borutodrinking 2_2 with dissolve:
        easein 0.8 zoom 1.1 yalign 1.0
    call increaselust(50) from _call_increaselust_255
    show borutodrinking:
        easein 0.5 yalign 0.1
    pause 0.44
    show borutodrinking 2_1 with dissolve:
        yalign 0.1
    saku"I see you s-staring intensly *Hic!* [bo_name]! Is something wrong?"
    bo"I j-just-"
    show undressing2 with dissolve:
        yalign 1.0
    show undressing2:
        easein 4 yalign 0.0
    saku"Didn't expect this...?"
    show screen parallax1280("undressing2",initial_ypos=1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_180
    saku"Well? Take a proper look... What do you think of your Auntie's body, [bo_name]?"
    saku"Is it as  amusing to you as a *Hic!*... younger lady's?"
    call increaselust(50) from _call_increaselust_256
    bo"...B-better!" with vpunch
    saku"Oooooh? In that case..."
    scene black
    call hidescrollingimage from _call_hidescrollingimage_111
    saku"Would you like to..."
    label replay_orgasmtogether:
    "Sakura takes a sit at her couch, right across of you..."
    show screen parallax1280("mutual2",initial_ypos=0.5) with dissolve
    call showscrollingimage from _call_showscrollingimage_181
    saku"...Would you like to see more of me?"
    bo"Y-yes please!"
    saku"Okay, but only if you show me something of yours first... *Hic!*"
    show screen parallax1280("blackscreen",initial_ypos=0.5) with dissolve
    saku"I've been watching your reaction down there, you know..."
    bo"S-since you asked for it..."
    hide screen parallax1280
    show screen parallax1280("mutal_boruto 1",initial_ypos=0.5)
    with dissolve
    saku"A woman is always observant... [bo_name] *Hic!* Even when you think she is not."
    saku"I've been observing how you act around me..."
    saku"I can tell you have the hots for your Auntie... Don't you?"
    show screen parallax1280("blackscreen",initial_ypos=0.5) with dissolve
    saku"That's very inappropriate, you know..."
    show screen parallax1280("mutual2",initial_ypos=0.5) with dissolve
    saku"But a deal is a deal. I said I'll show you more, didn't I?"
    hide screen parallax1280
    show screen parallax1280("sakura_mast_anim1",initial_ypos=1.0)
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/femalemast2.opus", channel="sfx2", loop=True, relative_volume = 1.8)
    saku"Tell me [bo_name]. Have you ever seen a woman's pussy before?"
    saku"Have you ever seen a woman pleasing herself like t-this...? *Hic!*" with vpunch
    bo"N-not... r-really..."
    saku"I could tell, you know..."
    saku"You see... Me and you, we have something in common..."
    scene black
    call hidescrollingimage("Click twice to 'help' yourself...") from _call_hidescrollingimage_112
    show sakura_mast_anim1:
        fit "contain" xalign -0.1
    show boruto_sakura_mast_anim1 behind sakura_mast_anim1:
        fit "contain" xalign 1.5 alpha 0.5
    with dissolve
    saku"With all I know of your condition by now, it must be so horrific, to always be in a constant state of arousal..."
    saku"With no one to help, no prior experience..."
    saku"What does a boy your age even do to satisfy those... desires."
    saku"I feel your pain [bo_name]. I really do..."
    saku"My s-sex drive... *Hic!* Has always been high, but my h-husband... he is..."
    saku"N-not like me, not like US, you know...?"
    saku"I am not the t-type of woman to engage in infidelity, but..."
    saku"If there's no penetration involved, p-perhaps we can help each other out with our... d-drives... Don't you think?"
    bo"A-auntie... *Moans* But... how do we... with no pen-"
    scene black with vpunch
    saku"Don't be so loud... [bo_name]!"
    saku"What if...Ah-ah♡... S-sarada wakes up. We h-have to be careful!"
    show mutual3 with dissolve:
        fit "contain" xalign 0.0
    bo"...S-sorry!"
    scene black
    show sakura_mast_anim2:
        fit "contain" xalign 0.0
    with dissolve
    saku"You see... if there's no p-penetration involved..."
    saku"Then it isn't... c-cheating, right?"
    saku"Besides... there's many ways you can please a woman without..."
    show sakura_mast_anim2:
        easein 1 xalign -0.5
    show boruto_sakura_mast_anim1 behind sakura_mast_anim2:
        fit "contain" xalign 1.8 alpha 0.8 
    saku"... your p-penis. Although yours is quite... intriguing, I must admit."
    bot"S-she likes my cock...? Auntie Sakura..."
    show boruto_sakura_mast_anim2 behind sakura_mast_anim2:
        fit "contain" xalign 1.8 alpha 0.8
    bo"Y-you mean... *Moans* M-my size?"
    "Upon hearing Sakura's comments, you couldn't help but furiously jerk it to her. Or rather, for her..."
    saku"Oh m-my... [bo_name]..."
    saku"Like an animal, in front of your A-auntie... *Hic!*" with vpunch
    $ renpy.sound.play("/audio/soun_fx/femalemast3.opus", channel="sfx2", loop=True, relative_volume = 1.8)
    show screen parallax1280("sakura_mast_anim2_1",initial_ypos=1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_182
    saku"In that case, I shall join you in our animalistic desires!" with vpunch
    "You both kept masturbating across each other. Looking at one another helped enhance the pleasure you felt..." with flash
    saku"Y-you know... *Hic!* The same applies to women too. I m-mean..."
    saku"With p-pleasing one another... *Moans*..."
    saku"Penetration is one thing... *Moans* P-pleasure is another!" with flash
    saku"W-what I am t-trying to say is..."
    bot"F-fuck I am about to cum!" with flash
    saku"We can do a lot for e-each other... Me and y-you..."
    saku"Just as long as... we don't h-have...actual... sex! *Moans*"
    bo"I am c-cumming, A-auntie!" with flash
    scene black
    call hidescrollingimage from _call_hidescrollingimage_113
    saku"Then let's have... *Hic!* an orgasm together!"
    show mutual4 with dissolve:
        yalign 0.0
    show mutual4:
        easein 2 yalign 1.0
    saku"Keep stroking that cock for your Auntie..."
    $ renpy.sound.play("/audio/soun_fx/femalemast3.opus", channel="sfx2", loop=True, relative_volume = 1.8)
    show screen parallax1280("sakura_mast_anim3",initial_ypos=1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_183
    saku"Ah-♡ah-Aah!♡ I am close too!" with flash
    saku"Ahwww... ♡ah-Aah! S-see how this feels... *Moans* so much better?" with flash
    $ renpy.sound.play("/audio/soun_fx/femalemastmoan2.opus", channel="sfx3", loop=False, relative_volume = 1.8)
    show screen parallax1280("sakura_mast_anim3_1",initial_ypos=1.0) with dissolve
    saku"Because... ♡ah-Aah! We h-have... ♡ah-Aah!... each other!" with flash
    scene black with dissolve
    call hidescrollingimage("Click twice to orgasm together!") from _call_hidescrollingimage_114
    saku"I am *Moans loudly*... c-convulsing! Ah-♡ah-Aaaawaahh!♡" with flash
    $ renpy.sound.play("/audio/soun_fx/cum0.opus", channel="sfx3", loop=False, relative_volume = 0.4)
    $ renpy.sound.play("/audio/soun_fx/femalecum2.opus", channel="sfx2", loop=False, relative_volume = 1.4)
    show screen parallax1280("mutual5_1",initial_ypos=0.9) with dissolve
    call showscrollingimage from _call_showscrollingimage_184
    saku"*Orgasmic Moans* Aaah!? ♡ Mmhmhm!!♡ Aawa♡aaa♡awwwah!♡" with flash
    bo"I am c-cumming too!" with flash
    "Sakura's muscles started convulsing. She lost control of her legs, dropping down on her tippy toes as the orgasmic feeling she was experiencing rippled throughout her body..."
    "She grabbed a nearby glass hoping to prevent an orgasmic mess!"
    $ sakura_helpherout = False
    menu randomsakura_menu12931924:
        "She grabbed a nearby glass hoping to prevent an orgasmic mess!"
        "Finish together.":
            hide screen parallax1280
            show screen parallax1280("mutual5_2",initial_ypos=1.0)
            saku"N-n-Aauwaaahh!♡ Mmhmhm!!♡" with flash
            hide screen parallax1280
            show screen parallax1280("mutual5_3",initial_ypos=1.0)
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
            bo"Arghh! *Moans loudly*!" with longerflash
            "Your load was strong enough to fly across the room, and land besides Sakura's feet..."
            scene black
            call hidescrollingimage from _call_hidescrollingimage_115
            jump sarada_wakes_up
        "{color=[dominancecolor]}Help her out!{/color}":
            call checkDominance(15, "randomsakura_menu12931924") from _call_checkDominance_48
            bo"A-auntie... I..."
            bot"I can't just sit here and jerk it! She's too f-fucking hot for that!"
            show screen parallax1280("blackscreen",initial_ypos=1.0)
            bo"L-let me help you... A-auntie!" with vpunch
            saku"*Gasps* [bo_name_stutter]!?"
            hide screen parallax1280
            show screen parallax1280("mutual6",initial_ypos=0.8)
            $ renpy.sound.play("/audio/soun_fx/cum0.opus", channel="sfx3", loop=False, relative_volume = 0.4)
            $ renpy.sound.play("/audio/soun_fx/femaleclimax.opus", channel="sfx2", loop=False, relative_volume = 0.8)
            saku"B-b-but I am... N-n-Aauwaaahh!♡ Mmhmhm!!♡" with flash
            hide screen parallax1280
            show screen parallax1280("mutual6_1",initial_ypos=1.0)
            $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx1", loop=False, relative_volume = 0.4)
            saku"C-coming! N-n-Aauwaaahh!♡ Mmhmhm!!♡" with longerflash
            "You rushed over to her just as she was about to orgasm..."
            "She reached for the glass to catch her gushing cum, but you knocked it away and buried your face in her dripping pussy, your tongue plunging deep into her!"
            "Sakura frantically rubbed her swollen clit, her body shaking as she squirted hard, spraying her hot juices across the room, splattering your face and chest." with flash
            "Her thick, discharged fluids poured into your mouth, drenching your chin and neck..." with flash
            scene black
            default sakura_helpherout = False
            $ sakura_helpherout = True
            call hidescrollingimage from _call_hidescrollingimage_116
            jump sarada_wakes_up


            jump sarada_wakes_up
        
label sarada_wakes_up:
    "Meanwhile..."
    show saradawake 1 with dissolve:
        yalign 1.0
    "????" "Is that..."
    show saradawake:
        easein 6 yalign 0.0
    "????" "*Drowsy* W-what's up with all... the n-noises..."
    sara"Mom...? *Yawns* Better go check on her..."
    scene black with dissolve
    if sakura_helpherout == True:
        $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        show mutual5_3 with dissolve:
            yalign 0.0
        "*Both Panting*..."
        saku"O-o-o-h my lords, [bo_name_stutter]! ♡ Mmhmhm!!♡" with flash
        saku"I am still... h-having an orgasm!"
        call decreaselust(100) from _call_decreaselust_129
        bo"Did you... e-enjoy that, a-auntie?"
        saku"♡ Mmhmhm!!♡ *Convulsing...*" with flash

    
    else:
        $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        show mutual7_1 with dissolve:
            yalign 1.0
        show mutual7_1:
            easein 6 yalign 0.1
        "*Both Panting*..."
        call decreaselust(100) from _call_decreaselust_130
        bo"A-auntie... that was-"
    scene black
    sara"...Mom?" with vpunch
    saku"*Gasps* O-out... *Hic!* N-NOW!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx3", loop=False, relative_volume = 2.0)
    "Sakura signals for you to get out as fast as possible! You frantically run around picking up only what you could, including your clothing, and storming out..."
    show saradawake 1_2 with dissolve:
        yalign 1.0
    show saradawake 1_2:
        easein 6 yalign 0.1
    sara"Is t-that you mom? *Yawns* Is everything alright?"
    saku"I am alright S-sarada, you can go back to sleep..."
    show screen parallax1280("mutual7",initial_ypos=0.5) with dissolve
    call showscrollingimage from _call_showscrollingimage_185
    sakut"There's no way I can c-clean up in time..."
    sara"M..."
    sara"Mooooom!?" with vpunch
    sakut"I'll have to to lie to her, just this one time! *Hic!*"
    scene black
    call hidescrollingimage from _call_hidescrollingimage_117
    sara"W-w-w-why are you..."
    saku"Nothing wrong with a woman... *Hic!*... taking care of her u-urges, you know... *Hic!*"
    sara"Y-yeah but... Were you drinking again mom!?" with vpunch
    saku"Only... *Hic!*... a little bit... *Hic!*" with vpunch
    sara"Come on mom! I told you to quit drinking! T-there's wine and s-stuff spilled everywhere!"
    sara"Is t-this about dad again?" with vpunch
    saku"Sasuke y-yes... *Hic!* I miss him... *Hic!*" with vpunch
    sara"*Sigh...* C-come on mom! Let's get you to bed. I'll clean up after..."
    default wine_counter = 0
    $ wine_counter = 1 #advances to next event
    $ wine_counter_mentioned = True #triggers one time conv
    jump action_taken



label sakura_wine_date2:
    $ initialize_replay_defaults()
    $ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    "*Knock Knock*"
    bot"."
    bot".."
    bot"...Come on, come on!" with vpunch
    call increaselust(10) from _call_increaselust_257
    bot"I am getting hard just thinking about you, Auntie!"
    $ playmusic("audio/ost/zsakura.opus", volume=0.5)
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    bot"There she is!"
    show sakurwine intro1 with dissolve:
        yalign 1.0
    show sakurwine intro1 with dissolve:
        easein 6 yalign 0.0
    bo"A...a-auntie!?" with vpunch
    saku"[bo_name]! Came back for more I see... *Giggles!*" with vpunch
    show sakurwine intro1 with dissolve:
        easein 0.2 yalign 1.0
    saku"Brought the good stuff too by the looks of it! Tonight's going to be fun..." with vpunch
    show sakurwine intro1 with dissolve:
        easein 2 yalign 0.0
    saku"Come on, come inside! You aren't shy because of m-me... are you?"
    scene black with dissolve
    bo"Of course n-not..."
    show sakurwine intro1_2ass with dissolve:
        yalign 1.0
    show sakurwine intro1_2ass:
        easein 2 yalign 0.0
    pause 1
    show screen parallax1280("sakurwine intro1_2ass",initial_ypos=1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_186
    saku"...You sure? Hihi! *Playful Giggle!*" with vpunch
    call increaselust(10) from _call_increaselust_258
    bot"She's teasing me!"
    bo"Careful Auntie... I might just pounce on you after last time!" with vpunch
    saku"No you wouldn't... Pounce on your favorite Auntie... really?"
    call hidescrollingimage from _call_hidescrollingimage_118
    if not _in_replay:
        call useItem(wine,1) from _call_useItem_11
    scene black
    saku"Give me that! *Giggles*!" with vpunch
    saku"Now go sit like the sweetie I know you are and wait for me to pour us a drink..."
    "..."
    saku"Here you go!"
    show undressing2 with dissolve:
        yalign 1.0
    show undressing2:
        easein 4 yalign 0.0
    "Sakura walked a few feet away from you after handing you your drink and turned back to address you..."
    show screen parallax1280("undressing2",initial_ypos=1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_187
    saku"I think..."
    saku"Today we should sit together, wouldn't that be nice...? *Giggles*!" with vpunch
    scene black
    call hidescrollingimage from _call_hidescrollingimage_119
    call increaselust(50) from _call_increaselust_259
    show borutodrinking 2_2 with dissolve:
        yalign 0.2
    bot"Auntie is such a fucking cock-tease!" with vpunch
    show borutodrinking 2_2 with dissolve:
        easein 0.8 zoom 1.1 yalign 1.0
    saku"Oh? I see you are having a little reaction..."
    show borutodrinking:
        easein 0.5 yalign 0.1
    saku"Are you anticipating sitting with your Auntie that much?"
    pause 0.44
    show borutodrinking 2_1 with dissolve:
        yalign 0.1
    bo"N-no, it's just... you know, m-my thing..."
    show screen parallax1280("2_app1",initial_ypos=1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_188
    saku"Your thing now... is it? Hmm..."
    saku"What I think it really is..."
    hide screen parallax1280
    show screen parallax1280("2_app2",initial_ypos=1.0)
    with dissolve
    saku"Is probably your dirty little mind, racing..." with vpunch
    "She presses her knee against your erection!" with vpunch
    call increaselust(20) from _call_increaselust_260
    saku"That little mind of yours, It's trying to figure out what the right move is to get you what you want... Isn't that right?"
    menu sdkjhfrask123:
        saku"That little mind of yours, It's trying to figure out what the right move is to get you what you want... Isn't that right?"
        "{color=[obediencecolor]}Maybe I am...{/color}":
            bo"Maybe I am, Auntie..."
            hide screen parallax1280
            show screen parallax1280("2_app2_1",initial_ypos=0.8)
            with dissolve
            bo"The question is, are you doing the same?"
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx2", loop=False, relative_volume = 1.8)
            hide screen parallax1280
            show screen parallax1280("boruto_sakura_extra_anim1",initial_ypos=0.8)
            with dissolve
            saku"Very forward [bo_name]... Impressive! But..."
            saku"You remember the rules, right?"
            scene black
            call hidescrollingimage from _call_hidescrollingimage_120



        "{color=[dominancecolor]}What I want, is you Auntie!{/color}":
            call checkDominance(20,"sdkjhfrask123") from _call_checkDominance_49
            bo"I know exactly what I want, Auntie..."
            hide screen parallax1280
            show screen parallax1280("2_app2_1",initial_ypos=0.8)
            with dissolve
            saku"...I s-see that much!"
            bo"You've got nice curves on you, Auntie, but..."
            bo"What I really want..."
            hide screen parallax1280
            show screen parallax1280("2_app2_spank",initial_ypos=0.8)
            with fade
            $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            with vpunch
            show screen parallax1280("2_app2_spank2",initial_ypos=0.8) with dissolve
            call changeDominance(1) from _call_changeDominance_120
            bo"...Is you! And I've had it with your teasing..." with vpunch
            saku"Oh m-my! That was... rough!"
            saku"Not that I mind some spice, but be patient, [bo_name]!"
            saku"This isn't teasing. This is foreplay, and it's very important to make what follows even more satisfying..."
            saku"That being said, you do remember the rules, don't you?"
            scene black
            call hidescrollingimage from _call_hidescrollingimage_121

        "Orgasm together again (Replay)":
            bo"I w-want us to have an orgasm together. Like last time..."
            saku"Such a lewd boy you are, [bo_name]..."
            scene black
            call hidescrollingimage from _call_hidescrollingimage_122
            jump replay_orgasmtogether
    bo"*Sigh...* No sex allowed, r-right...?"
    show screen parallax1280("2_drinkingtalk1",initial_ypos=1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_189
    saku"Indeed..."
    "Sakura fell on your lap, after teasing you for a while. A look of sadness quickly drained her typical bright mood..."
    saku"I hope you understand why, [bo_name]..."
    saku"As much as our needs have to be taken care of, there's something much more important than our own needs..."
    saku"Do you know what that is...?"
    menu:
        saku"Do you know what that is...?"
        "Dignity":
            saku"Not exactly..."
        "Family":
            pass
        "Safe sex!":
            bo"Safe sex! So next time I just bring condoms?"
            saku"..."
            call changesakura(-2) from _call_changesakura_42
            saku"N-no..."
    saku"It is family, [bo_name]..."
    saku"The most important thing in the world. The people you trust the most, the people you love the most..."
    saku"Me, or you... We cannot betray those that place their trust in us, okay?"
    hide screen parallax1280
    show screen parallax1280("sakurwine drinking2",initial_ypos=0.0)
    with dissolve
    saku"*Gulp*"
    "Sakura chugs most of her wine..."
    show screen parallax1280("2_drinkingtalk1",initial_ypos=0.0) with dissolve
    saku"My husband may be an idiot... *Hic!* But I still love him, you know..."
    saku"And then there's Sarada... her feelings for you..."
    menu:
        saku"And then Sarada... her f-feelings for you..."
        "What if I have feelings for you instead!":
            bo"What if I have feelings for-"
        "I don't like her!":
            bo"I don't really-"
    show screen parallax1280("blackscreen",initial_ypos=0.0)
    saku"Right-o!" with vpunch
    saku"There will be no more melancholy from here on out!"
    hide screen parallax1280
    show screen parallax1280("2_drinkingtalk2",initial_ypos=0.0)
    with dissolve
    saku"There will only be... *Hic!*... us!"
    saku"We still have a problem to solve, don't we? *Hic!*"
    saku"As long as no s-sex is involved..."  
    default sakura_drunk_counter = 0
    $ sakura_drunk_counter = 0
    menu sakura_drinkingmenu:
        saku"As long as no s-sex is involved..."
        "You are not very good with alcohol, are you Auntie?" if sakura_drunk_counter <2:
            
            if sakura_drunk_counter == 0:
                $ sakura_drunk_counter +=1
                bo"You are not very good with alcohol, are you Auntie?"
                saku"I'll have you know there's no better drinker than your Auntie in this entire nation..."
                hide screen parallax1280
                show screen parallax1280("sakurwine drinking2",initial_ypos=0.0)
                with dissolve
                saku"Just look at this!"
                "Sakura chugs her wine glass and gets a little drowsy..."
                hide screen parallax1280
                show screen parallax1280("2_drinkingtalk2",initial_ypos=0.0)
                with dissolve
                jump sakura_drinkingmenu
            elif sakura_drunk_counter == 1:
                bo"You are not fooling me! I can see it in your eyes..."
                saku"You can se... *Hic!* What in my e-eyes...?"
                bo"Those little hicups of yours are a dead giveaway Auntie! You are drunk, aren't you?"
                $ sakura_drunk_counter +=1
                hide screen parallax1280
                show screen parallax1280("sakurwine drinking_drunk",initial_ypos=0.0)
                with dissolve
                saku"A-are you kidding me? *Hic!* I could chug another one of these bottles right meow... *Hic!*" 
                hide screen parallax1280
                show screen parallax1280("2_drinkingtalk2_1",initial_ypos=0.0)
                with dissolve
                "Sakura is inebriated..."
                jump sakura_drinkingmenu

            else:
                
                jump sakura_drinkingmenu



        "{color=[obediencecolor]}Do you want me to...{/color}":
            bo"Hey A-auntie... Remember when you said there's other ways to settle our urges besides s-sex...?"
            saku"Mhm...? *Hic!*" with vpunch
            bo"Do you want me to... eat you out?"
            show screen parallax1280("blackscreen",initial_ypos=0.0) with vpunch
            saku"H-here, take this!"
            hide screen parallax1280
            show screen parallax1280("2_eather1",initial_ypos=0.0)
            with dissolve
            saku"Do you have any idea how *Hic!*... How wet I've been down there?"
            saku"Do you have any idea how in need I am of someone to take care of MY... *Hic!*... needs!?" with vpunch
            bo"A-auntie, you are bleeding!"
            saku"That's just the wine, silly..."
            show screen parallax1280("blackscreen",initial_ypos=0.0) with vpunch
            saku"NOW GET TO WORK... *Hic!*" with vpunch
            show screen parallax1280("2_eather1_1",initial_ypos=0.0) with dissolve
            bo"Shall I...?"
            saku"Are you really about to go down on your Auntie, [bo_name]?"
            bo"With p-pleasure..."
            call hidescrollingimage("Click twice to go down on her...") from _call_hidescrollingimage_123
            show 2_eather1_1 with dissolve:
                yalign 1.0
            show 2_eather1_1:
                easein 4 yalign 0.2
            bot"Auntie's pussy... Here I come!"
            pause 0.2
            $ renpy.sound.play("/audio/soun_fx/mgsalert.opus", channel="sfx3", loop=False, relative_volume = 0.9)
            pause 0.1
            show saradawake 1_2 with dissolve:
                yalign 1.0
            show saradawake:
                easein 3 yalign 0.0
            sara"...Mom?" with dissolve
            scene black with vpunch
            saku"*Gasps* O-out... *Hic!* N-NOW!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx3", loop=False, relative_volume = 2.0)
            "Upon hearing Sarada's voice, Sakura instantly snapped out of her trance-like state, and signaled for you to get out! "
            jump sarada_ending2_skaurawine


        "{color=[obediencecolor]}Have you ever sucked cock before?{/color}" if sakura_drunk_counter >= 1:
            bo"I was wondering Auntie..."
            bo"Did you ever please a man with your... mouth?"
            saku"H-hey... *Hic!* What kind of question is that..."
            bo"It's quite common isn't it...?"
            saku"Is it...? *Hic!* I've had a certain someone ask a few times... *Hic!*"
            bo"So... you've never done it before?"
            saku"I didn't say that... *Hic!*" with vpunch
            bo"I don't believe you!"
            show screen parallax1280("blackscreen",initial_ypos=0.0)
            saku"Your pants... *Hic!* Off! Right now... *Hic!*" with vpunch
            $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
            bot"*Gulp!* Is this actually going to work!?"
            hide screen parallax1280
            show screen parallax1280("sak_bj1",initial_ypos=0.8)
            with dissolve
            saku"...*Hic!*" with vpunch
            saku"Smells like... alcohol!"
            saku"Does it... taste as g-good too!? *Hic!*" with vpunch
            bo"W-why don't you... give it a try?"
            scene black
            call hidescrollingimage from _call_hidescrollingimage_124
            show sak_bj1 with dissolve:
                yalign 1.0
            show sak_bj1:
                easein 5 yalign 0.5
            saku"It's just... *Hic!*... S-so big..."
            show sak_bj2 with dissolve:
                zoom 1.1 xalign 0.5 yalign 0.6
            saku"I don't know if I can..."
            show sak_bj2_2 with dissolve:
                yalign 0.3
            $ renpy.sound.play("/audio/soun_fx/mgsalert.opus", channel="sfx3", loop=False, relative_volume = 0.9)
            pause 0.3
            show saradawake 1_2 with dissolve:
                yalign 1.0
            show saradawake:
                easein 3 yalign 0.0
            sara"...Mom?" with dissolve
            scene black with vpunch
            saku"*Gasps* O-out... *Hic!* N-NOW!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx3", loop=False, relative_volume = 2.0)
            "Upon hearing Sarada's voice, Sakura instantly snapped out of her trance-like state, and signaled for you to get out! "
            jump sarada_ending2_skaurawine

        "{color=[hatredcolor]}Let's fuck!{/color}" if sakura_drunk_counter >= 2:
            bot"She is losing it! If I could get her to drink a little more..."
            bo"You say there's no better drinker than you, right Auntie...?"
            saku"Thash 'ait! *Hic!*" with vpunch
            bo"Then how comes my glass is empty, while yours is halfway full!"
            saku"Thash 'cause... *Hic!*  I'm going easy on you."
            hide screen parallax1280
            show screen parallax1280("sakurwine drinking_drunk",initial_ypos=0.0)
            with dissolve
            saku"S-see...?"
            show screen parallax1280("blackscreen",initial_ypos=0.0) with vpunch
            $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
            saku"*Hic!*"
            hide screen parallax1280
            show screen parallax1280("2_drinkingtalk4",initial_ypos=0.0)
            with dissolve
            bo"A-auntie...?"
            saku"Fuck... *Hic!*!" with vpunch
            bot"She's fucking gone!"
            saku"...F-fffff-fuuuck!" with vpunch
            show screen parallax1280("blackscreen",initial_ypos=0.0) with dissolve
            $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
            bo"You ain't gotta tell me twice, Auntie!"
            hide screen parallax1280
            show screen parallax1280("sak_vag2",initial_ypos=1.0)
            with dissolve
            bo"You wanna fuck? Then let's fuck!" with vpunch
            show screen parallax1280("sak_vag2_1",initial_ypos=1.0, menuenabled=True) with dissolve
            bo"I am tired of all this t-teasing anyway!"
            menu:
                bo"I am tired of all this t-teasing anyway!"
                "{color=[hatredcolor]}Push it in!{/color}":
                    pass
            $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            hide screen parallax1280
            show screen parallax1280("sak_vag2_2",initial_ypos=1.0, menuenabled=True)
            with flash
            call changeHatred(1) from _call_changeHatred_182
            bo"J-just the tip, and yet your cunt is so fucking tight Auntie!" with vpunch
            saku"Ffff...fff-fffuuu" with vpunch
            menu:
                "{color=[hatredcolor]}Push it fuurther!{/color}":
                    pass
            show screen parallax1280("sak_vag2_3",initial_ypos=1.0) with dissolve
            $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            saku"Ffff-FUCK NARUTO!... *Hic!* T-that piece of s-shit... *Hic!*"
            bot"[na_rel]? W-what the fuck is going on!? Is this bitch crazy or what!?"
            call changeHatred(1) from _call_changeHatred_183
            bot"Not that it matters to me! Crazy or not, your pussy is still gripping me like crazy, Auntie!"
            call hidescrollingimage("Click twice to fuck her!") from _call_hidescrollingimage_126
            $ renpy.sound.play("/audio/soun_fx/mgsalert.opus", channel="sfx3", loop=False, relative_volume = 0.9)
            scene black with vpunch
            sara"...Mom?" with dissolve
            saku"*Gasps* O-out... *Hic!* N-NOW!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx3", loop=False, relative_volume = 2.0)
            "Upon hearing Sarada's voice, Sakura instantly snapped out of her trance-like state, and signaled for you to get out! "
            jump sarada_ending2_skaurawine


        "{color=[obediencecolor]}????{/color}" if sakura_drunk_counter < 1:
            "Get Sakura drunk to unlock!"
            jump sakura_drinkingmenu

        "{color=[hatredcolor]}????{/color}" if sakura_drunk_counter < 2:
            "Get Sakura shit-faced to unlock!"
            jump sakura_drinkingmenu

        "Orgasm together again (Replay)":
            bo"I w-want us to have an orgasm together. Like last time..."
            saku"Such a lewd boy you are, [bo_name]..."
            scene black
            call hidescrollingimage from _call_hidescrollingimage_125
            jump replay_orgasmtogether
          
        

label sarada_ending2_skaurawine:
    show saradawake 1_2 with dissolve:
        yalign 1.0
    show saradawake 1_2:
        easein 6 yalign 0.1
    sara"Is t-that you mom? *Yawns* I h-heard voices again..."
    scene black with dissolve
    saku"I am alright S-sarada, I w-was just... *Hic!* dreaming, I think..."
    sara"Mooom! When will you stop drinking this much!" with vpunch
    sara"Is t-this about dad again?" with vpunch
    saku"N-no... *Hic!* Yes? *Hic!* I don't..." with vpunch
    sara"*Sigh...* C-come on mom! Let's get you to bed you drunkard..."
    # $ wine_counter = 1 #advances to next event
    $ wine_counter_mentioned = True #triggers one time conv
    jump action_taken


