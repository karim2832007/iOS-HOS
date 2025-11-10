default sarada_sparring_goeasy = False
default sarada_sparring_wincounter = 0
default sarada_sparring_dickoutcounter = 0

label sarada_boruto_sparring:
    "..."
    $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=True, relative_volume = 0.3)
    scene v20_1sarada_forest1 with dissolve
    "You and Sarada tread towards the forest. You can sense a feeling of anticipation emanating from her..."
    sara"You still remember this place, don't you?"
    bo"How could I forget... After all those times I beat your ass!"
    sara"Ha! Don't make me laugh, loser!" with vpunch
    bo"You are still gunning to be Hokage, aren't you?"
    bo"You're going to have to beat me first, you know..."
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/jacketdrop1.opus", channel="sfx3", loop=False, relative_volume = 1.5)
    "Sarada tosses her jacket away, and starts stretching with a serious look on her face..."
    scene v20_1sarada_forest3 with dissolve
    sara"I am about to do just that! You better be taking this seriously..."
    sara"I won't forgive you if you go easy on me!"
    call increaselust(10) from _call_increaselust_275
    bot"She's been keeping in shape!"
    bot"So athletic and flexible, look at that effortless split even with heels on!"
    scene v20_1sarada_forest2 with dissolve
    sara"What are you sitting there staring at me for? \nYou better get your stretching in too..."
    sara"Unless you don't mind me injuring your scrawny little ass!" with vpunch
    scene black with dissolve
    bo"In your dreams...!" with vpunch
    scene v20_1sarada_forest4 with dissolve
    "Sarada takes her fighting stance, her face hardening with resolve and determination, ready to test her skills against yours."
    scene bg forest1 with dissolve
    show sarada fighting:
        xpos 300
    show boruto snob at left
    with dissolve
    if radiostation == 1:
        $ playmusic("audio/ost/reversesituation.opus",0.6)
    elif radiostation == 2:    
        $ playmusic("audio/ost/lightningspeed.opus",0.7)
    elif radiostation == 3:
        $ playmusic("audio/ost/gym_Junkyousha.opus",0.8)
    elif radiostation == 4:
        $ playmusic("audio/ost/nightattack.opus",0.7)
    elif radiostation == 5:
        $ playmusic("audio/ost/kokuten.opus",0.6)
    elif radiostation == 6: 
        $ playmusic("audio/ost/borutotheme.opus",0.5)
    else:
        $ playmusic("audio/ost/reversesituation.opus",0.6)

    bo"Oooh..? Ready to have at it? Just so you know, I hope you can manage to kee-..."
    $ renpy.sound.play("/audio/soun_fx/kunai_throw.opus", channel="sfx3", loop=False, relative_volume = 1.5)
    scene black with flash
    bo"W-what the...!" with vpunch
    "Sarada suddenly and without warning, throws a kunai straight at you, chasing behind it to follow up with another attack!"
    $ renpy.sound.play("/audio/soun_fx/kunai_clash.opus", channel="sfx3", loop=False, relative_volume = 1.2)
    show v20_sarada_spar1 with flash
    bo"T-that could have killed me, you crazy girl!"
    sara "You talk{i} way {/i}too much, [bo_name]!"
    sara "I told you, don't hold back, because I definitely won't!"
    menu:
        bot "Should I let her win?"
        "She's right, I need to give it my all!":
            $ sarada_sparring_goeasy = False
            "You nod, understanding the importance of pushing each other to improve."
            call changesarada(5) from _call_changesarada_2
            bo "If that's the way you wanna play it..."
            bo "You can count on it, Sarada! You're going down!" with vpunch
            pass

        "Maybe I should take it easy on her...":
            $ sarada_sparring_goeasy = True
            bot"Maybe I shouldn't go too hard on her..."
            bot "It must be very demoralizing to lose to me every time!"
            pass

    $ renpy.sound.play("/audio/soun_fx/kunai_clash.opus", channel="sfx3", loop=False, relative_volume = 1.2)
    scene v20_sarada_spar2 with flash
    "You clash furiously between the two of you for what feels like hours, exchanging blows and dodging each other's attacks with skill and precision."

    if sarada_sparring_goeasy == False:
        jump sarada_sparring_win
    else:
        jump sarada_sparring_lose

  


