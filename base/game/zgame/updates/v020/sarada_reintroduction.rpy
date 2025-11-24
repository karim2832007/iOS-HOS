default sarada_reintro_knock = False
default sarada_reintro_complete = False
default sarada_reintro_room_underwear = False
default rand_num = 0
default shared_father_details = False



label sarada_bento_intro:

    scene black with dissolve
    "You head to the kitchen and spend some time preparing the bento box with Sakura's help."
    show screen parallax1280("chores_done sakura1",1,0.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_218
    saku "... a little more rice here, and a touch of seasoning on the salmon."
    saku "Don't forget the pickled vegetables around the tamagoyaki, it has to be just right!"
    saku "Aaaand... There! Perfect!"
    scene black
    call hidescrollingimage from _call_hidescrollingimage_182
    saku "Now, this is a bento worthy of an Uchiha! She'll love it!"
    "Sakura carefully packages the food in a bento box, before passing it to you and leading you to Sarada's bedroom."
    bo "It looks great, and smells even better... Thanks Auntie!"
    hide screen parallax1280
    show bg uchiha_bedroom 
    with dissolve
    show sakura normal:
        xpos -100
    show boruto normal:
        xpos 300
    with dissolve
    saku "Of course it does! YOU prepared this with love after all, didn't you?"
    show boruto embarassed with dissolve
    bo"R-right..."
    show boruto normal with dissolve
    saku "Now, remember! This isn't about the food! It's about the act itself..."
    show sakura:
        easein 0.2 xalign 0.3
    show boruto normal:
        easein 0.3 xalign 0.5
    pause 0.2
    show boruto surprised with dissolve
    $ renpy.sound.play("/audio/soun_fx/smack.opus", channel="sfx1", loop=False, relative_volume = 0.3)
    "Sakura gives you an encouraging smack on the back!" with vpunch
    saku "It's time to get in there and show her you care!"
    hide sakura with dissolve
    saku"And don't forget to ask her out! *Giggles*!" with vpunch
    bo "R-right..."
    saku "*Encouraging whisper from afar* You got this!" with vpunch
    hide boruto
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/footsteps_hesitant_floor.opus", channel="sfx1", loop=False, relative_volume = 1.5)
    show bg uchiha_bedroom:
        subpixel True
        easein 5 zoom 1.2 xalign 0.5 yalign 0.6
    "You approach Sarada's door with a knot in your stomach, hiding the bento box behind your back as a surprise."
    bot "Here goes nothing... Keep it together, [bo_name]!"
    $ renpy.sound.play("/audio/soun_fx/gulp_nervous_male.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    bot "*Gulp*"
    menu:
        "Knock on her door":
            $ sarada_reintro_knock = True
            $ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx3", loop=False, relative_volume = 0.8)
            "You decide to knock on the door, hoping to catch Sarada in a good mood."
            play sound "audio/soun_fx/dooropen.opus" volume 0.7
            scene black with dissolve
            "..."
            scene bg saradabedroom
            show sarada angry3 at center
            with dissolve
            "She opens the door momentarily after, looking annoyed as soon as she realizes it's you."
            show sarada at smallshake
            sara "Look who decided to show up... UNANNOUNCED!" with vpunch
            show boruto embarassed at left
            show sarada at right
            with dissolve
            bo "H-hey Sarada, how's it going? It's n-nice to see you too..."
            sara "What do {i}you{/i} want? Who even let you in our house in the first place?" with vpunch
            show boruto worried with dissolve
            bo "I've been, uhm, thinking about you lately. I thought it'd be nice to catch up."
            show sarada angry with dissolve
            sara "Don't make me laugh! Since when do you think about anything other than yourself?"
            sara "Get out of my sight, I don't want to talk to you right now..." 
            show boruto surprised2 with dissolve
            bot "I expected this much. I guess it's time to play my trump card!"
            show boruto snob with dissolve
            bo "You sure about that? I've even brought you something!" with vpunch
            pass


        "Barge in and surprise her!":
            "You decide to barge in without knocking, hoping to surprise her!"
            play sound "audio/soun_fx/dooropen.opus" volume 0.7
            "Before you can even reach for the door handle, it swings open, revealing an angry Sarada."
            show sarada angry at right
            show boruto embarassed at left
            with dissolve
            sara "Huh? What the hell are you doing outside my door, creep?" with vpunch
            "Sarada glares at you, her eyes filled with irritation."
            bo "I-I was just about to come in and see you!"
            call changesarada(-1) from _call_changesarada_10
            sara "You were about to come {i}inside{/i}? Without knocking? \nDo you have a death wish?!"
            show boruto snob with dissolve
            bo "Heh, I, uh-... I'd rather stay alive... but I do have something for you!"
            pass
            
        
    show sarada flustered at right with dissolve
    sara "Y-you... brought something for me?"
    show sarada angry at right with dissolve
    show sarada at smallshake
    sara "Hmph! Probably another one of your stupid pranks, isn't it?"
    show boruto at smallshake
    bo "Come on, Sarada... You haven't even seen what it is yet!"
    show sarada snob with dissolve
    sara "I don't need to, I already know it's something dumb!" with vpunch
    show boruto:
        easein 2 xalign 0.5
    scene black with dissolve
    bo "You sure about that...?"
    "You pass the carefully wrapped bento box to Sarada, without yet spoiling the surprise..."
    show v20_1sarada_bento1 with dissolve:
        zoom 1.4 yalign 1.0
    show v20_1sarada_bento1:
        subpixel True
        easein 5 yalign 0.41 xalign 0.5
    
    sara "A... box?" with vpunch
    bo "Not just any box... Guess what's inside!"
    show v20_1sarada_bento1:
        easein 0.2 yalign 1.0
    sara"Is this...!?" with vpunch
    scene black with dissolve
    "Sarada turns her back on you as if to hide her reaction while unwrapping the box..."
    show v20_1sarada_bento2 with dissolve
    bo "Remember all the time we used to spend together, sparring each other damn near death...?"
    sarat "*Silent gasp*!" with vpunch
    bo"We'd then sit under the shadow of a tree and share something like this together. I thought that maybe we..."
    bo"M-maybe we could do that again some time?"
    sarat "Aww... How sweet of him! He still thinks about our time together!"
    call changesarada(2) from _call_changesarada_11
    sarat"Just like how I do... all the time!"
    show v20_1sarada_bento3 with dissolve:
        zoom 1.1 xalign 0.5 yalign 0.0
    sarat "D-does that mean he still l-likes me!?" with vpunch
    scene v20_1sarada_bento2 with dissolve:
        zoom 1.2 yalign 0.0 xalign 0.5
    sarat "N-no! Get it together girl!" with vpunch
    scene black with dissolve
    sarat "I can't think like that. All it'll do is lead to more disappointment..."
    scene bg saradabedroom
    show boruto sad at left
    show sarada angry3 at right
    with dissolve
    "She snaps out of her thoughts and her frown instantly returns."
    sara "You {i}truly are{/i} dumb, but at least this is one of your less dumb ideas."
    show sarada at smallshake
    sara "So what, you think this makes us friends again or s-something?"
    show boruto worried at left with dissolve
    bo "I-I don't know... But what I {i}do{/i} know is that I really miss the time we used to spend together."
    bo "I also know things have been rough between us, but I hope we can get back to that someday."
    bo "Besides... I could use the training, I haven't been able to keep up with it lately!"
    show sarada angry at right with dissolve
    sara "That's because you're a lazy idiot who doesn't take anything seriously!" with vpunch
    sara "Training is important, you should know that by now!"
    sara "You can't just slack off and expect to be strong!"
    show boruto embarassed at left with dissolve
    bo "Heh, I know, I know... \nIt's just that I've been so busy with everything else."
    sara "Busy with what?! Sleeping and goofing off?" with vpunch
    show boruto snob at left with dissolve
    bo "I bet I could still beat you in a fight though, even without training!"
    show sarada angry2 at smallshake
    sara "What?!" with vpunch
    sara "In your dreams, idiot!" with vpunch
    bo "Heh, maybe we should settle this with a little sparring match sometime...?"
    bo "What do you say, Sarada? \nA little friendly competition to see who's stronger?"
    bo "Or are you too scared to face me?"
    show sarada snob at right 
    sara "Scared? Me?! Don't make me laugh!" with vpunch
    show boruto smirk2 at left
    bo "Then it's settled! Whenever you're ready, we can have a little sparring session and see what you're made of these days."
    sara "Hmmph, fine! But don't expect me to go easy on you!" with vpunch
    sara "And don't think this means we're friends now either, got it?" with vpunch
    show sarada at smallshake
    sara "Now get the hell out of here, I have things to do!"
    show boruto smirk at left with dissolve
    bo "Okay, okay, I get it! I'll leave you alone for now."
    bo "But I'll be back soon, and next time... I'll be ready to take you on!"
    bo "See you around, Sarada!"
    sara "Yeah, w-whatever!"
    if sarada_reintro_knock == False:
        sara "And don't you dare try to barge in here again without knocking!" with vpunch
    hide boruto with dissolve
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 1.5)
    "..."
    show v20_1sarada_bento3 with dissolve
    sarat "I can't believe he actually did something so thoughtful..."
    sarat "And he did it for m-me... Maybe he isn't as clueless as I thought he was!"
    scene black with dissolve
    $ sarada_reintro_complete = True
    call changesarada(1) from _call_changesarada_12
    "You can now choose to spend time with Sarada."
    jump action_taken


label sarada_reintro_door:

    default sarada_talk = 0
    $ sarada_reintro_room_underwear = False

    menu:
        bot"Better take it slow with her..."

        "Knock on her door.":
            $ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx2", loop=False, relative_volume = 0.8)
            "*Knock knock*"
            bo"H-hey Sarada, it's me..."
            sara "Come in!"
            scene bg saradabedroom with fade 
            show sarada happy at left 
            show boruto suspicious at right
            with dissolve
            "You enter Sarada's room, finding her sitting on her bed, looking a bit surprised to see you."
            sara "Hey, [bo_name]! What brings you here?"
            jump sarada_menu_repeatable


        "Barge inside" if sarada_relationship < 25:
            "You decide to barge in without knocking, hoping to surprise her."
            $ rand_num = renpy.random.random()

            # 1st option 30% chance  low relationship - fail version (shared with high relationship)
            if rand_num < 0.3:
                jump sarada_reintro_bargein_masturbating

            # 2nd option 70% chance    low relationship - fail version 
            else:
                call randomCheck(False,"Nothing interesting is happening...") from _call_randomCheck_7
                bot "I bet she'll be so happy to see me again!"
                play sound "audio/soun_fx/dooropen.opus" volume 0.7
                scene black with dissolve
                bo"Hey Sarada, guess who's here to see you!"
                scene sarada_barge 1 with fade:
                    zoom 1.2 xalign 0.0 yalign 1.0
                show sarada_barge:
                    subpixel True
                    easein 8 zoom 1.0 xalign 0.5 yalign 0.7
                "Sarada being utterly lost in her reading, took a second before realizing your unannounced intrusion..."
                call increaselust(10) from _call_increaselust_276
                bot"Oh she's studying again... And in those lovely black panties! They shape so well around her bottom!"
                show sarada_barge 1_1 with vpunch:
                    zoom 1.1
                sara"[bo_name_stutter]!?" with vpunch
                "Sarada turned to you with a look you knew all too well from days old..."
                "The fiercest look you've ever seen a woman with, you know what is about to happen..."
                bot"Oh s-shit! Bad timing? Maybe I can just try to play it off..."
                bo"H-hey, you look quite nice today, how's it going? Heh-eh..."
                show sarada_barge 1_1 with dissolve:
                    zoom 1.2 xalign 0.0
                sara"Y-you..."
                $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 1.2)
                with Shake((0, 0, 0, 0), 2, dist=10, peak_time=2, smoothness=50)
                scene black with vpunch
                sara"GET THE HELL OUT OF HERE YOU BLASTED HALF-WIT!" with vpunch
                jump sarada_reintro_bargein_thrownout


        "{color=[obediencecolor]}???{/color}" if sarada_relationship < 25:
            call checkSarada(25) from _call_checkSarada_8
            "Increase your relationship with Sarada first to unlock this option."
            jump sarada_reintro_door

        "{color=[obediencecolor]}Barge inside{/color}" if sarada_relationship >= 25:
            call checkSarada(25) from _call_checkSarada_9
            "You decide to barge in without knocking, hoping to surprise her."
            $ rand_num = renpy.random.random()
            # 1st option 30% chance  high relationship - success version
            if rand_num < 0.3:
                label sarada_reintro_bargein_masturbating:
                    $ initialize_replay_defaults()
                    call randomCheck(True,"You hear something!") from _call_randomCheck_8
                    bot "I bet she'll be so happy to see me again!"
                    play sound "audio/soun_fx/dooropen.opus" volume 0.7
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/femalemastmoan1.opus", channel="sfx2", loop=True, relative_volume = 0.9)
                    sara"Uh... ♡ Ahh...! ♡"
                    hide screen parallax1280
                    show screen parallax1280("sarada_masturbating", zoom = 1.25, initial_ypos = 0.0) 
                    with dissolve
                    call showscrollingimage from _call_showscrollingimage_219
                    bot"...!" with vpunch
                    call increaselust(10) from _call_increaselust_277
                    bot"Is she m-masturbating?"
                    hide screen parallax1280
                    show screen parallax1280("sarada_masturbating1", zoom = 1.25, initial_ypos = 0.0, menuenabled = True)
                    with dissolve 
                    $ renpy.sound.play("/audio/soun_fx/eyesharingan1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    sara "W-who the f-...!"
                    sara "WHAT THE HELL ARE YOU DOING IN HERE, [bo_name.upper()]?!" with vpunch
                    bot "S-shit! I guess I should have knocked first..."
                    menu sarada_reintro_bargein_highrel:
                        "I thought this was the bathroom?" if sarada_relationship <50:
                            bo "I-I uhm... Sorry, I thought t-this was the bathroom?"
                            call hidescrollingimage("Click twice to get ready to RUN!") from _call_hidescrollingimage_183
                            show sarada_masturbating1 with dissolve:
                                zoom 1.25, yalign 0.0
                            sara "B-bathroo-...?"
                            $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 1.2)
                            with Shake((0, 0, 0, 0), 2, dist=10, peak_time=2, smoothness=50)
                            scene black with vpunch
                            sara"GET THE HELL OUT OF HERE YOU BLASTED HALF-WIT!" with vpunch
                            label sarada_reintro_bargein_thrownout:
                                $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                show bg uchiha_bedroom with dissolve
                                show boruto surprised3 at left with dissolve
                                bot "Well shit, how was I supposed to know she was busy?!"
                                show boruto embarassed with dissolve
                                bot "I guess that's what I get for not being careful..."
                                show sakura angry at right with dissolve
                                saku"[bo_name]...? What happened?"
                                saku "Did you do something stupid even after my warning?!"
                                show boruto at smallshake
                                bo"M-me? Noo... I would never...!"
                                bo"I think Sarada is just having one of those days... Heh-eh!"
                                show boruto surprised2 with dissolve
                                sara"{i}You're{/i} about to have one of your LAST days if I come outside and you're still there!" with vpunch
                                sara"MOOOM! GET HIM THE HELL OUT OF HERE!"
                                show sakura serious with dissolve
                                show sakura:
                                    easein 0.7 xalign 0.5
                                saku"{size=*0.8}Pst... I think now is a good time to leave. \nMaybe come back when she's cooled down a little bit!{/size}"
                                scene black with dissolve
                                "Unwilling to push your luck any further, you quickly take your leave from the household and return back home."
                                jump action_taken



                        "Mind if I come in?" if sarada_relationship >=50:
                            call checkSarada(50) from _call_checkSarada_10
                            bo"Hehe, mind if I come in?"
                            sara "Y-yes, I do mind!" with vpunch
                            sara "I'm a little busy here, can't you see?!"
                            bot "Oh, I can see alright..."
                            scene black
                            call hidescrollingimage from _call_hidescrollingimage_184
                            sara"Tsk! Just... t-turn around and give me a minute!"
                            
                            scene bg saradabedroom with fade 
                            show sarada underwear_angry2 at left
                            show boruto smirk at right
                            with dissolve
                            $ sarada_reintro_room_underwear = True
                            sara "Unbelievable... Can you at least knock next time so I have time to get dressed?!"
                            bo "And miss this view? Hehe..."
                            show sarada underwear_serious with dissolve
                            sara "Ughh... So what brings you here anyway?"
                            jump sarada_menu_repeatable
                

                        "{color=[obediencecolor]}???{/color}" if sarada_relationship < 50:
                            call checkSarada(50) from _call_checkSarada_11
                            "Increase your relationship with Sarada first to unlock this option."
                            jump sarada_reintro_bargein_highrel

                        "{color=[obediencecolor]}Calm down, cutie!{/color}" if sarada_relationship >= 50:
                            call checkSarada(50) from _call_checkSarada_12
                            bo "Calm down, cutie! It's only me..."
                            bo "No need to be embarassed!" 
                            sara "C-cutie?!" with vpunch
                            sara "I don't care how close we've gotten lately, you can't just barge in here like you own the place!"
                            bo "Oh come on, Sarada! You know I didn't mean to catch you like this!"
                            bo "I just came to surprise you and spend some time together!"
                            bo "Although, I must say... \nYou look so amazing with your hands down your panties!"
                            hide screen parallax1280
                            show screen parallax1280("sarada_masturbating", zoom = 1.25, initial_ypos = 0.0, menuenabled = True)
                            with dissolve 
                            sara "H-hey! You can't say stuff like that!" with vpunch
                            sara "And don't just stand there gawking at me!" 
                            menu sarada_reintro_bargein_highrel_mast:
                                "I can't help it, you're so hot!":
                                    bo "I can't help it, you're so hot!"
                                    bo "I mean, look at you!"
                                    bo "So beautiful and sexy, I just can't take my eyes off you!"
                                    hide screen parallax1280
                                    show screen parallax1280("sarada_masturbating2", initial_ypos = 0.0)
                                    with dissolve
                                    sara "Y-you really think so?"
                                    sara "You're not just saying that to save your skin, are you?"
                                    bo "No, I really mean it! \nI think you're an incredible woman, Sarada..."
                                    bo "I love how strong and determined you normally are... \nBut I also {i}love{/i} seeing this side of you!"
                                    bo "So vulnerable and relaxed, and watching that tight body of yours getting the attention it deserves turns me on!"
                                    hide screen parallax1280
                                    show screen parallax1280("sarada_masturbating", zoom = 1.25, initial_ypos = 0.0) 
                                    with dissolve
                                    $ renpy.sound.play("/audio/soun_fx/femalemastmoan1.opus", channel="sfx3", loop=True, relative_volume = 0.9)
                                    sara "O-oh... [bo_name]... ♡"
                                    bot "Heh, look at her touching her dripping wet pussy again, she just can't help herself!"
                                    sara "I-I... I need some alone time for a bit, okay?"
                                    sara "I'm not mad at you, b-but I just need space to... \nF-finish what I started here..."
                                    bo "Of course, I understand..."
                                    bo "I'll leave you to it but I'll be thinking about you, Sarada."
                                    bo "And wishing I was still here to watch you squirm and hear you moan!"
                                    $ renpy.sound.play("/audio/soun_fx/femalemastmoan2.opus", channel="sfx3", loop=True, relative_volume = 1.5)
                                    sara "H-hey! Ahh... ♡"
                                    sara "J-just go already!" with vpunch
                                    "With a smirk on your face and a final glance at Sarada losing herself in pleasure, you decide to leave her be for now."
                                    bo "Enjoy then!"
                                    sara "M-mhmm... ♡"
                                    call hidescrollingimage("Click twice to leave Sarada's room.") from _call_hidescrollingimage_185
                                    $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                                    show bg uchiha_bedroom with dissolve
                                    show boruto smirk2 at center with dissolve
                                    bot "Poor girl has needs too, I guess..."
                                    show boruto sceeming with dissolve
                                    bot "But damn, she's so hot when she gets going like that!" with vpunch
                                    show boruto sceeming2 with dissolve
                                    bot "I should maybe try and join her next time..."
                                    bot "You feisty little fox... You'll be mine, Sarada!"
                                    scene black with fade
                                    jump action_taken


                            
                                "{color=[dominancecolor]}I'll come help you instead{/color}":
                                    call checkDominance(20, "sarada_reintro_bargein_highrel_mast") from _call_checkDominance_60
                                    bo "You're right, it's rude of me to just stand here and stare!"
                                    bo "Let me come over and help you out, instead..."
                                    hide screen parallax1280
                                    show screen parallax1280("sarada_masturbating1", zoom = 1.25, initial_ypos = 0.0) 
                                    with dissolve
                                    sara "H-help me out?! That's not what I meant, idiot!" with vpunch
                                    bo "Heh, you say that... But look at you!"
                                    bo "You haven't even taken your hands out of those panties yet..."
                                    hide screen parallax1280
                                    show screen parallax1280("sarada_masturbating", zoom = 1.25, initial_ypos = 0.0, menuenabled = True)
                                    with dissolve
                                    $ renpy.sound.play("/audio/soun_fx/femalemast1.opus", channel="sfx2", loop=True, relative_volume = 1.4)
                                    sara "I-I... I just like how it feels, okay?!"
                                    sara "It t-tingles so much down there... I don't want to stop! ♡"
                                    hide screen parallax1280
                                    show screen parallax1280("sarada_masturbating4")
                                    with dissolve
                                    bo "I'm starting to think you secretly like it when I catch you like this, am I right?"
                                    sara "Wha-... Shut up!" with vpunch
                                    bo "Tell me the truth, Sarada... What is it that goes through your mind when you're all worked up like this?"
                                    bo "Is it me you think about when you touch yourself?"
                                    bo "Do you fantasize about it being my hands on your body, instead of your own?"
                                    sara "I-I... No! W-why would it be{i} you {/i}I'm thinking about?!"
                                    bo "Oh come on, Sarada! I know you better than that!"
                                    bo "Let's test a theory of mine... Shall we?"
                                    hide screen parallax1280
                                    show screen parallax1280("sarada_masturbating_anim2", initial_ypos=1.0)
                                    with dissolve
                                    $ renpy.sound.play("/audio/soun_fx/kyaa.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                    sara "*gasp*" with vpunch
                                    sara "H-hey! W-what are you doing?!"
                                    bo "I've seen the way you look at me, the way you crave my attention..."
                                    bo "You can't fool me, I know you lust for me just as much as I do for you!"
                                    sara "I-I don't lust for you! I j-just... W-wait... Y-you want me t-too?!"
                                    hide screen parallax1280
                                    show screen parallax1280("sarada_masturbating_anim1", initial_ypos=0.0) 
                                    with dissolve
                                    bo "I always have..."
                                    $ renpy.sound.play("/audio/soun_fx/himawari/himagasp.opus", channel="sfx3", loop=False, relative_volume = 1.5)
                                    sara "O-oh... "
                                    hide screen parallax1280
                                    show screen parallax1280("v020_sarada_fingering_anim1", initial_ypos=1.0)
                                    with dissolve
                                    $ renpy.sound.play("/audio/soun_fx/femalemastmoan2.opus", channel="sfx2", loop=True, relative_volume = 1.5)
                                    sara "M-mmh... ♡"
                                    bot "F-fuck, she's so hot!" with vpunch
                                    bot "Her pussy is soaking wet and so tight, I feel those walls squeezing my fingers on all sides..."
                                    sara "O-oh [bo_name]... Don't you d-dare stop! That feels s-so good!♡"
                                    call hidescrollingimage("Click twice to kiss her neck as you finger her.") from _call_hidescrollingimage_186
                                    show screen parallax1280("sarada_masturbating5")
                                    with dissolve
                                    $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                                    $ renpy.sound.play("/audio/soun_fx/femalemastmoan1.opus", channel="sfx2", loop=True, relative_volume = 1.5)
                                    bo "Mmm-m..."
                                    bo "I'm taking you all the way, Sarada... There's no stopping now!"
                                    $ renpy.sound.play("/audio/soun_fx/femalemast3.opus", channel="sfx2", loop=True, relative_volume = 2.3)
                                    $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx1", loop=True, relative_volume = 3.5,fadein=0.3)
                                    "Her breathing starts to speed up, with quick short gasps of air woven in between."
                                    "You match that pace by speeding up your hands working on her, escalating her pleasure as she nears her inevitable orgasm."
                                    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                    sara "O-OH F-FUU-... YESS ♡" with flash
                                    bo "There you go... You're so close, I can feel your pussy pulsing from the inside!"
                                    bo "Cum for me Sarada, I want to feel you release all over my fingers!"
                                    sara "J-just like that! Don't stop, don't stop!" with vpunch
                                    $ renpy.sound.play("/audio/soun_fx/cum0.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                    show screen parallax1280("sarada_masturbating6") with flash
                                    sara "YES, Y-YES, YES! ♡"
                                    $ renpy.sound.play("/audio/soun_fx/cum9.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                    $ renpy.sound.play("/audio/soun_fx/femaleorgasm.opus", channel="sfx1", loop=False, relative_volume = 1.6,fadein=1)
                                    show screen parallax1280("sarada_masturbating6") with flash
                                    sara "AHHHH F-FUUUUCK YES! ♡♡"
                                    $ renpy.sound.play("/audio/soun_fx/femalemast3.opus", channel="sfx2", loop=False, relative_volume = 2.3)
                                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                    show screen parallax1280("blackscreen") with longerflash
                                    "Sarada's body trembles as she finishes her climax, exhausted and satisfied as she rides out the waves of pleasure."
                                    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    bo"You are shivering! Here, you should probably wear this."
                                    hide screen parallax1280
                                    call showscrollingimage from _call_showscrollingimage_220
                                    show screen parallax1280("sarada_masturbating7", initial_ypos=1.0) 
                                    with dissolve
                                    sara"*Heavy breathing* W-what the..."
                                    bo "Woah, there's so much of it! I never knew you had it in you, Sarada!"
                                    bo "You look like you really needed to get that out of your system!"
                                    sara "A-ah... I-I... I need a second..."
                                    sara "A-are my legs still there? I can't feel them right now..."
                                    sara "S-so good... I can't believe you made me cum so hard!"
                                    scene black
                                    call hidescrollingimage from _call_hidescrollingimage_187
                                    "You both take some time to gather yourselves."
                                    scene bg saradabedroom with dissolve
                                    show sarada underwear_angry at left
                                    show boruto snob at right
                                    with dissolve
                                    sara "Ugh... I need to clean up now, look what you did, idiot!" with vpunch
                                    show sarada at smallshake
                                    sara "It's never been that messy before!"
                                    bo "Heh, seems like it was worth it, you went really hard!"
                                    show sarada underwear_normal with dissolve
                                    sara "I don't remember asking for your commentary, zip it!"
                                    bot "Back to her old self, I see... Haha!"
                                    show sarada underwear_angry2 with dissolve 
                                    show sarada at smallshake
                                    sara "Now get out of here, before Mom comes back and finds us here like this!"
                                    if sakura_helpherout == True:
                                        show boruto sceeming3 with dissolve
                                        bot "If only you knew the lengths I've been to with to with Auntie already..."
                                        bot "Makes me wonder... Would she even mind finding us here like this? Or would she..."
                                    scene black with fade
                                    bo "Okay, okay! I'll leave you to it..."
                                    bo "But this was a lot of fun! I enjoyed it!"
                                    sara "I- I... I did too... ♡"
                                    $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                                    sara "Now go!" with vpunch
                                    if day_part == 0 or day_part == 1 or day_part == 2:
                                        scene black
                                        scene inohouse day with dissolve

                                    else:
                                        scene black
                                        scene inohouse night with dissolve
                                    show boruto smirk2 at center with dissolve
                                    bot "Poor girl has needs too, I guess..."
                                    show boruto sceeming with dissolve
                                    bot "But damn she's so hot when she starts to get going!" with vpunch
                                    show boruto sceeming2 with dissolve
                                    bot "I'd bet she'll be swooning over me if I play my cards right!"
                                    scene black with fade
                                    jump action_taken

            # 2nd option 70% chance   high relationship - success version
            else:
                call randomCheck(False,"Nothing interesting is happening...") from _call_randomCheck_9
                bot "I bet she'll be so happy to see me again!"
                play sound "audio/soun_fx/dooropen.opus" volume 0.7
                scene black with dissolve
                bo"Hey Sarada, guess who's here to see you!"
                scene sarada_barge 1 with dissolve:
                    zoom 1.2 xalign 0.0 yalign 1.0
                show sarada_barge:
                    subpixel True
                    easein 4 zoom 1.0 xalign 0.5 yalign 0.7
                "Sarada being utterly lost in her reading, took a second before realizing your unannounced intrusion..."
                call increaselust(10) from _call_increaselust_278
                bot"Oh she's studying again... And in those lovely black panties! They shape so well around her bottom!"
                show sarada_barge 1_1 with dissolve:
                    zoom 1.1
                sara"[bo_name_stutter]!?" with vpunch
                "Sarada turned to you with a look you knew all too well from days old..."
                "The fiercest look you've ever seen a woman with, you know what is about to happen..."
                bot"Oh s-shit! Bad timing? Maybe I can just try to play it off..."
                bo"H-hey, you look quite nice today, how's it going? Heh-eh..."
                sara "I don't care how close we've gotten lately, you can't just barge in here like you own the place!"
                bo "Oh come on, Sarada! You know I didn't mean to catch you like this!"
                bo "I just came to surprise you and spend some time together!"
                bo "Although, I must say... \nI think you look incredibly hot in those panties!"

                show sarada_barge 1_1 with dissolve:
                    zoom 1.2 xalign 0.0
                sara "Y-you... do?" with vpunch
                bo "Without a doubt!"
                sara "W-well... I guess if you like them, I don't mind it then..."
                bot "Oh wow, she must really be getting comfortable with me if she's going to stay like for me..."
                bot "I could get used to this!"

                scene bg saradabedroom with fade 
                show sarada underwear_normal at left
                show boruto normal at right
                with dissolve
                $ sarada_reintro_room_underwear = True
                sara "So... What brings you here anyway?"
                jump sarada_menu_repeatable





    menu sarada_menu_repeatable:
        "Talk":
            menu sarada_menu_talkrepeatable:
                sara "What do you want to talk about?"

                "About Sakura"(greyed_out = (sarada_talk>=1)):
                    if sarada_talk == 0:
                        $ sarada_talk += 1

                    bo "How is your mom doing, Sarada?"
                    bo "She still being the overprotective parent she always was?"
                    sara "Ah yeah, she is... But I guess that's just how she is as a person."
                    sara "She always wants to make sure I'm safe and happy, even if it means being a bit overbearing at times."
                    sara "It comes from a good place, so I can't really blame her for it."
                    bo "You don't seem too thrilled about it, though..."
                    bo "Is there something else going on between you two?"
                    if sarada_reintro_room_underwear == True:
                        show sarada underwear_normal2 with dissolve
                    sara "Well, it's not that I don't appreciate her concern, but sometimes it feels like she doesn't trust me to take care of myself."
                    sara "I just wish she would give me a little more space to grow and learn on my own."
                    bo "Yeah I get that, it's tough when parents don't realize you're not a kid anymore."
                    bo "But I also understand that she is just trying to protect her little girl."
                    if sarada_reintro_room_underwear == True:
                        show sarada underwear_angry with dissolve
                    else:
                        show sarada angry with dissolve
                    sara "I'm not a little girl anymore, [bo_name]!" with vpunch
                    sara "If only she would protect me from your annoying ass instead!"
                    if sarada_reintro_room_underwear == True:
                        show sarada underwear_normal with dissolve
                    else:
                        show sarada happy with dissolve
                    jump sarada_menu_talkrepeatable

                "About her Father"(greyed_out = (sarada_talk>=2)) if sarada_relationship >= 10 and sarada_talk >= 1:
                    # Don't keep doing the stat check if it already passed once
                    if shared_father_details == False:
                        call checkSarada(10) from _call_checkSarada_13
                        $ shared_father_details = True
                    if sarada_talk == 1:
                        $ sarada_talk += 1
                    bo "I was wondering about your dad, Sasuke..."
                    bo "Any news from him lately?"
                    sara "Sadly nothing, it's been radio silence for quite a while..."
                    sara "I bet he's just really busy with one of his dangerous missions again, he'll eventually come around again like always."
                    sara "I just wish I could join him, you know...?"
                    bo "You must really miss him..."
                    if sarada_reintro_room_underwear == True:
                        show sarada underwear_serious at left with dissolve
                    sara "I do, yeah... But I've been training so hard, I want to also prove to him how capable I've become!"
                    bo "Give it some more time, I'm sure you'll be out and about saving the world just like him soon enough!"
                    sara "I really hope so, [bo_name]!"
                    sara "Although I can't imagine leaving mom all alone here..."
                    if sarada_reintro_room_underwear == True:
                        show sarada underwear_normal2 at left with dissolve
                    sara "She would be devastated if I left her alone for too long, especially with dad being away so much."
                    sara "She get's really lonely sometimes, and I try to be there for her as much as I can, but it's not always easy."
                    if sarada_reintro_room_underwear == True:
                        show sarada underwear_flustered at left with dissolve
                    sara "I've caught her drinking and... crying... a few times late at night recently."
                    if sarada_reintro_room_underwear == True:
                        show sarada underwear_normal at left with dissolve
                    sara "I just wish I could do more to help her, but I don't know how..."
                    bo "You two are really close, aren't you?"
                    sara "Yeah, of course... We're all each other has left, so we have to look out for one another."
                    show sarada at smallshake
                    sara "I'd do anything for her!"
                    show boruto sceeming with dissolve
                    bot "Anything, huh? Hehe..."
                    show boruto suspicious with dissolve
                    jump sarada_menu_talkrepeatable


                "{color=[obediencecolor]}About that Family Photo{/color}" if sarada_relationship >= 30 and sarada_dildo_found == True and sarada_talk >= 2:
                    call checkSarada(30) from _call_checkSarada_14
                    show boruto normal with dissolve
                    bo "I found this family photo of you, your mom and dad. It's really nice!"
                    if sarada_reintro_room_underwear == True:
                        show sarada underwear_angry at left with dissolve
                    else:
                        show sarada angry at left with dissolve
                    sara "Have you been snooping around my stuff again, [bo_name]?!" with vpunch
                    show boruto suspicious with dissolve
                    bo "No, no! I just stumbled upon it while cleaning up a little!"
                    bo "I thought it was a really nice picture of you three, so I wanted to ask about it!"
                    sara "Hmmph, why are you even cleaning up my room anyway?!"
                    if sarada_reintro_room_underwear == True:
                        show sarada underwear_normal at left with dissolve
                    else:
                        show sarada happy at left with dissolve
                    sara "But yeah..."
                    sara "Dad gave me that a while back to remind me of him and how much he loves us while he's away on his missions."
                    sara "I like looking at it sometimes, it makes me feel closer to him."
                    bo "Yeah, I get that... Must be hard not having him around all the time."
                    bo "The message on the photo is really sweet though, I can see why you cherish it so much."
                    bo "{i}- Your strength and determination makes me prouder than you'll ever know{/i}."
                    bo "It's a reminder that he believes in you and your potential, even when he's not there to tell you it in person."
                    if sarada_reintro_room_underwear == True:
                        show sarada underwear_normal2 at left with dissolve
                    sara "Yeah, Dad has always been my biggest supporter! Always encouraging me to be strong and follow my dreams."
                    sara "When he's back, I just want to show him how much I've grown and how much I appreciate everything he's done for me. For us..."
                    sara "Me and Mom really miss him, it's never the same without him..."
                    show boruto sceeming with dissolve
                    bot "Sounds like they could both really use a man around the house, hehe..."
                    show boruto suspicious with dissolve
                    jump sarada_menu_talkrepeatable

                "???" if sarada_relationship >= 10 and sarada_talk < 1:
                    call randomCheck(False, " ") from _call_randomCheck_10
                    "Exhaust previous talk options to unlock this."
                    jump sarada_menu_talkrepeatable

                "???" if sarada_relationship < 10:
                    call checkSarada(10) from _call_checkSarada_15
                    "Improve your relationship with Sarada and exhaust previous talk options to unlock this."
                    jump sarada_menu_talkrepeatable

                "???" if sarada_relationship < 30:
                    call checkSarada(30) from _call_checkSarada_16
                    "Improve your relationship with Sarada, exhaust previous talk options and stumble upon a particular item to unlock this."
                    jump sarada_menu_talkrepeatable
                
                "???" if sarada_relationship >= 30 and (sarada_dildo_found == False or sarada_talk < 2):
                    call randomCheck(False, " ") from _call_randomCheck_11
                    "Exhaust previous talk options and stumble upon a particular item to unlock this."
                    jump sarada_menu_talkrepeatable


                "Return":
                    jump sarada_menu_repeatable


        
        "Interact":
            menu sarada_menu_interactrepeatable:
                sara "What did you have in mind?"

                "Let's spar!":
                    if day_part == 1 or day_part == 2:
                        pass
                    else:
                        sara "It's a bit late for that, don't you think?"
                        sara "I feel like it would be a lot more productive if we did it another day instead."
                        jump sarada_menu_interactrepeatable
                    show boruto sceeming at right with dissolve
                    bo "How about we have a little sparring match today?"
                    sara "Sure, I could use the warm-up!"
                    if sarada_reintro_room_underwear == True:
                        show sarada underwear_serious at left with dissolve
                    else:
                        show sarada flustered at left with dissolve
                    sara "Just don't expect me to go easy on you!"
                    show boruto smirk at right with dissolve
                    bo "I wouldn't dream of it! Let's see what you've got!"
                    scene black with fade
                    jump sarada_boruto_sparring

                "Let's hang out here!":
                    bo "How about we just hang out here for a bit?"
                    if sarada_relationship < 50:
                        call checkSarada(50) from _call_checkSarada_17
                        if sarada_reintro_room_underwear == True:
                            show sarada underwear_angry at left with dissolve
                        else:
                            show sarada angry at left with dissolve

                        if sarada_relationship < 25:
                            sara "Why would I want to do that with {i}you{/i}?"
                            "Increase your relationship with Sarada first to unlock this option."
                            pass

                        else:
                            sara "I don't know, [bo_name]... I don't think that's such a good idea yet..."
                            "Increase your relationship with Sarada first to unlock this option."
                            pass

                        if sarada_reintro_room_underwear == True:
                            show sarada underwear_normal at left with dissolve
                        else:
                            show sarada happy at left with dissolve
                        jump sarada_menu_interactrepeatable
                    
                    else:
                        call checkSarada(50) from _call_checkSarada_18
                        sara "Sure, why not! I'd love to spend some time alone with you. ♡"
                        jump sarada_room_hangout

                "Return":
                    jump sarada_menu_repeatable

        "Information":
            show screen saradamenuinfo
            jump sarada_menu_repeatable

        "Leave":
            scene black with dissolve
            bot "I should get going now Sarada, thanks for hanging out!"
            scene black with dissolve
            "You leave the household after having spent some time with Sarada..."
            jump action_taken

label sarada_room_hangout:
    scene v20_sarada_lyingbedroom with dissolve
    call changesarada(3) from _call_changesarada_13
    $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
    "...You and Sarada spend some time in her room, talking about various subjects and enjoying each other's company."
    "Having gotten so close to each other now, you feel comfortable freely holding her and kissing her at every opportunity."
    stop sfx3 fadeout 1
    scene black with dissolve
    "After having your fill of Sarada's affection, you leave to go back home."
    # Potential for adding more scenes here, like plot devices or just cuddling, kissing, etc. or getting caught doing stuff by Sakura.
    jump action_taken