label sarada_sparring_win:
    $ initialize_replay_defaults()
    "You can feel the adrenaline pumping through your veins as you push yourself to your limits, determined to come out on top."
    scene black with flash
    $ renpy.sound.play("/audio/soun_fx/body_drop.opus", channel="sfx3", loop=False, relative_volume = 1)
    "Sarada, although strong and competent, is unable to persevere... Eventually falling to the ground, exhausted and defeated."
    scene v20_sarada_spar_win with dissolve
    bo "Well, well, well... Looks like someone has had enough for one day."
    scene v20_sarada_spar_win_01 with dissolve
    sara "Ugh... I can't believe I lost again..."
    bo "Is it really that surprising? I would have thought you'd be used to it by now!"
    sara "Hmph! Don't get too cocky with me, [bo_name]!"
    bo "Oh, is stating the obvious considered being cocky now?!"
    scene v20_sarada_spar_win_02 with dissolve:
        zoom 1.0 xalign 0.5 yalign 0.5
    "Sarada glares at you, clearly annoyed by your teasing."
    show v20_sarada_spar_win_02:
        subpixel True
        linear 0.3 zoom 1.2 xalign 0.2 yalign 0.7
    "You can see the rage in her eyes, her ego apparently bruised even more than her body."
    bo "You know, you really should consider training with me more often."
    bo "I could give you pointers, and maybe you'll eventually learn a thing or two!"
    show v20_sarada_spar_win_02:
        subpixel True
        linear 0.2 zoom 1 xalign 0.5 yalign 0.5
    sara "Hmph! I don't need your help to get stronger!"
    bo "Oh really? Then why do you keep losing to me?"
    show v20_sarada_spar_win_annoyed with dissolve:
        zoom 1.1 xalign 0.0 yalign 1.0
    sara "Can you just shut up already, and get the hell off me!?" with vpunch
    bo "Hmm... I don't know, I kind of like it here!"
    sara "Very funny..."
    menu sarada_sparring_winfloor_menu:
        "Help her to her feet" if sarada_sparring_wincounter == 0:
            if sarada_sparring_wincounter < 2:
                $ sarada_sparring_wincounter +=1
            bo"I'm just playing with you... Here, let me help you up."
            stop music fadeout 1
            scene black with dissolve
            "You get up and extend your hand out to help her, both of you exhausted but back on your feet."
            $ renpy.sound.play("/audio/soun_fx/forest_ambience.opus",channel="sfx4",loop=True,relative_volume=0.7)
            scene bg forest1
            show boruto snob at right
            show sarada angry at left
            with dissolve
            bo "You fought well today Sarada, and I know you'll come back even stronger next time."
            bo "I don't want you to get too discouraged, I always enjoy our sessions together..."
            show sarada at smallshake
            sara "Hmph... I hate to admit it, but this is actually really productive for me."
            sara "I'm starting to see the huge flaws in my technique thanks to you."
            show sarada shy with dissolve
            sara "And well... I guess I like spending time with you, even if you are a bit of a jerk sometimes!" 
            show boruto embarassed with dissolve
            bo "H-hey, I'm trying my best out here!"
            show boruto sad with dissolve
            bo "But I have to say... I'm really sorry for not being around as much lately."
            bo "I was just... preoccupied with other things, I guess."
            call changesarada(3) from _call_changesarada_3
            sara "I've really missed having you around..." 
            show sarada flustered with dissolve
            show sarada at smallshake
            sara "So don't be an idiot, you better not disappear on me again, okay?!"
            sara "Or else I'll have to come kick your butt and drag you back here myself!" with vpunch
            show boruto smirk2 with dissolve
            bo "Haha, I promise I won't!"  
            show boruto snob with dissolve
            bo "Although honestly, if today was any indication of our abilities... I think you might need to step up your game a little bit to be able to kick my butt!" 
            show sarada angry2 with dissolve
            sara "Ugh, you just wait until next time! I'll be ready for you!"
            show boruto smirk2 with dissolve
            bo "Haha come on, let's get you back to your house safely before your mom starts worrying about you..."
            $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.2)
            scene black with dissolve
            "You both brush off the leaves and sweep the dirt off of your clothes, before making your way back home."
            jump action_taken
            
        "{color=[obediencecolor]}Help her to her feet{/color}" if sarada_sparring_wincounter > 0:

            bo"I'm just playing with you... Here, let me help you up."
            stop music fadeout 1
            scene black with dissolve
            "You get up and extend your hand out to help her, both of you exhausted but back on your feet."
            label sarada_sparring_jumpfromfail:
                $ renpy.sound.play("/audio/soun_fx/forest_ambience.opus",channel="sfx4",loop=True,relative_volume=0.7)
                scene bg forest1
                show boruto snob at right
                show sarada shy at left
                with dissolve
                sara "Ughh, today was brutal..."
                show sarada at smallshake
                sara "Everything hurts, it's as if I've been thrown off a fifty foot cliff!"
                show boruto smirk2 with dissolve
                "You can't help but chuckle at her dramatic flair." 
                bo "You really know how to sell it, don't you?"
                show sarada annoyed with dissolve
                sara "Don't laugh at me! I really do feel like I've been through hell and back!" with vpunch
                bo "Oh... Well, if it really is that bad... \nWhy don't you let me help you out a bit?"
                show sarada flustered with dissolve
                sara "H-help me out? What do you mean?"
                show boruto sceeming with dissolve
                bo "Show me where it hurts, I'll see if I can get the blood flowing back there again for you."
                bo "That's what friends are for, right?"
                show boruto snob with dissolve
                bo "I can even kiss it better if you want!"
                show sarada angry2 with dissolve
                sara "W-wha-?!" with vpunch 
                "Sarada blushes slightly, clearly caught off guard by your playful comment."
                show sarada at smallshake
                sara "I-I mean... It's not like I need your help or anything!"
                show sarada shy with dissolve
                sara "It's just a little soreness, around the chest and shoulders..."
                show sarada happy with dissolve
                sara "I'll be fine, but... thanks, I guess."
                jump sarada_sparring_win_menu

                
            jump sarada_sparring_win_menu

        "{color=[obediencecolor]}???{/color}" if sarada_sparring_wincounter < 1:
            "Complete more successful sparring sessions to unlock this option."
            jump sarada_sparring_winfloor_menu


        "{color=[dominancecolor]}???{/color}" if sarada_sparring_wincounter < 2:
            "Complete more successful sparring sessions to unlock this option."
            jump sarada_sparring_winfloor_menu

        "{color=[dominancecolor]}Keep her pinned down!{/color}" if sarada_sparring_wincounter >= 2:
            call checkDominance(15, "sarada_sparring_winfloor_menu") from _call_checkDominance_53 
            "You keep her pinned in place, not letting her move an inch!"
            $ renpy.sound.play("/audio/soun_fx/gruntwoman1.opus", channel="sfx3", loop=False, relative_volume = 1.5)
            "Sarada tries struggling to break free, but you hold her down firmly, enjoying the feeling of power and control over her."
            bo "I'm starting to like the view from up here..."
            bo "Underneath me a poor, helpless little girl... Lying on the ground, defeated and at my mercy!"
            sara "This {i}helplesss little girl{/i} is going to seriously kick your ass if you don't let me go right now!"
            bo "Really? The same one that is so easily overpowered and trapped?"
            bo "What makes you think you're in any position to make demands and threats like that?"
            sara "Alright, we get it tough guy, you're big and strong and have a fragile ego to go with it. Congratulations!"
            sara "Now will you {i}please{/i} get the hell off me?"

            menu:
                "Let her go and help her up...":
                    "Satisfied with her reply, you decide to stop heckling her any more than necessary."
                    bo"I'm just playing with you... Here, let me help you up."
                    stop music fadeout 1
                    scene black with dissolve
                    "You get up and extend your hand out to help her, both of you exhausted but back on your feet."
                    $ renpy.sound.play("/audio/soun_fx/forest_ambience.opus",channel="sfx4",loop=True,relative_volume=0.7)
                    scene bg forest1
                    show boruto snob at right
                    show sarada shy at left
                    with dissolve
                    sara "Ughh, finally... Today really was brutal..."
                    show sarada at smallshake
                    sara "Everything hurts, it's as if I've been thrown off a fifty foot cliff!"
                    show boruto smirk2 with dissolve
                    "You can't help but chuckle at her dramatic flair." 
                    bo "You really know how to sell it, don't you?"
                    show sarada annoyed with dissolve
                    sara "Don't laugh at me! I really do feel like I've been through hell and back!" with vpunch
                    bo "Oh... Well, if it really is that bad... \nWhy don't you let me help you out a bit?"
                    show sarada flustered with dissolve
                    sara "H-help me out? Like how you helped me out on the floor? Yeah, no thanks!"
                    show boruto sceeming with dissolve
                    bo "*chuckle* Oh come on, you big baby..."
                    bo "Show me where it hurts, I'll see if I can get the blood flowing back there again for you."
                    bo "That's what friends are for, right?"
                    show sarada angry2 with dissolve
                    sara "Friends? Who needs enemies when you have friends like you!?"
                    show boruto snob with dissolve
                    bo "I can even kiss it better if you want!"
                    show sarada angry2 with dissolve
                    sara "W-wha-?!" with vpunch 
                    "Sarada blushes slightly, clearly caught off guard by your playful comment."
                    show sarada at smallshake
                    sara "I-I mean... It's not like I need your help or anything!"
                    show sarada shy with dissolve
                    sara "It's just a little soreness, around the chest and shoulders..."
                    show sarada happy with dissolve
                    sara "I'll be fine, but... thanks, I guess."
                    jump sarada_sparring_win_menu

                "{color=[hatredcolor]}Remind this bitch who is REALLY in charge here!{/color}":   
                    call checkHatred(15, "sarada_sparring_winfloor_menu") from _call_checkHatred_37
                    stop music fadeout 0.5
                    $ renpy.sound.play("/audio/soun_fx/bassstart.opus",channel="sfx1",loop=False,relative_volume=0.5)
                    $ renpy.sound.play("/audio/soun_fx/introbass3.opus",channel="sfx2",loop=True,relative_volume=0.7)
                    bo "You know... I'm really starting to dislike your attitude..."
                    bo "You just don't know when to quit..."
                    show v20_sarada_spar_win_hate1 with dissolve
                    bo "You keep pushing, and pushing, and pushing..."
                    bo "And at some point, I might just..."
                    show v20_sarada_spar_win with vpunch
                    $ renpy.sound.play("/audio/soun_fx/himawari/kyaa.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                    bo "{i}...SNAP!!{/i}" with vpunch
                    bo "You need to learn when to shut your fucking mouth, and accept your fate..."
                    scene v20_sarada_spar_win_annoyed with dissolve:
                        zoom 1.1 xalign 0.0 yalign 1.0
                    sara "H-hey... [bo_name] stop that, y-you're scaring me..."
                    show v20_sarada_spar_win with vpunch
                    bo "Good!" with vpunch
                    bo "You're scared for good reason, and you're finally realizing who really holds all the power here..."
                    scene v20_sarada_spar_win_annoyed with dissolve:
                        zoom 1.1 xalign 0.0 yalign 1.0
                    sara "L-listen, you d-don't have to be mean about it... I'm sorry, okay?"
                    sara "There, I even apologized... W-what more do you want from me?!"
                    show v20_sarada_spar_win_hate1 with dissolve 
                    bo "I can think of a few things I want from you, Sarada..."
                    bo "Ways to put you in your place, to break the spirit of the little brat that you've let yourself become!"
                    show v20_sarada_spar_win_hate1_1 with dissolve 
                    bo "I see the anger in your eyes, but I also smell the fear creeping up on you..."
                    scene v20_sarada_spar_win_annoyed with dissolve
                    bo "Are you afraid of me, Sarada?"
                    bo "Because you probably should be!" with vpunch
                    scene black with dissolve
                    sara "You bastard!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/gruntwoman2.opus", channel="sfx3", loop=False, relative_volume = 1)
                    "Sarada gasps and gives one final struggle with all her remaining strength!"
                    $ renpy.sound.play("/audio/soun_fx/body_drop.opus", channel="sfx3", loop=False, relative_volume = 1)
                    "She takes advantage of your shift of position, to change your center of gravity and shove you off of her, sending you tumbling to the ground!"
                    $ renpy.sound.play("/audio/soun_fx/woosh2.opus", channel="sfx3", loop=False, relative_volume = 0.4)
                    scene v20_sarada_spar3var with vpunch
                    "She swiftly climbs on top of you, pulling out a hidden kunai that is now poised directly at your throat!"
                    show v20_sarada_spar3var with dissolve:
                        zoom 1.1 xalign 0.0 yalign 1.0
                    "A furious, yet clearly upset look covers her face, as tears begin streaming down her eyes."
                    sara "*sob* I don't know what's gotten into you today, [bo_name]!"
                    sara "But this isn't funny anymore!" with vpunch
                    bo "Sarada, wait...!"
                    sara "S-shut the hell up! You've gone too far this time!"
                    sara "T-this isn't like you at all, but I refuse to hear any excuses!"
                    sara "I'm going home, s-so j-just..."
                    sara "Stay the hell away from me, okay?!" with vpunch
                    stop sfx1 fadeout 1.0
                    stop sfx2 fadeout 1
                    $ renpy.sound.play("/audio/soun_fx/forest_ambience.opus",channel="sfx4",loop=True,relative_volume=0.7)
                    scene black with dissolve
                    "She wipes her eyes as she gets up to leave, clearly upset and angry at your behavior."
                    show v20_1sarada_forest1_angry with dissolve
                    "You see her shoot you one last death stare as she walks away, leaving you there alone in the forest."
                    bot "Sarada..."
                    scene black with dissolve
                    bot "Well, I don't think that went as planned..."
                    bot "But at least she'll think twice now before trying to push me around again! Hehe..."
                    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    "You sit there for a moment, contemplating what exactly just happened, before getting up and brushing yourself off to leave."
                    bot "I'm sure she'll get over it... \nShe's just being sensitive, I didn't even do anything to her..."
                    bot "Time to head back home for now..."
                    jump action_taken


            jump sarada_sparring_win_menu


    menu sarada_sparring_win_menu:
        "{color=[obediencecolor]}Insist on 'helping' her{/color}":
            show boruto embarassed with dissolve
            bo "Come on, Sarada... I know you're tough, but you don't have to pretend to be invincible all the time!"
            show boruto sceeming with dissolve
            bo "Let me take care of you for once, maybe I can help you feel a bit better..."
            show sarada angry2 with dissolve
            sara "Since when did you become so caring?!" with vpunch
            show boruto sceeming2 with dissolve
            bo "I guess since I started spending more time with you again, I've realized that I need to make up for lost time."
            show sarada at smallshake
            sara "Hmmph... \nYeah, I'm sure you're doing this out of the kindness of your heart!"
            show sarada flustered with dissolve
            sara "B-but... I guess it wouldn't hurt to get a little help."
            show sarada shy with dissolve
            sara "I just hope you know what you're doing..."
            show boruto sceeming with dissolve
            bo "Don't worry, I know {i}exactly{/i} what I'm doing!"
            bo "Come here..."

            label sarada_sparring_win_grope:
                $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 1)
                scene v20_sarada_titsclothed_1_1_1 with fade
                "You gently place your hands on Sarada's body, feeling the warmth of her skin pressed up against yours."
                bo "Oh yeah, I can definitely feel the tension in your muscles."
                $ renpy.sound.play("audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
                "You start to massage her chest and breasts, working out the knots and tension that the sparring had caused."
                sara "H-hey... Watch where you're putting your hands, [bo_name]!"
                sara "That's not what I meant by helping me out!" with vpunch
                bo "It's okay, Sarada! I know what I'm doing, remember!?"
                bo "Just close your eyes and relax a little bit. Let me take care of you..."
                scene v20_sarada_titsclothed_1_1_1_closedeyes with dissolve 
                "With no energy left to argue anymore, Sarada complies and lets you continue."
                sara "I g-guess it does feel kinda nice..."
                "Sarada lets out a soft moan, clearly enjoying the sensation of your hands on her body, and your breath down the back of her neck."
                if sarada_relationship < 25:
                    sara "[bo_name_stutter]... A-are you sure this is okay?"
                    bo "Of course it is, Sarada. I just want to help you feel better, trust me."
                else:
                    sara "[bo_name_stutter]... A-are you sure you know what you're doing?"
                    bo "Of course, Sarada. I just want to help you feel better, trust me."
                call changesarada(2) from _call_changesarada_4
                sara "O-okay... I trust you!"
                bot "She might not have Auntie Sakura's big boobs, but she still has a nice pair of perky breasts that fit perfectly in my hands."
                bot "I wonder if she even realizes how much she's enjoying this, or if she's just too shy to admit it."
                bot "Either way, I can tell that she's starting to let go and lower her inhibitions."
                bot "Should I take it a step further and see how far I can push her boundaries?"
                menu sarada_sparring_win_grope_menu:
                    "Keep massaging her breasts": 
                        if sarada_sparring_wincounter < 3:
                            $ sarada_sparring_wincounter +=1
                        "You continue to massage her breasts, feeling the softness of her skin and the firmness of her nipples."
                        "Sarada continues to moan as the sensation overwhelms her."
                        sara "Mmm... That feels really good actually, [bo_name]...♡"
                        bo "I'm glad you like it, Sarada. I think it's something that you really needed..."
                        scene v20_sarada_titsclothed_1_1_3 with dissolve
                        "Sarada leans back into your touch, clearly enjoying the attention you're giving to her body."
                        "You can feel her breathing becoming heavier as you continue to massage her."
                        "Your left hand starts to naturally wander lower, brushing against her stomach and hips."
                        bot "What a nice body she has, so firm and toned from all that training."
                        bot "I wonder if she would stop me if I tried to go further..."                    
                        menu sarada_sparring_win_grope_menu2:
                            "Let your hand wander lower" if sarada_relationship < 25:
                                scene v20_sarada_titsclothed_1_1_3_1 with dissolve
                                "You let your hand wander lower, brushing past her waistline."
                                "Sarada gasps softly, but doesn't immediately pull away." with vpunch
                                sara "W-wait, [bo_name]... I don't know if we should be doing this..."
                                bo "Shh, just relax Sarada. I know you want this as much as I do!"
                                sara "N-no, I mean... Maybe... But it's not right!"
                                sara "I mean, we're just friends, right? We shouldn't be crossing any lines..."
                                bo "Oh... R-right..."
                                "You can see the conflict in her eyes, but you also sense a hint of curiosity and desire."
                                scene black with dissolve
                                bot "I can feel the tension in the air, I must have pushed her a bit too far before she was ready."
                                $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                scene bg forest1
                                show boruto suspicious at right
                                show sarada shy at left
                                with dissolve
                                sara "I-I think we should just start heading back home now, and forget this ever happened..."
                                bo "S-sure... If you say so Sarada..."
                                show boruto embarassed with dissolve
                                bo "Training together was really fun though! Let's do this again sometime though, okay?"
                                show sarada happy with dissolve
                                sara "Yeah, definitely! It's important to keep at it, and I {i}do{/i} look forward to spending some more time with you!"
                                show boruto normal with dissolve
                                bo "Sounds good to me!"
                                bo "Come on, let's get you back to your house safely before your mom starts worrying about you..."
                                $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                scene black with dissolve
                                "You both brush off the leaves and sweep the dirt off of your clothes, before making your way back home."
                                jump action_taken

                            "{color=[obediencecolor]}Let her enjoy your touch{/color}" if sarada_relationship >= 20:
                                scene v20_sarada_titsclothed_1_1_4 with dissolve 
                                "You let your hands explore her body, eventually resting on both of her breasts."
                                "Sarada gasps softly, but doesn't pull away, as you firmly grasp them and gently squeeze her tight chest."
                                sara "O-oh, [bo_name]... You're really good at this..."
                                bo "Shh, just relax Sarada. I know you want this as much as I do!"
                                sara "N-no... Well, maybe..."
                                sara "Honestly, I don't know what I want anymore!" with vpunch
                                sara "But this does feel nice after all that sparring... \nIt's helping to take the edge off."
                                bo "R-right..."
                                scene v20_sarada_titsclothed_1_1_5 with dissolve
                                "You gently grab her by the arm to turn her body around slightly, bringing her face to face with you."
                                $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx3", loop=False, relative_volume = 1)
                                "You give her a soft kiss on the lips, and one last gentle squeeze of her breasts as she moans into your mouth."
                                sara "Mmmm ♡"
                                sara "You always somehow find a way to make me feel better..."
                                bo "I just want to help, and I think I've done quite a good job by the looks of it!"
                                bo "You so seem so calm and relaxed to me right now!"
                                sara "Yeah, this was great... Thank you for today! ♡"
                                scene black with dissolve
                                "You both rest a bit longer, enjoying the peacefulness of the forest around you as time passes by."
                                $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                scene bg forest1 with dissolve
                                show boruto smirk at right
                                show sarada shy at left
                                with dissolve
                                sara "Let's leave it at that for today, it's getting a bit late."
                                show boruto normal with dissolve
                                bo "Yeah I guess we should probably start heading back home now..."
                                show boruto sceeming with dissolve
                                show boruto at smallshake
                                bo "Let's do this again sometime though, okay?"
                                show sarada happy with dissolve
                                sara "Definitely! I look forward to some more training and relaxing with you!"
                                $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                scene black with dissolve
                                "You both brush off the leaves and sweep the dirt off of your clothes, before making your way back home."
                                jump action_taken

                            "{color=[dominancecolor]}Pull her top down!{/color}" if sarada_sparring_wincounter >= 3:
                                call checkDominance(15, "sarada_sparring_win_grope_menu2") from _call_checkDominance_54 
                                scene v20_sarada_gropetits_3_2_3 with dissolve
                                "You pull Sarada's top down, exposing her breasts."
                                sara "H-hey! What are you doing?!"
                                bo "Just enjoying the view, Sarada. You have such beautiful breasts!"
                                sara "I-... I guess so... But you gotta warn me before doing something like that!"
                                bo "Oh sorry, I just couldn't help myself... They're so perfect!"
                                sara "You don't sound sorry at all honestly!" with vpunch
                                sara "B-but... Y-you really like them?"
                                bo "Of course I do! They compliment your figure so nicely..."
                                bo "I just wanted to give them a bit of fresh air and feel them in my hands, skin to skin."
                                bo "You've got such cute little nipples that harden instantly under my touch..."
                                sara "O-oh... You're really into this..."
                                sara "I'm not sure how to feel about you just pulling them out like that though! But I do like how you make them feel...♡"
                                bo " Yeah I can tell... I feel your heart pounding like crazy right now!"
                                scene v20_sarada_gropetits_3_2_3r with dissolve 
                                "Her breath grows shallow and quickens as you continue to caress and grope her."
                                sara "A-ahh... That feels pretty good...♡"
                                bo "Your body betrays you, Sarada. You're really enjoying it!"
                                sara "O-oh shut up! You just want an excuse to keep playing with them..." with vpunch
                                bo "Well, can you blame me? They're so soft and perky!"
                                sara "M-mmm... W-well d-don't stop just yet...I-I need this right now! ♡"
                                bo "I love hearing the sound of you moaning to my touch."
                                bo "It makes me want to do it even more!"
                                bo "Just look at you, all flushed and excited!"
                                sara "Well, it's hard not to be, when I'm all exposed and having my nipples rubbed like that!"
                                sara "I do feel very relaxed though, so I guess it's not all bad...♡"
                                sara "I think you've had enough fun for one day though!" with vpunch
                                sara "It's starting to get late, we should probably head back home soon..."
                                $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                scene bg forest1 with dissolve
                                show boruto worried at right
                                show sarada shy at left
                                with dissolve
                                bo "Aww, just when things were starting to get interesting..."
                                show boruto sceeming with dissolve
                                bo "I guess you're right. But I promise we'll do this again soon!"
                                show sarada happy with dissolve
                                sara "As long as you're not too rough... You won't hear me complaining about it!"
                                sara "Come on, let's get out of here..."
                                $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                scene black with dissolve
                                "You both brush off the leaves and sweep the dirt off of your clothes, slowly making your way back home."
                                jump action_taken

                            "{color=[obediencecolor]}???{/color}" if sarada_relationship < 20:
                                call checkSarada(20) from _call_checkSarada
                                "Increase Sarada's relationship level to unlock this."
                                jump sarada_sparring_win_grope_menu2

                            "{color=[dominancecolor]}???{/color}" if sarada_sparring_wincounter < 3:
                                call randomCheck(False, " ") from _call_randomCheck_5
                                "Complete more successful sparring sessions to unlock this option."
                                jump sarada_sparring_win_grope_menu2


                            "We're just friends, I shouldn't be inappropriate!" if sarada_relationship < 25:
                                scene black with dissolve
                                bot "Ugh, what am I doing, I need to snap out of it before I ruin my relationship with her!"
                                scene bg forest1 
                                show boruto worried at right
                                show sarada shy at left
                                with dissolve
                                bo "I think we should stop here, Sarada. I don't want to make you too uncomfortable."
                                sara "Oh..."
                                "Sarada looks a bit disappointed, but nods in agreement."
                                show sarada happy with dissolve
                                sara "Yeah, okay... I guess you're right, and I do appreciate your concern, [bo_name]."
                                show boruto suspicious with dissolve
                                bo "I just want to make sure we're both on the same page."
                                show boruto normal with dissolve
                                bo "Let's just enjoy the moment and not take it any further."
                                call changesarada(2) from _call_changesarada_5
                                sara "Yeah, I think that's for the best too..."
                                scene black with fade
                                "You both rest a bit longer, enjoying the peacefulness of the forest around you as time passes by."
                                sara "We can start heading back home now I guess... I'm exhausted!"
                                bo "You really went hard today! Let's get you back to your mom before she starts worrying about you."
                                $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                "You both brush off the leaves and sweep the dirt off of your clothes, before making your way back home."
                                jump action_taken

                            "Let her rest today..." if sarada_relationship >= 25:
                                show boruto worried with dissolve
                                bot "Maybe I shouldn't mess with her today, she seems really tired from the training session."
                                show boruto suspicious with dissolve
                                bo "I think we should stop here, Sarada. You look like you could use some rest today."
                                show sarada shy with dissolve
                                sara "Oh..."
                                "Sarada looks a bit disappointed, but nods in agreement."
                                sara "Yeah, okay... I guess you're right, and I do appreciate your concern, [bo_name]."
                                show boruto at smallshake
                                bo "You can count on me, I'll always look out for you!"
                                show boruto normal with dissolve
                                bo "Let's just enjoy the moment and not take it any further."
                                call changesarada(2) from _call_changesarada_6
                                show sarada happy with dissolve
                                sara "Yeah, I like the sound of that too..."
                                scene black with fade
                                "You both rest a bit longer, enjoying the peacefulness of the forest around you as time passes by."
                                sara "We can start heading back home now I guess... I'm exhausted!"
                                bo "You really went hard today! Let's get you back to your mom before she starts worrying about you."
                                $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                "You both brush off the leaves and sweep the dirt off of your clothes, before making your way back home."
                                jump action_taken



                    "{color=[dominancecolor]}Turn her around and kiss her{/color}" if sarada_sparring_wincounter >=2: 
                        call checkDominance(15, "sarada_sparring_win_grope_menu") from _call_checkDominance_55 
                        scene v20_sarada_titsclothed_1_1_5 with dissolve
                        $ sarada_sparring_wincounter +=1
                        "You decide to take a more assertive approach, and start turning Sarada around to face you."
                        $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx3", loop=False, relative_volume = 1)
                        "With one hand still on her breast, and the other with a gentle but firm grip on her arm, you bring her lips right up to yours."
                        sara "W-wait, [bo_name]... What are you doing?!"
                        bo "Shh, just relax Sarada. You're going to enjoy this, I promise..."
                        scene v20_sarada_kissing_1_2_1 with dissolve
                        $ renpy.sound.play("/audio/soun_fx/kiss2.opus", channel="sfx3", loop=False, relative_volume = 1)
                        "You press your lips against hers, sharing a sweet kiss that sends ripples of excitement through Sarada's body."
                        sara "Mmm...♡"
                        bot "She tastes so sweet, like cherries and honey."
                        bot "I could get used to this..."
                        "You can feel her body responding to your touch, going almost limp as she melts into your arms."
                        scene v20_sarada_titsclothed_1_1_4 with dissolve
                        "After a few moments, Sarada pulls back slightly, and turns her head away, blushing deeply."
                        sara "I... I didn't expect that, [bo_name]..."
                        bo "Neither did I, but it felt right in the moment! Didn't it feel good?"
                        if sarada_relationship < 25:
                            sara "Y-yeah, it did... but I don't know if we should be doing this..."
                            sara "I mean, we're just friends, right? We shouldn't be crossing any lines..."
                            bo "O-oh... R-right..."
                            bot "I can feel the tension in the air, I must have pushed her a bit too far before she was ready."
                        else:
                            sara "Y-yeah, it did... It always does with you... ♡"
                            sara "We should do this more often actually, I really enjoy it!"
                            bo "Looks like someone really likes having me around! *smirk*"
                            sara "O-oh shut up, you idiot!"
                            "You both share a playful chuckle at the situation, the mood lightening up a bit."
                            scene black with fade
                            "You both rest a bit longer, enjoying the peacefulness of the forest around you as time passes by."
                            sara "We can start heading back home now I guess... I'm exhausted!"
                            bo "You really went hard today! Let's get you back to your mom before she starts worrying about you."
                            $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                            "You both brush off the leaves and sweep the dirt off of your clothes, before making your way back home."
                            jump action_taken


                    "{color=[obediencecolor]}Passionately make out {/color}" if sarada_relationship >= 25: 
                        call checkSarada(25,"sarada_sparring_win_grope_menu") from _call_checkSarada_1 
                        $ sarada_sparring_wincounter +=1
                        bo "Come here, you..."
                        scene v20_sarada_kissing_1_2_4 with dissolve
                        $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx3", loop=True, relative_volume = 1)
                        "You pull her into a passionate kiss, your lips burning with desire as you press your bodies together."
                        "You swap saliva as your tongues intertwine, exploring each other's mouths with fervor."
                        "Sarada moans softly, her hands gripping your torso tightly as she melts into the kiss."
                        sara "Mmm... [bo_name]...♡"
                        sara "I love it when you kiss me like that..."
                        "You can feel her heart racing against your chest as her tight body presses up against yours, and you can't help but smile at the intensity of the moment."
                        bo "Wow, Sarada... I didn't know you had it in you!"
                        sara "Just shut up and kiss me, dummy!"
                        "Sarada practically pounces onto you as you stabilize yourself against the tree trunk behind you!"
                        bo "Woah, easy there tiger..."
                        scene v20_sarada_kissing_1_2_4_closedeyes with dissolve
                        $ renpy.sound.play("/audio/soun_fx/kiss2.opus", channel="sfx3", loop=True, relative_volume = 1)
                        "You gladly oblige, pulling her even closer as you deepen the kiss, your hands roaming over her body."
                        sara "Mmm..."
                        bo "I could stay like this forever..."
                        call changesarada(5) from _call_changesarada_7
                        sara "Me too...♡"
                        bo "You make me feel so alive, so... desired!"
                        bo "... I can't get enough of you!"
                        sara "You won't have to, you'll always have me by your side! ♡"
                        sara "To hug you, to kiss you, to hold you... To please you!"
                        bo "To p-please me, huh? Well, I might have a few ideas for that in mind actually..."
                        stop sfx3 fadeout 1
                        menu wtfrandommenu1234:
                            
                            "Grab her ass":
                                call checkSarada(25, "wtfrandommenu1234") from _call_checkSarada_2
                                $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                                scene v20_sarada_assclothed_2_1_3 with dissolve
                                "You let your hand slide down and firmly grasp her below the waist, with a big grin on your face."
                                sara "H-hey! What do you think you're doing?!" with vpunch
                                bo "I don't know what you're talking about..."
                                sara "W-what do you mean you don't know? You just grabbed my ass [bo_name]!"
                                bo "Well, can you blame me? It's kind of hard to resist...!"
                                sara "Ugh... you're impossible!"
                                sara "I... I can't believe I'm letting you do this, but..."
                                show v20_sarada_assclothed_2_1_1 with dissolve
                                sara "B-but it feels... kind of nice. \nYour hands feel like they belong on my body!"
                                bo "See? I knew you secretly liked it!"
                                sara "I... I guess so..."
                                sara "[bo_name]... Be honest please... Do you actually like my ass?"
                                bo "Of course I do! It's amazing!"
                                sara "Really? You mean it?"
                                sara "I've always wondered what you thought about my body..."
                                sara "I might not have gotten my mother's curves, but I think I turned out okay, right?"
                                bo "Are you kidding? You're gorgeous just the way you are!"
                                bo "I wouldn't change a thing about you."
                                bo "Especially not your ass!"
                                sara "*giggle* You're so dumb, you know that?"
                                sara "But I appreciate it... That means a lot coming from you...♡"
                                sara "I just... Want to feel wanted, you know?"
                                bo "You {i}are{/i} wanted, Sarada... Let me show you just how much..."
                                $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                                scene v20_sarada_assclothed_2_1_4 with dissolve
                                sara "Oh... [bo_name]...♡"
                                "Sarada playfully keeps her her back arched upwards, allowing her ass to fully be outlined and shaped in her tight shorts"
                                "With one hand stabilizing her from the waist, you caress and grab her ass with the other... Making sure to give it a firm squeeze with every rub."
                                bo "Look at you, all flustered and cute."
                                sara "W-what are you talking about?!"
                                bo "You know exactly what I mean!"
                                sara "I j-just... I like it when you think you're in control."
                                bo "Oh really? Sounds like I'll have to take charge more often then!"
                                sara "*giggle* You could definitely try...♡"
                                bo "Maybe I should take charge of your ass right now..."
                                sara "W-woah! That is not what I meant!" with vpunch
                                menu sarada_sparring_assgrab_randommenu243:
                                    "Gently spank her": 
                                        $ renpy.sound.play("/audio/soun_fx/grope2.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                                        scene v20_sarada_assclothed_2_1_5 with dissolve
                                        "You grasp her ass harder and with more vigor, getting a nice full handfull of her firm cheek."
                                        sara "O-oh... You're really g-getting in there...!"
                                        sara "I guess you weren't lying, you really do seem to enjoy my butt..."
                                        bo "And this is just the beginning!"
                                        sara "Huh-?... What do you m-mea-?!"
                                        $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                                        scene v20_sarada_assclothed_2_1_4_0 with flash:
                                            xzoom -1
                                        sara "H-HEYY!" with vpunch
                                        bo "An ass like this deserves some special attention... Don't you agree?"
                                        sara "Y-yes... It obviously does... But is this really necessary?!"
                                        $ renpy.sound.play("/audio/soun_fx/spank6.opus", channel="sfxstat", loop=False, relative_volume = 0.7)
                                        scene v20_sarada_assclothed_2_1_4_1 with flash:
                                            xzoom -1
                                        sara "AHH! ♡" with vpunch
                                        bo "See? You're starting to get into it!"
                                        sara "S-shut up!"
                                        sarat "Why does this actually feel good?! \nI guess he's not being too rough, I can let him have his fun..."
                                        bo "There's plenty more where that came from..."
                                        $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                        $ renpy.sound.play("/audio/soun_fx/kyaa.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                                        scene v20_sarada_assclothed_2_1_4_2 with flash:
                                            xzoom -1
                                        sara "O-OHH! ♡"
                                        bo "The sounds of your moaning are music to my ears, makes me want to keep doing this all day..."
                                        bo "But let's not spoil you too much though!"
                                        bo "We wouldn't want you getting used to this just yet, now would we?"
                                        sara "H-huh? W-why not?!"
                                        sara "I-I mean... Whatever, yeah... I guess..."
                                        scene v20_sarada_assclothed_2_1_2 with dissolve
                                        bo "Haha, don't worry, we're just saving some for next time too!"
                                        sara "Hmmph, fine!"
                                        sara "H-honestly, it k-kind of e-excites me..."
                                        bot "Hah! I knew she was getting into it!"
                                        bo "Perfect! I'll be looking forward to repeating this again very soon then."
                                        bo "Come though, it's starting to get a little late..."
                                        bo "Let's get you back home before your mom starts worrying about you..."
                                        sara "Ah yeah, she tends to do that a lot."
                                        show v20_1sarada_forest1 with dissolve
                                        $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                        "You both brush off the leaves and sweep the dirt off of your clothes, before making your way back home."
                                        "You can't help but keep staring at Sarada's butt all the way back, the sensation of it on your palms still fresh in your mind."
                                        bot "Oh, Sarada... What am I going to do with you...?"
                                        scene black with dissolve
                                        "..."
                                        jump action_taken

                                    "{color=[dominancecolor]}Pull her shorts down{/color}":
                                        call checkDominance(15, "sarada_sparring_assgrab_randommenu243") from _call_checkDominance_56 
                                        scene v20_sarada_undressass_2_2_2 with dissolve
                                        "Before she can protest, you pull Sarada's shorts down and hike up her top, exposing her firm little butt in her lacy black panties."
                                        sara "[bo_name_stutter]!" with vpunch
                                        $ renpy.sound.play("/audio/soun_fx/grope2.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                                        "You don't miss a beat, and immediately take advantage of the situation, grabbing and squeezing it as much as you please."
                                        bo "Woah, Sarada... You have such a beautiful ass!"
                                        bo "It deserves to be let out to get some fresh forest air..."
                                        bo "Out on display here for my viewing pleasure... Just the way I like it!"
                                        sara "W-what are you doing... I-it's so embarrassing!"
                                        sara "But I can't deny that it feels kinda good doing this with you."
                                        bo "You're loving it, I can tell!"
                                        sara "Enjoy it while it lasts I guess, you're exciting me too much to say no to you right now! ♡"
                                        $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                                        scene v20_sarada_undressass_2_2_1_3 with dissolve
                                        "She bends over further, playfully inviting you for more as she exposes herself while you liberally grope her firm buttcheeks"
                                        bo "How does that feel?"
                                        sara "I-it feels really g-good... ♡"
                                        sara "Your hands feel so stable and strong, no wonder you keep beating me in training!"
                                        sara "To the winner goes the spoils though, right? \nYou get to claim me as your prize now! ♡"
                                        bo "Oh, I intend to... And what a lovely prize it is! The best ass in the village!"
                                        sara "*giggle* I guess I should be more careful around you... You don't seem to have much self-control!"
                                        scene v20_sarada_assclothed_2_1_1 with dissolve
                                        $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                        sara "The show sadly ends though for now... It's getting a little late."
                                        bo "Aww, just when things were starting to get interesting!"
                                        sara "As much as I'm enjoying this, I don't want to keep my mom waiting!"
                                        bo "Yeah, you're probably right... We can continue again next time..."
                                        bo "I had a lot of fun today though, Sarada! Let's get you back home safely now..."
                                        show v20_1sarada_forest1 with dissolve
                                        $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                        "You both brush off the leaves and sweep the dirt off of your clothes, before making your way back home."
                                        "You can't help but keep staring at Sarada's butt all the way back, the sensation of it on your palms still fresh in your mind."
                                        bot "Oh, Sarada... What am I going to do with you...?"
                                        scene black with dissolve
                                        "..."
                                        jump action_taken

                            "Pull away from her":
                                bo "But for now, I think we should take a break and catch our breath."
                                scene v20_sarada_assclothed_2_1_1 with dissolve
                                "You both eventually pull back a little, breathless and smiling at each other."
                                bo "Wow, that was amazing!"
                                sara "Yeah... it really was. ♡"
                                "Sarada blushes deeply, clearly flustered by the kiss."
                                sara "I... I-I really didn't expect that to happen..."
                                bo "Neither did I, but I'm glad that it did!"
                                bo "I know we have a lot to figure out, but I just wanted to show you how I feel."
                                bo "I really care about you, Sarada. More than just a friend!"
                                sara "I care about you too, [bo_name]. More than I ever thought I possibly would..."
                                bo "Let's do this more often, okay?"
                                sara "Definitely! I look forward to our next session!"
                                bo "Looks like someone really likes having me around! *smirk*"
                                sara "O-oh shut up, you idiot!"
                                "You both share a playful chuckle at the situation, the mood lightening up a bit."
                                scene black with fade
                                "You both rest a bit longer, enjoying the peacefulness of the forest around you as time passes by."
                                sara "We can start heading back home now I guess... I'm exhausted!"
                                bo "You really went hard today! Let's get you back to your mom before she starts worrying about you."
                                $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                "You both brush off the leaves and sweep the dirt off of your clothes, before making your way back home."
                                jump action_taken
                            

                    "{color=[obediencecolor]}Pull your cock out! {/color}" if sarada_relationship >= 50 and sarada_sparring_wincounter>=4:
                        call checkSarada(50,"sarada_sparring_win_grope_menu") from _call_checkSarada_3
                        $ renpy.sound.play("/audio/soun_fx/zipper.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                        scene v20_sarada_dickout_3_1_1_lookdown with dissolve
                        sara "Oh my...♡" with vpunch
                        "She stares at your big cock as you whip it out of your unzipped pants, already rock-hard as it rests in your palm."
                        bo "It's a little something, just for you..."
                        sara "I think we both know that there's nothing little about {i}that{/i}!"
                        show v20_sarada_dickout_3_1_1 with dissolve
                        sara "That's probably big enough to completely break me!"
                        bo "Haha, maybe... Can't have any pleasure without a little bit of pain though! Am I right?!"
                        sara "Oh shut up, you dork!"
                        bo "Like I said, I'm just here to help you feel better..."
                        sara "And how exactly is this going to make feel better?!"
                        bo "Sharing is caring! So I'm willing to share a bit of me with you today, because of how much I care!"
                        bo "Doesn't it feel good knowing that you're the one that caused this?"
                        bo "Knowing that right now, it's you I'm thinking of and craving..."
                        sara "B-but how are you even so hard already?!"
                        sara "I didn't even do anything..."
                        menu sarada_sparring_dickout_randommenu314:
                            "Jerk off to her":
                                if sarada_sparring_dickoutcounter ==0:
                                    $ sarada_sparring_dickoutcounter +=1
                                bo "You're doing more than enough, by just being here as your sexy self..."
                                scene v20_sarada_dickout_3_1_r1 with dissolve
                                sara "Oh [bo_name]...!♡"
                                $ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx2", loop=True, relative_volume = 1.0)
                                show v020_sarada_borutomasturbate1 with dissolve
                                "You start to stroke your long shaft while maintaining eye-contact and holding her by the waist..."
                                "You let her drape herself over your shoulders while she steals glances at your cock as you're jerking it, her eyes filled with desire."
                                sara "Have you been perving on me since we started training or what?"
                                sara "Does just looking at me and touching me turn you on so much?"
                                bo "I-it does..."
                                bo "You have no idea just how much!" with vpunch
                                sara "Hmm... If that's true, I want to see you prove it now to me as well!"
                                sara "Show me how much you want me, [bo_name]..."
                                show v020_sarada_borutomasturbate1_1 with dissolve
                                $ renpy.sound.play("/audio/soun_fx/handjob5.opus", channel="sfx2", loop=True, relative_volume = 1.0)
                                "Encouraged by Sarada's words, you start to speed up and let your desire take over." 
                                bo "S-sure, I can d-do that..."
                                sara "I wanna see what it looks like when you cum while thinking of me! ♡"
                                bo "A-ahhhh... F-fu-u..." with vpunch
                                sara "Looks like the pressure is starting to build up..."
                                sara "This is so hot! ♡"
                                bo "A-ahhh... S-Sar-... S-Sarada, I'm getting close!"
                                bo "I can't hold back any longer!" with vpunch 
                                $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                show v20_sarada_dickout_3_1_r3 with longerflash
                                "You finally reach your limit and blow your load, filling the air with your release and splashing some on Sarada's outfit."
                                sara "Oh wow! ♡"
                                sara "That's a lot of sticky cum...!"
                                show v20_sarada_dickout_3_1_r4 with dissolve
                                "You let out a satisfied sigh as you finish, feeling the tension in your body release."
                                show v20_sarada_dickout_3_1_r5 with dissolve
                                sara "*giggle* Oh my... How did that feel?"
                                bo "Aghh... I-it wa-... T-that was good..."
                                show v20_sarada_dickout_3_1_r6 with dissolve
                                sara "I love it [bo_name], thank you for sharing it with me! ♡"
                                bo "Don't thank me yet, I didn't do anything... Not this time, at least..." 
                                bo "Thanks for your help though, I feel so alive right now!"
                                bo "Next time, I want you to be the one to make me cum though!"
                                sara "M-mmm... Sounds like fun, count me in!"
                                "You share a laugh, feeling satisfied and content after the intimate moment."
                                scene black with fade
                                "You both rest a bit longer, enjoying the peacefulness of the forest around you as time passes by."
                                sara "We can start heading back home now I guess... I'm exhausted!"
                                bo "Yeah you really went hard today! Let's get you back to your mom before she starts worrying about you."
                                sara "*giggle* I'm not the only one that went {i}really hard{/i} today though, was I?"
                                bo "Heh, I guess not..."
                                $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                "You both brush off the leaves and sweep the dirt off of your clothes, before making your way back home."
                                jump action_taken

                            "Make her jerk you off" if sarada_sparring_dickoutcounter >=1:
                                if sarada_sparring_dickoutcounter ==1:
                                    $ sarada_sparring_dickoutcounter +=1
                                bo "You're about to though!"
                                bo "I think you should be the one to take care of me this time, Sarada."
                                sara "O-oh? And how do you want me to do that?"
                                bo "I want you to jerk me off, right here, right now!"
                                sara "You're so bossy today... I kinda like it ♡"
                                scene v20_sarada_dickout_3_1_5 with dissolve
                                sara "I-I'm a bit n-nervous though [bo_name], even though I'm really into it!"
                                bo "Just like that, Sarada, no need to stress out... Now give it a nice, firm grip and stroke it slowly."
                                $ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx2", loop=True, relative_volume = 1.0)
                                show v020_sarada_borutomasturbate2 with dissolve
                                sara "L-like that? H-how does that feel? Am I doing it right?"
                                bo "Mmm... It feels amazing, Sarada. You're doing great, keep going!"
                                bo "Ahhh..."
                                "You continue to moan softly as Sarada strokes your cock, her hand moving up and down your shaft with a steady rhythm."
                                "She looks at you intensely with desire, as her mind is clouded with lust and arousal."
                                bo "A-ahhhh... F-fuck I'm getting close...!"
                                sara "S-so much pressure built up in this big cock already..."
                                sara "Pulsing and ready to burst!" with vpunch
                                bo "Y-yeah... I need to let it out!"
                                sara "Do it [bo_name], cum for me! I want to feel it shoot out while I'm holding it!"
                                sara "Let it all out!" with vpunch
                                $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                show v20_sarada_dickout_3_1_5_1cum with longerflash
                                bo "F-FUUUCK!" with vpunch
                                "You reach your limit and blow your load, filling the air with your release and splashing some on Sarada's outfit."
                                bo "Aghh... Yes... So good..."
                                sara "Oh wow! ♡"
                                sara "That's a lot of sticky cum...!" with vpunch
                                scene black with dissolve
                                "You let out a satisfied sigh as you finish oozing, feeling all the tension in your body release as you clean yourselves up a little."
                                $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                scene bg forest1
                                show boruto snob at right
                                show sarada happy at left
                                with dissolve
                                sara "*giggle* How did that feel?"
                                show boruto at smallshake
                                bo "It was... magical!"
                                show boruto embarassed with dissolve
                                bo "Sorry if I got a lot of it on you, there was just no holding it back..."
                                show sarada flustered with dissolve
                                sara "Well I would have preferred if you didn't get it all over my clothes..."
                                show sarada shy with dissolve
                                sara "But that's alright, this was so exciting!"
                                show sarada at smallshake
                                sara "Thank you for sharing it with me! ♡"
                                show boruto sceeming with dissolve
                                bo "Don't thank me yet, I didn't do anything... Not this time, at least..."
                                show boruto normal with dissolve
                                bo "Thanks for your help though, I feel so alive right now!"
                                bo "All thanks to you! ♡"
                                show sarada happy with dissolve
                                sara "*giggle* It was so much fun, I can't wait to do more!"
                                "You both share a laugh, feeling satisfied and content after the intimate moment."
                                bo "For now though, I think we should start heading back home."
                                show sarada sad with dissolve
                                sara "Yeah it's probably for the best... It's starting to get a bit late!"
                                scene black with dissolve
                                $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                "You both brush off the leaves and sweep the dirt off of your clothes, slowly making your way back home."
                                jump action_taken

                            "{color=[dominancecolor]}Grab her by the pussy!{/color}" if sarada_sparring_dickoutcounter >=2:
                                call checkDominance(15, "sarada_sparring_dickout_randommenu314") from _call_checkDominance_57
                                bo "It's not about what you do, it's about the cravings and emotions that you give me each time you're with me!"
                                bo "Don't you feel it too, Sarada? That little tingling down there whenever you think of me?"
                                sara "T-tingling?"
                                bo "Yeah somewhere riiight..."
                                scene v20_sarada_pussyrub_3_3_1 with vpunch 
                                $ renpy.sound.play("/audio/soun_fx/himawari/kyaa.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                bo "Here...!"
                                sara "*gasp* H-hey!"
                                bo "Do you feel it now, Sarada?"
                                bo "That little itch that you just can't seem to scratch on your own..."
                                sara "A-ah... W-well... I don't know, all I feel is your hand...?"
                                sara "B-but... It does tingle a little, it's nice! ♡"
                                bo "Remember, sharing is caring, Sarada... \nAnd I think it's your turn to share a bit of yourself with me!"
                                bo "I know you want to..."
                                sara "I-I g-guess...?"
                                bo "Good girl... Just let it all happen, I'll take good care of you!"
                                sara "O-oh... Okay [bo_name]... I trust you! ♡"
                                sara "I have to admit... Your h-hand is so gentle and soft, and... well..."
                                sara "It's making me so wet! ♡" with vpunch
                                bo "I can feel it, Sarada. You're soaking those panties and shorts for me already!"

                                menu sarada_sparring_dickout_randommenu222:
                                    "Focus on her pleasure":
                                        if sarada_sparring_dickoutcounter ==2:
                                            $ sarada_sparring_dickoutcounter +=1
                                        scene v020_sarada_fingeringspar2 with dissolve
                                        $ renpy.sound.play("/audio/soun_fx/femalemastmoan1.opus", channel="sfx2", loop=True, relative_volume = 1.4)
                                        sara "Ahhh... [bo_name]...♡"
                                        sara "This is so intense!" with vpunch
                                        bo "Is it getting to you already, Sarada?"
                                        sara "Y-yeess... I can't help it!"
                                        sara "I-it's just t-too much for me to handle!"
                                        sara "H-hitting all the right spots... ♡"
                                        bo "Good that's exactly what I want, you enjoying yourself here with me!"
                                        $ renpy.sound.play("/audio/soun_fx/femalemast3.opus", channel="sfx2", loop=True, relative_volume = 1.8)
                                        $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx3", loop=False, relative_volume = 1.4)
                                        "You continue to rub her pussy through her panties, feeling her body tremble with pleasure as she loses control!"
                                        sara "[bo_name_stutter]...! I can't... w-wait! WAIT!"
                                        show v20_sarada_pussyrub_3_3_4_2 with flash
                                        $ renpy.sound.play("/audio/soun_fx/cum0.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                        $ renpy.sound.play("/audio/soun_fx/femaleorgasm.opus", channel="sfx3", loop=False, relative_volume = 1)
                                        sara "AAAHHHH! ♡♡" with vpunch
                                        $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                        bo "Fuck yeah... that's it!"
                                        $ renpy.sound.play("/audio/soun_fx/bodythud.opus", channel="sfx1", loop=False, relative_volume = 1.0)
                                        scene black with vpunch
                                        "*Body Thuds*" with vpunch
                                        scene v20_sarada_pussyrub_3_3_4_3 with dissolve
                                        bo "Oops! Did I go too hard?"
                                        sara "F-fuuuu... M-my legs..."
                                        sara "N-not w-working anymore..."
                                        sara "*gasp* U-ugh... I think I've made a mess..."
                                        bo "Oh wow... You're shaking all over! You alright down there?"
                                        sara "Y-yeah... I just n-need a second..."
                                        "Sarada takes a moment to catch her breath, her body still trembling from the intense orgasm."
                                        "Disoriented, she tries desperately to regain her composure as she sits on the ground, hand between her legs as if to protect herself from any further physical stimulation."
                                        scene black with dissolve
                                        bot "Damn, she really went all out!"
                                        bot "Must be the sparring fatigue combined with a lot of pent up sexual frustration..."
                                        bot "That was so hot to watch though, I still can't believe she came so hard!"
                                        $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                        "Sarada finally manages to stumble back to her feet after a while."
                                        scene bg forest1 with dissolve
                                        show boruto snob at right
                                        show sarada shy at left
                                        with dissolve
                                        sara "O-okay, I'm all back now!"
                                        sara "Sorry about that... I-it just felt so good..."
                                        show sarada flustered with dissolve
                                        sara "It's so embarrassing... B-but..."
                                        show sarada at smallshake
                                        sara"I couldn't help myself!"
                                        show boruto smirk2 with dissolve
                                        bo "Don't worry, Sarada. That was honestly just really impressive..."
                                        bo "You completely lost all control, and had me worried there for a second!"
                                        show sarada happy with dissolve
                                        sara "I-I'm fine! Just a little overwhelmed, that's all..."
                                        show sarada at smallshake
                                        sara "What a perfect ending that was to such a perfect day! ♡"
                                        sara "*giggle* It was so much fun, I can't wait to do more!"
                                        scene black with dissolve
                                        "You both share a laugh, feeling satisfied and content after the intimate moment."
                                        sara "I think it's a good time to start heading back home now."
                                        bo "Yeah, it's getting a bit late..."
                                        bo "Come on, let's get you back to your house safely before your mom starts worrying about you!"
                                        scene black with dissolve
                                        $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=True, relative_volume = 0.3)
                                        "You both brush off the leaves and sweep the dirt off of your clothes, before making your way back home."
                                        jump action_taken

                                    "{color=[dominancecolor]}Pleasure each other together!{/color}" if sarada_sparring_dickoutcounter >=3:
                                        call checkDominance(30,"sarada_sparring_dickout_randommenu222") from _call_checkDominance_58
                                        bo "I want us to share this moment together!"
                                        scene black with dissolve
                                        $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 1)
                                        bo "Let's first get you more comfortable too, shall we?"
                                        show screen parallax1280("v20_sarada_pussyrubtogether", 1.0, initial_ypos=0.0) with dissolve 
                                        call showscrollingimage from _call_showscrollingimage_217
                                        sara "Oh [bo_name]... ♡"
                                        "Sarada seemingly enters a trance of lust and desire, as her hand instinctively grabs your cock without a thought of hesitation."
                                        hide screen parallax1280
                                        show screen parallax1280("v20_sarada_pussyrubtogether2", 1.0, initial_ypos=1.0) with dissolve
                                        "Without the constraints of her shorts, you're now free to shove your hand inside her panties and explore the dripping wet pussy inside!"
                                        sara"W-wait!" with vpunch
                                        show screen parallax1280("v20_sarada_pussyrubtogether2", 1.0, initial_ypos=1.0) with dissolve
                                        bo "Fuck Sarada... It's a waterfall down here!"
                                        sara "I-is that bad?!"
                                        bo "Not at all... It's just making me so horny and hard!"
                                        bo "All these juices running down my fingers and on to your thighs..."
                                        bo "I might have to get down there and give them a taste once I'm done with you!"
                                        sara "H-hey! Don't be so nasty...!"
                                        hide screen parallax1280
                                        show screen parallax1280("v020_sarada_fingeringspar1", 1.0, initial_ypos=1.0) with dissolve
                                        sara "It feels really nice though, your fingers are rubbing all the right spots! ♡"
                                        bo "Do you like how they stimulate your little clitoris like that?" 
                                        sara "Y-yeah... ♡"
                                        sara "It's so much better when you do it! I've never been able to make it feel like this before..."
                                        bo "Heh-... Wait till you see how it feels with me inside you..."
                                        sara "I-inside?!" with vpunch
                                        sara "I hope you're still talking about your fingers, don't be getting any ideas now!"
                                        bo "*smirks* Too late for that now, I've already had the ideas for so long...!"
                                        sara "H-huh?!" with vpunch
                                        bo "Haha... Don't worry about that now, just relax and enjoy my fingers today..."
                                        sara "Okay... If you say so, [bo_name]... ♡"
                                        "You both continue to pleasure each other, your hands moving in sync as you explore each other's bodies together."
                                        "You can feel Sarada's body trembling with pleasure as she loses herself in the moment, her breathing becoming more and more erratic."
                                        bot "She's completely surrending herself to me, I can feel it!"
                                        bot "I'm tempted to just take her right here and now, but I can't push her too far just yet..."
                                        "You feel her body tense up as she builds up to her climax, her moans becoming louder and more desperate."
                                        bo "I can feel you getting closer, Sarada... Are you ready to cum together?"
                                        sara "Y-yes... I can't hold it back any longer!"
                                        sara "Cum with me! I want it! ♡"
                                        "Her desperate pleas for release and the trembling of her wet pussy are enough to send you over the edge!"
                                        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                        hide screen parallax1280
                                        show screen parallax1280("v20_sarada_pussyrubtogether3", 1.0, initial_ypos=1.0) with longerflash
                                        "You reach your limit and blow your load, filling the air with your cum and splashing some on Sarada's outfit as she squirts all over your hand."
                                        sara "AAAHHHH! ♡♡" with vpunch
                                        bo "Aghh... Fuck yes... That was good..."
                                        "Sarada gasps for air, trying to regain control and find the words to speak again."
                                        sara "T-that... That w-was incredible...♡"
                                        bo "So I take it that I'm not the only one that enjoyed that? *smirk*"
                                        sara "Definitely not! *giggle*"
                                        scene black
                                        call hidescrollingimage("Click twice to clean up and get dressed.") from _call_hidescrollingimage_181
                                        $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                        "You both take a moment to gather yourselves..."
                                        scene bg forest1
                                        show sarada shy at left
                                        show boruto laughing at right
                                        with dissolve
                                        sara "Thank you for such a lovely experience [bo_name]..."
                                        sara "I never thought I would be able to feel like this with you..."
                                        show sarada flustered with dissolve
                                        sara "And to think, only weeks ago even just the thought of you would make my blood boil!"
                                        show boruto embarassed with dissolve
                                        bo "Haha, well I guess we've both changed a lot since then!"
                                        show sarada shy with dissolve
                                        sara "Yeah, I guess we have... For the better though!"
                                        sara "I really like this new side of you! *giggle*"
                                        bo "Heh-... I like it too, Sarada. I like it a lot! *smirk*"
                                        "You both share a laugh, feeling satisfied and content after today's intimacy."
                                        show sarada happy with dissolve
                                        sara "Alright Casanova, I think it's time for us to start heading back home now."
                                        bo "Yeah it's probably for the best... It's starting to get a bit late!"
                                        scene black with dissolve
                                        $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=True, relative_volume = 0.3)
                                        "After cleaning yourselves up, you both brush off the leaves and sweep the dirt off of your clothes, slowly making your way back home."
                                        jump action_taken

                                    "{color=[obediencecolor]}???{/color}" if sarada_sparring_dickoutcounter <3:
                                        play sound("/audio/soun_fx/attributeslost.opus")
                                        "Make Sarada more comfortable by reaching this point more often."
                                        jump sarada_sparring_dickout_randommenu222



                            "{color=[obediencecolor]}???{/color}" if sarada_sparring_dickoutcounter <1:
                                play sound("/audio/soun_fx/attributeslost.opus")
                                "Make Sarada more comfortable by reaching this point more often."
                                jump sarada_sparring_dickout_randommenu314
                            "{color=[obediencecolor]}???{/color}" if sarada_sparring_dickoutcounter <2:
                                play sound("/audio/soun_fx/attributeslost.opus")
                                "Make Sarada more comfortable by reaching this point more often."
                                jump sarada_sparring_dickout_randommenu314


                    "{color=[dominancecolor]}???{/color}" if sarada_sparring_wincounter <2:
                        play sound("/audio/soun_fx/attributeslost.opus")
                        "Successfully complete more sparring sessions to unlock this option."
                        jump sarada_sparring_win_grope_menu

                    "{color=[obediencecolor]}???{/color}" if sarada_relationship <25:
                        call checkSarada(25) from _call_checkSarada_4
                        "Increase your relationship with Sarada first to unlock this option."
                        jump sarada_sparring_win_grope_menu

                    "{color=[obediencecolor]}???{/color}" if sarada_relationship <50 or sarada_sparring_wincounter <=3:
                        call checkSarada(50) from _call_checkSarada_5
                        "Increase your relationship with Sarada and complete previous options first to unlock this option."
                        jump sarada_sparring_win_grope_menu

        "We're just friends, I shouldn't be inappropriate!" if sarada_relationship < 25: 
            show boruto worried with dissolve
            bot "Maybe we're crossing a line here that we shouldn't, I should probably stop before things get too heated."
            bo "I think we should stop here, Sarada. I don't want to make you too uncomfortable."
            show sarada shy with dissolve
            sara "Oh..."
            "Sarada looks a bit disappointed, but nods in agreement."
            show sarada happy with dissolve
            sara "Yeah, okay... I guess you're right, and I do appreciate your concern, [bo_name]."
            show boruto suspicious with dissolve
            bo "I just want to make sure we're both on the same page."
            show boruto normal with dissolve
            bo "Let's just enjoy the moment and not take it any further."
            call changesarada(2) from _call_changesarada_8
            sara "Yeah, I think that's for the best too..."
            scene black with fade
            "You both rest a bit longer, enjoying the peacefulness of the forest around you as time passes by."
            sara "We can start heading back home now I guess... I'm exhausted!"
            bo "You really went hard today! Let's get you back to your mom before she starts worrying about you."
            $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.3)
            "You both brush off the leaves and sweep the dirt off of your clothes, before making your way back home."
            jump action_taken

        "Let her rest this time..." if sarada_relationship >= 25:
            show boruto worried with dissolve
            bot "Maybe I shouldn't mess with her today, she seems really tired from the training session."
            show boruto suspicious with dissolve
            bo "I think we should stop here, Sarada. You look like you could use some rest today."
            show sarada shy with dissolve
            sara "Oh..."
            "Sarada looks a bit disappointed, but nods in agreement."
            sara "Yeah, okay... I guess you're right, and I do appreciate your concern, [bo_name]."
            show boruto at smallshake
            bo "You can count on me, I'll always look out for you!"
            show boruto normal with dissolve
            bo "Let's just enjoy the moment and not take it any further."
            call changesarada(2) from _call_changesarada_9
            show sarada happy with dissolve
            sara "Yeah, I like the sound of that too..."
            scene black with fade
            "You both rest a bit longer, enjoying the peacefulness of the forest around you as time passes by."
            sara "We can start heading back home now I guess... I'm exhausted!"
            bo "You really went hard today! Let's get you back to your mom before she starts worrying about you."
            $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.3)
            "You both brush off the leaves and sweep the dirt off of your clothes, before making your way back home."
            jump action_taken

label sarada_sparring_lose:
    $ initialize_replay_defaults()
    "You can feel the adrenaline pumping through your veins as you push Sarada up to her limits, pulling back a little when you feel fatigue creeping up on her."
    $ renpy.sound.play("/audio/soun_fx/woosh3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    scene black with flash
    "Eventually, you start to slow down and let her get the better of you, doing your best not to make it too obvious..."
    $ renpy.sound.play("/audio/soun_fx/body_drop.opus", channel="sfx3", loop=False, relative_volume = 1)
    scene v20_sarada_spar3 with flash:
        zoom 1.1 xalign 0.7
    show v20_sarada_spar3:
        subpixel True
        linear 4 zoom 1 xalign 0.5
    sara "Ha!" 
    sara "How does it feel to be on the losing end for once?"
    show v20_sarada_spar3_1 with dissolve
    bo "Ugh... You just got lucky, Sarada!"
    bo "Next time, I won't underestimate you as much!"
    sara "Oh, I don't know about that... I think you're just no match for me!"
    sara "Face it, you're just not as strong as I am!"
    bo "H-hey, that's not true!" with vpunch
    sara "Oh really? Then why are you lying on the ground groaning helplessly, and I'm not?"
    scene v20_sarada_spar3 with dissolve
    bo "I, uhh... I just need a moment to catch my breath, that's all!"
    "Sarada smirks, clearly enjoying her victory over you."
    scene v20_sarada_spar5 with dissolve
    "She leans down, placing her hands around your neck and looking you in the eyes."
    sara "You know, [bo_name]... I think it's about time you finally took me seriously!"
    "You can feel her warm breath on your face, and you can't help smiling back up at her as she proceeds to gloat in your face."
    bo "Take you seriously? I {i}seriously{/i} think you're delusional!"
    sara "You are so full of yourself!" with vpunch
    sara "Sounds like you've got your head all up in the clouds, I need to bring you back down to earth..."
    bo "You?! Hahaha! Don't make me laugh..."
    bo "If I were you, I wouldn't get too cocky, Sarada... \nI'll be back to challenge you for a rematch soon enough, and you won't like how it ends!"
    sara "Oh, I look forward to it! I'd love to see you try even harder only to end up on the ground yet again! *giggle*"
    bo "Hah, we'll see about that! The ground ain't so bad you know... It's actually quite comfortable down here!"
    menu sarada_sparring_floor_randommenu837516:
        "Push her off of you to leave":
            stop music fadeout 1
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/forest_ambience.opus",channel="sfx4",loop=True,relative_volume=0.7)
            "You use your remaining energy to push Sarada off you, getting back up to your feet."
            scene bg forest1
            show boruto embarassed at right
            show sarada happy at left
            with dissolve
            bo "Alright, alright, you win this time. But next time, I'll be ready for you!"
            sara "*smirk* I look forward to it! I'll have you eating dirt again in no time!"
            show boruto smirk at right with dissolve
            bo "Yeah, yeah... You're so very gracious in victory, I see."
            sara "Of course! Always! Where's the fun in winning if you can't gloat a little!"
            bo "Come on, wipe that goofy smile off your face and let's head back home."
            scene black with dissolve
            "You both brush off the leaves and sweep the dirt off of your clothes, before making your way back home."
            jump action_taken
        
        "{color=[dominancecolor]}Grab her ass!{/color}":
            call checkDominance(15, "sarada_sparring_floor_randommenu837516") from _call_checkDominance_59
            stop music fadeout 1
            scene v20_sarada_spar6 with dissolve
            $ renpy.sound.play("/audio/soun_fx/forest_ambience.opus",channel="sfx4",loop=True,relative_volume=0.7)
            $ renpy.sound.play("/audio/soun_fx/grope2.opus", channel="sfx3", loop=False, relative_volume = 1)
            "You let your hand slide up and firmly grasp her below the waist, with a big grin on your face."
            show v20_sarada_spar6_annoyed with dissolve:
                zoom 1.05 xalign 1.0 yalign 0.0
            sara "H-hey! What do you think you're doing?!" with vpunch
            bo "I don't know what you're talking about..."
            sara "W-what do you mean you don't know?! \nDon't play dumb, you just grabbed my ass idiot!"
            bo "I-... I'm just holding onto you, keeping you safe and making sure you don't fall off and hurt yourself."
            if sarada_relationship < 25 or sarada_sparring_wincounter == 0:
                if sarada_relationship < 25:
                    call checkSarada(25) from _call_checkSarada_6
                else:
                    call randomCheck(False, "Sarada is not comfortable with this...") from _call_randomCheck_6
                sara "Get your dirty hands off me, pervert!" with vpunch
                sara "We're just friends, you can't do that kind of stuff!"
                bo "Oh-... R-right... Sorry..."
                scene black with fade
                bot "I can feel the tension in the air, I must have pushed her a bit too far before she was ready."
                scene bg forest1
                show sarada snob at left
                show boruto embarassed at right
                with dissolve
                sara "I think we should start heading back home now..."
                bo "Yeah, you're probably right... Let's do this again sometime though, okay?"
                sara "Only if you're able to keep your hands to yourself next time... \nI look forward to beating your ass again soon though!"
                scene black with dissolve
                $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=True, relative_volume = 0.3)
                "You both brush off the leaves and sweep the dirt off of your clothes, before making your way back home."
                jump action_taken
            else:
                call checkSarada(25) from _call_checkSarada_7
                sara "I really don't think losers should be getting rewarded, [bo_name]..."
                bo "I didn't lose, my victory was just... Uhm, temporarily delayed!"
                bo "Besides, I think I deserve a little something for all my hard work today!"
                sara "And you've decided that your reward will be my {i}ass{/i}?"
                sara "Who died and put you in charge of my body?!" with vpunch
                bo "Well, seeing as how you haven't asked me to stop yet..."
                bo "I think that gives me the green light to keep going!"
                sara "I will admit, despite it being quite cheeky... This does feel kind of nice and I'm a little tempted to see where this goes..."
                bo "See? I knew you would come around..."
                scene black with dissolve
                sara "Come on, loser... Get your butt off the ground..."
                sara "I just want to make one thing clear!"
                sara "You are{i} NOT {/i}the one in charge here!" with vpunch
                bo "I think we both know that's not true... *smirk*"
                jump sarada_sparring_jumpfromfail 
            
    jump action_taken